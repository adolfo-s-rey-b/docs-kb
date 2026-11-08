[Skip to main content](https://numpy.org/doc/stable/reference/distutils_status_migration.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Status of `numpy.distutils` and migration advice[#](https://numpy.org/doc/stable/reference/distutils_status_migration.html#status-of-numpy-distutils-and-migration-advice "Link to this heading")

==================================================================================================================================================================================================

`numpy.distutils` was removed in NumPy `2.5.0`.

Migration advice[#](https://numpy.org/doc/stable/reference/distutils_status_migration.html#migration-advice "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

There are several build systems which are good options to migrate to. Assuming you have compiled code in your package (if not, you have several good options, e.g. the build backends offered by Poetry, Hatch or PDM) and you want to be using a well-designed, modern and reliable build system, we recommend:

1.  [Meson](https://mesonbuild.com/)
    , and the [meson-python](https://meson-python.readthedocs.io/)
     build backend
    
2.  [CMake](https://cmake.org/)
    , and the [scikit-build-core](https://scikit-build-core.readthedocs.io/en/latest/)
     build backend
    

If you have modest needs (only simple Cython/C extensions; no need for Fortran, BLAS/LAPACK, nested `setup.py` files, or other features of `numpy.distutils`) and have been happy with `numpy.distutils`, you can also consider switching to `setuptools`. Note that most functionality of `numpy.distutils` is unlikely to be ported to `setuptools`.

### Moving to Meson[#](https://numpy.org/doc/stable/reference/distutils_status_migration.html#moving-to-meson "Link to this heading")

SciPy has moved to Meson and meson-python for its 1.9.0 release. During this process, remaining issues with Meson’s Python support and feature parity with `numpy.distutils` were resolved. _Note: parity means a large superset (because Meson is a good general-purpose build system); only a few BLAS/LAPACK library selection niceties are missing_. SciPy uses almost all functionality that `numpy.distutils` offers, so if SciPy has successfully made a release with Meson as the build system, there should be no blockers left to migrate, and SciPy will be a good reference for other packages who are migrating. For more details about the SciPy migration, see:

*   [RFC: switch to Meson as a build system](https://github.com/scipy/scipy/issues/13615)
    
*   [Tracking issue for Meson support](https://github.com/rgommers/scipy/issues/22)
    

NumPy migrated to Meson for the 1.26 release.

### Moving to CMake / scikit-build[#](https://numpy.org/doc/stable/reference/distutils_status_migration.html#moving-to-cmake-scikit-build "Link to this heading")

The next generation of scikit-build is called [scikit-build-core](https://scikit-build-core.readthedocs.io/en/latest/)
. Where the older `scikit-build` used `setuptools` underneath, the rewrite does not. Like Meson, CMake is a good general-purpose build system.

### Moving to `setuptools`[#](https://numpy.org/doc/stable/reference/distutils_status_migration.html#moving-to-setuptools "Link to this heading")

For projects that only use `numpy.distutils` for historical reasons, and do not actually use features beyond those that `setuptools` also supports, moving to `setuptools` is likely the solution which costs the least effort. To assess that, there are the `numpy.distutils` features that are _not_ present in `setuptools`:

*   Nested `setup.py` files
    
*   Fortran build support
    
*   BLAS/LAPACK library support (OpenBLAS, MKL, ATLAS, Netlib LAPACK/BLAS, BLIS, 64-bit ILP interface, etc.)
    
*   Support for a few other scientific libraries, like FFTW and UMFPACK
    
*   Better MinGW support
    
*   Per-compiler build flag customization (e.g. _\-O3_ and _SSE2_ flags are default)
    
*   a simple user build config system, see [site.cfg.example](https://github.com/numpy/numpy/blob/v1.25.2/site.cfg.example)
    
*   SIMD intrinsics support
    
*   Support for the NumPy-specific `.src` templating format for `.c`/`.h` files
    

The most widely used feature is nested `setup.py` files. In case a project uses only a couple of `setup.py` files, it also could make sense to simply aggregate all the content of those files into a single `setup.py` file and then move to `setuptools`. This involves dropping all `Configuration` instances, and using `Extension` instead. E.g.,:

from distutils.core import setup
from distutils.extension import Extension
setup(name\='foobar',
      version\='1.0',
      ext\_modules\=\[\
          Extension('foopkg.foo', \['foo.c'\]),\
          Extension('barpkg.bar', \['bar.c'\]),\
          \],
      )

Copy to clipboard

For more details, see the [setuptools documentation](https://setuptools.pypa.io/en/latest/setuptools.html)

On this page