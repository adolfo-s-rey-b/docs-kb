### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/refcounting.html "Reference Counting")
     |
*   [previous](https://docs.python.org/3/c-api/stable.html "C API and ABI Stability")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [The Very High Level Layer](https://docs.python.org/3/c-api/veryhigh.html)
    
*    
    
    |
*   Theme Auto Light Dark |

The Very High Level Layer[¶](https://docs.python.org/3/c-api/veryhigh.html#the-very-high-level-layer "Link to this heading")

=============================================================================================================================

The functions in this chapter will let you execute Python source code given in a file or a buffer, but they will not let you interact in a more detailed way with the interpreter.

Several of these functions accept a start symbol from the grammar as a parameter. The available start symbols are [`Py_eval_input`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_eval_input "Py_eval_input")
, [`Py_file_input`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_file_input "Py_file_input")
, [`Py_single_input`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_single_input "Py_single_input")
, and [`Py_func_type_input`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_func_type_input "Py_func_type_input")
. These are described following the functions which accept them as parameters.

Note also that several of these functions take FILE\* parameters. One particular issue which needs to be handled carefully is that the `FILE` structure for different C libraries can be different and incompatible. Under Windows (at least), it is possible for dynamically linked extensions to actually use different libraries, so care should be taken that FILE\* parameters are only passed to these functions if it is certain that they were created by the same library that the Python runtime is using.

int PyRun\_AnyFile(FILE \*fp, const char \*filename)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_AnyFile "Link to this definition")
  

This is a simplified interface to [`PyRun_AnyFileExFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_AnyFileExFlags "PyRun_AnyFileExFlags")
 below, leaving _closeit_ set to `0` and _flags_ set to `NULL`.

int PyRun\_AnyFileFlags(FILE \*fp, const char \*filename, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_AnyFileFlags "Link to this definition")
  

This is a simplified interface to [`PyRun_AnyFileExFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_AnyFileExFlags "PyRun_AnyFileExFlags")
 below, leaving the _closeit_ argument set to `0`.

int PyRun\_AnyFileEx(FILE \*fp, const char \*filename, int closeit)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_AnyFileEx "Link to this definition")
  

This is a simplified interface to [`PyRun_AnyFileExFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_AnyFileExFlags "PyRun_AnyFileExFlags")
 below, leaving the _flags_ argument set to `NULL`.

int PyRun\_AnyFileExFlags(FILE \*fp, const char \*filename, int closeit, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_AnyFileExFlags "Link to this definition")
  

If _fp_ refers to a file associated with an interactive device (console or terminal input or Unix pseudo-terminal), return the value of [`PyRun_InteractiveLoop()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_InteractiveLoop "PyRun_InteractiveLoop")
, otherwise return the result of [`PyRun_SimpleFile()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleFile "PyRun_SimpleFile")
. _filename_ is decoded from the filesystem encoding ([`sys.getfilesystemencoding()`](https://docs.python.org/3/library/sys.html#sys.getfilesystemencoding "sys.getfilesystemencoding")
). If _filename_ is `NULL`, this function uses `"???"` as the filename. If _closeit_ is true, the file is closed before `PyRun_SimpleFileExFlags()` returns.

int PyRun\_SimpleString(const char \*command)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleString "Link to this definition")
  

This is a simplified interface to [`PyRun_SimpleStringFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleStringFlags "PyRun_SimpleStringFlags")
 below, leaving the [`PyCompilerFlags`](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
\* argument set to `NULL`.

int PyRun\_SimpleStringFlags(const char \*command, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleStringFlags "Link to this definition")
  

Executes the Python source code from _command_ in the [`__main__`](https://docs.python.org/3/library/__main__.html#module-__main__ "__main__: The environment where top-level code is run. Covers command-line interfaces, import-time behavior, and ``__name__ == '__main__'``.")
 module according to the _flags_ argument. If `__main__` does not already exist, it is created. Returns `0` on success or `-1` if an exception was raised. If there was an error, there is no way to get the exception information. For the meaning of _flags_, see below.

Note that if an otherwise unhandled [`SystemExit`](https://docs.python.org/3/builtins/exceptions.html#SystemExit "SystemExit")
 is raised, this function will not return `-1`, but exit the process, as long as [`PyConfig.inspect`](https://docs.python.org/3/c-api/init_config.html#c.PyConfig.inspect "PyConfig.inspect")
 is zero.

int PyRun\_SimpleFile(FILE \*fp, const char \*filename)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleFile "Link to this definition")
  

This is a simplified interface to [`PyRun_SimpleFileExFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleFileExFlags "PyRun_SimpleFileExFlags")
 below, leaving _closeit_ set to `0` and _flags_ set to `NULL`.

int PyRun\_SimpleFileEx(FILE \*fp, const char \*filename, int closeit)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleFileEx "Link to this definition")
  

This is a simplified interface to [`PyRun_SimpleFileExFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleFileExFlags "PyRun_SimpleFileExFlags")
 below, leaving _flags_ set to `NULL`.

int PyRun\_SimpleFileExFlags(FILE \*fp, const char \*filename, int closeit, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleFileExFlags "Link to this definition")
  

Similar to [`PyRun_SimpleStringFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_SimpleStringFlags "PyRun_SimpleStringFlags")
, but the Python source code is read from _fp_ instead of an in-memory string. _filename_ should be the name of the file, it is decoded from [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
. If _closeit_ is true, the file is closed before `PyRun_SimpleFileExFlags()` returns.

Note

On Windows, _fp_ should be opened as binary mode (e.g. `fopen(filename, "rb")`). Otherwise, Python may not handle script file with LF line ending correctly.

int PyRun\_InteractiveOneObject(FILE \*fp, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filename, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_InteractiveOneObject "Link to this definition")
  

Read and execute a single statement from a file associated with an interactive device according to the _flags_ argument. The user will be prompted using `sys.ps1` and `sys.ps2`. _filename_ must be a Python [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object.

Returns `0` when the input was executed successfully, `-1` if there was an exception, or an error code from the `errcode.h` include file distributed as part of Python if there was a parse error. (Note that `errcode.h` is not included by `Python.h`, so must be included specifically if needed.)

int PyRun\_InteractiveOne(FILE \*fp, const char \*filename)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_InteractiveOne "Link to this definition")
  

This is a simplified interface to [`PyRun_InteractiveOneFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_InteractiveOneFlags "PyRun_InteractiveOneFlags")
 below, leaving _flags_ set to `NULL`.

int PyRun\_InteractiveOneFlags(FILE \*fp, const char \*filename, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_InteractiveOneFlags "Link to this definition")
  

Similar to [`PyRun_InteractiveOneObject()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_InteractiveOneObject "PyRun_InteractiveOneObject")
, but _filename_ is a const char\*, which is decoded from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
.

int PyRun\_InteractiveLoop(FILE \*fp, const char \*filename)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_InteractiveLoop "Link to this definition")
  

This is a simplified interface to [`PyRun_InteractiveLoopFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_InteractiveLoopFlags "PyRun_InteractiveLoopFlags")
 below, leaving _flags_ set to `NULL`.

int PyRun\_InteractiveLoopFlags(FILE \*fp, const char \*filename, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_InteractiveLoopFlags "Link to this definition")
  

Read and execute statements from a file associated with an interactive device until EOF is reached. The user will be prompted using `sys.ps1` and `sys.ps2`. _filename_ is decoded from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
. Returns `0` at EOF or a negative number upon failure.

int (\*PyOS\_InputHook)(void)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_InputHook "Link to this definition")
  

_Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Can be set to point to a function with the prototype `int func(void)`. The function will be called when Python’s interpreter prompt is about to become idle and wait for user input from the terminal. The return value is ignored. Overriding this hook can be used to integrate the interpreter’s prompt with other event loops, as done in `Modules/_tkinter.c` in the Python source code.

The function is called without an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

Changed in version 3.12: This function is only called from the [main interpreter](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)
.

char \*(\*PyOS\_ReadlineFunctionPointer)(FILE\*, FILE\*, const char\*)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer "Link to this definition")
  

Can be set to point to a function with the prototype `char *func(FILE *stdin, FILE *stdout, const char *prompt)`, overriding the default function used to read a single line of input at the interpreter’s prompt. The function is expected to output the string _prompt_ if it’s not `NULL`, and then read a line of input from the provided standard input file, returning the resulting string. For example, the [`readline`](https://docs.python.org/3/library/readline.html#module-readline "readline: GNU readline support for Python.")
 module sets this hook to provide line-editing and tab-completion features.

The function is called without an [attached thread state](https://docs.python.org/3/glossary.html#term-attached-thread-state)
.

If this pointer is `NULL`, [`PyOS_Readline()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_Readline "PyOS_Readline")
 sets it to the default implementation, `PyOS_Readline()`, before reading input.

The returned string must be null-terminated and include the trailing newline, if one was read. Return an empty string if the end of the file is reached before any characters are read. Return `NULL` on failure or interruption; a Python exception may be set.

A non-`NULL` result must be a string allocated by [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
 or [`PyMem_RawRealloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawRealloc "PyMem_RawRealloc")
.

Changed in version 3.4: The result must be allocated by [`PyMem_RawMalloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawMalloc "PyMem_RawMalloc")
 or [`PyMem_RawRealloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_RawRealloc "PyMem_RawRealloc")
, instead of being allocated by [`PyMem_Malloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Malloc "PyMem_Malloc")
 or [`PyMem_Realloc()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Realloc "PyMem_Realloc")
.

Changed in version 3.12: This function is only called from the [main interpreter](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)
.

char \*PyOS\_Readline(FILE \*sys\_stdin, FILE \*sys\_stdout, const char \*prompt)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_Readline "Link to this definition")
  

Display _prompt_, if it is not `NULL`, and read a line from _sys\_stdin_. If both streams are terminals and the call is made from the [main interpreter](https://docs.python.org/3/c-api/subinterpreters.html#sub-interpreter-support)
, use [`PyOS_ReadlineFunctionPointer`](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer "PyOS_ReadlineFunctionPointer")
. Otherwise, use the default implementation, which flushes _sys\_stdout_ and writes _prompt_ to the C standard error stream.

The returned string follows the contract of [`PyOS_ReadlineFunctionPointer`](https://docs.python.org/3/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer "PyOS_ReadlineFunctionPointer")
, but the caller must free it with [`PyMem_Free()`](https://docs.python.org/3/c-api/memory.html#c.PyMem_Free "PyMem_Free")
. Return `NULL` on failure or interruption; a Python exception may be set.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyRun\_String(const char \*str, int start, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_String "Link to this definition")
  

_Return value: New reference._

This is a simplified interface to [`PyRun_StringFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_StringFlags "PyRun_StringFlags")
 below, leaving _flags_ set to `NULL`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyRun\_StringFlags(const char \*str, int start, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_StringFlags "Link to this definition")
  

_Return value: New reference._

Execute Python source code from _str_ in the context specified by the objects _globals_ and _locals_ with the compiler flags specified by _flags_. _globals_ must be a dictionary; _locals_ can be any object that implements the mapping protocol. The parameter _start_ specifies the start symbol and must be one of the [available start symbols](https://docs.python.org/3/c-api/veryhigh.html#start-symbols)
.

Returns the result of executing the code as a Python object, or `NULL` if an exception was raised.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyRun\_File(FILE \*fp, const char \*filename, int start, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_File "Link to this definition")
  

_Return value: New reference._

This is a simplified interface to [`PyRun_FileExFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_FileExFlags "PyRun_FileExFlags")
 below, leaving _closeit_ set to `0` and _flags_ set to `NULL`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyRun\_FileEx(FILE \*fp, const char \*filename, int start, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals, int closeit)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_FileEx "Link to this definition")
  

_Return value: New reference._

This is a simplified interface to [`PyRun_FileExFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_FileExFlags "PyRun_FileExFlags")
 below, leaving _flags_ set to `NULL`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyRun\_FileFlags(FILE \*fp, const char \*filename, int start, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_FileFlags "Link to this definition")
  

_Return value: New reference._

This is a simplified interface to [`PyRun_FileExFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_FileExFlags "PyRun_FileExFlags")
 below, leaving _closeit_ set to `0`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyRun\_FileExFlags(FILE \*fp, const char \*filename, int start, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals, int closeit, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_FileExFlags "Link to this definition")
  

_Return value: New reference._

Similar to [`PyRun_StringFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_StringFlags "PyRun_StringFlags")
, but the Python source code is read from _fp_ instead of an in-memory string. _filename_ should be the name of the file, it is decoded from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
. If _closeit_ is true, the file is closed before [`PyRun_FileExFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyRun_FileExFlags "PyRun_FileExFlags")
 returns.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_CompileString(const char \*str, const char \*filename, int start)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileString "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is a simplified interface to [`Py_CompileStringFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileStringFlags "Py_CompileStringFlags")
 below, leaving _flags_ set to `NULL`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_CompileStringFlags(const char \*str, const char \*filename, int start, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileStringFlags "Link to this definition")
  

_Return value: New reference._

This is a simplified interface to [`Py_CompileStringExFlags()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileStringExFlags "Py_CompileStringExFlags")
 below, with _optimize_ set to `-1`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_CompileStringObject(const char \*str, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*filename, int start, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags, int optimize)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileStringObject "Link to this definition")
  

_Return value: New reference._

Parse and compile the Python source code in _str_, returning the resulting code object. The start symbol is given by _start_; this can be used to constrain the code which can be compiled and should be [available start symbols](https://docs.python.org/3/c-api/veryhigh.html#start-symbols)
. The filename specified by _filename_ is used to construct the code object and may appear in tracebacks or [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
 exception messages. This returns `NULL` if the code cannot be parsed or compiled.

The integer _optimize_ specifies the optimization level of the compiler; a value of `-1` selects the optimization level of the interpreter as given by [`-O`](https://docs.python.org/3/using/cmdline.html#cmdoption-O)
 options. Explicit levels are `0` (no optimization; `__debug__` is true), `1` (asserts are removed, `__debug__` is false) or `2` (docstrings are removed too).

Added in version 3.4.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*Py\_CompileStringExFlags(const char \*str, const char \*filename, int start, [PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*flags, int optimize)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileStringExFlags "Link to this definition")
  

_Return value: New reference._

Like [`Py_CompileStringObject()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileStringObject "Py_CompileStringObject")
, but _filename_ is a byte string decoded from the [filesystem encoding and error handler](https://docs.python.org/3/glossary.html#term-filesystem-encoding-and-error-handler)
.

Added in version 3.2.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyEval\_EvalCode([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*co, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalCode "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is a simplified interface to [`PyEval_EvalCodeEx()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalCodeEx "PyEval_EvalCodeEx")
, with just the code object, and global and local variables. The other arguments are set to `NULL`.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyEval\_EvalCodeEx([PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*co, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*globals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*locals, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*const \*args, int argcount, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*const \*kws, int kwcount, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*const \*defs, int defcount, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*kwdefs, [PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*closure)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalCodeEx "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Evaluate a precompiled code object, given a particular environment for its evaluation. This environment consists of a dictionary of global variables, a mapping object of local variables, arrays of arguments, keywords and defaults, a dictionary of default values for [keyword-only](https://docs.python.org/3/glossary.html#keyword-only-parameter)
 arguments and a closure tuple of cells.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyEval\_EvalFrame([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*f)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalFrame "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

Evaluate an execution frame. This is a simplified interface to [`PyEval_EvalFrameEx()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalFrameEx "PyEval_EvalFrameEx")
, for backward compatibility.

[PyObject](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 \*PyEval\_EvalFrameEx([PyFrameObject](https://docs.python.org/3/c-api/frame.html#c.PyFrameObject "PyFrameObject")
 \*f, int throwflag)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_EvalFrameEx "Link to this definition")
  

_Return value: New reference._ _Part of the [Stable ABI](https://docs.python.org/3/c-api/stable.html#stable)
._

This is the main, unvarnished function of Python interpretation. The code object associated with the execution frame _f_ is executed, interpreting bytecode and executing calls as needed. The additional _throwflag_ parameter can mostly be ignored - if true, then it causes an exception to immediately be thrown; this is used for the [`throw()`](https://docs.python.org/3/builtins/stdtypes.html#generator.throw "generator.throw")
 methods of generator objects.

Changed in version 3.4: This function now includes a debug assertion to help ensure that it does not silently discard an active exception.

int PyEval\_MergeCompilerFlags([PyCompilerFlags](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "PyCompilerFlags")
 \*cf)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyEval_MergeCompilerFlags "Link to this definition")
  

This function changes the flags of the current evaluation frame, and returns true on success, false on failure.

struct PyCompilerFlags[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags "Link to this definition")
  

This is the structure used to hold compiler flags. In cases where code is only being compiled, it is passed as `int flags`, and in cases where code is being executed, it is passed as `PyCompilerFlags *flags`. In this case, `from __future__ import` can modify _flags_.

Whenever `PyCompilerFlags *flags` is `NULL`, [`cf_flags`](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags.cf_flags "PyCompilerFlags.cf_flags")
 is treated as equal to `0`, and any modification due to `from __future__ import` is discarded.

int cf\_flags[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags.cf_flags "Link to this definition")
  

Compiler flags.

int cf\_feature\_version[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags.cf_feature_version "Link to this definition")
  

_cf\_feature\_version_ is the minor Python version. It should be initialized to `PY_MINOR_VERSION`.

The field is ignored by default, it is used if and only if `PyCF_ONLY_AST` flag is set in [`cf_flags`](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompilerFlags.cf_flags "PyCompilerFlags.cf_flags")
.

Changed in version 3.8: Added _cf\_feature\_version_ field.

The available compiler flags are accessible as macros:

PyCF\_ALLOW\_TOP\_LEVEL\_AWAIT[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_ALLOW_TOP_LEVEL_AWAIT "Link to this definition")
  

PyCF\_ONLY\_AST[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_ONLY_AST "Link to this definition")
  

PyCF\_OPTIMIZED\_AST[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_OPTIMIZED_AST "Link to this definition")
  

PyCF\_TYPE\_COMMENTS[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_TYPE_COMMENTS "Link to this definition")
  

See [compiler flags](https://docs.python.org/3/library/ast.html#ast-compiler-flags)
 in documentation of the `ast` Python module, which exports these constants under the same names.

Low-level flags

The following flags and masks serve narrow needs of the standard library and interactive interpreters. Code outside the standard library rarely has a reason to use them. They are considered implementation details and may change at any time.

PyCF\_ALLOW\_INCOMPLETE\_INPUT[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_ALLOW_INCOMPLETE_INPUT "Link to this definition")
  

This flag is a private interface between the compiler and the [`codeop`](https://docs.python.org/3/library/codeop.html#module-codeop "codeop: Compile (possibly incomplete) Python code.")
 module. Do not use it; its behavior is unsupported and may change without warning.

With this flag set, when compilation fails because the source text ends where more input is expected, for example in the middle of an indented block or an unterminated string literal, the error raised is the undocumented `_IncompleteInputError`, a subclass of [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
. The [`codeop`](https://docs.python.org/3/library/codeop.html#module-codeop "codeop: Compile (possibly incomplete) Python code.")
 module sets this flag, together with [`PyCF_DONT_IMPLY_DEDENT`](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_DONT_IMPLY_DEDENT "PyCF_DONT_IMPLY_DEDENT")
, to tell input that is incomplete apart from input with a real syntax error, so that interactive interpreters know when to prompt for another line instead of reporting an error.

Added in version 3.11.

PyCF\_DONT\_IMPLY\_DEDENT[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_DONT_IMPLY_DEDENT "Link to this definition")
  

By default, when compiling with the [`Py_single_input`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_single_input "Py_single_input")
 start symbol, reaching the end of the source text implicitly closes any open indented blocks. With this flag set, open blocks are only closed if the last line of the source ends with a newline; otherwise, compilation fails with a [`SyntaxError`](https://docs.python.org/3/builtins/exceptions.html#SyntaxError "SyntaxError")
:

PyCompilerFlags flags \= {
    .cf\_flags \= 0,
    .cf\_feature\_version \= PY\_MINOR\_VERSION,
};
const char \*source \= "if a:\\n    pass";

/\* The "if" block is closed implicitly;
   this returns a code object: \*/
Py\_CompileStringFlags(source, "<input>", Py\_single\_input, &flags);

/\* With the flag, this fails with a SyntaxError,
   because the last line does not end with a newline: \*/
flags.cf\_flags \= PyCF\_DONT\_IMPLY\_DEDENT;
Py\_CompileStringFlags(source, "<input>", Py\_single\_input, &flags);

The [`codeop`](https://docs.python.org/3/library/codeop.html#module-codeop "codeop: Compile (possibly incomplete) Python code.")
 module uses this flag to detect incomplete interactive input. While the user is still typing inside an indented block, the source does not yet end with a newline, so it fails to compile and the user is prompted for another line.

PyCF\_IGNORE\_COOKIE[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_IGNORE_COOKIE "Link to this definition")
  

Read the source text as UTF-8, ignoring its [**PEP 263**](https://peps.python.org/pep-0263/)
 encoding declaration (“coding cookie”), if any:

PyCompilerFlags flags \= {
    .cf\_flags \= 0,
    .cf\_feature\_version \= PY\_MINOR\_VERSION,
};
const char \*source \= "# coding: latin-1\\ns = '\\xe9'\\n";

/\* The coding cookie is honored: byte 0xE9 is decoded as
   Latin-1, and this returns a code object that sets s to "é": \*/
Py\_CompileStringFlags(source, "<input>", Py\_file\_input, &flags);

/\* With the flag, the cookie is ignored and compilation fails
   with a SyntaxError, because 0xE9 is not valid UTF-8: \*/
flags.cf\_flags \= PyCF\_IGNORE\_COOKIE;
Py\_CompileStringFlags(source, "<input>", Py\_file\_input, &flags);

The [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
, [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
 and [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 built-in functions set this flag when the source is a [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 object, because they pass the text to the parser encoded as UTF-8.

PyCF\_SOURCE\_IS\_UTF8[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_SOURCE_IS_UTF8 "Link to this definition")
  

Mark the source text as known to be UTF-8 encoded. The [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
, [`eval()`](https://docs.python.org/3/builtins/functions.html#eval "eval")
 and [`exec()`](https://docs.python.org/3/builtins/functions.html#exec "exec")
 built-in functions set this flag, but it currently has no effect.

The “`PyCF`” flags above can be combined with “`CO_FUTURE`” flags such as [`CO_FUTURE_ANNOTATIONS`](https://docs.python.org/3/c-api/code.html#c.CO_FUTURE_ANNOTATIONS "CO_FUTURE_ANNOTATIONS")
 to enable features normally selectable using [future statements](https://docs.python.org/3/reference/simple_stmts.html#future)
. See [Code Object Flags](https://docs.python.org/3/c-api/code.html#c-codeobject-flags)
 for a complete list.

The following masks combine several flags:

PyCF\_MASK[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_MASK "Link to this definition")
  

Bitmask of all `CO_FUTURE` flags (see [Code Object Flags](https://docs.python.org/3/c-api/code.html#c-codeobject-flags)
), which select features normally enabled by [future statements](https://docs.python.org/3/reference/simple_stmts.html#future)
. When code compiled with a `PyCompilerFlags *flags` argument contains a `from __future__ import` statement, the flag for the imported feature is added to _flags_, so that code executed later in the same context inherits it.

PyCF\_MASK\_OBSOLETE[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_MASK_OBSOLETE "Link to this definition")
  

Do not use this mask in new code. It is kept only so that old code passing its flags to [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
 keeps working.

Bitmask of flags for obsolete future features that no longer have any effect.

PyCF\_COMPILE\_MASK[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_COMPILE_MASK "Link to this definition")
  

Bitmask of all `PyCF` flags that change how the source is compiled, such as [`PyCF_ONLY_AST`](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_ONLY_AST "PyCF_ONLY_AST")
. The [`compile()`](https://docs.python.org/3/builtins/functions.html#compile "compile")
 built-in function uses this mask to validate its _flags_ argument.

Available start symbols[¶](https://docs.python.org/3/c-api/veryhigh.html#available-start-symbols "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

int Py\_eval\_input[¶](https://docs.python.org/3/c-api/veryhigh.html#c.Py_eval_input "Link to this definition")
  

The start symbol from the Python grammar for isolated expressions; for use with [`Py_CompileString()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileString "Py_CompileString")
.

int Py\_file\_input[¶](https://docs.python.org/3/c-api/veryhigh.html#c.Py_file_input "Link to this definition")
  

The start symbol from the Python grammar for sequences of statements as read from a file or other source; for use with [`Py_CompileString()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileString "Py_CompileString")
. This is the symbol to use when compiling arbitrarily long Python source code.

int Py\_single\_input[¶](https://docs.python.org/3/c-api/veryhigh.html#c.Py_single_input "Link to this definition")
  

The start symbol from the Python grammar for a single statement; for use with [`Py_CompileString()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileString "Py_CompileString")
. This is the symbol used for the interactive interpreter loop.

int Py\_func\_type\_input[¶](https://docs.python.org/3/c-api/veryhigh.html#c.Py_func_type_input "Link to this definition")
  

The start symbol from the Python grammar for a function type; for use with [`Py_CompileString()`](https://docs.python.org/3/c-api/veryhigh.html#c.Py_CompileString "Py_CompileString")
. This is used to parse “signature type comments” from [**PEP 484**](https://peps.python.org/pep-0484/)
.

This requires the [`PyCF_ONLY_AST`](https://docs.python.org/3/c-api/veryhigh.html#c.PyCF_ONLY_AST "PyCF_ONLY_AST")
 flag to be set.

See also

*   [`ast.FunctionType`](https://docs.python.org/3/library/ast.html#ast.FunctionType "ast.FunctionType")
    
*   [**PEP 484**](https://peps.python.org/pep-0484/)
    

Added in version 3.8.

Stack Effects[¶](https://docs.python.org/3/c-api/veryhigh.html#stack-effects "Link to this heading")

-----------------------------------------------------------------------------------------------------

See also

[`dis.stack_effect()`](https://docs.python.org/3/library/dis.html#dis.stack_effect "dis.stack_effect")

PY\_INVALID\_STACK\_EFFECT[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PY_INVALID_STACK_EFFECT "Link to this definition")
  

Sentinel value representing an invalid stack effect.

This is currently equivalent to `INT_MAX`.

Added in version 3.8.

int PyCompile\_OpcodeStackEffect(int opcode, int oparg)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompile_OpcodeStackEffect "Link to this definition")
  

Compute the stack effect of _opcode_ with argument _oparg_.

On success, this function returns the stack effect; on failure, this returns [`PY_INVALID_STACK_EFFECT`](https://docs.python.org/3/c-api/veryhigh.html#c.PY_INVALID_STACK_EFFECT "PY_INVALID_STACK_EFFECT")
.

Added in version 3.4.

int PyCompile\_OpcodeStackEffectWithJump(int opcode, int oparg, int jump)[¶](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompile_OpcodeStackEffectWithJump "Link to this definition")
  

Similar to [`PyCompile_OpcodeStackEffect()`](https://docs.python.org/3/c-api/veryhigh.html#c.PyCompile_OpcodeStackEffect "PyCompile_OpcodeStackEffect")
, but don’t include the stack effect of jumping if _jump_ is zero.

If _jump_ is `0`, this will not include the stack effect of jumping, but if _jump_ is `1` or `-1`, this will include it.

On success, this function returns the stack effect; on failure, this returns [`PY_INVALID_STACK_EFFECT`](https://docs.python.org/3/c-api/veryhigh.html#c.PY_INVALID_STACK_EFFECT "PY_INVALID_STACK_EFFECT")
.

Added in version 3.8.

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [The Very High Level Layer](https://docs.python.org/3/c-api/veryhigh.html#)
    *   [Available start symbols](https://docs.python.org/3/c-api/veryhigh.html#available-start-symbols)
        
    *   [Stack Effects](https://docs.python.org/3/c-api/veryhigh.html#stack-effects)
        

#### Previous topic

[C API and ABI Stability](https://docs.python.org/3/c-api/stable.html "previous chapter")

#### Next topic

[Reference Counting](https://docs.python.org/3/c-api/refcounting.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=The+Very+High+Level+Layer&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fc-api%2Fveryhigh.html&pagesource=c-api%2Fveryhigh.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/c-api/veryhigh.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/c-api/refcounting.html "Reference Counting")
     |
*   [previous](https://docs.python.org/3/c-api/stable.html "C API and ABI Stability")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Python/C API reference manual](https://docs.python.org/3/c-api/index.html)
     »
*   [The Very High Level Layer](https://docs.python.org/3/c-api/veryhigh.html)
    
*    
    
    |
*   Theme Auto Light Dark |