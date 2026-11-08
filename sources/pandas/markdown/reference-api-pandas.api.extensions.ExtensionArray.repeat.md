[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.repeat.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.repeat.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.repeat[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.repeat.html#pandas-api-extensions-extensionarray-repeat "Link to this heading")

=================================================================================================================================================================================================================

ExtensionArray.repeat(_repeats_, _axis\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1883-L1927)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.repeat.html#pandas.api.extensions.ExtensionArray.repeat "Link to this definition")

Repeat elements of an ExtensionArray.

Returns a new ExtensionArray where each element of the current ExtensionArray is repeated consecutively a given number of times.

Parameters:

**repeats**int or array of ints

The number of repetitions for each element. This should be a non-negative integer. Repeating 0 times will return an empty ExtensionArray.

**axis**None

Must be `None`. Has no effect but is accepted for compatibility with numpy.

Returns:

ExtensionArray

Newly created ExtensionArray with repeated elements.

See also

`Series.repeat`

Equivalent function for Series.

`Index.repeat`

Equivalent function for Index.

[`numpy.repeat`](https://numpy.org/doc/stable/reference/generated/numpy.repeat.html#numpy.repeat "(in NumPy v2.5)")

Similar method for [`numpy.ndarray`](https://numpy.org/doc/stable/reference/generated/numpy.ndarray.html#numpy.ndarray "(in NumPy v2.5)")
.

[`ExtensionArray.take`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.take.html#pandas.api.extensions.ExtensionArray.take "pandas.api.extensions.ExtensionArray.take")

Take arbitrary positions.

Examples

\>>> cat \= pd.Categorical(\["a", "b", "c"\])
\>>> cat
\['a', 'b', 'c'\]
Categories (3, str): \['a', 'b', 'c'\]
\>>> cat.repeat(2)
\['a', 'a', 'b', 'b', 'c', 'c'\]
Categories (3, str): \['a', 'b', 'c'\]
\>>> cat.repeat(\[1, 2, 3\])
\['a', 'b', 'b', 'c', 'c', 'c'\]
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

On this page