# Token dictionary with IDs
token_list = {
    "keywords":{
        'array': 'ARRAY',
        'begin': 'PBEGIN',
        'call': 'CALL',
        'char': 'CHAR',
        'ChNode': 5,
        'constants': 'CONSTANTS',
        'declarations': 'DECLARATIONS',
        'define': 'DEFINE',
        'display': 'DISPLAY',
        'do': 'DO',
        'double': 'DOUBLE',
        'end': 12,
        'endfor': 'ENDFOR',
        'endfun': 'ENDFUN',
        'endwhile': 'ENDWHILE',
        'exit': 'MEXIT',
        'float': 'FLOAT',
        'for': 'FOR',
        'forward': 'FORWARD',
        'function': 'FUNCTION',
        'head': 21,
        'implementations': 'IMPLEMENTATIONS',
        'import': 'IMPORT',
        'input': 'INPUT',
        'integer': 'INTEGER',
        'is': 'IS',
        'last': 27,
        'loop': 28,
        'main': "MAIN",
        'NULL': 30,
        'num': 31,
        'of': 'OF',
        'parameters': 'PARAMETERS',
        'pointer': 'POINTER',
        'return': 'RETURN',
        'reverse': 36,
        'set': 'SET',
        'setup': 38,
        'structures': 'STRUCT',
        'symbol': 'SYMBOL',
        'to': 'TO',
        'type': 'TYPE',
        'using': 'USING',
        'variables': 'VARIABLES',
        'while': 'WHILE',
       
    },

    "operators":{
        '+': 'ADD',
        '-': 'SUBTRACT',
        '*': 'STAR',
        '/': 'DIVOP',
        '^': 405,
        '>': 'GREATERT',
        '<': 'LESST',
        '=': 'EQUALS',
        '(':409,
        ')':410,
        '.':'DOT',
        '**':412,
        '^=*':413,
        '>=**':'GREATERT OR EQUAL',
        '=>':'GREATERT OR EQUAL',
        '>=':'GREATERT OR EQUAL',
        '<=**':'LESST OR EQUAL',
        '=<':'LESST OR EQUAL',
        '<=':'LESST OR EQUAL',
        '<>':416,
        '><':417,
        '||': 418,
        '&':'AND',
        '|':'OR',
        '^*':'NOT',
        '-*':422
    },
    
    "special symbols":{
        ',': 'COMMA',
        ':': 'COLON'
    }
}

class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value
    
    def get_data(self):
        return [self.type, self.value]