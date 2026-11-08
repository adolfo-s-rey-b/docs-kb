[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.__array__.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Categorical.__array__.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.__array__.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Categorical.__array__.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Categorical.__array__.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Categorical.__array__.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Categorical.__array__.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Categorical.__array__.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Categorical.__array__.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Categorical.__array__.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Categorical.__array__.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Categorical.__array__.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Categorical.__array__.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Categorical.__array__.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Categorical.\_\_array\_\_[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.__array__.html#pandas-categorical-array "Link to this heading")

====================================================================================================================================================================

Categorical.\_\_array\_\_(_dtype\=None_, _copy\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/categorical.py#L1891-L1941)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.__array__.html#pandas.Categorical.__array__ "Link to this definition")

The numpy array interface.

Users should not call this directly. Rather, it is invoked by [`numpy.array()`](https://numpy.org/doc/stable/reference/generated/numpy.array.html#numpy.array "(in NumPy v2.5)")
 and [`numpy.asarray()`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "(in NumPy v2.5)")
.

Parameters:

**dtype**np.dtype or None

Specifies the dtype for the array.

**copy**bool or None, optional

See [`numpy.asarray()`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "(in NumPy v2.5)")
.

Returns:

numpy.array

A numpy array of either the specified dtype or, if dtype==None (default), the same dtype as categorical.categories.dtype.

See also

[`numpy.asarray`](https://numpy.org/doc/stable/reference/generated/numpy.asarray.html#numpy.asarray "(in NumPy v2.5)")

Convert input to numpy.ndarray.

Examples

\>>> cat \= pd.Categorical(\["a", "b"\], ordered\=True)

Copy to clipboard

The following calls `cat.__array__`

\>>> np.asarray(cat)
array(\['a', 'b'\], dtype=object)

Copy to clipboard

On this page