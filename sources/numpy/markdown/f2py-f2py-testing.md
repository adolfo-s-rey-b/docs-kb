[Skip to main content](https://numpy.org/doc/stable/f2py/f2py-testing.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/f2py/f2py-testing.html)
[2.5 (stable)](https://numpy.org/doc/stable/f2py/f2py-testing.html)
[2.4](https://numpy.org/doc/2.4/f2py/f2py-testing.html)
[2.3](https://numpy.org/doc/2.3/f2py/f2py-testing.html)
[2.2](https://numpy.org/doc/2.2/f2py/f2py-testing.html)
[2.1](https://numpy.org/doc/2.1/f2py/f2py-testing.html)
[2.0](https://numpy.org/doc/2.0/f2py/f2py-testing.html)
[1.26](https://numpy.org/doc/1.26/f2py/f2py-testing.html)
[1.25](https://numpy.org/doc/1.25/f2py/f2py-testing.html)
[1.24](https://numpy.org/doc/1.24/f2py/f2py-testing.html)
[1.23](https://numpy.org/doc/1.23/f2py/f2py-testing.html)
[1.22](https://numpy.org/doc/1.22/f2py/f2py-testing.html)
[1.21](https://numpy.org/doc/1.21/f2py/f2py-testing.html)
[1.20](https://numpy.org/doc/1.20/f2py/f2py-testing.html)
[1.19](https://numpy.org/doc/1.19/f2py/f2py-testing.html)
[1.18](https://numpy.org/doc/1.18/f2py/f2py-testing.html)
[1.17](https://numpy.org/doc/1.17/f2py/f2py-testing.html)
[1.16](https://numpy.org/doc/1.16/f2py/f2py-testing.html)
[1.15](https://numpy.org/doc/1.15/f2py/f2py-testing.html)
[1.14](https://numpy.org/doc/1.14/f2py/f2py-testing.html)
[1.13](https://numpy.org/doc/1.13/f2py/f2py-testing.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

F2PY test suite[#](https://numpy.org/doc/stable/f2py/f2py-testing.html#f2py-test-suite "Link to this heading")

===============================================================================================================

F2PY’s test suite is present in the directory `numpy/f2py/tests`. Its aim is to ensure that Fortran language features are correctly translated to Python. For example, the user can specify starting and ending indices of arrays in Fortran. This behaviour is translated to the generated CPython library where the arrays strictly start from 0 index.

The directory of the test suite looks like the following:

./tests/
├── \_\_init\_\_.py
├── src
│   ├── abstract\_interface
│   ├── array\_from\_pyobj
│   ├── // ... several test folders
│   └── string
├── test\_abstract\_interface.py
├── test\_array\_from\_pyobj.py
├── // ... several test files
├── test\_symbolic.py
└── util.py

Copy to clipboard

Files starting with `test_` contain tests for various aspects of f2py from parsing Fortran files to checking modules’ documentation. `src` directory contains the Fortran source files upon which we do the testing. `util.py` contains utility functions for building and importing Fortran modules during test time using a temporary location.

Adding a test[#](https://numpy.org/doc/stable/f2py/f2py-testing.html#adding-a-test "Link to this heading")

-----------------------------------------------------------------------------------------------------------

F2PY’s current test suite predates `pytest` and therefore does not use fixtures. Instead, the test files contain test classes that inherit from `F2PyTest` class present in `util.py`.

 1    backend \= SimplifiedMesonBackend(
 2        modulename\=module\_name,
 3        sources\=source\_files,
 4        extra\_objects\=kwargs.get("extra\_objects", \[\]),
 5        build\_dir\=build\_dir,
 6        include\_dirs\=kwargs.get("include\_dirs", \[\]),
 7        library\_dirs\=kwargs.get("library\_dirs", \[\]),
 8        libraries\=kwargs.get("libraries", \[\]),
 9        define\_macros\=kwargs.get("define\_macros", \[\]),
10        undef\_macros\=kwargs.get("undef\_macros", \[\]),

Copy to clipboard

This class many helper functions for parsing and compiling test source files. Its child classes can override its `sources` data member to provide their own source files. This superclass will then compile the added source files upon object creation and their functions will be appended to `self.module` data member. Thus, the child classes will be able to access the fortran functions specified in source file by calling `self.module.[fortran_function_name]`.

New in version v2.0.0b1.

Each of the `f2py` tests should run without failure if no Fortran compilers are present on the host machine. To facilitate this, the `CompilerChecker` is used, essentially providing a `meson` dependent set of utilities namely `has_{c,f77,f90,fortran}_compiler()`.

For the CLI tests in `test_f2py2e`, flags which are expected to call `meson` or otherwise depend on a compiler need to call `compiler_check_f2pycli()` instead of `f2pycli()`.

### Example[#](https://numpy.org/doc/stable/f2py/f2py-testing.html#example "Link to this heading")

Consider the following subroutines, contained in a file named `add-test.f`

        subroutine addb(k)
          real(8), intent(inout) :: k(:)
          k\=k+1
        endsubroutine

        subroutine addc(w,k)
          real(8), intent(in) :: w(:)
          real(8), intent(out) :: k(size(w))
          k\=w+1
        endsubroutine

Copy to clipboard

The first routine _addb_ simply takes an array and increases its elements by 1. The second subroutine _addc_ assigns a new array _k_ with elements greater that the elements of the input array _w_ by 1.

A test can be implemented as follows:

class TestAdd(util.F2PyTest):
    sources \= \[util.getpath("add-test.f")\]

    def test\_module(self):
        k \= np.array(\[1, 2, 3\], dtype\=np.float64)
        w \= np.array(\[1, 2, 3\], dtype\=np.float64)
        self.module.addb(k)
        assert np.allclose(k, w + 1)
        self.module.addc(\[w, k\])
        assert np.allclose(k, w + 1)

Copy to clipboard

We override the `sources` data member to provide the source file. The source files are compiled and subroutines are attached to module data member when the class object is created. The `test_module` function calls the subroutines and tests their results.

On this page