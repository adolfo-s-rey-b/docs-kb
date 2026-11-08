[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.shift.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.shift.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.shift.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.shift[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.shift.html#pandas-api-extensions-extensionarray-shift "Link to this heading")

==============================================================================================================================================================================================================

ExtensionArray.shift(_periods\=1_, _fill\_value\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1537-L1602)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.shift.html#pandas.api.extensions.ExtensionArray.shift "Link to this definition")

Shift values by desired number.

Newly introduced missing values are filled with `self.dtype.na_value`.

Parameters:

**periods**int, default 1

The number of periods to shift. Negative values are allowed for shifting backwards.

**fill\_value**object, optional

The scalar value to use for newly introduced missing values. The default is `self.dtype.na_value`.

Returns:

ExtensionArray

Shifted.

See also

`api.extensions.ExtensionArray.transpose`

Return a transposed view on this array.

`api.extensions.ExtensionArray.factorize`

Encode the extension array as an enumerated type.

Notes

If `self` is empty or `periods` is 0, a copy of `self` is returned.

If `periods > len(self)`, then an array of size len(self) is returned, with all values filled with `self.dtype.na_value`.

For 2-dimensional ExtensionArrays, we are always shifting along axis=0.

Examples

\>>> arr \= pd.array(\[1, 2, 3\])
\>>> arr.shift(2)
<IntegerArray>
\[<NA>, <NA>, 1\]
Length: 3, dtype: Int64

Copy to clipboard

On this page