[Skip to main content](https://numpy.org/doc/stable/building/blas_lapack.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/building/blas_lapack.html)
[2.5 (stable)](https://numpy.org/doc/stable/building/blas_lapack.html)
[2.4](https://numpy.org/doc/2.4/building/blas_lapack.html)
[2.3](https://numpy.org/doc/2.3/building/blas_lapack.html)
[2.2](https://numpy.org/doc/2.2/building/blas_lapack.html)
[2.1](https://numpy.org/doc/2.1/building/blas_lapack.html)
[2.0](https://numpy.org/doc/2.0/building/blas_lapack.html)
[1.26](https://numpy.org/doc/1.26/building/blas_lapack.html)
[1.25](https://numpy.org/doc/1.25/building/blas_lapack.html)
[1.24](https://numpy.org/doc/1.24/building/blas_lapack.html)
[1.23](https://numpy.org/doc/1.23/building/blas_lapack.html)
[1.22](https://numpy.org/doc/1.22/building/blas_lapack.html)
[1.21](https://numpy.org/doc/1.21/building/blas_lapack.html)
[1.20](https://numpy.org/doc/1.20/building/blas_lapack.html)
[1.19](https://numpy.org/doc/1.19/building/blas_lapack.html)
[1.18](https://numpy.org/doc/1.18/building/blas_lapack.html)
[1.17](https://numpy.org/doc/1.17/building/blas_lapack.html)
[1.16](https://numpy.org/doc/1.16/building/blas_lapack.html)
[1.15](https://numpy.org/doc/1.15/building/blas_lapack.html)
[1.14](https://numpy.org/doc/1.14/building/blas_lapack.html)
[1.13](https://numpy.org/doc/1.13/building/blas_lapack.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

BLAS and LAPACK[#](https://numpy.org/doc/stable/building/blas_lapack.html#blas-and-lapack "Link to this heading")

==================================================================================================================

Default behavior for BLAS and LAPACK selection[#](https://numpy.org/doc/stable/building/blas_lapack.html#default-behavior-for-blas-and-lapack-selection "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When a NumPy build is invoked, BLAS and LAPACK library detection happens automatically. The build system will attempt to locate a suitable library, and try a number of known libraries in a certain order - most to least performant. A typical order is: MKL, Accelerate, OpenBLAS, FlexiBLAS, BLIS, plain `libblas`/`liblapack`. This may vary per platform or over releases. That order, and which libraries are tried, can be changed through the `blas-order` and `lapack-order` build options, for example:

$ python -m pip install . -Csetup-args=-Dblas-order=openblas,mkl,blis -Csetup-args=-Dlapack-order=openblas,mkl,lapack

Copy to clipboard

The first suitable library that is found will be used. In case no suitable library is found, the NumPy build will print a warning and then use (slow!) NumPy-internal fallback routines. In order to disallow use of those slow routines, the `allow-noblas` build option can be used:

$ python -m pip install . -Csetup-args=-Dallow-noblas=false

Copy to clipboard

By default the LP64 (32-bit integer) interface to BLAS and LAPACK will be used. For building against the ILP64 (64-bit integer) interface, one must use the `use-ilp64` build option:

$ python -m pip install . -Csetup-args=-Duse-ilp64=true

Copy to clipboard

Selecting specific BLAS and LAPACK libraries[#](https://numpy.org/doc/stable/building/blas_lapack.html#selecting-specific-blas-and-lapack-libraries "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The `blas` and `lapack` build options are set to “auto” by default, which means trying all known libraries. If you want to use a specific library, you can set these build options to the library name (typically the lower-case name that `pkg-config` expects). For example, to select plain `libblas` and `liblapack` (this is typically Netlib BLAS/LAPACK on Linux distros, and can be dynamically switched between implementations on conda-forge), use:

$ # for a development build
$ spin build -C-Dblas=blas -C-Dlapack=lapack

$ # to build and install a wheel
$ python -m build -Csetup-args=-Dblas=blas -Csetup-args=-Dlapack=lapack
$ pip install dist/numpy\*.whl

$ # Or, with pip>=23.1, this works too:
$ python -m pip install . -Csetup-args=-Dblas=blas -Csetup-args=-Dlapack=lapack

Copy to clipboard

Other options that should work (as long as they’re installed with `pkg-config` support; otherwise they may still be detected but things are inherently more fragile) include `openblas`, `mkl`, `accelerate`, `atlas` and `blis`.

Using pkg-config to detect libraries in a nonstandard location[#](https://numpy.org/doc/stable/building/blas_lapack.html#using-pkg-config-to-detect-libraries-in-a-nonstandard-location "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The way BLAS and LAPACK detection works under the hood is that Meson tries to discover the specified libraries first with `pkg-config`, and then with CMake. If all you have is a standalone shared library file (e.g., `armpl_lp64.so` in `/a/random/path/lib/` and a corresponding header file in `/a/random/path/include/`), then what you have to do is craft your own pkg-config file. It should have a matching name (so in this example, `armpl_lp64.pc`) and may be located anywhere. The `PKG_CONFIG_PATH` environment variable should be set to point to the location of the `.pc` file. The contents of that file should be:

libdir=/path/to/library-dir      # e.g., /a/random/path/lib
includedir=/path/to/include-dir  # e.g., /a/random/path/include
version=1.2.3                    # set to actual version
extralib=-lm -lpthread -lgfortran   # if needed, the flags to link in dependencies
Name: armpl\_lp64
Description: ArmPL - Arm Performance Libraries
Version: ${version}
Libs: -L${libdir} -larmpl\_lp64      # linker flags
Libs.private: ${extralib}
Cflags: -I${includedir}

Copy to clipboard

To check that this works as expected, you should be able to run:

$ pkg-config --libs armpl\_lp64
-L/path/to/library-dir -larmpl\_lp64
$ pkg-config --cflags armpl\_lp64
-I/path/to/include-dir

Copy to clipboard

Full list of BLAS and LAPACK related build options[#](https://numpy.org/doc/stable/building/blas_lapack.html#full-list-of-blas-and-lapack-related-build-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

BLAS and LAPACK are complex dependencies. Some libraries have more options that are exposed via build options (see `meson.options` in the root of the repo for all of NumPy’s build options).

*   `blas`: name of the BLAS library to use (default: `auto`),
    
*   `lapack`: name of the LAPACK library to use (default: `auto`),
    
*   `allow-noblas`: whether or not to allow building without external BLAS/LAPACK libraries (default: `true`),
    
*   `blas-order`: order of BLAS libraries to try detecting (default may vary per platform),
    
*   `lapack-order`: order of LAPACK libraries to try detecting,
    
*   `use-ilp64`: whether to use the ILP64 interface (default: `false`),
    
*   `blas-symbol-suffix`: the symbol suffix to use for the detected libraries (default: `auto`),
    
*   `mkl-threading`: which MKL threading layer to use, one of `seq`, `iomp`, `gomp`, `tbb` (default: `auto`).
    

On this page