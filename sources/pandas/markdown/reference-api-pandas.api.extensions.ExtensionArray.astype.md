[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.astype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.astype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.astype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.astype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.astype.html#pandas-api-extensions-extensionarray-astype "Link to this heading")

=================================================================================================================================================================================================================

ExtensionArray.astype(_dtype_, _copy\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L845-L927)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.astype.html#pandas.api.extensions.ExtensionArray.astype "Link to this definition")

Cast to a NumPy array or ExtensionArray with ‘dtype’.

If the target dtype is an ExtensionDtype, the result is an ExtensionArray. Otherwise, the result is a NumPy ndarray.

Parameters:

**dtype**str or dtype

Typecode or data-type to which the array is cast.

**copy**bool, default True

Whether to copy the data, even if not necessary. If False, a copy is made only if the old dtype does not match the new dtype.

Returns:

np.ndarray or pandas.api.extensions.ExtensionArray

An `ExtensionArray` if `dtype` is `ExtensionDtype`, otherwise a Numpy ndarray with `dtype` for its dtype.

See also

`Series.astype`

Cast a Series to a different dtype.

`DataFrame.astype`

Cast a DataFrame to a different dtype.

`api.extensions.ExtensionArray`

Base class for ExtensionArray objects.

`core.arrays.DatetimeArray._from_sequence`

Create a DatetimeArray from a sequence.

`core.arrays.TimedeltaArray._from_sequence`

Create a TimedeltaArray from a sequence.

Examples

\>>> arr \= pd.array(\[1, 2, 3\])
\>>> arr
<IntegerArray>
\[1, 2, 3\]
Length: 3, dtype: Int64

Copy to clipboard

Casting to another `ExtensionDtype` returns an `ExtensionArray`:

\>>> arr1 \= arr.astype("Float64")
\>>> arr1
<FloatingArray>
\[1.0, 2.0, 3.0\]
Length: 3, dtype: Float64
\>>> arr1.dtype
Float64Dtype()

Copy to clipboard

Otherwise, we will get a Numpy ndarray:

\>>> arr2 \= arr.astype("float64")
\>>> arr2
array(\[1., 2., 3.\])
\>>> arr2.dtype
dtype('float64')

Copy to clipboard

On this page