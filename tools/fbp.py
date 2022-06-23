#! /usr/bin/python3
# Written by Brian White <bcwhite@pobox.com>
# This file is covered by the CC0 license.


import argparse
import json
import os
import re
import sys

import bpcodec


ARGS = None

ACTIVE_INDEX = 'active_index'
BLUEPRINT = 'blueprint'
BLUEPRINTS = 'blueprints'
BLUEPRINT_BOOK = 'blueprint_book'
DECONSTRUCTION_PLANNER = 'deconstruction_planner'
UPGRADE_PLANNER = 'upgrade_planner'

ITEM = 'item'
META = '.metadata'


def SafeName(name):
    return re.sub('[^A-Za-z0-9]+', '', name)


def SplitBlueprints(dir, blueprints):
    indices = {}
    for bp in blueprints:
        metadata = {}
        metafile = None
        def WriteMetadata():
            nonlocal metadata, metafile
            if metadata:
                assert metafile, f'Have metadata but no metafile ({metadata}).'
                file = open(metafile, 'w')
                file.write(bpcodec.Pretty(metadata))
                file.close()
            metadata = {}
            metafile = None

        for type, obj in bp.items():
            #print("-", type, obj)
            if type == BLUEPRINT_BOOK:
                assert 'label' in obj, f'Object of type "{type}" has no label.'
                print('Book:', obj['label'])
                WriteMetadata()
                subdir = SafeName(obj['label'])
                newdir = dir + '/' + subdir
                metafile = newdir + META
                SplitBook(newdir, obj)
            elif type == BLUEPRINT or type == DECONSTRUCTION_PLANNER or type == UPGRADE_PLANNER:
                assert 'label' in obj, f'Object of type "{type}" has no label.'
                print(f"- {type}: {obj['label']}")
                WriteMetadata()
                name = SafeName(obj['label'])
                path = dir + '/' + name
                metafile = path + META
                file = open(path + '.json', 'w')
                file.write(bpcodec.Pretty({ type: obj }))
                file.close()
            else:
                metadata[type] = obj
        WriteMetadata()


def SplitBook(dir, book):
    try:
        os.mkdir(dir, mode=0o755)
    except FileExistsError:
        pass

    metadata = {}
    for type, obj in book.items():
        #print(type, obj)
        if type == BLUEPRINTS:
            SplitBlueprints(dir, obj)
        else:
            metadata[type] = obj

    file = open(dir + '/' + META, 'w')
    file.write(bpcodec.Pretty(metadata))
    file.close()
    


def Split(outdir, infile):
    assert outdir, '"split" requires an "outdir"'
    assert infile, '"split" requires an "infile"'
    file = open(infile, 'r')
    text = file.read(1<<30)  # 1GiB max
    data = bpcodec.Decode(text)
    #print(bpcodec.Pretty(data))
    assert len(data) == 1, 'infile should have only one top-level object'
    for type, book in data.items():
        assert type == 'blueprint_book', f'Blueprint is not a book (was {type}).'
        SplitBook(outdir, book)


def BuildBook(dir):
    blueprints = []
    #print('dir:', dir)
    for entry in os.listdir(dir):
        path = dir + '/' + entry
        if entry[0] == '.':
            continue
        if entry.endswith(META):
            continue

        if os.path.isfile(path):
            file = open(path, 'r')
            data = json.load(file)
            file.close()
            print(f"- blueprint: {entry}")
            blueprints.append(data)
        elif os.path.isdir(path):
            print(f"Book: {entry}")
            data = BuildBook(path)
            blueprints.append(data)
        else:
            assert False, f'Somehow "{path}" is neither a file nor directory.'

        path = os.path.splitext(path)[0] + META
        file = open(path, 'r')
        meta = json.load(file)
        file.close()
        for key, val in meta.items():
            blueprints[-1][key] = val

    book = { BLUEPRINTS: blueprints }
    file = open(dir + '/' + META, 'r')
    data = file.read()
    file.close()
    meta = json.loads(data)
    #print('meta:', meta)
    for key, val in meta.items():
        #print('book-meta:', key, val)
        book[key] = val
    return { BLUEPRINT_BOOK: book }

    
def Build(outfile, indir):
    assert outfile, '"build" requires an "outfile"'
    assert indir, '"build" requires an "indir"'
    book = BuildBook(indir)
    #print('top-book:', json.dumps(book))
    file = open(outfile, 'w')
    file.write(bpcodec.Encode(book))
    file.close()


def Unpack(outfile, infile):
    assert outfile, '"unpack" requires an "outfile"'
    assert infile, '"unpack" requires an "infile"'
    file = open(infile, 'r')
    text = file.read(10<<20)  # 10MiB max
    file.close()
    bp = bpcodec.Decode(text)
    file = open(outfile, 'w')
    file.write(bpcodec.Pretty(bp))
    file.close()


def Pack(outfile, infile):
    assert outfile, '"pack" requires an "outfile"'
    assert infile, '"pack" requires an "infile"'
    file = open(infile, 'r')
    data = json.load(file)
    file.close()
    text = bpcodec.Encode(data)
    file = open(outfile, 'w')
    file.write(text)
    file.close()


def main():
    if ARGS.action == 'split':
        Split(ARGS.outdir, ARGS.infile)
    if ARGS.action == 'build':
        Build(ARGS.outfile, ARGS.indir)
    if ARGS.action == 'unpack':
        Unpack(ARGS.outfile, ARGS.infile)
    if ARGS.action == 'pack':
        Pack(ARGS.outfile, ARGS.infile)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Factorio Blueprint Tools')
    parser.add_argument('action', choices=['build', 'split', 'unpack', 'pack'], help='what action to perform')
    parser.add_argument('--indir', help='directory of individual blueprints to read')
    parser.add_argument('--outdir', help='directory of individual blueprints to write')
    parser.add_argument('--infile', help='blueprint file to read')
    parser.add_argument('--outfile', help='blueprint file to write')
    ARGS = parser.parse_args(sys.argv[1:])
    main()
