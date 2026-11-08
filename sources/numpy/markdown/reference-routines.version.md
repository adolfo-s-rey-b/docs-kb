[Skip to main content](https://numpy.org/doc/stable/reference/routines.version.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Version information[#](https://numpy.org/doc/stable/reference/routines.version.html#version-information "Link to this heading")

================================================================================================================================

The `numpy.version` submodule includes several constants that expose more detailed information about the exact version of the installed `numpy` package:

numpy.version.version[#](https://numpy.org/doc/stable/reference/routines.version.html#numpy.version.version "Link to this definition")

Version string for the installed package - matches `numpy.__version__`.

numpy.version.full\_version[#](https://numpy.org/doc/stable/reference/routines.version.html#numpy.version.full_version "Link to this definition")

Version string - the same as `numpy.version.version`.

numpy.version.short\_version[#](https://numpy.org/doc/stable/reference/routines.version.html#numpy.version.short_version "Link to this definition")

Version string without any local build identifiers.

Examples

\>>> np.\_\_version\_\_
'2.1.0.dev0+git20240319.2ea7ce0'  # may vary
\>>> np.version.short\_version
'2.1.0.dev0'  # may vary

Copy to clipboard

numpy.version.git\_revision[#](https://numpy.org/doc/stable/reference/routines.version.html#numpy.version.git_revision "Link to this definition")

String containing the git hash of the commit from which `numpy` was built.

numpy.version.release[#](https://numpy.org/doc/stable/reference/routines.version.html#numpy.version.release "Link to this definition")

`True` if this version is a `numpy` release, `False` if a dev version.

On this page