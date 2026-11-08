[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.info.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.info.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.info.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.info.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.info.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.info.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.info.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.info.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.info.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.info.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.info.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.info.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.info.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.info.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.info.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.info.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.info.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.info.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.info.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.info.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.info.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.info.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.info[#](https://numpy.org/doc/stable/reference/generated/numpy.info.html#numpy-info "Link to this heading")

==================================================================================================================

numpy.info(_object\=None_, _maxwidth\=76_, _output\=None_, _toplevel\='numpy'_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_utils_impl.py#L245-L404)
[#](https://numpy.org/doc/stable/reference/generated/numpy.info.html#numpy.info "Link to this definition")

Get help information for an array, function, class, or module.

Parameters:

**object**object or str, optional

Input object or name to get information about. If _object_ is an [`ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "numpy.ndarray")
 instance, information about the array is printed. If _object_ is a numpy object, its docstring is given. If it is a string, available modules are searched for matching objects. If None, information about [`info`](https://numpy.org/doc/stable/reference/generated/numpy.info.html#numpy.info "numpy.info")
 itself is returned.

**maxwidth**int, optional

Printing width.

**output**file like object, optional

File like object that the output is written to, default is `None`, in which case `sys.stdout` will be used. The object has to be opened in ‘w’ or ‘a’ mode.

**toplevel**str, optional

Start search at this level.

Notes

When used interactively with an object, `np.info(obj)` is equivalent to `help(obj)` on the Python prompt or `obj?` on the IPython prompt.

Examples

Try it in your browser!

\>>> np.info(np.polyval) 
   polyval(p, x)
     Evaluate the polynomial p at x.
     ...

Copy to clipboard

When using a string for _object_ it is possible to get multiple results.

\>>> np.info('fft') 
     \*\*\* Found in numpy \*\*\*
Core FFT routines
...
     \*\*\* Found in numpy.fft \*\*\*
 fft(a, n=None, axis=-1)
...
     \*\*\* Repeat reference found in numpy.fft.fftpack \*\*\*
     \*\*\* Total of 3 references found. \*\*\*

Copy to clipboard

When the argument is an array, information about the array is printed.

\>>> a \= np.array(\[\[1 + 2j, 3, \-4\], \[\-5j, 6, 0\]\], dtype\=np.complex64)
\>>> np.info(a)
class:  ndarray
shape:  (2, 3)
strides:  (24, 8)
itemsize:  8
aligned:  True
contiguous:  True
fortran:  False
data pointer: 0x562b6e0d2860  # may vary
byteorder:  little
byteswap:  False
type: complex64

Copy to clipboard

Go BackOpen In Tab

On this page