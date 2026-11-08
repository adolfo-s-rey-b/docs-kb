[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.xs.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.xs[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.xs.html#pandas-dataframe-xs "Link to this heading")

=========================================================================================================================================

DataFrame.xs(_key_, _axis\=0_, _level\=None_, _drop\_level\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L4148-L4331)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.xs.html#pandas.DataFrame.xs "Link to this definition")

Return cross-section from the Series/DataFrame.

This method takes a key argument to select data at a particular level of a MultiIndex.

Parameters:

**key**label or tuple of label

Label contained in the index, or partially in a MultiIndex.

**axis**{0 or ‘index’, 1 or ‘columns’}, default 0

Axis to retrieve cross-section on.

**level**object, defaults to first n levels (n=1 or len(key))

In case of a key partially contained in a MultiIndex, indicate which levels are used. Levels can be referred by label or position.

**drop\_level**bool, default True

If False, returns object with same levels as self.

Returns:

Series or DataFrame

Cross-section from the original Series or DataFrame corresponding to the selected index levels.

See also

[`DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc")

Access a group of rows and columns by label(s) or a boolean array.

[`DataFrame.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc")

Purely integer-location based indexing for selection by position.

Notes

xs can not be used to set values.

MultiIndex Slicers is a generic way to get/set values on any level or levels. It is a superset of xs functionality, see [MultiIndex Slicers](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-mi-slicers)
.

Examples

\>>> d \= {
...     "num\_legs": \[4, 4, 2, 2\],
...     "num\_wings": \[0, 0, 2, 2\],
...     "class": \["mammal", "mammal", "mammal", "bird"\],
...     "animal": \["cat", "dog", "bat", "penguin"\],
...     "locomotion": \["walks", "walks", "flies", "walks"\],
... }
\>>> df \= pd.DataFrame(data\=d)
\>>> df \= df.set\_index(\["class", "animal", "locomotion"\])
\>>> df
                           num\_legs  num\_wings
class  animal  locomotion
mammal cat     walks              4          0
       dog     walks              4          0
       bat     flies              2          2
bird   penguin walks              2          2

Copy to clipboard

Get values at specified index

\>>> df.xs("mammal")
                   num\_legs  num\_wings
animal locomotion
cat    walks              4          0
dog    walks              4          0
bat    flies              2          2

Copy to clipboard

Get values at several indexes

\>>> df.xs(("mammal", "dog", "walks"))
num\_legs     4
num\_wings    0
Name: (mammal, dog, walks), dtype: int64

Copy to clipboard

Get values at specified index and level

\>>> df.xs("cat", level\=1)
                   num\_legs  num\_wings
class  locomotion
mammal walks              4          0

Copy to clipboard

Get values at several indexes and levels

\>>> df.xs(("bird", "walks"), level\=\[0, "locomotion"\])
         num\_legs  num\_wings
animal
penguin         2          2

Copy to clipboard

Get values at specified column and axis

\>>> df.xs("num\_wings", axis\=1)
class   animal   locomotion
mammal  cat      walks         0
        dog      walks         0
        bat      flies         2
bird    penguin  walks         2
Name: num\_wings, dtype: int64

Copy to clipboard

On this page