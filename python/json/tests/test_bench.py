import json
import timeit

import pytest

import hyperjson
import orjson
import simdjson
import ujson


def test_speed(json_example):
    """Compare every example json file between simdjson and the built-in JSON module.

    Ideally, every file will parse signficantly faster under simdjson.

    .. note::

        This is very trivial test, and the results of a single run over such a
        low number should not be used as any sort of benchmark. This is a
        simple test just for debugging purposes.
    """
    file_name, file = json_example

    hyperjson_time = timeit.timeit(
        'json.loads(s)',
        globals={
            'json': hyperjson,
            's': file
        },
        number=100
    )

    orjson_time = timeit.timeit(
        'json.loads(s)',
        globals={
            'json': orjson,
            's': file
        },
        number=100
    )

    simdjson_time = timeit.timeit(
        'json.loads(s)',
        globals={
            'json': simdjson,
            's': file
        },
        number=100
    )

    ujson_time = timeit.timeit(
        'json.loads(s)',
        globals={
            'json': ujson,
            's': file
        },
        number=100
    )

    json_time = timeit.timeit(
        'json.loads(s)',
        globals={
            'json': json,
            's': file
        },
        number=100
    )

    assert False, (
        '\nhyperjson:  {}\norjson:     {}\nsimdjson:   {}\nujson:      {}\njson:       {}'
    ).format(
        hyperjson_time,
        orjson_time,
        simdjson_time,
        ujson_time,
        json_time,
    )
