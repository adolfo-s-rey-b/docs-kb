[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.equals.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray.equals.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray.equals.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.equals[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.equals.html#pandas-api-extensions-extensionarray-equals "Link to this heading")

=================================================================================================================================================================================================================

ExtensionArray.equals(_other_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L1694-L1743)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.equals.html#pandas.api.extensions.ExtensionArray.equals "Link to this definition")

Return if another array is equivalent to this array.

Equivalent means that both arrays have the same shape and dtype, and all values compare equal. Missing values in the same location are considered equal (in contrast with normal equality).

Parameters:

**other**ExtensionArray

Array to compare to this Array.

Returns:

boolean

Whether the arrays are equivalent.

See also

[`numpy.array_equal`](https://numpy.org/doc/stable/reference/generated/numpy.array_equal.html#numpy.array_equal "(in NumPy v2.5)")

Equivalent method for numpy array.

`Series.equals`

Equivalent method for Series.

`DataFrame.equals`

Equivalent method for DataFrame.

Examples

\>>> arr1 \= pd.array(\[1, 2, np.nan\])
\>>> arr2 \= pd.array(\[1, 2, np.nan\])
\>>> arr1.equals(arr2)
True

Copy to clipboard

\>>> arr1 \= pd.array(\[1, 3, np.nan\])
\>>> arr2 \= pd.array(\[1, 2, np.nan\])
\>>> arr1.equals(arr2)
False

Copy to clipboard

On this page