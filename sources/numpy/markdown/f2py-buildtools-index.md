[Skip to main content](https://numpy.org/doc/stable/f2py/buildtools/index.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

F2PY and build systems[#](https://numpy.org/doc/stable/f2py/buildtools/index.html#f2py-and-build-systems "Link to this heading")

=================================================================================================================================

In this section we will cover the various popular build systems and their usage with `f2py`.

Changed in version NumPy: 1.26.x

The default build system for `f2py` has traditionally been through the enhanced `numpy.distutils` module. This module is based on `distutils` which was removed in `NumPy2.5.0` in **June 2026**. Like the rest of NumPy and SciPy, `f2py` uses `meson` now, see [Status of numpy.distutils and migration advice](https://numpy.org/doc/stable/reference/distutils_status_migration.html#distutils-status-migration)
 for some more details.

> All changes to `f2py` are tested on SciPy, so their [CI configuration](https://docs.scipy.org/doc/scipy/dev/toolchain.html#official-builds)
>  is always supported.

Note

See [1 Migrating to meson](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#f2py-meson-distutils)
 for migration information.

Basic concepts[#](https://numpy.org/doc/stable/f2py/buildtools/index.html#basic-concepts "Link to this heading")

-----------------------------------------------------------------------------------------------------------------

Building an extension module which includes Python and Fortran consists of:

*   Fortran source(s)
    
*   One or more generated files from `f2py`
    
    *   A `C` wrapper file is always created
        
    *   Code with modules require an additional `.f90` wrapper
        
    *   Code with functions generate an additional `.f` wrapper
        
*   `fortranobject.{c,h}`
    
    *   Distributed with `numpy`
        
    *   Can be queried via `python -c "import numpy.f2py; print(numpy.f2py.get_include())"`
        
*   NumPy headers
    
    *   Can be queried via `python -c "import numpy; print(numpy.get_include())"`
        
*   Python libraries and development headers
    

Broadly speaking there are three cases which arise when considering the outputs of `f2py`:

Fortran 77 programs

*   Input file `blah.f`
    
*   Generates
    
    *   `blahmodule.c`
        
    *   `blah-f2pywrappers.f`
        

When no `COMMON` blocks are present only a `C` wrapper file is generated. Wrappers are also generated to rewrite assumed shape arrays as automatic arrays.

Fortran 90 programs

*   Input file `blah.f90`
    
*   Generates:
    
    *   `blahmodule.c`
        
    *   `blah-f2pywrappers.f`
        
    *   `blah-f2pywrappers2.f90`
        

The `f90` wrapper is used to handle code which is subdivided into modules. The `f` wrapper makes `subroutines` for `functions`. It rewrites assumed shape arrays as automatic arrays.

Signature files

*   Input file `blah.pyf`
    
*   Generates:
    
    *   `blahmodule.c`
        
    *   `blah-f2pywrappers2.f90` (occasionally)
        
    *   `blah-f2pywrappers.f` (occasionally)
        

Signature files `.pyf` do not signal their language standard via the file extension, they may generate the F90 and F77 specific wrappers depending on their contents; which shifts the burden of checking for generated files onto the build system.

Changed in version NumPy: `1.22.4`

`f2py` will deterministically generate wrapper files based on the input file Fortran standard (F77 or greater). `--skip-empty-wrappers` can be passed to `f2py` to restore the previous behaviour of only generating wrappers when needed by the input .

In theory keeping the above requirements in hand, any build system can be adapted to generate `f2py` extension modules. Here we will cover a subset of the more popular systems.

Note

`make` has no place in a modern multi-language setup, and so is not discussed further.

Build systems[#](https://numpy.org/doc/stable/f2py/buildtools/index.html#build-systems "Link to this heading")

---------------------------------------------------------------------------------------------------------------

*   [Using via `meson`](https://numpy.org/doc/stable/f2py/buildtools/meson.html)
    *   [Fibonacci walkthrough (F77)](https://numpy.org/doc/stable/f2py/buildtools/meson.html#fibonacci-walkthrough-f77)
        
    *   [Salient points](https://numpy.org/doc/stable/f2py/buildtools/meson.html#salient-points)
        
*   [Distributing F2PY extensions with `meson-python`](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html)
    *   [Prerequisites](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#prerequisites)
        
    *   [Minimal example](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#minimal-example)
        
    *   [Building and installing](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#building-and-installing)
        
    *   [Customizing the Fortran compiler](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#customizing-the-fortran-compiler)
        
    *   [Adding dependencies (BLAS, LAPACK, etc.)](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#adding-dependencies-blas-lapack-etc)
        
    *   [Differences from the `scikit-build-core` workflow](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#differences-from-the-scikit-build-core-workflow)
        
    *   [Further reading](https://numpy.org/doc/stable/f2py/buildtools/meson-python.html#further-reading)
        
*   [Using via `cmake`](https://numpy.org/doc/stable/f2py/buildtools/cmake.html)
    *   [Fibonacci walkthrough (F77)](https://numpy.org/doc/stable/f2py/buildtools/cmake.html#fibonacci-walkthrough-f77)
        
*   [Using via `scikit-build`](https://numpy.org/doc/stable/f2py/buildtools/skbuild.html)
    *   [Fibonacci walkthrough (F77)](https://numpy.org/doc/stable/f2py/buildtools/skbuild.html#fibonacci-walkthrough-f77)
        
*   [1 Migrating to `meson`](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html)
    *   [1.1 Baseline](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#baseline)
        
    *   [1.2 Compilation options](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#compilation-options)
        
    *   [1.3 Customizing builds](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#customizing-builds)
        

On this page