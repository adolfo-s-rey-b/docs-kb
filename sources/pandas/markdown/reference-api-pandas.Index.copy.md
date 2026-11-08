[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Index.copy.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Index.copy[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.copy.html#pandas-index-copy "Link to this heading")

===================================================================================================================================

Index.copy(_name\=None_, _deep\=False_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/base.py#L1377-L1424)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Index.copy.html#pandas.Index.copy "Link to this definition")

Make a copy of this object.

Name is set on the new object.

Parameters:

**name**Label, optional

Set name for new object.

**deep**bool, default False

If True attempts to make a deep copy of the Index.

Else makes a shallow copy.

Returns:

Index

Index refer to new object which is a copy of this object.

See also

[`Index.delete`](https://pandas.pydata.org/docs/reference/api/pandas.Index.delete.html#pandas.Index.delete "pandas.Index.delete")

Make new Index with passed location(-s) deleted.

[`Index.drop`](https://pandas.pydata.org/docs/reference/api/pandas.Index.drop.html#pandas.Index.drop "pandas.Index.drop")

Make new Index with passed list of labels deleted.

Notes

In most cases, there should be no functional difference from using `deep`, but if `deep` is passed it will attempt to deepcopy.

Examples

\>>> idx \= pd.Index(\["a", "b", "c"\])
\>>> new\_idx \= idx.copy()
\>>> idx is new\_idx
False

Copy to clipboard

On this page