[Skip to main content](https://pandas.pydata.org/docs/user_guide/gotchas.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/user_guide/gotchas.html)
[3.1 (stable)](https://pandas.pydata.org/docs/user_guide/gotchas.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/user_guide/gotchas.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/gotchas.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/user_guide/gotchas.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/user_guide/gotchas.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/gotchas.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/user_guide/gotchas.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/user_guide/gotchas.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/user_guide/gotchas.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/user_guide/gotchas.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/gotchas.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/user_guide/gotchas.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Frequently Asked Questions (FAQ)[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#frequently-asked-questions-faq "Link to this heading")

==================================================================================================================================================

DataFrame memory usage[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#dataframe-memory-usage "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

The memory usage of a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (including the index) is shown when calling the [`info()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info")
. A configuration option, `display.memory_usage` (see [the list of options](https://pandas.pydata.org/docs/user_guide/options.html#options-available)
), specifies if the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 memory usage will be displayed when invoking the [`info()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info")
 method.

For example, the memory usage of the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 below is shown when calling [`info()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info")
:

In \[1\]: dtypes \= \[\
   ...:    "int64",\
   ...:    "float64",\
   ...:    "datetime64\[ns\]",\
   ...:    "timedelta64\[ns\]",\
   ...:    "complex128",\
   ...:    "object",\
   ...:    "bool",\
   ...: \]
   ...: 

In \[2\]: n \= 5000

In \[3\]: data \= {t: np.random.randint(100, size\=n).astype(t) for t in dtypes}

In \[4\]: df \= pd.DataFrame(data)

In \[5\]: df\["categorical"\] \= df\["object"\].astype("category")

In \[6\]: df.info()
<class 'pandas.DataFrame'>
RangeIndex: 5000 entries, 0 to 4999
Data columns (total 8 columns):
 #   Column           Non-Null Count  Dtype          
\---  ------           --------------  -----          
 0   int64            5000 non-null   int64          
 1   float64          5000 non-null   float64        
 2   datetime64\[ns\]   5000 non-null   datetime64\[ns\] 
 3   timedelta64\[ns\]  5000 non-null   timedelta64\[ns\]
 4   complex128       5000 non-null   complex128     
 5   object           5000 non-null   object         
 6   bool             5000 non-null   bool           
 7   categorical      5000 non-null   category       
dtypes: bool(1), category(1), complex128(1), datetime64\[ns\](1), float64(1), int64(1), object(1), timedelta64\[ns\](1)
memory usage: 284.1+ KB

Copy to clipboard

The `+` symbol indicates that the true memory usage could be higher, because pandas does not count the memory used by values in columns with `dtype=object`.

Passing `memory_usage='deep'` will enable a more accurate memory usage report, accounting for the full usage of the contained objects. This is optional as it can be expensive to do this deeper introspection.

In \[7\]: df.info(memory\_usage\="deep")
<class 'pandas.DataFrame'>
RangeIndex: 5000 entries, 0 to 4999
Data columns (total 8 columns):
 #   Column           Non-Null Count  Dtype          
\---  ------           --------------  -----          
 0   int64            5000 non-null   int64          
 1   float64          5000 non-null   float64        
 2   datetime64\[ns\]   5000 non-null   datetime64\[ns\] 
 3   timedelta64\[ns\]  5000 non-null   timedelta64\[ns\]
 4   complex128       5000 non-null   complex128     
 5   object           5000 non-null   object         
 6   bool             5000 non-null   bool           
 7   categorical      5000 non-null   category       
dtypes: bool(1), category(1), complex128(1), datetime64\[ns\](1), float64(1), int64(1), object(1), timedelta64\[ns\](1)
memory usage: 420.8 KB

Copy to clipboard

By default the display option is set to `True` but can be explicitly overridden by passing the `memory_usage` argument when invoking [`info()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info")
.

The memory usage of each column can be found by calling the [`memory_usage()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html#pandas.DataFrame.memory_usage "pandas.DataFrame.memory_usage")
 method. This returns a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 with an index represented by column names and memory usage of each column shown in bytes. For the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 above, the memory usage of each column and the total memory usage can be found with the [`memory_usage()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html#pandas.DataFrame.memory_usage "pandas.DataFrame.memory_usage")
 method:

In \[8\]: df.memory\_usage()
Out\[8\]: 
Index                132
int64              40000
float64            40000
datetime64\[ns\]     40000
timedelta64\[ns\]    40000
complex128         80000
object             40000
bool                5000
categorical         5800
dtype: int64

\# total memory usage of dataframe
In \[9\]: df.memory\_usage().sum()
Out\[9\]: np.int64(290932)

Copy to clipboard

By default the memory usage of the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 index is shown in the returned [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
, the memory usage of the index can be suppressed by passing the `index=False` argument:

In \[10\]: df.memory\_usage(index\=False)
Out\[10\]: 
int64              40000
float64            40000
datetime64\[ns\]     40000
timedelta64\[ns\]    40000
complex128         80000
object             40000
bool                5000
categorical         5800
dtype: int64

Copy to clipboard

The memory usage displayed by the [`info()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info")
 method utilizes the [`memory_usage()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html#pandas.DataFrame.memory_usage "pandas.DataFrame.memory_usage")
 method to determine the memory usage of a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 while also formatting the output in human-readable units (base-2 representation; i.e. 1KB = 1024 bytes).

See also [Categorical Memory Usage](https://pandas.pydata.org/docs/user_guide/categorical.html#categorical-memory)
.

Using if/truth statements with pandas[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#using-if-truth-statements-with-pandas "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

pandas follows the NumPy convention of raising an error when you try to convert something to a `bool`. This happens in an `if`\-statement or when using the boolean operations: `and`, `or`, and `not`. It is not clear what the result of the following code should be:

\>>> if pd.Series(\[False, True, False\]):
...     pass

Copy to clipboard

Should it be `True` because it’s not zero-length, or `False` because there are `False` values? It is unclear, so instead, pandas raises a `ValueError`:

In \[11\]: if pd.Series(\[False, True, False\]):
   ....:    print("I was true")
   ....: 
\---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In\[11\], line 1
\----> 1 if pd.Series(\[False, True, False\]):
      2     print("I was true")

File ~/work/pandas/pandas/pandas/core/generic.py:1445, in NDFrame.\_\_bool\_\_(self)
   1443     @final
   1444     def \_\_bool\_\_(self) \-> NoReturn:
\-> 1445         raise ValueError(
   1446             f"The truth value of a {type(self).\_\_name\_\_} is ambiguous. "
   1447             "Use a.empty, a.item(), a.any() or a.all()."
   1448         )

ValueError: The truth value of a Series is ambiguous. Use a.empty, a.item(), a.any() or a.all().

Copy to clipboard

You need to explicitly choose what you want to do with the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
, e.g. use [`any()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html#pandas.DataFrame.any "pandas.DataFrame.any")
, [`all()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.all.html#pandas.DataFrame.all "pandas.DataFrame.all")
 or [`empty()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.empty.html#pandas.DataFrame.empty "pandas.DataFrame.empty")
. Alternatively, you might want to compare if the pandas object is `None`:

In \[12\]: if pd.Series(\[False, True, False\]) is not None:
   ....:    print("I was not None")
   ....: 
I was not None

Copy to clipboard

Below is how to check if any of the values are `True`:

In \[13\]: if pd.Series(\[False, True, False\]).any():
   ....:    print("I am any")
   ....: 
I am any

Copy to clipboard

### Bitwise Boolean[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#bitwise-boolean "Link to this heading")

Bitwise boolean operators like `==` and `!=` return a boolean [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 which performs an element-wise comparison when compared to a scalar.

In \[14\]: s \= pd.Series(range(5))

In \[15\]: s \== 4
Out\[15\]: 
0    False
1    False
2    False
3    False
4     True
dtype: bool

Copy to clipboard

See [boolean comparisons](https://pandas.pydata.org/docs/user_guide/basics.html#basics-compare)
 for more examples.

### Using the `in` operator[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#using-the-in-operator "Link to this heading")

Using the Python `in` operator on a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 tests for membership in the **index**, not membership among the values.

In \[16\]: s \= pd.Series(range(5), index\=list("abcde"))

In \[17\]: 2 in s
Out\[17\]: False

In \[18\]: 'b' in s
Out\[18\]: True

Copy to clipboard

If this behavior is surprising, keep in mind that using `in` on a Python dictionary tests keys, not values, and [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 are dict-like. To test for membership in the values, use the method [`isin()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#pandas.Series.isin "pandas.Series.isin")
:

In \[19\]: s.isin(\[2\])
Out\[19\]: 
a    False
b    False
c     True
d    False
e    False
dtype: bool

In \[20\]: s.isin(\[2\]).any()
Out\[20\]: np.True\_

Copy to clipboard

For [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
, likewise, `in` applies to the column axis, testing for membership in the list of column names.

Mutating with User Defined Function (UDF) methods[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#mutating-with-user-defined-function-udf-methods "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section applies to pandas methods that take a UDF. In particular, the methods [`DataFrame.apply()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")
, [`DataFrame.aggregate()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.aggregate.html#pandas.DataFrame.aggregate "pandas.DataFrame.aggregate")
, [`DataFrame.transform()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html#pandas.DataFrame.transform "pandas.DataFrame.transform")
, and [`DataFrame.filter()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html#pandas.DataFrame.filter "pandas.DataFrame.filter")
.

It is a general rule in programming that one should not mutate a container while it is being iterated over. Mutation will invalidate the iterator, causing unexpected behavior. Consider the example:

In \[21\]: values \= \[0, 1, 2, 3, 4, 5\]

In \[22\]: n\_removed \= 0

In \[23\]: for k, value in enumerate(values):
   ....:    idx \= k \- n\_removed
   ....:    if value % 2 \== 1:
   ....:        del values\[idx\]
   ....:        n\_removed += 1
   ....:    else:
   ....:        values\[idx\] \= value + 1
   ....: 

In \[24\]: values
Out\[24\]: \[1, 4, 5\]

Copy to clipboard

One probably would have expected that the result would be `[1, 3, 5]`. When using a pandas method that takes a UDF, internally pandas is often iterating over the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 or other pandas object. Therefore, if the UDF mutates (changes) the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
, unexpected behavior can arise.

Here is a similar example with [`DataFrame.apply()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")
:

In \[25\]: def f(s):
   ....:    s.pop("a")
   ....:    return s
   ....: 

In \[26\]: df \= pd.DataFrame({"a": \[1, 2, 3\], "b": \[4, 5, 6\]})

In \[27\]: df.apply(f, axis\="columns")
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
KeyError: 'a'

The above exception was the direct cause of the following exception:

KeyError                                  Traceback (most recent call last)
Cell In\[27\], line 1
\----> 1 df.apply(f, axis\="columns")

File ~/work/pandas/pandas/pandas/core/frame.py:15427, in DataFrame.apply(self, func, axis, raw, result\_type, args, by\_row, engine, engine\_kwargs, \*\*kwargs)
  15423                 engine\_kwargs\=engine\_kwargs,
  15424                 args\=args,
  15425                 kwargs\=kwargs,
  15426             )
\> 15427             return op.apply().\_\_finalize\_\_(self, method\="apply")
  15428         elif hasattr(engine, "\_\_pandas\_udf\_\_"):
  15429             if result\_type is not None:
  15430                 raise NotImplementedError(

File ~/work/pandas/pandas/pandas/core/apply.py:1106, in FrameApply.apply(self)
   1103 elif self.raw:
   1104     return self.apply\_raw(engine\=self.engine, engine\_kwargs\=self.engine\_kwargs)
\-> 1106 return self.apply\_standard()

File ~/work/pandas/pandas/pandas/core/apply.py:1334, in FrameApply.apply\_standard(self)
   1332 def apply\_standard(self):
   1333     if self.engine \== "python":
\-> 1334         results, res\_index \= self.apply\_series\_generator()
   1335     else:
   1336         results, res\_index \= self.apply\_series\_numba()

File ~/work/pandas/pandas/pandas/core/apply.py:1350, in FrameApply.apply\_series\_generator(self)
   1347 results \= {}
   1349 for i, v in enumerate(series\_gen):
\-> 1350     results\[i\] \= self.func(v, \*self.args, \*\*self.kwargs)
   1351     if isinstance(results\[i\], ABCSeries):
   1352         \# If we have a view on v, we need to make a copy because
   1353         \#  series\_generator will swap out the underlying data
   1354         results\[i\] \= results\[i\].copy(deep\=False)

Cell In\[25\], line 2, in f(s)
      1 def f(s):
\----> 2     s.pop("a")
      3     return s

File ~/work/pandas/pandas/pandas/core/series.py:6357, in Series.pop(self, item)
   6353         1    2
   6354         2    3
   6355         dtype: int64
   6356         """
\-> 6357         return super().pop(item=item)

File ~/work/pandas/pandas/pandas/core/generic.py:845, in NDFrame.pop(self, item)
    844     def pop(self, item: Hashable) -> Series | Any:
\--> 845         result = self\[item\]
    846         del self\[item\]
    847 
    848         return result

File ~/work/pandas/pandas/pandas/core/series.py:1102, in Series.\_\_getitem\_\_(self, key)
   1098 
   1099         elif key\_is\_scalar:
   1100             # Note: GH#50617 in 3.0 we changed int key to always be treated as
   1101             #  a label, matching DataFrame behavior.
\-> 1102             return self.\_get\_value(key)
   1103 
   1104         # Convert generator to list before going through hashable part
   1105         # (We will iterate through the generator there to check for slices)

File ~/work/pandas/pandas/pandas/core/series.py:1189, in Series.\_get\_value(self, label, takeable)
   1185         if takeable:
   1186             return self.\_ixs(label)
   1187 
   1188         # Similar to Index.get\_value, but we do not fall back to positional
\-> 1189         loc = self.index.get\_loc(label)
   1190 
   1191         if is\_integer(loc):
   1192             return self.\_ixs(loc)

File ~/work/pandas/pandas/pandas/core/indexes/base.py:3823, in Index.get\_loc(self, key)
   3818     if isinstance(casted\_key, slice) or (
   3819         isinstance(casted\_key, abc.Iterable)
   3820         and any(isinstance(x, slice) for x in casted\_key)
   3821     ):
   3822         raise InvalidIndexError(key) from err
\-> 3823     raise KeyError(key) from err
   3824 except TypeError:
   3825     # If we have a listlike key, \_check\_indexing\_error will raise
   3826     #  InvalidIndexError. Otherwise we fall through and re-raise
   3827     #  the TypeError.
   3828     self.\_check\_indexing\_error(key)

KeyError: 'a'

Copy to clipboard

To resolve this issue, one can make a copy so that the mutation does not apply to the container being iterated over.

In \[28\]: values \= \[0, 1, 2, 3, 4, 5\]

In \[29\]: n\_removed \= 0

In \[30\]: for k, value in enumerate(values.copy()):
   ....:    idx \= k \- n\_removed
   ....:    if value % 2 \== 1:
   ....:        del values\[idx\]
   ....:        n\_removed += 1
   ....:    else:
   ....:        values\[idx\] \= value + 1
   ....: 

In \[31\]: values
Out\[31\]: \[1, 3, 5\]

Copy to clipboard

In \[32\]: def f(s):
   ....:    s \= s.copy()
   ....:    s.pop("a")
   ....:    return s
   ....: 

In \[33\]: df \= pd.DataFrame({"a": \[1, 2, 3\], 'b': \[4, 5, 6\]})

In \[34\]: df.apply(f, axis\="columns")
Out\[34\]: 
   b
0  4
1  5
2  6

Copy to clipboard

Missing value representation for NumPy types[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#missing-value-representation-for-numpy-types "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### `np.nan` as the `NA` representation for NumPy types[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#np-nan-as-the-na-representation-for-numpy-types "Link to this heading")

For lack of `NA` (missing) support from the ground up in NumPy and Python in general, `NA` could have been represented with:

*   A _masked array_ solution: an array of data and an array of boolean values indicating whether a value is there or is missing.
    
*   Using a special sentinel value, bit pattern, or set of sentinel values to denote `NA` across the dtypes.
    

The special value `np.nan` (Not-A-Number) was chosen as the `NA` value for NumPy types, and there are API functions like [`DataFrame.isna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna "pandas.DataFrame.isna")
 and [`DataFrame.notna()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html#pandas.DataFrame.notna "pandas.DataFrame.notna")
 which can be used across the dtypes to detect NA values. However, this choice has a downside of coercing missing integer data as float types as shown in [Support for integer NA](https://pandas.pydata.org/docs/user_guide/gotchas.html#gotchas-intna)
.

### `NA` type promotions for NumPy types[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#na-type-promotions-for-numpy-types "Link to this heading")

When introducing NAs into an existing [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 or [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 via [`reindex()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html#pandas.Series.reindex "pandas.Series.reindex")
 or some other means, boolean and integer types will be promoted to a different dtype in order to store the NAs. The promotions are summarized in this table:

 
| Typeclass | Promotion dtype for storing NAs |
| --- | --- |
| `floating` | no change |
| `object` | no change |
| `integer` | cast to `float64` |
| `boolean` | cast to `object` |

### Support for integer `NA`[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#support-for-integer-na "Link to this heading")

In the absence of high performance `NA` support being built into NumPy from the ground up, the primary casualty is the ability to represent NAs in integer arrays. For example:

In \[35\]: s \= pd.Series(\[1, 2, 3, 4, 5\], index\=list("abcde"))

In \[36\]: s
Out\[36\]: 
a    1
b    2
c    3
d    4
e    5
dtype: int64

In \[37\]: s.dtype
Out\[37\]: dtype('int64')

In \[38\]: s2 \= s.reindex(\["a", "b", "c", "f", "u"\])

In \[39\]: s2
Out\[39\]: 
a    1.0
b    2.0
c    3.0
f    NaN
u    NaN
dtype: float64

In \[40\]: s2.dtype
Out\[40\]: dtype('float64')

Copy to clipboard

This trade-off is made largely for memory and performance reasons, and also so that the resulting [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 continues to be “numeric”.

If you need to represent integers with possibly missing values, use one of the nullable-integer extension dtypes provided by pandas or pyarrow

*   [`Int8Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int8Dtype.html#pandas.Int8Dtype "pandas.Int8Dtype")
    
*   [`Int16Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int16Dtype.html#pandas.Int16Dtype "pandas.Int16Dtype")
    
*   [`Int32Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int32Dtype.html#pandas.Int32Dtype "pandas.Int32Dtype")
    
*   [`Int64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int64Dtype.html#pandas.Int64Dtype "pandas.Int64Dtype")
    
*   [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
    

In \[41\]: s\_int \= pd.Series(\[1, 2, 3, 4, 5\], index\=list("abcde"), dtype\=pd.Int64Dtype())

In \[42\]: s\_int
Out\[42\]: 
a    1
b    2
c    3
d    4
e    5
dtype: Int64

In \[43\]: s\_int.dtype
Out\[43\]: Int64Dtype()

In \[44\]: s2\_int \= s\_int.reindex(\["a", "b", "c", "f", "u"\])

In \[45\]: s2\_int
Out\[45\]: 
a       1
b       2
c       3
f    <NA>
u    <NA>
dtype: Int64

In \[46\]: s2\_int.dtype
Out\[46\]: Int64Dtype()

In \[47\]: s\_int\_pa \= pd.Series(\[1, 2, None\], dtype\="int64\[pyarrow\]")

In \[48\]: s\_int\_pa
Out\[48\]: 
0       1
1       2
2    <NA>
dtype: int64\[pyarrow\]

Copy to clipboard

See [Nullable integer data type](https://pandas.pydata.org/docs/user_guide/integer_na.html#integer-na)
 and [PyArrow Functionality](https://pandas.pydata.org/docs/user_guide/pyarrow.html#pyarrow)
 for more.

### Why not make NumPy like R?[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#why-not-make-numpy-like-r "Link to this heading")

Many people have suggested that NumPy should simply emulate the `NA` support present in the more domain-specific statistical programming language [R](https://www.r-project.org/)
. Part of the reason is the [NumPy type hierarchy](https://numpy.org/doc/stable/user/basics.types.html)
.

The R language, by contrast, only has a handful of built-in data types: `integer`, `numeric` (floating-point), `character`, and `boolean`. `NA` types are implemented by reserving special bit patterns for each type to be used as the missing value. While doing this with the full NumPy type hierarchy would be possible, it would be a more substantial trade-off (especially for the 8- and 16-bit data types) and implementation undertaking.

However, R `NA` semantics are now available by using masked NumPy types such as [`Int64Dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Int64Dtype.html#pandas.Int64Dtype "pandas.Int64Dtype")
 or PyArrow types ([`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
).

Integer overflow[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#integer-overflow "Link to this heading")

--------------------------------------------------------------------------------------------------------------------

pandas uses NumPy’s fixed-width integer types (`int64` by default) rather than Python’s arbitrary-precision integers. This means integer arithmetic can silently overflow without raising an error:

In \[49\]: series \= pd.Series(\[406, 372, 496, 41, 63, 118, 311, 271, 431, 95, 57, 52\])

In \[50\]: series.dtype
Out\[50\]: dtype('int64')

Copy to clipboard

The product of these integers exceeds the range of `int64`, so the result wraps around silently:

In \[51\]: series.prod()
Out\[51\]: np.int64(3321523566636606464)

Copy to clipboard

Compare this to pure Python, which uses arbitrary-precision integers and gives the correct result:

In \[52\]: python\_product \= 1

In \[53\]: for val in \[406, 372, 496, 41, 63, 118, 311, 271, 431, 95, 57, 52\]:
   ....:    python\_product \*= val
   ....: 

In \[54\]: python\_product
Out\[54\]: 233542442569297099243299840

Copy to clipboard

This behavior comes from NumPy and affects all integer arithmetic operations (addition, subtraction, multiplication, etc.), not just [`prod()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.prod.html#pandas.Series.prod "pandas.Series.prod")
. See the [NumPy documentation on overflow errors](https://numpy.org/doc/stable/user/basics.types.html#overflow-errors)
 for more details.

If your computation may exceed `int64` range, you can convert to `float64` first (at the cost of precision for very large values) or use Python’s built-in integers via `object` dtype:

In \[55\]: series.astype("float64").prod()
Out\[55\]: np.float64(2.3354244256929707e+26)

In \[56\]: series.astype("object").prod()
Out\[56\]: 233542442569297099243299840

Copy to clipboard

NumPy compatibility kwargs[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#numpy-compatibility-kwargs "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

Many pandas methods accept additional keyword arguments (often passed as `**kwargs`) to ensure compatibility with NumPy’s API. When a pandas object is passed to a NumPy function (for example, `np.sum(df)`), NumPy will often pass its own arguments (such as `out` or `keepdims`) to the pandas method. To prevent errors, pandas accepts these keywords, if passed with their default value.

While pandas historically ignored many of these additional arguments, the library now strictly validates them (i.e. ensuring they are only passed with their default values) or deprecates them where they are not necessary for NumPy compatibility. If you pass an argument that pandas does not implement, it will raise an error or emit a deprecation warning. You should only rely on the arguments explicitly documented in the pandas method signature.

Differences with NumPy[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#differences-with-numpy "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

For [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 and [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 objects, [`var()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html#pandas.DataFrame.var "pandas.DataFrame.var")
 normalizes by `N-1` to produce [unbiased estimates of the population variance](https://en.wikipedia.org/wiki/Bias_of_an_estimator)
, while NumPy’s `numpy.var()` normalizes by N, which measures the variance of the sample. Note that [`cov()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cov.html#pandas.DataFrame.cov "pandas.DataFrame.cov")
 normalizes by `N-1` in both pandas and NumPy.

Thread-safety[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#thread-safety "Link to this heading")

--------------------------------------------------------------------------------------------------------------

pandas is not 100% thread safe. The known issues relate to the [`copy()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html#pandas.DataFrame.copy "pandas.DataFrame.copy")
 method. If you are doing a lot of copying of [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 objects shared among threads, we recommend holding locks inside the threads where the data copying occurs.

See [this link](https://stackoverflow.com/questions/13592618/python-pandas-dataframe-thread-safe)
 for more information.

Byte-ordering issues[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#byte-ordering-issues "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Occasionally you may have to deal with data that were created on a machine with a different byte order than the one on which you are running Python. A common symptom of this issue is an error like:

Traceback
    ...
ValueError: Big\-endian buffer not supported on little\-endian compiler

Copy to clipboard

To deal with this issue you should convert the underlying NumPy array to the native system byte order _before_ passing it to [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 or [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 constructors using something similar to the following:

In \[57\]: x \= np.array(list(range(10)), ">i4")  \# big endian

In \[58\]: newx \= x.byteswap().view(x.dtype.newbyteorder())  \# force native byteorder

In \[59\]: s \= pd.Series(newx)

Copy to clipboard

See [the NumPy documentation on byte order](https://numpy.org/doc/stable/user/byteswapping.html)
 for more details.

Storing lists inside a `DataFrame` or `Series`[#](https://pandas.pydata.org/docs/user_guide/gotchas.html#storing-lists-inside-a-dataframe-or-series "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

It is possible to store Python lists (or other collections) in the cells of a `DataFrame` or `Series`, but it is best avoided. A column containing lists has `object` dtype: each cell holds a reference to a separate Python object, so the column uses far more memory than a native-dtype column and no operation on it can use pandas’ vectorized code paths. Because lists are not hashable, such a column also cannot be used as a group or merge key, and methods that need to hash the values, like [`drop_duplicates()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "pandas.DataFrame.drop_duplicates")
, raise a `TypeError`.

In \[60\]: df \= pd.DataFrame(
   ....:    {
   ....:        "name": \["A.J. Price"\] \* 3,
   ....:        "opponent": \["76ers", "blazers", "bobcats"\],
   ....:    }
   ....: )
   ....: 

In \[61\]: df\["nearest\_neighbors"\] \= \[\["Zach LaVine", "Jeremy Lin", "Nate Robinson"\]\] \* 3

In \[62\]: df
Out\[62\]: 
         name opponent                         nearest\_neighbors
0  A.J. Price    76ers  \[Zach LaVine, Jeremy Lin, Nate Robinson\]
1  A.J. Price  blazers  \[Zach LaVine, Jeremy Lin, Nate Robinson\]
2  A.J. Price  bobcats  \[Zach LaVine, Jeremy Lin, Nate Robinson\]

In \[63\]: df.dtypes
Out\[63\]: 
name                    str
opponent                str
nearest\_neighbors    object
dtype: object

Copy to clipboard

Instead, prefer a “long” format, with one row per list element. Existing list-valued cells can be converted with [`explode()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html#pandas.DataFrame.explode "pandas.DataFrame.explode")
:

In \[64\]: exploded \= df.explode("nearest\_neighbors")

In \[65\]: exploded
Out\[65\]: 
         name opponent nearest\_neighbors
0  A.J. Price    76ers       Zach LaVine
0  A.J. Price    76ers        Jeremy Lin
0  A.J. Price    76ers     Nate Robinson
1  A.J. Price  blazers       Zach LaVine
1  A.J. Price  blazers        Jeremy Lin
1  A.J. Price  blazers     Nate Robinson
2  A.J. Price  bobcats       Zach LaVine
2  A.J. Price  bobcats        Jeremy Lin
2  A.J. Price  bobcats     Nate Robinson

In \[66\]: exploded.dtypes
Out\[66\]: 
name                 str
opponent             str
nearest\_neighbors    str
dtype: object

Copy to clipboard

Each element now occupies its own row in a natively-typed column, and the usual vectorized operations, grouping, and joining all apply. If a nested presentation is needed at the end of a computation, the lists can be rebuilt with `agg(list)`:

In \[67\]: exploded.groupby(\["name", "opponent"\], sort\=False)\["nearest\_neighbors"\].agg(list)
Out\[67\]: 
name        opponent
A.J. Price  76ers       \[Zach LaVine, Jeremy Lin, Nate Robinson\]
            blazers     \[Zach LaVine, Jeremy Lin, Nate Robinson\]
            bobcats     \[Zach LaVine, Jeremy Lin, Nate Robinson\]
Name: nearest\_neighbors, dtype: object

Copy to clipboard

For columns of delimited strings, split directly into columns or indicator variables with `.str` methods rather than creating lists as an intermediate step:

In \[68\]: ser \= pd.Series(\["a|b", "b", "a|c"\])

In \[69\]: ser.str.split("|", expand\=True)
Out\[69\]: 
   0    1
0  a    b
1  b  NaN
2  a    c

In \[70\]: ser.str.get\_dummies(sep\="|")
Out\[70\]: 
   a  b  c
0  1  1  0
1  0  1  0
2  1  0  1

Copy to clipboard

On this page