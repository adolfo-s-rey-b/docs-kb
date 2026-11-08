[Skip to main content](https://numpy.org/doc/stable/building/cpu_simd.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/building/cpu_simd.html)
[2.5 (stable)](https://numpy.org/doc/stable/building/cpu_simd.html)
[2.4](https://numpy.org/doc/2.4/building/cpu_simd.html)
[2.3](https://numpy.org/doc/2.3/building/cpu_simd.html)
[2.2](https://numpy.org/doc/2.2/building/cpu_simd.html)
[2.1](https://numpy.org/doc/2.1/building/cpu_simd.html)
[2.0](https://numpy.org/doc/2.0/building/cpu_simd.html)
[1.26](https://numpy.org/doc/1.26/building/cpu_simd.html)
[1.25](https://numpy.org/doc/1.25/building/cpu_simd.html)
[1.24](https://numpy.org/doc/1.24/building/cpu_simd.html)
[1.23](https://numpy.org/doc/1.23/building/cpu_simd.html)
[1.22](https://numpy.org/doc/1.22/building/cpu_simd.html)
[1.21](https://numpy.org/doc/1.21/building/cpu_simd.html)
[1.20](https://numpy.org/doc/1.20/building/cpu_simd.html)
[1.19](https://numpy.org/doc/1.19/building/cpu_simd.html)
[1.18](https://numpy.org/doc/1.18/building/cpu_simd.html)
[1.17](https://numpy.org/doc/1.17/building/cpu_simd.html)
[1.16](https://numpy.org/doc/1.16/building/cpu_simd.html)
[1.15](https://numpy.org/doc/1.15/building/cpu_simd.html)
[1.14](https://numpy.org/doc/1.14/building/cpu_simd.html)
[1.13](https://numpy.org/doc/1.13/building/cpu_simd.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

CPU support & SIMD[#](https://numpy.org/doc/stable/building/cpu_simd.html#cpu-support-simd "Link to this heading")

===================================================================================================================

NumPy supports a wide range of platforms and CPUs, and includes a significant amount of code optimized for specific CPUs. By default, NumPy targets a baseline with the minimum required SIMD instruction sets that are needed (e.g., SSE4.2 on x86-64 CPUs) and uses dynamic dispatch to use newer instruction sets (e.g., AVX2 and AVX512 on x86-64) when those are detected at runtime.

There are a number of build options that can be used to modify that behavior. The default build settings are chosen for both portability and performance, and should be reasonably close to optimal for creating redistributable binaries as well as local installs. That said, there are reasons one may want to change the default behavior, for example to obtain smaller binaries, to install on very old hardware, to work around bugs, or for testing.

To detect and use all CPU features available on your local machine:

$ python -m pip install . -Csetup-args=-Dcpu-baseline="native" -Csetup-args=-Dcpu-dispatch="none"

Copy to clipboard

To use a lower baseline without any SIMD optimizations, useful for very old CPUs:

$ python -m pip install . -Csetup-args=-Dcpu-baseline="none"

Copy to clipboard

For more usage scenarios and more in-depth information about NumPy’s SIMD support, see [CPU Build Options](https://numpy.org/doc/stable/reference/simd/build-options.html#cpu-build-options)
.