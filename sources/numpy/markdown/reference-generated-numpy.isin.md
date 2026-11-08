[Skip to main content](https://numpy.org/doc/stable/reference/generated/numpy.isin.html#main-content)

Back to top Ctrl+K

Light Dark System Settings

2.5 (stable)

[dev](https://numpy.org/devdocs/reference/generated/numpy.isin.html)
[2.5 (stable)](https://numpy.org/doc/stable/reference/generated/numpy.isin.html)
[2.4](https://numpy.org/doc/2.4/reference/generated/numpy.isin.html)
[2.3](https://numpy.org/doc/2.3/reference/generated/numpy.isin.html)
[2.2](https://numpy.org/doc/2.2/reference/generated/numpy.isin.html)
[2.1](https://numpy.org/doc/2.1/reference/generated/numpy.isin.html)
[2.0](https://numpy.org/doc/2.0/reference/generated/numpy.isin.html)
[1.26](https://numpy.org/doc/1.26/reference/generated/numpy.isin.html)
[1.25](https://numpy.org/doc/1.25/reference/generated/numpy.isin.html)
[1.24](https://numpy.org/doc/1.24/reference/generated/numpy.isin.html)
[1.23](https://numpy.org/doc/1.23/reference/generated/numpy.isin.html)
[1.22](https://numpy.org/doc/1.22/reference/generated/numpy.isin.html)
[1.21](https://numpy.org/doc/1.21/reference/generated/numpy.isin.html)
[1.20](https://numpy.org/doc/1.20/reference/generated/numpy.isin.html)
[1.19](https://numpy.org/doc/1.19/reference/generated/numpy.isin.html)
[1.18](https://numpy.org/doc/1.18/reference/generated/numpy.isin.html)
[1.17](https://numpy.org/doc/1.17/reference/generated/numpy.isin.html)
[1.16](https://numpy.org/doc/1.16/reference/generated/numpy.isin.html)
[1.15](https://numpy.org/doc/1.15/reference/generated/numpy.isin.html)
[1.14](https://numpy.org/doc/1.14/reference/generated/numpy.isin.html)
[1.13](https://numpy.org/doc/1.13/reference/generated/numpy.isin.html)

*   [GitHub](https://github.com/numpy/numpy)
    

Collapse Sidebar Expand Sidebar

numpy.isin[#](https://numpy.org/doc/stable/reference/generated/numpy.isin.html#numpy-isin "Link to this heading")

==================================================================================================================

numpy.isin(_element_, _test\_elements_, _assume\_unique\=False_, _invert\=False_, _\*_, _kind\=None_)[\[source\]](https://github.com/numpy/numpy/blob/v2.5.0/numpy/lib/_arraysetops_impl.py#L958-L1076)
[#](https://numpy.org/doc/stable/reference/generated/numpy.isin.html#numpy.isin "Link to this definition")

Calculates `element in test_elements`, broadcasting over _element_ only. Returns a boolean array of the same shape as _element_ that is True where an element of _element_ is in _test\_elements_ and False otherwise.

Parameters:

**element**array\_like

Input array.

**test\_elements**array\_like

The values against which to test each value of _element_. This argument is flattened if it is an array or array\_like. See notes for behavior with non-array-like parameters.

**assume\_unique**bool, optional

If True, the input arrays are both assumed to be unique, which can speed up the calculation. Default is False.

**invert**bool, optional

If True, the values in the returned array are inverted, as if calculating _element not in test\_elements_. Default is False. `np.isin(a, b, invert=True)` is equivalent to (but faster than) `np.invert(np.isin(a, b))`.

**kind**{None, ‘sort’, ‘table’}, optional

The algorithm to use. This will not affect the final result, but will affect the speed and memory use. The default, None, will select automatically based on memory considerations.

*   If ‘sort’, will use a mergesort-based approach. This will have a memory usage of roughly 6 times the sum of the sizes of _element_ and _test\_elements_, not accounting for size of dtypes.
    
*   If ‘table’, will use a lookup table approach similar to a counting sort. This is only available for boolean and integer arrays. This will have a memory usage of the size of _element_ plus the max-min value of _test\_elements_. _assume\_unique_ has no effect when the ‘table’ option is used.
    
*   If None, will automatically choose ‘table’ if the required memory allocation is less than or equal to 6 times the sum of the sizes of _element_ and _test\_elements_, otherwise will use ‘sort’. This is done to not use a large amount of memory by default, even though ‘table’ may be faster in most cases. If ‘table’ is chosen, _assume\_unique_ will have no effect.
    

Returns:

**isin**ndarray, bool

Has the same shape as _element_. The values _element\[isin\]_ are in _test\_elements_.

Notes

[`isin`](https://numpy.org/doc/stable/reference/generated/numpy.isin.html#numpy.isin "numpy.isin")
 is an element-wise function version of the python keyword _in_. `isin(a, b)` is roughly equivalent to `np.array([item in b for item in a])` if _a_ and _b_ are 1-D sequences.

_element_ and _test\_elements_ are converted to arrays if they are not already. If _test\_elements_ is a set (or other non-sequence collection) it will be converted to an object array with one element, rather than an array of the values contained in _test\_elements_. This is a consequence of the [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
 constructor’s way of handling non-sequence collections. Converting the set to a list usually gives the desired behavior.

Using `kind='table'` tends to be faster than _kind=’sort’_ if the following relationship is true: `log10(len(test_elements)) > (log10(max(test_elements)-min(test_elements)) - 2.27) / 0.927`, but may use greater memory. The default value for _kind_ will be automatically selected based only on memory usage, so one may manually set `kind='table'` if memory constraints can be relaxed.

Examples

Try it in your browser!

\>>> import numpy as np
\>>> element \= 2\*np.arange(4).reshape((2, 2))
\>>> element
array(\[\[0, 2\],\
       \[4, 6\]\])
\>>> test\_elements \= \[1, 2, 4, 8\]
\>>> mask \= np.isin(element, test\_elements)
\>>> mask
array(\[\[False,  True\],\
       \[ True, False\]\])
\>>> element\[mask\]
array(\[2, 4\])

Copy to clipboard

The indices of the matched values can be obtained with [`nonzero`](https://numpy.org/doc/stable/reference/generated/numpy.nonzero.html#numpy.nonzero "numpy.nonzero")
:

\>>> np.nonzero(mask)
(array(\[0, 1\]), array(\[1, 0\]))

Copy to clipboard

The test can also be inverted:

\>>> mask \= np.isin(element, test\_elements, invert\=True)
\>>> mask
array(\[\[ True, False\],\
       \[False,  True\]\])
\>>> element\[mask\]
array(\[0, 6\])

Copy to clipboard

Because of how [`array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "numpy.array")
 handles sets, the following does not work as expected:

\>>> test\_set \= {1, 2, 4, 8}
\>>> np.isin(element, test\_set)
array(\[\[False, False\],\
       \[False, False\]\])

Copy to clipboard

Casting the set to a list gives the expected result:

\>>> np.isin(element, list(test\_set))
array(\[\[False,  True\],\
       \[ True, False\]\])

Copy to clipboard

Go BackOpen In Tab

On this page