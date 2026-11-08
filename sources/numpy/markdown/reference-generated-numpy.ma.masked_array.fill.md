[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.fill.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

Choose version

*   [GitHub](https://github.com/numpy/numpy)
    

numpy.ma.masked\_array.fill[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.fill.html#numpy-ma-masked-array-fill "Link to this heading")

===================================================================================================================================================================

method

ma.masked\_array.fill(_value_)[#](https://numpy.org/doc/stable/reference/generated/numpy.ma.masked_array.fill.html#numpy.ma.masked_array.fill "Link to this definition")

Fill the array with a scalar value.

Parameters:

**value**scalar

All elements of _a_ will be assigned this value.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> a \= np.array(\[1, 2\])
\>>> a.fill(0)
\>>> a
array(\[0, 0\])
\>>> a \= np.empty(2)
\>>> a.fill(1)
\>>> a
array(\[1.,  1.\])

Copy to clipboard

Fill expects a scalar value and always behaves the same as assigning to a single array element. The following is a rare example where this distinction is important:

\>>> a \= np.array(\[None, None\], dtype\=np.object\_)
\>>> a\[0\] \= np.array(3)
\>>> a
array(\[array(3), None\], dtype=object)
\>>> a.fill(np.array(3))
\>>> a
array(\[array(3), array(3)\], dtype=object)

Copy to clipboard

Where other forms of assignments will unpack the array being assigned:

\>>> a\[...\] \= np.array(3)
\>>> a
array(\[3, 3\], dtype=object)

Copy to clipboard

Go BackOpen In Tab

On this page