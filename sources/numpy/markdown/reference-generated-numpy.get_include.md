[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.get_include.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.get_include.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.get_include.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.get_include.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.get_include.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.get_include.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.get_include.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.get_include.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.get_include.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.get_include.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.get_include.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.get_include.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.get_include.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.get_include.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.get_include.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.get_include.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.get_include.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.get_include.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.get_include.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.get_include.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.get_include.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.get_include.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.get\_include[#](https://numpy.org/doc/stable/reference/generated/numpy.get_include.html#numpy-get-include "Link to this heading")

========================================================================================================================================

numpy.get\_include()[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_utils_impl.py#L77-L120)
[#](https://numpy.org/doc/stable/reference/generated/numpy.get_include.html#numpy.get_include "Link to this definition")

Return the directory that contains the NumPy \*.h header files.

Extension modules that need to compile against NumPy may need to use this function to locate the appropriate include directory.

Notes

When using `setuptools`, for example in `setup.py`:

import numpy as np
...
Extension('extension\_name', ...
          include\_dirs\=\[np.get\_include()\])
...

Copy to clipboard

Note that a CLI tool `numpy-config` was introduced in NumPy 2.0, using that is likely preferred for build systems other than `setuptools`:

$ numpy-config --cflags
-I/path/to/site-packages/numpy/\_core/include

# Or rely on pkg-config:
$ export PKG\_CONFIG\_PATH=$(numpy-config --pkgconfigdir)
$ pkg-config --cflags
-I/path/to/site-packages/numpy/\_core/include

Copy to clipboard

Examples

Try it in your browser!

\>>> np.get\_include()
'.../site-packages/numpy/core/include'  # may vary

Copy to clipboard

Go BackOpen In Tab

On this page