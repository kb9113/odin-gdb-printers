python
import sys
sys.path.insert(0, '<path to this repo on your disk>')
from printers import build_pretty_printer
gdb.printing.register_pretty_printer(gdb.current_objfile(), build_pretty_printer())
end
