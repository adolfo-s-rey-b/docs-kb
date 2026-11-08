[Skip to main content](https://numpy.org/doc/stable/f2py/buildtools/meson.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/f2py/buildtools/meson.html)
[2.5 (stable)](https://numpy.org/doc/stable/f2py/buildtools/meson.html)
[2.4](https://numpy.org/doc/2.4/f2py/buildtools/meson.html)
[2.3](https://numpy.org/doc/2.3/f2py/buildtools/meson.html)
[2.2](https://numpy.org/doc/2.2/f2py/buildtools/meson.html)
[2.1](https://numpy.org/doc/2.1/f2py/buildtools/meson.html)
[2.0](https://numpy.org/doc/2.0/f2py/buildtools/meson.html)
[1.26](https://numpy.org/doc/1.26/f2py/buildtools/meson.html)
[1.25](https://numpy.org/doc/1.25/f2py/buildtools/meson.html)
[1.24](https://numpy.org/doc/1.24/f2py/buildtools/meson.html)
[1.23](https://numpy.org/doc/1.23/f2py/buildtools/meson.html)
[1.22](https://numpy.org/doc/1.22/f2py/buildtools/meson.html)
[1.21](https://numpy.org/doc/1.21/f2py/buildtools/meson.html)
[1.20](https://numpy.org/doc/1.20/f2py/buildtools/meson.html)
[1.19](https://numpy.org/doc/1.19/f2py/buildtools/meson.html)
[1.18](https://numpy.org/doc/1.18/f2py/buildtools/meson.html)
[1.17](https://numpy.org/doc/1.17/f2py/buildtools/meson.html)
[1.16](https://numpy.org/doc/1.16/f2py/buildtools/meson.html)
[1.15](https://numpy.org/doc/1.15/f2py/buildtools/meson.html)
[1.14](https://numpy.org/doc/1.14/f2py/buildtools/meson.html)
[1.13](https://numpy.org/doc/1.13/f2py/buildtools/meson.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Using via `meson`[#](https://numpy.org/doc/stable/f2py/buildtools/meson.html#using-via-meson "Link to this heading")

=====================================================================================================================

Note

Much of this document is now obsoleted, one can run `f2py` with `--build-dir` to get a skeleton `meson` project with basic dependencies setup.

Changed in version 1.26.x: The default build system for `f2py` is now `meson`, see [Status of numpy.distutils and migration advice](https://numpy.org/doc/stable/reference/distutils_status_migration.html#distutils-status-migration)
 for some more details..

Fibonacci walkthrough (F77)[#](https://numpy.org/doc/stable/f2py/buildtools/meson.html#fibonacci-walkthrough-f77 "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

We will need the generated `C` wrapper before we can use a general purpose build system like `meson`. We will acquire this by:

python \-m numpy.f2py fib1.f \-m fib2

Copy to clipboard

Now, consider the following `meson.build` file for the `fib` and `scalar` examples from [Three ways to wrap - getting started](https://numpy.org/doc/stable/f2py/f2py.getting-started.html#f2py-getting-started)
 section:

project('f2py\_examples', 'c',
  version : '0.1',
  license: 'BSD-3',
  meson\_version: '>=0.64.0',
  default\_options : \['warning\_level=2'\],
)

add\_languages('fortran')

py\_mod \= import('python')
py \= py\_mod.find\_installation(pure: false)
py\_dep \= py.dependency()

incdir\_numpy \= run\_command(py,
  \['-c', 'import os; os.chdir(".."); import numpy; print(numpy.get\_include())'\],
  check : true
).stdout().strip()

incdir\_f2py \= run\_command(py,
    \['-c', 'import os; os.chdir(".."); import numpy.f2py; print(numpy.f2py.get\_include())'\],
    check : true
).stdout().strip()

inc\_np \= include\_directories(incdir\_numpy, incdir\_f2py)

py.extension\_module('fib2',
  \[\
    'fib1.f',\
    'fib2module.c',  \# note: this assumes f2py was manually run before!\
  \],
  incdir\_f2py / 'fortranobject.c',
  include\_directories: inc\_np,
  dependencies : py\_dep,
  install : true
)

Copy to clipboard

At this point the build will complete, but the import will fail:

meson setup builddir
meson compile \-C builddir
cd builddir
python \-c 'import fib2'
Traceback (most recent call last):
File "<string>", line 1, in <module>
ImportError: fib2.cpython-39-x86\_64-linux-gnu.so: undefined symbol: FIB\_
\# Check this isn't a false positive
nm \-A fib2.cpython-39-x86\_64-linux-gnu.so | grep FIB\_
fib2.cpython-39-x86\_64-linux-gnu.so: U FIB\_

Copy to clipboard

Recall that the original example, as reproduced below, was in SCREAMCASE:

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

With the standard approach, the subroutine exposed to `python` is `fib` and not `FIB`. This means we have a few options. One approach (where possible) is to lowercase the original Fortran file with say:

tr "\[:upper:\]" "\[:lower:\]" < fib1.f \> fib1.f
python \-m numpy.f2py fib1.f \-m fib2
meson \--wipe builddir
meson compile \-C builddir
cd builddir
python \-c 'import fib2'

Copy to clipboard

However this requires the ability to modify the source which is not always possible. The easiest way to solve this is to let `f2py` deal with it:

python \-m numpy.f2py fib1.f \-m fib2 \--lower
meson \--wipe builddir
meson compile \-C builddir
cd builddir
python \-c 'import fib2'

Copy to clipboard

### Automating wrapper generation[#](https://numpy.org/doc/stable/f2py/buildtools/meson.html#automating-wrapper-generation "Link to this heading")

A major pain point in the workflow defined above, is the manual tracking of inputs. Although it would require more effort to figure out the actual outputs for reasons discussed in [F2PY and build systems](https://numpy.org/doc/stable/f2py/buildtools/index.html#f2py-bldsys)
.

Note

From NumPy `1.22.4` onwards, `f2py` will deterministically generate wrapper files based on the input file Fortran standard (F77 or greater). `--skip-empty-wrappers` can be passed to `f2py` to restore the previous behaviour of only generating wrappers when needed by the input .

However, we can augment our workflow in a straightforward to take into account files for which the outputs are known when the build system is set up.

project('f2py\_examples', 'c',
  version : '0.1',
  license: 'BSD-3',
  meson\_version: '>=0.64.0',
  default\_options : \['warning\_level=2'\],
)

add\_languages('fortran')

py\_mod \= import('python')
py \= py\_mod.find\_installation(pure: false)
py\_dep \= py.dependency()

incdir\_numpy \= run\_command(py,
  \['-c', 'import os; os.chdir(".."); import numpy; print(numpy.get\_include())'\],
  check : true
).stdout().strip()

incdir\_f2py \= run\_command(py,
    \['-c', 'import os; os.chdir(".."); import numpy.f2py; print(numpy.f2py.get\_include())'\],
    check : true
).stdout().strip()

fibby\_source \= custom\_target('fibbymodule.c',
  input : \['fib1.f'\],  \# .f so no F90 wrappers
  output : \['fibbymodule.c', 'fibby-f2pywrappers.f'\],
  command : \[py, '-m', 'numpy.f2py', '@INPUT@', '-m', 'fibby', '--lower'\]
)

inc\_np \= include\_directories(incdir\_numpy, incdir\_f2py)

py.extension\_module('fibby',
  \['fib1.f', fibby\_source\],
  incdir\_f2py / 'fortranobject.c',
  include\_directories: inc\_np,
  dependencies : py\_dep,
  install : true
)

Copy to clipboard

This can be compiled and run as before.

rm \-rf builddir
meson setup builddir
meson compile \-C builddir
cd builddir
python \-c "import numpy as np; import fibby; a = np.zeros(9); fibby.fib(a); print (a)"
\# \[ 0.  1.  1.  2.  3.  5.  8. 13. 21.\]

Copy to clipboard

Salient points[#](https://numpy.org/doc/stable/f2py/buildtools/meson.html#salient-points "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

It is worth keeping in mind the following:

*   It is not possible to use SCREAMCASE in this context, so either the contents of the `.f` file or the generated wrapper `.c` needs to be lowered to regular letters; which can be facilitated by the `--lower` option of `F2PY`
    

On this page