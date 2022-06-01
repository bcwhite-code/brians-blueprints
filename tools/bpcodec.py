# Factorio blueprints codec.
# Copyright (c) 2022 by Brian White <bcwhite@pobox.com>


import base64
import json
import zlib


def Pretty(data):
    return json.dumps(data, sort_keys=True, indent=2)


def Decode(text):
    assert (len(text) > 1), 'Empty blueprint string.'
    version = text[0]
    assert (version == '0'), 'Only blueprint version 0 (zero) is supported.'
    binary = base64.b64decode(text[1:])
    data = zlib.decompress(binary)
    return json.loads(data)


def Encode(output):
    data = json.dumps(output)
    binary = zlib.compress(data.encode(), level=9)
    text = base64.b64encode(binary).decode()
    return '0' + text
