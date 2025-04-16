from typing import Dict, Any

import orjson


def json_loads(s: str) -> Dict:
    return orjson.loads(s)


def json_dumps(data: Any) -> str:
    return orjson.dumps(
        data,
        option=orjson.OPT_INDENT_2 | orjson.OPT_SORT_KEYS | orjson.OPT_NON_STR_KEYS
    ).decode("utf-8")


def json_loads_from_file(path: str) -> Dict:
    with open(path, "r", encoding="utf-8") as f:
        return json_loads(f.read())


def json_dumps_to_file(data: Any, path: str) -> None:
    with open(path, "w", encoding="utf-8") as f:
        f.write(json_dumps(data))
