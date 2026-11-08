[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flags.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.memmap.flags.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flags.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.memmap.flags.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.memmap.flags.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.memmap.flags.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.memmap.flags.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.memmap.flags.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.memmap.flags.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.memmap.flags.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.memmap.flags.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.memmap.flags.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.memmap.flags.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.memmap.flags.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.memmap.flags.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.memmap.flags.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.memmap.flags.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.memmap.flags.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.memmap.flags.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.memmap.flags.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.memmap.flags.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.memmap.flags.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.memmap.flags[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flags.html#numpy-memmap-flags "Link to this heading")

==========================================================================================================================================

attribute

memmap.flags[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flags.html#numpy.memmap.flags "Link to this definition")

Information about the memory layout of the array.

Attributes:

**C\_CONTIGUOUS (C)**

The data is in a single, C-style contiguous segment.

**F\_CONTIGUOUS (F)**

The data is in a single, Fortran-style contiguous segment.

**OWNDATA (O)**

The array owns the memory it uses or borrows it from another object.

**WRITEABLE (W)**

The data area can be written to. Setting this to False locks the data, making it read-only. A view (slice, etc.) inherits WRITEABLE from its base array at creation time, but a view of a writeable array may be subsequently locked while the base array remains writeable. (The opposite is not true, in that a view of a locked array may not be made writeable. However, currently, locking a base object does not lock any views that already reference it, so under that circumstance it is possible to alter the contents of a locked array via a previously created writeable view onto it.) Attempting to change a non-writeable array raises a RuntimeError exception.

**ALIGNED (A)**

The data and all elements are aligned appropriately for the hardware.

**WRITEBACKIFCOPY (X)**

This array is a copy of some other array. The C-API function PyArray\_ResolveWritebackIfCopy must be called before deallocating to the base array will be updated with the contents of this array.

**FNC**

F\_CONTIGUOUS and not C\_CONTIGUOUS.

**FORC**

F\_CONTIGUOUS or C\_CONTIGUOUS (one-segment test).

**BEHAVED (B)**

ALIGNED and WRITEABLE.

**CARRAY (CA)**

BEHAVED and C\_CONTIGUOUS.

**FARRAY (FA)**

BEHAVED and F\_CONTIGUOUS and not C\_CONTIGUOUS.

Notes

The [`flags`](https://numpy.org/doc/stable/reference/generated/numpy.memmap.flags.html#numpy.memmap.flags "numpy.memmap.flags")
 object can be accessed dictionary-like (as in `a.flags['WRITEABLE']`), or by using lowercased attribute names (as in `a.flags.writeable`). Short flag names are only supported in dictionary access.

Only the WRITEBACKIFCOPY, WRITEABLE, and ALIGNED flags can be changed by the user, via direct assignment to the attribute or dictionary entry, or by calling [`ndarray.setflags`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.setflags.html#numpy.ndarray.setflags "numpy.ndarray.setflags")
.

The array flags cannot be set arbitrarily:

*   WRITEBACKIFCOPY can only be set `False`.
    
*   ALIGNED can only be set `True` if the data is truly aligned.
    
*   WRITEABLE can only be set `True` if the array owns its own memory or the ultimate owner of the memory exposes a writeable buffer interface or is a string.
    

Arrays can be both C-style and Fortran-style contiguous simultaneously. This is clear for 1-dimensional arrays, but can also be true for higher dimensional arrays.

Even for contiguous arrays a stride for a given dimension `arr.strides[dim]` may be _arbitrary_ if `arr.shape[dim] == 1` or the array has no elements. It does _not_ generally hold that `self.strides[-1] == self.itemsize` for C-style contiguous arrays or `self.strides[0] == self.itemsize` for Fortran-style contiguous arrays is true.

On this page