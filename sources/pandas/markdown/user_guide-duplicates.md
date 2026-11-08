[Skip to main content](https://pandas.pydata.org/docs/user_guide/duplicates.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/user_guide/duplicates.html)
[3.1 (stable)](https://pandas.pydata.org/docs/user_guide/duplicates.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/user_guide/duplicates.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/duplicates.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/user_guide/duplicates.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/user_guide/duplicates.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/duplicates.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/user_guide/duplicates.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/user_guide/duplicates.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/user_guide/duplicates.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/user_guide/duplicates.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/duplicates.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/user_guide/duplicates.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Duplicate Labels[#](https://pandas.pydata.org/docs/user_guide/duplicates.html#duplicate-labels "Link to this heading")

=======================================================================================================================

`Index` objects are not required to be unique; you can have duplicate row or column labels. This may be a bit confusing at first. If you’re familiar with SQL, you know that row labels are similar to a primary key on a table, and you would never want duplicates in a SQL table. But one of pandas’ roles is to clean messy, real-world data before it goes to some downstream system. And real-world data has duplicates, even in fields that are supposed to be unique.

This section describes how duplicate labels change the behavior of certain operations, and how prevent duplicates from arising during operations, or to detect them if they do.

In \[1\]: import pandas as pd

In \[2\]: import numpy as np

Copy to clipboard

Consequences of Duplicate Labels[#](https://pandas.pydata.org/docs/user_guide/duplicates.html#consequences-of-duplicate-labels "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

Some pandas methods (`Series.reindex()` for example) just don’t work with duplicates present. The output can’t be determined, and so pandas raises.

In \[3\]: s1 \= pd.Series(\[0, 1, 2\], index\=\["a", "b", "b"\])

In \[4\]: s1.reindex(\["a", "b", "c"\])
\---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In\[4\], line 1
\----> 1 s1.reindex(\["a", "b", "c"\])

File ~/work/pandas/pandas/pandas/core/series.py:6035, in Series.reindex(self, index, axis, method, copy, level, fill\_value, limit, tolerance)
   6031         original index entry) unfilled.
   6032 
   6033         See the :ref:\`user guide <basics.reindexing\>\` for more.
   6034         """
\-> 6035         return super().reindex(
   6036             index=index,
   6037             method=method,
   6038             level=level,

File ~/work/pandas/pandas/pandas/core/generic.py:5544, in NDFrame.reindex(self, labels, index, columns, axis, method, copy, level, fill\_value, limit, tolerance)
   5540         if self.\_needs\_reindex\_multi(axes, method, level):
   5541             return self.\_reindex\_multi(axes, fill\_value)
   5542 
   5543         # perform the reindex on the axes
\-> 5544         return self.\_reindex\_axes(
   5545             axes, level, limit, tolerance, method, fill\_value
   5546         ).\_\_finalize\_\_(self, method="reindex")

File ~/work/pandas/pandas/pandas/core/generic.py:5566, in NDFrame.\_reindex\_axes(self, axes, level, limit, tolerance, method, fill\_value)
   5562             if labels is None:
   5563                 continue
   5564 
   5565             ax = self.\_get\_axis(a)
\-> 5566             new\_index, indexer = ax.reindex(
   5567                 labels, level=level, limit=limit, tolerance=tolerance, method=method
   5568             )
   5569 

File ~/work/pandas/pandas/pandas/core/indexes/base.py:4450, in Index.reindex(self, target, method, level, limit, tolerance)
   4447     raise ValueError("cannot handle a non-unique multi-index!")
   4448 elif not self.is\_unique:
   4449     # GH#42568
\-> 4450     raise ValueError("cannot reindex on an axis with duplicate labels")
   4451 else:
   4452     indexer, \_ = self.get\_indexer\_non\_unique(target)

ValueError: cannot reindex on an axis with duplicate labels

Copy to clipboard

Other methods, like indexing, can give very surprising results. Typically indexing with a scalar will _reduce dimensionality_. Slicing a `DataFrame` with a scalar will return a `Series`. Slicing a `Series` with a scalar will return a scalar. But with duplicates, this isn’t the case.

In \[5\]: df1 \= pd.DataFrame(\[\[0, 1, 2\], \[3, 4, 5\]\], columns\=\["A", "A", "B"\])

In \[6\]: df1
Out\[6\]: 
   A  A  B
0  0  1  2
1  3  4  5

Copy to clipboard

We have duplicates in the columns. If we slice `'B'`, we get back a `Series`

In \[7\]: df1\["B"\]  \# a series
Out\[7\]: 
0    2
1    5
Name: B, dtype: int64

Copy to clipboard

But slicing `'A'` returns a `DataFrame`

In \[8\]: df1\["A"\]  \# a DataFrame
Out\[8\]: 
   A  A
0  0  1
1  3  4

Copy to clipboard

This applies to row labels as well

In \[9\]: df2 \= pd.DataFrame({"A": \[0, 1, 2\]}, index\=\["a", "a", "b"\])

In \[10\]: df2
Out\[10\]: 
   A
a  0
a  1
b  2

In \[11\]: df2.loc\["b", "A"\]  \# a scalar
Out\[11\]: np.int64(2)

In \[12\]: df2.loc\["a", "A"\]  \# a Series
Out\[12\]: 
a    0
a    1
Name: A, dtype: int64

Copy to clipboard

Duplicate Label Detection[#](https://pandas.pydata.org/docs/user_guide/duplicates.html#duplicate-label-detection "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

You can check whether an `Index` (storing the row or column labels) is unique with `Index.is_unique`:

In \[13\]: df2
Out\[13\]: 
   A
a  0
a  1
b  2

In \[14\]: df2.index.is\_unique
Out\[14\]: False

In \[15\]: df2.columns.is\_unique
Out\[15\]: True

Copy to clipboard

Note

Checking whether an index is unique is somewhat expensive for large datasets. pandas does cache this result, so re-checking on the same index is very fast.

`Index.duplicated()` will return a boolean ndarray indicating whether a label is repeated.

In \[16\]: df2.index.duplicated()
Out\[16\]: array(\[False,  True, False\])

Copy to clipboard

Which can be used as a boolean filter to drop duplicate rows.

In \[17\]: df2.loc\[~df2.index.duplicated(), :\]
Out\[17\]: 
   A
a  0
b  2

Copy to clipboard

This approach keeps the first occurrence of each label. To keep the last occurrence instead, you can pass `keep="last"`:

In \[18\]: df2.loc\[~df2.index.duplicated(keep\="last"), :\]
Out\[18\]: 
   A
a  1
b  2

Copy to clipboard

If you want to remove all occurrences of duplicated labels, you can use `keep=False`:

In \[19\]: df2.loc\[~df2.index.duplicated(keep\=False), :\]
Out\[19\]: 
   A
b  2

Copy to clipboard

If you need additional logic to handle duplicate labels, rather than just dropping the repeats, using `groupby()` on the index is a common trick. For example, we’ll resolve duplicates by taking the average of all rows with the same label.

In \[20\]: df2.groupby(level\=0).mean()
Out\[20\]: 
     A
a  0.5
b  2.0

Copy to clipboard

Disallowing Duplicate Labels[#](https://pandas.pydata.org/docs/user_guide/duplicates.html#disallowing-duplicate-labels "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

As noted above, handling duplicates is an important feature when reading in raw data. That said, you may want to avoid introducing duplicates as part of a data processing pipeline (from methods like [`pandas.concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat "pandas.concat")
, `rename()`, etc.). Both `Series` and `DataFrame` _disallow_ duplicate labels by calling `.set_flags(allows_duplicate_labels=False)`. (the default is to allow them). If there are duplicate labels, an exception will be raised.

In \[21\]: pd.Series(\[0, 1, 2\], index\=\["a", "b", "b"\]).set\_flags(allows\_duplicate\_labels\=False)
\---------------------------------------------------------------------------
DuplicateLabelError                       Traceback (most recent call last)
Cell In\[21\], line 1
\----> 1 pd.Series(\[0, 1, 2\], index\=\["a", "b", "b"\]).set\_flags(allows\_duplicate\_labels\=False)

File ~/work/pandas/pandas/pandas/core/generic.py:484, in NDFrame.set\_flags(self, copy, allows\_duplicate\_labels)
    480         """
    481         self.\_check\_copy\_deprecation(copy)
    482         df = self.copy(deep=False)
    483         if allows\_duplicate\_labels is not None:
\--> 484             df.flags\["allows\_duplicate\_labels"\] = allows\_duplicate\_labels
    485         return df

File ~/work/pandas/pandas/pandas/core/flags.py:121, in Flags.\_\_setitem\_\_(self, key, value)
    119 if key not in self.\_keys:
    120     raise ValueError(f"Unknown flag {key}. Must be one of {self.\_keys}")
\--> 121 setattr(self, key, value)

File ~/work/pandas/pandas/pandas/core/flags.py:108, in Flags.allows\_duplicate\_labels(self, value)
    106 if not value:
    107     for ax in obj.axes:
\--> 108         ax.\_maybe\_check\_unique()
    110 self.\_allows\_duplicate\_labels = value

File ~/work/pandas/pandas/pandas/core/indexes/base.py:726, in Index.\_maybe\_check\_unique(self)
    723 duplicates = self.\_format\_duplicate\_message()
    724 msg += f"\\n{duplicates}"
\--> 726 raise DuplicateLabelError(msg)

DuplicateLabelError: Index has duplicates.
      positions
label          
b        \[1, 2\]

Copy to clipboard

This applies to both row and column labels for a `DataFrame`

In \[22\]: pd.DataFrame(\[\[0, 1, 2\], \[3, 4, 5\]\], columns\=\["A", "B", "C"\],).set\_flags(
   ....:    allows\_duplicate\_labels\=False
   ....: )
   ....: 
Out\[22\]: 
   A  B  C
0  0  1  2
1  3  4  5

Copy to clipboard

This attribute can be checked or set with `allows_duplicate_labels`, which indicates whether that object can have duplicate labels.

In \[23\]: df \= pd.DataFrame({"A": \[0, 1, 2, 3\]}, index\=\["x", "y", "X", "Y"\]).set\_flags(
   ....:    allows\_duplicate\_labels\=False
   ....: )
   ....: 

In \[24\]: df
Out\[24\]: 
   A
x  0
y  1
X  2
Y  3

In \[25\]: df.flags.allows\_duplicate\_labels
Out\[25\]: False

Copy to clipboard

`DataFrame.set_flags()` can be used to return a new `DataFrame` with attributes like `allows_duplicate_labels` set to some value

In \[26\]: df2 \= df.set\_flags(allows\_duplicate\_labels\=True)

In \[27\]: df2.flags.allows\_duplicate\_labels
Out\[27\]: True

Copy to clipboard

The new `DataFrame` returned is a view on the same data as the old `DataFrame`. Or the property can just be set directly on the same object

In \[28\]: df2.flags.allows\_duplicate\_labels \= False

In \[29\]: df2.flags.allows\_duplicate\_labels
Out\[29\]: False

Copy to clipboard

When processing raw, messy data you might initially read in the messy data (which potentially has duplicate labels), deduplicate, and then disallow duplicates going forward, to ensure that your data pipeline doesn’t introduce duplicates.

\>>> raw \= pd.read\_csv("...")
\>>> deduplicated \= raw.groupby(level\=0).first()  \# remove duplicates
\>>> deduplicated.flags.allows\_duplicate\_labels \= False  \# disallow going forward

Copy to clipboard

Setting `allows_duplicate_labels=False` on a `Series` or `DataFrame` with duplicate labels or performing an operation that introduces duplicate labels on a `Series` or `DataFrame` that disallows duplicates will raise an `errors.DuplicateLabelError`.

In \[30\]: df.rename(str.upper)
\---------------------------------------------------------------------------
DuplicateLabelError                       Traceback (most recent call last)
Cell In\[30\], line 1
\----> 1 df.rename(str.upper)

File ~/work/pandas/pandas/pandas/core/frame.py:7167, in DataFrame.rename(self, mapper, index, columns, axis, copy, inplace, level, errors)
   7163         """
   7164         inplace = self.\_check\_inplace\_deprecation(inplace, "rename")
   7165         self.\_check\_copy\_deprecation(copy)
   7166 
\-> 7167         return super().\_rename(
   7168             mapper=mapper,
   7169             index=index,
   7170             columns=columns,

File ~/work/pandas/pandas/pandas/core/generic.py:1078, in NDFrame.\_rename(self, mapper, index, columns, axis, inplace, level, errors)
   1074         if inplace:
   1075             self.\_update\_inplace(result)
   1076             return None
   1077         else:
\-> 1078             return result.\_\_finalize\_\_(self, method="rename")

File ~/work/pandas/pandas/pandas/core/generic.py:6398, in NDFrame.\_\_finalize\_\_(self, other, method, \*\*kwargs)
   6394                 self.attrs = deepcopy(other.attrs)
   6395             # Since new objects always start with allows\_duplicate\_labels=True,
   6396             # we only need to act when other has it set to False.
   6397             if not other.\_flags.\_allows\_duplicate\_labels:
\-> 6398                 self.flags.allows\_duplicate\_labels = False
   6399             # For subclasses using \_metadata.
   6400             for name in set(self.\_metadata) & set(other.\_metadata):
   6401                 assert isinstance(name, str)

File ~/work/pandas/pandas/pandas/core/flags.py:108, in Flags.allows\_duplicate\_labels(self, value)
    106 if not value:
    107     for ax in obj.axes:
\--> 108         ax.\_maybe\_check\_unique()
    110 self.\_allows\_duplicate\_labels = value

File ~/work/pandas/pandas/pandas/core/indexes/base.py:726, in Index.\_maybe\_check\_unique(self)
    723 duplicates = self.\_format\_duplicate\_message()
    724 msg += f"\\n{duplicates}"
\--> 726 raise DuplicateLabelError(msg)

DuplicateLabelError: Index has duplicates.
      positions
label          
X        \[0, 2\]
Y        \[1, 3\]

Copy to clipboard

This error message contains the labels that are duplicated, and the numeric positions of all the duplicates (including the “original”) in the `Series` or `DataFrame`

### Duplicate Label Propagation[#](https://pandas.pydata.org/docs/user_guide/duplicates.html#duplicate-label-propagation "Link to this heading")

In general, disallowing duplicates is “sticky”. It’s preserved through operations.

In \[31\]: s1 \= pd.Series(0, index\=\["a", "b"\]).set\_flags(allows\_duplicate\_labels\=False)

In \[32\]: s1
Out\[32\]: 
a    0
b    0
dtype: int64

In \[33\]: s1.head().rename({"a": "b"})
\---------------------------------------------------------------------------
DuplicateLabelError                       Traceback (most recent call last)
Cell In\[33\], line 1
\----> 1 s1.head().rename({"a": "b"})

File ~/work/pandas/pandas/pandas/core/series.py:5731, in Series.rename(self, index, axis, copy, inplace, level, errors)
   5727             \# error: Argument 1 to "\_rename" of "NDFrame" has incompatible
   5728             \# type "Union\[Union\[Mapping\[Any, Hashable\], Callable\[\[Any\],\
   5729             \# Hashable\]\], Hashable, None\]"; expected "Union\[Mapping\[Any,\
   5730             \# Hashable\], Callable\[\[Any\], Hashable\], None\]"
\-> 5731             return super().\_rename(
   5732                 index,  \# type: ignore\[arg-type\]
   5733                 inplace\=inplace,
   5734                 level\=level,

File ~/work/pandas/pandas/pandas/core/generic.py:1078, in NDFrame.\_rename(self, mapper, index, columns, axis, inplace, level, errors)
   1074         if inplace:
   1075             self.\_update\_inplace(result)
   1076             return None
   1077         else:
\-> 1078             return result.\_\_finalize\_\_(self, method\="rename")

File ~/work/pandas/pandas/pandas/core/generic.py:6398, in NDFrame.\_\_finalize\_\_(self, other, method, \*\*kwargs)
   6394                 self.attrs \= deepcopy(other.attrs)
   6395             \# Since new objects always start with allows\_duplicate\_labels=True,
   6396             \# we only need to act when other has it set to False.
   6397             if not other.\_flags.\_allows\_duplicate\_labels:
\-> 6398                 self.flags.allows\_duplicate\_labels \= False
   6399             \# For subclasses using \_metadata.
   6400             for name in set(self.\_metadata) & set(other.\_metadata):
   6401                 assert isinstance(name, str)

File ~/work/pandas/pandas/pandas/core/flags.py:108, in Flags.allows\_duplicate\_labels(self, value)
    106 if not value:
    107     for ax in obj.axes:
\--> 108         ax.\_maybe\_check\_unique()
    110 self.\_allows\_duplicate\_labels \= value

File ~/work/pandas/pandas/pandas/core/indexes/base.py:726, in Index.\_maybe\_check\_unique(self)
    723 duplicates \= self.\_format\_duplicate\_message()
    724 msg += f"\\n{duplicates}"
\--> 726 raise DuplicateLabelError(msg)

DuplicateLabelError: Index has duplicates.
      positions
label          
b        \[0, 1\]

Copy to clipboard

Warning

Many methods do not yet propagate the `allows_duplicate_labels` value through to their result. The long-term goal is for every method that takes or returns a `DataFrame` or `Series` to preserve it.

On this page