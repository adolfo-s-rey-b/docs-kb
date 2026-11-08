[Skip to main content](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/f2py/buildtools/distutils-to-meson.html)
[2.5 (stable)](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html)
[2.4](https://numpy.org/doc/2.4/f2py/buildtools/distutils-to-meson.html)
[2.3](https://numpy.org/doc/2.3/f2py/buildtools/distutils-to-meson.html)
[2.2](https://numpy.org/doc/2.2/f2py/buildtools/distutils-to-meson.html)
[2.1](https://numpy.org/doc/2.1/f2py/buildtools/distutils-to-meson.html)
[2.0](https://numpy.org/doc/2.0/f2py/buildtools/distutils-to-meson.html)
[1.26](https://numpy.org/doc/1.26/f2py/buildtools/distutils-to-meson.html)
[1.25](https://numpy.org/doc/1.25/f2py/buildtools/distutils-to-meson.html)
[1.24](https://numpy.org/doc/1.24/f2py/buildtools/distutils-to-meson.html)
[1.23](https://numpy.org/doc/1.23/f2py/buildtools/distutils-to-meson.html)
[1.22](https://numpy.org/doc/1.22/f2py/buildtools/distutils-to-meson.html)
[1.21](https://numpy.org/doc/1.21/f2py/buildtools/distutils-to-meson.html)
[1.20](https://numpy.org/doc/1.20/f2py/buildtools/distutils-to-meson.html)
[1.19](https://numpy.org/doc/1.19/f2py/buildtools/distutils-to-meson.html)
[1.18](https://numpy.org/doc/1.18/f2py/buildtools/distutils-to-meson.html)
[1.17](https://numpy.org/doc/1.17/f2py/buildtools/distutils-to-meson.html)
[1.16](https://numpy.org/doc/1.16/f2py/buildtools/distutils-to-meson.html)
[1.15](https://numpy.org/doc/1.15/f2py/buildtools/distutils-to-meson.html)
[1.14](https://numpy.org/doc/1.14/f2py/buildtools/distutils-to-meson.html)
[1.13](https://numpy.org/doc/1.13/f2py/buildtools/distutils-to-meson.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

1 Migrating to `meson`[#](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#migrating-to-meson "Link to this heading")

==========================================================================================================================================

As per the timeline laid out in [Status of numpy.distutils and migration advice](https://numpy.org/doc/stable/reference/distutils_status_migration.html#distutils-status-migration)
, `distutils` has been removed. This page collects common workflows.

Note

This is a **living** document, [pull requests](https://numpy.org/doc/stable/dev/howto-docs.html)
 are very welcome!

1.1 Baseline[#](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#baseline "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

We will start out with a slightly modern variation of the classic Fibonnaci series generator.

! fib.f90
subroutine fib(a, n)
  use iso\_c\_binding
   integer(c\_int), intent(in) :: n
   integer(c\_int), intent(out) :: a(n)
   do i \= 1, n
      if (i .eq. 1) then
         a(i) \= 0.0d0
      elseif (i .eq. 2) then
         a(i) \= 1.0d0
      else
         a(i) \= a(i \- 1) + a(i \- 2)
      end if
   end do
end

Copy to clipboard

This will not win any awards, but can be a reasonable starting point.

1.2 Compilation options[#](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#compilation-options "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

### 1.2.1 Basic Usage[#](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#basic-usage "Link to this heading")

python \-m numpy.f2py \-c fib.f90 \-m fib
❯ python \-c "import fib; print(fib.fib(30))"
\[     0      1      1      2      3      5      8     13     21     34\
     55     89    144    233    377    610    987   1597   2584   4181\
   6765  10946  17711  28657  46368  75025 121393 196418 317811 514229\]

Copy to clipboard

### 1.2.2 Specify the backend[#](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#specify-the-backend "Link to this heading")

python \-m numpy.f2py \-c fib.f90 \-m fib

Copy to clipboard

This is the only option. There used to be a `distutils` backend but it was removed in NumPy2.5.0.

### 1.2.3 Pass a compiler name[#](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#pass-a-compiler-name "Link to this heading")

FC\=gfortran python \-m numpy.f2py \-c fib.f90 \-m fib

Copy to clipboard

Native files can also be used.

Similarly, `CC` can be used in both cases to set the `C` compiler. Since the environment variables are generally pretty common across both, so a small sample is included below.

|     |     |
| --- | --- |
| **Name** | **What** |
| FC  | Fortran compiler |
| CC  | C compiler |
| CFLAGS | C compiler options |
| FFLAGS | Fortran compiler options |
| LDFLAGS | Linker options |
| LD\_LIBRARY\_PATH | Library file locations (Unix) |
| LIBS | Libraries to link against |
| PATH | Search path for executables |
| CXX | C++ compiler |
| CXXFLAGS | C++ compiler options |

Note

For Windows, these may not work very reliably, so [native files](https://mesonbuild.com/Native-environments.html)
 are likely the best bet, or by direct [1.3 Customizing builds](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#customizing-builds)
.

### 1.2.4 Dependencies[#](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#dependencies "Link to this heading")

python \-m numpy.f2py \-c fib.f90 \-m fib \--dep lapack

Copy to clipboard

This maps to `dependency("lapack")` and so can be used for a wide variety of dependencies. They can be [customized further](https://mesonbuild.com/Dependencies.html)
 to use CMake or other systems to resolve dependencies.

### 1.2.5 Libraries[#](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#libraries "Link to this heading")

`meson` is capable of linking against libraries.

python \-m numpy.f2py \-c fib.f90 \-m fib \-lmylib \-L/path/to/mylib

Copy to clipboard

1.3 Customizing builds[#](https://numpy.org/doc/stable/f2py/buildtools/distutils-to-meson.html#customizing-builds "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

python \-m numpy.f2py \-c fib.f90 \-m fib \--build-dir blah

Copy to clipboard

The resulting build can be customized via the [Meson Build How-To Guide](https://mesonbuild.com/howtox.html)
. In fact, the resulting set of files can even be committed directly and used as a meson subproject in a separate codebase.

On this page