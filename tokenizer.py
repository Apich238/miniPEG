class aTokenizer:
    def __init__(self, definitions):
        self.token_rules = definitions.copy()

    def __call__(self, line: str):
        raise NotImplementedError()


import re
from collections import namedtuple

Token = namedtuple('Token', ['type', 'value', 'pos'])


class RegExpTokenizer(aTokenizer):
    def __init__(self, definitions):
        super().__init__(definitions)
        # tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in self.terms_spec)
        self.tok_regex = '|'.join('(?P<{}>{})'.format(k, self.token_rules[k]) for k in self.token_rules)
        self.tok_regex += '|(?P<MISMATCH>.)'

    def __call__(self, line: str):
        '''
            Токенизация
            :param line: строка
            :return: генератор токенов
            '''
        line_start = 0
        for mo in re.finditer(self.tok_regex, line):
            kind = mo.lastgroup
            value = mo.group()
            column = mo.start() - line_start

            if kind == 'MISMATCH':
                raise RuntimeError('value {} unexpected at {}'.format(value, line_start))

            yield Token(kind, value, column)

# if __name__ == '__main__':
#     t = RegExpTokenizer({
#         'num': r'[0-9]+(\.[0-9]*)?',
#         'opbracket': r'\(',
#         'clbracket': r'\)',
#         'plus': r'\+',
#         'minus': r'\-',
#         'prod': r'\*',
#         'div': r'\/',
#         'ignore': r' +'
#     })
#     ls = ['1', '0.', '0.0010', '-1', '1+2', '1*2', '1*-2', '-1*2', '1-2*3',
#           '1*2-3', '1-2/3*5+4', '1-2/(3+4)/5',
#           '345 - -56 + (1+2)', '1*2*3/(4+5)*6+-7-2',
#           '(876-787+(765-234)*2736/23/123)/23*76*5-1']
#     for l in ls:
#         ts=t(l)
#         print('=================================')
#         print(l)
#         for tok in ts:
#             print(tok)
