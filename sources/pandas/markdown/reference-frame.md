[Skip to main content](https://pandas.pydata.org/docs/reference/frame.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/frame.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/frame.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/frame.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/frame.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/frame.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/frame.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/frame.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/frame.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/frame.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/frame.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/frame.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/frame.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/frame.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

DataFrame[#](https://pandas.pydata.org/docs/reference/frame.html#dataframe "Link to this heading")

===================================================================================================

Note

For an introduction to using DataFrames, see [Essential basic functionality](https://pandas.pydata.org/docs/user_guide/basics.html#basics)
.

Constructor[#](https://pandas.pydata.org/docs/reference/frame.html#constructor "Link to this heading")

-------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")<br>(\[data, index, columns, dtype, copy\]) | Two-dimensional, size-mutable, potentially heterogeneous tabular data. |

Attributes and underlying data[#](https://pandas.pydata.org/docs/reference/frame.html#attributes-and-underlying-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

**Axes**

|     |     |
| --- | --- |
| [`DataFrame.index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html#pandas.DataFrame.index "pandas.DataFrame.index") | The index (row labels) of the DataFrame. |
| [`DataFrame.columns`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html#pandas.DataFrame.columns "pandas.DataFrame.columns") | The column labels of the DataFrame. |

|     |     |
| --- | --- |
| [`DataFrame.dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html#pandas.DataFrame.dtypes "pandas.DataFrame.dtypes") | Return the dtypes in the DataFrame. |
| [`DataFrame.info`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info")<br>(\[verbose, buf, max\_cols, ...\]) | Print a concise summary of a DataFrame. |
| [`DataFrame.select_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes "pandas.DataFrame.select_dtypes")<br>(\[include, exclude\]) | Return a subset of the DataFrame's columns based on the column dtypes. |
| [`DataFrame.values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html#pandas.DataFrame.values "pandas.DataFrame.values") | Return a Numpy representation of the DataFrame. |
| [`DataFrame.axes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.axes.html#pandas.DataFrame.axes "pandas.DataFrame.axes") | Return a list representing the axes of the DataFrame. |
| [`DataFrame.ndim`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ndim.html#pandas.DataFrame.ndim "pandas.DataFrame.ndim") | Return an int representing the number of axes / array dimensions. |
| [`DataFrame.size`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.size.html#pandas.DataFrame.size "pandas.DataFrame.size") | Return an int representing the number of elements in this object. |
| [`DataFrame.shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html#pandas.DataFrame.shape "pandas.DataFrame.shape") | Return a tuple representing the dimensionality of the DataFrame. |
| [`DataFrame.memory_usage`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html#pandas.DataFrame.memory_usage "pandas.DataFrame.memory_usage")<br>(\[index, deep\]) | Return the memory usage of each column in bytes. |
| [`DataFrame.empty`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.empty.html#pandas.DataFrame.empty "pandas.DataFrame.empty") | Indicator whether Series/DataFrame is empty. |
| [`DataFrame.set_flags`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_flags.html#pandas.DataFrame.set_flags "pandas.DataFrame.set_flags")<br>(\*\[, copy, ...\]) | Return a new object with updated flags. |

Conversion[#](https://pandas.pydata.org/docs/reference/frame.html#conversion "Link to this heading")

-----------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.astype`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas.DataFrame.astype "pandas.DataFrame.astype")<br>(dtype\[, copy, errors\]) | Cast a pandas object to a specified dtype `dtype`. |
| [`DataFrame.convert_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.convert_dtypes.html#pandas.DataFrame.convert_dtypes "pandas.DataFrame.convert_dtypes")<br>(\[infer\_objects, ...\]) | Convert columns from numpy dtypes to the best dtypes that support `pd.NA`. |
| [`DataFrame.infer_objects`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.infer_objects.html#pandas.DataFrame.infer_objects "pandas.DataFrame.infer_objects")<br>(\[copy\]) | Attempt to infer better dtypes for object columns. |
| [`DataFrame.copy`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html#pandas.DataFrame.copy "pandas.DataFrame.copy")<br>(\[deep\]) | Make a copy of this object's indices and data. |
| [`DataFrame.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy")<br>(\[dtype, copy, na\_value\]) | Convert the DataFrame to a NumPy array. |

Indexing, iteration[#](https://pandas.pydata.org/docs/reference/frame.html#indexing-iteration "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.head`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head "pandas.DataFrame.head")<br>(\[n\]) | Return the first n rows. |
| [`DataFrame.at`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at "pandas.DataFrame.at") | Access a single value for a row/column label pair. |
| [`DataFrame.iat`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat "pandas.DataFrame.iat") | Access a single value for a row/column pair by integer position. |
| [`DataFrame.loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc") | Access a group of rows and columns by label(s) or a boolean array. |
| [`DataFrame.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc") | Purely integer-location based indexing for selection by position. |
| [`DataFrame.insert`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html#pandas.DataFrame.insert "pandas.DataFrame.insert")<br>(loc, column, value\[, ...\]) | Insert column into DataFrame at specified location. |
| [`DataFrame.__iter__`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__iter__.html#pandas.DataFrame.__iter__ "pandas.DataFrame.__iter__")<br>() | Iterate over info axis. |
| [`DataFrame.items`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.items.html#pandas.DataFrame.items "pandas.DataFrame.items")<br>() | Iterate over (column name, Series) pairs. |
| [`DataFrame.keys`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.keys.html#pandas.DataFrame.keys "pandas.DataFrame.keys")<br>() | Get the 'info axis' (see Indexing for more). |
| [`DataFrame.iterrows`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html#pandas.DataFrame.iterrows "pandas.DataFrame.iterrows")<br>() | Iterate over DataFrame rows as (index, Series) pairs. |
| [`DataFrame.itertuples`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html#pandas.DataFrame.itertuples "pandas.DataFrame.itertuples")<br>(\[index, name\]) | Iterate over DataFrame rows as namedtuples. |
| [`DataFrame.pop`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pop.html#pandas.DataFrame.pop "pandas.DataFrame.pop")<br>(item) | Return item and drop it from DataFrame. |
| [`DataFrame.tail`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail "pandas.DataFrame.tail")<br>(\[n\]) | Return the last n rows. |
| [`DataFrame.xs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.xs.html#pandas.DataFrame.xs "pandas.DataFrame.xs")<br>(key\[, axis, level, drop\_level\]) | Return cross-section from the Series/DataFrame. |
| [`DataFrame.get`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.get.html#pandas.DataFrame.get "pandas.DataFrame.get")<br>(key\[, default\]) | Get item from object for given key (ex: DataFrame column). |
| [`DataFrame.isin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html#pandas.DataFrame.isin "pandas.DataFrame.isin")<br>(values) | Whether each element in the DataFrame is contained in values. |
| [`DataFrame.where`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where "pandas.DataFrame.where")<br>(cond\[, other, inplace, ...\]) | Replace values where the condition is False. |
| [`DataFrame.mask`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html#pandas.DataFrame.mask "pandas.DataFrame.mask")<br>(cond\[, other, inplace, axis, ...\]) | Replace values where the condition is True. |
| [`DataFrame.query`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query")<br>(expr, \*\[, parser, engine, ...\]) | Query the columns of a DataFrame with a boolean expression. |
| [`DataFrame.isetitem`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isetitem.html#pandas.DataFrame.isetitem "pandas.DataFrame.isetitem")<br>(loc, value) | Set the given value in the column with position loc. |

For more information on `.at`, `.iat`, `.loc`, and `.iloc`, see the [indexing documentation](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing)
.

Binary operator functions[#](https://pandas.pydata.org/docs/reference/frame.html#binary-operator-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.__add__`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__add__.html#pandas.DataFrame.__add__ "pandas.DataFrame.__add__")<br>(other) | Get Addition of DataFrame and other, column-wise. |
| [`DataFrame.add`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add.html#pandas.DataFrame.add "pandas.DataFrame.add")<br>(other\[, axis, level, fill\_value\]) | Get Addition of dataframe and other, element-wise (binary operator add). |
| [`DataFrame.sub`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sub.html#pandas.DataFrame.sub "pandas.DataFrame.sub")<br>(other\[, axis, level, fill\_value\]) | Get Subtraction of dataframe and other, element-wise (binary operator sub). |
| [`DataFrame.mul`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mul.html#pandas.DataFrame.mul "pandas.DataFrame.mul")<br>(other\[, axis, level, fill\_value\]) | Get Multiplication of dataframe and other, element-wise (binary operator mul). |
| [`DataFrame.div`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.div.html#pandas.DataFrame.div "pandas.DataFrame.div")<br>(other\[, axis, level, fill\_value\]) | Get Floating division of dataframe and other, element-wise (binary operator truediv). |
| [`DataFrame.truediv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truediv.html#pandas.DataFrame.truediv "pandas.DataFrame.truediv")<br>(other\[, axis, level, ...\]) | Get Floating division of dataframe and other, element-wise (binary operator truediv). |
| [`DataFrame.floordiv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.floordiv.html#pandas.DataFrame.floordiv "pandas.DataFrame.floordiv")<br>(other\[, axis, level, ...\]) | Get Integer division of dataframe and other, element-wise (binary operator floordiv). |
| [`DataFrame.mod`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mod.html#pandas.DataFrame.mod "pandas.DataFrame.mod")<br>(other\[, axis, level, fill\_value\]) | Get Modulo of dataframe and other, element-wise (binary operator mod). |
| [`DataFrame.pow`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pow.html#pandas.DataFrame.pow "pandas.DataFrame.pow")<br>(other\[, axis, level, fill\_value\]) | Get Exponential power of dataframe and other, element-wise (binary operator pow). |
| [`DataFrame.dot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dot.html#pandas.DataFrame.dot "pandas.DataFrame.dot")<br>(other) | Compute the matrix multiplication between the DataFrame and other. |
| [`DataFrame.radd`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.radd.html#pandas.DataFrame.radd "pandas.DataFrame.radd")<br>(other\[, axis, level, fill\_value\]) | Get Addition of dataframe and other, element-wise (binary operator radd). |
| [`DataFrame.rsub`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rsub.html#pandas.DataFrame.rsub "pandas.DataFrame.rsub")<br>(other\[, axis, level, fill\_value\]) | Get Subtraction of dataframe and other, element-wise (binary operator rsub). |
| [`DataFrame.rmul`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rmul.html#pandas.DataFrame.rmul "pandas.DataFrame.rmul")<br>(other\[, axis, level, fill\_value\]) | Get Multiplication of dataframe and other, element-wise (binary operator rmul). |
| [`DataFrame.rdiv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rdiv.html#pandas.DataFrame.rdiv "pandas.DataFrame.rdiv")<br>(other\[, axis, level, fill\_value\]) | Get Floating division of dataframe and other, element-wise (binary operator rtruediv). |
| [`DataFrame.rtruediv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rtruediv.html#pandas.DataFrame.rtruediv "pandas.DataFrame.rtruediv")<br>(other\[, axis, level, ...\]) | Get Floating division of dataframe and other, element-wise (binary operator rtruediv). |
| [`DataFrame.rfloordiv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rfloordiv.html#pandas.DataFrame.rfloordiv "pandas.DataFrame.rfloordiv")<br>(other\[, axis, level, ...\]) | Get Integer division of dataframe and other, element-wise (binary operator rfloordiv). |
| [`DataFrame.rmod`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rmod.html#pandas.DataFrame.rmod "pandas.DataFrame.rmod")<br>(other\[, axis, level, fill\_value\]) | Get Modulo of dataframe and other, element-wise (binary operator rmod). |
| [`DataFrame.rpow`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rpow.html#pandas.DataFrame.rpow "pandas.DataFrame.rpow")<br>(other\[, axis, level, fill\_value\]) | Get Exponential power of dataframe and other, element-wise (binary operator rpow). |
| [`DataFrame.lt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.lt.html#pandas.DataFrame.lt "pandas.DataFrame.lt")<br>(other\[, axis, level\]) | Get Less than of dataframe and other, element-wise (binary operator lt). |
| [`DataFrame.gt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.gt.html#pandas.DataFrame.gt "pandas.DataFrame.gt")<br>(other\[, axis, level\]) | Get Greater than of dataframe and other, element-wise (binary operator gt). |
| [`DataFrame.le`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.le.html#pandas.DataFrame.le "pandas.DataFrame.le")<br>(other\[, axis, level\]) | Get Less than or equal to of dataframe and other, element-wise (binary operator le). |
| [`DataFrame.ge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ge.html#pandas.DataFrame.ge "pandas.DataFrame.ge")<br>(other\[, axis, level\]) | Get Greater than or equal to of dataframe and other, element-wise (binary operator ge). |
| [`DataFrame.ne`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ne.html#pandas.DataFrame.ne "pandas.DataFrame.ne")<br>(other\[, axis, level\]) | Get Not equal to of dataframe and other, element-wise (binary operator ne). |
| [`DataFrame.eq`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eq.html#pandas.DataFrame.eq "pandas.DataFrame.eq")<br>(other\[, axis, level\]) | Get Equal to of dataframe and other, element-wise (binary operator eq). |
| [`DataFrame.combine`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine.html#pandas.DataFrame.combine "pandas.DataFrame.combine")<br>(other, func\[, fill\_value, ...\]) | Perform column-wise combine with another DataFrame. |
| [`DataFrame.combine_first`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first "pandas.DataFrame.combine_first")<br>(other) | Update null elements with value in the same location in other. |

Unary operator functions[#](https://pandas.pydata.org/docs/reference/frame.html#unary-operator-functions "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.__invert__`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__invert__.html#pandas.DataFrame.__invert__ "pandas.DataFrame.__invert__")<br>() | Return the bitwise inverse of the Series/DataFrame, element-wise. |

Function application, GroupBy & window[#](https://pandas.pydata.org/docs/reference/frame.html#function-application-groupby-window "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.apply`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")<br>(func\[, axis, raw, ...\]) | Apply a function along an axis of the DataFrame. |
| [`DataFrame.map`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas.DataFrame.map "pandas.DataFrame.map")<br>(func\[, na\_action\]) | Apply a function to a Dataframe elementwise. |
| [`DataFrame.pipe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe "pandas.DataFrame.pipe")<br>(func, \*args, \*\*kwargs) | Apply chainable functions that expect Series or DataFrames. |
| [`DataFrame.agg`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg "pandas.DataFrame.agg")<br>(\[func, axis\]) | Aggregate using one or more operations over the specified axis. |
| [`DataFrame.aggregate`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.aggregate.html#pandas.DataFrame.aggregate "pandas.DataFrame.aggregate")<br>(\[func, axis\]) | Aggregate using one or more operations over the specified axis. |
| [`DataFrame.transform`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html#pandas.DataFrame.transform "pandas.DataFrame.transform")<br>(func\[, axis\]) | Call `func` on self producing a DataFrame with the same axis shape as self. |
| [`DataFrame.groupby`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")<br>(\[by, level, as\_index, ...\]) | Group DataFrame using a mapper or by a Series of columns. |
| [`DataFrame.rolling`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling "pandas.DataFrame.rolling")<br>(window\[, min\_periods, ...\]) | Provide rolling window calculations. |
| [`DataFrame.expanding`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.expanding.html#pandas.DataFrame.expanding "pandas.DataFrame.expanding")<br>(\[min\_periods, method\]) | Provide expanding window calculations. |
| [`DataFrame.ewm`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ewm.html#pandas.DataFrame.ewm "pandas.DataFrame.ewm")<br>(\[com, span, halflife, alpha, ...\]) | Provide exponentially weighted (EW) calculations. |

Computations / descriptive stats[#](https://pandas.pydata.org/docs/reference/frame.html#computations-descriptive-stats "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.abs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.abs.html#pandas.DataFrame.abs "pandas.DataFrame.abs")<br>() | Return a Series/DataFrame with absolute numeric value of each element. |
| [`DataFrame.all`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.all.html#pandas.DataFrame.all "pandas.DataFrame.all")<br>(\*\[, axis, bool\_only, skipna\]) | Return whether all elements are True, potentially over an axis. |
| [`DataFrame.any`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html#pandas.DataFrame.any "pandas.DataFrame.any")<br>(\*\[, axis, bool\_only, skipna\]) | Return whether any element is True, potentially over an axis. |
| [`DataFrame.clip`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.clip.html#pandas.DataFrame.clip "pandas.DataFrame.clip")<br>(\[lower, upper, axis, inplace\]) | Trim values at input threshold(s). |
| [`DataFrame.corr`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#pandas.DataFrame.corr "pandas.DataFrame.corr")<br>(\[method, min\_periods, ...\]) | Compute pairwise correlation of columns, excluding NA/null values. |
| [`DataFrame.corrwith`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corrwith.html#pandas.DataFrame.corrwith "pandas.DataFrame.corrwith")<br>(other\[, axis, drop, ...\]) | Compute pairwise correlation. |
| [`DataFrame.count`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html#pandas.DataFrame.count "pandas.DataFrame.count")<br>(\[axis, numeric\_only\]) | Count non-NA cells for each column or row. |
| [`DataFrame.cov`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cov.html#pandas.DataFrame.cov "pandas.DataFrame.cov")<br>(\[min\_periods, ddof, numeric\_only\]) | Compute pairwise covariance of columns, excluding NA/null values. |
| [`DataFrame.cummax`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cummax.html#pandas.DataFrame.cummax "pandas.DataFrame.cummax")<br>(\[axis, skipna, numeric\_only\]) | Return cumulative maximum over a DataFrame or Series axis. |
| [`DataFrame.cummin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cummin.html#pandas.DataFrame.cummin "pandas.DataFrame.cummin")<br>(\[axis, skipna, numeric\_only\]) | Return cumulative minimum over a DataFrame or Series axis. |
| [`DataFrame.cumprod`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumprod.html#pandas.DataFrame.cumprod "pandas.DataFrame.cumprod")<br>(\[axis, skipna, numeric\_only\]) | Return cumulative product over a DataFrame or Series axis. |
| [`DataFrame.cumsum`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumsum.html#pandas.DataFrame.cumsum "pandas.DataFrame.cumsum")<br>(\[axis, skipna, numeric\_only\]) | Return cumulative sum over a DataFrame or Series axis. |
| [`DataFrame.describe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe")<br>(\[percentiles, include, ...\]) | Generate descriptive statistics. |
| [`DataFrame.diff`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html#pandas.DataFrame.diff "pandas.DataFrame.diff")<br>(\[periods, axis\]) | First discrete difference of element. |
| [`DataFrame.eval`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval "pandas.DataFrame.eval")<br>(expr, \*\[, inplace\]) | Evaluate a string describing operations on DataFrame columns. |
| [`DataFrame.kurt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.kurt.html#pandas.DataFrame.kurt "pandas.DataFrame.kurt")<br>(\*\[, axis, skipna, numeric\_only\]) | Return unbiased kurtosis over requested axis. |
| [`DataFrame.kurtosis`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.kurtosis.html#pandas.DataFrame.kurtosis "pandas.DataFrame.kurtosis")<br>(\*\[, axis, skipna, ...\]) | Return unbiased kurtosis over requested axis. |
| [`DataFrame.max`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html#pandas.DataFrame.max "pandas.DataFrame.max")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the maximum of the values over the requested axis. |
| [`DataFrame.mean`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html#pandas.DataFrame.mean "pandas.DataFrame.mean")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the mean of the values over the requested axis. |
| [`DataFrame.median`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html#pandas.DataFrame.median "pandas.DataFrame.median")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the median of the values over the requested axis. |
| [`DataFrame.min`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html#pandas.DataFrame.min "pandas.DataFrame.min")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the minimum of the values over the requested axis. |
| [`DataFrame.mode`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html#pandas.DataFrame.mode "pandas.DataFrame.mode")<br>(\[axis, numeric\_only, dropna\]) | Get the mode(s) of each element along the selected axis. |
| [`DataFrame.pct_change`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html#pandas.DataFrame.pct_change "pandas.DataFrame.pct_change")<br>(\[periods, fill\_method, ...\]) | Fractional change between the current and a prior element. |
| [`DataFrame.prod`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.prod.html#pandas.DataFrame.prod "pandas.DataFrame.prod")<br>(\*\[, axis, skipna, ...\]) | Return the product of the values over the requested axis. |
| [`DataFrame.product`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.product.html#pandas.DataFrame.product "pandas.DataFrame.product")<br>(\*\[, axis, skipna, ...\]) | Return the product of the values over the requested axis. |
| [`DataFrame.quantile`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html#pandas.DataFrame.quantile "pandas.DataFrame.quantile")<br>(\[q, axis, numeric\_only, ...\]) | Return values at the given quantile over requested axis. |
| [`DataFrame.rank`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html#pandas.DataFrame.rank "pandas.DataFrame.rank")<br>(\[axis, method, numeric\_only, ...\]) | Compute numerical data ranks (1 through n) along axis. |
| [`DataFrame.round`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html#pandas.DataFrame.round "pandas.DataFrame.round")<br>(\[decimals\]) | Round numeric columns in a DataFrame to a variable number of decimal places. |
| [`DataFrame.sem`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sem.html#pandas.DataFrame.sem "pandas.DataFrame.sem")<br>(\*\[, axis, skipna, ddof, ...\]) | Return unbiased standard error of the mean over requested axis. |
| [`DataFrame.skew`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.skew.html#pandas.DataFrame.skew "pandas.DataFrame.skew")<br>(\*\[, axis, skipna, numeric\_only\]) | Return unbiased skew over requested axis. |
| [`DataFrame.sum`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html#pandas.DataFrame.sum "pandas.DataFrame.sum")<br>(\*\[, axis, skipna, ...\]) | Return the sum of the values over the requested axis. |
| [`DataFrame.std`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html#pandas.DataFrame.std "pandas.DataFrame.std")<br>(\*\[, axis, skipna, ddof, ...\]) | Return sample standard deviation over requested axis. |
| [`DataFrame.var`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html#pandas.DataFrame.var "pandas.DataFrame.var")<br>(\*\[, axis, skipna, ddof, ...\]) | Return unbiased variance over requested axis. |
| [`DataFrame.nunique`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html#pandas.DataFrame.nunique "pandas.DataFrame.nunique")<br>(\[axis, dropna\]) | Count number of distinct elements in specified axis. |
| [`DataFrame.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html#pandas.DataFrame.value_counts "pandas.DataFrame.value_counts")<br>(\[subset, normalize, ...\]) | Return a Series containing the frequency of each distinct row in the DataFrame. |

Reindexing / selection / label manipulation[#](https://pandas.pydata.org/docs/reference/frame.html#reindexing-selection-label-manipulation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.add_prefix`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_prefix.html#pandas.DataFrame.add_prefix "pandas.DataFrame.add_prefix")<br>(prefix\[, axis\]) | Prefix labels with string prefix. |
| [`DataFrame.add_suffix`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_suffix.html#pandas.DataFrame.add_suffix "pandas.DataFrame.add_suffix")<br>(suffix\[, axis\]) | Suffix labels with string suffix. |
| [`DataFrame.align`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.align.html#pandas.DataFrame.align "pandas.DataFrame.align")<br>(other\[, join, axis, level, ...\]) | Align two objects on their axes with the specified join method. |
| [`DataFrame.at_time`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at_time.html#pandas.DataFrame.at_time "pandas.DataFrame.at_time")<br>(time\[, asof, axis\]) | Select values at particular time of day (e.g., 9:30AM). |
| [`DataFrame.between_time`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.between_time.html#pandas.DataFrame.between_time "pandas.DataFrame.between_time")<br>(start\_time, end\_time) | Select values between particular times of the day (e.g., 9:00-9:30 AM). |
| [`DataFrame.drop`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop "pandas.DataFrame.drop")<br>(\[labels, axis, index, ...\]) | Drop specified labels from rows or columns. |
| [`DataFrame.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "pandas.DataFrame.drop_duplicates")<br>(\[subset, keep, ...\]) | Return DataFrame with duplicate rows removed. |
| [`DataFrame.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html#pandas.DataFrame.duplicated "pandas.DataFrame.duplicated")<br>(\[subset, keep\]) | Return boolean Series denoting duplicate rows. |
| [`DataFrame.equals`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html#pandas.DataFrame.equals "pandas.DataFrame.equals")<br>(other) | Test whether two objects contain the same elements. |
| [`DataFrame.filter`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html#pandas.DataFrame.filter "pandas.DataFrame.filter")<br>(\[arg, like, regex, axis, ...\]) | Subset the rows or columns according to a boolean mask or the labels. |
| [`DataFrame.idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html#pandas.DataFrame.idxmax "pandas.DataFrame.idxmax")<br>(\[axis, skipna, numeric\_only\]) | Return index of first occurrence of maximum over requested axis. |
| [`DataFrame.idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html#pandas.DataFrame.idxmin "pandas.DataFrame.idxmin")<br>(\[axis, skipna, numeric\_only\]) | Return index of first occurrence of minimum over requested axis. |
| [`DataFrame.reindex`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex")<br>(\[labels, index, columns, ...\]) | Conform DataFrame to new index with optional filling logic. |
| [`DataFrame.reindex_like`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex_like.html#pandas.DataFrame.reindex_like "pandas.DataFrame.reindex_like")<br>(other\[, method, ...\]) | Return an object with matching indices as other object. |
| [`DataFrame.rename`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename "pandas.DataFrame.rename")<br>(\[mapper, index, columns, ...\]) | Rename columns or index labels. |
| [`DataFrame.rename_axis`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html#pandas.DataFrame.rename_axis "pandas.DataFrame.rename_axis")<br>(\[mapper, index, ...\]) | Set the name of the axis for the index or columns. |
| [`DataFrame.reset_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index "pandas.DataFrame.reset_index")<br>(\[level, drop, ...\]) | Reset the index, or a level of it. |
| [`DataFrame.sample`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html#pandas.DataFrame.sample "pandas.DataFrame.sample")<br>(\[n, frac, replace, ...\]) | Return a random sample of items from an axis of object. |
| [`DataFrame.select`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select.html#pandas.DataFrame.select "pandas.DataFrame.select")<br>(\*args, \*\*kwargs) | Select a subset of columns from the DataFrame. |
| [`DataFrame.set_axis`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_axis.html#pandas.DataFrame.set_axis "pandas.DataFrame.set_axis")<br>(labels, \*\[, axis, copy\]) | Assign desired index to given axis. |
| [`DataFrame.set_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index "pandas.DataFrame.set_index")<br>(keys, \*\[, drop, append, ...\]) | Set the DataFrame index using existing columns. |
| [`DataFrame.take`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.take.html#pandas.DataFrame.take "pandas.DataFrame.take")<br>(indices\[, axis\]) | Return the elements in the given _positional_ indices along an axis. |
| [`DataFrame.truncate`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truncate.html#pandas.DataFrame.truncate "pandas.DataFrame.truncate")<br>(\[before, after, axis, copy\]) | Truncate a Series or DataFrame before and after some index value. |

Missing data handling[#](https://pandas.pydata.org/docs/reference/frame.html#missing-data-handling "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.bfill`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.bfill.html#pandas.DataFrame.bfill "pandas.DataFrame.bfill")<br>(\*\[, axis, inplace, limit, ...\]) | Fill NA/NaN values by using the next valid observation to fill the gap. |
| [`DataFrame.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")<br>(\*\[, axis, how, thresh, ...\]) | Remove missing values. |
| [`DataFrame.ffill`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html#pandas.DataFrame.ffill "pandas.DataFrame.ffill")<br>(\*\[, axis, inplace, limit, ...\]) | Fill NA/NaN values by propagating the last valid observation to next valid. |
| [`DataFrame.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna "pandas.DataFrame.fillna")<br>(value, \*\[, axis, inplace, ...\]) | Fill NA/NaN values with value. |
| [`DataFrame.interpolate`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html#pandas.DataFrame.interpolate "pandas.DataFrame.interpolate")<br>(\[method, axis, limit, ...\]) | Fill NaN values using an interpolation method. |
| [`DataFrame.isna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna "pandas.DataFrame.isna")<br>() | Detect missing values. |
| [`DataFrame.isnull`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html#pandas.DataFrame.isnull "pandas.DataFrame.isnull")<br>() | DataFrame.isnull is an alias for DataFrame.isna. |
| [`DataFrame.notna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html#pandas.DataFrame.notna "pandas.DataFrame.notna")<br>() | Detect existing (non-missing) values. |
| [`DataFrame.notnull`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notnull.html#pandas.DataFrame.notnull "pandas.DataFrame.notnull")<br>() | DataFrame.notnull is an alias for DataFrame.notna. |
| [`DataFrame.replace`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html#pandas.DataFrame.replace "pandas.DataFrame.replace")<br>(\[to\_replace, value, ...\]) | Replace values given in to\_replace with value. |

Reshaping, sorting, transposing[#](https://pandas.pydata.org/docs/reference/frame.html#reshaping-sorting-transposing "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.droplevel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.droplevel.html#pandas.DataFrame.droplevel "pandas.DataFrame.droplevel")<br>(level\[, axis\]) | Return Series/DataFrame with requested index / column level(s) removed. |
| [`DataFrame.pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "pandas.DataFrame.pivot")<br>(\*, columns\[, index, values\]) | Return reshaped DataFrame organized by given index / column values. |
| [`DataFrame.pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table "pandas.DataFrame.pivot_table")<br>(\[values, index, ...\]) | Create a spreadsheet-style pivot table as a DataFrame. |
| [`DataFrame.reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reorder_levels.html#pandas.DataFrame.reorder_levels "pandas.DataFrame.reorder_levels")<br>(order\[, axis\]) | Rearrange index or column levels using input `order`. |
| [`DataFrame.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")<br>(by, \*\[, axis, ...\]) | Sort by the values along either axis. |
| [`DataFrame.sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "pandas.DataFrame.sort_index")<br>(\*\[, axis, level, ...\]) | Sort object by labels (along an axis). |
| [`DataFrame.nlargest`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html#pandas.DataFrame.nlargest "pandas.DataFrame.nlargest")<br>(n, columns\[, keep\]) | Return the first n rows ordered by columns in descending order. |
| [`DataFrame.nsmallest`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nsmallest.html#pandas.DataFrame.nsmallest "pandas.DataFrame.nsmallest")<br>(n, columns\[, keep\]) | Return the first n rows ordered by columns in ascending order. |
| [`DataFrame.swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.swaplevel.html#pandas.DataFrame.swaplevel "pandas.DataFrame.swaplevel")<br>(\[i, j, axis\]) | Swap levels i and j in a [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")<br>. |
| [`DataFrame.stack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack "pandas.DataFrame.stack")<br>(\[level, dropna, sort, ...\]) | Stack the prescribed level(s) from columns to index. |
| [`DataFrame.unstack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack "pandas.DataFrame.unstack")<br>(\[level, fill\_value, sort\]) | Pivot a level of the (necessarily hierarchical) index labels. |
| [`DataFrame.melt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html#pandas.DataFrame.melt "pandas.DataFrame.melt")<br>(\[id\_vars, value\_vars, ...\]) | Unpivot DataFrame from wide to long format, optionally leaving identifiers set. |
| [`DataFrame.explode`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html#pandas.DataFrame.explode "pandas.DataFrame.explode")<br>(column\[, ignore\_index\]) | Transform each element of a list-like to a row, replicating index values. |
| [`DataFrame.squeeze`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.squeeze.html#pandas.DataFrame.squeeze "pandas.DataFrame.squeeze")<br>(\[axis\]) | Squeeze 1 dimensional axis objects into scalars. |
| [`DataFrame.to_xarray`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xarray.html#pandas.DataFrame.to_xarray "pandas.DataFrame.to_xarray")<br>() | Return an xarray object from the pandas object. |
| [`DataFrame.T`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html#pandas.DataFrame.T "pandas.DataFrame.T") | The transpose of the DataFrame. |
| [`DataFrame.transpose`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html#pandas.DataFrame.transpose "pandas.DataFrame.transpose")<br>(\*args\[, copy\]) | Transpose index and columns. |

Combining / comparing / joining / merging[#](https://pandas.pydata.org/docs/reference/frame.html#combining-comparing-joining-merging "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.assign`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign")<br>(\*\*kwargs) | Assign new columns to a DataFrame. |
| [`DataFrame.compare`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html#pandas.DataFrame.compare "pandas.DataFrame.compare")<br>(other\[, align\_axis, ...\]) | Compare to another DataFrame and show the differences. |
| [`DataFrame.join`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join "pandas.DataFrame.join")<br>(other\[, on, how, lsuffix, ...\]) | Join columns of another DataFrame. |
| [`DataFrame.merge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge "pandas.DataFrame.merge")<br>(right\[, how, on, left\_on, ...\]) | Merge DataFrame or named Series objects with a database-style join. |
| [`DataFrame.update`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.update.html#pandas.DataFrame.update "pandas.DataFrame.update")<br>(other\[, join, overwrite, ...\]) | Modify in place using non-NA values from another DataFrame. |

Time Series-related[#](https://pandas.pydata.org/docs/reference/frame.html#time-series-related "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.asfreq.html#pandas.DataFrame.asfreq "pandas.DataFrame.asfreq")<br>(freq\[, method, how, ...\]) | Convert time series to specified frequency. |
| [`DataFrame.asof`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.asof.html#pandas.DataFrame.asof "pandas.DataFrame.asof")<br>(where\[, subset\]) | Return the last row(s) without any NaNs before where. |
| [`DataFrame.shift`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html#pandas.DataFrame.shift "pandas.DataFrame.shift")<br>(\[periods, freq, axis, ...\]) | Shift index by desired number of periods with an optional time freq. |
| [`DataFrame.first_valid_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.first_valid_index.html#pandas.DataFrame.first_valid_index "pandas.DataFrame.first_valid_index")<br>() | Return index for first non-missing value or None, if no value is found. |
| [`DataFrame.last_valid_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.last_valid_index.html#pandas.DataFrame.last_valid_index "pandas.DataFrame.last_valid_index")<br>() | Return index for last non-missing value or None, if no value is found. |
| [`DataFrame.resample`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html#pandas.DataFrame.resample "pandas.DataFrame.resample")<br>(rule\[, closed, label, ...\]) | Resample time-series data. |
| [`DataFrame.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_period.html#pandas.DataFrame.to_period "pandas.DataFrame.to_period")<br>(\[freq, axis, copy\]) | Convert DataFrame from DatetimeIndex to PeriodIndex. |
| [`DataFrame.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_timestamp.html#pandas.DataFrame.to_timestamp "pandas.DataFrame.to_timestamp")<br>(\[freq, how, axis, copy\]) | Cast PeriodIndex to DatetimeIndex of timestamps, at _beginning_ of period. |
| [`DataFrame.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tz_convert.html#pandas.DataFrame.tz_convert "pandas.DataFrame.tz_convert")<br>(tz\[, axis, level, copy\]) | Convert tz-aware axis to target time zone. |
| [`DataFrame.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tz_localize.html#pandas.DataFrame.tz_localize "pandas.DataFrame.tz_localize")<br>(tz\[, axis, level, ...\]) | Localize time zone naive index of a Series or DataFrame to target time zone. |

Flags[#](https://pandas.pydata.org/docs/reference/frame.html#flags "Link to this heading")

-------------------------------------------------------------------------------------------

Flags refer to attributes of the pandas object. Properties of the dataset (like the date it was recorded, the URL it was accessed from, etc.) should be stored in [`DataFrame.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas.DataFrame.attrs "pandas.DataFrame.attrs")
.

|     |     |
| --- | --- |
| [`Flags`](https://pandas.pydata.org/docs/reference/api/pandas.Flags.html#pandas.Flags "pandas.Flags")<br>(obj, \*, allows\_duplicate\_labels) | Flags that apply to pandas objects. |

Metadata[#](https://pandas.pydata.org/docs/reference/frame.html#metadata "Link to this heading")

-------------------------------------------------------------------------------------------------

[`DataFrame.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas.DataFrame.attrs "pandas.DataFrame.attrs")
 is a dictionary for storing global metadata for this DataFrame.

Warning

`DataFrame.attrs` is considered experimental and may change without warning.

|     |     |
| --- | --- |
| [`DataFrame.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas.DataFrame.attrs "pandas.DataFrame.attrs") | Dictionary of global attributes of this dataset. |

Plotting[#](https://pandas.pydata.org/docs/reference/frame.html#plotting "Link to this heading")

-------------------------------------------------------------------------------------------------

`DataFrame.plot` is both a callable method and a namespace attribute for specific plotting methods of the form `DataFrame.plot.<kind>`.

|     |     |
| --- | --- |
| [`DataFrame.plot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.html#pandas.DataFrame.plot "pandas.DataFrame.plot")<br>(\[x, y, kind, ax, ....\]) | DataFrame plotting accessor and method |

|     |     |
| --- | --- |
| [`DataFrame.plot.area`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.area.html#pandas.DataFrame.plot.area "pandas.DataFrame.plot.area")<br>(\[x, y, stacked\]) | Make a stacked area plot. |
| [`DataFrame.plot.bar`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html#pandas.DataFrame.plot.bar "pandas.DataFrame.plot.bar")<br>(\[x, y, color\]) | Make a vertical bar plot. |
| [`DataFrame.plot.barh`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.barh.html#pandas.DataFrame.plot.barh "pandas.DataFrame.plot.barh")<br>(\[x, y, color\]) | Make a horizontal bar plot. |
| [`DataFrame.plot.box`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.box.html#pandas.DataFrame.plot.box "pandas.DataFrame.plot.box")<br>(\[by\]) | Make a box plot of the DataFrame columns. |
| [`DataFrame.plot.density`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.density.html#pandas.DataFrame.plot.density "pandas.DataFrame.plot.density")<br>(\[bw\_method, ind, weights\]) | Make a Kernel Density Estimate plot using Gaussian kernels. |
| [`DataFrame.plot.hexbin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hexbin.html#pandas.DataFrame.plot.hexbin "pandas.DataFrame.plot.hexbin")<br>(x, y\[, C, ...\]) | Make a hexagonal binning plot. |
| [`DataFrame.plot.hist`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.hist.html#pandas.DataFrame.plot.hist "pandas.DataFrame.plot.hist")<br>(\[by, bins\]) | Make one histogram of the DataFrame's columns. |
| [`DataFrame.plot.kde`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.kde.html#pandas.DataFrame.plot.kde "pandas.DataFrame.plot.kde")<br>(\[bw\_method, ind, weights\]) | Make a Kernel Density Estimate plot using Gaussian kernels. |
| [`DataFrame.plot.line`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.line.html#pandas.DataFrame.plot.line "pandas.DataFrame.plot.line")<br>(\[x, y, color\]) | Make a line plot of a Series or DataFrame. |
| [`DataFrame.plot.pie`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.pie.html#pandas.DataFrame.plot.pie "pandas.DataFrame.plot.pie")<br>(\[y\]) | Make a pie plot. |
| [`DataFrame.plot.scatter`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.scatter.html#pandas.DataFrame.plot.scatter "pandas.DataFrame.plot.scatter")<br>(x, y\[, s, c\]) | Make a scatter plot with varying marker point size and color. |

|     |     |
| --- | --- |
| [`DataFrame.boxplot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html#pandas.DataFrame.boxplot "pandas.DataFrame.boxplot")<br>(\[column, by, ax, ...\]) | Make a box plot from DataFrame columns. |
| [`DataFrame.hist`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html#pandas.DataFrame.hist "pandas.DataFrame.hist")<br>(\[column, by, grid, ...\]) | Make a histogram of the DataFrame's columns. |

Sparse accessor[#](https://pandas.pydata.org/docs/reference/frame.html#sparse-accessor "Link to this heading")

---------------------------------------------------------------------------------------------------------------

Sparse-dtype specific methods and attributes are provided under the `DataFrame.sparse` accessor.

|     |     |
| --- | --- |
| [`DataFrame.sparse.density`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.density.html#pandas.DataFrame.sparse.density "pandas.DataFrame.sparse.density") | Ratio of non-sparse points to total (dense) data points. |

|     |     |
| --- | --- |
| [`DataFrame.sparse.from_spmatrix`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.from_spmatrix.html#pandas.DataFrame.sparse.from_spmatrix "pandas.DataFrame.sparse.from_spmatrix")<br>(data\[, ...\]) | Create a new DataFrame from a scipy sparse matrix. |
| [`DataFrame.sparse.to_coo`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_coo.html#pandas.DataFrame.sparse.to_coo "pandas.DataFrame.sparse.to_coo")<br>() | Return the contents of the frame as a sparse SciPy COO matrix. |
| [`DataFrame.sparse.to_dense`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.to_dense.html#pandas.DataFrame.sparse.to_dense "pandas.DataFrame.sparse.to_dense")<br>() | Convert a DataFrame with sparse values to dense. |

Serialization / IO / conversion[#](https://pandas.pydata.org/docs/reference/frame.html#serialization-io-conversion "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrame.from_arrow`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_arrow.html#pandas.DataFrame.from_arrow "pandas.DataFrame.from_arrow")<br>(data) | Construct a DataFrame from a tabular Arrow object. |
| [`DataFrame.from_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#pandas.DataFrame.from_dict "pandas.DataFrame.from_dict")<br>(data\[, orient, dtype, ...\]) | Construct DataFrame from dict of array-like or dicts. |
| [`DataFrame.from_records`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records "pandas.DataFrame.from_records")<br>(data\[, index, ...\]) | Convert structured or record ndarray to DataFrame. |
| [`DataFrame.to_orc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_orc.html#pandas.DataFrame.to_orc "pandas.DataFrame.to_orc")<br>(\[path, engine, index, ...\]) | Write a DataFrame to the Optimized Row Columnar (ORC) format. |
| [`DataFrame.to_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas.DataFrame.to_parquet "pandas.DataFrame.to_parquet")<br>(\[path, engine, ...\]) | Write a DataFrame to the binary parquet format. |
| [`DataFrame.to_pickle`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html#pandas.DataFrame.to_pickle "pandas.DataFrame.to_pickle")<br>(path, \*\[, compression, ...\]) | Pickle (serialize) object to file. |
| [`DataFrame.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")<br>(\[path\_or\_buf, sep, na\_rep, ...\]) | Write object to a comma-separated values (csv) file. |
| [`DataFrame.to_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html#pandas.DataFrame.to_hdf "pandas.DataFrame.to_hdf")<br>(path\_or\_buf, \*, key\[, ...\]) | Write the contained data to an HDF5 file using HDFStore. |
| [`DataFrame.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql "pandas.DataFrame.to_sql")<br>(name, con, \*\[, schema, ...\]) | Write records stored in a DataFrame to a SQL database. |
| [`DataFrame.to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html#pandas.DataFrame.to_dict "pandas.DataFrame.to_dict")<br>(\[orient, into, index\]) | Convert the DataFrame to a dictionary. |
| [`DataFrame.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel "pandas.DataFrame.to_excel")<br>(excel\_writer, \*\[, ...\]) | Write object to an Excel sheet. |
| [`DataFrame.to_json`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html#pandas.DataFrame.to_json "pandas.DataFrame.to_json")<br>(\[path\_or\_buf, orient, ...\]) | Convert the object to a JSON string. |
| [`DataFrame.to_html`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html "pandas.DataFrame.to_html")<br>(\[buf, columns, col\_space, ...\]) | Render a DataFrame as an HTML table. |
| [`DataFrame.to_feather`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_feather.html#pandas.DataFrame.to_feather "pandas.DataFrame.to_feather")<br>(path, \*\*kwargs) | Write a DataFrame to the binary Feather format. |
| [`DataFrame.to_latex`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html#pandas.DataFrame.to_latex "pandas.DataFrame.to_latex")<br>(\[buf, columns, header, ...\]) | Render object to a LaTeX tabular, longtable, or nested table. |
| [`DataFrame.to_stata`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html#pandas.DataFrame.to_stata "pandas.DataFrame.to_stata")<br>(path, \*\[, convert\_dates, ...\]) | Export DataFrame object to Stata dta format. |
| [`DataFrame.to_records`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_records.html#pandas.DataFrame.to_records "pandas.DataFrame.to_records")<br>(\[index, column\_dtypes, ...\]) | Convert DataFrame to a NumPy record array. |
| [`DataFrame.to_string`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html#pandas.DataFrame.to_string "pandas.DataFrame.to_string")<br>(\[buf, columns, ...\]) | Render a DataFrame to a console-friendly tabular output. |
| [`DataFrame.to_clipboard`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html#pandas.DataFrame.to_clipboard "pandas.DataFrame.to_clipboard")<br>(\*\[, excel, sep\]) | Copy object to the system clipboard. |
| [`DataFrame.to_markdown`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html#pandas.DataFrame.to_markdown "pandas.DataFrame.to_markdown")<br>(\[buf, mode, index, ...\]) | Print DataFrame in Markdown-friendly format. |
| [`DataFrame.style`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.style.html#pandas.DataFrame.style "pandas.DataFrame.style") | Returns a Styler object. |
| [`DataFrame.__dataframe__`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.__dataframe__.html#pandas.DataFrame.__dataframe__ "pandas.DataFrame.__dataframe__")<br>(\[nan\_as\_null, ...\]) | (DEPRECATED) Return the dataframe interchange object implementing the interchange protocol. |

On this page