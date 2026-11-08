[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.codes.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.codes.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.codes.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.codes.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.codes.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.codes.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.codes.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.codes.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.codes.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.codes.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.codes.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.codes.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.codes.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.codes.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.codes[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.codes.html#pandas-multiindex-codes "Link to this heading")

=====================================================================================================================================================

property MultiIndex.codes[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L1158-L1183)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.codes.html#pandas.MultiIndex.codes "Link to this definition")

Codes of the MultiIndex.

Codes are the position of the index value in the list of level values for each level.

Returns:

tuple of numpy.ndarray

The codes of the MultiIndex. Each array in the tuple corresponds to a level in the MultiIndex.

See also

[`MultiIndex.set_codes`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.set_codes.html#pandas.MultiIndex.set_codes "pandas.MultiIndex.set_codes")

Set new codes on MultiIndex.

Examples

\>>> arrays \= \[\[1, 1, 2, 2\], \["red", "blue", "red", "blue"\]\]
\>>> mi \= pd.MultiIndex.from\_arrays(arrays, names\=("number", "color"))
\>>> mi.codes
FrozenList(\[\[0, 0, 1, 1\], \[1, 0, 1, 0\]\])

Copy to clipboard

On this page