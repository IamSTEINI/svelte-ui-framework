import sys

def escape(s):
    return s.replace('\r\n', '\n').replace('\r', '\n').replace('\\', '\\\\').replace('\t', '\\t').replace('\n', '\\n').replace('"', '\\"')

if sys.stdin.isatty():
    print('paste text then CTRL Z TO GET TEXT', file=sys.stderr)
txt = sys.stdin.read()
print(escape(txt))