[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.swaplevel.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.MultiIndex.swaplevel.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.swaplevel.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.MultiIndex.swaplevel.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.MultiIndex.swaplevel.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.MultiIndex.swaplevel.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.MultiIndex.swaplevel.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.MultiIndex.swaplevel.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.MultiIndex.swaplevel.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.MultiIndex.swaplevel.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.MultiIndex.swaplevel.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.MultiIndex.swaplevel.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.MultiIndex.swaplevel.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.MultiIndex.swaplevel.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.MultiIndex.swaplevel[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.swaplevel.html#pandas-multiindex-swaplevel "Link to this heading")

=================================================================================================================================================================

MultiIndex.swaplevel(_i\=\-2_, _j\=\-1_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/indexes/multi.py#L3041-L3115)
[#](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.swaplevel.html#pandas.MultiIndex.swaplevel "Link to this definition")

Swap level i with level j.

Calling this method does not change the ordering of the values.

Default is to swap the last two levels of the MultiIndex.

Parameters:

**i**int, str, default -2

First level of index to be swapped. Can pass level name as string. Type of parameters can be mixed. If i is a negative int, the first level is indexed relative to the end of the MultiIndex.

**j**int, str, default -1

Second level of index to be swapped. Can pass level name as string. Type of parameters can be mixed. If j is a negative int, the second level is indexed relative to the end of the MultiIndex.

Returns:

MultiIndex

A new MultiIndex.

See also

[`Series.swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.Series.swaplevel.html#pandas.Series.swaplevel "pandas.Series.swaplevel")

Swap levels i and j in a MultiIndex.

[`DataFrame.swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.swaplevel.html#pandas.DataFrame.swaplevel "pandas.DataFrame.swaplevel")

Swap levels i and j in a MultiIndex on a particular axis.

Examples

\>>> mi \= pd.MultiIndex(
...     levels\=\[\["a", "b"\], \["bb", "aa"\], \["aaa", "bbb"\]\],
...     codes\=\[\[0, 0, 1, 1\], \[0, 1, 0, 1\], \[1, 0, 1, 0\]\],
... )
\>>> mi
MultiIndex(\[('a', 'bb', 'bbb'),\
            ('a', 'aa', 'aaa'),\
            ('b', 'bb', 'bbb'),\
            ('b', 'aa', 'aaa')\],
           )
\>>> mi.swaplevel()
MultiIndex(\[('a', 'bbb', 'bb'),\
            ('a', 'aaa', 'aa'),\
            ('b', 'bbb', 'bb'),\
            ('b', 'aaa', 'aa')\],
           )
\>>> mi.swaplevel(0)
MultiIndex(\[('bbb', 'bb', 'a'),\
            ('aaa', 'aa', 'a'),\
            ('bbb', 'bb', 'b'),\
            ('aaa', 'aa', 'b')\],
           )
\>>> mi.swaplevel(0, 1)
MultiIndex(\[('bb', 'a', 'bbb'),\
            ('aa', 'a', 'aaa'),\
            ('bb', 'b', 'bbb'),\
            ('aa', 'b', 'aaa')\],
        )

Copy to clipboard

On this page