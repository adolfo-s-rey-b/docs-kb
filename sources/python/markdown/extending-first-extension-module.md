### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/extending.html "Using the C API: Assorted topics")
     |
*   [previous](https://docs.python.org/3/extending/index.html "Extending and Embedding the Python Interpreter")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)
     »
*   [Your first C API extension module](https://docs.python.org/3/extending/first-extension-module.html)
    
*    
    
    |
*   Theme Auto Light Dark |

Your first C API extension module[¶](https://docs.python.org/3/extending/first-extension-module.html#your-first-c-api-extension-module "Link to this heading")

===============================================================================================================================================================

This tutorial will take you through creating a simple Python extension module written in C or C++.

We will use the low-level Python C API directly. For easier ways to create extension modules, see the [recommended third party tools](https://docs.python.org/3/c-api/intro.html#c-api-tools)
.

The tutorial assumes basic knowledge about Python: you should be able to define functions in Python code before starting to write them in C. See [The Python Tutorial](https://docs.python.org/3/tutorial/index.html#tutorial-index)
 for an introduction to Python itself.

The tutorial should be approachable for anyone who can write a basic C library. While we will mention several concepts that a C beginner would not be expected to know, like `static` functions or linkage declarations, understanding these is not necessary for success.

We will focus on giving you a “feel” of what Python’s C API is like. It will not teach you important concepts, like error handling and reference counting, which are covered in later chapters.

We will assume that you use a Unix-like system (including macOS and Linux), or Windows. On other systems, you might need to adjust some details – for example, a system command name.

You need to have a suitable C compiler and Python development headers installed. On Linux, headers are often in a package like `python3-dev` or `python3-devel`.

You need to be able to install Python packages. This tutorial uses [pip](https://pip.pypa.io/)
 (`pip install`), but you can substitute any tool that can build and install `pyproject.toml`\-based projects, like [uv](https://docs.astral.sh/uv/)
 (`uv pip install`). Preferably, have a [virtual environment](https://docs.python.org/3/library/venv.html#venv-def)
 activated.

Note

This tutorial uses APIs that were added in CPython 3.15. To create an extension that’s compatible with earlier versions of CPython, please follow an earlier version of this documentation.

This tutorial uses C syntax added in C11 and C++20. If your extension needs to be compatible with earlier standards, please follow tutorials in documentation for Python 3.14 or below.

What we’ll do[¶](https://docs.python.org/3/extending/first-extension-module.html#what-we-ll-do "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

Let’s create an extension module called `spam` [\[1\]](https://docs.python.org/3/extending/first-extension-module.html#why-spam)
, which will include a Python interface to the C standard library function `system()`. This function is defined in `stdlib.h`. It takes a C string as argument, runs the argument as a system command, and returns a result value as an integer. A manual page for `system()` might summarize it this way:

#include <stdlib.h>
int system(const char \*command);

Note that like many functions in the C standard library, this function is already exposed in Python. In production, use [`os.system()`](https://docs.python.org/3/library/os.html#os.system "os.system")
 or [`subprocess.run()`](https://docs.python.org/3/library/subprocess.html#subprocess.run "subprocess.run")
 rather than the module you’ll write here.

We want this function to be callable from Python as follows:

Copy

\>>> import spam
\>>> status \= spam.system("whoami")
User Name
\>>> status
0

Note

The system command `whoami` prints out your username. It’s useful in tutorials like this one because it has the same name on both Unix and Windows.

Start with the headers[¶](https://docs.python.org/3/extending/first-extension-module.html#start-with-the-headers "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

Begin by creating a directory for this tutorial, and switching to it on the command line. Then, create a file named `spammodule.c` in your directory. [\[2\]](https://docs.python.org/3/extending/first-extension-module.html#why-spammodule)

In this file, we’ll include two headers: `Python.h` to pull in all declarations of the Python C API, and `stdlib.h` for the `system()` function. [\[3\]](https://docs.python.org/3/extending/first-extension-module.html#stdlib-h)

Add the following lines to `spammodule.c`:

#include <Python.h>
#include <stdlib.h>     // for system()

Be sure to put `stdlib.h`, and any other standard library includes, _after_ `Python.h`. On some systems, Python may define some pre-processor definitions that affect the standard headers.

Running your build tool[¶](https://docs.python.org/3/extending/first-extension-module.html#running-your-build-tool "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

With only the includes in place, your extension won’t do anything. Still, it’s a good time to compile it and try to import it. This will ensure that your build tool works, so that you can make and test incremental changes as you follow the rest of the text.

CPython itself does not come with a tool to build extension modules; it is recommended to use a third-party project for this. In this tutorial, we’ll use [meson-python](https://mesonbuild.com/meson-python/)
. (If you want to use another one, see [Appendix: Other build tools](https://docs.python.org/3/extending/first-extension-module.html#first-extension-other-tools)
.)

`meson-python` requires defining a “project” using two extra files.

First, add `pyproject.toml` with these contents:

\[build-system\]
build-backend \= 'mesonpy'
requires \= \['meson-python'\]

\[project\]
\# Placeholder project information
\# (change this before distributing the module)
name \= 'sampleproject'
version \= '0'

Then, create `meson.build` containing the following:

project('sampleproject', 'c')

py \= import('python').find\_installation(pure: false)

py.extension\_module(
   'spam',          \# name of the importable Python module
   'spammodule.c',  \# the C source file
   install: true,
)

Note

See the [meson-python documentation](https://mesonbuild.com/meson-python/)
 for details on configuration.

Now, build install the _project in the current directory_ (`.`) via `pip`:

Copy

python \-m pip \-v install .

The `-v` (`--verbose`) option causes `pip` to show the output from the compiler, which is often useful during development.

Tip

If you don’t have `pip` installed, run `python -m ensurepip`, preferably in a [virtual environment](https://docs.python.org/3/library/venv.html#venv-def)
. (Or, if you prefer another tool that can build and install `pyproject.toml`\-based projects, use that.)

Note that you will need to run this command again every time you change your extension. Unlike Python, C has an explicit compilation step.

When your extension is compiled and installed, start Python and try to import it. This should fail with the following exception:

Copy

\>>> import spam
Traceback (most recent call last):
   ...
ImportError: dynamic module does not define module export function (PyModExport\_spam or PyInit\_spam)

Module export hook[¶](https://docs.python.org/3/extending/first-extension-module.html#module-export-hook "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

The exception you got when you tried to import the module told you that Python is looking for a “module export function”, also known as a [module export hook](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
. Let’s define one.

First, add a prototype below the `#include` lines:

PyMODEXPORT\_FUNC PyModExport\_spam(void);

Tip

The prototype is not strictly necessary, but some modern compilers emit warnings without it. It’s generally better to add the prototype than to disable the warning.

The [`PyMODEXPORT_FUNC`](https://docs.python.org/3/c-api/extension-modules.html#c.PyMODEXPORT_FUNC "PyMODEXPORT_FUNC")
 macro declares the function’s return type, and adds any special linkage declarations needed to make the function visible and usable when CPython loads it.

After the prototype, add the function itself. For now, make it return `NULL`:

PyMODEXPORT\_FUNC
PyModExport\_spam(void)
{
   return NULL;
}

Compile and load the module again. You should get a different error this time.

Copy

\>>> import spam
Traceback (most recent call last):
   ...
SystemError: module export hook for module 'spam' failed without setting an exception

Simply returning `NULL` is _not_ correct behavior for an export hook, and CPython complains about it. That’s good – it means that CPython found the function! Let’s now make it do something useful.

The slot table[¶](https://docs.python.org/3/extending/first-extension-module.html#the-slot-table "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

Rather than `NULL`, the export hook should return the information needed to create a module. Let’s start with the basics: the name and docstring.

The information should be defined in an array of [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 entries, which are essentially key-value pairs. Define this array just before your export hook:

PyABIInfo\_VAR(abi\_info);

static PySlot spam\_slots\[\] \= {
   PySlot\_STATIC\_DATA(Py\_mod\_abi, &abi\_info),
   PySlot\_STATIC\_DATA(Py\_mod\_name, "spam"),
   PySlot\_STATIC\_DATA(Py\_mod\_doc, "A wonderful module with an example function"),
   PySlot\_END
};

The [`PySlot_STATIC_DATA`](https://docs.python.org/3/c-api/slots.html#c.PySlot_STATIC_DATA "PySlot_STATIC_DATA")
 macro is used when the slot value (here: `&abi_info`, `"spam"`, and the docstring) is a pointer to constant, statically allocated data.

The `PyABIInfo_VAR(abi_info);` macro and the [`Py_mod_abi`](https://docs.python.org/3/c-api/module.html#c.Py_mod_abi "Py_mod_abi")
 slot are a bit of boilerplate that helps prevent extensions compiled for a different version of Python from crashing the interpreter.

For both [`Py_mod_name`](https://docs.python.org/3/c-api/module.html#c.Py_mod_name "Py_mod_name")
 and [`Py_mod_doc`](https://docs.python.org/3/c-api/module.html#c.Py_mod_doc "Py_mod_doc")
, the values are C strings – that is, NUL-terminated, UTF-8 encoded byte arrays.

Note `PySlot_END` sentinel entry at the end. This marks the end of the array. If you forget it, you’ll trigger undefined behavior.

The array is defined as `static` – that is, not visible outside this `.c` file. This will be a common theme. CPython only needs to access the export hook; all global variables and all other functions should generally be `static`, so that they don’t clash with other extensions.

Return this array from your export hook instead of `NULL`:

PyMODEXPORT\_FUNC
PyModExport\_spam(void)
{
   return spam\_slots;
}

Now, recompile and try it out:

Copy

\>>> import spam
\>>> print(spam)
<module 'spam' from '/home/encukou/dev/cpython/spam.so'>

You have an extension module! Try `help(spam)` to see the docstring.

The next step will be adding a function.

Exposing a function[¶](https://docs.python.org/3/extending/first-extension-module.html#exposing-a-function "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

To expose the `system()` C function directly to Python, we’ll need to write a layer of glue code to convert arguments from Python objects to C values, and the C return value back to Python.

One of the simplest ways to write glue code is a “[`METH_O`](https://docs.python.org/3/c-api/structures.html#c.METH_O "METH_O")
” function, which takes two Python objects and returns one. All Python objects – regardless of the Python type – are represented in C as pointers to the [`PyObject`](https://docs.python.org/3/c-api/structures.html#c.PyObject "PyObject")
 structure.

Add such a function above the slots array:

static PyObject \*
spam\_system(PyObject \*self, PyObject \*arg)
{
   Py\_RETURN\_NONE;
}

For now, we ignore the arguments, and use the [`Py_RETURN_NONE`](https://docs.python.org/3/c-api/none.html#c.Py_RETURN_NONE "Py_RETURN_NONE")
 macro, which expands to a `return` statement that properly returns a Python [`None`](https://docs.python.org/3/builtins/constants.html#None "None")
 object.

Recompile your extension to make sure you don’t have syntax errors. We haven’t yet added `spam_system` to the module, so you might get a warning that `spam_system` is unused.

### Method definitions[¶](https://docs.python.org/3/extending/first-extension-module.html#method-definitions "Link to this heading")

To expose the C function to Python, you will need to provide several pieces of information in a structure called [`PyMethodDef`](https://docs.python.org/3/c-api/structures.html#c.PyMethodDef "PyMethodDef")
 [\[4\]](https://docs.python.org/3/extending/first-extension-module.html#why-pymethoddef)
:

*   `ml_name`: the name of the Python function;
    
*   `ml_doc`: a docstring;
    
*   `ml_meth`: the C function to be called; and
    
*   `ml_flags`: a set of flags describing details like how Python arguments are passed to the C function. We’ll use [`METH_O`](https://docs.python.org/3/c-api/structures.html#c.METH_O "METH_O")
     here – the flag that matches our `spam_system` function’s signature.
    

Because modules typically create several functions, these definitions need to be collected in an array, with a zero-filled sentinel at the end. Add this array just below the `spam_system` function:

static PyMethodDef spam\_methods\[\] \= {
    {
        .ml\_name\="system",
        .ml\_meth\=spam\_system,
        .ml\_flags\=METH\_O,
        .ml\_doc\="Execute a shell command.",
    },
    {NULL, NULL, 0, NULL}        /\* Sentinel \*/
};

As with module slots, a zero-filled sentinel marks the end of the array.

Next, we’ll add the method to the module. Add a [`Py_mod_methods`](https://docs.python.org/3/c-api/module.html#c.Py_mod_methods "Py_mod_methods")
 slot to your [`PySlot`](https://docs.python.org/3/c-api/slots.html#c.PySlot "PySlot")
 array:

PyABIInfo\_VAR(abi\_info);

static PySlot spam\_slots\[\] \= {
    PySlot\_STATIC\_DATA(Py\_mod\_abi, &abi\_info),    PySlot\_STATIC\_DATA(Py\_mod\_name, "spam"),
    PySlot\_STATIC\_DATA(Py\_mod\_doc, "A wonderful module with an example function"),
    PySlot\_STATIC\_DATA(Py\_mod\_methods, spam\_methods),
    PySlot\_END
};

Recompile your extension again, and test it. Be sure to restart the Python interpreter, so that `import spam` picks up the new version of the module.

You should now be able to call the function:

Copy

\>>> import spam
\>>> print(spam.system)
<built-in function system>
\>>> print(spam.system('whoami'))
None

Note that our `spam.system` does not yet run the `whoami` command; it only returns `None`.

Check that the function accepts exactly one argument, as specified by the [`METH_O`](https://docs.python.org/3/c-api/structures.html#c.METH_O "METH_O")
 flag:

Copy

\>>> print(spam.system('too', 'many', 'arguments'))
Traceback (most recent call last):
   ...
TypeError: spam.system() takes exactly one argument (3 given)

Returning an integer[¶](https://docs.python.org/3/extending/first-extension-module.html#returning-an-integer "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

Now, let’s take a look at the return value. Instead of `None`, we’ll want `spam.system` to return a number – that is, a Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 object. Eventually this will be the exit code of a system command, but let’s start with a fixed value, say, `3`.

The Python C API provides a function to create a Python [`int`](https://docs.python.org/3/builtins/functions.html#int "int")
 object from a C `int` value: [`PyLong_FromLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong "PyLong_FromLong")
. [\[5\]](https://docs.python.org/3/extending/first-extension-module.html#why-pylongfromlong)

To call it, replace the `Py_RETURN_NONE` with the following 3 lines:

static PyObject \*
spam\_system(PyObject \*self, PyObject \*arg)
{
   int status \= 3;   PyObject \*result \= PyLong\_FromLong(status);   return result;
}

Recompile, restart the Python interpreter again, and check that the function now returns 3:

Copy

\>>> import spam
\>>> spam.system('whoami')
3

Accepting a string[¶](https://docs.python.org/3/extending/first-extension-module.html#accepting-a-string "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

Finally, let’s handle the function argument.

Our C function, `spam_system()`, takes two arguments. The first one, `PyObject *self`, will be set to the `spam` module object. This isn’t useful in our case, so we’ll ignore it.

The other one, `PyObject *arg`, will be set to the object that the user passed from Python. We expect that it should be a Python string. In order to use the information in it, we will need to convert it to a C value – in this case, a C string (`const char *`).

There’s a slight type mismatch here: Python’s [`str`](https://docs.python.org/3/builtins/stdtypes.html#str "str")
 objects store Unicode text, but C strings are arrays of bytes. So, we’ll need to _encode_ the data, and we’ll use the UTF-8 encoding for it. (UTF-8 might not always be correct for system commands, but it’s what [`str.encode()`](https://docs.python.org/3/builtins/stdtypes.html#str.encode "str.encode")
 uses by default, and the C API has special support for it.)

The function to encode a Python string into a UTF-8 buffer is named [`PyUnicode_AsUTF8AndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize "PyUnicode_AsUTF8AndSize")
 [\[6\]](https://docs.python.org/3/extending/first-extension-module.html#why-pyunicodeasutf8)
. Call it like this:

static PyObject \*
spam\_system(PyObject \*self, PyObject \*arg)
{
   const char \*command \= PyUnicode\_AsUTF8AndSize(arg, NULL);   int status \= 3;
   PyObject \*result \= PyLong\_FromLong(status);
   return result;
}

If [`PyUnicode_AsUTF8AndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize "PyUnicode_AsUTF8AndSize")
 is successful, _command_ will point to the resulting C string – a zero-terminated array of bytes [\[7\]](https://docs.python.org/3/extending/first-extension-module.html#embedded-nul)
. This buffer is managed by the _arg_ object, which means we don’t need to free it, but we must follow some rules:

*   We should only use the buffer inside the `spam_system` function. After `spam_system` returns, _arg_ and the buffer it manages might be garbage-collected.
    
*   We must not modify it. This is why we use `const`.
    

If [`PyUnicode_AsUTF8AndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize "PyUnicode_AsUTF8AndSize")
 was _not_ successful, it returns a `NULL` pointer. When calling _any_ Python C API, we always need to handle such error cases. The way to do this in general is left for later chapters of this documentation. For now, be assured that we are already handling errors from [`PyLong_FromLong()`](https://docs.python.org/3/c-api/long.html#c.PyLong_FromLong "PyLong_FromLong")
 correctly.

For the [`PyUnicode_AsUTF8AndSize()`](https://docs.python.org/3/c-api/unicode.html#c.PyUnicode_AsUTF8AndSize "PyUnicode_AsUTF8AndSize")
 call, the correct way to handle errors is returning `NULL` from `spam_system`. Add an `if` block for this:

static PyObject \*
spam\_system(PyObject \*self, PyObject \*arg)
{
   const char \*command \= PyUnicode\_AsUTF8AndSize(arg, NULL);
   if (command \== NULL) {      return NULL;   }   int status \= 3;
   PyObject \*result \= PyLong\_FromLong(status);
   return result;
}

To test that error handling works, compile again, restart Python so that `import spam` picks up the new version of your module, and try passing a non-string value to your function:

Copy

\>>> import spam
\>>> spam.system(3)
Traceback (most recent call last):
   ...
TypeError: bad argument type for built-in operation

Now, all that is left is calling the C library function `system()` with the `char *` buffer, and using its result instead of the `3`:

static PyObject \*
spam\_system(PyObject \*self, PyObject \*arg)
{
   const char \*command \= PyUnicode\_AsUTF8AndSize(arg, NULL);
   if (command \== NULL) {
      return NULL;
   }
   int status \= system(command);   PyObject \*result \= PyLong\_FromLong(status);
   return result;
}

Compile your module, restart Python, and test. This time, you should see your username – the output of the `whoami` system command:

Copy

\>>> import spam
\>>> result \= spam.system('whoami')
User Name
\>>> result
0

You can also test with other commands, like `ls`, `dir`, or one that doesn’t exist:

Copy

\>>> import spam
\>>> result \= spam.system('nonexistent-command')
sh: line 1: nonexistent-command: command not found
\>>> result
32512

The result[¶](https://docs.python.org/3/extending/first-extension-module.html#the-result "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

Congratulations! You have written a complete Python C API extension module, and completed this tutorial!

Here is the entire source file, for your convenience:

/// Includes

#include <Python.h>
#include <stdlib.h>     // for system()

/// Implementation of spam.system

static PyObject \*
spam\_system(PyObject \*self, PyObject \*arg)
{
   const char \*command \= PyUnicode\_AsUTF8AndSize(arg, NULL);
   if (command \== NULL) {
      return NULL;
   }
   int status \= system(command);
   PyObject \*result \= PyLong\_FromLong(status);
   return result;
}

/// Module method table

static PyMethodDef spam\_methods\[\] \= {
    {
        .ml\_name\="system",
        .ml\_meth\=spam\_system,
        .ml\_flags\=METH\_O,
        .ml\_doc\="Execute a shell command.",
    },
    {NULL, NULL, 0, NULL}        /\* Sentinel \*/
};

/// Module slot table

PyABIInfo\_VAR(abi\_info);

static PySlot spam\_slots\[\] \= {
    PySlot\_STATIC\_DATA(Py\_mod\_abi, &abi\_info),
    PySlot\_STATIC\_DATA(Py\_mod\_name, "spam"),
    PySlot\_STATIC\_DATA(Py\_mod\_doc, "A wonderful module with an example function"),
    PySlot\_STATIC\_DATA(Py\_mod\_methods, spam\_methods),
    PySlot\_END
};

/// Export hook prototype

PyMODEXPORT\_FUNC PyModExport\_spam(void);

/// Module export hook

PyMODEXPORT\_FUNC
PyModExport\_spam(void)
{
   return spam\_slots;
}

Appendix: Other build tools[¶](https://docs.python.org/3/extending/first-extension-module.html#appendix-other-build-tools "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

You should be able to follow this tutorial – except the _Running your build tool_ section itself – with a build tool other than `meson-python`.

The Python Packaging User Guide has a [list of recommended tools](https://packaging.python.org/en/latest/guides/tool-recommendations/#build-backends-for-extension-modules)
; be sure to choose one for the C language.

### Workaround for missing PyInit function[¶](https://docs.python.org/3/extending/first-extension-module.html#workaround-for-missing-pyinit-function "Link to this heading")

If your build tool output complains about missing `PyInit_spam`, add the following function to your module for now:

// A workaround
void \*PyInit\_spam(void) { return NULL; }

This is a shim for an old-style [initialization function](https://docs.python.org/3/c-api/extension-modules.html#extension-export-hook)
, which was required in extension modules for CPython 3.14 and below. Current CPython does not need it, but some build tools may still assume that all extension modules need to define it.

If you use this workaround, you will get the exception `SystemError: initialization of spam failed without raising an exception` instead of `ImportError: dynamic module does not define module export function`.

### Compiling directly[¶](https://docs.python.org/3/extending/first-extension-module.html#compiling-directly "Link to this heading")

Using a third-party build tool is heavily recommended, as it will take care of various details of your platform and Python installation, of naming the resulting extension, and, later, of distributing your work.

If you are building an extension for as _specific_ system, or for yourself only, you might instead want to run your compiler directly. The way to do this is system-specific; be prepared for issues you will need to solve yourself.

#### Linux[¶](https://docs.python.org/3/extending/first-extension-module.html#linux "Link to this heading")

On Linux, the Python development package may include a `python3-config` command that prints out the required compiler flags. If you use it, check that it corresponds to the CPython interpreter you’ll use to load the module. Then, start with the following command:

Copy

gcc \--shared $(python3-config \--cflags \--ldflags) spammodule.c \-o spam.so

This should generate a `spam.so` file that you need to put in a directory on [`sys.path`](https://docs.python.org/3/library/sys.html#sys.path "sys.path")
.

Footnotes

### [Table of Contents](https://docs.python.org/3/contents.html)

*   [Your first C API extension module](https://docs.python.org/3/extending/first-extension-module.html#)
    *   [What we’ll do](https://docs.python.org/3/extending/first-extension-module.html#what-we-ll-do)
        
    *   [Start with the headers](https://docs.python.org/3/extending/first-extension-module.html#start-with-the-headers)
        
    *   [Running your build tool](https://docs.python.org/3/extending/first-extension-module.html#running-your-build-tool)
        
    *   [Module export hook](https://docs.python.org/3/extending/first-extension-module.html#module-export-hook)
        
    *   [The slot table](https://docs.python.org/3/extending/first-extension-module.html#the-slot-table)
        
    *   [Exposing a function](https://docs.python.org/3/extending/first-extension-module.html#exposing-a-function)
        *   [Method definitions](https://docs.python.org/3/extending/first-extension-module.html#method-definitions)
            
    *   [Returning an integer](https://docs.python.org/3/extending/first-extension-module.html#returning-an-integer)
        
    *   [Accepting a string](https://docs.python.org/3/extending/first-extension-module.html#accepting-a-string)
        
    *   [The result](https://docs.python.org/3/extending/first-extension-module.html#the-result)
        
    *   [Appendix: Other build tools](https://docs.python.org/3/extending/first-extension-module.html#appendix-other-build-tools)
        *   [Workaround for missing PyInit function](https://docs.python.org/3/extending/first-extension-module.html#workaround-for-missing-pyinit-function)
            
        *   [Compiling directly](https://docs.python.org/3/extending/first-extension-module.html#compiling-directly)
            *   [Linux](https://docs.python.org/3/extending/first-extension-module.html#linux)
                

#### Previous topic

[Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html "previous chapter")

#### Next topic

[Using the C API: Assorted topics](https://docs.python.org/3/extending/extending.html "next chapter")

### This page

*   [Report a bug](https://docs.python.org/3/bugs.html)
    
*   [Improve this page](https://docs.python.org/3/improve-page.html?pagetitle=Your+first+C+API+extension+module&pageurl=https%3A%2F%2Fdocs.python.org%2F3%2Fextending%2Ffirst-extension-module.html&pagesource=extending%2Ffirst-extension-module.rst)
    
*   [Show source](https://github.com/python/cpython/blob/3.15/Doc/extending/first-extension-module.rst?plain=1)
    

«

### Navigation

*   [index](https://docs.python.org/3/genindex.html "General Index")
    
*   [modules](https://docs.python.org/3/py-modindex.html "Python Module Index")
     |
*   [next](https://docs.python.org/3/extending/extending.html "Using the C API: Assorted topics")
     |
*   [previous](https://docs.python.org/3/extending/index.html "Extending and Embedding the Python Interpreter")
     |
*   ![Python logo](https://docs.python.org/3/_static/py.svg)
*   [Python](https://www.python.org/)
     »
*   German | DeutschGreek | ΕλληνικάEnglishSpanish | españolPersian | فارسیFrench | françaisItalian | italianoJapanese | 日本語Korean | 한국어Punjabi | ਪੰਜਾਬੀPolish | polskiBrazilian Portuguese | Português brasileiroRomanian | RomâneșteRussian | РусскийTurkish | TürkçeSimplified Chinese | 简体中文Traditional Chinese | 繁體中文
    
    dev (3.16)3.15.23.143.133.123.113.103.93.83.73.63.53.43.33.23.13.02.72.6
    

*   [3.15.2 documentation](https://docs.python.org/3/index.html)
     »
*   [Extending and Embedding the Python Interpreter](https://docs.python.org/3/extending/index.html)
     »
*   [Your first C API extension module](https://docs.python.org/3/extending/first-extension-module.html)
    
*    
    
    |
*   Theme Auto Light Dark |