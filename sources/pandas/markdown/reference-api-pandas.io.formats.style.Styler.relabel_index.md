[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.relabel_index.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.relabel_index.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.relabel\_index[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.relabel_index.html#pandas-io-formats-style-styler-relabel-index "Link to this heading")

=====================================================================================================================================================================================================================

Styler.relabel\_index(_labels_, _axis\=0_, _level\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style_render.py#L1470-L1633)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.relabel_index.html#pandas.io.formats.style.Styler.relabel_index "Link to this definition")

Relabel the index, or column header, keys to display a set of specified values.

This method provides a way to completely replace the displayed index or column header labels with user-specified values without modifying the underlying DataFrame. It is especially useful when the desired display labels are not a simple function of the existing keys, or when enumeration-based labeling is needed.

Parameters:

**labels**list-like or Index

New labels to display. Must have same length as the underlying values not hidden.

**axis**{“index”, 0, “columns”, 1}

Apply to the index or columns.

**level**int, str, list, optional

The level(s) over which to apply the new labels. If None will apply to all levels of an Index or MultiIndex which are not hidden.

Returns:

Styler

Returns itself for chaining.

See also

[`Styler.format_index`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html#pandas.io.formats.style.Styler.format_index "pandas.io.formats.style.Styler.format_index")

Format the text display value of index or column headers.

[`Styler.hide`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html#pandas.io.formats.style.Styler.hide "pandas.io.formats.style.Styler.hide")

Hide the index, column headers, or specified data from display.

Notes

As part of Styler, this method allows the display of an index to be completely user-specified without affecting the underlying DataFrame data, index, or column headers. This means that the flexibility of indexing is maintained whilst the final display is customisable.

Since Styler is designed to be progressively constructed with method chaining, this method is adapted to react to the **currently specified hidden elements**. This is useful because it means one does not have to specify all the new labels if the majority of an index, or column headers, have already been hidden. The following produce equivalent display (note the length of `labels` in each case).

\# relabel first, then hide
df \= pd.DataFrame({"col": \["a", "b", "c"\]})
df.style.relabel\_index(\["A", "B", "C"\]).hide(\[0, 1\])
\# hide first, then relabel
df \= pd.DataFrame({"col": \["a", "b", "c"\]})
df.style.hide(\[0, 1\]).relabel\_index(\["C"\])

Copy to clipboard

This method should be used, rather than [`Styler.format_index()`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html#pandas.io.formats.style.Styler.format_index "pandas.io.formats.style.Styler.format_index")
, in one of the following cases (see examples):

> *   A specified set of labels are required which are not a function of the underlying index keys.
>     
> *   The function of the underlying index keys requires a counter variable, such as those available upon enumeration.
>     

Examples

Basic use

\>>> df \= pd.DataFrame({"col": \["a", "b", "c"\]})
\>>> df.style.relabel\_index(\["A", "B", "C"\])
     col
A      a
B      b
C      c

Copy to clipboard

Chaining with pre-hidden elements

\>>> df.style.hide(\[0, 1\]).relabel\_index(\["C"\])
     col
C      c

Copy to clipboard

Using a MultiIndex

\>>> midx \= pd.MultiIndex.from\_product(\[\[0, 1\], \[0, 1\], \[0, 1\]\])
\>>> df \= pd.DataFrame({"col": list(range(8))}, index\=midx)
\>>> styler \= df.style
          col
0  0  0     0
      1     1
   1  0     2
      1     3
1  0  0     4
      1     5
   1  0     6
      1     7
\>>> styler.hide(
...     (midx.get\_level\_values(0) \== 0) | (midx.get\_level\_values(1) \== 0)
... )
...
\>>> styler.hide(level\=\[0, 1\])
\>>> styler.relabel\_index(\["binary6", "binary7"\])
          col
binary6     6
binary7     7

Copy to clipboard

We can also achieve the above by indexing first and then re-labeling

\>>> styler \= df.loc\[\[(1, 1, 0), (1, 1, 1)\]\].style
\>>> styler.hide(level\=\[0, 1\]).relabel\_index(\["binary6", "binary7"\])
...
          col
binary6     6
binary7     7

Copy to clipboard

Defining a formatting function which uses an enumeration counter. Also note that the value of the index key is passed in the case of string labels so it can also be inserted into the label, using curly brackets (or double curly brackets if the string if pre-formatted),

\>>> df \= pd.DataFrame({"samples": np.random.rand(10)})
\>>> styler \= df.loc\[np.random.randint(0, 10, 3)\].style
\>>> styler.relabel\_index(\[f"sample{i + 1} ({{}})" for i in range(3)\])
...
                 samples
sample1 (5)     0.315811
sample2 (0)     0.495941
sample3 (2)     0.067946

Copy to clipboard

On this page