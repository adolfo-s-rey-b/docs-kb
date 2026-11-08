[Skip to main content](https://numpy.org/doc/stable/f2py/windows/msys2.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/f2py/windows/msys2.html)
[2.5 (stable)](https://numpy.org/doc/stable/f2py/windows/msys2.html)
[2.4](https://numpy.org/doc/2.4/f2py/windows/msys2.html)
[2.3](https://numpy.org/doc/2.3/f2py/windows/msys2.html)
[2.2](https://numpy.org/doc/2.2/f2py/windows/msys2.html)
[2.1](https://numpy.org/doc/2.1/f2py/windows/msys2.html)
[2.0](https://numpy.org/doc/2.0/f2py/windows/msys2.html)
[1.26](https://numpy.org/doc/1.26/f2py/windows/msys2.html)
[1.25](https://numpy.org/doc/1.25/f2py/windows/msys2.html)
[1.24](https://numpy.org/doc/1.24/f2py/windows/msys2.html)
[1.23](https://numpy.org/doc/1.23/f2py/windows/msys2.html)
[1.22](https://numpy.org/doc/1.22/f2py/windows/msys2.html)
[1.21](https://numpy.org/doc/1.21/f2py/windows/msys2.html)
[1.20](https://numpy.org/doc/1.20/f2py/windows/msys2.html)
[1.19](https://numpy.org/doc/1.19/f2py/windows/msys2.html)
[1.18](https://numpy.org/doc/1.18/f2py/windows/msys2.html)
[1.17](https://numpy.org/doc/1.17/f2py/windows/msys2.html)
[1.16](https://numpy.org/doc/1.16/f2py/windows/msys2.html)
[1.15](https://numpy.org/doc/1.15/f2py/windows/msys2.html)
[1.14](https://numpy.org/doc/1.14/f2py/windows/msys2.html)
[1.13](https://numpy.org/doc/1.13/f2py/windows/msys2.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

F2PY and Windows with MSYS2[#](https://numpy.org/doc/stable/f2py/windows/msys2.html#f2py-and-windows-with-msys2 "Link to this heading")

========================================================================================================================================

Follow the standard [installation instructions](https://www.msys2.org/)
. Then, to grab the requisite Fortran compiler with `MVSC`:

\# Assuming a fresh install
pacman \-Syu \# Restart the terminal
pacman \-Su  \# Update packages
\# Get the toolchains
pacman \-S \--needed base-devel gcc-fortran
pacman \-S mingw-w64-x86\_64-toolchain

Copy to clipboard