[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.fillna.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.fillna.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.fillna[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.fillna.html#pandas-api-extensions-extensionarray-fillna "Link to this heading")

=================================================================================================================================================================================================================

ExtensionArray.fillna(_value_, _limit\=None_, _copy\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1393-L1468)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.fillna.html#pandas.api.extensions.ExtensionArray.fillna "Link to this definition")

Fill NA/NaN values using the specified method.

This method replaces missing values in the array with a scalar value or corresponding values from an array-like object.

Parameters:

**value**scalar, array-like

If a scalar value is passed it is used to fill all missing values. Alternatively, an array-like “value” can be given. It’s expected that the array-like have the same length as ‘self’.

**limit**int, default None

The maximum number of entries where NA values will be filled.

**copy**bool, default True

Whether to make a copy of the data before filling. If False, then the original should be modified and no new memory should be allocated. For ExtensionArray subclasses that cannot do this, it is at the author’s discretion whether to ignore “copy=False” or to raise.

Returns:

ExtensionArray

With NA/NaN filled.

See also

`api.extensions.ExtensionArray.dropna`

Return ExtensionArray without NA values.

`api.extensions.ExtensionArray.isna`

A 1-D array indicating if each value is missing.

Examples

\>>> arr \= pd.array(\[np.nan, np.nan, 2, 3, np.nan, np.nan\])
\>>> arr.fillna(0)
<IntegerArray>
\[0, 0, 2, 3, 0, 0\]
Length: 6, dtype: Int64

Copy to clipboard

On this page