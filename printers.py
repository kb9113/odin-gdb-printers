import gdb.printing
'''
The below is a useful resource for understanding how this stuff works
https://sourceware.org/gdb/current/onlinedocs/gdb.html/Pretty-Printing-API.html#Pretty-Printing-API
'''

class Slice:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        try:
            data = self.val['data']
            length = int(self.val['len'])
            ans = "["
            for i in range(length):
                if i != 0:
                    ans += ", "
                visualized_default = gdb.default_visualizer((data + i).dereference())
                if visualized_default == None:
                    ans += str((data + i).dereference())
                else:
                    ans += visualized_default.to_string()
            ans += "]"
            return ans
        except Exception as e:
            return f"<invalid value: {e}>"

    def children(self):
        try:
            data = self.val['data']
            length = int(self.val['len'])
            for i in range(length):
                yield f'[{i}]', (data + i).dereference()
        except Exception as e:
            yield 'error', f'<{e}>'

    def display_hint(self):
        return 'array'

class String:
    def __init__(self, val):
        self.val = val

    def to_string(self):
        try:
            data = self.val['data']
            length = int(self.val['len'])
            return "\"" + data.string(length=length) + "\""
        except Exception as e:
            return f"<invalid value: {e}>"

    def display_hint(self):
        return 'array'

def build_pretty_printer():
    pp = gdb.printing.RegexpCollectionPrettyPrinter("my_project")
    pp.add_printer('slice', '^\\[\\].+$', Slice)
    pp.add_printer('string', 'string', String)
    return pp
