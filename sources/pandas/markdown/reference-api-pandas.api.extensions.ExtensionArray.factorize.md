[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.factorize.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.factorize.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.factorize[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.factorize.html#pandas-api-extensions-extensionarray-factorize "Link to this heading")

==========================================================================================================================================================================================================================

ExtensionArray.factorize(_use\_na\_sentinel\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1814-L1881)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.factorize.html#pandas.api.extensions.ExtensionArray.factorize "Link to this definition")

Encode the extension array as an enumerated type.

This method encodes the array values as integer codes that index into an array of unique values. Missing values can be encoded with a sentinel value of -1.

Parameters:

**use\_na\_sentinel**bool, default True

If True, the sentinel -1 will be used for NaN values. If False, NaN values will be encoded as non-negative integers and will not drop the NaN from the uniques of the values.

Returns:

**codes**ndarray

An integer NumPy array that’s an indexer into the original ExtensionArray.

**uniques**ExtensionArray

An ExtensionArray containing the unique values of self.

Note

uniques will _not_ contain an entry for the NA value of the ExtensionArray if there are any missing values present in self.

See also

[`factorize`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.factorize.html#pandas.api.extensions.ExtensionArray.factorize "pandas.api.extensions.ExtensionArray.factorize")

Top-level factorize method that dispatches here.

Notes

[`pandas.factorize()`](https://pandas.pydata.org/docs/reference/api/pandas.factorize.html#pandas.factorize "pandas.factorize")
 offers a sort keyword as well.

Examples

\>>> idx1 \= pd.PeriodIndex(
...     \["2014-01", "2014-01", "2014-02", "2014-02", "2014-03", "2014-03"\],
...     freq\="M",
... )
\>>> arr, idx \= idx1.factorize()
\>>> arr
array(\[0, 0, 1, 1, 2, 2\])
\>>> idx
PeriodIndex(\['2014-01', '2014-02', '2014-03'\], dtype='period\[M\]')

Copy to clipboard

On this page