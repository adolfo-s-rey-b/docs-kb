[Skip to main content](https://numpy.org/doc/stable/building/redistributable_binaries.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/building/redistributable_binaries.html)
[2.5 (stable)](https://numpy.org/doc/stable/building/redistributable_binaries.html)
[2.4](https://numpy.org/doc/2.4/building/redistributable_binaries.html)
[2.3](https://numpy.org/doc/2.3/building/redistributable_binaries.html)
[2.2](https://numpy.org/doc/2.2/building/redistributable_binaries.html)
[2.1](https://numpy.org/doc/2.1/building/redistributable_binaries.html)
[2.0](https://numpy.org/doc/2.0/building/redistributable_binaries.html)
[1.26](https://numpy.org/doc/1.26/building/redistributable_binaries.html)
[1.25](https://numpy.org/doc/1.25/building/redistributable_binaries.html)
[1.24](https://numpy.org/doc/1.24/building/redistributable_binaries.html)
[1.23](https://numpy.org/doc/1.23/building/redistributable_binaries.html)
[1.22](https://numpy.org/doc/1.22/building/redistributable_binaries.html)
[1.21](https://numpy.org/doc/1.21/building/redistributable_binaries.html)
[1.20](https://numpy.org/doc/1.20/building/redistributable_binaries.html)
[1.19](https://numpy.org/doc/1.19/building/redistributable_binaries.html)
[1.18](https://numpy.org/doc/1.18/building/redistributable_binaries.html)
[1.17](https://numpy.org/doc/1.17/building/redistributable_binaries.html)
[1.16](https://numpy.org/doc/1.16/building/redistributable_binaries.html)
[1.15](https://numpy.org/doc/1.15/building/redistributable_binaries.html)
[1.14](https://numpy.org/doc/1.14/building/redistributable_binaries.html)
[1.13](https://numpy.org/doc/1.13/building/redistributable_binaries.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Building redistributable binaries[#](https://numpy.org/doc/stable/building/redistributable_binaries.html#building-redistributable-binaries "Link to this heading")

===================================================================================================================================================================

When `python -m build` or `pip wheel` is used to build a NumPy wheel, that wheel will rely on external shared libraries (at least for BLAS/LAPACK and a Fortran compiler runtime library, perhaps other libraries). Such wheels therefore will only run on the system on which they are built. See [the pypackaging-native content under “Building and installing or uploading artifacts”](https://pypackaging-native.github.io/meta-topics/build_steps_conceptual/#building-and-installing-or-uploading-artifacts)
 for more context on that.

A wheel like that is therefore an intermediate stage to producing a binary that can be distributed. That final binary may be a wheel - in that case, run `auditwheel` (Linux), `delocate` (macOS) or `delvewheel` (Windows) to vendor the required shared libraries into the wheel.

The final binary may also be in another packaging format (e.g., a `.rpm`, `.deb` or `.conda` package). In that case, there are packaging ecosystem-specific tools to first install the wheel into a staging area, then making the extension modules in that install location relocatable (e.g., by rewriting RPATHs), and then repackaging it into the final package format.