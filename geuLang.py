import sys


class GeuLang:
    def __init__(self):
        self.data = [0]*256
        self.end = False
        self.goto = 0

    def toNumber(self, codesome):
        if '흐' in codesome:
            tokens = codesome.split(' ')
            result = 1
            sign = '*'
            if len(tokens) == 1:
                val = self.data[tokens[0].count('흐')]
                val += (tokens[0].count('.') - tokens[0].count('~'))
                result *= val

            else:
                for token in tokens:
                    if '흐' in token:
                        val = self.data[token.count('흐')]
                        if sign == '+':
                            result += val
                        elif sign == '-':
                            result -= val
                        else:
                            result *= val

                        if token[-1] == '.':
                            sign = '+'
                        elif token[-1] == '~':
                            sign = '-'
                        else:
                            sign = '*'

                    else:
                        val = token.count('.') - token.count('~')
                        result *= val
                        sign = '*'

        else:
            tokens = codesome.split(' ')
            result = 1

            for token in tokens:
                temp = token.count('.') - token.count('~')
                result *= temp

            # codesome = codesome.replace('.', '')
            # codesome = codesome.replace('~', '')
        # if not codesome.empty():
        # raise SyntaxError('이이이이ㅣ잉 정수우우우!!')

        return result

    def getType(self, code):
        if not code:
            return 'BLANK'

        if ';' not in code:
            raise SyntaxError(f'세에미콜로오온!!')

        if code.startswith('그') and '?' in code:
            return 'INPUT'
        if code.startswith('그'):
            return 'DEF'
        if code.startswith('흐'):
            return 'CALL'
        if code.startswith('행복한소리'):
            return 'IF'
        if code.startswith('읗'):
            return 'PRINT'
        if code.startswith('세미콜론'):
            return 'GOTO'
        if code.startswith('두루미합체'):
            return 'END'

    def compileLine(self, code):
        TYPE = self.getType(code)
        if TYPE == 'BLANK':
            return

        elif TYPE == 'DEF':
            var = code.count('그')
            self.data[var] = self.toNumber(code)

        elif TYPE == 'INPUT':
            var = code.count('그')
            self.data[var] = int(input())

        elif TYPE == 'PRINT':
            val = self.toNumber(code)
            print(val)

        elif TYPE == 'IF':
            var1, var2, cmd = code.split('?')
            val1 = self.toNumber(var1)
            val2 = self.toNumber(var2)
            if val1 == val2:
                self.compileLine(cmd)
        elif TYPE == 'GOTO':
            self.goto = self.toNumber(code)-1

        elif TYPE == 'END':
            self.end = True

    def compile(self, codes):
        # for lineNum in range(len(codes[:-1])):
        lineNum = 0
        while lineNum != len(codes)-1:
            self.goto = lineNum
            self.compileLine(codes[lineNum])
            lineNum = self.goto if lineNum != self.goto else lineNum+1
        if self.getType(codes[-1]) == 'END':
            return
        else:
            raise SyntaxError('이이이ㅣ이잉! 두루미 합체에에!')

    def compileFile(self, path):
        with open(path, encoding='utf-8') as f:
            codes = f.read().splitlines()
            self.compile(codes)


if __name__ == '__main__':
    compiler = GeuLang()
    compiler.compileFile(sys.argv[1])
