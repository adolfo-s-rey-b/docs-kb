[Skip to main content](https://pandas.pydata.org/docs/user_guide/advanced.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/user_guide/advanced.html)
[3.1 (stable)](https://pandas.pydata.org/docs/user_guide/advanced.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/user_guide/advanced.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/advanced.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/user_guide/advanced.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/user_guide/advanced.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/advanced.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/user_guide/advanced.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/user_guide/advanced.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/user_guide/advanced.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/user_guide/advanced.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/advanced.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/user_guide/advanced.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

MultiIndex / advanced indexing[#](https://pandas.pydata.org/docs/user_guide/advanced.html#multiindex-advanced-indexing "Link to this heading")

===============================================================================================================================================

This section covers [indexing with a MultiIndex](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-hierarchical)
 and [other advanced indexing features](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-index-types)
.

See the [Indexing and Selecting Data](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing)
 for general indexing documentation.

See the [cookbook](https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook-selection)
 for some advanced strategies.

Hierarchical indexing (MultiIndex)[#](https://pandas.pydata.org/docs/user_guide/advanced.html#hierarchical-indexing-multiindex "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

Hierarchical / Multi-level indexing is very exciting as it opens the door to some quite sophisticated data analysis and manipulation, especially for working with higher dimensional data. In essence, it enables you to store and manipulate data with an arbitrary number of dimensions in lower dimensional data structures like `Series` (1d) and `DataFrame` (2d).

In this section, we will show what exactly we mean by “hierarchical” indexing and how it integrates with all of the pandas indexing functionality described above and in prior sections. Later, when discussing [group by](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby)
 and [pivoting and reshaping data](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping)
, we’ll show non-trivial applications to illustrate how it aids in structuring data for analysis.

See the [cookbook](https://pandas.pydata.org/docs/user_guide/cookbook.html#cookbook-multi-index)
 for some advanced strategies.

### Creating a MultiIndex (hierarchical index) object[#](https://pandas.pydata.org/docs/user_guide/advanced.html#creating-a-multiindex-hierarchical-index-object "Link to this heading")

The [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")
 object is the hierarchical analogue of the standard [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 object which typically stores the axis labels in pandas objects. You can think of `MultiIndex` as an array of tuples where each tuple is unique. A `MultiIndex` can be created from a list of arrays (using [`MultiIndex.from_arrays()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_arrays.html#pandas.MultiIndex.from_arrays "pandas.MultiIndex.from_arrays")
), an array of tuples (using [`MultiIndex.from_tuples()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_tuples.html#pandas.MultiIndex.from_tuples "pandas.MultiIndex.from_tuples")
), a crossed set of iterables (using [`MultiIndex.from_product()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#pandas.MultiIndex.from_product "pandas.MultiIndex.from_product")
), or a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (using [`MultiIndex.from_frame()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#pandas.MultiIndex.from_frame "pandas.MultiIndex.from_frame")
). The `Index` constructor will attempt to return a `MultiIndex` when it is passed a list of tuples. The following examples demonstrate different ways to initialize MultiIndexes.

In \[1\]: arrays \= \[\
   ...:    \["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"\],\
   ...:    \["one", "two", "one", "two", "one", "two", "one", "two"\],\
   ...: \]
   ...: 

In \[2\]: tuples \= list(zip(\*arrays))

In \[3\]: tuples
Out\[3\]: 
\[('bar', 'one'),\
 ('bar', 'two'),\
 ('baz', 'one'),\
 ('baz', 'two'),\
 ('foo', 'one'),\
 ('foo', 'two'),\
 ('qux', 'one'),\
 ('qux', 'two')\]

In \[4\]: index \= pd.MultiIndex.from\_tuples(tuples, names\=\["first", "second"\])

In \[5\]: index
Out\[5\]: 
MultiIndex(\[('bar', 'one'),\
            ('bar', 'two'),\
            ('baz', 'one'),\
            ('baz', 'two'),\
            ('foo', 'one'),\
            ('foo', 'two'),\
            ('qux', 'one'),\
            ('qux', 'two')\],
           names=\['first', 'second'\])

In \[6\]: s \= pd.Series(np.random.randn(8), index\=index)

In \[7\]: s
Out\[7\]: 
first  second
bar    one       0.469112
       two      -0.282863
baz    one      -1.509059
       two      -1.135632
foo    one       1.212112
       two      -0.173215
qux    one       0.119209
       two      -1.044236
dtype: float64

Copy to clipboard

When you want every pairing of the elements in two iterables, it can be easier to use the [`MultiIndex.from_product()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_product.html#pandas.MultiIndex.from_product "pandas.MultiIndex.from_product")
 method:

In \[8\]: iterables \= \[\["bar", "baz", "foo", "qux"\], \["one", "two"\]\]

In \[9\]: pd.MultiIndex.from\_product(iterables, names\=\["first", "second"\])
Out\[9\]: 
MultiIndex(\[('bar', 'one'),\
            ('bar', 'two'),\
            ('baz', 'one'),\
            ('baz', 'two'),\
            ('foo', 'one'),\
            ('foo', 'two'),\
            ('qux', 'one'),\
            ('qux', 'two')\],
           names=\['first', 'second'\])

Copy to clipboard

You can also construct a `MultiIndex` from a `DataFrame` directly, using the method [`MultiIndex.from_frame()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.from_frame.html#pandas.MultiIndex.from_frame "pandas.MultiIndex.from_frame")
. This is a complementary method to [`MultiIndex.to_frame()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.to_frame.html#pandas.MultiIndex.to_frame "pandas.MultiIndex.to_frame")
.

In \[10\]: df \= pd.DataFrame(
   ....:    \[\["bar", "one"\], \["bar", "two"\], \["foo", "one"\], \["foo", "two"\]\],
   ....:    columns\=\["first", "second"\],
   ....: )
   ....: 

In \[11\]: pd.MultiIndex.from\_frame(df)
Out\[11\]: 
MultiIndex(\[('bar', 'one'),\
            ('bar', 'two'),\
            ('foo', 'one'),\
            ('foo', 'two')\],
           names=\['first', 'second'\])

Copy to clipboard

As a convenience, you can pass a list of arrays directly into `Series` or `DataFrame` to construct a `MultiIndex` automatically:

In \[12\]: arrays \= \[\
   ....:    np.array(\["bar", "bar", "baz", "baz", "foo", "foo", "qux", "qux"\]),\
   ....:    np.array(\["one", "two", "one", "two", "one", "two", "one", "two"\]),\
   ....: \]
   ....: 

In \[13\]: s \= pd.Series(np.random.randn(8), index\=arrays)

In \[14\]: s
Out\[14\]: 
bar  one   -0.861849
     two   -2.104569
baz  one   -0.494929
     two    1.071804
foo  one    0.721555
     two   -0.706771
qux  one   -1.039575
     two    0.271860
dtype: float64

In \[15\]: df \= pd.DataFrame(np.random.randn(8, 4), index\=arrays)

In \[16\]: df
Out\[16\]: 
                0         1         2         3
bar one -0.424972  0.567020  0.276232 -1.087401
    two -0.673690  0.113648 -1.478427  0.524988
baz one  0.404705  0.577046 -1.715002 -1.039268
    two -0.370647 -1.157892 -1.344312  0.844885
foo one  1.075770 -0.109050  1.643563 -1.469388
    two  0.357021 -0.674600 -1.776904 -0.968914
qux one -1.294524  0.413738  0.276662 -0.472035
    two -0.013960 -0.362543 -0.006154 -0.923061

Copy to clipboard

All of the `MultiIndex` constructors accept a `names` argument which stores string names for the levels themselves. If no names are provided, `None` will be assigned:

In \[17\]: df.index.names
Out\[17\]: FrozenList(\[None, None\])

Copy to clipboard

This index can back any axis of a pandas object, and the number of **levels** of the index is up to you:

In \[18\]: df \= pd.DataFrame(np.random.randn(3, 8), index\=\["A", "B", "C"\], columns\=index)

In \[19\]: df
Out\[19\]: 
first        bar                 baz  ...                 qux          
second       one       two       one  ...       two       one       two
A       0.895717  0.805244 -1.206412  ...  1.340309 -1.170299 -0.226169
B       0.410835  0.813850  0.132003  ... -1.187678  1.130127 -1.436737
C      -1.413681  1.607920  1.024180  ... -2.211372  0.974466 -2.006747

\[3 rows x 8 columns\]

In \[20\]: pd.DataFrame(np.random.randn(6, 6), index\=index\[:6\], columns\=index\[:6\])
Out\[20\]: 
first              bar                 baz                 foo          
second             one       two       one       two       one       two
first second                                                            
bar   one    -0.410001 -0.078638  0.545952 -1.219217 -1.226825  0.769804
      two    -1.281247 -0.727707 -0.121306 -0.097883  0.695775  0.341734
baz   one     0.959726 -1.110336 -0.619976  0.149748 -0.732339  0.687738
      two     0.176444  0.403310 -0.154951  0.301624 -2.179861 -1.369849
foo   one    -0.954208  1.462696 -1.743161 -0.826591 -0.345352  1.314232
      two     0.690579  0.995761  2.396780  0.014871  3.357427 -0.317441

Copy to clipboard

We’ve “sparsified” the higher levels of the indexes to make the console output a bit easier on the eyes. Note that how the index is displayed can be controlled using the `multi_sparse` option in `pandas.set_option()`:

In \[21\]: with pd.option\_context("display.multi\_sparse", False):
   ....:    df
   ....: 

Copy to clipboard

It’s worth keeping in mind that there’s nothing preventing you from using tuples as atomic labels on an axis:

In \[22\]: pd.Series(np.random.randn(8), index\=tuples)
Out\[22\]: 
(bar, one)   -1.236269
(bar, two)    0.896171
(baz, one)   -0.487602
(baz, two)   -0.082240
(foo, one)   -2.182937
(foo, two)    0.380396
(qux, one)    0.084844
(qux, two)    0.432390
dtype: float64

Copy to clipboard

The reason that the `MultiIndex` matters is that it can allow you to do grouping, selection, and reshaping operations as we will describe below and in subsequent areas of the documentation. As you will see in later sections, you can find yourself working with hierarchically-indexed data without creating a `MultiIndex` explicitly yourself. However, when loading data from a file, you may wish to generate your own `MultiIndex` when preparing the data set.

### Reconstructing the level labels[#](https://pandas.pydata.org/docs/user_guide/advanced.html#reconstructing-the-level-labels "Link to this heading")

The method [`get_level_values()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_level_values.html#pandas.MultiIndex.get_level_values "pandas.MultiIndex.get_level_values")
 will return a vector of the labels for each location at a particular level:

In \[23\]: index.get\_level\_values(0)
Out\[23\]: 
Index(\['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'\], dtype='str',
      name='first')

In \[24\]: index.get\_level\_values("second")
Out\[24\]: 
Index(\['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two'\], dtype='str',
      name='second')

Copy to clipboard

### Basic indexing on axis with MultiIndex[#](https://pandas.pydata.org/docs/user_guide/advanced.html#basic-indexing-on-axis-with-multiindex "Link to this heading")

One of the important features of hierarchical indexing is that you can select data by a “partial” label identifying a subgroup in the data. **Partial** selection “drops” levels of the hierarchical index in the result in a completely analogous way to selecting a column in a regular DataFrame:

In \[25\]: df\["bar"\]
Out\[25\]: 
second       one       two
A       0.895717  0.805244
B       0.410835  0.813850
C      -1.413681  1.607920

In \[26\]: df\["bar", "one"\]
Out\[26\]: 
A    0.895717
B    0.410835
C   -1.413681
Name: (bar, one), dtype: float64

In \[27\]: df\["bar"\]\["one"\]
Out\[27\]: 
A    0.895717
B    0.410835
C   -1.413681
Name: one, dtype: float64

In \[28\]: s\["qux"\]
Out\[28\]: 
one   -1.039575
two    0.271860
dtype: float64

Copy to clipboard

For a `Series`, `[]` selects on the index, so `s["qux"]` above performs partial selection on the row labels. For a `DataFrame`, however, `[]` selects _columns_: `df["bar"]` works above only because this `df` has a `MultiIndex` on its columns. If the `MultiIndex` is on the rows instead, selecting a partial label with `[]` raises a `KeyError` — use `.loc` for partial selection on the rows:

In \[29\]: df.T\["bar"\]
\---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
File ~/work/pandas/pandas/pandas/core/indexes/base.py:3816, in Index.get\_loc(self, key)
   3815 try:
\-> 3816     return self.\_engine.get\_loc(casted\_key)
   3817 except KeyError as err:

File pandas/\_libs/index.pyx:172, in pandas.\_libs.index.IndexEngine.get\_loc()
\--> 172 'Could not get source, probably due dynamically evaluated source code.'
File pandas/\_libs/index.pyx:201, in pandas.\_libs.index.IndexEngine.get\_loc()
\--> 201 'Could not get source, probably due dynamically evaluated source code.'
File pandas/\_libs/hashtable\_class\_helper.pxi:7726, in pandas.\_libs.hashtable.PyObjectHashTable.get\_item()
\-> 7726 'Could not get source, probably due dynamically evaluated source code.'
File pandas/\_libs/hashtable\_class\_helper.pxi:7734, in pandas.\_libs.hashtable.PyObjectHashTable.get\_item()
\-> 7734 'Could not get source, probably due dynamically evaluated source code.'
KeyError: 'bar'

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
Cell In\[29\], line 1
\----> 1 df.T\["bar"\]

File ~/work/pandas/pandas/pandas/core/frame.py:4330, in DataFrame.\_\_getitem\_\_(self, key)
   4326 
   4327         if is\_single\_key:
   4328             if self.columns.nlevels \> 1:
   4329                 return self.\_getitem\_multilevel(key)
\-> 4330             indexer \= self.columns.get\_loc(key)
   4331             if is\_integer(indexer):
   4332                 indexer \= \[indexer\]  \# type: ignore\[assignment\]
   4333         else:

File ~/work/pandas/pandas/pandas/core/indexes/base.py:3823, in Index.get\_loc(self, key)
   3818     if isinstance(casted\_key, slice) or (
   3819         isinstance(casted\_key, abc.Iterable)
   3820         and any(isinstance(x, slice) for x in casted\_key)
   3821     ):
   3822         raise InvalidIndexError(key) from err
\-> 3823     raise KeyError(key) from err
   3824 except TypeError:
   3825     \# If we have a listlike key, \_check\_indexing\_error will raise
   3826     \#  InvalidIndexError. Otherwise we fall through and re-raise
   3827     \#  the TypeError.
   3828     self.\_check\_indexing\_error(key)

KeyError: 'bar'

Copy to clipboard

In \[30\]: df.T.loc\["bar"\]
Out\[30\]: 
               A         B         C
second                              
one     0.895717  0.410835 -1.413681
two     0.805244  0.813850  1.607920

Copy to clipboard

See [Cross-section with hierarchical index](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-xs)
 for how to select on a deeper level.

Note

Empty strings in a `MultiIndex` on the columns are treated as missing level values when selecting with `[]`. For example, with columns `pd.MultiIndex.from_tuples([("a", ""), ("b", "c")])`, selecting `df["a"]` drops the empty level and returns a `Series` rather than a `DataFrame` with a single column labeled `""`.

### Defined levels[#](https://pandas.pydata.org/docs/user_guide/advanced.html#defined-levels "Link to this heading")

The [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")
 keeps all the defined levels of an index, even if they are not actually used. When slicing an index, you may notice this. For example:

In \[31\]: df.columns.levels  \# original MultiIndex
Out\[31\]: FrozenList(\[\['bar', 'baz', 'foo', 'qux'\], \['one', 'two'\]\])

In \[32\]: df\[\["foo","qux"\]\].columns.levels  \# sliced
Out\[32\]: FrozenList(\[\['bar', 'baz', 'foo', 'qux'\], \['one', 'two'\]\])

Copy to clipboard

This is done to avoid a recomputation of the levels in order to make slicing highly performant. If you want to see only the used levels, you can use the [`get_level_values()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.get_level_values.html#pandas.MultiIndex.get_level_values "pandas.MultiIndex.get_level_values")
 method.

In \[33\]: df\[\["foo", "qux"\]\].columns.to\_numpy()
Out\[33\]: 
array(\[('foo', 'one'), ('foo', 'two'), ('qux', 'one'), ('qux', 'two')\],
      dtype=object)

\# for a specific level
In \[34\]: df\[\["foo", "qux"\]\].columns.get\_level\_values(0)
Out\[34\]: Index(\['foo', 'foo', 'qux', 'qux'\], dtype='str', name='first')

Copy to clipboard

To reconstruct the `MultiIndex` with only the used levels, the [`remove_unused_levels()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.remove_unused_levels.html#pandas.MultiIndex.remove_unused_levels "pandas.MultiIndex.remove_unused_levels")
 method may be used.

In \[35\]: new\_mi \= df\[\["foo", "qux"\]\].columns.remove\_unused\_levels()

In \[36\]: new\_mi.levels
Out\[36\]: FrozenList(\[\['foo', 'qux'\], \['one', 'two'\]\])

Copy to clipboard

### Data alignment and using `reindex`[#](https://pandas.pydata.org/docs/user_guide/advanced.html#data-alignment-and-using-reindex "Link to this heading")

Operations between differently-indexed objects having `MultiIndex` on the axes will work as you expect; data alignment will work the same as an Index of tuples:

In \[37\]: s + s\[:\-2\]
Out\[37\]: 
bar  one   -1.723698
     two   -4.209138
baz  one   -0.989859
     two    2.143608
foo  one    1.443110
     two   -1.413542
qux  one         NaN
     two         NaN
dtype: float64

In \[38\]: s + s\[::2\]
Out\[38\]: 
bar  one   -1.723698
     two         NaN
baz  one   -0.989859
     two         NaN
foo  one    1.443110
     two         NaN
qux  one   -2.079150
     two         NaN
dtype: float64

Copy to clipboard

The [`reindex()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex")
 method of `Series`/`DataFrames` can be called with another `MultiIndex`, or even a list or array of tuples:

In \[39\]: s.reindex(index\[:3\])
Out\[39\]: 
first  second
bar    one      -0.861849
       two      -2.104569
baz    one      -0.494929
dtype: float64

In \[40\]: s.reindex(\[("foo", "two"), ("bar", "one"), ("qux", "one"), ("baz", "one")\])
Out\[40\]: 
foo  two   -0.706771
bar  one   -0.861849
qux  one   -1.039575
baz  one   -0.494929
dtype: float64

Copy to clipboard

Advanced indexing with hierarchical index[#](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-indexing-with-hierarchical-index "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Syntactically integrating `MultiIndex` in advanced indexing with `.loc` is a bit challenging, but we’ve made every effort to do so. In general, MultiIndex keys take the form of tuples. For example, the following works as you would expect:

In \[41\]: df \= df.T

In \[42\]: df
Out\[42\]: 
                     A         B         C
first second                              
bar   one     0.895717  0.410835 -1.413681
      two     0.805244  0.813850  1.607920
baz   one    -1.206412  0.132003  1.024180
      two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
qux   one    -1.170299  1.130127  0.974466
      two    -0.226169 -1.436737 -2.006747

In \[43\]: df.loc\[("bar", "two")\]
Out\[43\]: 
A    0.805244
B    0.813850
C    1.607920
Name: (bar, two), dtype: float64

Copy to clipboard

Note that `df.loc['bar', 'two']` would also work in this example, but this shorthand notation can lead to ambiguity in general.

If you also want to index a specific column with `.loc`, you must use a tuple like this:

In \[44\]: df.loc\[("bar", "two"), "A"\]
Out\[44\]: np.float64(0.8052440253863785)

Copy to clipboard

You don’t have to specify all levels of the `MultiIndex` by passing only the first elements of the tuple. For example, you can use “partial” indexing to get all elements with `bar` in the first level as follows:

In \[45\]: df.loc\["bar"\]
Out\[45\]: 
               A         B         C
second                              
one     0.895717  0.410835 -1.413681
two     0.805244  0.813850  1.607920

Copy to clipboard

This is a shortcut for the slightly more verbose notation `df.loc[('bar',),]` (equivalent to `df.loc['bar',]` in this example).

“Partial” slicing also works quite nicely.

In \[46\]: df.loc\["baz":"foo"\]
Out\[46\]: 
                     A         B         C
first second                              
baz   one    -1.206412  0.132003  1.024180
      two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372

Copy to clipboard

You can slice with a ‘range’ of values, by providing a slice of tuples.

In \[47\]: df.loc\[("baz", "two"):("qux", "one")\]
Out\[47\]: 
                     A         B         C
first second                              
baz   two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
qux   one    -1.170299  1.130127  0.974466

In \[48\]: df.loc\[("baz", "two"):"foo"\]
Out\[48\]: 
                     A         B         C
first second                              
baz   two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372

Copy to clipboard

Passing a list of labels or tuples works similar to reindexing:

In \[49\]: df.loc\[\[("bar", "two"), ("qux", "one")\]\]
Out\[49\]: 
                     A         B         C
first second                              
bar   two     0.805244  0.813850  1.607920
qux   one    -1.170299  1.130127  0.974466

Copy to clipboard

Note

It is important to note that tuples and lists are not treated identically in pandas when it comes to indexing. Whereas a tuple is interpreted as one multi-level key, a list is used to specify several keys. Or in other words, tuples go horizontally (traversing levels), lists go vertically (scanning levels).

Importantly, a list of tuples indexes several complete `MultiIndex` keys, whereas a tuple of lists refer to several values within a level:

In \[50\]: s \= pd.Series(
   ....:    \[1, 2, 3, 4, 5, 6\],
   ....:    index\=pd.MultiIndex.from\_product(\[\["A", "B"\], \["c", "d", "e"\]\]),
   ....: )
   ....: 

In \[51\]: s.loc\[\[("A", "c"), ("B", "d")\]\]  \# list of tuples
Out\[51\]: 
A  c    1
B  d    5
dtype: int64

In \[52\]: s.loc\[(\["A", "B"\], \["c", "d"\])\]  \# tuple of lists
Out\[52\]: 
A  c    1
   d    2
B  c    4
   d    5
dtype: int64

Copy to clipboard

### Using slicers[#](https://pandas.pydata.org/docs/user_guide/advanced.html#using-slicers "Link to this heading")

You can slice a `MultiIndex` by providing multiple indexers.

You can provide any of the selectors as if you are indexing by label, see [Selection by Label](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-label)
, including slices, lists of labels, labels, and boolean indexers.

You can use `slice(None)` to select all the contents of _that_ level. You do not need to specify all the _deeper_ levels, they will be implied as `slice(None)`.

As usual, **both sides** of the slicers are included as this is label indexing.

Warning

You should specify all axes in the `.loc` specifier, meaning the indexer for the **index** and for the **columns**. There are some ambiguous cases where the passed indexer could be misinterpreted as indexing _both_ axes, rather than into say the `MultiIndex` for the rows.

You should do this:

df.loc\[(slice("A1", "A3"), ...), :\]  \# noqa: E999

Copy to clipboard

You should **not** do this:

df.loc\[(slice("A1", "A3"), ...)\]  \# noqa: E999

Copy to clipboard

The same ambiguity arises with integer labels. `df.loc[0, 0]` is first tried as `df.loc[(0, 0)]` – a single key into the row `MultiIndex` – and is only interpreted as row label `0` of column label `0` when that lookup fails. Use [`pandas.IndexSlice`](https://pandas.pydata.org/docs/reference/api/pandas.IndexSlice.html#pandas.IndexSlice "pandas.IndexSlice")
, e.g. `df.loc[pd.IndexSlice[0, :], 0]`, or pass a length-1 tuple for the rows, e.g. `df.loc[(0,), 0]`, to disambiguate.

In \[53\]: def mklbl(prefix, n):
   ....:    return \["%s%s" % (prefix, i) for i in range(n)\]
   ....: 

In \[54\]: miindex \= pd.MultiIndex.from\_product(
   ....:    \[mklbl("A", 4), mklbl("B", 2), mklbl("C", 4), mklbl("D", 2)\]
   ....: )
   ....: 

In \[55\]: micolumns \= pd.MultiIndex.from\_tuples(
   ....:    \[("a", "foo"), ("a", "bar"), ("b", "foo"), ("b", "bah")\], names\=\["lvl0", "lvl1"\]
   ....: )
   ....: 

In \[56\]: dfmi \= (
   ....:    pd.DataFrame(
   ....:        np.arange(len(miindex) \* len(micolumns)).reshape(
   ....:            (len(miindex), len(micolumns))
   ....:        ),
   ....:        index\=miindex,
   ....:        columns\=micolumns,
   ....:    )
   ....:    .sort\_index()
   ....:    .sort\_index(axis\=1)
   ....: )
   ....: 

In \[57\]: dfmi
Out\[57\]: 
lvl0           a         b     
lvl1         bar  foo  bah  foo
A0 B0 C0 D0    1    0    3    2
         D1    5    4    7    6
      C1 D0    9    8   11   10
         D1   13   12   15   14
      C2 D0   17   16   19   18
...          ...  ...  ...  ...
A3 B1 C1 D1  237  236  239  238
      C2 D0  241  240  243  242
         D1  245  244  247  246
      C3 D0  249  248  251  250
         D1  253  252  255  254

\[64 rows x 4 columns\]

Copy to clipboard

Basic MultiIndex slicing using slices, lists, and labels.

In \[58\]: dfmi.loc\[(slice("A1", "A3"), slice(None), \["C1", "C3"\]), :\]
Out\[58\]: 
lvl0           a         b     
lvl1         bar  foo  bah  foo
A1 B0 C1 D0   73   72   75   74
         D1   77   76   79   78
      C3 D0   89   88   91   90
         D1   93   92   95   94
   B1 C1 D0  105  104  107  106
...          ...  ...  ...  ...
A3 B0 C3 D1  221  220  223  222
   B1 C1 D0  233  232  235  234
         D1  237  236  239  238
      C3 D0  249  248  251  250
         D1  253  252  255  254

\[24 rows x 4 columns\]

Copy to clipboard

You can use [`pandas.IndexSlice`](https://pandas.pydata.org/docs/reference/api/pandas.IndexSlice.html#pandas.IndexSlice "pandas.IndexSlice")
 to facilitate a more natural syntax using `:`, rather than using `slice(None)`.

In \[59\]: idx \= pd.IndexSlice

In \[60\]: dfmi.loc\[idx\[:, :, \["C1", "C3"\]\], idx\[:, "foo"\]\]
Out\[60\]: 
lvl0           a    b
lvl1         foo  foo
A0 B0 C1 D0    8   10
         D1   12   14
      C3 D0   24   26
         D1   28   30
   B1 C1 D0   40   42
...          ...  ...
A3 B0 C3 D1  220  222
   B1 C1 D0  232  234
         D1  236  238
      C3 D0  248  250
         D1  252  254

\[32 rows x 2 columns\]

Copy to clipboard

It is possible to perform quite complicated selections using this method on multiple axes at the same time.

In \[61\]: dfmi.loc\["A1", (slice(None), "foo")\]
Out\[61\]: 
lvl0        a    b
lvl1      foo  foo
B0 C0 D0   64   66
      D1   68   70
   C1 D0   72   74
      D1   76   78
   C2 D0   80   82
...       ...  ...
B1 C1 D1  108  110
   C2 D0  112  114
      D1  116  118
   C3 D0  120  122
      D1  124  126

\[16 rows x 2 columns\]

In \[62\]: dfmi.loc\[idx\[:, :, \["C1", "C3"\]\], idx\[:, "foo"\]\]
Out\[62\]: 
lvl0           a    b
lvl1         foo  foo
A0 B0 C1 D0    8   10
         D1   12   14
      C3 D0   24   26
         D1   28   30
   B1 C1 D0   40   42
...          ...  ...
A3 B0 C3 D1  220  222
   B1 C1 D0  232  234
         D1  236  238
      C3 D0  248  250
         D1  252  254

\[32 rows x 2 columns\]

Copy to clipboard

Using a boolean indexer you can provide selection related to the _values_.

In \[63\]: mask \= dfmi\[("a", "foo")\] \> 200

In \[64\]: dfmi.loc\[idx\[mask, :, \["C1", "C3"\]\], idx\[:, "foo"\]\]
Out\[64\]: 
lvl0           a    b
lvl1         foo  foo
A3 B0 C1 D1  204  206
      C3 D0  216  218
         D1  220  222
   B1 C1 D0  232  234
         D1  236  238
      C3 D0  248  250
         D1  252  254

Copy to clipboard

You can also specify the `axis` argument to `.loc` to interpret the passed slicers on a single axis.

In \[65\]: dfmi.loc(axis\=0)\[:, :, \["C1", "C3"\]\]
Out\[65\]: 
lvl0           a         b     
lvl1         bar  foo  bah  foo
A0 B0 C1 D0    9    8   11   10
         D1   13   12   15   14
      C3 D0   25   24   27   26
         D1   29   28   31   30
   B1 C1 D0   41   40   43   42
...          ...  ...  ...  ...
A3 B0 C3 D1  221  220  223  222
   B1 C1 D0  233  232  235  234
         D1  237  236  239  238
      C3 D0  249  248  251  250
         D1  253  252  255  254

\[32 rows x 4 columns\]

Copy to clipboard

Furthermore, you can _set_ the values using the following methods.

In \[66\]: df2 \= dfmi.copy()

In \[67\]: df2.loc(axis\=0)\[:, :, \["C1", "C3"\]\] \= \-10

In \[68\]: df2
Out\[68\]: 
lvl0           a         b     
lvl1         bar  foo  bah  foo
A0 B0 C0 D0    1    0    3    2
         D1    5    4    7    6
      C1 D0  -10  -10  -10  -10
         D1  -10  -10  -10  -10
      C2 D0   17   16   19   18
...          ...  ...  ...  ...
A3 B1 C1 D1  -10  -10  -10  -10
      C2 D0  241  240  243  242
         D1  245  244  247  246
      C3 D0  -10  -10  -10  -10
         D1  -10  -10  -10  -10

\[64 rows x 4 columns\]

Copy to clipboard

You can use a right-hand-side of an alignable object as well.

In \[69\]: df2 \= dfmi.copy()

In \[70\]: df2.loc\[idx\[:, :, \["C1", "C3"\]\], :\] \= df2 \* 1000

In \[71\]: df2
Out\[71\]: 
lvl0              a               b        
lvl1            bar     foo     bah     foo
A0 B0 C0 D0       1       0       3       2
         D1       5       4       7       6
      C1 D0    9000    8000   11000   10000
         D1   13000   12000   15000   14000
      C2 D0      17      16      19      18
...             ...     ...     ...     ...
A3 B1 C1 D1  237000  236000  239000  238000
      C2 D0     241     240     243     242
         D1     245     244     247     246
      C3 D0  249000  248000  251000  250000
         D1  253000  252000  255000  254000

\[64 rows x 4 columns\]

Copy to clipboard

### Cross-section[#](https://pandas.pydata.org/docs/user_guide/advanced.html#cross-section "Link to this heading")

The [`xs()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.xs.html#pandas.DataFrame.xs "pandas.DataFrame.xs")
 method of `DataFrame` additionally takes a level argument to make selecting data at a particular level of a `MultiIndex` easier.

In \[72\]: df
Out\[72\]: 
                     A         B         C
first second                              
bar   one     0.895717  0.410835 -1.413681
      two     0.805244  0.813850  1.607920
baz   one    -1.206412  0.132003  1.024180
      two     2.565646 -0.827317  0.569605
foo   one     1.431256 -0.076467  0.875906
      two     1.340309 -1.187678 -2.211372
qux   one    -1.170299  1.130127  0.974466
      two    -0.226169 -1.436737 -2.006747

In \[73\]: df.xs("one", level\="second")
Out\[73\]: 
              A         B         C
first                              
bar    0.895717  0.410835 -1.413681
baz   -1.206412  0.132003  1.024180
foo    1.431256 -0.076467  0.875906
qux   -1.170299  1.130127  0.974466

Copy to clipboard

\# using the slicers
In \[74\]: df.loc\[(slice(None), "one"), :\]
Out\[74\]: 
                     A         B         C
first second                              
bar   one     0.895717  0.410835 -1.413681
baz   one    -1.206412  0.132003  1.024180
foo   one     1.431256 -0.076467  0.875906
qux   one    -1.170299  1.130127  0.974466

Copy to clipboard

You can also select on the columns with `xs`, by providing the axis argument.

In \[75\]: df \= df.T

In \[76\]: df.xs("one", level\="second", axis\=1)
Out\[76\]: 
first       bar       baz       foo       qux
A      0.895717 -1.206412  1.431256 -1.170299
B      0.410835  0.132003 -0.076467  1.130127
C     -1.413681  1.024180  0.875906  0.974466

Copy to clipboard

\# using the slicers
In \[77\]: df.loc\[:, (slice(None), "one")\]
Out\[77\]: 
first        bar       baz       foo       qux
second       one       one       one       one
A       0.895717 -1.206412  1.431256 -1.170299
B       0.410835  0.132003 -0.076467  1.130127
C      -1.413681  1.024180  0.875906  0.974466

Copy to clipboard

`xs` also allows selection with multiple keys.

In \[78\]: df.xs(("one", "bar"), level\=("second", "first"), axis\=1)
Out\[78\]: 
first        bar
second       one
A       0.895717
B       0.410835
C      -1.413681

Copy to clipboard

\# using the slicers
In \[79\]: df.loc\[:, ("bar", "one")\]
Out\[79\]: 
A    0.895717
B    0.410835
C   -1.413681
Name: (bar, one), dtype: float64

Copy to clipboard

You can pass `drop_level=False` to `xs` to retain the level that was selected.

In \[80\]: df.xs("one", level\="second", axis\=1, drop\_level\=False)
Out\[80\]: 
first        bar       baz       foo       qux
second       one       one       one       one
A       0.895717 -1.206412  1.431256 -1.170299
B       0.410835  0.132003 -0.076467  1.130127
C      -1.413681  1.024180  0.875906  0.974466

Copy to clipboard

Compare the above with the result using `drop_level=True` (the default value).

In \[81\]: df.xs("one", level\="second", axis\=1, drop\_level\=True)
Out\[81\]: 
first       bar       baz       foo       qux
A      0.895717 -1.206412  1.431256 -1.170299
B      0.410835  0.132003 -0.076467  1.130127
C     -1.413681  1.024180  0.875906  0.974466

Copy to clipboard

### Advanced reindexing and alignment[#](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-reindexing-and-alignment "Link to this heading")

Using the parameter `level` in the [`reindex()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex")
 and [`align()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.align.html#pandas.DataFrame.align "pandas.DataFrame.align")
 methods of pandas objects is useful to broadcast values across a level. For instance:

In \[82\]: midx \= pd.MultiIndex(
   ....:    levels\=\[\["zero", "one"\], \["x", "y"\]\], codes\=\[\[1, 1, 0, 0\], \[1, 0, 1, 0\]\]
   ....: )
   ....: 

In \[83\]: df \= pd.DataFrame(np.random.randn(4, 2), index\=midx)

In \[84\]: df
Out\[84\]: 
               0         1
one  y  1.519970 -0.493662
     x  0.600178  0.274230
zero y  0.132885 -0.023688
     x  2.410179  1.450520

In \[85\]: df2 \= df.groupby(level\=0).mean()

In \[86\]: df2
Out\[86\]: 
             0         1
one   1.060074 -0.109716
zero  1.271532  0.713416

In \[87\]: df2.reindex(df.index, level\=0)
Out\[87\]: 
               0         1
one  y  1.060074 -0.109716
     x  1.060074 -0.109716
zero y  1.271532  0.713416
     x  1.271532  0.713416

\# aligning
In \[88\]: df\_aligned, df2\_aligned \= df.align(df2, level\=0)

In \[89\]: df\_aligned
Out\[89\]: 
               0         1
one  y  1.519970 -0.493662
     x  0.600178  0.274230
zero y  0.132885 -0.023688
     x  2.410179  1.450520

In \[90\]: df2\_aligned
Out\[90\]: 
               0         1
one  y  1.060074 -0.109716
     x  1.060074 -0.109716
zero y  1.271532  0.713416
     x  1.271532  0.713416

Copy to clipboard

### Swapping levels with `swaplevel`[#](https://pandas.pydata.org/docs/user_guide/advanced.html#swapping-levels-with-swaplevel "Link to this heading")

The [`swaplevel()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.swaplevel.html#pandas.MultiIndex.swaplevel "pandas.MultiIndex.swaplevel")
 method can switch the order of two levels:

In \[91\]: df\[:5\]
Out\[91\]: 
               0         1
one  y  1.519970 -0.493662
     x  0.600178  0.274230
zero y  0.132885 -0.023688
     x  2.410179  1.450520

In \[92\]: df\[:5\].swaplevel(0, 1, axis\=0)
Out\[92\]: 
               0         1
y one   1.519970 -0.493662
x one   0.600178  0.274230
y zero  0.132885 -0.023688
x zero  2.410179  1.450520

Copy to clipboard

### Reordering levels with `reorder_levels`[#](https://pandas.pydata.org/docs/user_guide/advanced.html#reordering-levels-with-reorder-levels "Link to this heading")

The [`reorder_levels()`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.reorder_levels.html#pandas.MultiIndex.reorder_levels "pandas.MultiIndex.reorder_levels")
 method generalizes the `swaplevel` method, allowing you to permute the hierarchical index levels in one step:

In \[93\]: df\[:5\].reorder\_levels(\[1, 0\], axis\=0)
Out\[93\]: 
               0         1
y one   1.519970 -0.493662
x one   0.600178  0.274230
y zero  0.132885 -0.023688
x zero  2.410179  1.450520

Copy to clipboard

### Renaming names of an `Index` or `MultiIndex`[#](https://pandas.pydata.org/docs/user_guide/advanced.html#renaming-names-of-an-index-or-multiindex "Link to this heading")

The [`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename "pandas.DataFrame.rename")
 method is used to rename the labels of a `MultiIndex`, and is typically used to rename the columns of a `DataFrame`. The `columns` argument of `rename` allows a dictionary to be specified that includes only the columns you wish to rename.

In \[94\]: df.rename(columns\={0: "col0", 1: "col1"})
Out\[94\]: 
            col0      col1
one  y  1.519970 -0.493662
     x  0.600178  0.274230
zero y  0.132885 -0.023688
     x  2.410179  1.450520

Copy to clipboard

This method can also be used to rename specific labels of the main index of the `DataFrame`.

In \[95\]: df.rename(index\={"one": "two", "y": "z"})
Out\[95\]: 
               0         1
two  z  1.519970 -0.493662
     x  0.600178  0.274230
zero z  0.132885 -0.023688
     x  2.410179  1.450520

Copy to clipboard

The [`rename_axis()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html#pandas.DataFrame.rename_axis "pandas.DataFrame.rename_axis")
 method is used to rename the name of a `Index` or `MultiIndex`. In particular, the names of the levels of a `MultiIndex` can be specified, which is useful if `reset_index()` is later used to move the values from the `MultiIndex` to a column.

In \[96\]: df.rename\_axis(index\=\["abc", "def"\])
Out\[96\]: 
                 0         1
abc  def                    
one  y    1.519970 -0.493662
     x    0.600178  0.274230
zero y    0.132885 -0.023688
     x    2.410179  1.450520

Copy to clipboard

Note that the columns of a `DataFrame` are an index, so that using `rename_axis` with the `columns` argument will change the name of that index.

In \[97\]: df.rename\_axis(columns\="Cols").columns
Out\[97\]: RangeIndex(start=0, stop=2, step=1, name='Cols')

Copy to clipboard

Both `rename` and `rename_axis` support specifying a dictionary, `Series` or a mapping function to map labels/names to new values.

When working with an `Index` object directly, rather than via a `DataFrame`, [`Index.set_names()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.set_names.html#pandas.Index.set_names "pandas.Index.set_names")
 can be used to change the names.

In \[98\]: mi \= pd.MultiIndex.from\_product(\[\[1, 2\], \["a", "b"\]\], names\=\["x", "y"\])

In \[99\]: mi.names
Out\[99\]: FrozenList(\['x', 'y'\])

In \[100\]: mi2 \= mi.rename("new name", level\=0)

In \[101\]: mi2
Out\[101\]: 
MultiIndex(\[(1, 'a'),\
            (1, 'b'),\
            (2, 'a'),\
            (2, 'b')\],
           names=\['new name', 'y'\])

Copy to clipboard

You cannot set the names of the MultiIndex via a level.

In \[102\]: mi.levels\[0\].name \= "name via level"
\---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)
Cell In\[102\], line 1
\----> 1 mi.levels\[0\].name \= "name via level"

File ~/work/pandas/pandas/pandas/core/indexes/base.py:1869, in Index.name(self, value)
   1865 @name.setter
   1866 def name(self, value: Hashable) \-> None:
   1867     if self.\_no\_setting\_name:
   1868         \# Used in MultiIndex.levels to avoid silently ignoring name updates.
\-> 1869         raise RuntimeError(
   1870             "Cannot set name on a level of a MultiIndex. Use "
   1871             "'MultiIndex.set\_names' instead."
   1872         )
   1873     maybe\_extract\_name(value, None, type(self))
   1874     self.\_name \= value

RuntimeError: Cannot set name on a level of a MultiIndex. Use 'MultiIndex.set\_names' instead.

Copy to clipboard

Use [`Index.set_names()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.set_names.html#pandas.Index.set_names "pandas.Index.set_names")
 instead.

Sorting a `MultiIndex`[#](https://pandas.pydata.org/docs/user_guide/advanced.html#sorting-a-multiindex "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

For [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")
\-ed objects to be indexed and sliced effectively, they need to be sorted. As with any index, you can use [`sort_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "pandas.DataFrame.sort_index")
.

In \[103\]: import random

In \[104\]: random.shuffle(tuples)

In \[105\]: s \= pd.Series(np.random.randn(8), index\=pd.MultiIndex.from\_tuples(tuples))

In \[106\]: s
Out\[106\]: 
qux  one    0.206053
baz  two   -0.251905
qux  two   -2.213588
foo  one    1.063327
     two    1.266143
baz  one    0.299368
bar  one   -0.863838
     two    0.408204
dtype: float64

In \[107\]: s.sort\_index()
Out\[107\]: 
bar  one   -0.863838
     two    0.408204
baz  one    0.299368
     two   -0.251905
foo  one    1.063327
     two    1.266143
qux  one    0.206053
     two   -2.213588
dtype: float64

In \[108\]: s.sort\_index(level\=0)
Out\[108\]: 
bar  one   -0.863838
     two    0.408204
baz  one    0.299368
     two   -0.251905
foo  one    1.063327
     two    1.266143
qux  one    0.206053
     two   -2.213588
dtype: float64

In \[109\]: s.sort\_index(level\=1)
Out\[109\]: 
bar  one   -0.863838
baz  one    0.299368
foo  one    1.063327
qux  one    0.206053
bar  two    0.408204
baz  two   -0.251905
foo  two    1.266143
qux  two   -2.213588
dtype: float64

Copy to clipboard

You may also pass a level name to `sort_index` if the `MultiIndex` levels are named.

In \[110\]: s.index \= s.index.set\_names(\["L1", "L2"\])

In \[111\]: s.sort\_index(level\="L1")
Out\[111\]: 
L1   L2 
bar  one   -0.863838
     two    0.408204
baz  one    0.299368
     two   -0.251905
foo  one    1.063327
     two    1.266143
qux  one    0.206053
     two   -2.213588
dtype: float64

In \[112\]: s.sort\_index(level\="L2")
Out\[112\]: 
L1   L2 
bar  one   -0.863838
baz  one    0.299368
foo  one    1.063327
qux  one    0.206053
bar  two    0.408204
baz  two   -0.251905
foo  two    1.266143
qux  two   -2.213588
dtype: float64

Copy to clipboard

On higher dimensional objects, you can sort any of the other axes by level if they have a `MultiIndex`:

In \[113\]: df.T.sort\_index(level\=1, axis\=1)
Out\[113\]: 
        one      zero       one      zero
          x         x         y         y
0  0.600178  2.410179  1.519970  0.132885
1  0.274230  1.450520 -0.493662 -0.023688

Copy to clipboard

Indexing will work even if the data are not sorted, but will be rather inefficient (and show a `PerformanceWarning`). It will also return a copy of the data rather than a view:

In \[114\]: dfm \= pd.DataFrame(
   .....:    {"jim": \[0, 0, 1, 1\], "joe": \["x", "x", "z", "y"\], "jolie": np.random.rand(4)}
   .....: )
   .....: 

In \[115\]: dfm \= dfm.set\_index(\["jim", "joe"\])

In \[116\]: dfm
Out\[116\]: 
            jolie
jim joe          
0   x    0.490671
    x    0.120248
1   z    0.537020
    y    0.110968

In \[117\]: dfm.loc\[(1, 'z')\]
Out\[117\]: 
jolie    0.53702
Name: (1, z), dtype: float64

Copy to clipboard

Furthermore, if you try to index something that is not fully lexsorted, this can raise:

In \[118\]: dfm.loc\[(0, 'y'):(1, 'z')\]
\---------------------------------------------------------------------------
UnsortedIndexError                        Traceback (most recent call last)
Cell In\[118\], line 1
\----> 1 dfm.loc\[(0, 'y'):(1, 'z')\]

File ~/work/pandas/pandas/pandas/core/indexing.py:1342, in \_LocationIndexer.\_\_getitem\_\_(self, key)
   1340 maybe\_callable \= com.apply\_if\_callable(key, self.obj)
   1341 maybe\_callable \= self.\_raise\_callable\_usage(key, maybe\_callable)
\-> 1342 return self.\_getitem\_axis(maybe\_callable, axis\=axis)

File ~/work/pandas/pandas/pandas/core/indexing.py:1914, in \_LocIndexer.\_getitem\_axis(self, key, axis)
   1912 if isinstance(key, slice):
   1913     self.\_validate\_key(key, axis)
\-> 1914     return self.\_get\_slice\_axis(key, axis\=axis)
   1915 elif com.is\_bool\_indexer(key):
   1916     return self.\_getbool\_axis(key, axis\=axis)

File ~/work/pandas/pandas/pandas/core/indexing.py:1978, in \_LocIndexer.\_get\_slice\_axis(self, slice\_obj, axis)
   1975     return obj.copy(deep\=False)
   1977 labels \= obj.\_get\_axis(axis)
\-> 1978 indexer \= labels.slice\_indexer(slice\_obj.start, slice\_obj.stop, slice\_obj.step)
   1980 if isinstance(indexer, slice):
   1981     return self.obj.\_slice(indexer, axis\=axis)

File ~/work/pandas/pandas/pandas/core/indexes/base.py:7136, in Index.slice\_indexer(self, start, end, step)
   7085 def slice\_indexer(
   7086     self,
   7087     start: Hashable | None \= None,
   7088     end: Hashable | None \= None,
   7089     step: int | None \= None,
   7090 ) \-> slice:
   7091     """
   7092     Compute the slice indexer for input labels and step.
   7093 
   (...)   7134     slice(1, 3, None)
   7135     """
\-> 7136     start\_slice, end\_slice \= self.slice\_locs(start, end, step\=step)
   7138     \# return a slice
   7139     if not is\_scalar(start\_slice):

File ~/work/pandas/pandas/pandas/core/indexes/multi.py:3547, in MultiIndex.slice\_locs(self, start, end, step)
   3494 """
   3495 For an ordered MultiIndex, compute the slice locations for input
   3496 labels.
   (...)   3543                       sequence of such.
   3544 """
   3545 \# This function adds nothing to its parent implementation (the magic
   3546 \# happens in get\_slice\_bound method), but it adds meaningful doc.
\-> 3547 return super().slice\_locs(start, end, step)

File ~/work/pandas/pandas/pandas/core/indexes/base.py:7413, in Index.slice\_locs(self, start, end, step)
   7411 start\_slice \= None
   7412 if start is not None:
\-> 7413     start\_slice \= self.get\_slice\_bound(start, "left")
   7414 if start\_slice is None:
   7415     start\_slice \= 0

File ~/work/pandas/pandas/pandas/core/indexes/multi.py:3489, in MultiIndex.get\_slice\_bound(self, label, side)
   3487 if not isinstance(label, tuple):
   3488     label \= (label,)
\-> 3489 result \= self.\_partial\_tup\_index(label, side\=side)
   3490 result \= maybe\_unbox\_numpy\_scalar(result)
   3491 return result

File ~/work/pandas/pandas/pandas/core/indexes/multi.py:3555, in MultiIndex.\_partial\_tup\_index(self, tup, side)
   3553     \_raise\_key\_length\_error(len(tup), self.nlevels)
   3554 if len(tup) \> self.\_lexsort\_depth:
\-> 3555     raise UnsortedIndexError(
   3556         f"Key length ({len(tup)}) was greater than MultiIndex lexsort depth "
   3557         f"({self.\_lexsort\_depth})"
   3558     )
   3560 n \= len(tup)
   3561 start, end \= 0, len(self)

UnsortedIndexError: 'Key length (2) was greater than MultiIndex lexsort depth (1)'

Copy to clipboard

The `is_monotonic_increasing()` method on a `MultiIndex` shows if the index is sorted:

In \[119\]: dfm.index.is\_monotonic\_increasing
Out\[119\]: False

Copy to clipboard

In \[120\]: dfm \= dfm.sort\_index()

In \[121\]: dfm
Out\[121\]: 
            jolie
jim joe          
0   x    0.490671
    x    0.120248
1   y    0.110968
    z    0.537020

In \[122\]: dfm.index.is\_monotonic\_increasing
Out\[122\]: True

Copy to clipboard

And now selection works as expected.

In \[123\]: dfm.loc\[(0, "y"):(1, "z")\]
Out\[123\]: 
            jolie
jim joe          
1   y    0.110968
    z    0.537020

Copy to clipboard

Take methods[#](https://pandas.pydata.org/docs/user_guide/advanced.html#take-methods "Link to this heading")

-------------------------------------------------------------------------------------------------------------

Similar to NumPy ndarrays, pandas `Index`, `Series`, and `DataFrame` also provides the [`take()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.take.html#pandas.DataFrame.take "pandas.DataFrame.take")
 method that retrieves elements along a given axis at the given indices. The given indices must be either a list or an ndarray of integer index positions. `take` will also accept negative integers as relative positions to the end of the object.

In \[124\]: index \= pd.Index(np.random.randint(0, 1000, 10))

In \[125\]: index
Out\[125\]: Index(\[214, 502, 712, 567, 786, 175, 993, 133, 758, 329\], dtype='int64')

In \[126\]: positions \= \[0, 9, 3\]

In \[127\]: index\[positions\]
Out\[127\]: Index(\[214, 329, 567\], dtype='int64')

In \[128\]: index.take(positions)
Out\[128\]: Index(\[214, 329, 567\], dtype='int64')

In \[129\]: ser \= pd.Series(np.random.randn(10))

In \[130\]: ser.iloc\[positions\]
Out\[130\]: 
0   -0.179666
9    1.824375
3    0.392149
dtype: float64

In \[131\]: ser.take(positions)
Out\[131\]: 
0   -0.179666
9    1.824375
3    0.392149
dtype: float64

Copy to clipboard

For DataFrames, the given indices should be a 1d list or ndarray that specifies row or column positions.

In \[132\]: frm \= pd.DataFrame(np.random.randn(5, 3))

In \[133\]: frm.take(\[1, 4, 3\])
Out\[133\]: 
          0         1         2
1 -1.237881  0.106854 -1.276829
4  0.629675 -1.425966  1.857704
3  0.979542 -1.633678  0.615855

In \[134\]: frm.take(\[0, 2\], axis\=1)
Out\[134\]: 
          0         2
0  0.595974  0.601544
1 -1.237881 -1.276829
2 -0.767101  1.499591
3  0.979542  0.615855
4  0.629675  1.857704

Copy to clipboard

It is important to note that the `take` method on pandas objects are not intended to work on boolean indices and may return unexpected results.

In \[135\]: arr \= np.random.randn(10)

In \[136\]: arr.take(\[False, False, True, True\])
Out\[136\]: array(\[-1.1935, -1.1935,  0.6775,  0.6775\])

In \[137\]: arr\[\[0, 1\]\]
Out\[137\]: array(\[-1.1935,  0.6775\])

In \[138\]: ser \= pd.Series(np.random.randn(10))

In \[139\]: ser.take(\[False, False, True, True\])
Out\[139\]: 
0    0.233141
0    0.233141
1   -0.223540
1   -0.223540
dtype: float64

In \[140\]: ser.iloc\[\[0, 1\]\]
Out\[140\]: 
0    0.233141
1   -0.223540
dtype: float64

Copy to clipboard

Finally, as a small note on performance, because the `take` method handles a narrower range of inputs, it can offer performance that is a good deal faster than fancy indexing.

In \[141\]: arr \= np.random.randn(10000, 5)

In \[142\]: indexer \= np.arange(10000)

In \[143\]: random.shuffle(indexer)

In \[144\]: %timeit arr\[indexer\]
   .....: %timeit arr.take(indexer, axis=0)
   .....: 
269 us +- 9.95 us per loop (mean +- std. dev. of 7 runs, 1,000 loops each)
62 us +- 2.42 us per loop (mean +- std. dev. of 7 runs, 10,000 loops each)

Copy to clipboard

In \[145\]: ser \= pd.Series(arr\[:, 0\])

In \[146\]: %timeit ser.iloc\[indexer\]
   .....: %timeit ser.take(indexer)
   .....: 
118 us +- 9.18 us per loop (mean +- std. dev. of 7 runs, 10,000 loops each)
110 us +- 3.55 us per loop (mean +- std. dev. of 7 runs, 10,000 loops each)

Copy to clipboard

Index types[#](https://pandas.pydata.org/docs/user_guide/advanced.html#index-types "Link to this heading")

-----------------------------------------------------------------------------------------------------------

We have discussed `MultiIndex` in the previous sections pretty extensively. Documentation about `DatetimeIndex` and `PeriodIndex` are shown [here](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-overview)
, and documentation about `TimedeltaIndex` is found [here](https://pandas.pydata.org/docs/user_guide/timedeltas.html#timedeltas-index)
.

In the following sub-sections we will highlight some other index types.

### CategoricalIndex[#](https://pandas.pydata.org/docs/user_guide/advanced.html#categoricalindex "Link to this heading")

[`CategoricalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.CategoricalIndex.html#pandas.CategoricalIndex "pandas.CategoricalIndex")
 is a type of index that is useful for supporting indexing with duplicates. This is a container around a [`Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
 and allows efficient indexing and storage of an index with a large number of duplicated elements.

In \[147\]: from pandas.api.types import CategoricalDtype

In \[148\]: df \= pd.DataFrame({"A": np.arange(6), "B": list("aabbca")})

In \[149\]: df\["B"\] \= df\["B"\].astype(CategoricalDtype(list("cab")))

In \[150\]: df
Out\[150\]: 
   A  B
0  0  a
1  1  a
2  2  b
3  3  b
4  4  c
5  5  a

In \[151\]: df.dtypes
Out\[151\]: 
A       int64
B    category
dtype: object

In \[152\]: df\["B"\].cat.categories
Out\[152\]: Index(\['c', 'a', 'b'\], dtype='str')

Copy to clipboard

Setting the index will create a `CategoricalIndex`.

In \[153\]: df2 \= df.set\_index("B")

In \[154\]: df2.index
Out\[154\]: 
CategoricalIndex(\['a', 'a', 'b', 'b', 'c', 'a'\], categories=\['c', 'a', 'b'\],
                 ordered=False, dtype='category', name='B')

Copy to clipboard

Indexing with `__getitem__/.iloc/.loc` works similarly to an `Index` with duplicates. The indexers **must** be in the category or the operation will raise a `KeyError`.

In \[155\]: df2.loc\["a"\]
Out\[155\]: 
   A
B   
a  0
a  1
a  5

Copy to clipboard

The `CategoricalIndex` is **preserved** after indexing:

In \[156\]: df2.loc\["a"\].index
Out\[156\]: 
CategoricalIndex(\['a', 'a', 'a'\], categories=\['c', 'a', 'b'\], ordered=False,
                 dtype='category', name='B')

Copy to clipboard

Sorting the index will sort by the order of the categories (recall that we created the index with `CategoricalDtype(list('cab'))`, so the sorted order is `cab`).

In \[157\]: df2.sort\_index()
Out\[157\]: 
   A
B   
c  4
a  0
a  1
a  5
b  2
b  3

Copy to clipboard

Groupby operations on the index will preserve the index nature as well.

In \[158\]: df2.groupby(level\=0, observed\=True).sum()
Out\[158\]: 
   A
B   
c  4
a  6
b  5

In \[159\]: df2.groupby(level\=0, observed\=True).sum().index
Out\[159\]: 
CategoricalIndex(\['c', 'a', 'b'\], categories=\['c', 'a', 'b'\], ordered=False,
                 dtype='category', name='B')

Copy to clipboard

Reindexing operations will return a resulting index based on the type of the passed indexer. Passing a list will return a plain-old `Index`; indexing with a `Categorical` will return a `CategoricalIndex`, indexed according to the categories of the **passed** `Categorical` dtype. This allows one to arbitrarily index these even with values **not** in the categories, similarly to how you can reindex **any** pandas index.

In \[160\]: df3 \= pd.DataFrame(
   .....:    {"A": np.arange(3), "B": pd.Series(list("abc")).astype("category")}
   .....: )
   .....: 

In \[161\]: df3 \= df3.set\_index("B")

In \[162\]: df3
Out\[162\]: 
   A
B   
a  0
b  1
c  2

Copy to clipboard

In \[163\]: df3.reindex(\["a", "e"\])
Out\[163\]: 
     A
B     
a  0.0
e  NaN

In \[164\]: df3.reindex(\["a", "e"\]).index
Out\[164\]: Index(\['a', 'e'\], dtype='str', name='B')

In \[165\]: df3.reindex(pd.Categorical(\["a", "e"\], categories\=list("abe")))
Out\[165\]: 
     A
B     
a  0.0
e  NaN

In \[166\]: df3.reindex(pd.Categorical(\["a", "e"\], categories\=list("abe"))).index
Out\[166\]: 
CategoricalIndex(\['a', 'e'\], categories=\['a', 'b', 'e'\], ordered=False,
                 dtype='category', name='B')

Copy to clipboard

Warning

Reshaping and Comparison operations on a `CategoricalIndex` must have the same categories or a `TypeError` will be raised.

In \[167\]: df4 \= pd.DataFrame({"A": np.arange(2), "B": list("ba")})

In \[168\]: df4\["B"\] \= df4\["B"\].astype(CategoricalDtype(list("ab")))

In \[169\]: df4 \= df4.set\_index("B")

In \[170\]: df4.index
Out\[170\]: 
CategoricalIndex(\['b', 'a'\], categories=\['a', 'b'\], ordered=False,
                 dtype='category', name='B')

In \[171\]: df5 \= pd.DataFrame({"A": np.arange(2), "B": list("bc")})

In \[172\]: df5\["B"\] \= df5\["B"\].astype(CategoricalDtype(list("bc")))

In \[173\]: df5 \= df5.set\_index("B")

In \[174\]: df5.index
Out\[174\]: 
CategoricalIndex(\['b', 'c'\], categories=\['b', 'c'\], ordered=False,
                 dtype='category', name='B')

Copy to clipboard

In \[175\]: pd.concat(\[df4, df5\])
Out\[175\]: 
   A
B   
b  0
a  1
b  0
c  1

Copy to clipboard

### RangeIndex[#](https://pandas.pydata.org/docs/user_guide/advanced.html#rangeindex "Link to this heading")

[`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")
 is a sub-class of [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 that provides the default index for all [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 and [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 objects. `RangeIndex` is an optimized version of `Index` that can represent a monotonic ordered set. These are analogous to Python [range types](https://docs.python.org/3/library/stdtypes.html#typesseq-range)
. A `RangeIndex` will always have an `int64` dtype.

In \[176\]: idx \= pd.RangeIndex(5)

In \[177\]: idx
Out\[177\]: RangeIndex(start=0, stop=5, step=1)

Copy to clipboard

`RangeIndex` is the default index for all [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 and [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 objects:

In \[178\]: ser \= pd.Series(\[1, 2, 3\])

In \[179\]: ser.index
Out\[179\]: RangeIndex(start=0, stop=3, step=1)

In \[180\]: df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\])

In \[181\]: df.index
Out\[181\]: RangeIndex(start=0, stop=2, step=1)

In \[182\]: df.columns
Out\[182\]: RangeIndex(start=0, stop=2, step=1)

Copy to clipboard

A `RangeIndex` will behave similarly to a [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 with an `int64` dtype and operations on a `RangeIndex`, whose result cannot be represented by a `RangeIndex`, but should have an integer dtype, will be converted to an `Index` with `int64`. For example:

In \[183\]: idx\[\[0, 2\]\]
Out\[183\]: RangeIndex(start=0, stop=4, step=2)

Copy to clipboard

### Intervals[#](https://pandas.pydata.org/docs/user_guide/advanced.html#intervals "Link to this heading")

[`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")
 represents a single interval, while a collection of intervals can be held in an [`IntervalIndex`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.html#pandas.IntervalIndex "pandas.IntervalIndex")
 (with corresponding dtype `IntervalDtype`). Together these provide first-class support for interval notation in pandas. The `IntervalIndex` allows some unique indexing and is also used as a return type for the categories in [`cut()`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")
 and [`qcut()`](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html#pandas.qcut "pandas.qcut")
.

#### The `Interval` scalar[#](https://pandas.pydata.org/docs/user_guide/advanced.html#the-interval-scalar "Link to this heading")

An [`Interval`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.html#pandas.Interval "pandas.Interval")
 is constructed from a left and a right endpoint:

In \[184\]: iv \= pd.Interval(0, 5)

In \[185\]: iv
Out\[185\]: Interval(0, 5, closed='right')

Copy to clipboard

By default, an `Interval` is closed on the right. The `closed` argument controls which side(s) are inclusive — `"right"`, `"left"`, `"both"`, or `"neither"`:

In \[186\]: pd.Interval(0, 5, closed\="left")
Out\[186\]: Interval(0, 5, closed='left')

In \[187\]: pd.Interval(0, 5, closed\="both")
Out\[187\]: Interval(0, 5, closed='both')

In \[188\]: pd.Interval(0, 5, closed\="neither")
Out\[188\]: Interval(0, 5, closed='neither')

Copy to clipboard

The endpoints and derived quantities are accessible as attributes:

In \[189\]: iv.left, iv.right
Out\[189\]: (0, 5)

In \[190\]: iv.mid
Out\[190\]: 2.5

In \[191\]: iv.length
Out\[191\]: 5

Copy to clipboard

Membership is tested with `in`. Inclusion respects the `closed` setting, so an endpoint is only contained when its side is closed:

In \[192\]: 2.5 in iv
Out\[192\]: True

In \[193\]: 0 in iv
Out\[193\]: False

In \[194\]: 5 in iv
Out\[194\]: True

In \[195\]: 0 in pd.Interval(0, 5, closed\="left")
Out\[195\]: True

Copy to clipboard

Two intervals can be compared with [`Interval.overlaps()`](https://pandas.pydata.org/docs/reference/api/pandas.Interval.overlaps.html#pandas.Interval.overlaps "pandas.Interval.overlaps")
. Intervals that share only an open endpoint do not overlap:

In \[196\]: iv.overlaps(pd.Interval(3, 8))
Out\[196\]: True

In \[197\]: iv.overlaps(pd.Interval(5, 10))
Out\[197\]: False

In \[198\]: iv.overlaps(pd.Interval(5, 10, closed\="both"))
Out\[198\]: True

Copy to clipboard

Endpoints may also be [`Timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Timestamp.html#pandas.Timestamp "pandas.Timestamp")
 or [`Timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Timedelta.html#pandas.Timedelta "pandas.Timedelta")
 values, which makes `Interval` useful for representing time ranges:

In \[199\]: pd.Interval(pd.Timestamp("2017-01-01"), pd.Timestamp("2017-01-08"))
Out\[199\]: Interval(2017-01-01 00:00:00, 2017-01-08 00:00:00, closed='right')

Copy to clipboard

#### Indexing with an `IntervalIndex`[#](https://pandas.pydata.org/docs/user_guide/advanced.html#indexing-with-an-intervalindex "Link to this heading")

An `IntervalIndex` can be used in `Series` and in `DataFrame` as the index.

In \[200\]: df \= pd.DataFrame(
   .....:    {"A": \[1, 2, 3, 4\]}, index\=pd.IntervalIndex.from\_breaks(\[0, 1, 2, 3, 4\])
   .....: )
   .....: 

In \[201\]: df
Out\[201\]: 
        A
(0, 1\]  1
(1, 2\]  2
(2, 3\]  3
(3, 4\]  4

Copy to clipboard

Label based indexing via `.loc` along the edges of an interval works as you would expect, selecting that particular interval.

In \[202\]: df.loc\[2\]
Out\[202\]: 
A    2
Name: (1, 2\], dtype: int64

In \[203\]: df.loc\[\[2, 3\]\]
Out\[203\]: 
        A
(1, 2\]  2
(2, 3\]  3

Copy to clipboard

If you select a label _contained_ within an interval, this will also select the interval.

In \[204\]: df.loc\[2.5\]
Out\[204\]: 
A    3
Name: (2, 3\], dtype: int64

In \[205\]: df.loc\[\[2.5, 3.5\]\]
Out\[205\]: 
        A
(2, 3\]  3
(3, 4\]  4

Copy to clipboard

Selecting using an `Interval` will only return exact matches.

In \[206\]: df.loc\[pd.Interval(1, 2)\]
Out\[206\]: 
A    2
Name: (1, 2\], dtype: int64

Copy to clipboard

Trying to select an `Interval` that is not exactly contained in the `IntervalIndex` will raise a `KeyError`.

In \[207\]: df.loc\[pd.Interval(0.5, 2.5)\]
\---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In\[207\], line 1
\----> 1 df.loc\[pd.Interval(0.5, 2.5)\]

File ~/work/pandas/pandas/pandas/core/indexing.py:1342, in \_LocationIndexer.\_\_getitem\_\_(self, key)
   1340 maybe\_callable \= com.apply\_if\_callable(key, self.obj)
   1341 maybe\_callable \= self.\_raise\_callable\_usage(key, maybe\_callable)
\-> 1342 return self.\_getitem\_axis(maybe\_callable, axis\=axis)

File ~/work/pandas/pandas/pandas/core/indexing.py:1966, in \_LocIndexer.\_getitem\_axis(self, key, axis)
   1964 \# fall thru to straight lookup
   1965 self.\_validate\_key(key, axis)
\-> 1966 return self.\_get\_label(key, axis\=axis)

File ~/work/pandas/pandas/pandas/core/indexing.py:1884, in \_LocIndexer.\_get\_label(self, label, axis)
   1882 def \_get\_label(self, label, axis: AxisInt):
   1883     \# GH#5567 this will fail if the label is not present in the axis.
\-> 1884     return self.obj.xs(label, axis\=axis)

File ~/work/pandas/pandas/pandas/core/generic.py:4291, in NDFrame.xs(self, key, axis, level, drop\_level)
   4287                     new\_index \= index\[loc : loc + 1\]
   4288                 else:
   4289                     new\_index \= index\[loc\]
   4290         else:
\-> 4291             loc \= index.get\_loc(key)
   4292 
   4293             if isinstance(loc, np.ndarray):
   4294                 if loc.dtype \== np.bool\_:

File ~/work/pandas/pandas/pandas/core/indexes/interval.py:1170, in IntervalIndex.get\_loc(self, key)
   1168 matches \= mask.sum()
   1169 if matches \== 0:
\-> 1170     raise KeyError(key)
   1171 if matches \== 1:
   1172     return maybe\_unbox\_numpy\_scalar(mask.argmax())

KeyError: Interval(0.5, 2.5, closed='right')

Copy to clipboard

Selecting all `Intervals` that overlap a given `Interval` can be performed using the [`overlaps()`](https://pandas.pydata.org/docs/reference/api/pandas.IntervalIndex.overlaps.html#pandas.IntervalIndex.overlaps "pandas.IntervalIndex.overlaps")
 method to create a boolean indexer.

In \[208\]: idxr \= df.index.overlaps(pd.Interval(0.5, 2.5))

In \[209\]: idxr
Out\[209\]: array(\[ True,  True,  True, False\])

In \[210\]: df\[idxr\]
Out\[210\]: 
        A
(0, 1\]  1
(1, 2\]  2
(2, 3\]  3

Copy to clipboard

#### Binning data with `cut` and `qcut`[#](https://pandas.pydata.org/docs/user_guide/advanced.html#binning-data-with-cut-and-qcut "Link to this heading")

[`cut()`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")
 and [`qcut()`](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html#pandas.qcut "pandas.qcut")
 both return a `Categorical` object, and the bins they create are stored as an `IntervalIndex` in its `.categories` attribute.

In \[211\]: c \= pd.cut(range(4), bins\=2)

In \[212\]: c
Out\[212\]: 
\[(-0.003, 1.5\], (-0.003, 1.5\], (1.5, 3.0\], (1.5, 3.0\]\]
Categories (2, interval\[float64, right\]): \[(-0.003, 1.5\] < (1.5, 3.0\]\]

In \[213\]: c.categories
Out\[213\]: IntervalIndex(\[(-0.003, 1.5\], (1.5, 3.0\]\], dtype='interval\[float64, right\]')

Copy to clipboard

[`cut()`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")
 also accepts an `IntervalIndex` for its `bins` argument, which enables a useful pandas idiom. First, We call [`cut()`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")
 with some data and `bins` set to a fixed number, to generate the bins. Then, we pass the values of `.categories` as the `bins` argument in subsequent calls to [`cut()`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")
, supplying new data which will be binned into the same bins.

In \[214\]: pd.cut(\[0, 3, 5, 1\], bins\=c.categories)
Out\[214\]: 
\[(-0.003, 1.5\], (1.5, 3.0\], NaN, (-0.003, 1.5\]\]
Categories (2, interval\[float64, right\]): \[(-0.003, 1.5\] < (1.5, 3.0\]\]

Copy to clipboard

Any value which falls outside all bins will be assigned a `NaN` value.

#### Generating ranges of intervals[#](https://pandas.pydata.org/docs/user_guide/advanced.html#generating-ranges-of-intervals "Link to this heading")

If we need intervals on a regular frequency, we can use the [`interval_range()`](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#pandas.interval_range "pandas.interval_range")
 function to create an `IntervalIndex` using various combinations of `start`, `end`, and `periods`. The default frequency for `interval_range` is a 1 for numeric intervals, and calendar day for datetime-like intervals:

In \[215\]: pd.interval\_range(start\=0, end\=5)
Out\[215\]: 
IntervalIndex(\[(0, 1\], (1, 2\], (2, 3\], (3, 4\], (4, 5\]\],
              dtype='interval\[int64, right\]')

In \[216\]: pd.interval\_range(start\=pd.Timestamp("2017-01-01"), periods\=4)
Out\[216\]: 
IntervalIndex(\[(2017-01-01 00:00:00, 2017-01-02 00:00:00\],
               (2017-01-02 00:00:00, 2017-01-03 00:00:00\],
               (2017-01-03 00:00:00, 2017-01-04 00:00:00\],
               (2017-01-04 00:00:00, 2017-01-05 00:00:00\]\],
              dtype='interval\[datetime64\[us\], right\]')

In \[217\]: pd.interval\_range(end\=pd.Timedelta("3 days"), periods\=3)
Out\[217\]: 
IntervalIndex(\[(0 days 00:00:00, 1 days 00:00:00\],
               (1 days 00:00:00, 2 days 00:00:00\],
               (2 days 00:00:00, 3 days 00:00:00\]\],
              dtype='interval\[timedelta64\[us\], right\]')

Copy to clipboard

The `freq` parameter can used to specify non-default frequencies, and can utilize a variety of [frequency aliases](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries-offset-aliases)
 with datetime-like intervals:

In \[218\]: pd.interval\_range(start\=0, periods\=5, freq\=1.5)
Out\[218\]: 
IntervalIndex(\[(0.0, 1.5\], (1.5, 3.0\], (3.0, 4.5\], (4.5, 6.0\], (6.0, 7.5\]\],
              dtype='interval\[float64, right\]')

In \[219\]: pd.interval\_range(start\=pd.Timestamp("2017-01-01"), periods\=4, freq\="W")
Out\[219\]: 
IntervalIndex(\[(2017-01-01 00:00:00, 2017-01-08 00:00:00\],
               (2017-01-08 00:00:00, 2017-01-15 00:00:00\],
               (2017-01-15 00:00:00, 2017-01-22 00:00:00\],
               (2017-01-22 00:00:00, 2017-01-29 00:00:00\]\],
              dtype='interval\[datetime64\[us\], right\]')

In \[220\]: pd.interval\_range(start\=pd.Timedelta("0 days"), periods\=3, freq\="9h")
Out\[220\]: 
IntervalIndex(\[(0 days 00:00:00, 0 days 09:00:00\],
               (0 days 09:00:00, 0 days 18:00:00\],
               (0 days 18:00:00, 1 days 03:00:00\]\],
              dtype='interval\[timedelta64\[us\], right\]')

Copy to clipboard

Additionally, the `closed` parameter can be used to specify which side(s) the intervals are closed on. Intervals are closed on the right side by default.

In \[221\]: pd.interval\_range(start\=0, end\=4, closed\="both")
Out\[221\]: IntervalIndex(\[\[0, 1\], \[1, 2\], \[2, 3\], \[3, 4\]\], dtype='interval\[int64, both\]')

In \[222\]: pd.interval\_range(start\=0, end\=4, closed\="neither")
Out\[222\]: IntervalIndex(\[(0, 1), (1, 2), (2, 3), (3, 4)\], dtype='interval\[int64, neither\]')

Copy to clipboard

Specifying `start`, `end`, and `periods` will generate a range of evenly spaced intervals from `start` to `end` inclusively, with `periods` number of elements in the resulting `IntervalIndex`:

In \[223\]: pd.interval\_range(start\=0, end\=6, periods\=4)
Out\[223\]: 
IntervalIndex(\[(0.0, 1.5\], (1.5, 3.0\], (3.0, 4.5\], (4.5, 6.0\]\],
              dtype='interval\[float64, right\]')

In \[224\]: pd.interval\_range(pd.Timestamp("2018-01-01"), pd.Timestamp("2018-02-28"), periods\=3)
Out\[224\]: 
IntervalIndex(\[(2018-01-01 00:00:00, 2018-01-20 08:00:00\],
               (2018-01-20 08:00:00, 2018-02-08 16:00:00\],
               (2018-02-08 16:00:00, 2018-02-28 00:00:00\]\],
              dtype='interval\[datetime64\[us\], right\]')

Copy to clipboard

Miscellaneous indexing FAQ[#](https://pandas.pydata.org/docs/user_guide/advanced.html#miscellaneous-indexing-faq "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

### Integer indexing[#](https://pandas.pydata.org/docs/user_guide/advanced.html#integer-indexing "Link to this heading")

Label-based indexing with integer axis labels is a thorny topic. It has been discussed heavily on mailing lists and among various members of the scientific Python community. In pandas, our general viewpoint is that labels matter more than integer locations. Therefore, with an integer axis index _only_ label-based indexing is possible with the standard tools like `.loc`. The following code will generate exceptions:

In \[225\]: s \= pd.Series(range(5))

In \[226\]: s\[\-1\]
\---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
File ~/work/pandas/pandas/pandas/core/indexes/range.py:545, in RangeIndex.get\_loc(self, key)
    544 try:
\--> 545     return self.\_range.index(new\_key)
    546 except ValueError as err:

ValueError: -1 is not in range

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
Cell In\[226\], line 1
\----> 1 s\[\-1\]

File ~/work/pandas/pandas/pandas/core/series.py:1102, in Series.\_\_getitem\_\_(self, key)
   1098 
   1099         elif key\_is\_scalar:
   1100             \# Note: GH#50617 in 3.0 we changed int key to always be treated as
   1101             \#  a label, matching DataFrame behavior.
\-> 1102             return self.\_get\_value(key)
   1103 
   1104         \# Convert generator to list before going through hashable part
   1105         \# (We will iterate through the generator there to check for slices)

File ~/work/pandas/pandas/pandas/core/series.py:1189, in Series.\_get\_value(self, label, takeable)
   1185         if takeable:
   1186             return self.\_ixs(label)
   1187 
   1188         \# Similar to Index.get\_value, but we do not fall back to positional
\-> 1189         loc \= self.index.get\_loc(label)
   1190 
   1191         if is\_integer(loc):
   1192             return self.\_ixs(loc)

File ~/work/pandas/pandas/pandas/core/indexes/range.py:547, in RangeIndex.get\_loc(self, key)
    545         return self.\_range.index(new\_key)
    546     except ValueError as err:
\--> 547         raise KeyError(key) from err
    548 if isinstance(key, Hashable):
    549     raise KeyError(key)

KeyError: -1

In \[227\]: df \= pd.DataFrame(np.random.randn(5, 4))

In \[228\]: df
Out\[228\]: 
          0         1         2         3
0 -0.435772 -1.188928 -0.808286 -0.284634
1 -1.815703  1.347213 -0.243487  0.514704
2  1.162969 -0.287725 -0.179734  0.993962
3 -0.212673  0.909872 -0.733333 -0.349893
4  0.456434 -0.306735  0.553396  0.166221

In \[229\]: df.loc\[\-2:\]
Out\[229\]: 
          0         1         2         3
0 -0.435772 -1.188928 -0.808286 -0.284634
1 -1.815703  1.347213 -0.243487  0.514704
2  1.162969 -0.287725 -0.179734  0.993962
3 -0.212673  0.909872 -0.733333 -0.349893
4  0.456434 -0.306735  0.553396  0.166221

Copy to clipboard

This deliberate decision was made to prevent ambiguities and subtle bugs (many users reported finding bugs when the API change was made to stop “falling back” on position-based indexing).

### Non-monotonic indexes require exact matches[#](https://pandas.pydata.org/docs/user_guide/advanced.html#non-monotonic-indexes-require-exact-matches "Link to this heading")

If the index of a `Series` or `DataFrame` is monotonically increasing or decreasing, then the bounds of a label-based slice can be outside the range of the index, much like slice indexing a normal Python `list`. Monotonicity of an index can be tested with the [`is_monotonic_increasing()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_increasing.html#pandas.Index.is_monotonic_increasing "pandas.Index.is_monotonic_increasing")
 and [`is_monotonic_decreasing()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_monotonic_decreasing.html#pandas.Index.is_monotonic_decreasing "pandas.Index.is_monotonic_decreasing")
 attributes.

In \[230\]: df \= pd.DataFrame(index\=\[2, 3, 3, 4, 5\], columns\=\["data"\], data\=list(range(5)))

In \[231\]: df.index.is\_monotonic\_increasing
Out\[231\]: True

\# no rows 0 or 1, but still returns rows 2, 3 (both of them), and 4:
In \[232\]: df.loc\[0:4, :\]
Out\[232\]: 
   data
2     0
3     1
3     2
4     3

\# slice is are outside the index, so empty DataFrame is returned
In \[233\]: df.loc\[13:15, :\]
Out\[233\]: 
Empty DataFrame
Columns: \[data\]
Index: \[\]

Copy to clipboard

On the other hand, if the index is not monotonic, then both slice bounds must be _unique_ members of the index.

In \[234\]: df \= pd.DataFrame(index\=\[2, 3, 1, 4, 3, 5\], columns\=\["data"\], data\=list(range(6)))

In \[235\]: df.index.is\_monotonic\_increasing
Out\[235\]: False

\# OK because 2 and 4 are in the index
In \[236\]: df.loc\[2:4, :\]
Out\[236\]: 
   data
2     0
3     1
1     2
4     3

Copy to clipboard

 # 0 is not in the index
In \[237\]: df.loc\[0:4, :\]
\---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In\[237\], line 1
\----> 1 df.loc\[0:4, :\]

File ~/work/pandas/pandas/pandas/core/indexing.py:1335, in \_LocationIndexer.\_\_getitem\_\_(self, key)
   1333     if self.\_is\_scalar\_access(key):
   1334         return self.obj.\_get\_value(\*key, takeable\=self.\_takeable)
\-> 1335     return self.\_getitem\_tuple(key)
   1336 else:
   1337     \# we by definition only have the 0th axis
   1338     axis \= self.axis or 0

File ~/work/pandas/pandas/pandas/core/indexing.py:1871, in \_LocIndexer.\_getitem\_tuple(self, tup)
   1869 with suppress(IndexingError):
   1870     tup \= self.\_expand\_ellipsis(tup)
\-> 1871     return self.\_getitem\_lowerdim(tup)
   1873 \# no multi-index, so validate all of the indexers
   1874 tup \= self.\_validate\_tuple\_indexer(tup)

File ~/work/pandas/pandas/pandas/core/indexing.py:1228, in \_LocationIndexer.\_getitem\_lowerdim(self, tup)
   1220 for i, key in zip(range(len(tup) \- 1, \-1, \-1), reversed(tup), strict\=True):
   1221     if (
   1222         is\_label\_like(key)
   1223         or is\_list\_like(key)
   (...)   1226         \# We don't need to check for tuples here because those are
   1227         \#  caught by the \_is\_nested\_tuple\_indexer check above.
\-> 1228         section \= self.\_getitem\_axis(key, axis\=i)
   1230         \# We should never have a scalar section here, because
   1231         \#  \_getitem\_lowerdim is only called after a check for
   1232         \#  is\_scalar\_access, which that would be.
   1233         if section.ndim \== self.ndim:
   1234             \# we're in the middle of slicing through a MultiIndex
   1235             \# revise the key wrt to \`section\` by inserting an \_NS

File ~/work/pandas/pandas/pandas/core/indexing.py:1914, in \_LocIndexer.\_getitem\_axis(self, key, axis)
   1912 if isinstance(key, slice):
   1913     self.\_validate\_key(key, axis)
\-> 1914     return self.\_get\_slice\_axis(key, axis\=axis)
   1915 elif com.is\_bool\_indexer(key):
   1916     return self.\_getbool\_axis(key, axis\=axis)

File ~/work/pandas/pandas/pandas/core/indexing.py:1978, in \_LocIndexer.\_get\_slice\_axis(self, slice\_obj, axis)
   1975     return obj.copy(deep\=False)
   1977 labels \= obj.\_get\_axis(axis)
\-> 1978 indexer \= labels.slice\_indexer(slice\_obj.start, slice\_obj.stop, slice\_obj.step)
   1980 if isinstance(indexer, slice):
   1981     return self.obj.\_slice(indexer, axis\=axis)

File ~/work/pandas/pandas/pandas/core/indexes/base.py:7136, in Index.slice\_indexer(self, start, end, step)
   7085 def slice\_indexer(
   7086     self,
   7087     start: Hashable | None \= None,
   7088     end: Hashable | None \= None,
   7089     step: int | None \= None,
   7090 ) \-> slice:
   7091     """
   7092     Compute the slice indexer for input labels and step.
   7093 
   (...)   7134     slice(1, 3, None)
   7135     """
\-> 7136     start\_slice, end\_slice \= self.slice\_locs(start, end, step\=step)
   7138     \# return a slice
   7139     if not is\_scalar(start\_slice):

File ~/work/pandas/pandas/pandas/core/indexes/base.py:7413, in Index.slice\_locs(self, start, end, step)
   7411 start\_slice \= None
   7412 if start is not None:
\-> 7413     start\_slice \= self.get\_slice\_bound(start, "left")
   7414 if start\_slice is None:
   7415     start\_slice \= 0

File ~/work/pandas/pandas/pandas/core/indexes/base.py:7308, in Index.get\_slice\_bound(self, label, side)
   7306         return self.\_searchsorted\_monotonic(label, side)
   7307     except ValueError:
\-> 7308         raise KeyError(
   7309             f"Cannot get {side} slice bound for non-monotonic index "
   7310             f"with a missing label {original\_label!r}. "
   7311             "Either sort the index or specify an existing label."
   7312         ) from None
   7314 if isinstance(slc, np.ndarray):
   7315     \# get\_loc may return a boolean array, which
   7316     \# is OK as long as they are representable by a slice.
   7317     assert is\_bool\_dtype(slc.dtype)

KeyError: 'Cannot get left slice bound for non-monotonic index with a missing label 0. Either sort the index or specify an existing label.'

 \# 3 is not a unique label
In \[238\]: df.loc\[2:3, :\]
\---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
Cell In\[238\], line 1
\----> 1 df.loc\[2:3, :\]

File ~/work/pandas/pandas/pandas/core/indexing.py:1335, in \_LocationIndexer.\_\_getitem\_\_(self, key)
   1333     if self.\_is\_scalar\_access(key):
   1334         return self.obj.\_get\_value(\*key, takeable\=self.\_takeable)
\-> 1335     return self.\_getitem\_tuple(key)
   1336 else:
   1337     \# we by definition only have the 0th axis
   1338     axis \= self.axis or 0

File ~/work/pandas/pandas/pandas/core/indexing.py:1871, in \_LocIndexer.\_getitem\_tuple(self, tup)
   1869 with suppress(IndexingError):
   1870     tup \= self.\_expand\_ellipsis(tup)
\-> 1871     return self.\_getitem\_lowerdim(tup)
   1873 \# no multi-index, so validate all of the indexers
   1874 tup \= self.\_validate\_tuple\_indexer(tup)

File ~/work/pandas/pandas/pandas/core/indexing.py:1228, in \_LocationIndexer.\_getitem\_lowerdim(self, tup)
   1220 for i, key in zip(range(len(tup) \- 1, \-1, \-1), reversed(tup), strict\=True):
   1221     if (
   1222         is\_label\_like(key)
   1223         or is\_list\_like(key)
   (...)   1226         \# We don't need to check for tuples here because those are
   1227         \#  caught by the \_is\_nested\_tuple\_indexer check above.
\-> 1228         section \= self.\_getitem\_axis(key, axis\=i)
   1230         \# We should never have a scalar section here, because
   1231         \#  \_getitem\_lowerdim is only called after a check for
   1232         \#  is\_scalar\_access, which that would be.
   1233         if section.ndim \== self.ndim:
   1234             \# we're in the middle of slicing through a MultiIndex
   1235             \# revise the key wrt to \`section\` by inserting an \_NS

File ~/work/pandas/pandas/pandas/core/indexing.py:1914, in \_LocIndexer.\_getitem\_axis(self, key, axis)
   1912 if isinstance(key, slice):
   1913     self.\_validate\_key(key, axis)
\-> 1914     return self.\_get\_slice\_axis(key, axis\=axis)
   1915 elif com.is\_bool\_indexer(key):
   1916     return self.\_getbool\_axis(key, axis\=axis)

File ~/work/pandas/pandas/pandas/core/indexing.py:1978, in \_LocIndexer.\_get\_slice\_axis(self, slice\_obj, axis)
   1975     return obj.copy(deep\=False)
   1977 labels \= obj.\_get\_axis(axis)
\-> 1978 indexer \= labels.slice\_indexer(slice\_obj.start, slice\_obj.stop, slice\_obj.step)
   1980 if isinstance(indexer, slice):
   1981     return self.obj.\_slice(indexer, axis\=axis)

File ~/work/pandas/pandas/pandas/core/indexes/base.py:7136, in Index.slice\_indexer(self, start, end, step)
   7085 def slice\_indexer(
   7086     self,
   7087     start: Hashable | None \= None,
   7088     end: Hashable | None \= None,
   7089     step: int | None \= None,
   7090 ) \-> slice:
   7091     """
   7092     Compute the slice indexer for input labels and step.
   7093 
   (...)   7134     slice(1, 3, None)
   7135     """
\-> 7136     start\_slice, end\_slice \= self.slice\_locs(start, end, step\=step)
   7138     \# return a slice
   7139     if not is\_scalar(start\_slice):

File ~/work/pandas/pandas/pandas/core/indexes/base.py:7419, in Index.slice\_locs(self, start, end, step)
   7417 end\_slice \= None
   7418 if end is not None:
\-> 7419     end\_slice \= self.get\_slice\_bound(end, "right")
   7420 if end\_slice is None:
   7421     end\_slice \= len(self)

File ~/work/pandas/pandas/pandas/core/indexes/base.py:7320, in Index.get\_slice\_bound(self, label, side)
   7318     slc \= lib.maybe\_booleans\_to\_slice(slc.view("u1"))  \# type: ignore\[assignment\]
   7319     if isinstance(slc, np.ndarray):
\-> 7320         raise KeyError(
   7321             f"Cannot get {side} slice bound for non-unique "
   7322             f"label: {original\_label!r}"
   7323         )
   7325 if isinstance(slc, slice):
   7326     if side \== "left":

KeyError: 'Cannot get right slice bound for non-unique label: 3'

Copy to clipboard

`Index.is_monotonic_increasing` and `Index.is_monotonic_decreasing` only check that an index is weakly monotonic. To check for strict monotonicity, you can combine one of those with the [`is_unique()`](https://pandas.pydata.org/docs/reference/api/pandas.Index.is_unique.html#pandas.Index.is_unique "pandas.Index.is_unique")
 attribute.

In \[239\]: weakly\_monotonic \= pd.Index(\["a", "b", "c", "c"\])

In \[240\]: weakly\_monotonic
Out\[240\]: Index(\['a', 'b', 'c', 'c'\], dtype='str')

In \[241\]: weakly\_monotonic.is\_monotonic\_increasing
Out\[241\]: True

In \[242\]: weakly\_monotonic.is\_monotonic\_increasing & weakly\_monotonic.is\_unique
Out\[242\]: False

Copy to clipboard

### Endpoints are inclusive[#](https://pandas.pydata.org/docs/user_guide/advanced.html#endpoints-are-inclusive "Link to this heading")

Compared with standard Python sequence slicing in which the slice endpoint is not inclusive, label-based slicing in pandas **is inclusive**. The primary reason for this is that it is often not possible to easily determine the “successor” or next element after a particular label in an index. For example, consider the following `Series`:

In \[243\]: s \= pd.Series(np.random.randn(6), index\=list("abcdef"))

In \[244\]: s
Out\[244\]: 
a   -0.101684
b   -0.734907
c   -0.130121
d   -0.476046
e    0.759104
f    0.213379
dtype: float64

Copy to clipboard

Suppose we wished to slice from `c` to `e`, using integers this would be accomplished as such:

In \[245\]: s\[2:5\]
Out\[245\]: 
c   -0.130121
d   -0.476046
e    0.759104
dtype: float64

Copy to clipboard

However, if you only had `c` and `e`, determining the next element in the index can be somewhat complicated. For example, the following does not work:

In \[246\]: s.loc\['c':'e' + 1\]
\---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In\[246\], line 1
\----> 1 s.loc\['c':'e' + 1\]

TypeError: can only concatenate str (not "int") to str

Copy to clipboard

A very common use case is to limit a time series to start and end at two specific dates. To enable this, we made the design choice to make label-based slicing include both endpoints:

In \[247\]: s.loc\["c":"e"\]
Out\[247\]: 
c   -0.130121
d   -0.476046
e    0.759104
dtype: float64

Copy to clipboard

This is most definitely a “practicality beats purity” sort of thing, but it is something to watch out for if you expect label-based slicing to behave exactly in the way that standard Python integer slicing works.

### Indexing potentially changes underlying Series dtype[#](https://pandas.pydata.org/docs/user_guide/advanced.html#indexing-potentially-changes-underlying-series-dtype "Link to this heading")

The different indexing operation can potentially change the dtype of a `Series`.

In \[248\]: series1 \= pd.Series(\[1, 2, 3\])

In \[249\]: series1.dtype
Out\[249\]: dtype('int64')

In \[250\]: res \= series1.reindex(\[0, 4\])

In \[251\]: res.dtype
Out\[251\]: dtype('float64')

In \[252\]: res
Out\[252\]: 
0    1.0
4    NaN
dtype: float64

Copy to clipboard

In \[253\]: series2 \= pd.Series(\[True\])

In \[254\]: series2.dtype
Out\[254\]: dtype('bool')

In \[255\]: res \= series2.reindex\_like(series1)

In \[256\]: res.dtype
Out\[256\]: dtype('O')

In \[257\]: res
Out\[257\]: 
0    True
1     NaN
2     NaN
dtype: object

Copy to clipboard

This is because the (re)indexing operations above silently inserts `NaNs` and the `dtype` changes accordingly. This can cause some issues when using `numpy` `ufuncs` such as `numpy.logical_and`.

See the [GH 2388](https://github.com/pandas-dev/pandas/issues/2388)
 for a more detailed discussion.

On this page