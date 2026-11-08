[Skip to main content](https://pandas.pydata.org/docs/user_guide/boolean.html#main-content)

Back to top Ctrl+K

Choose version

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Nullable Boolean data type[#](https://pandas.pydata.org/docs/user_guide/boolean.html#nullable-boolean-data-type "Link to this heading")

========================================================================================================================================

Indexing with NA values[#](https://pandas.pydata.org/docs/user_guide/boolean.html#indexing-with-na-values "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

pandas allows indexing with `NA` values in a boolean array, which are treated as `False`.

In \[1\]: s \= pd.Series(\[1, 2, 3\])

In \[2\]: mask \= pd.array(\[True, False, pd.NA\], dtype\="boolean")

In \[3\]: s\[mask\]
Out\[3\]: 
0    1
dtype: int64

Copy to clipboard

If you would prefer to keep the `NA` values you can manually fill them with `fillna(True)`.

In \[4\]: s\[mask.fillna(True)\]
Out\[4\]: 
0    1
2    3
dtype: int64

Copy to clipboard

If you create a column of `NA` values (for example to fill them later) with `df['new_col'] = pd.NA`, the `dtype` would be set to `object` in the new column. The performance on this column will be worse than with the appropriate type. It’s better to use `df['new_col'] = pd.Series(pd.NA, dtype="boolean")` (or another `dtype` that supports `NA`).

In \[5\]: df \= pd.DataFrame()

In \[6\]: df\['objects'\] \= pd.NA

In \[7\]: df.dtypes
Out\[7\]: 
objects    object
dtype: object

Copy to clipboard

Kleene logical operations[#](https://pandas.pydata.org/docs/user_guide/boolean.html#kleene-logical-operations "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

[`arrays.BooleanArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.BooleanArray.html#pandas.arrays.BooleanArray "pandas.arrays.BooleanArray")
 implements [Kleene Logic](https://en.wikipedia.org/wiki/Three-valued_logic#Kleene_and_Priest_logics)
 (sometimes called three-value logic) for logical operations like `&` (and), `|` (or) and `^` (exclusive-or).

This table demonstrates the results for every combination. These operations are symmetrical, so flipping the left- and right-hand side makes no difference in the result.

| Expression | Result |
| --- | --- |
| `True & True` | `True` |
| `True & False` | `False` |
| `True & NA` | `NA` |
| `False & False` | `False` |
| `False & NA` | `False` |
| `NA & NA` | `NA` |
| `True \| True` | `True` |
| `True \| False` | `True` |
| `True \| NA` | `True` |
| `False \| False` | `False` |
| `False \| NA` | `NA` |
| `NA \| NA` | `NA` |
| `True ^ True` | `False` |
| `True ^ False` | `True` |
| `True ^ NA` | `NA` |
| `False ^ False` | `False` |
| `False ^ NA` | `NA` |
| `NA ^ NA` | `NA` |

When an `NA` is present in an operation, the output value is `NA` only if the result cannot be determined solely based on the other input. For example, `True | NA` is `True`, because both `True | True` and `True | False` are `True`. In that case, we don’t actually need to consider the value of the `NA`.

On the other hand, `True & NA` is `NA`. The result depends on whether the `NA` really is `True` or `False`, since `True & True` is `True`, but `True & False` is `False`, so we can’t determine the output.

This differs from how `np.nan` behaves in logical operations. pandas treated `np.nan` is _always false in the output_.

In `or`

In \[8\]: pd.Series(\[True, False, np.nan\], dtype\="object") | True
Out\[8\]: 
0     True
1     True
2    False
dtype: bool

In \[9\]: pd.Series(\[True, False, np.nan\], dtype\="boolean") | True
Out\[9\]: 
0    True
1    True
2    True
dtype: boolean

Copy to clipboard

In `and`

In \[10\]: pd.Series(\[True, False, np.nan\], dtype\="object") & True
Out\[10\]: 
0     True
1    False
2    False
dtype: bool

In \[11\]: pd.Series(\[True, False, np.nan\], dtype\="boolean") & True
Out\[11\]: 
0     True
1    False
2     <NA>
dtype: boolean

Copy to clipboard

On this page