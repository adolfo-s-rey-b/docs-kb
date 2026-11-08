[Skip to main content](https://numpy.org/doc/stable/building/introspecting_a_build.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/building/introspecting_a_build.html)
[2.5 (stable)](https://numpy.org/doc/stable/building/introspecting_a_build.html)
[2.4](https://numpy.org/doc/2.4/building/introspecting_a_build.html)
[2.3](https://numpy.org/doc/2.3/building/introspecting_a_build.html)
[2.2](https://numpy.org/doc/2.2/building/introspecting_a_build.html)
[2.1](https://numpy.org/doc/2.1/building/introspecting_a_build.html)
[2.0](https://numpy.org/doc/2.0/building/introspecting_a_build.html)
[1.26](https://numpy.org/doc/1.26/building/introspecting_a_build.html)
[1.25](https://numpy.org/doc/1.25/building/introspecting_a_build.html)
[1.24](https://numpy.org/doc/1.24/building/introspecting_a_build.html)
[1.23](https://numpy.org/doc/1.23/building/introspecting_a_build.html)
[1.22](https://numpy.org/doc/1.22/building/introspecting_a_build.html)
[1.21](https://numpy.org/doc/1.21/building/introspecting_a_build.html)
[1.20](https://numpy.org/doc/1.20/building/introspecting_a_build.html)
[1.19](https://numpy.org/doc/1.19/building/introspecting_a_build.html)
[1.18](https://numpy.org/doc/1.18/building/introspecting_a_build.html)
[1.17](https://numpy.org/doc/1.17/building/introspecting_a_build.html)
[1.16](https://numpy.org/doc/1.16/building/introspecting_a_build.html)
[1.15](https://numpy.org/doc/1.15/building/introspecting_a_build.html)
[1.14](https://numpy.org/doc/1.14/building/introspecting_a_build.html)
[1.13](https://numpy.org/doc/1.13/building/introspecting_a_build.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Introspecting build steps[#](https://numpy.org/doc/stable/building/introspecting_a_build.html#introspecting-build-steps "Link to this heading")

================================================================================================================================================

When you have an issue with a particular Python extension module or other build target, there are a number of ways to figure out what the build system is doing exactly. Beyond looking at the `meson.build` content for the target of interest, these include:

1.  Reading the generated `build.ninja` file in the build directory,
    
2.  Using `meson introspect` to learn more about build options, dependencies and flags used for the target,
    
3.  Reading `<build-dir>/meson-info/*.json` for details on discovered dependencies, where Meson plans to install files to, etc.
    

These things are all available after the configure stage of the build (i.e., `meson setup`) has run. It is typically more effective to look at this information, rather than running the build and reading the full build log.

For more details on this topic, see the [SciPy doc page on build introspection](https://scipy.github.io/devdocs/building/introspecting_a_build.html)
.