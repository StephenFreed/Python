from typing import List, Dict, Union


# basic function hinting
def greeting(name: str) -> str:
    return "Hello, {}".format(name)


print(greeting("Stephen"))


# must import from typing to type hint List
def greeting_list(names: List[str]) -> str:
    return "Hello, {}".format(", ".join(names))


print(greeting_list(["jane", "john", "judy"]))


# must import from typing to type hint Dict
def greeting_dict(names: Dict[str, int]) -> str:
    keys = names.keys()
    return "Hello, {}".format(", ".join(keys))


print(greeting_dict({"jane": 10, "john": 11, "judy": 12}))


# union gives optional typing
def greeting_union(name: Union[str, int]) -> str:
    return "Hello, {}".format(name)


print(greeting_union("Stephen"))
print(greeting_union(36))
