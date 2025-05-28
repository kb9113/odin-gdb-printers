python
import sys
sys.path.insert(0, '/home/calebmanning/Documents/change_note/main/_python_debug_scritps')
from slice_gdb import build_pretty_printer
gdb.printing.register_pretty_printer(gdb.current_objfile(), build_pretty_printer())
end
