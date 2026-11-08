[Skip to main content](https://numpy.org/doc/stable/f2py/usage.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/f2py/usage.html)
[2.5 (stable)](https://numpy.org/doc/stable/f2py/usage.html)
[2.4](https://numpy.org/doc/2.4/f2py/usage.html)
[2.3](https://numpy.org/doc/2.3/f2py/usage.html)
[2.2](https://numpy.org/doc/2.2/f2py/usage.html)
[2.1](https://numpy.org/doc/2.1/f2py/usage.html)
[2.0](https://numpy.org/doc/2.0/f2py/usage.html)
[1.26](https://numpy.org/doc/1.26/f2py/usage.html)
[1.25](https://numpy.org/doc/1.25/f2py/usage.html)
[1.24](https://numpy.org/doc/1.24/f2py/usage.html)
[1.23](https://numpy.org/doc/1.23/f2py/usage.html)
[1.22](https://numpy.org/doc/1.22/f2py/usage.html)
[1.21](https://numpy.org/doc/1.21/f2py/usage.html)
[1.20](https://numpy.org/doc/1.20/f2py/usage.html)
[1.19](https://numpy.org/doc/1.19/f2py/usage.html)
[1.18](https://numpy.org/doc/1.18/f2py/usage.html)
[1.17](https://numpy.org/doc/1.17/f2py/usage.html)
[1.16](https://numpy.org/doc/1.16/f2py/usage.html)
[1.15](https://numpy.org/doc/1.15/f2py/usage.html)
[1.14](https://numpy.org/doc/1.14/f2py/usage.html)
[1.13](https://numpy.org/doc/1.13/f2py/usage.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Using F2PY[#](https://numpy.org/doc/stable/f2py/usage.html#using-f2py "Link to this heading")

==============================================================================================

This page contains a reference to all command-line options for the `f2py` command, as well as a reference to internal functions of the `numpy.f2py` module.

Using `f2py` as a command-line tool[#](https://numpy.org/doc/stable/f2py/usage.html#using-f2py-as-a-command-line-tool "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

When used as a command-line tool, `f2py` has three major modes, distinguished by the usage of `-c` and `-h` switches.

### 1\. Signature file generation[#](https://numpy.org/doc/stable/f2py/usage.html#signature-file-generation "Link to this heading")

To scan Fortran sources and generate a signature file, use

f2py \-h <filename.pyf> <options> <fortran files>   \\
  \[\[ only: <fortran functions>  : \]                \\\
    \[ skip: <fortran functions>  : \]\]...           \\
  \[<fortran files> ...\]

Copy to clipboard

Note

A Fortran source file can contain many routines, and it is often not necessary to allow all routines to be usable from Python. In such cases, either specify which routines should be wrapped (in the `only: .. :` part) or which routines F2PY should ignore (in the `skip: .. :` part).

F2PY has no concept of a “per-file” `skip` or `only` list, so if functions are listed in `only`, no other functions will be taken from any other files.

If `<filename.pyf>` is specified as `stdout`, then signatures are written to standard output instead of a file.

Among other options (see below), the following can be used in this mode:

`--overwrite-signature`

Overwrites an existing signature file.

### 2\. Extension module construction[#](https://numpy.org/doc/stable/f2py/usage.html#extension-module-construction "Link to this heading")

To construct an extension module, use

f2py \-m <modulename> <options> <fortran files>   \\
  \[\[ only: <fortran functions>  : \]              \\\
    \[ skip: <fortran functions>  : \]\]...          \\
  \[<fortran files> ...\]

Copy to clipboard

The constructed extension module is saved as `<modulename>module.c` to the current directory.

Here `<fortran files>` may also contain signature files. Among other options (see below), the following options can be used in this mode:

`--debug-capi`

Adds debugging hooks to the extension module. When using this extension module, various diagnostic information about the wrapper is written to the standard output, for example, the values of variables, the steps taken, etc.

`-include'<includefile>'`

Add a CPP `#include` statement to the extension module source. `<includefile>` should be given in one of the following forms

"filename.ext"
<filename.ext\>

Copy to clipboard

The include statement is inserted just before the wrapper functions. This feature enables using arbitrary C functions (defined in `<includefile>`) in F2PY generated wrappers.

Note

This option is deprecated. Use `usercode` statement to specify C code snippets directly in signature files.

`--[no-]wrap-functions`

Create Fortran subroutine wrappers to Fortran functions. `--wrap-functions` is default because it ensures maximum portability and compiler independence.

`--[no-]freethreading-compatible`

Create a module that declares it does or doesn’t require the GIL. The default is `--no-freethreading-compatible` for backwards compatibility. Inspect the fortran code you are wrapping for thread safety issues before passing `--freethreading-compatible`, as `f2py` does not analyze fortran code for thread safety issues.

`--include-paths "<path1>:<path2>..."`

Search include files from given directories.

Note

The paths are to be separated by the correct operating system separator [`pathsep`](https://docs.python.org/3/library/os.html#os.pathsep "(in Python v3.14)")
, that is `:` on Linux / MacOS and `;` on Windows. In `CMake` this corresponds to using `$<SEMICOLON>`.

### 3\. Building a module[#](https://numpy.org/doc/stable/f2py/usage.html#building-a-module "Link to this heading")

To build an extension module, use

f2py \-c <options> <fortran files>       \\
  \[\[ only: <fortran functions>  : \]     \\\
    \[ skip: <fortran functions>  : \]\]... \\
  \[ <fortran/c source files> \] \[ <.o, .a, .so files> \]

Copy to clipboard

If `<fortran files>` contains a signature file, then the source for an extension module is constructed, all Fortran and C sources are compiled, and finally all object and library files are linked to the extension module `<modulename>.so` which is saved into the current directory.

If `<fortran files>` does not contain a signature file, then an extension module is constructed by scanning all Fortran source codes for routine signatures, before proceeding to build the extension module.

Warning

`distutils` has been removed. Use environment variables or native files to interact with `meson` instead. See its [FAQ](https://mesonbuild.com/howtox.html)
 for more information.

Among other options (see below) and options described for previous modes, the following can be used.

Note

Changed in version 2.5.0: The `distutils` backend has been removed.

Common build flags:

`--backend <backend_type>`

Legacy option, only `meson` is supported.

`--f77flags=<string>`

Specify F77 compiler flags

`--f90flags=<string>`

Specify F90 compiler flags

`--debug`

Compile with debugging information

`-l<libname>`

Use the library `<libname>` when linking.

`-D<macro>[=<defn=1>]`

Define macro `<macro>` as `<defn>`.

`-U<macro>`

Define macro `<macro>`

`-I<dir>`

Append directory `<dir>` to the list of directories searched for include files.

`-L<dir>`

Add directory `<dir>` to the list of directories to be searched for `-l`.

`--dep <dependency>`

Specify a meson dependency for the module. This may be passed multiple times for multiple dependencies. Dependencies are stored in a list for further processing. Example: `--dep lapack --dep scalapack` This will identify “lapack” and “scalapack” as dependencies and remove them from argv, leaving a dependencies list containing \[“lapack”, “scalapack”\].

Note

The `f2py -c` option must be applied either to an existing `.pyf` file (plus the source/object/library files) or one must specify the `-m <modulename>` option (plus the sources/object/library files). Use one of the following options:

f2py \-c \-m fib1 fib1.f

Copy to clipboard

or

f2py \-m fib1 fib1.f \-h fib1.pyf
f2py \-c fib1.pyf fib1.f

Copy to clipboard

For more information, see the [Building C and C++ Extensions](https://docs.python.org/3/extending/building.html)
 Python documentation for details.

When building an extension module, a combination of the following macros may be required for non-gcc Fortran compilers:

\-DPREPEND\_FORTRAN
-DNO\_APPEND\_FORTRAN
-DUPPERCASE\_FORTRAN

Copy to clipboard

To test the performance of F2PY generated interfaces, use `-DF2PY_REPORT_ATEXIT`. Then a report of various timings is printed out at the exit of Python. This feature may not work on all platforms, and currently only Linux is supported.

To see whether F2PY generated interface performs copies of array arguments, use `-DF2PY_REPORT_ON_ARRAY_COPY=<int>`. When the size of an array argument is larger than `<int>`, a message about the copying is sent to `stderr`.

### Other options[#](https://numpy.org/doc/stable/f2py/usage.html#other-options "Link to this heading")

`-m <modulename>`

Name of an extension module. Default is `untitled`.

Warning

Don’t use this option if a signature file (`*.pyf`) is used.

Changed in version 1.26.3: Will ignore `-m` if a `pyf` file is provided.

`--[no-]lower`

Do \[not\] lower the cases in `<fortran files>`. By default, `--lower` is assumed with `-h` switch, and `--no-lower` without the `-h` switch.

`-include<header>`

Writes additional headers in the C wrapper, can be passed multiple times, generates #include <header> each time. Note that this is meant to be passed in single quotes and without spaces, for example `'-include<stdbool.h>'`

`--build-dir <dirname>`

All F2PY generated files are created in `<dirname>`. Default is `tempfile.mkdtemp()`.

`--f2cmap <filename>`

Load Fortran-to-C `KIND` specifications from the given file.

`--quiet`

Run quietly.

`--verbose`

Run with extra verbosity.

`--skip-empty-wrappers`

Do not generate wrapper files unless required by the inputs. This is a backwards compatibility flag to restore pre 1.22.4 behavior.

`-v`

Print the F2PY version and exit.

Execute `f2py` without any options to get an up-to-date list of available options.

Python module `numpy.f2py`[#](https://numpy.org/doc/stable/f2py/usage.html#python-module-numpy-f2py "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Warning

Changed in version 2.0.0: There used to be a `f2py.compile` function, which was removed, users may wrap `python -m numpy.f2py` via `subprocess.run` manually, and set environment variables to interact with `meson` as required.

When using `numpy.f2py` as a module, the following functions can be invoked.

Fortran to Python Interface Generator.

Copyright 1999 – 2011 Pearu Peterson all rights reserved. Copyright 2011 – present NumPy Developers. Permission to use, modify, and distribute this software is given under the terms of the NumPy License.

NO WARRANTY IS EXPRESSED OR IMPLIED. USE AT YOUR OWN RISK.

numpy.f2py.get\_include()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/f2py/__init__.py#L25-L63)
[#](https://numpy.org/doc/stable/f2py/usage.html#numpy.f2py.get_include "Link to this definition")

Return the directory that contains the `fortranobject.c` and `.h` files.

Python extension modules built with f2py-generated code need to use `fortranobject.c` as a source file, and include the `fortranobject.h` header. This function can be used to obtain the directory containing both of these files.

Returns:

**include\_path**str

Absolute path to the directory containing `fortranobject.c` and `fortranobject.h`.

See also

[`numpy.get_include`](https://numpy.org/doc/stable/reference/generated/numpy.get_include.html#numpy.get_include "numpy.get_include")

function that returns the numpy include directory

Notes

New in version 1.21.1.

Unless the build system you are using has specific support for f2py, building a Python extension using a `.pyf` signature file is a two-step process. For a module `mymod`:

*   Step 1: run `python -m numpy.f2py mymod.pyf --quiet`. This generates `mymodmodule.c` and (if needed) `mymod-f2pywrappers.f` files next to `mymod.pyf`.
    
*   Step 2: build your Python extension module. This requires the following source files:
    
    *   `mymodmodule.c`
        
    *   `mymod-f2pywrappers.f` (if it was generated in Step 1)
        
    *   `fortranobject.c`
        

numpy.f2py.run\_main(_comline\_list_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/f2py/f2py2e.py#L426-L511)
[#](https://numpy.org/doc/stable/f2py/usage.html#numpy.f2py.run_main "Link to this definition")

Equivalent to running:

f2py <args\>

Copy to clipboard

where `<args>=string.join(<list>,' ')`, but in Python. Unless `-h` is used, this function returns a dictionary containing information on generated modules and their dependencies on source files.

You cannot build extension modules with this function, that is, using `-c` is not allowed. Use the `compile` command instead.

Examples

Try it in your browser!

The command `f2py -m scalar scalar.f` can be executed from Python as follows.

\>>> import numpy.f2py
\>>> r \= numpy.f2py.run\_main(\['-m','scalar','doc/source/f2py/scalar.f'\])
Reading fortran codes...
        Reading file 'doc/source/f2py/scalar.f' (format:fix,strict)
Post-processing...
        Block: scalar
                        Block: FOO
Building modules...
        Building module "scalar"...
        Wrote C/API module "scalar" to file "./scalarmodule.c"
\>>> print(r)
{'scalar': {'h': \['/home/users/pearu/src\_cvs/f2py/src/fortranobject.h'\],
	 'csrc': \['./scalarmodule.c', \
                  '/home/users/pearu/src\_cvs/f2py/src/fortranobject.c'\]}}

Copy to clipboard

Go BackOpen In Tab

Building with Meson (Examples)[#](https://numpy.org/doc/stable/f2py/usage.html#building-with-meson-examples "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

### Using f2py with Meson[#](https://numpy.org/doc/stable/f2py/usage.html#using-f2py-with-meson "Link to this heading")

Meson is a modern build system recommended for building Python extension modules, especially starting with Python 3.12 and NumPy 2.x. Meson provides a robust and maintainable way to build Fortran extensions with f2py.

To build a Fortran extension using f2py and Meson, you can use Meson’s `custom_target` to invoke f2py and generate the extension module. The following minimal example demonstrates how to do this:

This example shows how to build the `add` extension from the `add.f` and `add.pyf` files described in the [F2PY examples](https://numpy.org/doc/stable/f2py/f2py-examples.html#f2py-examples)
 (note that you do not always need a `.pyf` file: in many cases `f2py` can figure out the annotations by itself).

Project layout:

f2py\_examples/
  meson.build
  add.f
  add.pyf (optional)
  \_\_init\_\_.py  (can be empty)

Copy to clipboard

Example `meson.build`:

project('f2py\_examples', 'fortran')

py \= import('python').find\_installation()

\# List your Fortran source files
sources \= files('add.pyf', 'add.f')

\# Build the extension by invoking f2py via a custom target
add\_mod \= custom\_target(
  'add\_extension',
  input: sources,
  output: \['add' + py.extension\_suffix()\],
  command: \[\
    py.full\_path(), '-m', 'numpy.f2py',\
    '-c', 'add.pyf', 'add.f',\
    '-m', 'add'\
  \],
  build\_by\_default: true
)

\# Install into site-packages under the f2py\_examples package
install\_subdir('.', install\_dir: join\_paths(py.site\_packages\_dir(), 'f2py\_examples'),
               strip\_directory: false,
               exclude\_files: \['meson.build'\])

\# Also install the built extension (place it beside \_\_init\_\_.py)
install\_data(add\_mod, install\_dir: join\_paths(py.site\_packages\_dir(), 'f2py\_examples'))

Copy to clipboard

For more details and advanced usage, see the Meson build guide in the user documentation or refer to SciPy’s Meson build files for real-world examples: [scipy/scipy](https://github.com/scipy/scipy/tree/main/meson.build)

On this page