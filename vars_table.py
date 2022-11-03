from typing import Union
from semantic_cube import types
from memory import virtual_memory

# TODO: Grow this data structure as we add more to the variable table
class VarsTableEntry:
    def __init__(self, type: str, address: int) -> None:
        self.type = type
        self.address = address

    def __str__(self) -> str:
        return f'type: {self.type} address: {self.address}'

    def __repr__(self) -> str:
        return f'type: {self.type} address: {self.address}'

    

class VarsTable():
    vars_table = {}
    def __str__(self) -> str:
        return str(self.vars_table)

    def add_entry(self, name: str, type: str) -> None:
        if type not in types:
            raise Exception(f'Unknown type used {type}')
        if name in self.vars_table:
            raise Exception('Redeclaration of identifier is not allowed')
        address = virtual_memory.assign_mem_address(types[type], is_temp=False)
        self.vars_table[name] = VarsTableEntry(types[type], address)

    def lookup_entry(self, name: str) -> tuple[bool, Union[VarsTableEntry, None]]:
        if name not in self.vars_table:
            return (False, None)
        return (True, self.vars_table[name])