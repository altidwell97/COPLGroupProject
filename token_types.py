# Token dictionary with IDs
token_list = {
    "keywords":{
        'array': 1,
        'begin': 2,
        'call': 3,
        'char': 4,
        'ChNode': 5,
        'constants': 6,
        'declarations': 7,
        'define': 8,
        'display': 9,
        'do': 10,
        'double': 11,
        'end': 12,
        'endfor': 13,
        'endfun': 14,
        'endwhile': 15,
        'exit': 16,
        'float': 17,
        'for': 18,
        'forward': 19,
        'function': 20,
        'head': 21,
        'implementations': 22,
        'import': 23,
        'input': 24,
        'integer': 25,
        'is': 26,
        'last': 27,
        'loop': 28,
        'main': 29,
        'NULL': 30,
        'num': 31,
        'of': 32,
        'parameters': 33,
        'pointer': 34,
        'return': 35,
        'reverse': 36,
        'set': 37,
        'setup': 38,
        'structures': 39,
        'symbol': 40,
        'to': 41,
        'type': 42,
        'using': 43,
        'variables': 44,
        'while': 45,
       
    },

    "operators":{
        '+': 401,
        '-': 402,
        '*': 403,
        '/': 404,
        '^': 405,
        '>': 406,
        '<': 407,
        '=': 408,
        '(':409,
        ')':410,
        '.':411 #TODO Need to add some way to signify operator vs special symbol
    },

    "special symbols":{
        ',': 801,
        '.': 802,
        '"': 803,
        '\'': 804,
    }
}

class Token:
    def __init__(self,type,id,value):
        self.type = type
        self.id = id
        self.value = value
    
    def get_data(self):
        return [self.type, self.id, self.value]
