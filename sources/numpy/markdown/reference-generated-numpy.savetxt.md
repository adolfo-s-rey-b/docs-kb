[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.savetxt.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.savetxt.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.savetxt.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.savetxt.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.savetxt.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.savetxt.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.savetxt.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.savetxt.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.savetxt.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.savetxt.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.savetxt.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.savetxt.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.savetxt.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.savetxt.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.savetxt.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.savetxt.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.savetxt.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.savetxt.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.savetxt.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.savetxt.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.savetxt[#](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#numpy-savetxt "Link to this heading")

===========================================================================================================================

numpy.savetxt(_fname_, _X_, _fmt\='%.18e'_, _delimiter\=' '_, _newline\='\\n'_, _header\=''_, _footer\=''_, _comments\='# '_, _encoding\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_npyio_impl.py#L1398-L1628)
[#](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#numpy.savetxt "Link to this definition")

Save an array to a text file.

Parameters:

**fname**filename, file handle or pathlib.Path

If the filename ends in `.gz`, the file is automatically saved in compressed gzip format. [`loadtxt`](https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy.loadtxt "numpy.loadtxt")
 understands gzipped files transparently.

**X**1D or 2D array\_like

Data to be saved to a text file.

**fmt**str or sequence of strs, optional

A single format (%10.5f), a sequence of formats, or a multi-format string, e.g. ‘Iteration %d – %10.5f’, in which case _delimiter_ is ignored. For complex _X_, the legal options for _fmt_ are:

*   a single specifier, `fmt='%.4e'`, resulting in numbers formatted like `' (%s+%sj)' % (fmt, fmt)`
    
*   a full string specifying every real and imaginary part, e.g. `' %.4e %+.4ej %.4e %+.4ej %.4e %+.4ej'` for 3 columns
    
*   a list of specifiers, one per column - in this case, the real and imaginary part must have separate specifiers, e.g. `['%.3e + %.3ej', '(%.15e%+.15ej)']` for 2 columns
    

**delimiter**str, optional

String or character separating columns.

**newline**str, optional

String or character separating lines.

**header**str, optional

String that will be written at the beginning of the file.

**footer**str, optional

String that will be written at the end of the file.

**comments**str, optional

String that will be prepended to the `header` and `footer` strings, to mark them as comments. Default: ‘# ‘, as expected by e.g. `numpy.loadtxt`.

**encoding**{None, str}, optional

Encoding used to encode the outputfile. Does not apply to output streams. If the encoding is something other than ‘bytes’ or ‘latin1’ you will not be able to load the file in NumPy versions < 1.14. Default is ‘latin1’.

See also

[`save`](https://numpy.org/doc/stable/reference/generated/numpy.save.html#numpy.save "numpy.save")

Save an array to a binary file in NumPy `.npy` format

[`savez`](https://numpy.org/doc/stable/reference/generated/numpy.savez.html#numpy.savez "numpy.savez")

Save several arrays into an uncompressed `.npz` archive

[`savez_compressed`](https://numpy.org/doc/stable/reference/generated/numpy.savez_compressed.html#numpy.savez_compressed "numpy.savez_compressed")

Save several arrays into a compressed `.npz` archive

Notes

Further explanation of the _fmt_ parameter (`%[flag]width[.precision]specifier`):

flags:

`-` : left justify

`+` : Forces to precede result with + or -.

`0` : Left pad the number with zeros instead of space (see width).

width:

Minimum number of characters to be printed. The value is not truncated if it has more characters.

precision:

*   For integer specifiers (eg. `d,i,o,x`), the minimum number of digits.
    
*   For `e, E` and `f` specifiers, the number of digits to print after the decimal point.
    
*   For `g` and `G`, the maximum number of significant digits.
    
*   For `s`, the maximum number of characters.
    

specifiers:

`c` : character

`d` or `i` : signed decimal integer

`e` or `E` : scientific notation with `e` or `E`.

`f` : decimal floating point

`g,G` : use the shorter of `e,E` or `f`

`o` : signed octal

`s` : string of characters

`u` : unsigned decimal integer

`x,X` : unsigned hexadecimal integer

This explanation of `fmt` is not complete, for an exhaustive specification see [\[1\]](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#r672d4d5b6143-1)
.

References

\[[1](https://numpy.org/doc/stable/reference/generated/numpy.savetxt.html#id1)\
\]

[Format Specification Mini-Language](https://docs.python.org/library/string.html#format-specification-mini-language)
, Python Documentation.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> x \= y \= z \= np.arange(0.0,5.0,1.0)
\>>> np.savetxt('test.out', x, delimiter\=',')   \# X is an array
\>>> np.savetxt('test.out', (x,y,z))   \# x,y,z equal sized 1D arrays
\>>> np.savetxt('test.out', x, fmt\='%1.4e')   \# use exponential notation

Copy to clipboard

Go BackOpen In Tab

On this page