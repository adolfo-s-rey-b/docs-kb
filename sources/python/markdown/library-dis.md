### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pickletools.html "pickletools — Tools for pickle developers")
     |
*   [previous](https://docs.python.org/3/library/compileall.html "compileall — Byte-compile Python libraries")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Python Language Services](https://docs.python.org/3/library/language.html)
     »
*   [`dis` — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html)
    
*    
    
    |
*   Theme Auto Light Dark |

`dis` — Disassembler for Python bytecode[¶](https://docs.python.org/3/library/dis.html#module-dis "Link to this heading")

==========================================================================================================================

**Source code:** [Lib/dis.py](https://github.com/python/cpython/tree/3.15/Lib/dis.py)

* * *

The `dis` module supports the analysis of CPython [bytecode](https://docs.python.org/3/glossary.html#term-bytecode)
 by disassembling it. The CPython bytecode which this module takes as an input is defined in the file `Include/opcode.h` and used by the compiler and the interpreter.

**CPython implementation detail:** Bytecode is an implementation detail of the CPython interpreter. No guarantees are made that bytecode will not be added, removed, or changed between versions of Python. Use of this module should not be considered to work across Python VMs or Python releases.

Changed in version 3.6: Use 2 bytes for each instruction. Previously the number of bytes varied by instruction.

Changed in version 3.10: The argument of jump, exception handling and loop instructions is now the instruction offset rather than the byte offset.

Changed in version 3.11: Some instructions are accompanied by one or more inline cache entries, which take the form of [`CACHE`](https://docs.python.org/3/library/dis.html#opcode-CACHE)
 instructions. These instructions are hidden by default, but can be shown by passing `show_caches=True` to any `dis` utility. Furthermore, the interpreter now adapts the bytecode to specialize it for different runtime conditions. The adaptive bytecode can be shown by passing `adaptive=True`.

Changed in version 3.12: The argument of a jump is the offset of the target instruction relative to the instruction that appears immediately after the jump instruction’s [`CACHE`](https://docs.python.org/3/library/dis.html#opcode-CACHE)
 entries.

As a consequence, the presence of the [`CACHE`](https://docs.python.org/3/library/dis.html#opcode-CACHE)
 instructions is transparent for forward jumps but needs to be taken into account when reasoning about backward jumps.

Changed in version 3.13: The output shows logical labels rather than instruction offsets for jump targets and exception handlers. The `-O` command line option and the `show_offsets` argument were added.

Changed in version 3.14: The [`-P`](https://docs.python.org/3/library/dis.html#cmdoption-dis-P)
 command-line option and the `show_positions` argument were added.

The [`-S`](https://docs.python.org/3/library/dis.html#cmdoption-dis-S)
 command-line option is added.

Example: Given the function `myfunc()`:

Copy

def myfunc(alist):
    return len(alist)

the following command can be used to display the disassembly of `myfunc()`:

Copy

\>>> dis.dis(myfunc)
  2           RESUME                   0

  3           LOAD\_GLOBAL              1 (len + NULL)
              LOAD\_FAST\_BORROW         0 (alist)
              CALL                     1
              RETURN\_VALUE

(The “2” is a line number).

Command-line interface[¶](https://docs.python.org/3/library/dis.html#command-line-interface "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

The `dis` module can be invoked as a script from the command line:

Copy

python \-m dis \[\-h\] \[\-C\] \[\-O\] \[\-P\] \[\-S\] \[infile\]

The following options are accepted:

\-h, \--help[¶](https://docs.python.org/3/library/dis.html#cmdoption-dis-h "Link to this definition")

Display usage and exit.

\-C, \--show-caches[¶](https://docs.python.org/3/library/dis.html#cmdoption-dis-C "Link to this definition")

Show inline caches.

Added in version 3.13.

\-O, \--show-offsets[¶](https://docs.python.org/3/library/dis.html#cmdoption-dis-O "Link to this definition")

Show offsets of instructions.

Added in version 3.13.

\-P, \--show-positions[¶](https://docs.python.org/3/library/dis.html#cmdoption-dis-P "Link to this definition")

Show positions of instructions in the source code.

Added in version 3.14.

\-S, \--specialized[¶](https://docs.python.org/3/library/dis.html#cmdoption-dis-S "Link to this definition")

Show specialized bytecode.

Added in version 3.14.

If `infile` is specified, its disassembled code will be written to stdout. Otherwise, disassembly is performed on compiled source code received from stdin.

Bytecode analysis[¶](https://docs.python.org/3/library/dis.html#bytecode-analysis "Link to this heading")

----------------------------------------------------------------------------------------------------------

Added in version 3.4.

The bytecode analysis API allows pieces of Python code to be wrapped in a [`Bytecode`](https://docs.python.org/3/library/dis.html#dis.Bytecode "dis.Bytecode")
 object that provides easy access to details of the compiled code.

class dis.Bytecode(_x_, _\*_, _first\_line\=None_, _current\_offset\=None_, _show\_caches\=False_, _adaptive\=False_, _show\_offsets\=False_, _show\_positions\=False_)[¶](https://docs.python.org/3/library/dis.html#dis.Bytecode "Link to this definition")

Analyse the bytecode corresponding to a function, generator, asynchronous generator, coroutine, method, string of source code, or a code object (as returned by [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
).

This is a convenience wrapper around many of the functions listed below, most notably [`get_instructions()`](https://docs.python.org/3/library/dis.html#dis.get_instructions "dis.get_instructions")
, as iterating over a `Bytecode` instance yields the bytecode operations as [`Instruction`](https://docs.python.org/3/library/dis.html#dis.Instruction "dis.Instruction")
 instances.

If _first\_line_ is not `None`, it indicates the line number that should be reported for the first source line in the disassembled code. Otherwise, the source line information (if any) is taken directly from the disassembled code object.

If _current\_offset_ is not `None`, it refers to an instruction offset in the disassembled code. Setting this means [`dis()`](https://docs.python.org/3/library/dis.html#dis.Bytecode.dis "dis.Bytecode.dis")
 will display a “current instruction” marker against the specified opcode.

If _show\_caches_ is `True`, [`dis()`](https://docs.python.org/3/library/dis.html#dis.Bytecode.dis "dis.Bytecode.dis")
 will display inline cache entries used by the interpreter to specialize the bytecode.

If _adaptive_ is `True`, [`dis()`](https://docs.python.org/3/library/dis.html#dis.Bytecode.dis "dis.Bytecode.dis")
 will display specialized bytecode that may be different from the original bytecode.

If _show\_offsets_ is `True`, [`dis()`](https://docs.python.org/3/library/dis.html#dis.Bytecode.dis "dis.Bytecode.dis")
 will include instruction offsets in the output.

If _show\_positions_ is `True`, [`dis()`](https://docs.python.org/3/library/dis.html#dis.Bytecode.dis "dis.Bytecode.dis")
 will include instruction source code positions in the output.

classmethod from\_traceback(_tb_, _\*_, _show\_caches\=False_)[¶](https://docs.python.org/3/library/dis.html#dis.Bytecode.from_traceback "Link to this definition")

Construct a `Bytecode` instance from the given traceback, setting _current\_offset_ to the instruction responsible for the exception.

codeobj[¶](https://docs.python.org/3/library/dis.html#dis.Bytecode.codeobj "Link to this definition")

The compiled code object.

first\_line[¶](https://docs.python.org/3/library/dis.html#dis.Bytecode.first_line "Link to this definition")

The first source line of the code object (if available)

dis()[¶](https://docs.python.org/3/library/dis.html#dis.Bytecode.dis "Link to this definition")

Return a formatted view of the bytecode operations (the same as printed by [`dis.dis()`](https://docs.python.org/3/library/dis.html#dis.dis "dis.dis")
, but returned as a multi-line string).

info()[¶](https://docs.python.org/3/library/dis.html#dis.Bytecode.info "Link to this definition")

Return a formatted multi-line string with detailed information about the code object, like [`code_info()`](https://docs.python.org/3/library/dis.html#dis.code_info "dis.code_info")
.

Changed in version 3.7: This can now handle coroutine and asynchronous generator objects.

Changed in version 3.11: Added the _show\_caches_ and _adaptive_ parameters.

Changed in version 3.13: Added the _show\_offsets_ parameter

Changed in version 3.14: Added the _show\_positions_ parameter.

Example:

Copy

\>>> bytecode \= dis.Bytecode(myfunc)
\>>> for instr in bytecode:
...     print(instr.opname)
...
RESUME
LOAD\_GLOBAL
LOAD\_FAST\_BORROW
CALL
RETURN\_VALUE

Analysis functions[¶](https://docs.python.org/3/library/dis.html#analysis-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------

The `dis` module also defines the following analysis functions that convert the input directly to the desired output. They can be useful if only a single operation is being performed, so the intermediate analysis object isn’t useful:

dis.code\_info(_x_)[¶](https://docs.python.org/3/library/dis.html#dis.code_info "Link to this definition")

Return a formatted multi-line string with detailed code object information for the supplied function, generator, asynchronous generator, coroutine, method, source code string or code object.

Note that the exact contents of code info strings are highly implementation dependent and they may change arbitrarily across Python VMs or Python releases.

Added in version 3.2.

Changed in version 3.7: This can now handle coroutine and asynchronous generator objects.

dis.show\_code(_x_, _\*_, _file\=None_)[¶](https://docs.python.org/3/library/dis.html#dis.show_code "Link to this definition")

Print detailed code object information for the supplied function, method, source code string or code object to _file_ (or `sys.stdout` if _file_ is not specified).

This is a convenient shorthand for `print(code_info(x), file=file)`, intended for interactive exploration at the interpreter prompt.

Added in version 3.2.

Changed in version 3.4: Added _file_ parameter.

dis.dis(_x\=None_, _\*_, _file\=None_, _depth\=None_, _show\_caches\=False_, _adaptive\=False_, _show\_offsets\=False_, _show\_positions\=False_)[¶](https://docs.python.org/3/library/dis.html#dis.dis "Link to this definition")

Disassemble the _x_ object. _x_ can denote either a module, a class, a method, a function, a generator, an asynchronous generator, a coroutine, a code object, a string of source code or a byte sequence of raw bytecode. For a module, it disassembles all functions. For a class, it disassembles all methods (including class and static methods). For a code object or sequence of raw bytecode, it prints one line per bytecode instruction. It also recursively disassembles nested code objects. These can include generator expressions, nested functions, the bodies of nested classes, and the code objects used for [annotation scopes](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
. Strings are first compiled to code objects with the [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
 built-in function before being disassembled. If no object is provided, this function disassembles the last traceback.

The disassembly is written as text to the supplied _file_ argument if provided and to `sys.stdout` otherwise.

The maximal depth of recursion is limited by _depth_ unless it is `None`. `depth=0` means no recursion.

If _show\_caches_ is `True`, this function will display inline cache entries used by the interpreter to specialize the bytecode.

If _adaptive_ is `True`, this function will display specialized bytecode that may be different from the original bytecode.

Changed in version 3.4: Added _file_ parameter.

Changed in version 3.7: Implemented recursive disassembling and added _depth_ parameter.

Changed in version 3.7: This can now handle coroutine and asynchronous generator objects.

Changed in version 3.11: Added the _show\_caches_ and _adaptive_ parameters.

Changed in version 3.13: Added the _show\_offsets_ parameter.

Changed in version 3.14: Added the _show\_positions_ parameter.

dis.distb(_tb\=None_, _\*_, _file\=None_, _show\_caches\=False_, _adaptive\=False_, _show\_offset\=False_, _show\_positions\=False_)[¶](https://docs.python.org/3/library/dis.html#dis.distb "Link to this definition")

Disassemble the top-of-stack function of a traceback, using the last traceback if none was passed. The instruction causing the exception is indicated.

The disassembly is written as text to the supplied _file_ argument if provided and to `sys.stdout` otherwise.

Changed in version 3.4: Added _file_ parameter.

Changed in version 3.11: Added the _show\_caches_ and _adaptive_ parameters.

Changed in version 3.13: Added the _show\_offsets_ parameter.

Changed in version 3.14: Added the _show\_positions_ parameter.

dis.disassemble(_code_, _lasti\=\-1_, _\*_, _file\=None_, _show\_caches\=False_, _adaptive\=False_, _show\_offsets\=False_, _show\_positions\=False_)[¶](https://docs.python.org/3/library/dis.html#dis.disassemble "Link to this definition")

dis.disco(_code_, _lasti\=\-1_, _\*_, _file\=None_, _show\_caches\=False_, _adaptive\=False_, _show\_offsets\=False_, _show\_positions\=False_)[¶](https://docs.python.org/3/library/dis.html#dis.disco "Link to this definition")

Disassemble a code object, indicating the last instruction if _lasti_ was provided. The output is divided in the following columns:

1.  the source code location of the instruction. Complete location information is shown if _show\_positions_ is true. Otherwise (the default) only the line number is displayed.
    
2.  the current instruction, indicated as `-->`,
    
3.  a labelled instruction, indicated with `>>`,
    
4.  the address of the instruction,
    
5.  the operation code name,
    
6.  operation parameters, and
    
7.  interpretation of the parameters in parentheses.
    

The parameter interpretation recognizes local and global variable names, constant values, branch targets, and compare operators.

The disassembly is written as text to the supplied _file_ argument if provided and to `sys.stdout` otherwise.

Changed in version 3.4: Added _file_ parameter.

Changed in version 3.11: Added the _show\_caches_ and _adaptive_ parameters.

Changed in version 3.13: Added the _show\_offsets_ parameter.

Changed in version 3.14: Added the _show\_positions_ parameter.

dis.get\_instructions(_x_, _\*_, _first\_line\=None_, _show\_caches\=False_, _adaptive\=False_)[¶](https://docs.python.org/3/library/dis.html#dis.get_instructions "Link to this definition")

Return an iterator over the instructions in the supplied function, method, source code string or code object.

The iterator generates a series of [`Instruction`](https://docs.python.org/3/library/dis.html#dis.Instruction "dis.Instruction")
 named tuples giving the details of each operation in the supplied code.

If _first\_line_ is not `None`, it indicates the line number that should be reported for the first source line in the disassembled code. Otherwise, the source line information (if any) is taken directly from the disassembled code object.

The _adaptive_ parameter works as it does in [`dis()`](https://docs.python.org/3/library/dis.html#dis.dis "dis.dis")
.

Added in version 3.4.

Changed in version 3.11: Added the _show\_caches_ and _adaptive_ parameters.

Changed in version 3.13: The _show\_caches_ parameter is deprecated and has no effect. The iterator generates the [`Instruction`](https://docs.python.org/3/library/dis.html#dis.Instruction "dis.Instruction")
 instances with the _cache\_info_ field populated (regardless of the value of _show\_caches_) and it no longer generates separate items for the cache entries.

dis.findlinestarts(_code_)[¶](https://docs.python.org/3/library/dis.html#dis.findlinestarts "Link to this definition")

This generator function uses the [`co_lines()`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lines "codeobject.co_lines")
 method of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)
 _code_ to find the offsets which are starts of lines in the source code. They are generated as `(offset, lineno)` pairs.

Changed in version 3.6: Line numbers can be decreasing. Before, they were always increasing.

Changed in version 3.10: The [**PEP 626**](https://peps.python.org/pep-0626/)
 [`co_lines()`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_lines "codeobject.co_lines")
 method is used instead of the [`co_firstlineno`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_firstlineno "codeobject.co_firstlineno")
 and `codeobject.co_lnotab` attributes of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)
.

Changed in version 3.13: Line numbers can be `None` for bytecode that does not map to source lines.

dis.findlabels(_code_)[¶](https://docs.python.org/3/library/dis.html#dis.findlabels "Link to this definition")

Detect all offsets in the raw compiled bytecode string _code_ which are jump targets, and return a list of these offsets.

dis.stack\_effect(_opcode_, _oparg\=None_, _\*_, _jump\=None_)[¶](https://docs.python.org/3/library/dis.html#dis.stack_effect "Link to this definition")

Compute the stack effect of _opcode_ with argument _oparg_.

If the code has a jump target and _jump_ is `True`, `stack_effect()` will return the stack effect of jumping. If _jump_ is `False`, it will return the stack effect of not jumping. And if _jump_ is `None` (default), it will return the maximal stack effect of both cases.

Added in version 3.4.

Changed in version 3.8: Added _jump_ parameter.

Changed in version 3.13: If `oparg` is omitted (or `None`), the stack effect is now returned for `oparg=0`. Previously this was an error for opcodes that use their arg. It is also no longer an error to pass an integer `oparg` when the `opcode` does not use it; the `oparg` in this case is ignored.

Python Bytecode Instructions[¶](https://docs.python.org/3/library/dis.html#python-bytecode-instructions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

The [`get_instructions()`](https://docs.python.org/3/library/dis.html#dis.get_instructions "dis.get_instructions")
 function and [`Bytecode`](https://docs.python.org/3/library/dis.html#dis.Bytecode "dis.Bytecode")
 class provide details of bytecode instructions as [`Instruction`](https://docs.python.org/3/library/dis.html#dis.Instruction "dis.Instruction")
 instances:

class dis.Instruction[¶](https://docs.python.org/3/library/dis.html#dis.Instruction "Link to this definition")

Details for a bytecode operation

opcode[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.opcode "Link to this definition")

numeric code for operation, corresponding to the opcode values listed below and the bytecode values in the [Opcode collections](https://docs.python.org/3/library/dis.html#opcode-collections)
.

opname[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.opname "Link to this definition")

human readable name for operation

baseopcode[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.baseopcode "Link to this definition")

numeric code for the base operation if operation is specialized; otherwise equal to [`opcode`](https://docs.python.org/3/library/dis.html#dis.Instruction.opcode "dis.Instruction.opcode")

baseopname[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.baseopname "Link to this definition")

human readable name for the base operation if operation is specialized; otherwise equal to [`opname`](https://docs.python.org/3/library/dis.html#dis.opname "dis.opname")

arg[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.arg "Link to this definition")

numeric argument to operation (if any), otherwise `None`

oparg[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.oparg "Link to this definition")

alias for [`arg`](https://docs.python.org/3/library/dis.html#dis.Instruction.arg "dis.Instruction.arg")

argval[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.argval "Link to this definition")

resolved arg value (if any), otherwise `None`

argrepr[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.argrepr "Link to this definition")

human readable description of operation argument (if any), otherwise an empty string.

offset[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.offset "Link to this definition")

start index of operation within bytecode sequence

start\_offset[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.start_offset "Link to this definition")

start index of operation within bytecode sequence, including prefixed `EXTENDED_ARG` operations if present; otherwise equal to [`offset`](https://docs.python.org/3/library/dis.html#dis.Instruction.offset "dis.Instruction.offset")

cache\_offset[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.cache_offset "Link to this definition")

start index of the cache entries following the operation

end\_offset[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.end_offset "Link to this definition")

end index of the cache entries following the operation

starts\_line[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.starts_line "Link to this definition")

`True` if this opcode starts a source line, otherwise `False`

line\_number[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.line_number "Link to this definition")

source line number associated with this opcode (if any), otherwise `None`

is\_jump\_target[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.is_jump_target "Link to this definition")

`True` if other code jumps to here, otherwise `False`

jump\_target[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.jump_target "Link to this definition")

bytecode index of the jump target if this is a jump operation, otherwise `None`

positions[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.positions "Link to this definition")

[`dis.Positions`](https://docs.python.org/3/library/dis.html#dis.Positions "dis.Positions")
 object holding the start and end locations that are covered by this instruction.

cache\_info[¶](https://docs.python.org/3/library/dis.html#dis.Instruction.cache_info "Link to this definition")

Information about the cache entries of this instruction, as triplets of the form `(name, size, data)`, where the `name` and `size` describe the cache format and data is the contents of the cache. `cache_info` is `None` if the instruction does not have caches.

Added in version 3.4.

Changed in version 3.11: Field `positions` is added.

Changed in version 3.13: Changed field `starts_line`.

Added fields `start_offset`, `cache_offset`, `end_offset`, `baseopname`, `baseopcode`, `jump_target`, `oparg`, `line_number` and `cache_info`.

class dis.Positions[¶](https://docs.python.org/3/library/dis.html#dis.Positions "Link to this definition")

In case the information is not available, some fields might be `None`.

lineno[¶](https://docs.python.org/3/library/dis.html#dis.Positions.lineno "Link to this definition")

end\_lineno[¶](https://docs.python.org/3/library/dis.html#dis.Positions.end_lineno "Link to this definition")

col\_offset[¶](https://docs.python.org/3/library/dis.html#dis.Positions.col_offset "Link to this definition")

end\_col\_offset[¶](https://docs.python.org/3/library/dis.html#dis.Positions.end_col_offset "Link to this definition")

Added in version 3.11.

The Python compiler currently generates the following bytecode instructions.

**General instructions**

In the following, We will refer to the interpreter stack as `STACK` and describe operations on it as if it was a Python list. The top of the stack corresponds to `STACK[-1]` in this language.

NOP[¶](https://docs.python.org/3/library/dis.html#opcode-NOP "Link to this definition")

Do nothing code. Used as a placeholder by the bytecode optimizer, and to generate line tracing events.

NOT\_TAKEN[¶](https://docs.python.org/3/library/dis.html#opcode-NOT_TAKEN "Link to this definition")

Do nothing code. Used by the interpreter to record [`BRANCH_LEFT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_LEFT)
 and [`BRANCH_RIGHT`](https://docs.python.org/3/library/sys.monitoring.html#monitoring-event-BRANCH_RIGHT)
 events for [`sys.monitoring`](https://docs.python.org/3/library/sys.monitoring.html#module-sys.monitoring "sys.monitoring: Access and control event monitoring")
.

Added in version 3.14.

POP\_ITER[¶](https://docs.python.org/3/library/dis.html#opcode-POP_ITER "Link to this definition")

Removes the iterator from the top of the stack.

Added in version 3.14.

POP\_TOP[¶](https://docs.python.org/3/library/dis.html#opcode-POP_TOP "Link to this definition")

Removes the top-of-stack item:

Copy

STACK.pop()

END\_FOR[¶](https://docs.python.org/3/library/dis.html#opcode-END_FOR "Link to this definition")

Removes the top-of-stack item. Equivalent to `POP_TOP`. Used to clean up at the end of loops, hence the name.

Added in version 3.12.

END\_SEND[¶](https://docs.python.org/3/library/dis.html#opcode-END_SEND "Link to this definition")

Implements `del STACK[-2]`. Used to clean up when a generator exits.

Added in version 3.12.

COPY(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-COPY "Link to this definition")

Push the i-th item to the top of the stack without removing it from its original location:

Copy

assert i \> 0
STACK.append(STACK\[\-i\])

Added in version 3.11.

SWAP(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-SWAP "Link to this definition")

Swap the top of the stack with the i-th element:

Copy

STACK\[\-i\], STACK\[\-1\] \= STACK\[\-1\], STACK\[\-i\]

Added in version 3.11.

CACHE[¶](https://docs.python.org/3/library/dis.html#opcode-CACHE "Link to this definition")

Rather than being an actual instruction, this opcode is used to mark extra space for the interpreter to cache useful data directly in the bytecode itself. It is automatically hidden by all `dis` utilities, but can be viewed with `show_caches=True`.

Logically, this space is part of the preceding instruction. Many opcodes expect to be followed by an exact number of caches, and will instruct the interpreter to skip over them at runtime.

Populated caches can look like arbitrary instructions, so great care should be taken when reading or modifying raw, adaptive bytecode containing quickened data.

Added in version 3.11.

**Unary operations**

Unary operations take the top of the stack, apply the operation, and push the result back on the stack.

UNARY\_NEGATIVE[¶](https://docs.python.org/3/library/dis.html#opcode-UNARY_NEGATIVE "Link to this definition")

Implements `STACK[-1] = -STACK[-1]`.

UNARY\_NOT[¶](https://docs.python.org/3/library/dis.html#opcode-UNARY_NOT "Link to this definition")

Implements `STACK[-1] = not STACK[-1]`.

Changed in version 3.13: This instruction now requires an exact [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 operand.

UNARY\_INVERT[¶](https://docs.python.org/3/library/dis.html#opcode-UNARY_INVERT "Link to this definition")

Implements `STACK[-1] = ~STACK[-1]`.

GET\_ITER[¶](https://docs.python.org/3/library/dis.html#opcode-GET_ITER "Link to this definition")

Implements `STACK[-1] = iter(STACK[-1])`.

GET\_YIELD\_FROM\_ITER[¶](https://docs.python.org/3/library/dis.html#opcode-GET_YIELD_FROM_ITER "Link to this definition")

If `STACK[-1]` is a [generator iterator](https://docs.python.org/3/glossary.html#term-generator-iterator)
 or [coroutine](https://docs.python.org/3/glossary.html#term-coroutine)
 object it is left as is. Otherwise, implements `STACK[-1] = iter(STACK[-1])`.

Added in version 3.5.

TO\_BOOL[¶](https://docs.python.org/3/library/dis.html#opcode-TO_BOOL "Link to this definition")

Implements `STACK[-1] = bool(STACK[-1])`.

Added in version 3.13.

**Binary and in-place operations**

Binary operations remove the top two items from the stack (`STACK[-1]` and `STACK[-2]`). They perform the operation, then put the result back on the stack.

In-place operations are like binary operations, but the operation is done in-place when `STACK[-2]` supports it, and the resulting `STACK[-1]` may be (but does not have to be) the original `STACK[-2]`.

BINARY\_OP(_op_)[¶](https://docs.python.org/3/library/dis.html#opcode-BINARY_OP "Link to this definition")

Implements the binary and in-place operators (depending on the value of _op_):

Copy

rhs \= STACK.pop()
lhs \= STACK.pop()
STACK.append(lhs op rhs)

Added in version 3.11.

Changed in version 3.14: With oparg :`NB_SUBSCR`, implements binary subscript (replaces opcode `BINARY_SUBSCR`)

STORE\_SUBSCR[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_SUBSCR "Link to this definition")

Implements:

Copy

key \= STACK.pop()
container \= STACK.pop()
value \= STACK.pop()
container\[key\] \= value

DELETE\_SUBSCR[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_SUBSCR "Link to this definition")

Implements:

Copy

key \= STACK.pop()
container \= STACK.pop()
del container\[key\]

BINARY\_SLICE[¶](https://docs.python.org/3/library/dis.html#opcode-BINARY_SLICE "Link to this definition")

Implements:

Copy

end \= STACK.pop()
start \= STACK.pop()
container \= STACK.pop()
STACK.append(container\[start:end\])

Added in version 3.12.

STORE\_SLICE[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_SLICE "Link to this definition")

Implements:

Copy

end \= STACK.pop()
start \= STACK.pop()
container \= STACK.pop()
value \= STACK.pop()
container\[start:end\] \= value

Added in version 3.12.

**Coroutine opcodes**

GET\_AWAITABLE(_where_)[¶](https://docs.python.org/3/library/dis.html#opcode-GET_AWAITABLE "Link to this definition")

Implements `STACK[-1] = get_awaitable(STACK[-1])`, where `get_awaitable(o)` returns `o` if `o` is a coroutine object or a generator object with the [`CO_ITERABLE_COROUTINE`](https://docs.python.org/3/library/inspect.html#inspect.CO_ITERABLE_COROUTINE "inspect.CO_ITERABLE_COROUTINE")
 flag, or resolves `o.__await__`.

> If the `where` operand is nonzero, it indicates where the instruction occurs:
> 
> *   `1`: After a call to `__aenter__`
>     
> *   `2`: After a call to `__aexit__`
>     

Added in version 3.5.

Changed in version 3.11: Previously, this instruction did not have an oparg.

GET\_AITER[¶](https://docs.python.org/3/library/dis.html#opcode-GET_AITER "Link to this definition")

Implements `STACK[-1] = STACK[-1].__aiter__()`.

Added in version 3.5.

Changed in version 3.7: Returning awaitable objects from `__aiter__` is no longer supported.

GET\_ANEXT[¶](https://docs.python.org/3/library/dis.html#opcode-GET_ANEXT "Link to this definition")

Implement `STACK.append(get_awaitable(STACK[-1].__anext__()))` to the stack. See `GET_AWAITABLE` for details about `get_awaitable`.

Added in version 3.5.

END\_ASYNC\_FOR[¶](https://docs.python.org/3/library/dis.html#opcode-END_ASYNC_FOR "Link to this definition")

Terminates an [`async for`](https://docs.python.org/3/reference/compound_stmts.html#async-for)
 loop. Handles an exception raised when awaiting a next item. The stack contains the async iterable in `STACK[-2]` and the raised exception in `STACK[-1]`. Both are popped. If the exception is not [`StopAsyncIteration`](https://docs.python.org/3/builtins/exceptions.html#StopAsyncIteration "StopAsyncIteration")
, it is re-raised.

Added in version 3.8.

Changed in version 3.11: Exception representation on the stack now consist of one, not three, items.

CLEANUP\_THROW[¶](https://docs.python.org/3/library/dis.html#opcode-CLEANUP_THROW "Link to this definition")

Handles an exception raised during a [`throw()`](https://docs.python.org/3/builtins/stdtypes.html#generator.throw "generator.throw")
 or [`close()`](https://docs.python.org/3/builtins/stdtypes.html#generator.close "generator.close")
 call through the current frame. If `STACK[-1]` is an instance of [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
, pop three values from the stack and push its `value` member. Otherwise, re-raise `STACK[-1]`.

Added in version 3.12.

**Miscellaneous opcodes**

SET\_ADD(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-SET_ADD "Link to this definition")

Implements:

Copy

item \= STACK.pop()
set.add(STACK\[\-i\], item)

Used to implement set comprehensions.

LIST\_APPEND(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LIST_APPEND "Link to this definition")

Implements:

Copy

item \= STACK.pop()
list.append(STACK\[\-i\], item)

Used to implement list comprehensions.

MAP\_ADD(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-MAP_ADD "Link to this definition")

Implements:

Copy

value \= STACK.pop()
key \= STACK.pop()
dict.\_\_setitem\_\_(STACK\[\-i\], key, value)

Used to implement dict comprehensions.

Added in version 3.1.

Changed in version 3.8: Map value is `STACK[-1]` and map key is `STACK[-2]`. Before, those were reversed.

For all of the [`SET_ADD`](https://docs.python.org/3/library/dis.html#opcode-SET_ADD)
, [`LIST_APPEND`](https://docs.python.org/3/library/dis.html#opcode-LIST_APPEND)
 and [`MAP_ADD`](https://docs.python.org/3/library/dis.html#opcode-MAP_ADD)
 instructions, while the added value or key/value pair is popped off, the container object remains on the stack so that it is available for further iterations of the loop.

RETURN\_VALUE[¶](https://docs.python.org/3/library/dis.html#opcode-RETURN_VALUE "Link to this definition")

Returns with `STACK[-1]` to the caller of the function.

YIELD\_VALUE[¶](https://docs.python.org/3/library/dis.html#opcode-YIELD_VALUE "Link to this definition")

Yields `STACK.pop()` from a [generator](https://docs.python.org/3/glossary.html#term-generator)
.

Changed in version 3.11: oparg set to be the stack depth.

Changed in version 3.12: oparg set to be the exception block depth, for efficient closing of generators.

Changed in version 3.13: oparg is `1` if this instruction is part of a yield-from or await, and `0` otherwise.

SETUP\_ANNOTATIONS[¶](https://docs.python.org/3/library/dis.html#opcode-SETUP_ANNOTATIONS "Link to this definition")

Checks whether `__annotations__` is defined in `locals()`, if not it is set up to an empty `dict`. This opcode is only emitted if a class or module body contains [variable annotations](https://docs.python.org/3/glossary.html#term-variable-annotation)
 statically.

Added in version 3.6.

POP\_EXCEPT[¶](https://docs.python.org/3/library/dis.html#opcode-POP_EXCEPT "Link to this definition")

Pops a value from the stack, which is used to restore the exception state.

Changed in version 3.11: Exception representation on the stack now consist of one, not three, items.

RERAISE[¶](https://docs.python.org/3/library/dis.html#opcode-RERAISE "Link to this definition")

Re-raises the exception currently on top of the stack. If oparg is non-zero, pops an additional value from the stack which is used to set [`f_lasti`](https://docs.python.org/3/reference/datamodel.html#frame.f_lasti "frame.f_lasti")
 of the current frame.

Added in version 3.9.

Changed in version 3.11: Exception representation on the stack now consist of one, not three, items.

PUSH\_EXC\_INFO[¶](https://docs.python.org/3/library/dis.html#opcode-PUSH_EXC_INFO "Link to this definition")

Pops a value from the stack. Pushes the current exception to the top of the stack. Pushes the value originally popped back to the stack. Used in exception handlers.

Added in version 3.11.

CHECK\_EXC\_MATCH[¶](https://docs.python.org/3/library/dis.html#opcode-CHECK_EXC_MATCH "Link to this definition")

Performs exception matching for `except`. Tests whether the `STACK[-2]` is an exception matching `STACK[-1]`. Pops `STACK[-1]` and pushes the boolean result of the test.

Added in version 3.11.

CHECK\_EG\_MATCH[¶](https://docs.python.org/3/library/dis.html#opcode-CHECK_EG_MATCH "Link to this definition")

Performs exception matching for `except*`. Applies `split(STACK[-1])` on the exception group representing `STACK[-2]`.

In case of a match, pops two items from the stack and pushes the non-matching subgroup (`None` in case of full match) followed by the matching subgroup. When there is no match, pops one item (the match type) and pushes `None`.

Added in version 3.11.

WITH\_EXCEPT\_START[¶](https://docs.python.org/3/library/dis.html#opcode-WITH_EXCEPT_START "Link to this definition")

Calls the function in position 4 on the stack with arguments (type, val, tb) representing the exception at the top of the stack. Used to implement the call `context_manager.__exit__(*exc_info())` when an exception has occurred in a [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 statement.

Added in version 3.9.

Changed in version 3.11: The `__exit__` function is in position 4 of the stack rather than 7. Exception representation on the stack now consist of one, not three, items.

LOAD\_COMMON\_CONSTANT[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_COMMON_CONSTANT "Link to this definition")

Pushes a common constant onto the stack. The interpreter contains a hardcoded list of constants supported by this instruction. Used by the [`assert`](https://docs.python.org/3/reference/simple_stmts.html#assert)
 statement to load [`AssertionError`](https://docs.python.org/3/builtins/exceptions.html#AssertionError "AssertionError")
.

Added in version 3.14.

LOAD\_BUILD\_CLASS[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_BUILD_CLASS "Link to this definition")

Pushes `builtins.__build_class__()` onto the stack. It is later called to construct a class.

GET\_LEN[¶](https://docs.python.org/3/library/dis.html#opcode-GET_LEN "Link to this definition")

Perform `STACK.append(len(STACK[-1]))`. Used in [`match`](https://docs.python.org/3/reference/compound_stmts.html#match)
 statements where comparison with structure of pattern is needed.

Added in version 3.10.

MATCH\_MAPPING[¶](https://docs.python.org/3/library/dis.html#opcode-MATCH_MAPPING "Link to this definition")

If `STACK[-1]` is an instance of [`collections.abc.Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping")
 (or, more technically: if it has the [`Py_TPFLAGS_MAPPING`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_MAPPING "Py_TPFLAGS_MAPPING")
 flag set in its [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
), push `True` onto the stack. Otherwise, push `False`.

Added in version 3.10.

MATCH\_SEQUENCE[¶](https://docs.python.org/3/library/dis.html#opcode-MATCH_SEQUENCE "Link to this definition")

If `STACK[-1]` is an instance of [`collections.abc.Sequence`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Sequence "collections.abc.Sequence")
 and is _not_ an instance of [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
/[`bytes`](https://docs.python.org/3/builtins/stdtypes.html#bytes "bytes")
/[`bytearray`](https://docs.python.org/3/builtins/stdtypes.html#bytearray "bytearray")
 (or, more technically: if it has the [`Py_TPFLAGS_SEQUENCE`](https://docs.python.org/3/c-api/typeobj.html#c.Py_TPFLAGS_SEQUENCE "Py_TPFLAGS_SEQUENCE")
 flag set in its [`tp_flags`](https://docs.python.org/3/c-api/typeobj.html#c.PyTypeObject.tp_flags "PyTypeObject.tp_flags")
), push `True` onto the stack. Otherwise, push `False`.

Added in version 3.10.

MATCH\_KEYS[¶](https://docs.python.org/3/library/dis.html#opcode-MATCH_KEYS "Link to this definition")

`STACK[-1]` is a tuple of mapping keys, and `STACK[-2]` is the match subject. If `STACK[-2]` contains all of the keys in `STACK[-1]`, push a [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
 containing the corresponding values. Otherwise, push `None`.

Added in version 3.10.

Changed in version 3.11: Previously, this instruction also pushed a boolean value indicating success (`True`) or failure (`False`).

STORE\_NAME(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_NAME "Link to this definition")

Implements `name = STACK.pop()`. _namei_ is the index of _name_ in the attribute [`co_names`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_names "codeobject.co_names")
 of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)
. The compiler tries to use [`STORE_FAST`](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST)
 or [`STORE_GLOBAL`](https://docs.python.org/3/library/dis.html#opcode-STORE_GLOBAL)
 if possible.

DELETE\_NAME(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_NAME "Link to this definition")

Implements `del name`, where _namei_ is the index into [`co_names`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_names "codeobject.co_names")
 attribute of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)
.

UNPACK\_SEQUENCE(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-UNPACK_SEQUENCE "Link to this definition")

Unpacks `STACK[-1]` into _count_ individual values, which are put onto the stack right-to-left. Require there to be exactly _count_ values.:

Copy

assert(len(STACK\[\-1\]) \== count)
STACK.extend(STACK.pop()\[:\-count\-1:\-1\])

UNPACK\_EX(_counts_)[¶](https://docs.python.org/3/library/dis.html#opcode-UNPACK_EX "Link to this definition")

Implements assignment with a starred target: Unpacks an iterable in `STACK[-1]` into individual values, where the total number of values can be smaller than the number of items in the iterable: one of the new values will be a list of all leftover items.

The number of values before and after the list value is limited to 255.

The number of values before the list value is encoded in the argument of the opcode. The number of values after the list if any is encoded using an `EXTENDED_ARG`. As a consequence, the argument can be seen as a two bytes values where the low byte of _counts_ is the number of values before the list value, the high byte of _counts_ the number of values after it.

The extracted values are put onto the stack right-to-left, i.e. `a, *b, c = d` will be stored after execution as `STACK.extend((a, b, c))`.

STORE\_ATTR(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_ATTR "Link to this definition")

Implements:

Copy

obj \= STACK.pop()
value \= STACK.pop()
obj.name \= value

where _namei_ is the index of name in [`co_names`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_names "codeobject.co_names")
 of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)
.

DELETE\_ATTR(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_ATTR "Link to this definition")

Implements:

Copy

obj \= STACK.pop()
del obj.name

where _namei_ is the index of name into [`co_names`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_names "codeobject.co_names")
 of the [code object](https://docs.python.org/3/reference/datamodel.html#code-objects)
.

STORE\_GLOBAL(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_GLOBAL "Link to this definition")

Works as [`STORE_NAME`](https://docs.python.org/3/library/dis.html#opcode-STORE_NAME)
, but stores the name as a global.

DELETE\_GLOBAL(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_GLOBAL "Link to this definition")

Works as [`DELETE_NAME`](https://docs.python.org/3/library/dis.html#opcode-DELETE_NAME)
, but deletes a global name.

LOAD\_CONST(_consti_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_CONST "Link to this definition")

Pushes `co_consts[consti]` onto the stack.

LOAD\_SMALL\_INT(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_SMALL_INT "Link to this definition")

Pushes the integer `i` onto the stack. `i` must be in `range(256)`

Added in version 3.14.

LOAD\_NAME(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_NAME "Link to this definition")

Pushes the value associated with `co_names[namei]` onto the stack. The name is looked up within the locals, then the globals, then the builtins.

LOAD\_LOCALS[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_LOCALS "Link to this definition")

Pushes a reference to the locals dictionary onto the stack. This is used to prepare namespace dictionaries for [`LOAD_FROM_DICT_OR_DEREF`](https://docs.python.org/3/library/dis.html#opcode-LOAD_FROM_DICT_OR_DEREF)
 and [`LOAD_FROM_DICT_OR_GLOBALS`](https://docs.python.org/3/library/dis.html#opcode-LOAD_FROM_DICT_OR_GLOBALS)
.

Added in version 3.12.

LOAD\_FROM\_DICT\_OR\_GLOBALS(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FROM_DICT_OR_GLOBALS "Link to this definition")

Pops a mapping off the stack and looks up the value for `co_names[namei]`. If the name is not found there, looks it up in the globals and then the builtins, similar to [`LOAD_GLOBAL`](https://docs.python.org/3/library/dis.html#opcode-LOAD_GLOBAL)
. This is used for loading global variables in [annotation scopes](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
 within class bodies.

Added in version 3.12.

BUILD\_TEMPLATE[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_TEMPLATE "Link to this definition")

Constructs a new [`Template`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Template "string.templatelib.Template")
 instance from a tuple of strings and a tuple of interpolations and pushes the resulting object onto the stack:

Copy

interpolations \= STACK.pop()
strings \= STACK.pop()
STACK.append(\_build\_template(strings, interpolations))

Added in version 3.14.

BUILD\_INTERPOLATION(_format_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_INTERPOLATION "Link to this definition")

Constructs a new [`Interpolation`](https://docs.python.org/3/library/string.templatelib.html#string.templatelib.Interpolation "string.templatelib.Interpolation")
 instance from a value and its source expression and pushes the resulting object onto the stack.

If no conversion or format specification is present, `format` is set to `2`.

If the low bit of `format` is set, it indicates that the interpolation contains a format specification.

If `format >> 2` is non-zero, it indicates that the interpolation contains a conversion. The value of `format >> 2` is the conversion type (`0` for no conversion, `1` for `!s`, `2` for `!r`, and `3` for `!a`):

Copy

conversion \= format \>> 2
if format & 1:
    format\_spec \= STACK.pop()
else:
    format\_spec \= None
expression \= STACK.pop()
value \= STACK.pop()
STACK.append(\_build\_interpolation(value, expression, conversion, format\_spec))

Added in version 3.14.

BUILD\_TUPLE(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_TUPLE "Link to this definition")

Creates a tuple consuming _count_ items from the stack, and pushes the resulting tuple onto the stack:

Copy

if count \== 0:
    value \= ()
else:
    value \= tuple(STACK\[\-count:\])
    STACK \= STACK\[:\-count\]

STACK.append(value)

BUILD\_LIST(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_LIST "Link to this definition")

Works as [`BUILD_TUPLE`](https://docs.python.org/3/library/dis.html#opcode-BUILD_TUPLE)
, but creates a list.

BUILD\_SET(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_SET "Link to this definition")

Works as [`BUILD_TUPLE`](https://docs.python.org/3/library/dis.html#opcode-BUILD_TUPLE)
, but creates a set.

BUILD\_MAP(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_MAP "Link to this definition")

Pushes a new dictionary object onto the stack. Pops `2 * count` items so that the dictionary holds _count_ entries: `{..., STACK[-4]: STACK[-3], STACK[-2]: STACK[-1]}`.

Changed in version 3.5: The dictionary is created from stack items instead of creating an empty dictionary pre-sized to hold _count_ items.

BUILD\_STRING(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_STRING "Link to this definition")

Concatenates _count_ strings from the stack and pushes the resulting string onto the stack.

Added in version 3.6.

LIST\_EXTEND(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LIST_EXTEND "Link to this definition")

Implements:

Copy

seq \= STACK.pop()
list.extend(STACK\[\-i\], seq)

Used to build lists.

Added in version 3.9.

SET\_UPDATE(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-SET_UPDATE "Link to this definition")

Implements:

Copy

seq \= STACK.pop()
set.update(STACK\[\-i\], seq)

Used to build sets.

Added in version 3.9.

DICT\_UPDATE(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-DICT_UPDATE "Link to this definition")

Implements:

Copy

map \= STACK.pop()
dict.update(STACK\[\-i\], map)

Used to build dicts.

Added in version 3.9.

DICT\_MERGE(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-DICT_MERGE "Link to this definition")

Like [`DICT_UPDATE`](https://docs.python.org/3/library/dis.html#opcode-DICT_UPDATE)
 but raises an exception for duplicate keys.

Added in version 3.9.

LOAD\_ATTR(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_ATTR "Link to this definition")

If the low bit of `namei` is not set, this replaces `STACK[-1]` with `getattr(STACK[-1], co_names[namei>>1])`.

If the low bit of `namei` is set, this will attempt to load a method named `co_names[namei>>1]` from the `STACK[-1]` object. `STACK[-1]` is popped. This bytecode distinguishes two cases: if `STACK[-1]` has a method with the correct name, the bytecode pushes the unbound method and `STACK[-1]`. `STACK[-1]` will be used as the first argument (`self`) by [`CALL`](https://docs.python.org/3/library/dis.html#opcode-CALL)
 or [`CALL_KW`](https://docs.python.org/3/library/dis.html#opcode-CALL_KW)
 when calling the unbound method. Otherwise, `NULL` and the object returned by the attribute lookup are pushed.

Changed in version 3.12: If the low bit of `namei` is set, then a `NULL` or `self` is pushed to the stack before the attribute or unbound method respectively.

LOAD\_SUPER\_ATTR(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_SUPER_ATTR "Link to this definition")

This opcode implements [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
, both in its zero-argument and two-argument forms (e.g. `super().method()`, `super().attr` and `super(cls, self).method()`, `super(cls, self).attr`).

It pops three values from the stack (from top of stack down):

*   `self`: the first argument to the current method
    
*   `cls`: the class within which the current method was defined
    
*   the global `super`
    

With respect to its argument, it works similarly to [`LOAD_ATTR`](https://docs.python.org/3/library/dis.html#opcode-LOAD_ATTR)
, except that `namei` is shifted right by 2 bits instead of 1.

The low bit of `namei` signals to attempt a method load, as with [`LOAD_ATTR`](https://docs.python.org/3/library/dis.html#opcode-LOAD_ATTR)
, which results in pushing `NULL` and the loaded method. When it is unset a single value is pushed to the stack.

The second-low bit of `namei`, if set, means that this was a two-argument call to [`super()`](https://docs.python.org/3/builtins/functions.html#super "super")
 (unset means zero-argument).

Added in version 3.12.

COMPARE\_OP(_opname_)[¶](https://docs.python.org/3/library/dis.html#opcode-COMPARE_OP "Link to this definition")

Performs a Boolean operation. The operation name can be found in `cmp_op[opname >> 5]`. If the fifth-lowest bit of `opname` is set (`opname & 16`), the result should be coerced to `bool`.

Changed in version 3.13: The fifth-lowest bit of the oparg now indicates a forced conversion to [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
.

IS\_OP(_invert_)[¶](https://docs.python.org/3/library/dis.html#opcode-IS_OP "Link to this definition")

Performs `is` comparison, or `is not` if `invert` is 1.

Added in version 3.9.

CONTAINS\_OP(_invert_)[¶](https://docs.python.org/3/library/dis.html#opcode-CONTAINS_OP "Link to this definition")

Performs `in` comparison, or `not in` if `invert` is 1.

Added in version 3.9.

IMPORT\_NAME(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-IMPORT_NAME "Link to this definition")

Imports the module `co_names[namei]`. `STACK[-1]` and `STACK[-2]` are popped and provide the _fromlist_ and _level_ arguments of [`__import__()`](https://docs.python.org/3/builtins/functions.html#import__ "__import__")
. The module object is pushed onto the stack. The current namespace is not affected: for a proper import statement, a subsequent [`STORE_FAST`](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST)
 instruction modifies the namespace.

IMPORT\_FROM(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-IMPORT_FROM "Link to this definition")

Loads the attribute `co_names[namei]` from the module found in `STACK[-1]`. The resulting object is pushed onto the stack, to be subsequently stored by a [`STORE_FAST`](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST)
 instruction.

JUMP\_FORWARD(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_FORWARD "Link to this definition")

Increments bytecode counter by _delta_.

JUMP\_BACKWARD(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_BACKWARD "Link to this definition")

Decrements bytecode counter by _delta_. Checks for interrupts.

Added in version 3.11.

JUMP\_BACKWARD\_NO\_INTERRUPT(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_BACKWARD_NO_INTERRUPT "Link to this definition")

Decrements bytecode counter by _delta_. Does not check for interrupts.

Added in version 3.11.

POP\_JUMP\_IF\_TRUE(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-POP_JUMP_IF_TRUE "Link to this definition")

If `STACK[-1]` is true, increments the bytecode counter by _delta_. `STACK[-1]` is popped.

Changed in version 3.11: The oparg is now a relative delta rather than an absolute target. This opcode is a pseudo-instruction, replaced in final bytecode by the directed versions (forward/backward).

Changed in version 3.12: This is no longer a pseudo-instruction.

Changed in version 3.13: This instruction now requires an exact [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 operand.

POP\_JUMP\_IF\_FALSE(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-POP_JUMP_IF_FALSE "Link to this definition")

If `STACK[-1]` is false, increments the bytecode counter by _delta_. `STACK[-1]` is popped.

Changed in version 3.11: The oparg is now a relative delta rather than an absolute target. This opcode is a pseudo-instruction, replaced in final bytecode by the directed versions (forward/backward).

Changed in version 3.12: This is no longer a pseudo-instruction.

Changed in version 3.13: This instruction now requires an exact [`bool`](https://docs.python.org/3/builtins/functions.html#bool "bool")
 operand.

POP\_JUMP\_IF\_NOT\_NONE(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-POP_JUMP_IF_NOT_NONE "Link to this definition")

If `STACK[-1]` is not `None`, increments the bytecode counter by _delta_. `STACK[-1]` is popped.

Added in version 3.11.

Changed in version 3.12: This is no longer a pseudo-instruction.

POP\_JUMP\_IF\_NONE(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-POP_JUMP_IF_NONE "Link to this definition")

If `STACK[-1]` is `None`, increments the bytecode counter by _delta_. `STACK[-1]` is popped.

Added in version 3.11.

Changed in version 3.12: This is no longer a pseudo-instruction.

FOR\_ITER(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-FOR_ITER "Link to this definition")

`STACK[-1]` is an [iterator](https://docs.python.org/3/glossary.html#term-iterator)
. Call its [`__next__()`](https://docs.python.org/3/builtins/stdtypes.html#iterator.__next__ "iterator.__next__")
 method. If this yields a new value, push it on the stack (leaving the iterator below it). If the iterator indicates it is [exhausted](https://docs.python.org/3/glossary.html#term-exhausted)
 then the byte code counter is incremented by _delta_.

Changed in version 3.12: Up until 3.11 the iterator was popped when it was exhausted.

LOAD\_GLOBAL(_namei_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_GLOBAL "Link to this definition")

Loads the global named `co_names[namei>>1]` onto the stack. If the low bit of `namei` is set, a `NULL` is pushed onto the stack after the global variable.

Changed in version 3.11: The low bit of `namei` indicates whether a `NULL` is pushed.

Changed in version 3.13: The `NULL` is pushed after the global variable, rather than before it.

LOAD\_FAST(_var\_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST "Link to this definition")

Pushes a reference to the local `co_varnames[var_num]` onto the stack.

Changed in version 3.12: This opcode is now only used in situations where the local variable is guaranteed to be initialized. It cannot raise [`UnboundLocalError`](https://docs.python.org/3/builtins/exceptions.html#UnboundLocalError "UnboundLocalError")
.

LOAD\_FAST\_BORROW(_var\_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST_BORROW "Link to this definition")

Pushes a borrowed reference to the local `co_varnames[var_num]` onto the stack.

Added in version 3.14.

LOAD\_FAST\_LOAD\_FAST(_var\_nums_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST_LOAD_FAST "Link to this definition")

Pushes references to `co_varnames[var_nums >> 4]` and `co_varnames[var_nums & 15]` onto the stack.

Added in version 3.13.

LOAD\_FAST\_BORROW\_LOAD\_FAST\_BORROW(_var\_nums_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST_BORROW_LOAD_FAST_BORROW "Link to this definition")

Pushes borrowed references to `co_varnames[var_nums >> 4]` and `co_varnames[var_nums & 15]` onto the stack.

Added in version 3.14.

LOAD\_FAST\_CHECK(_var\_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST_CHECK "Link to this definition")

Pushes a reference to the local `co_varnames[var_num]` onto the stack, raising an [`UnboundLocalError`](https://docs.python.org/3/builtins/exceptions.html#UnboundLocalError "UnboundLocalError")
 if the local variable has not been initialized.

Added in version 3.12.

LOAD\_FAST\_AND\_CLEAR(_var\_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FAST_AND_CLEAR "Link to this definition")

Pushes a reference to the local `co_varnames[var_num]` onto the stack (or pushes `NULL` onto the stack if the local variable has not been initialized) and sets `co_varnames[var_num]` to `NULL`.

Added in version 3.12.

STORE\_FAST(_var\_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST "Link to this definition")

Stores `STACK.pop()` into the local `co_varnames[var_num]`.

STORE\_FAST\_STORE\_FAST(_var\_nums_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST_STORE_FAST "Link to this definition")

Stores `STACK[-1]` into `co_varnames[var_nums >> 4]` and `STACK[-2]` into `co_varnames[var_nums & 15]`.

Added in version 3.13.

STORE\_FAST\_LOAD\_FAST(_var\_nums_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_FAST_LOAD_FAST "Link to this definition")

Stores `STACK.pop()` into the local `co_varnames[var_nums >> 4]` and pushes a reference to the local `co_varnames[var_nums & 15]` onto the stack.

Added in version 3.13.

DELETE\_FAST(_var\_num_)[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_FAST "Link to this definition")

Deletes local `co_varnames[var_num]`.

MAKE\_CELL(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-MAKE_CELL "Link to this definition")

Creates a new cell in slot `i`. If that slot is nonempty then that value is stored into the new cell.

Added in version 3.11.

LOAD\_DEREF(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_DEREF "Link to this definition")

Loads the cell contained in slot `i` of the “fast locals” storage. Pushes a reference to the object the cell contains on the stack.

Changed in version 3.11: `i` is no longer offset by the length of [`co_varnames`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_varnames "codeobject.co_varnames")
.

LOAD\_FROM\_DICT\_OR\_DEREF(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_FROM_DICT_OR_DEREF "Link to this definition")

Pops a mapping off the stack and looks up the name associated with slot `i` of the “fast locals” storage in this mapping. If the name is not found there, loads it from the cell contained in slot `i`, similar to [`LOAD_DEREF`](https://docs.python.org/3/library/dis.html#opcode-LOAD_DEREF)
. This is used for loading [closure variables](https://docs.python.org/3/glossary.html#term-closure-variable)
 in class bodies (which previously used `LOAD_CLASSDEREF`) and in [annotation scopes](https://docs.python.org/3/reference/executionmodel.html#annotation-scopes)
 within class bodies.

Added in version 3.12.

STORE\_DEREF(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-STORE_DEREF "Link to this definition")

Stores `STACK.pop()` into the cell contained in slot `i` of the “fast locals” storage.

Changed in version 3.11: `i` is no longer offset by the length of [`co_varnames`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_varnames "codeobject.co_varnames")
.

DELETE\_DEREF(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-DELETE_DEREF "Link to this definition")

Empties the cell contained in slot `i` of the “fast locals” storage. Used by the [`del`](https://docs.python.org/3/reference/simple_stmts.html#del)
 statement.

Added in version 3.2.

Changed in version 3.11: `i` is no longer offset by the length of [`co_varnames`](https://docs.python.org/3/reference/datamodel.html#codeobject.co_varnames "codeobject.co_varnames")
.

COPY\_FREE\_VARS(_n_)[¶](https://docs.python.org/3/library/dis.html#opcode-COPY_FREE_VARS "Link to this definition")

Copies the `n` [free (closure) variables](https://docs.python.org/3/glossary.html#term-closure-variable)
 from the closure into the frame. Removes the need for special code on the caller’s side when calling closures.

Added in version 3.11.

RAISE\_VARARGS(_argc_)[¶](https://docs.python.org/3/library/dis.html#opcode-RAISE_VARARGS "Link to this definition")

Raises an exception using one of the 3 forms of the `raise` statement, depending on the value of _argc_:

*   0: `raise` (re-raise previous exception)
    
*   1: `raise STACK[-1]` (raise exception instance or type at `STACK[-1]`)
    
*   2: `raise STACK[-2] from STACK[-1]` (raise exception instance or type at `STACK[-2]` with `__cause__` set to `STACK[-1]`)
    

CALL(_argc_)[¶](https://docs.python.org/3/library/dis.html#opcode-CALL "Link to this definition")

Calls a callable object with the number of arguments specified by `argc`. On the stack are (in ascending order):

*   The callable
    
*   `self` or `NULL`
    
*   The remaining positional arguments
    

`argc` is the total of the positional arguments, excluding `self`.

`CALL` pops all arguments and the callable object off the stack, calls the callable object with those arguments, and pushes the return value returned by the callable object.

Added in version 3.11.

Changed in version 3.13: The callable now always appears at the same position on the stack.

Changed in version 3.13: Calls with keyword arguments are now handled by [`CALL_KW`](https://docs.python.org/3/library/dis.html#opcode-CALL_KW)
.

CALL\_KW(_argc_)[¶](https://docs.python.org/3/library/dis.html#opcode-CALL_KW "Link to this definition")

Calls a callable object with the number of arguments specified by `argc`, including one or more named arguments. On the stack are (in ascending order):

*   The callable
    
*   `self` or `NULL`
    
*   The remaining positional arguments
    
*   The named arguments
    
*   A [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple "tuple")
     of keyword argument names
    

`argc` is the total of the positional and named arguments, excluding `self`. The length of the tuple of keyword argument names is the number of named arguments.

`CALL_KW` pops all arguments, the keyword names, and the callable object off the stack, calls the callable object with those arguments, and pushes the return value returned by the callable object.

Added in version 3.13.

CALL\_FUNCTION\_EX(_flags_)[¶](https://docs.python.org/3/library/dis.html#opcode-CALL_FUNCTION_EX "Link to this definition")

Calls a callable object with variable set of positional and keyword arguments. If the lowest bit of _flags_ is set, the top of the stack contains a mapping object containing additional keyword arguments. Before the callable is called, the mapping object and iterable object are each “unpacked” and their contents passed in as keyword and positional arguments respectively. `CALL_FUNCTION_EX` pops all arguments and the callable object off the stack, calls the callable object with those arguments, and pushes the return value returned by the callable object.

Added in version 3.6.

PUSH\_NULL[¶](https://docs.python.org/3/library/dis.html#opcode-PUSH_NULL "Link to this definition")

Pushes a `NULL` to the stack. Used in the call sequence to match the `NULL` pushed by [`LOAD_ATTR`](https://docs.python.org/3/library/dis.html#opcode-LOAD_ATTR)
 for non-method calls.

Added in version 3.11.

MAKE\_FUNCTION[¶](https://docs.python.org/3/library/dis.html#opcode-MAKE_FUNCTION "Link to this definition")

Pushes a new function object on the stack built from the code object at `STACK[-1]`.

Changed in version 3.10: Flag value `0x04` is a tuple of strings instead of dictionary

Changed in version 3.11: Qualified name at `STACK[-1]` was removed.

Changed in version 3.13: Extra function attributes on the stack, signaled by oparg flags, were removed. They now use [`SET_FUNCTION_ATTRIBUTE`](https://docs.python.org/3/library/dis.html#opcode-SET_FUNCTION_ATTRIBUTE)
.

SET\_FUNCTION\_ATTRIBUTE(_flag_)[¶](https://docs.python.org/3/library/dis.html#opcode-SET_FUNCTION_ATTRIBUTE "Link to this definition")

Sets an attribute on a function object. Expects the function at `STACK[-1]` and the attribute value to set at `STACK[-2]`; consumes both and leaves the function at `STACK[-1]`. The flag determines which attribute to set:

*   `0x01` a tuple of default values for positional-only and positional-or-keyword parameters in positional order
    
*   `0x02` a dictionary of keyword-only parameters’ default values
    
*   `0x04` a tuple of strings containing parameters’ annotations
    
*   `0x08` a tuple containing cells for free variables, making a closure
    
*   `0x10` the [annotate function](https://docs.python.org/3/glossary.html#term-annotate-function)
     for the function object
    

Added in version 3.13.

Changed in version 3.14: Added `0x10` to indicate the annotate function for the function object.

BUILD\_SLICE(_argc_)[¶](https://docs.python.org/3/library/dis.html#opcode-BUILD_SLICE "Link to this definition")

Pushes a slice object on the stack. _argc_ must be 2 or 3. If it is 2, implements:

Copy

end \= STACK.pop()
start \= STACK.pop()
STACK.append(slice(start, end))

if it is 3, implements:

Copy

step \= STACK.pop()
end \= STACK.pop()
start \= STACK.pop()
STACK.append(slice(start, end, step))

See the [`slice()`](https://docs.python.org/3/builtins/functions.html#slice "slice")
 built-in function for more information.

EXTENDED\_ARG(_ext_)[¶](https://docs.python.org/3/library/dis.html#opcode-EXTENDED_ARG "Link to this definition")

Prefixes any opcode which has an argument too big to fit into the default one byte. _ext_ holds an additional byte which act as higher bits in the argument. For each opcode, at most three prefixal `EXTENDED_ARG` are allowed, forming an argument from two-byte to four-byte.

CONVERT\_VALUE(_oparg_)[¶](https://docs.python.org/3/library/dis.html#opcode-CONVERT_VALUE "Link to this definition")

Convert value to a string, depending on `oparg`:

Copy

value \= STACK.pop()
result \= func(value)
STACK.append(result)

*   `oparg == 1`: call [`str()`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
     on _value_
    
*   `oparg == 2`: call [`repr()`](https://docs.python.org/3/builtins/functions.html#repr "repr")
     on _value_
    
*   `oparg == 3`: call [`ascii()`](https://docs.python.org/3/builtins/functions.html#ascii "ascii")
     on _value_
    

Used for implementing formatted string literals (f-strings).

Added in version 3.13.

FORMAT\_SIMPLE[¶](https://docs.python.org/3/library/dis.html#opcode-FORMAT_SIMPLE "Link to this definition")

Formats the value on top of stack:

Copy

value \= STACK.pop()
result \= value.\_\_format\_\_("")
STACK.append(result)

Used for implementing formatted string literals (f-strings).

Added in version 3.13.

FORMAT\_WITH\_SPEC[¶](https://docs.python.org/3/library/dis.html#opcode-FORMAT_WITH_SPEC "Link to this definition")

Formats the given value with the given format spec:

Copy

spec \= STACK.pop()
value \= STACK.pop()
result \= value.\_\_format\_\_(spec)
STACK.append(result)

Used for implementing formatted string literals (f-strings).

Added in version 3.13.

MATCH\_CLASS(_count_)[¶](https://docs.python.org/3/library/dis.html#opcode-MATCH_CLASS "Link to this definition")

`STACK[-1]` is a tuple of keyword attribute names, `STACK[-2]` is the class being matched against, and `STACK[-3]` is the match subject. _count_ is the number of positional sub-patterns.

Pop `STACK[-1]`, `STACK[-2]`, and `STACK[-3]`. If `STACK[-3]` is an instance of `STACK[-2]` and has the positional and keyword attributes required by _count_ and `STACK[-1]`, push a tuple of extracted attributes. Otherwise, push `None`.

Added in version 3.10.

Changed in version 3.11: Previously, this instruction also pushed a boolean value indicating success (`True`) or failure (`False`).

RESUME(_context_)[¶](https://docs.python.org/3/library/dis.html#opcode-RESUME "Link to this definition")

A no-op. Performs internal tracing, debugging and optimization checks.

The `context` operand consists of two parts. The lowest two bits indicate where the `RESUME` occurs:

*   `0` The start of a function, which is neither a generator, coroutine nor an async generator
    
*   `1` After a `yield` expression
    
*   `2` After a `yield from` expression
    
*   `3` After an `await` expression
    

The next bit is `1` if the RESUME is at except-depth `1`, and `0` otherwise.

Added in version 3.11.

Changed in version 3.13: The oparg value changed to include information about except-depth

RETURN\_GENERATOR[¶](https://docs.python.org/3/library/dis.html#opcode-RETURN_GENERATOR "Link to this definition")

Create a generator, coroutine, or async generator from the current frame. Used as first opcode of in code object for the above mentioned callables. Clear the current frame and return the newly created generator.

Added in version 3.11.

SEND(_delta_)[¶](https://docs.python.org/3/library/dis.html#opcode-SEND "Link to this definition")

Equivalent to `STACK[-1] = STACK[-2].send(STACK[-1])`. Used in `yield from` and `await` statements.

If the call raises [`StopIteration`](https://docs.python.org/3/builtins/exceptions.html#StopIteration "StopIteration")
, pop the top value from the stack, push the exception’s `value` attribute, and increment the bytecode counter by _delta_.

Added in version 3.11.

HAVE\_ARGUMENT[¶](https://docs.python.org/3/library/dis.html#opcode-HAVE_ARGUMENT "Link to this definition")

This is not really an opcode. It identifies the dividing line between opcodes in the range \[0,255\] which don’t use their argument and those that do (`< HAVE_ARGUMENT` and `>= HAVE_ARGUMENT`, respectively).

If your application uses pseudo instructions or specialized instructions, use the [`hasarg`](https://docs.python.org/3/library/dis.html#dis.hasarg "dis.hasarg")
 collection instead.

Changed in version 3.6: Now every instruction has an argument, but opcodes `< HAVE_ARGUMENT` ignore it. Before, only opcodes `>= HAVE_ARGUMENT` had an argument.

Changed in version 3.12: Pseudo instructions were added to the `dis` module, and for them it is not true that comparison with `HAVE_ARGUMENT` indicates whether they use their arg.

Deprecated since version 3.13: Use [`hasarg`](https://docs.python.org/3/library/dis.html#dis.hasarg "dis.hasarg")
 instead.

CALL\_INTRINSIC\_1[¶](https://docs.python.org/3/library/dis.html#opcode-CALL_INTRINSIC_1 "Link to this definition")

Calls an intrinsic function with one argument. Passes `STACK[-1]` as the argument and sets `STACK[-1]` to the result. Used to implement functionality that is not performance critical.

The operand determines which intrinsic function is called:

| Operand | Description |
| --- | --- |
| `INTRINSIC_1_INVALID` | Not valid |
| `INTRINSIC_PRINT` | Prints the argument to standard out. Used in the REPL. |
| `INTRINSIC_IMPORT_STAR` | Performs `import *` for the named module. |
| `INTRINSIC_STOPITERATION_ERROR` | Extracts the return value from a `StopIteration` exception. |
| `INTRINSIC_ASYNC_GEN_WRAP` | Wraps an async generator value |
| `INTRINSIC_UNARY_POSITIVE` | Performs the unary `+` operation |
| `INTRINSIC_LIST_TO_TUPLE` | Converts a list to a tuple |
| `INTRINSIC_TYPEVAR` | Creates a [`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar") |
| `INTRINSIC_PARAMSPEC` | Creates a [`typing.ParamSpec`](https://docs.python.org/3/library/typing.html#typing.ParamSpec "typing.ParamSpec") |
| `INTRINSIC_TYPEVARTUPLE` | Creates a [`typing.TypeVarTuple`](https://docs.python.org/3/library/typing.html#typing.TypeVarTuple "typing.TypeVarTuple") |
| `INTRINSIC_SUBSCRIPT_GENERIC` | Returns [`typing.Generic`](https://docs.python.org/3/library/typing.html#typing.Generic "typing.Generic")<br> subscripted with the argument |
| `INTRINSIC_TYPEALIAS` | Creates a [`typing.TypeAliasType`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType "typing.TypeAliasType")<br>; used in the [`type`](https://docs.python.org/3/reference/simple_stmts.html#type)<br> statement. The argument is a tuple of the type alias’s name, type parameters, and value. |

Added in version 3.12.

CALL\_INTRINSIC\_2[¶](https://docs.python.org/3/library/dis.html#opcode-CALL_INTRINSIC_2 "Link to this definition")

Calls an intrinsic function with two arguments. Used to implement functionality that is not performance critical:

Copy

arg2 \= STACK.pop()
arg1 \= STACK.pop()
result \= intrinsic2(arg1, arg2)
STACK.append(result)

The operand determines which intrinsic function is called:

| Operand | Description |
| --- | --- |
| `INTRINSIC_2_INVALID` | Not valid |
| `INTRINSIC_PREP_RERAISE_STAR` | Calculates the [`ExceptionGroup`](https://docs.python.org/3/builtins/exceptions.html#ExceptionGroup "ExceptionGroup")<br> to raise from a `try-except*`. |
| `INTRINSIC_TYPEVAR_WITH_BOUND` | Creates a [`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar")<br> with a bound. |
| `INTRINSIC_TYPEVAR_WITH_CONSTRAINTS` | Creates a [`typing.TypeVar`](https://docs.python.org/3/library/typing.html#typing.TypeVar "typing.TypeVar")<br> with constraints. |
| `INTRINSIC_SET_FUNCTION_TYPE_PARAMS` | Sets the `__type_params__` attribute of a function. |

Added in version 3.12.

LOAD\_SPECIAL[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_SPECIAL "Link to this definition")

Performs special method lookup on `STACK[-1]`. If `type(STACK[-1]).__xxx__` is a method, leave `type(STACK[-1]).__xxx__; STACK[-1]` on the stack. If `type(STACK[-1]).__xxx__` is not a method, leave `STACK[-1].__xxx__; NULL` on the stack.

Added in version 3.14.

**Pseudo-instructions**

These opcodes do not appear in Python bytecode. They are used by the compiler but are replaced by real opcodes or removed before bytecode is generated.

SETUP\_FINALLY(_target_)[¶](https://docs.python.org/3/library/dis.html#opcode-SETUP_FINALLY "Link to this definition")

Set up an exception handler for the following code block. If an exception occurs, the value stack level is restored to its current state and control is transferred to the exception handler at `target`.

SETUP\_CLEANUP(_target_)[¶](https://docs.python.org/3/library/dis.html#opcode-SETUP_CLEANUP "Link to this definition")

Like `SETUP_FINALLY`, but in case of an exception also pushes the last instruction (`lasti`) to the stack so that `RERAISE` can restore it. If an exception occurs, the value stack level and the last instruction on the frame are restored to their current state, and control is transferred to the exception handler at `target`.

SETUP\_WITH(_target_)[¶](https://docs.python.org/3/library/dis.html#opcode-SETUP_WITH "Link to this definition")

Like `SETUP_CLEANUP`, but in case of an exception one more item is popped from the stack before control is transferred to the exception handler at `target`.

This variant is used in [`with`](https://docs.python.org/3/reference/compound_stmts.html#with)
 and [`async with`](https://docs.python.org/3/reference/compound_stmts.html#async-with)
 constructs, which push the return value of the context manager’s [`__enter__()`](https://docs.python.org/3/reference/datamodel.html#object.__enter__ "object.__enter__")
 or [`__aenter__()`](https://docs.python.org/3/reference/datamodel.html#object.__aenter__ "object.__aenter__")
 to the stack.

POP\_BLOCK[¶](https://docs.python.org/3/library/dis.html#opcode-POP_BLOCK "Link to this definition")

Marks the end of the code block associated with the last `SETUP_FINALLY`, `SETUP_CLEANUP` or `SETUP_WITH`.

JUMP[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP "Link to this definition")

JUMP\_NO\_INTERRUPT[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_NO_INTERRUPT "Link to this definition")

Undirected relative jump instructions which are replaced by their directed (forward/backward) counterparts by the assembler.

JUMP\_IF\_TRUE[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_IF_TRUE "Link to this definition")

JUMP\_IF\_FALSE[¶](https://docs.python.org/3/library/dis.html#opcode-JUMP_IF_FALSE "Link to this definition")

Conditional jumps which do not impact the stack. Replaced by the sequence `COPY 1`, `TO_BOOL`, `POP_JUMP_IF_TRUE/FALSE`.

LOAD\_CLOSURE(_i_)[¶](https://docs.python.org/3/library/dis.html#opcode-LOAD_CLOSURE "Link to this definition")

Pushes a reference to the cell contained in slot `i` of the “fast locals” storage.

Note that `LOAD_CLOSURE` is replaced with `LOAD_FAST` in the assembler.

Changed in version 3.13: This opcode is now a pseudo-instruction.

Opcode collections[¶](https://docs.python.org/3/library/dis.html#opcode-collections "Link to this heading")

------------------------------------------------------------------------------------------------------------

These collections are provided for automatic introspection of bytecode instructions:

Changed in version 3.12: The collections now contain pseudo instructions and instrumented instructions as well. These are opcodes with values `>= MIN_PSEUDO_OPCODE` and `>= MIN_INSTRUMENTED_OPCODE`.

dis.opname[¶](https://docs.python.org/3/library/dis.html#dis.opname "Link to this definition")

Sequence of operation names, indexable using the bytecode.

dis.opmap[¶](https://docs.python.org/3/library/dis.html#dis.opmap "Link to this definition")

Dictionary mapping operation names to bytecodes.

dis.cmp\_op[¶](https://docs.python.org/3/library/dis.html#dis.cmp_op "Link to this definition")

Sequence of all compare operation names.

dis.hasarg[¶](https://docs.python.org/3/library/dis.html#dis.hasarg "Link to this definition")

Sequence of bytecodes that use their argument.

Added in version 3.12.

dis.hasconst[¶](https://docs.python.org/3/library/dis.html#dis.hasconst "Link to this definition")

Sequence of bytecodes that access a constant.

dis.hasfree[¶](https://docs.python.org/3/library/dis.html#dis.hasfree "Link to this definition")

Sequence of bytecodes that access a [free (closure) variable](https://docs.python.org/3/glossary.html#term-closure-variable)
. ‘free’ in this context refers to names in the current scope that are referenced by inner scopes or names in outer scopes that are referenced from this scope. It does _not_ include references to global or builtin scopes.

dis.hasname[¶](https://docs.python.org/3/library/dis.html#dis.hasname "Link to this definition")

Sequence of bytecodes that access an attribute by name.

dis.hasjump[¶](https://docs.python.org/3/library/dis.html#dis.hasjump "Link to this definition")

Sequence of bytecodes that have a jump target. All jumps are relative.

Added in version 3.13.

dis.haslocal[¶](https://docs.python.org/3/library/dis.html#dis.haslocal "Link to this definition")

Sequence of bytecodes that access a local variable.

dis.hascompare[¶](https://docs.python.org/3/library/dis.html#dis.hascompare "Link to this definition")

Sequence of bytecodes of Boolean operations.

dis.hasexc[¶](https://docs.python.org/3/library/dis.html#dis.hasexc "Link to this definition")

Sequence of bytecodes that set an exception handler.

Added in version 3.12.

dis.hasjrel[¶](https://docs.python.org/3/library/dis.html#dis.hasjrel "Link to this definition")

Sequence of bytecodes that have a relative jump target.

Deprecated since version 3.13: All jumps are now relative. Use [`hasjump`](https://docs.python.org/3/library/dis.html#dis.hasjump "dis.hasjump")
.

dis.hasjabs[¶](https://docs.python.org/3/library/dis.html#dis.hasjabs "Link to this definition")

Sequence of bytecodes that have an absolute jump target.

Deprecated since version 3.13: All jumps are now relative. This list is empty.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [`dis` — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html#)
    *   [Command-line interface](https://docs.python.org/3/library/dis.html#command-line-interface)
        
    *   [Bytecode analysis](https://docs.python.org/3/library/dis.html#bytecode-analysis)
        
    *   [Analysis functions](https://docs.python.org/3/library/dis.html#analysis-functions)
        
    *   [Python Bytecode Instructions](https://docs.python.org/3/library/dis.html#python-bytecode-instructions)
        
    *   [Opcode collections](https://docs.python.org/3/library/dis.html#opcode-collections)
        

#### Previous topic

[`compileall` — Byte-compile Python libraries](https://docs.python.org/3/library/compileall.html "previous chapter")

#### Next topic

[`pickletools` — Tools for pickle developers](https://docs.python.org/3/library/pickletools.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=dis+%E2%80%94+Disassembler+for+Python+bytecode&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Flibrary%2Fdis.html&pagesource=library%2Fdis.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/library/dis.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/library/pickletools.html "pickletools — Tools for pickle developers")
     |
*   [previous](https://docs.python.org/3/library/compileall.html "compileall — Byte-compile Python libraries")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [The Python standard library](https://docs.python.org/3/library/index.html)
     »
*   [Python Language Services](https://docs.python.org/3/library/language.html)
     »
*   [`dis` — Disassembler for Python bytecode](https://docs.python.org/3/library/dis.html)
    
*    
    
    |
*   Theme Auto Light Dark |