
from typing import Dict
from functools import reduce


class ParseException(Exception):

    def __init__(self, msg: str, kv_pair: Dict, *args: object) -> None:
        super().__init__(*args)
        self.msg = msg or ""
        self.kv_pair = kv_pair or {}

    def __str__(self) -> str:
        kv_log = ""
        for k, v in self.kv_pair.items():
            kv_log += f"{k}: {v};\n"
        return super().__str__() + self.msg + "\n" + kv_log