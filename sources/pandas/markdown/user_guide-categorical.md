[Skip to main content](https://pandas.pydata.org/docs/user_guide/categorical.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/user_guide/categorical.html)
[3.1 (stable)](https://pandas.pydata.org/docs/user_guide/categorical.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/user_guide/categorical.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/categorical.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/user_guide/categorical.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/user_guide/categorical.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/categorical.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/user_guide/categorical.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/user_guide/categorical.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/user_guide/categorical.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/user_guide/categorical.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/categorical.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/user_guide/categorical.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Categorical data[#](https://pandas.pydata.org/docs/user_guide/categorical.html#categorical-data "Link to this heading")

========================================================================================================================

This is an introduction to pandas categorical data type, including a short comparison with R’s `factor`.

`Categoricals` are a pandas data type corresponding to categorical variables in statistics. A categorical variable takes on a limited, and usually fixed, number of possible values (`categories`; `levels` in R). Examples are gender, social class, blood type, country affiliation, observation time or rating via Likert scales.

In contrast to statistical categorical variables, categorical data might have an order (e.g. ‘strongly agree’ vs ‘agree’ or ‘first observation’ vs. ‘second observation’), but numerical operations (additions, divisions, …) are not possible.

All values of categorical data are either in `categories` or `np.nan`. Order is defined by the order of `categories`, not lexical order of the values. Internally, the data structure consists of a `categories` array and an integer array of `codes` which point to the real value in the `categories` array.

The categorical data type is useful in the following cases:

*   A string variable consisting of only a few different values. Converting such a string variable to a categorical variable will save some memory, see section [Memory usage](https://pandas.pydata.org/docs/user_guide/categorical.html#categorical-memory)
    .
    
*   The lexical order of a variable is not the same as the logical order (“one”, “two”, “three”). By converting to a categorical and specifying an order on the categories, sorting and min/max will use the logical order instead of the lexical order, see section [Sorting and order](https://pandas.pydata.org/docs/user_guide/categorical.html#categorical-sort)
    .
    
*   As a signal to other Python libraries that this column should be treated as a categorical variable (e.g. to use suitable statistical methods or plot types).
    

See also the [API docs on categoricals](https://pandas.pydata.org/docs/reference/arrays.html#api-arrays-categorical)
.

Object creation[#](https://pandas.pydata.org/docs/user_guide/categorical.html#object-creation "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

### Series creation[#](https://pandas.pydata.org/docs/user_guide/categorical.html#series-creation "Link to this heading")

Categorical `Series` or columns in a `DataFrame` can be created in several ways:

By specifying `dtype="category"` when constructing a `Series`:

In \[1\]: s \= pd.Series(\["a", "b", "c", "a"\], dtype\="category")

In \[2\]: s
Out\[2\]: 
0    a
1    b
2    c
3    a
dtype: category
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

By converting an existing `Series` or column to a `category` dtype:

In \[3\]: df \= pd.DataFrame({"A": \["a", "b", "c", "a"\]})

In \[4\]: df\["B"\] \= df\["A"\].astype("category")

In \[5\]: df
Out\[5\]: 
   A  B
0  a  a
1  b  b
2  c  c
3  a  a

Copy to clipboard

By using special functions, such as [`cut()`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")
, which groups data into discrete bins. See the [example on tiling](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-tile-cut)
 in the docs.

In \[6\]: df \= pd.DataFrame({"value": np.random.randint(0, 100, 20)})

In \[7\]: labels \= \["{0} - {1}".format(i, i + 9) for i in range(0, 100, 10)\]

In \[8\]: df\["group"\] \= pd.cut(df.value, range(0, 105, 10), right\=False, labels\=labels)

In \[9\]: df.head(10)
Out\[9\]: 
   value    group
0     65  60 - 69
1     49  40 - 49
2     56  50 - 59
3     43  40 - 49
4     43  40 - 49
5     91  90 - 99
6     32  30 - 39
7     87  80 - 89
8     36  30 - 39
9      8    0 - 9

Copy to clipboard

By passing a [`pandas.Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
 object to a `Series` or assigning it to a `DataFrame`.

In \[10\]: raw\_cat \= pd.Categorical(
   ....:    \[None, "b", "c", None\], categories\=\["b", "c", "d"\], ordered\=False
   ....: )
   ....: 

In \[11\]: s \= pd.Series(raw\_cat)

In \[12\]: s
Out\[12\]: 
0    NaN
1      b
2      c
3    NaN
dtype: category
Categories (3, str): \['b', 'c', 'd'\]

In \[13\]: df \= pd.DataFrame({"A": \["a", "b", "c", "a"\]})

In \[14\]: df\["B"\] \= raw\_cat

In \[15\]: df
Out\[15\]: 
   A    B
0  a  NaN
1  b    b
2  c    c
3  a  NaN

Copy to clipboard

Categorical data has a specific `category` [dtype](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)
:

In \[16\]: df.dtypes
Out\[16\]: 
A         str
B    category
dtype: object

Copy to clipboard

### DataFrame creation[#](https://pandas.pydata.org/docs/user_guide/categorical.html#dataframe-creation "Link to this heading")

Similar to the previous section where a single column was converted to categorical, all columns in a `DataFrame` can be batch converted to categorical either during or after construction.

This can be done during construction by specifying `dtype="category"` in the `DataFrame` constructor:

In \[17\]: df \= pd.DataFrame({"A": list("abca"), "B": list("bccd")}, dtype\="category")

In \[18\]: df.dtypes
Out\[18\]: 
A    category
B    category
dtype: object

Copy to clipboard

Note that the categories present in each column differ; the conversion is done column by column, so only labels present in a given column are categories:

In \[19\]: df\["A"\]
Out\[19\]: 
0    a
1    b
2    c
3    a
Name: A, dtype: category
Categories (3, str): \['a', 'b', 'c'\]

In \[20\]: df\["B"\]
Out\[20\]: 
0    b
1    c
2    c
3    d
Name: B, dtype: category
Categories (3, str): \['b', 'c', 'd'\]

Copy to clipboard

Analogously, all columns in an existing `DataFrame` can be batch converted using [`DataFrame.astype()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas.DataFrame.astype "pandas.DataFrame.astype")
:

In \[21\]: df \= pd.DataFrame({"A": list("abca"), "B": list("bccd")})

In \[22\]: df\_cat \= df.astype("category")

In \[23\]: df\_cat.dtypes
Out\[23\]: 
A    category
B    category
dtype: object

Copy to clipboard

This conversion is likewise done column by column:

In \[24\]: df\_cat\["A"\]
Out\[24\]: 
0    a
1    b
2    c
3    a
Name: A, dtype: category
Categories (3, str): \['a', 'b', 'c'\]

In \[25\]: df\_cat\["B"\]
Out\[25\]: 
0    b
1    c
2    c
3    d
Name: B, dtype: category
Categories (3, str): \['b', 'c', 'd'\]

Copy to clipboard

### Controlling behavior[#](https://pandas.pydata.org/docs/user_guide/categorical.html#controlling-behavior "Link to this heading")

In the examples above where we passed `dtype='category'`, we used the default behavior:

1.  Categories are inferred from the data.
    
2.  Categories are unordered.
    

To control those behaviors, instead of passing `'category'`, use an instance of `CategoricalDtype`.

In \[26\]: from pandas.api.types import CategoricalDtype

In \[27\]: s \= pd.Series(\[None, "b", "c", None\])

In \[28\]: cat\_type \= CategoricalDtype(categories\=\["b", "c", "d"\], ordered\=True)

In \[29\]: s\_cat \= s.astype(cat\_type)

In \[30\]: s\_cat
Out\[30\]: 
0    NaN
1      b
2      c
3    NaN
dtype: category
Categories (3, str): \['b' < 'c' < 'd'\]

Copy to clipboard

Similarly, a `CategoricalDtype` can be used with a `DataFrame` to ensure that categories are consistent among all columns.

In \[31\]: from pandas.api.types import CategoricalDtype

In \[32\]: df \= pd.DataFrame({"A": list("abca"), "B": list("bccd")})

In \[33\]: cat\_type \= CategoricalDtype(categories\=list("abcd"), ordered\=True)

In \[34\]: df\_cat \= df.astype(cat\_type)

In \[35\]: df\_cat\["A"\]
Out\[35\]: 
0    a
1    b
2    c
3    a
Name: A, dtype: category
Categories (4, str): \['a' < 'b' < 'c' < 'd'\]

In \[36\]: df\_cat\["B"\]
Out\[36\]: 
0    b
1    c
2    c
3    d
Name: B, dtype: category
Categories (4, str): \['a' < 'b' < 'c' < 'd'\]

Copy to clipboard

Note

To perform table-wise conversion, where all labels in the entire `DataFrame` are used as categories for each column, the `categories` parameter can be determined programmatically by `categories = pd.unique(df.to_numpy().ravel())`.

If you already have `codes` and `categories`, you can use the [`from_codes()`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.from_codes.html#pandas.Categorical.from_codes "pandas.Categorical.from_codes")
 constructor to save the factorize step during normal constructor mode:

In \[37\]: splitter \= np.random.choice(\[0, 1\], 5, p\=\[0.5, 0.5\])

In \[38\]: s \= pd.Series(pd.Categorical.from\_codes(splitter, categories\=\["train", "test"\]))

Copy to clipboard

### Regaining original data[#](https://pandas.pydata.org/docs/user_guide/categorical.html#regaining-original-data "Link to this heading")

To get back to the original `Series` or NumPy array, use `Series.astype(original_dtype)` or `np.asarray(categorical)`:

In \[39\]: s \= pd.Series(\["a", "b", "c", "a"\])

In \[40\]: s
Out\[40\]: 
0    a
1    b
2    c
3    a
dtype: str

In \[41\]: s2 \= s.astype("category")

In \[42\]: s2
Out\[42\]: 
0    a
1    b
2    c
3    a
dtype: category
Categories (3, str): \['a', 'b', 'c'\]

In \[43\]: s2.astype(str)
Out\[43\]: 
0    a
1    b
2    c
3    a
dtype: str

In \[44\]: np.asarray(s2)
Out\[44\]: array(\['a', 'b', 'c', 'a'\], dtype=object)

Copy to clipboard

Note

In contrast to R’s `factor` function, categorical data is not converting input values to strings; categories will end up the same data type as the original values.

Note

In contrast to R’s `factor` function, there is currently no way to assign/change labels at creation time. Use `categories` to change the categories after creation time.

CategoricalDtype[#](https://pandas.pydata.org/docs/user_guide/categorical.html#categoricaldtype "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

A categorical’s type is fully described by

1.  `categories`: a sequence of unique values and no missing values
    
2.  `ordered`: a boolean
    

This information can be stored in a `CategoricalDtype`. The `categories` argument is optional, which implies that the actual categories should be inferred from whatever is present in the data when the [`pandas.Categorical`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.html#pandas.Categorical "pandas.Categorical")
 is created. The categories are assumed to be unordered by default.

In \[45\]: from pandas.api.types import CategoricalDtype

In \[46\]: CategoricalDtype(\["a", "b", "c"\])
Out\[46\]: CategoricalDtype(categories=\['a', 'b', 'c'\], ordered=False, categories\_dtype=str)

In \[47\]: CategoricalDtype(\["a", "b", "c"\], ordered\=True)
Out\[47\]: CategoricalDtype(categories=\['a', 'b', 'c'\], ordered=True, categories\_dtype=str)

In \[48\]: CategoricalDtype()
Out\[48\]: CategoricalDtype(categories=None, ordered=False, categories\_dtype=None)

Copy to clipboard

A `CategoricalDtype` can be used in any place pandas expects a `dtype`. For example [`pandas.read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")
, [`pandas.DataFrame.astype()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas.DataFrame.astype "pandas.DataFrame.astype")
, or in the `Series` constructor.

Note

As a convenience, you can use the string `'category'` in place of a `CategoricalDtype` when you want the default behavior of the categories being unordered, and equal to the set values present in the array. In other words, `dtype='category'` is equivalent to `dtype=CategoricalDtype()`.

### Equality semantics[#](https://pandas.pydata.org/docs/user_guide/categorical.html#equality-semantics "Link to this heading")

Two instances of `CategoricalDtype` compare equal whenever they have the same categories and order. When comparing two unordered categoricals, the order of the `categories` is not considered. Note that categories with different dtypes are not the same.

In \[49\]: c1 \= CategoricalDtype(\["a", "b", "c"\], ordered\=False)

\# Equal, since order is not considered when ordered=False
In \[50\]: c1 \== CategoricalDtype(\["b", "c", "a"\], ordered\=False)
Out\[50\]: True

\# Unequal, since the second CategoricalDtype is ordered
In \[51\]: c1 \== CategoricalDtype(\["a", "b", "c"\], ordered\=True)
Out\[51\]: False

Copy to clipboard

All instances of `CategoricalDtype` compare equal to the string `'category'`.

In \[52\]: c1 \== "category"
Out\[52\]: True

Copy to clipboard

Notice that the `categories_dtype` should be considered, especially when comparing with two empty `CategoricalDtype` instances.

In \[53\]: c2 \= pd.Categorical(np.array(\[\], dtype\=object))

In \[54\]: c3 \= pd.Categorical(np.array(\[\], dtype\=float))

In \[55\]: c2.dtype \== c3.dtype
Out\[55\]: False

Copy to clipboard

Description[#](https://pandas.pydata.org/docs/user_guide/categorical.html#description "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Using [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe")
 on categorical data will produce similar output to a `Series` or `DataFrame` of type `string`.

In \[56\]: cat \= pd.Categorical(\["a", "c", "c", np.nan\], categories\=\["b", "a", "c"\])

In \[57\]: df \= pd.DataFrame({"cat": cat, "s": \["a", "c", "c", np.nan\]})

In \[58\]: df.describe()
Out\[58\]: 
       cat  s
count    3  3
unique   2  2
top      c  c
freq     2  2

In \[59\]: df\["cat"\].describe()
Out\[59\]: 
count     3
unique    2
top       c
freq      2
Name: cat, dtype: object

Copy to clipboard

Working with categories[#](https://pandas.pydata.org/docs/user_guide/categorical.html#working-with-categories "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Categorical data has a `categories` and a `ordered` property, which list their possible values and whether the ordering matters or not. These properties are exposed as `s.cat.categories` and `s.cat.ordered`. If you don’t manually specify categories and ordering, they are inferred from the passed arguments.

In \[60\]: s \= pd.Series(\["a", "b", "c", "a"\], dtype\="category")

In \[61\]: s.cat.categories
Out\[61\]: Index(\['a', 'b', 'c'\], dtype='str')

In \[62\]: s.cat.ordered
Out\[62\]: False

Copy to clipboard

It’s also possible to pass in the categories in a specific order:

In \[63\]: s \= pd.Series(pd.Categorical(\["a", "b", "c", "a"\], categories\=\["c", "b", "a"\]))

In \[64\]: s.cat.categories
Out\[64\]: Index(\['c', 'b', 'a'\], dtype='str')

In \[65\]: s.cat.ordered
Out\[65\]: False

Copy to clipboard

Note

New categorical data are **not** automatically ordered. You must explicitly pass `ordered=True` to indicate an ordered `Categorical`.

Note

The result of [`unique()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#pandas.Series.unique "pandas.Series.unique")
 is not always the same as `Series.cat.categories`, because `Series.unique()` has a couple of guarantees, namely that it returns categories in the order of appearance, and it only includes values that are actually present.

In \[66\]: s \= pd.Series(list("babc")).astype(CategoricalDtype(list("abcd")))

In \[67\]: s
Out\[67\]: 
0    b
1    a
2    b
3    c
dtype: category
Categories (4, str): \['a', 'b', 'c', 'd'\]

\# categories
In \[68\]: s.cat.categories
Out\[68\]: Index(\['a', 'b', 'c', 'd'\], dtype='str')

\# uniques
In \[69\]: s.unique()
Out\[69\]: 
\['b', 'a', 'c'\]
Categories (4, str): \['a', 'b', 'c', 'd'\]

Copy to clipboard

### Renaming categories[#](https://pandas.pydata.org/docs/user_guide/categorical.html#renaming-categories "Link to this heading")

Renaming categories is done by using the [`rename_categories()`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.rename_categories.html#pandas.Categorical.rename_categories "pandas.Categorical.rename_categories")
 method:

In \[70\]: s \= pd.Series(\["a", "b", "c", "a"\], dtype\="category")

In \[71\]: s
Out\[71\]: 
0    a
1    b
2    c
3    a
dtype: category
Categories (3, str): \['a', 'b', 'c'\]

In \[72\]: new\_categories \= \["Group %s" % g for g in s.cat.categories\]

In \[73\]: s \= s.cat.rename\_categories(new\_categories)

In \[74\]: s
Out\[74\]: 
0    Group a
1    Group b
2    Group c
3    Group a
dtype: category
Categories (3, str): \['Group a', 'Group b', 'Group c'\]

\# You can also pass a dict-like object to map the renaming
In \[75\]: s \= s.cat.rename\_categories({"Group a": "x", "Group b": "y", "Group c": "z"})

In \[76\]: s
Out\[76\]: 
0    x
1    y
2    z
3    x
dtype: category
Categories (3, str): \['x', 'y', 'z'\]

Copy to clipboard

Note

In contrast to R’s `factor`, categorical data can have categories of other types than string.

Categories must be unique or a `ValueError` is raised:

In \[77\]: try:
   ....:    s \= s.cat.rename\_categories(\[1, 1, 1\])
   ....: except ValueError as e:
   ....:    print("ValueError:", str(e))
   ....: 
ValueError: Categorical categories must be unique

Copy to clipboard

Categories must also not be `NaN` or a `ValueError` is raised:

In \[78\]: try:
   ....:    s \= s.cat.rename\_categories(\[1, 2, np.nan\])
   ....: except ValueError as e:
   ....:    print("ValueError:", str(e))
   ....: 
ValueError: Categorical categories cannot be null

Copy to clipboard

To merge several categories into one, use [`Series.replace()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html#pandas.Series.replace "pandas.Series.replace")
 to replace the values and then drop the categories that are no longer used with [`remove_unused_categories()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_unused_categories.html#pandas.Series.cat.remove_unused_categories "pandas.Series.cat.remove_unused_categories")
:

In \[79\]: s \= pd.Series(\["a", "b", "c", "a"\], dtype\="category")

In \[80\]: s \= s.replace({"a": "b"}).cat.remove\_unused\_categories()

In \[81\]: s
Out\[81\]: 
0    b
1    b
2    c
3    b
dtype: category
Categories (2, str): \['b', 'c'\]

Copy to clipboard

### Appending new categories[#](https://pandas.pydata.org/docs/user_guide/categorical.html#appending-new-categories "Link to this heading")

Appending categories can be done by using the [`add_categories()`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.add_categories.html#pandas.Categorical.add_categories "pandas.Categorical.add_categories")
 method:

In \[82\]: s \= s.cat.add\_categories(\[4\])

In \[83\]: s.cat.categories
Out\[83\]: Index(\['b', 'c', 4\], dtype='object')

In \[84\]: s
Out\[84\]: 
0    b
1    b
2    c
3    b
dtype: category
Categories (3, object): \['b', 'c', 4\]

Copy to clipboard

### Removing categories[#](https://pandas.pydata.org/docs/user_guide/categorical.html#removing-categories "Link to this heading")

Removing categories can be done by using the [`remove_categories()`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.remove_categories.html#pandas.Categorical.remove_categories "pandas.Categorical.remove_categories")
 method. Values which are removed are replaced by `np.nan`.:

In \[85\]: s \= s.cat.remove\_categories(\[4\])

In \[86\]: s
Out\[86\]: 
0    b
1    b
2    c
3    b
dtype: category
Categories (2, object): \['b', 'c'\]

Copy to clipboard

### Removing unused categories[#](https://pandas.pydata.org/docs/user_guide/categorical.html#removing-unused-categories "Link to this heading")

Removing unused categories can also be done:

In \[87\]: s \= pd.Series(pd.Categorical(\["a", "b", "a"\], categories\=\["a", "b", "c", "d"\]))

In \[88\]: s
Out\[88\]: 
0    a
1    b
2    a
dtype: category
Categories (4, str): \['a', 'b', 'c', 'd'\]

In \[89\]: s.cat.remove\_unused\_categories()
Out\[89\]: 
0    a
1    b
2    a
dtype: category
Categories (2, str): \['a', 'b'\]

Copy to clipboard

### Setting categories[#](https://pandas.pydata.org/docs/user_guide/categorical.html#setting-categories "Link to this heading")

If you want to do remove and add new categories in one step (which has some speed advantage), or simply set the categories to a predefined scale, use [`set_categories()`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.set_categories.html#pandas.Categorical.set_categories "pandas.Categorical.set_categories")
.

In \[90\]: s \= pd.Series(\["one", "two", "four", "-"\], dtype\="category")

In \[91\]: s
Out\[91\]: 
0     one
1     two
2    four
3       -
dtype: category
Categories (4, str): \['-', 'four', 'one', 'two'\]

In \[92\]: s \= s.cat.set\_categories(\["one", "two", "three", "four"\])

In \[93\]: s
Out\[93\]: 
0     one
1     two
2    four
3     NaN
dtype: category
Categories (4, str): \['one', 'two', 'three', 'four'\]

Copy to clipboard

Note

Be aware that [`Categorical.set_categories()`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.set_categories.html#pandas.Categorical.set_categories "pandas.Categorical.set_categories")
 cannot know whether some category is omitted intentionally or because it is misspelled or (under Python3) due to a type difference (e.g., NumPy S1 dtype and Python strings). This can result in surprising behaviour!

Sorting and order[#](https://pandas.pydata.org/docs/user_guide/categorical.html#sorting-and-order "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

If categorical data is ordered (`s.cat.ordered == True`), then the order of the categories has a meaning and certain operations are possible. If the categorical is unordered, `.min()/.max()` will raise a `TypeError`.

In \[94\]: s \= pd.Series(pd.Categorical(\["a", "b", "c", "a"\], ordered\=False))

In \[95\]: s \= s.sort\_values()

In \[96\]: s \= pd.Series(\["a", "b", "c", "a"\]).astype(CategoricalDtype(ordered\=True))

In \[97\]: s \= s.sort\_values()

In \[98\]: s
Out\[98\]: 
0    a
3    a
1    b
2    c
dtype: category
Categories (3, str): \['a' < 'b' < 'c'\]

In \[99\]: s.min(), s.max()
Out\[99\]: ('a', 'c')

Copy to clipboard

You can set categorical data to be ordered by using `as_ordered()` or unordered by using `as_unordered()`. These will by default return a _new_ object.

In \[100\]: s.cat.as\_ordered()
Out\[100\]: 
0    a
3    a
1    b
2    c
dtype: category
Categories (3, str): \['a' < 'b' < 'c'\]

In \[101\]: s.cat.as\_unordered()
Out\[101\]: 
0    a
3    a
1    b
2    c
dtype: category
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

Sorting will use the order defined by categories, not any lexical order present on the data type. This is even true for strings and numeric data:

In \[102\]: s \= pd.Series(\[1, 2, 3, 1\], dtype\="category")

In \[103\]: s \= s.cat.set\_categories(\[2, 3, 1\], ordered\=True)

In \[104\]: s
Out\[104\]: 
0    1
1    2
2    3
3    1
dtype: category
Categories (3, int64): \[2 < 3 < 1\]

In \[105\]: s \= s.sort\_values()

In \[106\]: s
Out\[106\]: 
1    2
2    3
0    1
3    1
dtype: category
Categories (3, int64): \[2 < 3 < 1\]

In \[107\]: s.min(), s.max()
Out\[107\]: (np.int64(2), np.int64(1))

Copy to clipboard

### Reordering[#](https://pandas.pydata.org/docs/user_guide/categorical.html#reordering "Link to this heading")

Reordering the categories is possible via the [`Categorical.reorder_categories()`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.reorder_categories.html#pandas.Categorical.reorder_categories "pandas.Categorical.reorder_categories")
 and the [`Categorical.set_categories()`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.set_categories.html#pandas.Categorical.set_categories "pandas.Categorical.set_categories")
 methods. For [`Categorical.reorder_categories()`](https://pandas.pydata.org/docs/reference/api/pandas.Categorical.reorder_categories.html#pandas.Categorical.reorder_categories "pandas.Categorical.reorder_categories")
, all old categories must be included in the new categories and no new categories are allowed. This will necessarily make the sort order the same as the categories order.

In \[108\]: s \= pd.Series(\[1, 2, 3, 1\], dtype\="category")

In \[109\]: s \= s.cat.reorder\_categories(\[2, 3, 1\], ordered\=True)

In \[110\]: s
Out\[110\]: 
0    1
1    2
2    3
3    1
dtype: category
Categories (3, int64): \[2 < 3 < 1\]

In \[111\]: s \= s.sort\_values()

In \[112\]: s
Out\[112\]: 
1    2
2    3
0    1
3    1
dtype: category
Categories (3, int64): \[2 < 3 < 1\]

In \[113\]: s.min(), s.max()
Out\[113\]: (np.int64(2), np.int64(1))

Copy to clipboard

Note

Note the difference between assigning new categories and reordering the categories: the first renames categories and therefore the individual values in the `Series`, but if the first position was sorted last, the renamed value will still be sorted last. Reordering means that the way values are sorted is different afterwards, but not that individual values in the `Series` are changed.

Note

If the `Categorical` is not ordered, [`Series.min()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min "pandas.Series.min")
 and [`Series.max()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max "pandas.Series.max")
 will raise `TypeError`. Numeric operations like `+`, `-`, `*`, `/` and operations based on them (e.g. [`Series.median()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html#pandas.Series.median "pandas.Series.median")
, which would need to compute the mean between two values if the length of an array is even) do not work and raise a `TypeError`.

### Multi column sorting[#](https://pandas.pydata.org/docs/user_guide/categorical.html#multi-column-sorting "Link to this heading")

A categorical dtyped column will participate in a multi-column sort in a similar manner to other columns. The ordering of the categorical is determined by the `categories` of that column.

In \[114\]: dfs \= pd.DataFrame(
   .....:    {
   .....:        "A": pd.Categorical(
   .....:            list("bbeebbaa"),
   .....:            categories\=\["e", "a", "b"\],
   .....:            ordered\=True,
   .....:        ),
   .....:        "B": \[1, 2, 1, 2, 2, 1, 2, 1\],
   .....:    }
   .....: )
   .....: 

In \[115\]: dfs.sort\_values(by\=\["A", "B"\])
Out\[115\]: 
   A  B
2  e  1
3  e  2
7  a  1
6  a  2
0  b  1
5  b  1
1  b  2
4  b  2

Copy to clipboard

Reordering the `categories` changes a future sort.

In \[116\]: dfs\["A"\] \= dfs\["A"\].cat.reorder\_categories(\["a", "b", "e"\])

In \[117\]: dfs.sort\_values(by\=\["A", "B"\])
Out\[117\]: 
   A  B
7  a  1
6  a  2
0  b  1
5  b  1
1  b  2
4  b  2
2  e  1
3  e  2

Copy to clipboard

Comparisons[#](https://pandas.pydata.org/docs/user_guide/categorical.html#comparisons "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Comparing categorical data with other objects is possible in three cases:

*   Comparing equality (`==` and `!=`) to a list-like object (list, Series, array, …) of the same length as the categorical data.
    
*   All comparisons (`==`, `!=`, `>`, `>=`, `<`, and `<=`) of categorical data to another categorical Series, when `ordered==True` and the `categories` are the same.
    
*   All comparisons of a categorical data to a scalar.
    

All other comparisons, especially “non-equality” comparisons of two categoricals with different categories or a categorical with any list-like object, will raise a `TypeError`.

Note

Any “non-equality” comparisons of categorical data with a `Series`, `np.array`, `list` or categorical data with different categories or ordering will raise a `TypeError` because custom categories ordering could be interpreted in two ways: one with taking into account the ordering and one without.

In \[118\]: cat \= pd.Series(\[1, 2, 3\]).astype(CategoricalDtype(\[3, 2, 1\], ordered\=True))

In \[119\]: cat\_base \= pd.Series(\[2, 2, 2\]).astype(CategoricalDtype(\[3, 2, 1\], ordered\=True))

In \[120\]: cat\_base2 \= pd.Series(\[2, 2, 2\]).astype(CategoricalDtype(ordered\=True))

In \[121\]: cat
Out\[121\]: 
0    1
1    2
2    3
dtype: category
Categories (3, int64): \[3 < 2 < 1\]

In \[122\]: cat\_base
Out\[122\]: 
0    2
1    2
2    2
dtype: category
Categories (3, int64): \[3 < 2 < 1\]

In \[123\]: cat\_base2
Out\[123\]: 
0    2
1    2
2    2
dtype: category
Categories (1, int64): \[2\]

Copy to clipboard

Comparing to a categorical with the same categories and ordering or to a scalar works:

In \[124\]: cat \> cat\_base
Out\[124\]: 
0     True
1    False
2    False
dtype: bool

In \[125\]: cat \> 2
Out\[125\]: 
0     True
1    False
2    False
dtype: bool

Copy to clipboard

Equality comparisons work with any list-like object of same length and scalars:

In \[126\]: cat \== cat\_base
Out\[126\]: 
0    False
1     True
2    False
dtype: bool

In \[127\]: cat \== np.array(\[1, 2, 3\])
Out\[127\]: 
0    True
1    True
2    True
dtype: bool

In \[128\]: cat \== 2
Out\[128\]: 
0    False
1     True
2    False
dtype: bool

Copy to clipboard

This doesn’t work because the categories are not the same:

In \[129\]: try:
   .....:    cat \> cat\_base2
   .....: except TypeError as e:
   .....:    print("TypeError:", str(e))
   .....: 
TypeError: Categoricals can only be compared if 'categories' are the same.

Copy to clipboard

If you want to do a “non-equality” comparison of a categorical series with a list-like object which is not categorical data, you need to be explicit and convert the categorical data back to the original values:

In \[130\]: base \= np.array(\[1, 2, 3\])

In \[131\]: try:
   .....:    cat \> base
   .....: except TypeError as e:
   .....:    print("TypeError:", str(e))
   .....: 
TypeError: Cannot compare a Categorical for op \_\_gt\_\_ with type <class 'numpy.ndarray'>.
If you want to compare values, use 'np.asarray(cat) <op> other'.

In \[132\]: np.asarray(cat) \> base
Out\[132\]: array(\[False, False, False\])

Copy to clipboard

When you compare two unordered categoricals with the same categories, the order is not considered:

In \[133\]: c1 \= pd.Categorical(\["a", "b"\], categories\=\["a", "b"\], ordered\=False)

In \[134\]: c2 \= pd.Categorical(\["a", "b"\], categories\=\["b", "a"\], ordered\=False)

In \[135\]: c1 \== c2
Out\[135\]: array(\[ True,  True\])

Copy to clipboard

Operations[#](https://pandas.pydata.org/docs/user_guide/categorical.html#operations "Link to this heading")

------------------------------------------------------------------------------------------------------------

Apart from [`Series.min()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min "pandas.Series.min")
, [`Series.max()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max "pandas.Series.max")
 and [`Series.mode()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html#pandas.Series.mode "pandas.Series.mode")
, the following operations are possible with categorical data:

`Series` methods like [`Series.value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts "pandas.Series.value_counts")
 will use all categories, even if some categories are not present in the data:

In \[136\]: s \= pd.Series(pd.Categorical(\["a", "b", "c", "c"\], categories\=\["c", "a", "b", "d"\]))

In \[137\]: s.value\_counts()
Out\[137\]: 
c    2
a    1
b    1
d    0
Name: count, dtype: int64

Copy to clipboard

`DataFrame` methods like [`DataFrame.sum()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html#pandas.DataFrame.sum "pandas.DataFrame.sum")
 also show “unused” categories when `observed=False`.

In \[138\]: columns \= pd.Categorical(
   .....:    \["One", "One", "Two"\], categories\=\["One", "Two", "Three"\], ordered\=True
   .....: )
   .....: 

In \[139\]: df \= pd.DataFrame(
   .....:    data\=\[\[1, 2, 3\], \[4, 5, 6\]\],
   .....:    columns\=pd.MultiIndex.from\_arrays(\[\["A", "B", "B"\], columns\]),
   .....: ).T
   .....: 

In \[140\]: df.groupby(level\=1, observed\=False).sum()
Out\[140\]: 
       0  1
One    3  9
Two    3  6
Three  0  0

Copy to clipboard

Groupby will also show “unused” categories when `observed=False`:

In \[141\]: cats \= pd.Categorical(
   .....:    \["a", "b", "b", "b", "c", "c", "c"\], categories\=\["a", "b", "c", "d"\]
   .....: )
   .....: 

In \[142\]: df \= pd.DataFrame({"cats": cats, "values": \[1, 2, 2, 2, 3, 4, 5\]})

In \[143\]: df.groupby("cats", observed\=False).mean()
Out\[143\]: 
      values
cats        
a        1.0
b        2.0
c        4.0
d        NaN

In \[144\]: cats2 \= pd.Categorical(\["a", "a", "b", "b"\], categories\=\["a", "b", "c"\])

In \[145\]: df2 \= pd.DataFrame(
   .....:    {
   .....:        "cats": cats2,
   .....:        "B": \["c", "d", "c", "d"\],
   .....:        "values": \[1, 2, 3, 4\],
   .....:    }
   .....: )
   .....: 

In \[146\]: df2.groupby(\["cats", "B"\], observed\=False).mean()
Out\[146\]: 
        values
cats B        
a    c     1.0
     d     2.0
b    c     3.0
     d     4.0
c    c     NaN
     d     NaN

Copy to clipboard

Pivot tables:

In \[147\]: raw\_cat \= pd.Categorical(\["a", "a", "b", "b"\], categories\=\["a", "b", "c"\])

In \[148\]: df \= pd.DataFrame({"A": raw\_cat, "B": \["c", "d", "c", "d"\], "values": \[1, 2, 3, 4\]})

In \[149\]: pd.pivot\_table(df, values\="values", index\=\["A", "B"\], observed\=False)
Out\[149\]: 
     values
A B        
a c     1.0
  d     2.0
b c     3.0
  d     4.0

Copy to clipboard

Data munging[#](https://pandas.pydata.org/docs/user_guide/categorical.html#data-munging "Link to this heading")

----------------------------------------------------------------------------------------------------------------

The optimized pandas data access methods `.loc`, `.iloc`, `.at`, and `.iat`, work as normal. The only difference is the return type (for getting) and that only values already in `categories` can be assigned.

### Getting[#](https://pandas.pydata.org/docs/user_guide/categorical.html#getting "Link to this heading")

If the slicing operation returns either a `DataFrame` or a column of type `Series`, the `category` dtype is preserved.

In \[150\]: idx \= pd.Index(\["h", "i", "j", "k", "l", "m", "n"\])

In \[151\]: cats \= pd.Series(\["a", "b", "b", "b", "c", "c", "c"\], dtype\="category", index\=idx)

In \[152\]: values \= \[1, 2, 2, 2, 3, 4, 5\]

In \[153\]: df \= pd.DataFrame({"cats": cats, "values": values}, index\=idx)

In \[154\]: df.iloc\[2:4, :\]
Out\[154\]: 
  cats  values
j    b       2
k    b       2

In \[155\]: df.iloc\[2:4, :\].dtypes
Out\[155\]: 
cats      category
values       int64
dtype: object

In \[156\]: df.loc\["h":"j", "cats"\]
Out\[156\]: 
h    a
i    b
j    b
Name: cats, dtype: category
Categories (3, str): \['a', 'b', 'c'\]

In \[157\]: df\[df\["cats"\] \== "b"\]
Out\[157\]: 
  cats  values
i    b       2
j    b       2
k    b       2

Copy to clipboard

An example where the category type is not preserved is if you take one single row: the resulting `Series` is of dtype `object`:

\# get the complete "h" row as a Series
In \[158\]: df.loc\["h", :\]
Out\[158\]: 
cats      a
values    1
Name: h, dtype: object

Copy to clipboard

Returning a single item from categorical data will also return the value, not a categorical of length “1”.

In \[159\]: df.iat\[0, 0\]
Out\[159\]: 'a'

In \[160\]: df\["cats"\] \= df\["cats"\].cat.rename\_categories(\["x", "y", "z"\])

In \[161\]: df.at\["h", "cats"\]  \# returns a string
Out\[161\]: 'x'

Copy to clipboard

Note

This is in contrast to R’s `factor` function, where `factor(c(1,2,3))[1]` returns a single value `factor`.

To get a single value `Series` of type `category`, you pass in a list with a single value:

In \[162\]: df.loc\[\["h"\], "cats"\]
Out\[162\]: 
h    x
Name: cats, dtype: category
Categories (3, str): \['x', 'y', 'z'\]

Copy to clipboard

### String and datetime accessors[#](https://pandas.pydata.org/docs/user_guide/categorical.html#string-and-datetime-accessors "Link to this heading")

The accessors `.dt` and `.str` will work if the `s.cat.categories` are of an appropriate type:

In \[163\]: str\_s \= pd.Series(list("aabb"))

In \[164\]: str\_cat \= str\_s.astype("category")

In \[165\]: str\_cat
Out\[165\]: 
0    a
1    a
2    b
3    b
dtype: category
Categories (2, str): \['a', 'b'\]

In \[166\]: str\_cat.str.contains("a")
Out\[166\]: 
0     True
1     True
2    False
3    False
dtype: bool

In \[167\]: date\_s \= pd.Series(pd.date\_range("1/1/2015", periods\=5))

In \[168\]: date\_cat \= date\_s.astype("category")

In \[169\]: date\_cat
Out\[169\]: 
0   2015-01-01
1   2015-01-02
2   2015-01-03
3   2015-01-04
4   2015-01-05
dtype: category
Categories (5, datetime64\[us\]): \[2015-01-01, 2015-01-02, 2015-01-03, 2015-01-04,\
                                 2015-01-05\]

In \[170\]: date\_cat.dt.day
Out\[170\]: 
0    1
1    2
2    3
3    4
4    5
dtype: int32

Copy to clipboard

Note

The returned `Series` (or `DataFrame`) is of the same type as if you used the `.str.<method>` / `.dt.<method>` on a `Series` of that type (and not of type `category`!).

That means, that the returned values from methods and properties on the accessors of a `Series` and the returned values from methods and properties on the accessors of this `Series` transformed to one of type `category` will be equal:

In \[171\]: ret\_s \= str\_s.str.contains("a")

In \[172\]: ret\_cat \= str\_cat.str.contains("a")

In \[173\]: ret\_s.dtype \== ret\_cat.dtype
Out\[173\]: True

In \[174\]: ret\_s \== ret\_cat
Out\[174\]: 
0    True
1    True
2    True
3    True
dtype: bool

Copy to clipboard

Note

The work is done on the `categories` and then a new `Series` is constructed. This has some performance implication if you have a `Series` of type string, where lots of elements are repeated (i.e. the number of unique elements in the `Series` is a lot smaller than the length of the `Series`). In this case it can be faster to convert the original `Series` to one of type `category` and use `.str.<method>` or `.dt.<property>` on that.

### Setting[#](https://pandas.pydata.org/docs/user_guide/categorical.html#setting "Link to this heading")

Setting values in a categorical column (or `Series`) works as long as the value is included in the `categories`:

In \[175\]: idx \= pd.Index(\["h", "i", "j", "k", "l", "m", "n"\])

In \[176\]: cats \= pd.Categorical(\["a", "a", "a", "a", "a", "a", "a"\], categories\=\["a", "b"\])

In \[177\]: values \= \[1, 1, 1, 1, 1, 1, 1\]

In \[178\]: df \= pd.DataFrame({"cats": cats, "values": values}, index\=idx)

In \[179\]: df.iloc\[2:4, :\] \= \[\["b", 2\], \["b", 2\]\]

In \[180\]: df
Out\[180\]: 
  cats  values
h    a       1
i    a       1
j    b       2
k    b       2
l    a       1
m    a       1
n    a       1

In \[181\]: try:
   .....:    df.iloc\[2:4, :\] \= \[\["c", 3\], \["c", 3\]\]
   .....: except TypeError as e:
   .....:    print("TypeError:", str(e))
   .....: 
TypeError: Cannot setitem on a Categorical with a new category, set the categories first

Copy to clipboard

Setting values by assigning categorical data will also check that the `categories` match:

In \[182\]: df.loc\["j":"k", "cats"\] \= pd.Categorical(\["a", "a"\], categories\=\["a", "b"\])

In \[183\]: df
Out\[183\]: 
  cats  values
h    a       1
i    a       1
j    a       2
k    a       2
l    a       1
m    a       1
n    a       1

In \[184\]: try:
   .....:    df.loc\["j":"k", "cats"\] \= pd.Categorical(\["b", "b"\], categories\=\["a", "b", "c"\])
   .....: except TypeError as e:
   .....:    print("TypeError:", str(e))
   .....: 
TypeError: Cannot set a Categorical with another, without identical categories

Copy to clipboard

Assigning a `Categorical` to parts of a column of other types will use the values:

In \[185\]: df \= pd.DataFrame({"a": \[1, 1, 1, 1, 1\], "b": \["a", "a", "a", "a", "a"\]})

In \[186\]: df.loc\[1:2, "a"\] \= pd.Categorical(\[2, 2\], categories\=\[2, 3\])

In \[187\]: df.loc\[2:3, "b"\] \= pd.Categorical(\["b", "b"\], categories\=\["a", "b"\])

In \[188\]: df
Out\[188\]: 
   a  b
0  1  a
1  2  a
2  2  b
3  1  b
4  1  a

In \[189\]: df.dtypes
Out\[189\]: 
a    int64
b      str
dtype: object

Copy to clipboard

Note

The examples above use `.loc` / `.iloc` to set values _within_ an existing categorical column, which preserves the `category` dtype. Assigning to a full column with `df["cats"] = value` instead **replaces** the column, so the dtype is inferred from `value` rather than kept. See [Column assignment vs. in-place setting](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-column-assignment-vs-in-place)
 for details.

### Merging / concatenation[#](https://pandas.pydata.org/docs/user_guide/categorical.html#merging-concatenation "Link to this heading")

By default, combining `Series` or `DataFrames` which contain the same categories results in `category` dtype, otherwise results will depend on the dtype of the underlying categories. Merges that result in non-categorical dtypes will likely have higher memory usage. Use `union_categories=True`, `.astype` or `union_categoricals` to ensure `category` results.

In \[190\]: from pandas.api.types import union\_categoricals

\# same categories
In \[191\]: s1 \= pd.Series(\["a", "b"\], dtype\="category")

In \[192\]: s2 \= pd.Series(\["a", "b", "a"\], dtype\="category")

In \[193\]: pd.concat(\[s1, s2\])
Out\[193\]: 
0    a
1    b
0    a
1    b
2    a
dtype: category
Categories (2, str): \['a', 'b'\]

\# different categories
In \[194\]: s3 \= pd.Series(\["b", "c"\], dtype\="category")

In \[195\]: pd.concat(\[s1, s3\])
Out\[195\]: 
0    a
1    b
0    b
1    c
dtype: str

\# Output dtype is inferred based on categories values
In \[196\]: int\_cats \= pd.Series(\[1, 2\], dtype\="category")

In \[197\]: float\_cats \= pd.Series(\[3.0, 4.0\], dtype\="category")

In \[198\]: pd.concat(\[int\_cats, float\_cats\])
Out\[198\]: 
0    1.0
1    2.0
0    3.0
1    4.0
dtype: float64

In \[199\]: pd.concat(\[s1, s3\], union\_categories\=True)
Out\[199\]: 
0    a
1    b
0    b
1    c
dtype: category
Categories (3, str): \['a', 'b', 'c'\]

In \[200\]: pd.concat(\[int\_cats, float\_cats\], union\_categories\=True)
Out\[200\]: 
0    1.0
1    2.0
0    3.0
1    4.0
dtype: category
Categories (4, float64): \[1.0, 2.0, 3.0, 4.0\]

In \[201\]: pd.concat(\[s1, s3\]).astype("category")
Out\[201\]: 
0    a
1    b
0    b
1    c
dtype: category
Categories (3, str): \['a', 'b', 'c'\]

In \[202\]: union\_categoricals(\[s1.array, s3.array\])
Out\[202\]: 
\['a', 'b', 'b', 'c'\]
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

The following table summarizes the results of merging `Categoricals`:

| arg1 | arg2 | identical | result |
| --- | --- | --- | --- |
| category | category | True | category |
| category (object) | category (object) | False | object (dtype is inferred) |
| category (int) | category (float) | False | float (dtype is inferred) |

### Unioning[#](https://pandas.pydata.org/docs/user_guide/categorical.html#unioning "Link to this heading")

If you want to combine categoricals that do not necessarily have the same categories, the [`union_categoricals()`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.union_categoricals.html#pandas.api.types.union_categoricals "pandas.api.types.union_categoricals")
 function will combine a list-like of categoricals. The new categories will be the union of the categories being combined.

In \[203\]: from pandas.api.types import union\_categoricals

In \[204\]: a \= pd.Categorical(\["b", "c"\])

In \[205\]: b \= pd.Categorical(\["a", "b"\])

In \[206\]: union\_categoricals(\[a, b\])
Out\[206\]: 
\['b', 'c', 'a', 'b'\]
Categories (3, str): \['b', 'c', 'a'\]

Copy to clipboard

By default, the resulting categories will be ordered as they appear in the data. If you want the categories to be lexsorted, use `sort_categories=True` argument.

In \[207\]: union\_categoricals(\[a, b\], sort\_categories\=True)
Out\[207\]: 
\['b', 'c', 'a', 'b'\]
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

`union_categoricals` also works with the “easy” case of combining two categoricals of the same categories and order information (e.g. what you could also `append` for).

In \[208\]: a \= pd.Categorical(\["a", "b"\], ordered\=True)

In \[209\]: b \= pd.Categorical(\["a", "b", "a"\], ordered\=True)

In \[210\]: union\_categoricals(\[a, b\])
Out\[210\]: 
\['a', 'b', 'a', 'b', 'a'\]
Categories (2, str): \['a' < 'b'\]

Copy to clipboard

The below raises `TypeError` because the categories are ordered and not identical.

In \[211\]: a \= pd.Categorical(\["a", "b"\], ordered\=True)

In \[212\]: b \= pd.Categorical(\["a", "b", "c"\], ordered\=True)

In \[213\]: union\_categoricals(\[a, b\])
\---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
Cell In\[213\], line 1
\----> 1 union\_categoricals(\[a, b\])

File ~/work/pandas/pandas/pandas/core/dtypes/concat.py:393, in union\_categoricals(to\_union, sort\_categories, ignore\_order)
    391     if all(c.ordered for c in to\_union):
    392         msg \= "to union ordered Categoricals, all categories must be the same"
\--> 393         raise TypeError(msg)
    394     raise TypeError("Categorical.ordered must be the same")
    396 if ignore\_order:

TypeError: to union ordered Categoricals, all categories must be the same

Copy to clipboard

Ordered categoricals with different categories or orderings can be combined by using the `ignore_order=True` argument.

In \[214\]: a \= pd.Categorical(\["a", "b", "c"\], ordered\=True)

In \[215\]: b \= pd.Categorical(\["c", "b", "a"\], ordered\=True)

In \[216\]: union\_categoricals(\[a, b\], ignore\_order\=True)
Out\[216\]: 
\['a', 'b', 'c', 'c', 'b', 'a'\]
Categories (3, str): \['a', 'b', 'c'\]

Copy to clipboard

[`union_categoricals()`](https://pandas.pydata.org/docs/reference/api/pandas.api.types.union_categoricals.html#pandas.api.types.union_categoricals "pandas.api.types.union_categoricals")
 also works with a `CategoricalIndex`, or `Series` containing categorical data, but note that the resulting array will always be a plain `Categorical`:

In \[217\]: a \= pd.Series(\["b", "c"\], dtype\="category")

In \[218\]: b \= pd.Series(\["a", "b"\], dtype\="category")

In \[219\]: union\_categoricals(\[a, b\])
Out\[219\]: 
\['b', 'c', 'a', 'b'\]
Categories (3, str): \['b', 'c', 'a'\]

Copy to clipboard

Note

`union_categoricals` may recode the integer codes for categories when combining categoricals. This is likely what you want, but if you are relying on the exact numbering of the categories, be aware.

In \[220\]: c1 \= pd.Categorical(\["b", "c"\])

In \[221\]: c2 \= pd.Categorical(\["a", "b"\])

In \[222\]: c1
Out\[222\]: 
\['b', 'c'\]
Categories (2, str): \['b', 'c'\]

\# "b" is coded to 0
In \[223\]: c1.codes
Out\[223\]: array(\[0, 1\], dtype=int8)

In \[224\]: c2
Out\[224\]: 
\['a', 'b'\]
Categories (2, str): \['a', 'b'\]

\# "b" is coded to 1
In \[225\]: c2.codes
Out\[225\]: array(\[0, 1\], dtype=int8)

In \[226\]: c \= union\_categoricals(\[c1, c2\])

In \[227\]: c
Out\[227\]: 
\['b', 'c', 'a', 'b'\]
Categories (3, str): \['b', 'c', 'a'\]

\# "b" is coded to 0 throughout, same as c1, different from c2
In \[228\]: c.codes
Out\[228\]: array(\[0, 1, 2, 0\], dtype=int8)

Copy to clipboard

Getting data in/out[#](https://pandas.pydata.org/docs/user_guide/categorical.html#getting-data-in-out "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

You can write data that contains `category` dtypes to a `HDFStore`. See [here](https://pandas.pydata.org/docs/user_guide/io.html#io-hdf5-categorical)
 for an example and caveats.

It is also possible to write data to and reading data from _Stata_ format files. See [here](https://pandas.pydata.org/docs/user_guide/io.html#io-stata-categorical)
 for an example and caveats.

Writing to a CSV file will convert the data, effectively removing any information about the categorical (categories and ordering). So if you read back the CSV file you have to convert the relevant columns back to `category` and assign the right categories and categories ordering.

In \[229\]: import io

In \[230\]: s \= pd.Series(pd.Categorical(\["a", "b", "b", "a", "a", "d"\]))

\# rename the categories
In \[231\]: s \= s.cat.rename\_categories(\["very good", "good", "bad"\])

\# reorder the categories and add missing categories
In \[232\]: s \= s.cat.set\_categories(\["very bad", "bad", "medium", "good", "very good"\])

In \[233\]: df \= pd.DataFrame({"cats": s, "vals": \[1, 2, 3, 4, 5, 6\]})

In \[234\]: csv \= io.StringIO()

In \[235\]: df.to\_csv(csv)

In \[236\]: df2 \= pd.read\_csv(io.StringIO(csv.getvalue()))

In \[237\]: df2.dtypes
Out\[237\]: 
Unnamed: 0    int64
cats            str
vals          int64
dtype: object

In \[238\]: df2\["cats"\]
Out\[238\]: 
0    very good
1         good
2         good
3    very good
4    very good
5          bad
Name: cats, dtype: str

\# Redo the category
In \[239\]: df2\["cats"\] \= df2\["cats"\].astype("category")

In \[240\]: df2\["cats"\] \= df2\["cats"\].cat.set\_categories(
   .....:    \["very bad", "bad", "medium", "good", "very good"\]
   .....: )
   .....: 

In \[241\]: df2.dtypes
Out\[241\]: 
Unnamed: 0       int64
cats          category
vals             int64
dtype: object

In \[242\]: df2\["cats"\]
Out\[242\]: 
0    very good
1         good
2         good
3    very good
4    very good
5          bad
Name: cats, dtype: category
Categories (5, str): \['very bad', 'bad', 'medium', 'good', 'very good'\]

Copy to clipboard

The same holds for writing to a SQL database with `to_sql`.

Missing data[#](https://pandas.pydata.org/docs/user_guide/categorical.html#missing-data "Link to this heading")

----------------------------------------------------------------------------------------------------------------

pandas primarily uses the value `np.nan` to represent missing data. It is by default not included in computations. See [Working with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data)
.

Missing values should **not** be included in the Categorical’s `categories`, only in the `values`. Instead, it is understood that NaN is different, and is always a possibility. When working with the Categorical’s `codes`, missing values will always have a code of `-1`.

In \[243\]: s \= pd.Series(\["a", "b", np.nan, "a"\], dtype\="category")

\# only two categories
In \[244\]: s
Out\[244\]: 
0      a
1      b
2    NaN
3      a
dtype: category
Categories (2, str): \['a', 'b'\]

In \[245\]: s.cat.codes
Out\[245\]: 
0    0
1    1
2   -1
3    0
dtype: int8

Copy to clipboard

Methods for working with missing data, e.g. [`isna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html#pandas.Series.isna "pandas.Series.isna")
, [`fillna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html#pandas.Series.fillna "pandas.Series.fillna")
, [`dropna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html#pandas.Series.dropna "pandas.Series.dropna")
, all work normally:

In \[246\]: s \= pd.Series(\["a", "b", np.nan\], dtype\="category")

In \[247\]: s
Out\[247\]: 
0      a
1      b
2    NaN
dtype: category
Categories (2, str): \['a', 'b'\]

In \[248\]: pd.isna(s)
Out\[248\]: 
0    False
1    False
2     True
dtype: bool

In \[249\]: s.fillna("a")
Out\[249\]: 
0    a
1    b
2    a
dtype: category
Categories (2, str): \['a', 'b'\]

Copy to clipboard

Differences to R’s `factor`[#](https://pandas.pydata.org/docs/user_guide/categorical.html#differences-to-r-s-factor "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

The following differences to R’s factor functions can be observed:

*   R’s `levels` are named `categories`.
    
*   R’s `levels` are always of type string, while `categories` in pandas can be of any dtype.
    
*   It’s not possible to specify labels at creation time. Use `s.cat.rename_categories(new_labels)` afterwards.
    
*   In contrast to R’s `factor` function, using categorical data as the sole input to create a new categorical series will _not_ remove unused categories but create a new categorical series which is equal to the passed in one!
    
*   R allows for missing values to be included in its `levels` (pandas’ `categories`). pandas does not allow `NaN` categories, but missing values can still be in the `values`.
    

Gotchas[#](https://pandas.pydata.org/docs/user_guide/categorical.html#gotchas "Link to this heading")

------------------------------------------------------------------------------------------------------

### Memory usage[#](https://pandas.pydata.org/docs/user_guide/categorical.html#memory-usage "Link to this heading")

The memory usage of a `Categorical` is proportional to the number _and size_ of categories plus the length of the data. In contrast, an `object` dtype is proportional to the size of the objects times the length of the data.

In \[250\]: s \= pd.Series(\["foo", "bar"\] \* 1000, dtype\="object")

\# object dtype
In \[251\]: s.memory\_usage(deep\=True)
Out\[251\]: 104132

\# category dtype
In \[252\]: s.astype("category").memory\_usage(deep\=True)
Out\[252\]: 2155

Copy to clipboard

Note

If the number of categories approaches the length of the data, the `Categorical` will use nearly the same or more memory than an equivalent `object` dtype representation.

In \[253\]: s \= pd.Series(\["foo%04d" % i for i in range(2000)\], dtype\="object")

\# object dtype
In \[254\]: s.memory\_usage(deep\=True)
Out\[254\]: 112132

\# category dtype
In \[255\]: s.astype("category").memory\_usage(deep\=True)
Out\[255\]: 34382

Copy to clipboard

### `Categorical` is not a `numpy` array[#](https://pandas.pydata.org/docs/user_guide/categorical.html#categorical-is-not-a-numpy-array "Link to this heading")

Currently, categorical data and the underlying `Categorical` is implemented as a Python object and not as a low-level NumPy array dtype. This leads to some problems.

NumPy itself doesn’t know about the new `dtype`:

In \[256\]: try:
   .....:    np.dtype("category")
   .....: except TypeError as e:
   .....:    print("TypeError:", str(e))
   .....: 
TypeError: data type 'category' not understood

In \[257\]: dtype \= pd.Categorical(\["a"\]).dtype

In \[258\]: try:
   .....:    np.dtype(dtype)
   .....: except TypeError as e:
   .....:    print("TypeError:", str(e))
   .....: 
TypeError: Cannot interpret 'CategoricalDtype(categories=\['a'\], ordered=False, categories\_dtype=str)' as a data type

Copy to clipboard

Dtype comparisons work:

In \[259\]: dtype \== np.str\_
Out\[259\]: False

In \[260\]: np.str\_ \== dtype
Out\[260\]: False

Copy to clipboard

To check if a Series contains Categorical data, use `hasattr(s, 'cat')`:

In \[261\]: hasattr(pd.Series(\["a"\], dtype\="category"), "cat")
Out\[261\]: True

In \[262\]: hasattr(pd.Series(\["a"\]), "cat")
Out\[262\]: False

Copy to clipboard

Using NumPy functions on a `Series` of type `category` should not work as `Categoricals` are not numeric data (even in the case that `.categories` is numeric).

In \[263\]: s \= pd.Series(pd.Categorical(\[1, 2, 3, 4\]))

In \[264\]: try:
   .....:    np.sum(s)
   .....: except TypeError as e:
   .....:    print("TypeError:", str(e))
   .....: 
TypeError: 'Categorical' with dtype category does not support operation 'sum'

Copy to clipboard

Note

If such a function works, please file a bug at [pandas-dev/pandas](https://github.com/pandas-dev/pandas)
!

### dtype in apply[#](https://pandas.pydata.org/docs/user_guide/categorical.html#dtype-in-apply "Link to this heading")

pandas currently does not preserve the dtype in apply functions: If you apply along rows you get a `Series` of `object` `dtype` (same as getting a row -> getting one element will return a basic type) and applying along columns will also convert to object. `NaN` values are unaffected. You can use `fillna` to handle missing values before applying a function.

In \[265\]: df \= pd.DataFrame(
   .....:    {
   .....:        "a": \[1, 2, 3, 4\],
   .....:        "b": \["a", "b", "c", "d"\],
   .....:        "cats": pd.Categorical(\[1, 2, 3, 2\]),
   .....:    }
   .....: )
   .....: 

In \[266\]: df.apply(lambda row: type(row\["cats"\]), axis\=1)
Out\[266\]: 
0    <class 'int'>
1    <class 'int'>
2    <class 'int'>
3    <class 'int'>
dtype: object

In \[267\]: df.apply(lambda col: col.dtype, axis\=0)
Out\[267\]: 
a          int64
b            str
cats    category
dtype: object

Copy to clipboard

### Categorical index[#](https://pandas.pydata.org/docs/user_guide/categorical.html#categorical-index "Link to this heading")

`CategoricalIndex` is a type of index that is useful for supporting indexing with duplicates. This is a container around a `Categorical` and allows efficient indexing and storage of an index with a large number of duplicated elements. See the [advanced indexing docs](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced-categoricalindex)
 for a more detailed explanation.

Setting the index will create a `CategoricalIndex`:

In \[268\]: cats \= pd.Categorical(\[1, 2, 3, 4\], categories\=\[4, 2, 3, 1\])

In \[269\]: strings \= \["a", "b", "c", "d"\]

In \[270\]: values \= \[4, 2, 3, 1\]

In \[271\]: df \= pd.DataFrame({"strings": strings, "values": values}, index\=cats)

In \[272\]: df.index
Out\[272\]: 
CategoricalIndex(\[1, 2, 3, 4\], categories=\[4, 2, 3, 1\], ordered=False,
                 dtype='category')

\# This now sorts by the categories order
In \[273\]: df.sort\_index()
Out\[273\]: 
  strings  values
4       d       1
2       b       2
3       c       3
1       a       4

Copy to clipboard

On this page