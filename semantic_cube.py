types = {
    'int': 'int',
    'float': 'float',
    'char': 'char',
    'bool': 'bool',
}

operations = {
    '+': 0, 
    '-': 1, 
    '*': 2, 
    '/': 3, 
    '&&': 4, 
    '||': 5, 
    '==': 6, 
    '!=': 7, 
    '>': 8,
    '<': 9,
    '>=': 10, 
    '<=': 11,
    '!': 12,
    '=': 13,
}

class SemanticCube():
    

    semantic_cube = {
        'int': {
            'int': {
                '+': types['int'],
                '-': types['int'],
                '*': types['int'],
                '/': types['int'],
                '&&': types['bool'],
                '||': types['bool'],
                '==': types['bool'],
                '!=': types['bool'],
                '>': types['bool'],
                '<': types['bool'],
                '>=': types['bool'],
                '<=': types['bool'],
                '=': types['int'],
            },
            'float': {
                '+': types['float'],
                '-': types['float'],
                '*': types['float'],
                '/': types['float'],
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': types['bool'],
                '<': types['bool'],
                '>=': types['bool'],
                '<=': types['bool'],
                '=': 'ERROR',
            },
            'char': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
                '=': 'ERROR',
            },
            'bool': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
                '=': 'ERROR',
            }
        },
        'float': {
            'int': {
                '+': types['float'],
                '-': types['float'],
                '*': types['float'],
                '/': types['float'],
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': types['bool'],
                '<': types['bool'],
                '>=': types['bool'],
                '<=': types['bool'],
                '=': 'ERROR',
            },
            'float': {
                '+': types['float'],
                '-': types['float'],
                '*': types['float'],
                '/': types['float'],
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': types['bool'],
                '!=': types['bool'],
                '>': types['bool'],
                '<': types['bool'],
                '>=': types['bool'],
                '<=': types['bool'],
                '=': types['float']
            },
            'char': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
                '=': 'ERROR',
            },
            'bool': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
                '=': 'ERROR',
            }
        },
        'char': {
            'int': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
                '=': 'ERROR',
            },
            'float': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
                '=': 'ERROR',
            },
            'char': {
                '+':'ERROR',
                '-':'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': types['bool'],
                '!=': types['bool'],
                '>': types['bool'],
                '<': types['bool'],
                '>=': types['bool'],
                '<=': types['bool'],
                '=': types['char'],
            },
            'bool': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
                '=': 'ERROR',
            }
        },
        'bool': {
            'int': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
                '=': 'ERROR',
            },
            'float': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
                '=': 'ERROR',
            },
            'char': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': 'ERROR',
                '||': 'ERROR',
                '==': 'ERROR',
                '!=': 'ERROR',
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
                '=': 'ERROR',
            },
            'bool': {
                '+': 'ERROR',
                '-': 'ERROR',
                '*': 'ERROR',
                '/': 'ERROR',
                '&&': types['bool'],
                '||': types['bool'],
                '==': types['bool'],
                '!=': types['bool'],
                '>': 'ERROR',
                '<': 'ERROR',
                '>=': 'ERROR',
                '<=': 'ERROR',
                '=': types['bool'],
            }
        }
    }
   
    def match_types(self, type1: str, type2: str, operator: str) -> str:
        if type1 not in types or type2 not in types:
            raise Exception('Unknown type used')
        
        if operator not in operations:
            raise Exception('Unknown operator used')

        sem_type1 = types[type1]
        sem_type2 = types[type2]
        result = self.semantic_cube[sem_type1][sem_type2][operator]
        return result