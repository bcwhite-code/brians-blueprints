#!/usr/bin/env python3
# Factorio blueprints codec.
# Written by Brian White <bcwhite@pobox.com>
# This file is covered by the CC0 license.


import base64
import json
import zlib


def Pretty(data):
    return json.dumps(data, sort_keys=True, indent=2, ensure_ascii=False)


def Decode(text):
    assert (len(text) > 1), 'Empty blueprint string.'
    version = text[0]
    assert (version == '0'), 'Only blueprint version 0 (zero) is supported.'
    binary = base64.b64decode(text[1:])
    data = zlib.decompress(binary)
    return json.loads(data)


def Encode(output):
    data = json.dumps(output, ensure_ascii=False)
    binary = zlib.compress(data.encode(), level=9)
    text = base64.b64encode(binary).decode()
    return f'0{text}\n'
