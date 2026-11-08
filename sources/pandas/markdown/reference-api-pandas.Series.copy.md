[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.copy.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.copy[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.copy.html#pandas-series-copy "Link to this heading")

======================================================================================================================================

Series.copy(_deep\=True_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L6800-L6906)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.copy.html#pandas.Series.copy "Link to this definition")

Make a copy of this object’s indices and data.

When `deep=True` (default), a new object will be created with a copy of the calling object’s data and indices. Modifications to the data or indices of the copy will not be reflected in the original object (see notes below).

When `deep=False`, a new object will be created without copying the calling object’s data or index (only references to the data and index are copied). With Copy-on-Write, changes to the original will _not_ be reflected in the shallow copy (and vice versa). The shallow copy uses a lazy (deferred) copy mechanism that copies the data only when any changes to the original or shallow copy are made, ensuring memory efficiency while maintaining data integrity.

Note

In pandas versions prior to 3.0, the default behavior without Copy-on-Write was different: changes to the original _were_ reflected in the shallow copy (and vice versa). See the [Copy-on-Write user guide](https://pandas.pydata.org/docs/user_guide/migration.html#copy-on-write)
 for more information.

Parameters:

**deep**bool, default True

Make a deep copy, including a copy of the data and the indices. With `deep=False` neither the indices nor the data are copied.

Returns:

Series or DataFrame

Object type matches caller.

See also

[`copy.copy`](https://docs.python.org/3/library/copy.html#copy.copy "(in Python v3.15)")

Return a shallow copy of an object.

[`copy.deepcopy`](https://docs.python.org/3/library/copy.html#copy.deepcopy "(in Python v3.15)")

Return a deep copy of an object.

Notes

When `deep=True`, data is copied but actual Python objects will not be copied recursively, only the reference to the object. This is in contrast to [`copy.deepcopy()`](https://docs.python.org/3/library/copy.html#copy.deepcopy "(in Python v3.15)")
 in the Standard Library, which recursively copies object data (see examples below).

While `Index` objects are copied when `deep=True`, the underlying numpy array is not copied for performance reasons. Since `Index` is immutable, the underlying data can be safely shared and a copy is not needed.

Since pandas is not thread safe, see the [gotchas](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-thread-safety)
 when copying in a threading environment.

Copy-on-Write protects shallow copies against accidental modifications. This means that any changes to the copied data would make a new copy of the data upon write (and vice versa). Changes made to either the original or copied variable would not be reflected in the counterpart. See [Copy\_on\_Write](https://pandas.pydata.org/docs/user_guide/migration.html#copy-on-write)
 for more information.

Examples

\>>> s \= pd.Series(\[1, 2\], index\=\["a", "b"\])
\>>> s
a    1
b    2
dtype: int64

Copy to clipboard

\>>> s\_copy \= s.copy(deep\=True)
\>>> s\_copy
a    1
b    2
dtype: int64

Copy to clipboard

Due to Copy-on-Write, shallow copies still protect data modifications. Note shallow does not get modified below.

\>>> s \= pd.Series(\[1, 2\], index\=\["a", "b"\])
\>>> shallow \= s.copy(deep\=False)
\>>> s.iloc\[1\] \= 200
\>>> shallow
a    1
b    2
dtype: int64

Copy to clipboard

When the data has object dtype, even a deep copy does not copy the underlying Python objects. Updating a nested data object will be reflected in the deep copy.

\>>> s \= pd.Series(\[\[1, 2\], \[3, 4\]\])
\>>> deep \= s.copy()
\>>> s\[0\]\[0\] \= 10
\>>> s
0    \[10, 2\]
1     \[3, 4\]
dtype: object
\>>> deep
0    \[10, 2\]
1     \[3, 4\]
dtype: object

Copy to clipboard

On this page