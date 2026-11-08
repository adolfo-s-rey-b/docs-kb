[Skip to main content](https://numpy.org/doc/stable/f2py/buildtools/skbuild.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Using via `scikit-build`[#](https://numpy.org/doc/stable/f2py/buildtools/skbuild.html#using-via-scikit-build "Link to this heading")

=====================================================================================================================================

`scikit-build` provides two separate concepts geared towards the users of Python extension modules.

1.  A `setuptools` replacement (legacy behaviour)
    
2.  A series of `cmake` modules with definitions which help building Python extensions
    

Note

It is possible to use `scikit-build`’s `cmake` modules to [bypass the cmake setup mechanism](https://scikit-build.readthedocs.io/en/latest/cmake-modules/F2PY.html)
 completely, and to write targets which call `f2py -c`. This usage is **not recommended** since the point of these build system documents are to move away from the internal `numpy.distutils` methods.

For situations where no `setuptools` replacements are required or wanted (i.e. if `wheels` are not needed), it is recommended to instead use the vanilla `cmake` setup described in [Using via cmake](https://numpy.org/doc/stable/f2py/buildtools/cmake.html#f2py-cmake)
.

Fibonacci walkthrough (F77)[#](https://numpy.org/doc/stable/f2py/buildtools/skbuild.html#fibonacci-walkthrough-f77 "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

We will consider the `fib` example from [Three ways to wrap - getting started](https://numpy.org/doc/stable/f2py/f2py.getting-started.html#f2py-getting-started)
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

### `CMake` modules only[#](https://numpy.org/doc/stable/f2py/buildtools/skbuild.html#cmake-modules-only "Link to this heading")

Consider using the following `CMakeLists.txt`.

\### setup project ###
cmake\_minimum\_required(VERSION 3.9)

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

\# Ensure scikit-build modules
if (NOT SKBUILD)
  find\_package(PythonInterp 3.8 REQUIRED)
  \# Kanged --> https://github.com/Kitware/torch\_liberator/blob/master/CMakeLists.txt
  \# If skbuild is not the driver; include its utilities in CMAKE\_MODULE\_PATH
  execute\_process(
    COMMAND "${PYTHON\_EXECUTABLE}"
    \-c "import os, skbuild; print(os.path.dirname(skbuild.\_\_file\_\_))"
    OUTPUT\_VARIABLE SKBLD\_DIR
    OUTPUT\_STRIP\_TRAILING\_WHITESPACE
  )
  list(APPEND CMAKE\_MODULE\_PATH "${SKBLD\_DIR}/resources/cmake")
  message(STATUS "Looking in ${SKBLD\_DIR}/resources/cmake for CMake modules")
endif()

\# scikit-build style includes
find\_package(PythonExtensions REQUIRED) \# for ${PYTHON\_EXTENSION\_MODULE\_SUFFIX}

\# Grab the variables from a local Python installation
\# NumPy headers
execute\_process(
  COMMAND "${PYTHON\_EXECUTABLE}"
  \-c "import numpy; print(numpy.get\_include())"
  OUTPUT\_VARIABLE NumPy\_INCLUDE\_DIRS
  OUTPUT\_STRIP\_TRAILING\_WHITESPACE
)
\# F2PY headers
execute\_process(
  COMMAND "${PYTHON\_EXECUTABLE}"
  \-c "import numpy.f2py; print(numpy.f2py.get\_include())"
  OUTPUT\_VARIABLE F2PY\_INCLUDE\_DIR
  OUTPUT\_STRIP\_TRAILING\_WHITESPACE
)

\# Prepping the module
set(f2py\_module\_name "fibby")
set(fortran\_src\_file "${CMAKE\_SOURCE\_DIR}/fib1.f")
set(f2py\_module\_c "${f2py\_module\_name}module.c")

\# Target for enforcing dependencies
add\_custom\_target(genpyf
  DEPENDS "${fortran\_src\_file}"
)
add\_custom\_command(
  OUTPUT "${CMAKE\_CURRENT\_BINARY\_DIR}/${f2py\_module\_c}"
  COMMAND ${PYTHON\_EXECUTABLE}  \-m "numpy.f2py"
                   "${fortran\_src\_file}"
                   \-m "fibby"
                   \--lower \# Important
  DEPENDS fib1.f \# Fortran source
)

add\_library(${CMAKE\_PROJECT\_NAME} MODULE
            "${f2py\_module\_name}module.c"
            "${F2PY\_INCLUDE\_DIR}/fortranobject.c"
            "${fortran\_src\_file}")

target\_include\_directories(${CMAKE\_PROJECT\_NAME} PUBLIC
                           ${F2PY\_INCLUDE\_DIR}
                           ${NumPy\_INCLUDE\_DIRS}
                           ${PYTHON\_INCLUDE\_DIRS})
set\_target\_properties(${CMAKE\_PROJECT\_NAME} PROPERTIES SUFFIX "${PYTHON\_EXTENSION\_MODULE\_SUFFIX}")
set\_target\_properties(${CMAKE\_PROJECT\_NAME} PROPERTIES PREFIX "")

\# Linker fixes
if (UNIX)
  if (APPLE)
    set\_target\_properties(${CMAKE\_PROJECT\_NAME} PROPERTIES
    LINK\_FLAGS  '-Wl,-dylib,-undefined,dynamic\_lookup')
  else()
    set\_target\_properties(${CMAKE\_PROJECT\_NAME} PROPERTIES
  LINK\_FLAGS  '-Wl,--allow-shlib-undefined')
  endif()
endif()

add\_dependencies(${CMAKE\_PROJECT\_NAME} genpyf)

install(TARGETS ${CMAKE\_PROJECT\_NAME} DESTINATION fibby)

Copy to clipboard

Much of the logic is the same as in [Using via cmake](https://numpy.org/doc/stable/f2py/buildtools/cmake.html#f2py-cmake)
, however notably here the appropriate module suffix is generated via `sysconfig.get_config_var("SO")`. The resulting extension can be built and loaded in the standard workflow.

ls .
\# CMakeLists.txt fib1.f
cmake \-S . \-B build
cmake \--build build
cd build
python \-c "import numpy as np; import fibby; a = np.zeros(9); fibby.fib(a); print (a)"
\# \[ 0.  1.  1.  2.  3.  5.  8. 13. 21.\]

Copy to clipboard

### `setuptools` replacement[#](https://numpy.org/doc/stable/f2py/buildtools/skbuild.html#setuptools-replacement "Link to this heading")

Note

**As of November 2021**

The behavior described here of driving the `cmake` build of a module is considered to be legacy behaviour and should not be depended on.

The utility of `scikit-build` lies in being able to drive the generation of more than extension modules, in particular a common usage pattern is the generation of Python distributables (for example for PyPI).

The workflow with `scikit-build` straightforwardly supports such packaging requirements. Consider augmenting the project with a `setup.py` as defined:

from skbuild import setup

setup(
    name\="fibby",
    version\="0.0.1",
    description\="a minimal example package (fortran version)",
    license\="MIT",
    packages\=\['fibby'\],
    python\_requires\=">=3.7",
)

Copy to clipboard

Along with a commensurate `pyproject.toml`

\[build-system\]
requires \= \["setuptools>=42", "wheel", "scikit-build", "cmake>=3.9", "numpy>=1.21"\]
build-backend \= "setuptools.build\_meta"

Copy to clipboard

Together these can build the extension using `cmake` in tandem with other standard `setuptools` outputs. Running `cmake` through `setup.py` is mostly used when it is necessary to integrate with extension modules not built with `cmake`.

ls .
\# CMakeLists.txt fib1.f pyproject.toml setup.py
python setup.py build\_ext \--inplace
python \-c "import numpy as np; import fibby.fibby; a = np.zeros(9); fibby.fibby.fib(a); print (a)"
\# \[ 0.  1.  1.  2.  3.  5.  8. 13. 21.\]

Copy to clipboard

Where we have modified the path to the module as `--inplace` places the extension module in a subfolder.

On this page