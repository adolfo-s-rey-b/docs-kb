[Skip to main content](https://numpy.org/doc/stable/reference/routines.other.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/routines.other.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/routines.other.html)
[2.4](https://numpy.org/doc/2.4/reference/routines.other.html)
[2.3](https://numpy.org/doc/2.3/reference/routines.other.html)
[2.2](https://numpy.org/doc/2.2/reference/routines.other.html)
[2.1](https://numpy.org/doc/2.1/reference/routines.other.html)
[2.0](https://numpy.org/doc/2.0/reference/routines.other.html)
[1.26](https://numpy.org/doc/1.26/reference/routines.other.html)
[1.25](https://numpy.org/doc/1.25/reference/routines.other.html)
[1.24](https://numpy.org/doc/1.24/reference/routines.other.html)
[1.23](https://numpy.org/doc/1.23/reference/routines.other.html)
[1.22](https://numpy.org/doc/1.22/reference/routines.other.html)
[1.21](https://numpy.org/doc/1.21/reference/routines.other.html)
[1.20](https://numpy.org/doc/1.20/reference/routines.other.html)
[1.19](https://numpy.org/doc/1.19/reference/routines.other.html)
[1.18](https://numpy.org/doc/1.18/reference/routines.other.html)
[1.17](https://numpy.org/doc/1.17/reference/routines.other.html)
[1.16](https://numpy.org/doc/1.16/reference/routines.other.html)
[1.15](https://numpy.org/doc/1.15/reference/routines.other.html)
[1.14](https://numpy.org/doc/1.14/reference/routines.other.html)
[1.13](https://numpy.org/doc/1.13/reference/routines.other.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

Miscellaneous routines[#](https://numpy.org/doc/stable/reference/routines.other.html#miscellaneous-routines "Link to this heading")

====================================================================================================================================

Performance tuning[#](https://numpy.org/doc/stable/reference/routines.other.html#performance-tuning "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`setbufsize`](https://numpy.org/doc/stable/reference/generated/numpy.setbufsize.html#numpy.setbufsize "numpy.setbufsize")<br>(size) | Set the size of the buffer used in ufuncs. |
| [`getbufsize`](https://numpy.org/doc/stable/reference/generated/numpy.getbufsize.html#numpy.getbufsize "numpy.getbufsize")<br>() | Return the size of the buffer used in ufuncs. |

Memory ranges[#](https://numpy.org/doc/stable/reference/routines.other.html#memory-ranges "Link to this heading")

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`shares_memory`](https://numpy.org/doc/stable/reference/generated/numpy.shares_memory.html#numpy.shares_memory "numpy.shares_memory")<br>(a, b, /\[, max\_work\]) | Determine if two arrays share memory. |
| [`may_share_memory`](https://numpy.org/doc/stable/reference/generated/numpy.may_share_memory.html#numpy.may_share_memory "numpy.may_share_memory")<br>(a, b, /\[, max\_work\]) | Determine if two arrays might share memory |

Utility[#](https://numpy.org/doc/stable/reference/routines.other.html#utility "Link to this heading")

------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`get_include`](https://numpy.org/doc/stable/reference/generated/numpy.get_include.html#numpy.get_include "numpy.get_include")<br>() | Return the directory that contains the NumPy \*.h header files. |
| [`show_config`](https://numpy.org/doc/stable/reference/generated/numpy.show_config.html#numpy.show_config "numpy.show_config")<br>(\[mode\]) | Show libraries and system information on which NumPy was built and is being used |
| [`show_runtime`](https://numpy.org/doc/stable/reference/generated/numpy.show_runtime.html#numpy.show_runtime "numpy.show_runtime")<br>() | Print information about various resources in the system including available intrinsic support and BLAS/LAPACK library in use |
| [`broadcast_shapes`](https://numpy.org/doc/stable/reference/generated/numpy.broadcast_shapes.html#numpy.broadcast_shapes "numpy.broadcast_shapes")<br>(\*args) | Broadcast the input shapes into a single shape. |

NumPy-specific help function[#](https://numpy.org/doc/stable/reference/routines.other.html#numpy-specific-help-function "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`info`](https://numpy.org/doc/stable/reference/generated/numpy.info.html#numpy.info "numpy.info")<br>(\[object, maxwidth, output, toplevel\]) | Get help information for an array, function, class, or module. |

On this page