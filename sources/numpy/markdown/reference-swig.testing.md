[Skip to main content](https://numpy.org/doc/stable/reference/swig.testing.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/swig.testing.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/swig.testing.html)
[2.4](https://numpy.org/doc/2.4/reference/swig.testing.html)
[2.3](https://numpy.org/doc/2.3/reference/swig.testing.html)
[2.2](https://numpy.org/doc/2.2/reference/swig.testing.html)
[2.1](https://numpy.org/doc/2.1/reference/swig.testing.html)
[2.0](https://numpy.org/doc/2.0/reference/swig.testing.html)
[1.26](https://numpy.org/doc/1.26/reference/swig.testing.html)
[1.25](https://numpy.org/doc/1.25/reference/swig.testing.html)
[1.24](https://numpy.org/doc/1.24/reference/swig.testing.html)
[1.23](https://numpy.org/doc/1.23/reference/swig.testing.html)
[1.22](https://numpy.org/doc/1.22/reference/swig.testing.html)
[1.21](https://numpy.org/doc/1.21/reference/swig.testing.html)
[1.20](https://numpy.org/doc/1.20/reference/swig.testing.html)
[1.19](https://numpy.org/doc/1.19/reference/swig.testing.html)
[1.18](https://numpy.org/doc/1.18/reference/swig.testing.html)
[1.17](https://numpy.org/doc/1.17/reference/swig.testing.html)
[1.16](https://numpy.org/doc/1.16/reference/swig.testing.html)
[1.15](https://numpy.org/doc/1.15/reference/swig.testing.html)
[1.14](https://numpy.org/doc/1.14/reference/swig.testing.html)
[1.13](https://numpy.org/doc/1.13/reference/swig.testing.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Testing the numpy.i typemaps[#](https://numpy.org/doc/stable/reference/swig.testing.html#testing-the-numpy-i-typemaps "Link to this heading")

==============================================================================================================================================

Introduction[#](https://numpy.org/doc/stable/reference/swig.testing.html#introduction "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Writing tests for the `numpy.i` [SWIG](https://www.swig.org/)
 interface file is a combinatorial headache. At present, 12 different data types are supported, each with 74 different argument signatures, for a total of 888 typemaps supported “out of the box”. Each of these typemaps, in turn, might require several unit tests in order to verify expected behavior for both proper and improper inputs. Currently, this results in more than 1,000 individual unit tests executed when `make test` is run in the `numpy/tools/swig` subdirectory.

To facilitate this many similar unit tests, some high-level programming techniques are employed, including C and [SWIG](https://www.swig.org/)
 macros, as well as Python inheritance. The purpose of this document is to describe the testing infrastructure employed to verify that the `numpy.i` typemaps are working as expected.

Testing organization[#](https://numpy.org/doc/stable/reference/swig.testing.html#testing-organization "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

There are three independent testing frameworks supported, for one-, two-, and three-dimensional arrays respectively. For one-dimensional arrays, there are two C++ files, a header and a source, named:

Vector.h
Vector.cxx

Copy to clipboard

that contain prototypes and code for a variety of functions that have one-dimensional arrays as function arguments. The file:

Vector.i

Copy to clipboard

is a [SWIG](https://www.swig.org/)
 interface file that defines a python module `Vector` that wraps the functions in `Vector.h` while utilizing the typemaps in `numpy.i` to correctly handle the C arrays.

The `Makefile` calls `swig` to generate `Vector.py` and `Vector_wrap.cxx`, and also executes the `setup.py` script that compiles `Vector_wrap.cxx` and links together the extension module `_Vector.so` or `_Vector.dylib`, depending on the platform. This extension module and the proxy file `Vector.py` are both placed in a subdirectory under the `build` directory.

The actual testing takes place with a Python script named:

testVector.py

Copy to clipboard

that uses the standard Python library module `unittest`, which performs several tests of each function defined in `Vector.h` for each data type supported.

Two-dimensional arrays are tested in exactly the same manner. The above description applies, but with `Matrix` substituted for `Vector`. For three-dimensional tests, substitute `Tensor` for `Vector`. For four-dimensional tests, substitute `SuperTensor` for `Vector`. For flat in-place array tests, substitute `Flat` for `Vector`. For the descriptions that follow, we will reference the `Vector` tests, but the same information applies to `Matrix`, `Tensor` and `SuperTensor` tests.

The command `make test` will ensure that all of the test software is built and then run all three test scripts.

Testing header files[#](https://numpy.org/doc/stable/reference/swig.testing.html#testing-header-files "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

`Vector.h` is a C++ header file that defines a C macro called `TEST_FUNC_PROTOS` that takes two arguments: `TYPE`, which is a data type name such as `unsigned int`; and `SNAME`, which is a short name for the same data type with no spaces, e.g. `uint`. This macro defines several function prototypes that have the prefix `SNAME` and have at least one argument that is an array of type `TYPE`. Those functions that have return arguments return a `TYPE` value.

`TEST_FUNC_PROTOS` is then implemented for all of the data types supported by `numpy.i`:

*   `signed char`
    
*   `unsigned char`
    
*   `short`
    
*   `unsigned short`
    
*   `int`
    
*   `unsigned int`
    
*   `long`
    
*   `unsigned long`
    
*   `long long`
    
*   `unsigned long long`
    
*   `float`
    
*   `double`
    

Testing source files[#](https://numpy.org/doc/stable/reference/swig.testing.html#testing-source-files "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

`Vector.cxx` is a C++ source file that implements compilable code for each of the function prototypes specified in `Vector.h`. It defines a C macro `TEST_FUNCS` that has the same arguments and works in the same way as `TEST_FUNC_PROTOS` does in `Vector.h`. `TEST_FUNCS` is implemented for each of the 12 data types as above.

Testing SWIG interface files[#](https://numpy.org/doc/stable/reference/swig.testing.html#testing-swig-interface-files "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

`Vector.i` is a [SWIG](https://www.swig.org/)
 interface file that defines python module `Vector`. It follows the conventions for using `numpy.i` as described in this chapter. It defines a [SWIG](https://www.swig.org/)
 macro `%apply_numpy_typemaps` that has a single argument `TYPE`. It uses the [SWIG](https://www.swig.org/)
 directive `%apply` to apply the provided typemaps to the argument signatures found in `Vector.h`. This macro is then implemented for all of the data types supported by `numpy.i`. It then does a `%include "Vector.h"` to wrap all of the function prototypes in `Vector.h` using the typemaps in `numpy.i`.

Testing Python scripts[#](https://numpy.org/doc/stable/reference/swig.testing.html#testing-python-scripts "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

After `make` is used to build the testing extension modules, `testVector.py` can be run to execute the tests. As with other scripts that use `unittest` to facilitate unit testing, `testVector.py` defines a class that inherits from `unittest.TestCase`:

class VectorTestCase(unittest.TestCase):

Copy to clipboard

However, this class is not run directly. Rather, it serves as a base class to several other python classes, each one specific to a particular data type. The `VectorTestCase` class stores two strings for typing information:

**self.typeStr**

A string that matches one of the `SNAME` prefixes used in `Vector.h` and `Vector.cxx`. For example, `"double"`.

**self.typeCode**

A short (typically single-character) string that represents a data type in numpy and corresponds to `self.typeStr`. For example, if `self.typeStr` is `"double"`, then `self.typeCode` should be `"d"`.

Each test defined by the `VectorTestCase` class extracts the python function it is trying to test by accessing the `Vector` module’s dictionary:

length \= Vector.\_\_dict\_\_\[self.typeStr + "Length"\]

Copy to clipboard

In the case of double precision tests, this will return the python function `Vector.doubleLength`.

We then define a new test case class for each supported data type with a short definition such as:

class doubleTestCase(VectorTestCase):
    def \_\_init\_\_(self, methodName\="runTest"):
        VectorTestCase.\_\_init\_\_(self, methodName)
        self.typeStr  \= "double"
        self.typeCode \= "d"

Copy to clipboard

Each of these 12 classes is collected into a `unittest.TestSuite`, which is then executed. Errors and failures are summed together and returned as the exit argument. Any non-zero result indicates that at least one test did not pass.

On this page