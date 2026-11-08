[Skip to main content](https://numpy.org/doc/stable/f2py/buildtools/cmake.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/f2py/buildtools/cmake.html)
[2.5 (stable)](https://numpy.org/doc/stable/f2py/buildtools/cmake.html)
[2.4](https://numpy.org/doc/2.4/f2py/buildtools/cmake.html)
[2.3](https://numpy.org/doc/2.3/f2py/buildtools/cmake.html)
[2.2](https://numpy.org/doc/2.2/f2py/buildtools/cmake.html)
[2.1](https://numpy.org/doc/2.1/f2py/buildtools/cmake.html)
[2.0](https://numpy.org/doc/2.0/f2py/buildtools/cmake.html)
[1.26](https://numpy.org/doc/1.26/f2py/buildtools/cmake.html)
[1.25](https://numpy.org/doc/1.25/f2py/buildtools/cmake.html)
[1.24](https://numpy.org/doc/1.24/f2py/buildtools/cmake.html)
[1.23](https://numpy.org/doc/1.23/f2py/buildtools/cmake.html)
[1.22](https://numpy.org/doc/1.22/f2py/buildtools/cmake.html)
[1.21](https://numpy.org/doc/1.21/f2py/buildtools/cmake.html)
[1.20](https://numpy.org/doc/1.20/f2py/buildtools/cmake.html)
[1.19](https://numpy.org/doc/1.19/f2py/buildtools/cmake.html)
[1.18](https://numpy.org/doc/1.18/f2py/buildtools/cmake.html)
[1.17](https://numpy.org/doc/1.17/f2py/buildtools/cmake.html)
[1.16](https://numpy.org/doc/1.16/f2py/buildtools/cmake.html)
[1.15](https://numpy.org/doc/1.15/f2py/buildtools/cmake.html)
[1.14](https://numpy.org/doc/1.14/f2py/buildtools/cmake.html)
[1.13](https://numpy.org/doc/1.13/f2py/buildtools/cmake.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Using via `cmake`[#](https://numpy.org/doc/stable/f2py/buildtools/cmake.html#using-via-cmake "Link to this heading")

=====================================================================================================================

In terms of complexity, `cmake` falls between `make` and `meson`. The learning curve is steeper since CMake syntax is not pythonic and is closer to `make` with environment variables.

However, the trade-off is enhanced flexibility and support for most architectures and compilers. An introduction to the syntax is out of scope for this document, but this [extensive CMake collection](https://cliutils.gitlab.io/modern-cmake/)
 of resources is great.

Note

`cmake` is very popular for mixed-language systems, however support for `f2py` is not particularly native or pleasant; and a more natural approach is to consider [Using via scikit-build](https://numpy.org/doc/stable/f2py/buildtools/skbuild.html#f2py-skbuild)

Fibonacci walkthrough (F77)[#](https://numpy.org/doc/stable/f2py/buildtools/cmake.html#fibonacci-walkthrough-f77 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

Returning to the `fib` example from [Three ways to wrap - getting started](https://numpy.org/doc/stable/f2py/f2py.getting-started.html#f2py-getting-started)
 section.

C FILE: FIB1.F
      SUBROUTINE FIB(A,N)
C
C     CALCULATE FIRST N FIBONACCI NUMBERS
C
      INTEGER N
      REAL\*8 A(N)
      DO I\=1,N
         IF (I.EQ.1) THEN
            A(I) \= 0.0D0
         ELSEIF (I.EQ.2) THEN
            A(I) \= 1.0D0
         ELSE 
            A(I) \= A(I\-1) + A(I\-2)
         ENDIF
      ENDDO
      END
C END FILE FIB1.F

Copy to clipboard

We do not need to explicitly generate the `python -m numpy.f2py fib1.f` output, which is `fib1module.c`, which is beneficial. With this; we can now initialize a `CMakeLists.txt` file as follows:

cmake\_minimum\_required(VERSION 3.18) \# Needed to avoid requiring embedded Python libs too

project(fibby
  VERSION 1.0
  DESCRIPTION "FIB module"
  LANGUAGES C Fortran
)

\# Safety net
if(PROJECT\_SOURCE\_DIR STREQUAL PROJECT\_BINARY\_DIR)
  message(
    FATAL\_ERROR
      "In-source builds not allowed. Please make a new directory (called a build directory) and run CMake from there.\\n"
  )
endif()

\# Grab Python, 3.8 or newer
find\_package(Python 3.8 REQUIRED
  COMPONENTS Interpreter Development.Module NumPy)

\# Grab the variables from a local Python installation
\# F2PY headers
execute\_process(
  COMMAND "${Python\_EXECUTABLE}"
  \-c "import numpy.f2py; print(numpy.f2py.get\_include())"
  OUTPUT\_VARIABLE F2PY\_INCLUDE\_DIR
  OUTPUT\_STRIP\_TRAILING\_WHITESPACE
)

\# Print out the discovered paths
include(CMakePrintHelpers)
cmake\_print\_variables(Python\_INCLUDE\_DIRS)
cmake\_print\_variables(F2PY\_INCLUDE\_DIR)
cmake\_print\_variables(Python\_NumPy\_INCLUDE\_DIRS)

\# Common variables
set(f2py\_module\_name "fibby")
set(fortran\_src\_file "${CMAKE\_SOURCE\_DIR}/fib1.f")
set(f2py\_module\_c "${f2py\_module\_name}module.c")

\# Generate sources
add\_custom\_target(
  genpyf
  DEPENDS "${CMAKE\_CURRENT\_BINARY\_DIR}/${f2py\_module\_c}"
)
add\_custom\_command(
  OUTPUT "${CMAKE\_CURRENT\_BINARY\_DIR}/${f2py\_module\_c}"
  COMMAND ${Python\_EXECUTABLE}  \-m "numpy.f2py"
                   "${fortran\_src\_file}"
                   \-m "fibby"
                   \--lower \# Important
  DEPENDS fib1.f \# Fortran source
)

\# Set up target
Python\_add\_library(${CMAKE\_PROJECT\_NAME} MODULE WITH\_SOABI
  "${CMAKE\_CURRENT\_BINARY\_DIR}/${f2py\_module\_c}" \# Generated
  "${F2PY\_INCLUDE\_DIR}/fortranobject.c" \# From NumPy
  "${fortran\_src\_file}" \# Fortran source(s)
)

\# Depend on sources
target\_link\_libraries(${CMAKE\_PROJECT\_NAME} PRIVATE Python::NumPy)
add\_dependencies(${CMAKE\_PROJECT\_NAME} genpyf)
target\_include\_directories(${CMAKE\_PROJECT\_NAME} PRIVATE "${F2PY\_INCLUDE\_DIR}")

Copy to clipboard

A key element of the `CMakeLists.txt` file defined above is that the `add_custom_command` is used to generate the wrapper `C` files and then added as a dependency of the actual shared library target via a `add_custom_target` directive which prevents the command from running every time. Additionally, the method used for obtaining the `fortranobject.c` file can also be used to grab the `numpy` headers on older `cmake` versions.

This then works in the same manner as the other modules, although the naming conventions are different and the output library is not automatically prefixed with the `cython` information.

ls .
\# CMakeLists.txt fib1.f
cmake \-S . \-B build
cmake \--build build
cd build
python \-c "import numpy as np; import fibby; a = np.zeros(9); fibby.fib(a); print (a)"
\# \[ 0.  1.  1.  2.  3.  5.  8. 13. 21.\]

Copy to clipboard

This is particularly useful where an existing toolchain already exists and `scikit-build` or other additional `python` dependencies are discouraged.

On this page