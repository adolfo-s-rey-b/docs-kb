[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.align.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.align.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.align.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.align.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.align.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.align.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.align.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.align.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.align.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.align.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.align.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.align.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.align.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.align.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.align[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.align.html#pandas-series-align "Link to this heading")

=========================================================================================================================================

Series.align(_other_, _join\='outer'_, _axis\=None_, _level\=None_, _copy\=<no\_default>_, _fill\_value\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L10040-L10220)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.align.html#pandas.Series.align "Link to this definition")

Align two objects on their axes with the specified join method.

Join method is specified for each axis Index.

Parameters:

**other**DataFrame or Series

The object to align with.

**join**{‘outer’, ‘inner’, ‘left’, ‘right’}, default ‘outer’

Type of alignment to be performed.

*   left: use only keys from left frame, preserve key order.
    
*   right: use only keys from right frame, preserve key order.
    
*   outer: use union of keys from both frames, sort keys lexicographically.
    
*   inner: use intersection of keys from both frames, preserve the order of the left keys.
    

**axis**allowed axis of the other object, default None

Align on index (0), columns (1), or both (None).

**level**int or level name, default None

Broadcast across a level, matching Index values on the passed MultiIndex level.

**copy**bool, default False

This keyword is now ignored; changing its value will have no impact on the method.

Deprecated since version 3.0.0: This keyword is ignored and will be removed in pandas 4.0. Since pandas 3.0, this method always returns a new object using a lazy copy mechanism that defers copies until necessary (Copy-on-Write). See the [user guide on Copy-on-Write](https://pandas.pydata.org/docs/dev/user_guide/migration.html)
 for more details.

**fill\_value**scalar, default np.nan

Value to use for missing values. Defaults to NaN, but can be any “compatible” value.

Returns:

tuple of (Series/DataFrame, type of other)

Aligned objects.

See also

[`Series.align`](https://pandas.pydata.org/docs/reference/api/pandas.Series.align.html#pandas.Series.align "pandas.Series.align")

Align two objects on their axes with specified join method.

[`DataFrame.align`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.align.html#pandas.DataFrame.align "pandas.DataFrame.align")

Align two objects on their axes with specified join method.

Examples

\>>> df \= pd.DataFrame(
...     \[\[1, 2, 3, 4\], \[6, 7, 8, 9\]\], columns\=\["D", "B", "E", "A"\], index\=\[1, 2\]
... )
\>>> other \= pd.DataFrame(
...     \[\[10, 20, 30, 40\], \[60, 70, 80, 90\], \[600, 700, 800, 900\]\],
...     columns\=\["A", "B", "C", "D"\],
...     index\=\[2, 3, 4\],
... )
\>>> df
   D  B  E  A
1  1  2  3  4
2  6  7  8  9
\>>> other
    A    B    C    D
2   10   20   30   40
3   60   70   80   90
4  600  700  800  900

Copy to clipboard

Align on columns:

\>>> left, right \= df.align(other, join\="outer", axis\=1)
\>>> left
   A  B   C  D  E
1  4  2 NaN  1  3
2  9  7 NaN  6  8
\>>> right
    A    B    C    D   E
2   10   20   30   40 NaN
3   60   70   80   90 NaN
4  600  700  800  900 NaN

Copy to clipboard

We can also align on the index:

\>>> left, right \= df.align(other, join\="outer", axis\=0)
\>>> left
    D    B    E    A
1  1.0  2.0  3.0  4.0
2  6.0  7.0  8.0  9.0
3  NaN  NaN  NaN  NaN
4  NaN  NaN  NaN  NaN
\>>> right
    A      B      C      D
1    NaN    NaN    NaN    NaN
2   10.0   20.0   30.0   40.0
3   60.0   70.0   80.0   90.0
4  600.0  700.0  800.0  900.0

Copy to clipboard

Finally, the default axis=None will align on both index and columns:

\>>> left, right \= df.align(other, join\="outer", axis\=None)
\>>> left
     A    B   C    D    E
1  4.0  2.0 NaN  1.0  3.0
2  9.0  7.0 NaN  6.0  8.0
3  NaN  NaN NaN  NaN  NaN
4  NaN  NaN NaN  NaN  NaN
\>>> right
       A      B      C      D   E
1    NaN    NaN    NaN    NaN NaN
2   10.0   20.0   30.0   40.0 NaN
3   60.0   70.0   80.0   90.0 NaN
4  600.0  700.0  800.0  900.0 NaN

Copy to clipboard

On this page