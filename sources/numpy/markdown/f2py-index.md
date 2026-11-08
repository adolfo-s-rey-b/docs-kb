[Skip to main content](https://numpy.org/doc/stable/f2py/index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/f2py/index.html)
[2.5 (stable)](https://numpy.org/doc/stable/f2py/index.html)
[2.4](https://numpy.org/doc/2.4/f2py/index.html)
[2.3](https://numpy.org/doc/2.3/f2py/index.html)
[2.2](https://numpy.org/doc/2.2/f2py/index.html)
[2.1](https://numpy.org/doc/2.1/f2py/index.html)
[2.0](https://numpy.org/doc/2.0/f2py/index.html)
[1.26](https://numpy.org/doc/1.26/f2py/index.html)
[1.25](https://numpy.org/doc/1.25/f2py/index.html)
[1.24](https://numpy.org/doc/1.24/f2py/index.html)
[1.23](https://numpy.org/doc/1.23/f2py/index.html)
[1.22](https://numpy.org/doc/1.22/f2py/index.html)
[1.21](https://numpy.org/doc/1.21/f2py/index.html)
[1.20](https://numpy.org/doc/1.20/f2py/index.html)
[1.19](https://numpy.org/doc/1.19/f2py/index.html)
[1.18](https://numpy.org/doc/1.18/f2py/index.html)
[1.17](https://numpy.org/doc/1.17/f2py/index.html)
[1.16](https://numpy.org/doc/1.16/f2py/index.html)
[1.15](https://numpy.org/doc/1.15/f2py/index.html)
[1.14](https://numpy.org/doc/1.14/f2py/index.html)
[1.13](https://numpy.org/doc/1.13/f2py/index.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

F2PY user guide and reference manual[#](https://numpy.org/doc/stable/f2py/index.html#f2py-user-guide-and-reference-manual "Link to this heading")

==================================================================================================================================================

The purpose of the `F2PY` –_Fortran to Python interface generator_– utility is to provide a connection between Python and Fortran. F2PY distributed as part of [NumPy](https://www.numpy.org/)
 (`numpy.f2py`) and once installed is also available as a standalone command line tool. Originally created by Pearu Peterson, and older changelogs are in the [historical reference](https://web.archive.org/web/20140822061353/http://cens.ioc.ee/projects/f2py2e)
.

F2PY facilitates creating/building native [Python C/API extension modules](https://docs.python.org/3/extending/extending.html#extending-python-with-c-or-c)
 that make it possible

*   to call Fortran 77/90/95 external subroutines and Fortran 90/95 module subroutines as well as C functions;
    
*   to access Fortran 77 `COMMON` blocks and Fortran 90/95 module data, including allocatable arrays
    

from Python.

Note

Fortran 77 is essentially feature complete, and an increasing amount of Modern Fortran is supported within F2PY. Most `iso_c_binding` interfaces can be compiled to native extension modules automatically with `f2py`. Bug reports welcome!

F2PY can be used either as a command line tool `f2py` or as a Python module `numpy.f2py`. While we try to provide the command line tool as part of the numpy setup, some platforms like Windows make it difficult to reliably put the executables on the `PATH`. If the `f2py` command is not available in your system, you may have to run it as a module:

python \-m numpy.f2py

Copy to clipboard

Using the `python -m` invocation is also good practice if you have multiple Python installs with NumPy in your system (outside of virtual environments) and you want to ensure you pick up a particular version of Python/F2PY.

If you run `f2py` with no arguments, and the line `numpy Version` at the end matches the NumPy version printed from `python -m numpy.f2py`, then you can use the shorter version. If not, or if you cannot run `f2py`, you should replace all calls to `f2py` mentioned in this guide with the longer version.

For Meson build examples, see [Using F2PY](https://numpy.org/doc/stable/f2py/usage.html)
.

*   [F2PY user guide](https://numpy.org/doc/stable/f2py/f2py-user.html)
    *   [Three ways to wrap - getting started](https://numpy.org/doc/stable/f2py/f2py.getting-started.html)
        *   [The quick way](https://numpy.org/doc/stable/f2py/f2py.getting-started.html#the-quick-way)
            
        *   [The smart way](https://numpy.org/doc/stable/f2py/f2py.getting-started.html#the-smart-way)
            
        *   [The quick and smart way](https://numpy.org/doc/stable/f2py/f2py.getting-started.html#the-quick-and-smart-way)
            
    *   [Using F2PY](https://numpy.org/doc/stable/f2py/usage.html)
        *   [Using `f2py` as a command-line tool](https://numpy.org/doc/stable/f2py/usage.html#using-f2py-as-a-command-line-tool)
            
        *   [Python module `numpy.f2py`](https://numpy.org/doc/stable/f2py/usage.html#python-module-numpy-f2py)
            
        *   [Building with Meson (Examples)](https://numpy.org/doc/stable/f2py/usage.html#building-with-meson-examples)
            
    *   [F2PY examples](https://numpy.org/doc/stable/f2py/f2py-examples.html)
        *   [F2PY walkthrough: a basic extension module](https://numpy.org/doc/stable/f2py/f2py-examples.html#f2py-walkthrough-a-basic-extension-module)
            
        *   [A filtering example](https://numpy.org/doc/stable/f2py/f2py-examples.html#a-filtering-example)
            
        *   [`depends` keyword example](https://numpy.org/doc/stable/f2py/f2py-examples.html#depends-keyword-example)
            
        *   [Read more](https://numpy.org/doc/stable/f2py/f2py-examples.html#read-more)
            
*   [F2PY reference manual](https://numpy.org/doc/stable/f2py/f2py-reference.html)
    *   [Signature file](https://numpy.org/doc/stable/f2py/signature-file.html)
        *   [Signature files syntax](https://numpy.org/doc/stable/f2py/signature-file.html#signature-files-syntax)
            
    *   [Using F2PY bindings in Python](https://numpy.org/doc/stable/f2py/python-usage.html)
        *   [Fortran type objects](https://numpy.org/doc/stable/f2py/python-usage.html#fortran-type-objects)
            
        *   [Scalar arguments](https://numpy.org/doc/stable/f2py/python-usage.html#scalar-arguments)
            
        *   [String arguments](https://numpy.org/doc/stable/f2py/python-usage.html#string-arguments)
            
        *   [Array arguments](https://numpy.org/doc/stable/f2py/python-usage.html#array-arguments)
            
        *   [Call-back arguments](https://numpy.org/doc/stable/f2py/python-usage.html#call-back-arguments)
            
        *   [Common blocks](https://numpy.org/doc/stable/f2py/python-usage.html#common-blocks)
            
        *   [Fortran 90 module data](https://numpy.org/doc/stable/f2py/python-usage.html#fortran-90-module-data)
            
        *   [Allocatable arrays](https://numpy.org/doc/stable/f2py/python-usage.html#allocatable-arrays)
            
    *   [F2PY and build systems](https://numpy.org/doc/stable/f2py/buildtools/index.html)
        *   [Basic concepts](https://numpy.org/doc/stable/f2py/buildtools/index.html#basic-concepts)
            
        *   [Build systems](https://numpy.org/doc/stable/f2py/buildtools/index.html#build-systems)
            
    *   [Advanced F2PY use cases](https://numpy.org/doc/stable/f2py/advanced/use_cases.html)
        *   [Adding user-defined functions to F2PY generated modules](https://numpy.org/doc/stable/f2py/advanced/use_cases.html#adding-user-defined-functions-to-f2py-generated-modules)
            
        *   [Adding user-defined variables](https://numpy.org/doc/stable/f2py/advanced/use_cases.html#adding-user-defined-variables)
            
        *   [Dealing with KIND specifiers](https://numpy.org/doc/stable/f2py/advanced/use_cases.html#dealing-with-kind-specifiers)
            
        *   [Character strings](https://numpy.org/doc/stable/f2py/advanced/use_cases.html#character-strings)
            
    *   [Boilerplate reduction and templating](https://numpy.org/doc/stable/f2py/advanced/boilerplating.html)
        *   [Using FYPP for binding generic interfaces](https://numpy.org/doc/stable/f2py/advanced/boilerplating.html#using-fypp-for-binding-generic-interfaces)
            
    *   [F2PY test suite](https://numpy.org/doc/stable/f2py/f2py-testing.html)
        *   [Adding a test](https://numpy.org/doc/stable/f2py/f2py-testing.html#adding-a-test)
            
*   [F2PY and Windows](https://numpy.org/doc/stable/f2py/windows/index.html)
    *   [Overview](https://numpy.org/doc/stable/f2py/windows/index.html#overview)
        
    *   [Baseline](https://numpy.org/doc/stable/f2py/windows/index.html#baseline)
        
    *   [PowerShell and MSVC](https://numpy.org/doc/stable/f2py/windows/index.html#powershell-and-msvc)
        
    *   [Microsoft Store Python paths](https://numpy.org/doc/stable/f2py/windows/index.html#microsoft-store-python-paths)
        *   [F2PY and Windows Intel Fortran](https://numpy.org/doc/stable/f2py/windows/intel.html)
            
        *   [F2PY and Windows with MSYS2](https://numpy.org/doc/stable/f2py/windows/msys2.html)
            
        *   [F2PY and Conda on Windows](https://numpy.org/doc/stable/f2py/windows/conda.html)
            
        *   [F2PY and PGI Fortran on Windows](https://numpy.org/doc/stable/f2py/windows/pgi.html)
            
*   [1 Migrating to `meson`](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html)
    *   [1.1 Baseline](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#baseline)
        
    *   [1.2 Compilation options](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#compilation-options)
        *   [1.2.1 Basic Usage](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#basic-usage)
            
        *   [1.2.2 Specify the backend](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#specify-the-backend)
            
        *   [1.2.3 Pass a compiler name](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#pass-a-compiler-name)
            
        *   [1.2.4 Dependencies](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#dependencies)
            
        *   [1.2.5 Libraries](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#libraries)
            
    *   [1.3 Customizing builds](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#customizing-builds)