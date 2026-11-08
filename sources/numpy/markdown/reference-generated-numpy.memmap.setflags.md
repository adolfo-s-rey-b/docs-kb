[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.memmap.setflags.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.memmap.setflags.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.memmap.setflags.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.memmap.setflags.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.memmap.setflags.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.memmap.setflags.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.memmap.setflags.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.memmap.setflags.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.memmap.setflags.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.memmap.setflags.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.memmap.setflags.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.memmap.setflags.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.memmap.setflags.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.memmap.setflags.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.memmap.setflags.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.memmap.setflags.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.memmap.setflags.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.memmap.setflags.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.memmap.setflags.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.memmap.setflags.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.memmap.setflags.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.memmap.setflags.html)

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.memmap.setflags[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.setflags.html#numpy-memmap-setflags "Link to this heading")

===================================================================================================================================================

method

memmap.setflags(_write\=None_, _align\=None_, _uic\=None_)[#](https://numpy.org/doc/stable/reference/generated/numpy.memmap.setflags.html#numpy.memmap.setflags "Link to this definition")

Set array flags WRITEABLE, ALIGNED, WRITEBACKIFCOPY, respectively.

These Boolean-valued flags affect how numpy interprets the memory area used by _a_ (see Notes below). The ALIGNED flag can only be set to True if the data is actually aligned according to the type. The WRITEBACKIFCOPY flag can never be set to True. The flag WRITEABLE can only be set to True if the array owns its own memory, or the ultimate owner of the memory exposes a writeable buffer interface, or is a string. (The exception for string is made so that unpickling can be done without copying memory.)

Parameters:

**write**bool, optional

Describes whether or not _a_ can be written to.

**align**bool, optional

Describes whether or not _a_ is aligned properly for its type.

**uic**bool, optional

Describes whether or not _a_ is a copy of another “base” array.

Notes

Array flags provide information about how the memory area used for the array is to be interpreted. There are 7 Boolean flags in use, only three of which can be changed by the user: WRITEBACKIFCOPY, WRITEABLE, and ALIGNED.

WRITEABLE (W) the data area can be written to;

ALIGNED (A) the data and strides are aligned appropriately for the hardware (as determined by the compiler);

WRITEBACKIFCOPY (X) this array is a copy of some other array (referenced by .base). When the C-API function PyArray\_ResolveWritebackIfCopy is called, the base array will be updated with the contents of this array.

All flags can be accessed using the single (upper case) letter as well as the full name.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> y \= np.array(\[\[3, 1, 7\],\
...               \[2, 0, 0\],\
...               \[8, 5, 9\]\])
\>>> y
array(\[\[3, 1, 7\],\
       \[2, 0, 0\],\
       \[8, 5, 9\]\])
\>>> y.flags
  C\_CONTIGUOUS : True
  F\_CONTIGUOUS : False
  OWNDATA : True
  WRITEABLE : True
  ALIGNED : True
  WRITEBACKIFCOPY : False
\>>> y.setflags(write\=0, align\=0)
\>>> y.flags
  C\_CONTIGUOUS : True
  F\_CONTIGUOUS : False
  OWNDATA : True
  WRITEABLE : False
  ALIGNED : False
  WRITEBACKIFCOPY : False
\>>> y.setflags(uic\=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: cannot set WRITEBACKIFCOPY flag to True

Copy to clipboard

Go BackOpen In Tab

On this page