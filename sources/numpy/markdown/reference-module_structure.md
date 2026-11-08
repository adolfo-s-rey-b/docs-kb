[Skip to main content](https://numpy.org/doc/stable/reference/module_structure.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/module_structure.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/module_structure.html)
[2.4](https://numpy.org/doc/2.4/reference/module_structure.html)
[2.3](https://numpy.org/doc/2.3/reference/module_structure.html)
[2.2](https://numpy.org/doc/2.2/reference/module_structure.html)
[2.1](https://numpy.org/doc/2.1/reference/module_structure.html)
[2.0](https://numpy.org/doc/2.0/reference/module_structure.html)
[1.26](https://numpy.org/doc/1.26/reference/module_structure.html)
[1.25](https://numpy.org/doc/1.25/reference/module_structure.html)
[1.24](https://numpy.org/doc/1.24/reference/module_structure.html)
[1.23](https://numpy.org/doc/1.23/reference/module_structure.html)
[1.22](https://numpy.org/doc/1.22/reference/module_structure.html)
[1.21](https://numpy.org/doc/1.21/reference/module_structure.html)
[1.20](https://numpy.org/doc/1.20/reference/module_structure.html)
[1.19](https://numpy.org/doc/1.19/reference/module_structure.html)
[1.18](https://numpy.org/doc/1.18/reference/module_structure.html)
[1.17](https://numpy.org/doc/1.17/reference/module_structure.html)
[1.16](https://numpy.org/doc/1.16/reference/module_structure.html)
[1.15](https://numpy.org/doc/1.15/reference/module_structure.html)
[1.14](https://numpy.org/doc/1.14/reference/module_structure.html)
[1.13](https://numpy.org/doc/1.13/reference/module_structure.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

NumPy’s module structure[#](https://numpy.org/doc/stable/reference/module_structure.html#numpy-s-module-structure "Link to this heading")

==========================================================================================================================================

NumPy has a large number of submodules. Most regular usage of NumPy requires only the main namespace and a smaller set of submodules. The rest either have special-purpose or niche namespaces.

Main namespaces[#](https://numpy.org/doc/stable/reference/module_structure.html#main-namespaces "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

Regular/recommended user-facing namespaces for general use:

*   [numpy](https://numpy.org/doc/stable/reference/routines.html#routines)
    
*   [numpy.exceptions](https://numpy.org/doc/stable/reference/routines.exceptions.html#routines-exceptions)
    
*   [numpy.fft](https://numpy.org/doc/stable/reference/routines.fft.html#routines-fft)
    
*   [numpy.linalg](https://numpy.org/doc/stable/reference/routines.linalg.html#routines-linalg)
    
*   [numpy.polynomial](https://numpy.org/doc/stable/reference/routines.polynomials-package.html#numpy-polynomial)
    
*   [numpy.random](https://numpy.org/doc/stable/reference/random/index.html#numpyrandom)
    
*   [numpy.strings](https://numpy.org/doc/stable/reference/routines.strings.html#routines-strings)
    
*   [numpy.testing](https://numpy.org/doc/stable/reference/routines.testing.html#routines-testing)
    
*   [numpy.typing](https://numpy.org/doc/stable/reference/typing.html#typing)
    

Special-purpose namespaces[#](https://numpy.org/doc/stable/reference/module_structure.html#special-purpose-namespaces "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

*   [numpy.ctypeslib](https://numpy.org/doc/stable/reference/routines.ctypeslib.html#routines-ctypeslib)
     - interacting with NumPy objects with [`ctypes`](https://docs.python.org/3/library/ctypes.html#module-ctypes "(in Python v3.14)")
    
*   [numpy.dtypes](https://numpy.org/doc/stable/reference/routines.dtypes.html#routines-dtypes)
     - dtype classes (typically not used directly by end users)
    
*   [numpy.emath](https://numpy.org/doc/stable/reference/routines.emath.html#routines-emath)
     - mathematical functions with automatic domain
    
*   [numpy.lib](https://numpy.org/doc/stable/reference/routines.lib.html#routines-lib)
     - utilities & functionality which do not fit the main namespace
    
*   [numpy.rec](https://numpy.org/doc/stable/reference/routines.rec.html#routines-rec)
     - record arrays (largely superseded by dataframe libraries)
    
*   [numpy.version](https://numpy.org/doc/stable/reference/routines.version.html#routines-version)
     - small module with more detailed version info
    

Legacy namespaces[#](https://numpy.org/doc/stable/reference/module_structure.html#legacy-namespaces "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Prefer not to use these namespaces for new code. There are better alternatives and/or this code is deprecated or isn’t reliable.

*   [numpy.char](https://numpy.org/doc/stable/reference/routines.char.html#routines-char)
     - legacy string functionality, only for fixed-width strings
    
*   [numpy.f2py](https://numpy.org/doc/stable/f2py/usage.html#python-module-numpy-f2py)
     - Fortran binding generation (usually used from the command line only)
    
*   [numpy.ma](https://numpy.org/doc/stable/reference/routines.ma.html#routines-ma)
     - masked arrays (not very reliable, needs an overhaul)
    
*   [numpy.matlib](https://numpy.org/doc/stable/reference/routines.matlib.html#routines-matlib)
     (pending deprecation) - functions supporting `matrix` instances
    

On this page