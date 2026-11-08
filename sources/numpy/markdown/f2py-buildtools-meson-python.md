[Skip to main content](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/f2py/buildtools/meson-python.html)
[2.5 (stable)](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html)
[2.4](https://numpy.org/doc/2.4/f2py/buildtools/meson-python.html)
[2.3](https://numpy.org/doc/2.3/f2py/buildtools/meson-python.html)
[2.2](https://numpy.org/doc/2.2/f2py/buildtools/meson-python.html)
[2.1](https://numpy.org/doc/2.1/f2py/buildtools/meson-python.html)
[2.0](https://numpy.org/doc/2.0/f2py/buildtools/meson-python.html)
[1.26](https://numpy.org/doc/1.26/f2py/buildtools/meson-python.html)
[1.25](https://numpy.org/doc/1.25/f2py/buildtools/meson-python.html)
[1.24](https://numpy.org/doc/1.24/f2py/buildtools/meson-python.html)
[1.23](https://numpy.org/doc/1.23/f2py/buildtools/meson-python.html)
[1.22](https://numpy.org/doc/1.22/f2py/buildtools/meson-python.html)
[1.21](https://numpy.org/doc/1.21/f2py/buildtools/meson-python.html)
[1.20](https://numpy.org/doc/1.20/f2py/buildtools/meson-python.html)
[1.19](https://numpy.org/doc/1.19/f2py/buildtools/meson-python.html)
[1.18](https://numpy.org/doc/1.18/f2py/buildtools/meson-python.html)
[1.17](https://numpy.org/doc/1.17/f2py/buildtools/meson-python.html)
[1.16](https://numpy.org/doc/1.16/f2py/buildtools/meson-python.html)
[1.15](https://numpy.org/doc/1.15/f2py/buildtools/meson-python.html)
[1.14](https://numpy.org/doc/1.14/f2py/buildtools/meson-python.html)
[1.13](https://numpy.org/doc/1.13/f2py/buildtools/meson-python.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Distributing F2PY extensions with `meson-python`[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#distributing-f2py-extensions-with-meson-python "Link to this heading")

==========================================================================================================================================================================================

The [Using via meson](https://numpy.org/doc/stable/f2py/buildtools/meson.html#f2py-meson)
 page covers building F2PY extensions using raw `meson` commands. This page shows how to package those extensions into installable Python distributions (sdists and wheels) using [meson-python](https://meson-python.readthedocs.io/)
 as the PEP 517 build backend.

This is the recommended approach for distributing F2PY-wrapped Fortran code as a Python package on PyPI or for local `pip install` workflows.

Note

`meson-python` replaced `setuptools` / `numpy.distutils` as the standard way to build and distribute compiled extensions in the NumPy and SciPy ecosystem. See [Status of numpy.distutils and migration advice](https://numpy.org/doc/stable/reference/distutils_status_migration.html#distutils-status-migration)
 for background.

Prerequisites[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#prerequisites "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

You need:

*   A C compiler
    
*   A Fortran compiler (`gfortran`, `ifort`, `ifx`, `flang-new`, etc.), if you use any Fortran code in your package
    
*   Python >= 3.10
    
*   `meson`, `meson-python`, and `numpy` (installed automatically during the build when listed in `build-system.requires`)
    

Minimal example[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#minimal-example "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

The project below wraps a Fortran `fib` subroutine into an importable Python package called `fib_wrapper`.

Project layout:

fib\_wrapper/           # project root
├── fib.f90            # Fortran source
├── fib\_wrapper/       # Python package directory
│   └── \_\_init\_\_.py
├── meson.build
└── pyproject.toml

Copy to clipboard

### Fortran source[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#fortran-source "Link to this heading")

Save the following as `fib.f90`:

subroutine fib(a, n)
  use iso\_c\_binding
  integer(c\_int), intent(in) :: n
  integer(c\_int), intent(out) :: a(n)
  integer :: i
  do i \= 1, n
     if (i \== 1) then
        a(i) \= 0
     else if (i \== 2) then
        a(i) \= 1
     else
        a(i) \= a(i \- 1) + a(i \- 2)
     end if
  end do
end subroutine fib

Copy to clipboard

### `pyproject.toml`[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#pyproject-toml "Link to this heading")

\[build-system\]
\# numpy>=2.0 is required for dependency('numpy') support in meson.build
requires \= \["meson-python>=0.15.0", "numpy>=2.0"\]
build-backend \= "mesonpy"

\[project\]
name \= "fib\_wrapper"
version \= "0.1.0"
requires-python \= ">=3.10"
dependencies \= \["numpy"\]

Copy to clipboard

Two entries matter here:

*   `build-backend = "mesonpy"` tells build frontends to use `meson-python`.
    
*   `requires` lists build-time dependencies. `numpy >= 2.0` is required so that `f2py`, the NumPy headers, and `dependency('numpy')` support in Meson are available during compilation.
    

### `meson.build`[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#meson-build "Link to this heading")

project('fib\_wrapper', 'c',
  version : '0.1.0',
  meson\_version: '>=1.1.0',
  default\_options : \['warning\_level=2'\],
)

add\_languages('fortran', native: false)

py \= import('python').find\_installation(pure: false)

\# NumPy >=2.0 provides include dirs via dependency()
np\_dep \= dependency('numpy')

incdir\_f2py \= run\_command(py,
  \['-c', 'import numpy.f2py; print(numpy.f2py.get\_include())'\],
  check : true
).stdout().strip()

\# f2py include dir (for fortranobject.h) is not in dependency('numpy'),
\# so add it separately
f2py\_dep \= declare\_dependency(
  include\_directories : incdir\_f2py,
)

\# Generate the f2py wrappers
fib\_source \= custom\_target('fibmodule.c',
  input : \['fib.f90'\],
  output : \['fibmodule.c', 'fib-f2pywrappers.f'\],
  command : \[py, '-m', 'numpy.f2py', '@INPUT@', '-m', 'fib', '--lower'\]
)

py.extension\_module('fib',
  \['fib.f90', fib\_source, incdir\_f2py / 'fortranobject.c'\],
  dependencies : \[np\_dep, f2py\_dep\],
  subdir: 'fib\_wrapper',
  install : true,
)

\# Install the Python package files
py.install\_sources(
  'fib\_wrapper/\_\_init\_\_.py',
  subdir: 'fib\_wrapper',
)

Copy to clipboard

Note

The file is stored as `meson_mesonpy.build` in the documentation source tree to avoid collisions with other examples. In your project, name it `meson.build`.

The `meson.build` file does four things:

1.  Uses `dependency('numpy')` to locate NumPy headers, and a `declare_dependency` to add the F2PY include directory (for `fortranobject.h`).
    
2.  Runs `f2py` via `custom_target` to generate the C wrapper sources.
    
3.  Compiles the generated C code together with the Fortran source into a Python extension module using `py.extension_module`.
    
4.  Installs `__init__.py` into the package directory so the result is a proper Python package.
    

The `subdir: 'fib_wrapper'` argument on the extension module is required so that the compiled `fib` shared library is installed inside the `fib_wrapper/` package directory, next to `__init__.py`. Without it the extension would be installed at the top level and `import fib_wrapper` would not find the `fib` extension. The resulting installed layout is:

site-packages/
└── fib\_wrapper/
    ├── \_\_init\_\_.py        # from .fib import fib
    └── fib.cpython-\*.so   # compiled extension module

Copy to clipboard

### `__init__.py`[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#init-py "Link to this heading")

A minimal `__init__.py` re-exports the wrapped function:

from .fib import fib

Copy to clipboard

Building and installing[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#building-and-installing "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

### Editable install (development)[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#editable-install-development "Link to this heading")

pip install \--no-build-isolation \--editable .

Copy to clipboard

`--no-build-isolation` reuses the current environment, which is useful when iterating. This requires `meson-python`, `meson`, `ninja`, and `numpy` to already be installed.

### Building a wheel[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#building-a-wheel "Link to this heading")

\# If you don't yet have \`pypa/build\` installed: \`pip install build\`
python \-m build \--wheel

Copy to clipboard

The resulting `.whl` file in `dist/` can be uploaded to PyPI, or installed elsewhere with `pip install dist/fib_wrapper-0.1.0-*.whl`.

### Verifying the install[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#verifying-the-install "Link to this heading")

\>>> from fib\_wrapper import fib
\>>> fib(10)
array(\[ 0,  1,  1,  2,  3,  5,  8, 13, 21, 34\], dtype=int32)

Copy to clipboard

Customizing the Fortran compiler[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#customizing-the-fortran-compiler "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------

`meson-python` delegates compiler selection to `meson`. By default, `meson` will choose the first Fortran compiler it finds on the PATH. If you want more control over Fortran compiler selection, set the `FC` environment variable before building:

FC\=ifx python \-m build \--wheel

Copy to clipboard

For more control, use a [Meson native file](https://mesonbuild.com/Native-environments.html)
:

; native.ini
\[binaries\]
fortran \= 'ifx'
c \= 'icx'

Copy to clipboard

python \-m build \--wheel \-Csetup-args\="--native-file=native.ini"

Copy to clipboard

Adding dependencies (BLAS, LAPACK, etc.)[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#adding-dependencies-blas-lapack-etc "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Use `dependency()` in `meson.build` to link against system libraries:

lapack\_dep = dependency('lapack')

py.extension\_module('mymod',
  \[sources, generated, incdir\_f2py / 'fortranobject.c'\],
  dependencies : \[np\_dep, f2py\_dep, lapack\_dep\],
  install : true,
)

Copy to clipboard

`meson` resolves dependencies through `pkg-config`, CMake, or its own detection logic. See the [Meson dependency documentation](https://mesonbuild.com/Dependencies.html)
 for details.

Differences from the `scikit-build-core` workflow[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#differences-from-the-scikit-build-core-workflow "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `scikit-build-core` approach documented in [Using via scikit-build](https://numpy.org/doc/stable/f2py/buildtools/skbuild.html#f2py-skbuild)
 uses CMake under the hood. `meson-python` provides:

*   Native Fortran compiler support in `meson` (no CMake layer).
    
*   Direct integration with `pip` / `build` via PEP 517.
    
*   The same build system used by NumPy and SciPy themselves.
    

Further reading[#](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#further-reading "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

*   [meson-python documentation](https://meson-python.readthedocs.io/)
    
*   [Meson build system](https://mesonbuild.com/)
    
*   [SciPy’s meson build configuration](https://github.com/scipy/scipy/blob/main/meson.build)
     (real-world F2PY usage)
    
*   [Using via meson](https://numpy.org/doc/stable/f2py/buildtools/meson.html#f2py-meson)
     (raw meson build without `meson-python`)
    
*   [Using via scikit-build](https://numpy.org/doc/stable/f2py/buildtools/skbuild.html#f2py-skbuild)
     (alternative using `scikit-build-core` / CMake)
    
*   [1 Migrating to meson](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#f2py-meson-distutils)
     (migration from `distutils`)
    

On this page