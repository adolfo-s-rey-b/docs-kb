[Skip to main content](https://pandas.pydata.org/docs/reference/series.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/series.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/series.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/series.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/series.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/series.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/series.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/series.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/series.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/series.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/series.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/series.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/series.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/series.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Series[#](https://pandas.pydata.org/docs/reference/series.html#series "Link to this heading")

==============================================================================================

Note

For an introduction to using Series, see [Essential basic functionality](https://pandas.pydata.org/docs/user_guide/basics.html#basics)
.

Constructor[#](https://pandas.pydata.org/docs/reference/series.html#constructor "Link to this heading")

--------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")<br>(\[data, index, dtype, name, copy\]) | One-dimensional ndarray with axis labels (including time series). |

Attributes[#](https://pandas.pydata.org/docs/reference/series.html#attributes "Link to this heading")

------------------------------------------------------------------------------------------------------

**Axes**

|     |     |
| --- | --- |
| [`Series.index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html#pandas.Series.index "pandas.Series.index") | The index (axis labels) of the Series. |
| [`Series.array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array") | The ExtensionArray of the data backing this Series or Index. |
| [`Series.values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.values.html#pandas.Series.values "pandas.Series.values") | Return Series as ndarray or ndarray-like depending on the dtype. |
| [`Series.dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html#pandas.Series.dtype "pandas.Series.dtype") | Return the dtype object of the underlying data. |
| [`Series.info`](https://pandas.pydata.org/docs/reference/api/pandas.Series.info.html#pandas.Series.info "pandas.Series.info")<br>(\[verbose, buf, max\_cols, ...\]) | Print a concise summary of a Series. |
| [`Series.shape`](https://pandas.pydata.org/docs/reference/api/pandas.Series.shape.html#pandas.Series.shape "pandas.Series.shape") | Return a tuple of the shape of the underlying data. |
| [`Series.nbytes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nbytes.html#pandas.Series.nbytes "pandas.Series.nbytes") | Return the number of bytes in the underlying data. |
| [`Series.ndim`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ndim.html#pandas.Series.ndim "pandas.Series.ndim") | Number of dimensions of the underlying data, by definition 1. |
| [`Series.size`](https://pandas.pydata.org/docs/reference/api/pandas.Series.size.html#pandas.Series.size "pandas.Series.size") | Return the number of elements in the underlying data. |
| [`Series.T`](https://pandas.pydata.org/docs/reference/api/pandas.Series.T.html#pandas.Series.T "pandas.Series.T") | Return the transpose, which is by definition self. |
| [`Series.memory_usage`](https://pandas.pydata.org/docs/reference/api/pandas.Series.memory_usage.html#pandas.Series.memory_usage "pandas.Series.memory_usage")<br>(\[index, deep\]) | Return the memory usage of the Series. |
| [`Series.hasnans`](https://pandas.pydata.org/docs/reference/api/pandas.Series.hasnans.html#pandas.Series.hasnans "pandas.Series.hasnans") | Return True if there are any NaNs. |
| [`Series.empty`](https://pandas.pydata.org/docs/reference/api/pandas.Series.empty.html#pandas.Series.empty "pandas.Series.empty") | Indicator whether Index is empty. |
| [`Series.dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtypes.html#pandas.Series.dtypes "pandas.Series.dtypes") | Return the dtype object of the underlying data. |
| [`Series.name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html#pandas.Series.name "pandas.Series.name") | Return the name of the Series. |
| [`Series.flags`](https://pandas.pydata.org/docs/reference/api/pandas.Series.flags.html#pandas.Series.flags "pandas.Series.flags") | Get the properties associated with this pandas object. |
| [`Series.set_flags`](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_flags.html#pandas.Series.set_flags "pandas.Series.set_flags")<br>(\*\[, copy, ...\]) | Return a new object with updated flags. |

Conversion[#](https://pandas.pydata.org/docs/reference/series.html#conversion "Link to this heading")

------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.astype`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html#pandas.Series.astype "pandas.Series.astype")<br>(dtype\[, copy, errors\]) | Cast a pandas object to a specified dtype `dtype`. |
| [`Series.convert_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.convert_dtypes.html#pandas.Series.convert_dtypes "pandas.Series.convert_dtypes")<br>(\[infer\_objects, ...\]) | Convert columns from numpy dtypes to the best dtypes that support `pd.NA`. |
| [`Series.infer_objects`](https://pandas.pydata.org/docs/reference/api/pandas.Series.infer_objects.html#pandas.Series.infer_objects "pandas.Series.infer_objects")<br>(\[copy\]) | Attempt to infer better dtypes for object columns. |
| [`Series.copy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.copy.html#pandas.Series.copy "pandas.Series.copy")<br>(\[deep\]) | Make a copy of this object's indices and data. |
| [`Series.to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")<br>(\[dtype, copy, na\_value\]) | A NumPy ndarray representing the values in this Series or Index. |
| [`Series.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_period.html#pandas.Series.to_period "pandas.Series.to_period")<br>(\[freq, copy\]) | Convert Series from DatetimeIndex to PeriodIndex. |
| [`Series.to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_timestamp.html#pandas.Series.to_timestamp "pandas.Series.to_timestamp")<br>(\[freq, how, copy\]) | Cast to DatetimeIndex of Timestamps, at _beginning_ of period. |
| [`Series.to_list`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html#pandas.Series.to_list "pandas.Series.to_list")<br>() | Return a list of the values. |
| [`Series.__array__`](https://pandas.pydata.org/docs/reference/api/pandas.Series.__array__.html#pandas.Series.__array__ "pandas.Series.__array__")<br>(\[dtype, copy\]) | Return the values as a NumPy array. |

Indexing, iteration[#](https://pandas.pydata.org/docs/reference/series.html#indexing-iteration "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.get`](https://pandas.pydata.org/docs/reference/api/pandas.Series.get.html#pandas.Series.get "pandas.Series.get")<br>(key\[, default\]) | Get item from object for given key (ex: DataFrame column). |
| [`Series.at`](https://pandas.pydata.org/docs/reference/api/pandas.Series.at.html#pandas.Series.at "pandas.Series.at") | Access a single value for a row/column label pair. |
| [`Series.iat`](https://pandas.pydata.org/docs/reference/api/pandas.Series.iat.html#pandas.Series.iat "pandas.Series.iat") | Access a single value for a row/column pair by integer position. |
| [`Series.loc`](https://pandas.pydata.org/docs/reference/api/pandas.Series.loc.html#pandas.Series.loc "pandas.Series.loc") | Access a group of rows and columns by label(s) or a boolean array. |
| [`Series.iloc`](https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html#pandas.Series.iloc "pandas.Series.iloc") | Purely integer-location based indexing for selection by position. |
| [`Series.__iter__`](https://pandas.pydata.org/docs/reference/api/pandas.Series.__iter__.html#pandas.Series.__iter__ "pandas.Series.__iter__")<br>() | Return an iterator of the values. |
| [`Series.items`](https://pandas.pydata.org/docs/reference/api/pandas.Series.items.html#pandas.Series.items "pandas.Series.items")<br>() | Lazily iterate over (index, value) tuples. |
| [`Series.keys`](https://pandas.pydata.org/docs/reference/api/pandas.Series.keys.html#pandas.Series.keys "pandas.Series.keys")<br>() | Return alias for index. |
| [`Series.pop`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pop.html#pandas.Series.pop "pandas.Series.pop")<br>(item) | Return item and drops from series. |
| [`Series.item`](https://pandas.pydata.org/docs/reference/api/pandas.Series.item.html#pandas.Series.item "pandas.Series.item")<br>() | Return the first element of the underlying data as a Python scalar. |
| [`Series.xs`](https://pandas.pydata.org/docs/reference/api/pandas.Series.xs.html#pandas.Series.xs "pandas.Series.xs")<br>(key\[, axis, level, drop\_level\]) | Return cross-section from the Series/DataFrame. |

For more information on `.at`, `.iat`, `.loc`, and `.iloc`, see the [indexing documentation](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing)
.

Binary operator functions[#](https://pandas.pydata.org/docs/reference/series.html#binary-operator-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.add`](https://pandas.pydata.org/docs/reference/api/pandas.Series.add.html#pandas.Series.add "pandas.Series.add")<br>(other\[, level, fill\_value, axis\]) | Return Addition of series and other, element-wise (binary operator add). |
| [`Series.sub`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sub.html#pandas.Series.sub "pandas.Series.sub")<br>(other\[, level, fill\_value, axis\]) | Return Subtraction of series and other, element-wise (binary operator sub). |
| [`Series.mul`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mul.html#pandas.Series.mul "pandas.Series.mul")<br>(other\[, level, fill\_value, axis\]) | Return Multiplication of series and other, element-wise (binary operator mul). |
| [`Series.div`](https://pandas.pydata.org/docs/reference/api/pandas.Series.div.html#pandas.Series.div "pandas.Series.div")<br>(other\[, level, fill\_value, axis\]) | Return Floating division of series and other, element-wise (binary operator truediv). |
| [`Series.divmod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.divmod.html#pandas.Series.divmod "pandas.Series.divmod")<br>(other\[, level, fill\_value, axis\]) | Return Integer division and modulo of series and other, element-wise (binary operator divmod). |
| [`Series.truediv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.truediv.html#pandas.Series.truediv "pandas.Series.truediv")<br>(other\[, level, fill\_value, axis\]) | Return Floating division of series and other, element-wise (binary operator truediv). |
| [`Series.floordiv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.floordiv.html#pandas.Series.floordiv "pandas.Series.floordiv")<br>(other\[, level, fill\_value, axis\]) | Return Integer division of series and other, element-wise (binary operator floordiv). |
| [`Series.mod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mod.html#pandas.Series.mod "pandas.Series.mod")<br>(other\[, level, fill\_value, axis\]) | Return Modulo of series and other, element-wise (binary operator mod). |
| [`Series.pow`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pow.html#pandas.Series.pow "pandas.Series.pow")<br>(other\[, level, fill\_value, axis\]) | Return Exponential power of series and other, element-wise (binary operator pow). |
| [`Series.radd`](https://pandas.pydata.org/docs/reference/api/pandas.Series.radd.html#pandas.Series.radd "pandas.Series.radd")<br>(other\[, level, fill\_value, axis\]) | Return Addition of series and other, element-wise (binary operator radd). |
| [`Series.rsub`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rsub.html#pandas.Series.rsub "pandas.Series.rsub")<br>(other\[, level, fill\_value, axis\]) | Return Subtraction of series and other, element-wise (binary operator rsub). |
| [`Series.rmul`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rmul.html#pandas.Series.rmul "pandas.Series.rmul")<br>(other\[, level, fill\_value, axis\]) | Return Multiplication of series and other, element-wise (binary operator rmul). |
| [`Series.rdiv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rdiv.html#pandas.Series.rdiv "pandas.Series.rdiv")<br>(other\[, level, fill\_value, axis\]) | Return Floating division of series and other, element-wise (binary operator rtruediv). |
| [`Series.rdivmod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rdivmod.html#pandas.Series.rdivmod "pandas.Series.rdivmod")<br>(other\[, level, fill\_value, axis\]) | Return Integer division and modulo of series and other, element-wise (binary operator rdivmod). |
| [`Series.rtruediv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rtruediv.html#pandas.Series.rtruediv "pandas.Series.rtruediv")<br>(other\[, level, fill\_value, axis\]) | Return Floating division of series and other, element-wise (binary operator rtruediv). |
| [`Series.rfloordiv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rfloordiv.html#pandas.Series.rfloordiv "pandas.Series.rfloordiv")<br>(other\[, level, fill\_value, ...\]) | Return Integer division of series and other, element-wise (binary operator rfloordiv). |
| [`Series.rmod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rmod.html#pandas.Series.rmod "pandas.Series.rmod")<br>(other\[, level, fill\_value, axis\]) | Return Modulo of series and other, element-wise (binary operator rmod). |
| [`Series.rpow`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rpow.html#pandas.Series.rpow "pandas.Series.rpow")<br>(other\[, level, fill\_value, axis\]) | Return Exponential power of series and other, element-wise (binary operator rpow). |
| [`Series.combine`](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine.html#pandas.Series.combine "pandas.Series.combine")<br>(other, func\[, fill\_value\]) | Combine the Series with a Series or scalar according to func. |
| [`Series.combine_first`](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine_first.html#pandas.Series.combine_first "pandas.Series.combine_first")<br>(other) | Update null elements with value in the same location in 'other'. |
| [`Series.round`](https://pandas.pydata.org/docs/reference/api/pandas.Series.round.html#pandas.Series.round "pandas.Series.round")<br>(\[decimals\]) | Round each value in a Series to the given number of decimals. |
| [`Series.lt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.lt.html#pandas.Series.lt "pandas.Series.lt")<br>(other\[, level, fill\_value, axis\]) | Return Less than of series and other, element-wise (binary operator lt). |
| [`Series.gt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.gt.html#pandas.Series.gt "pandas.Series.gt")<br>(other\[, level, fill\_value, axis\]) | Return Greater than of series and other, element-wise (binary operator gt). |
| [`Series.le`](https://pandas.pydata.org/docs/reference/api/pandas.Series.le.html#pandas.Series.le "pandas.Series.le")<br>(other\[, level, fill\_value, axis\]) | Return Less than or equal to of series and other, element-wise (binary operator le). |
| [`Series.ge`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ge.html#pandas.Series.ge "pandas.Series.ge")<br>(other\[, level, fill\_value, axis\]) | Return Greater than or equal to of series and other, element-wise (binary operator ge). |
| [`Series.ne`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ne.html#pandas.Series.ne "pandas.Series.ne")<br>(other\[, level, fill\_value, axis\]) | Return Not equal to of series and other, element-wise (binary operator ne). |
| [`Series.eq`](https://pandas.pydata.org/docs/reference/api/pandas.Series.eq.html#pandas.Series.eq "pandas.Series.eq")<br>(other\[, level, fill\_value, axis\]) | Return Equal to of series and other, element-wise (binary operator eq). |
| [`Series.product`](https://pandas.pydata.org/docs/reference/api/pandas.Series.product.html#pandas.Series.product "pandas.Series.product")<br>(\*\[, axis, skipna, ...\]) | Return the product of the values over the requested axis. |
| [`Series.dot`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dot.html#pandas.Series.dot "pandas.Series.dot")<br>(other) | Compute the dot product between the Series and the columns of other. |

Unary operator functions[#](https://pandas.pydata.org/docs/reference/series.html#unary-operator-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.__invert__`](https://pandas.pydata.org/docs/reference/api/pandas.Series.__invert__.html#pandas.Series.__invert__ "pandas.Series.__invert__")<br>() | Return the bitwise inverse of the Series/DataFrame, element-wise. |

Function application, GroupBy & window[#](https://pandas.pydata.org/docs/reference/series.html#function-application-groupby-window "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.apply`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#pandas.Series.apply "pandas.Series.apply")<br>(func\[, args, by\_row\]) | Invoke function on values of Series. |
| [`Series.agg`](https://pandas.pydata.org/docs/reference/api/pandas.Series.agg.html#pandas.Series.agg "pandas.Series.agg")<br>(\[func, axis\]) | Aggregate using one or more operations over the specified axis. |
| [`Series.aggregate`](https://pandas.pydata.org/docs/reference/api/pandas.Series.aggregate.html#pandas.Series.aggregate "pandas.Series.aggregate")<br>(\[func, axis\]) | Aggregate using one or more operations over the specified axis. |
| [`Series.transform`](https://pandas.pydata.org/docs/reference/api/pandas.Series.transform.html#pandas.Series.transform "pandas.Series.transform")<br>(func\[, axis\]) | Call `func` on self producing a Series with the same axis shape as self. |
| [`Series.map`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map "pandas.Series.map")<br>(\[func, na\_action, engine\]) | Map values of Series according to an input mapping or function. |
| [`Series.groupby`](https://pandas.pydata.org/docs/reference/api/pandas.Series.groupby.html#pandas.Series.groupby "pandas.Series.groupby")<br>(\[by, level, as\_index, sort, ...\]) | Group Series using a mapper or by a Series of columns. |
| [`Series.rolling`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html#pandas.Series.rolling "pandas.Series.rolling")<br>(window\[, min\_periods, ...\]) | Provide rolling window calculations. |
| [`Series.expanding`](https://pandas.pydata.org/docs/reference/api/pandas.Series.expanding.html#pandas.Series.expanding "pandas.Series.expanding")<br>(\[min\_periods, method\]) | Provide expanding window calculations. |
| [`Series.ewm`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ewm.html#pandas.Series.ewm "pandas.Series.ewm")<br>(\[com, span, halflife, alpha, ...\]) | Provide exponentially weighted (EW) calculations. |
| [`Series.pipe`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pipe.html#pandas.Series.pipe "pandas.Series.pipe")<br>(func, \*args, \*\*kwargs) | Apply chainable functions that expect Series or DataFrames. |

Computations / descriptive stats[#](https://pandas.pydata.org/docs/reference/series.html#computations-descriptive-stats "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.abs`](https://pandas.pydata.org/docs/reference/api/pandas.Series.abs.html#pandas.Series.abs "pandas.Series.abs")<br>() | Return a Series/DataFrame with absolute numeric value of each element. |
| [`Series.all`](https://pandas.pydata.org/docs/reference/api/pandas.Series.all.html#pandas.Series.all "pandas.Series.all")<br>(\*\[, axis, bool\_only, skipna\]) | Return whether all elements are True, potentially over an axis. |
| [`Series.any`](https://pandas.pydata.org/docs/reference/api/pandas.Series.any.html#pandas.Series.any "pandas.Series.any")<br>(\*\[, axis, bool\_only, skipna\]) | Return whether any element is True, potentially over an axis. |
| [`Series.autocorr`](https://pandas.pydata.org/docs/reference/api/pandas.Series.autocorr.html#pandas.Series.autocorr "pandas.Series.autocorr")<br>(\[lag\]) | Compute the lag-N autocorrelation. |
| [`Series.between`](https://pandas.pydata.org/docs/reference/api/pandas.Series.between.html#pandas.Series.between "pandas.Series.between")<br>(left, right\[, inclusive\]) | Return boolean Series equivalent to left <= series <= right. |
| [`Series.clip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.clip.html#pandas.Series.clip "pandas.Series.clip")<br>(\[lower, upper, axis, inplace\]) | Trim values at input threshold(s). |
| [`Series.corr`](https://pandas.pydata.org/docs/reference/api/pandas.Series.corr.html#pandas.Series.corr "pandas.Series.corr")<br>(other\[, method, min\_periods\]) | Compute correlation with other Series, excluding missing values. |
| [`Series.count`](https://pandas.pydata.org/docs/reference/api/pandas.Series.count.html#pandas.Series.count "pandas.Series.count")<br>() | Return number of non-NA/null observations in the Series. |
| [`Series.cov`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cov.html#pandas.Series.cov "pandas.Series.cov")<br>(other\[, min\_periods, ddof\]) | Compute covariance with Series, excluding missing values. |
| [`Series.cummax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummax.html#pandas.Series.cummax "pandas.Series.cummax")<br>(\[axis, skipna\]) | Return cumulative maximum over a Series. |
| [`Series.cummin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummin.html#pandas.Series.cummin "pandas.Series.cummin")<br>(\[axis, skipna\]) | Return cumulative minimum over a Series. |
| [`Series.cumprod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cumprod.html#pandas.Series.cumprod "pandas.Series.cumprod")<br>(\[axis, skipna\]) | Return cumulative product over a Series. |
| [`Series.cumsum`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cumsum.html#pandas.Series.cumsum "pandas.Series.cumsum")<br>(\[axis, skipna\]) | Return cumulative sum over a Series. |
| [`Series.describe`](https://pandas.pydata.org/docs/reference/api/pandas.Series.describe.html#pandas.Series.describe "pandas.Series.describe")<br>(\[percentiles, include, exclude\]) | Generate descriptive statistics. |
| [`Series.diff`](https://pandas.pydata.org/docs/reference/api/pandas.Series.diff.html#pandas.Series.diff "pandas.Series.diff")<br>(\[periods\]) | First discrete difference of Series elements. |
| [`Series.factorize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.factorize.html#pandas.Series.factorize "pandas.Series.factorize")<br>(\[sort, use\_na\_sentinel\]) | Encode the object as an enumerated type or categorical variable. |
| [`Series.kurt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.kurt.html#pandas.Series.kurt "pandas.Series.kurt")<br>(\*\[, axis, skipna, numeric\_only\]) | Return unbiased kurtosis over requested axis. |
| [`Series.max`](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max "pandas.Series.max")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the maximum of the values over the requested axis. |
| [`Series.mean`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#pandas.Series.mean "pandas.Series.mean")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the mean of the values over the requested axis. |
| [`Series.median`](https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html#pandas.Series.median "pandas.Series.median")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the median of the values over the requested axis. |
| [`Series.min`](https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min "pandas.Series.min")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the minimum of the values over the requested axis. |
| [`Series.mode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html#pandas.Series.mode "pandas.Series.mode")<br>(\[dropna\]) | Return the mode(s) of the Series. |
| [`Series.nlargest`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nlargest.html#pandas.Series.nlargest "pandas.Series.nlargest")<br>(\[n, keep\]) | Return the largest n elements. |
| [`Series.nsmallest`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nsmallest.html#pandas.Series.nsmallest "pandas.Series.nsmallest")<br>(\[n, keep\]) | Return the smallest n elements. |
| [`Series.pct_change`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pct_change.html#pandas.Series.pct_change "pandas.Series.pct_change")<br>(\[periods, fill\_method, freq\]) | Fractional change between the current and a prior element. |
| [`Series.prod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.prod.html#pandas.Series.prod "pandas.Series.prod")<br>(\*\[, axis, skipna, numeric\_only, ...\]) | Return the product of the values over the requested axis. |
| [`Series.quantile`](https://pandas.pydata.org/docs/reference/api/pandas.Series.quantile.html#pandas.Series.quantile "pandas.Series.quantile")<br>(\[q, interpolation\]) | Return value at the given quantile. |
| [`Series.rank`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rank.html#pandas.Series.rank "pandas.Series.rank")<br>(\[axis, method, numeric\_only, ...\]) | Compute numerical data ranks (1 through n) along axis. |
| [`Series.sem`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sem.html#pandas.Series.sem "pandas.Series.sem")<br>(\*\[, axis, skipna, ddof, numeric\_only\]) | Return unbiased standard error of the mean over requested axis. |
| [`Series.skew`](https://pandas.pydata.org/docs/reference/api/pandas.Series.skew.html#pandas.Series.skew "pandas.Series.skew")<br>(\*\[, axis, skipna, numeric\_only\]) | Return unbiased skew over requested axis. |
| [`Series.std`](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#pandas.Series.std "pandas.Series.std")<br>(\*\[, axis, skipna, ddof, numeric\_only\]) | Return sample standard deviation. |
| [`Series.sum`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html#pandas.Series.sum "pandas.Series.sum")<br>(\*\[, axis, skipna, numeric\_only, ...\]) | Return the sum of the values over the requested axis. |
| [`Series.var`](https://pandas.pydata.org/docs/reference/api/pandas.Series.var.html#pandas.Series.var "pandas.Series.var")<br>(\*\[, axis, skipna, ddof, numeric\_only\]) | Return unbiased variance over requested axis. |
| [`Series.kurtosis`](https://pandas.pydata.org/docs/reference/api/pandas.Series.kurtosis.html#pandas.Series.kurtosis "pandas.Series.kurtosis")<br>(\*\[, axis, skipna, numeric\_only\]) | Return unbiased kurtosis over requested axis. |
| [`Series.unique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#pandas.Series.unique "pandas.Series.unique")<br>() | Return unique values of Series object. |
| [`Series.nunique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nunique.html#pandas.Series.nunique "pandas.Series.nunique")<br>(\[dropna\]) | Return number of unique elements in the object. |
| [`Series.is_unique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_unique.html#pandas.Series.is_unique "pandas.Series.is_unique") | Return True if values in the object are unique. |
| [`Series.is_monotonic_increasing`](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_increasing.html#pandas.Series.is_monotonic_increasing "pandas.Series.is_monotonic_increasing") | Return True if values in the object are monotonically increasing. |
| [`Series.is_monotonic_decreasing`](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_decreasing.html#pandas.Series.is_monotonic_decreasing "pandas.Series.is_monotonic_decreasing") | Return True if values in the object are monotonically decreasing. |
| [`Series.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts "pandas.Series.value_counts")<br>(\[normalize, sort, ...\]) | Return a Series containing counts of unique values. |

Reindexing / selection / label manipulation[#](https://pandas.pydata.org/docs/reference/series.html#reindexing-selection-label-manipulation "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.align`](https://pandas.pydata.org/docs/reference/api/pandas.Series.align.html#pandas.Series.align "pandas.Series.align")<br>(other\[, join, axis, level, ...\]) | Align two objects on their axes with the specified join method. |
| [`Series.case_when`](https://pandas.pydata.org/docs/reference/api/pandas.Series.case_when.html#pandas.Series.case_when "pandas.Series.case_when")<br>(caselist) | Replace values where the conditions are True. |
| [`Series.drop`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop.html#pandas.Series.drop "pandas.Series.drop")<br>(\[labels, axis, index, columns, ...\]) | Return Series with specified index labels removed. |
| [`Series.droplevel`](https://pandas.pydata.org/docs/reference/api/pandas.Series.droplevel.html#pandas.Series.droplevel "pandas.Series.droplevel")<br>(level\[, axis\]) | Return Series/DataFrame with requested index / column level(s) removed. |
| [`Series.drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates "pandas.Series.drop_duplicates")<br>(\*\[, keep, inplace, ...\]) | Return Series with duplicate values removed. |
| [`Series.duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html#pandas.Series.duplicated "pandas.Series.duplicated")<br>(\[keep\]) | Indicate duplicate Series values. |
| [`Series.equals`](https://pandas.pydata.org/docs/reference/api/pandas.Series.equals.html#pandas.Series.equals "pandas.Series.equals")<br>(other) | Test whether two objects contain the same elements. |
| [`Series.head`](https://pandas.pydata.org/docs/reference/api/pandas.Series.head.html#pandas.Series.head "pandas.Series.head")<br>(\[n\]) | Return the first n rows. |
| [`Series.idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html#pandas.Series.idxmax "pandas.Series.idxmax")<br>(\[axis, skipna\]) | Return the row label of the maximum value. |
| [`Series.idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html#pandas.Series.idxmin "pandas.Series.idxmin")<br>(\[axis, skipna\]) | Return the row label of the minimum value. |
| [`Series.isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#pandas.Series.isin "pandas.Series.isin")<br>(values) | Whether elements in Series are contained in values. |
| [`Series.reindex`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html#pandas.Series.reindex "pandas.Series.reindex")<br>(\[index, axis, method, copy, ...\]) | Conform Series to new index with optional filling logic. |
| [`Series.reindex_like`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex_like.html#pandas.Series.reindex_like "pandas.Series.reindex_like")<br>(other\[, method, copy, ...\]) | Return an object with matching indices as other object. |
| [`Series.rename`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename.html#pandas.Series.rename "pandas.Series.rename")<br>(\[index, axis, copy, inplace, ...\]) | Alter Series index labels or name. |
| [`Series.rename_axis`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename_axis.html#pandas.Series.rename_axis "pandas.Series.rename_axis")<br>(\[mapper, index, axis, ...\]) | Set the name of the axis for the index. |
| [`Series.reset_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reset_index.html#pandas.Series.reset_index "pandas.Series.reset_index")<br>(\[level, drop, name, ...\]) | Generate a new DataFrame or Series with the index reset. |
| [`Series.sample`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sample.html#pandas.Series.sample "pandas.Series.sample")<br>(\[n, frac, replace, weights, ...\]) | Return a random sample of items from an axis of object. |
| [`Series.set_axis`](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_axis.html#pandas.Series.set_axis "pandas.Series.set_axis")<br>(labels, \*\[, axis, copy\]) | Assign desired index to given axis. |
| [`Series.take`](https://pandas.pydata.org/docs/reference/api/pandas.Series.take.html#pandas.Series.take "pandas.Series.take")<br>(indices\[, axis\]) | Return the elements in the given _positional_ indices along an axis. |
| [`Series.tail`](https://pandas.pydata.org/docs/reference/api/pandas.Series.tail.html#pandas.Series.tail "pandas.Series.tail")<br>(\[n\]) | Return the last n rows. |
| [`Series.truncate`](https://pandas.pydata.org/docs/reference/api/pandas.Series.truncate.html#pandas.Series.truncate "pandas.Series.truncate")<br>(\[before, after, axis, copy\]) | Truncate a Series or DataFrame before and after some index value. |
| [`Series.where`](https://pandas.pydata.org/docs/reference/api/pandas.Series.where.html#pandas.Series.where "pandas.Series.where")<br>(cond\[, other, inplace, axis, level\]) | Replace values where the condition is False. |
| [`Series.mask`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mask.html#pandas.Series.mask "pandas.Series.mask")<br>(cond\[, other, inplace, axis, level\]) | Replace values where the condition is True. |
| [`Series.add_prefix`](https://pandas.pydata.org/docs/reference/api/pandas.Series.add_prefix.html#pandas.Series.add_prefix "pandas.Series.add_prefix")<br>(prefix\[, axis\]) | Prefix labels with string prefix. |
| [`Series.add_suffix`](https://pandas.pydata.org/docs/reference/api/pandas.Series.add_suffix.html#pandas.Series.add_suffix "pandas.Series.add_suffix")<br>(suffix\[, axis\]) | Suffix labels with string suffix. |
| [`Series.filter`](https://pandas.pydata.org/docs/reference/api/pandas.Series.filter.html#pandas.Series.filter "pandas.Series.filter")<br>(\[arg, like, regex, axis, ...\]) | Subset the rows or columns according to a boolean mask or the labels. |

Missing data handling[#](https://pandas.pydata.org/docs/reference/series.html#missing-data-handling "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.bfill`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html#pandas.Series.bfill "pandas.Series.bfill")<br>(\*\[, axis, inplace, limit, ...\]) | Fill NA/NaN values by using the next valid observation to fill the gap. |
| [`Series.dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html#pandas.Series.dropna "pandas.Series.dropna")<br>(\*\[, axis, inplace, how, ...\]) | Return a new Series with missing values removed. |
| [`Series.ffill`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html#pandas.Series.ffill "pandas.Series.ffill")<br>(\*\[, axis, inplace, limit, ...\]) | Fill NA/NaN values by propagating the last valid observation to next valid. |
| [`Series.fillna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html#pandas.Series.fillna "pandas.Series.fillna")<br>(value, \*\[, axis, inplace, limit\]) | Fill NA/NaN values with value. |
| [`Series.interpolate`](https://pandas.pydata.org/docs/reference/api/pandas.Series.interpolate.html#pandas.Series.interpolate "pandas.Series.interpolate")<br>(\[method, axis, limit, ...\]) | Fill NaN values using an interpolation method. |
| [`Series.isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html#pandas.Series.isna "pandas.Series.isna")<br>() | Detect missing values. |
| [`Series.isnull`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isnull.html#pandas.Series.isnull "pandas.Series.isnull")<br>() | Series.isnull is an alias for Series.isna. |
| [`Series.notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html#pandas.Series.notna "pandas.Series.notna")<br>() | Detect existing (non-missing) values. |
| [`Series.notnull`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notnull.html#pandas.Series.notnull "pandas.Series.notnull")<br>() | Series.notnull is an alias for Series.notna. |
| [`Series.replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html#pandas.Series.replace "pandas.Series.replace")<br>(\[to\_replace, value, inplace, ...\]) | Replace values given in to\_replace with value. |

Reshaping, sorting[#](https://pandas.pydata.org/docs/reference/series.html#reshaping-sorting "Link to this heading")

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.argsort`](https://pandas.pydata.org/docs/reference/api/pandas.Series.argsort.html#pandas.Series.argsort "pandas.Series.argsort")<br>(\[axis, kind, order, stable\]) | Return the integer indices that would sort the Series values. |
| [`Series.argmin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmin.html#pandas.Series.argmin "pandas.Series.argmin")<br>(\[axis, skipna\]) | Return int position of the smallest value in the Series. |
| [`Series.argmax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmax.html#pandas.Series.argmax "pandas.Series.argmax")<br>(\[axis, skipna\]) | Return int position of the largest value in the Series. |
| [`Series.reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reorder_levels.html#pandas.Series.reorder_levels "pandas.Series.reorder_levels")<br>(order) | Rearrange index levels using input order. |
| [`Series.sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values "pandas.Series.sort_values")<br>(\*\[, axis, ascending, ...\]) | Sort by the values. |
| [`Series.sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_index.html#pandas.Series.sort_index "pandas.Series.sort_index")<br>(\*\[, axis, level, ...\]) | Sort Series by index labels. |
| [`Series.swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.Series.swaplevel.html#pandas.Series.swaplevel "pandas.Series.swaplevel")<br>(\[i, j, copy\]) | Swap levels i and j in a [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")<br>. |
| [`Series.unstack`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unstack.html#pandas.Series.unstack "pandas.Series.unstack")<br>(\[level, fill\_value, sort\]) | Unstack, also known as pivot, Series with MultiIndex to produce DataFrame. |
| [`Series.explode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.explode.html#pandas.Series.explode "pandas.Series.explode")<br>(\[ignore\_index\]) | Transform each element of a list-like to a row. |
| [`Series.searchsorted`](https://pandas.pydata.org/docs/reference/api/pandas.Series.searchsorted.html#pandas.Series.searchsorted "pandas.Series.searchsorted")<br>(value\[, side, sorter\]) | Find indices where elements should be inserted to maintain order. |
| [`Series.repeat`](https://pandas.pydata.org/docs/reference/api/pandas.Series.repeat.html#pandas.Series.repeat "pandas.Series.repeat")<br>(repeats\[, axis\]) | Repeat elements of a Series. |
| [`Series.squeeze`](https://pandas.pydata.org/docs/reference/api/pandas.Series.squeeze.html#pandas.Series.squeeze "pandas.Series.squeeze")<br>(\[axis\]) | Squeeze 1 dimensional axis objects into scalars. |

Combining / comparing / joining / merging[#](https://pandas.pydata.org/docs/reference/series.html#combining-comparing-joining-merging "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.compare`](https://pandas.pydata.org/docs/reference/api/pandas.Series.compare.html#pandas.Series.compare "pandas.Series.compare")<br>(other\[, align\_axis, ...\]) | Compare to another Series and show the differences. |
| [`Series.update`](https://pandas.pydata.org/docs/reference/api/pandas.Series.update.html#pandas.Series.update "pandas.Series.update")<br>(other) | Modify Series in place using values from passed Series. |

Time Series-related[#](https://pandas.pydata.org/docs/reference/series.html#time-series-related "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.Series.asfreq.html#pandas.Series.asfreq "pandas.Series.asfreq")<br>(freq\[, method, how, ...\]) | Convert time series to specified frequency. |
| [`Series.asof`](https://pandas.pydata.org/docs/reference/api/pandas.Series.asof.html#pandas.Series.asof "pandas.Series.asof")<br>(where\[, subset\]) | Return the last row(s) without any NaNs before where. |
| [`Series.shift`](https://pandas.pydata.org/docs/reference/api/pandas.Series.shift.html#pandas.Series.shift "pandas.Series.shift")<br>(\[periods, freq, axis, ...\]) | Shift index by desired number of periods with an optional time freq. |
| [`Series.first_valid_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.first_valid_index.html#pandas.Series.first_valid_index "pandas.Series.first_valid_index")<br>() | Return index for first non-missing value or None, if no value is found. |
| [`Series.last_valid_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.last_valid_index.html#pandas.Series.last_valid_index "pandas.Series.last_valid_index")<br>() | Return index for last non-missing value or None, if no value is found. |
| [`Series.resample`](https://pandas.pydata.org/docs/reference/api/pandas.Series.resample.html#pandas.Series.resample "pandas.Series.resample")<br>(rule\[, closed, label, ...\]) | Resample time-series data. |
| [`Series.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_convert.html#pandas.Series.tz_convert "pandas.Series.tz_convert")<br>(tz\[, axis, level, copy\]) | Convert tz-aware axis to target time zone. |
| [`Series.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_localize.html#pandas.Series.tz_localize "pandas.Series.tz_localize")<br>(tz\[, axis, level, copy, ...\]) | Localize time zone naive index of a Series or DataFrame to target time zone. |
| [`Series.at_time`](https://pandas.pydata.org/docs/reference/api/pandas.Series.at_time.html#pandas.Series.at_time "pandas.Series.at_time")<br>(time\[, asof, axis\]) | Select values at particular time of day (e.g., 9:30AM). |
| [`Series.between_time`](https://pandas.pydata.org/docs/reference/api/pandas.Series.between_time.html#pandas.Series.between_time "pandas.Series.between_time")<br>(start\_time, end\_time\[, ...\]) | Select values between particular times of the day (e.g., 9:00-9:30 AM). |

Accessors[#](https://pandas.pydata.org/docs/reference/series.html#accessors "Link to this heading")

----------------------------------------------------------------------------------------------------

pandas provides dtype-specific methods under various accessors. These are separate namespaces within [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 that only apply to specific data types.

|     |     |
| --- | --- |
| [`Series.str`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.html#pandas.Series.str "pandas.Series.str") |     |
| [`Series.cat`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.html#pandas.Series.cat "pandas.Series.cat") |     |
| [`Series.dt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.html#pandas.Series.dt "pandas.Series.dt") |     |
| [`Series.sparse`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.html#pandas.Series.sparse "pandas.Series.sparse") |     |
| [`DataFrame.sparse`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sparse.html#pandas.DataFrame.sparse "pandas.DataFrame.sparse") |     |
| [`Index.str`](https://pandas.pydata.org/docs/reference/api/pandas.Index.str.html#pandas.Index.str "pandas.Index.str") |     |

| Data Type | Accessor |
| --- | --- |
| Datetime, Timedelta, Period | [dt](https://pandas.pydata.org/docs/reference/series.html#api-series-dt) |
| String | [str](https://pandas.pydata.org/docs/reference/series.html#api-series-str) |
| Categorical | [cat](https://pandas.pydata.org/docs/reference/series.html#api-series-cat) |
| Sparse | [sparse](https://pandas.pydata.org/docs/reference/series.html#api-series-sparse) |
| PyArrow list | [list](https://pandas.pydata.org/docs/reference/series.html#api-series-list) |
| PyArrow struct | [struct](https://pandas.pydata.org/docs/reference/series.html#api-series-struct) |

### Datetimelike properties[#](https://pandas.pydata.org/docs/reference/series.html#datetimelike-properties "Link to this heading")

`Series.dt` can be used to access the values of the series as datetimelike and return several properties. These can be accessed like `Series.dt.<property>`.

#### Datetime properties[#](https://pandas.pydata.org/docs/reference/series.html#datetime-properties "Link to this heading")

|     |     |
| --- | --- |
| [`Series.dt.date`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.date.html#pandas.Series.dt.date "pandas.Series.dt.date") | Returns numpy array of python [`datetime.date`](https://docs.python.org/3/library/datetime.html#datetime.date "(in Python v3.15)")<br> objects. |
| [`Series.dt.time`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.time.html#pandas.Series.dt.time "pandas.Series.dt.time") | Returns numpy array of [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "(in Python v3.15)")<br> objects. |
| [`Series.dt.timetz`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.timetz.html#pandas.Series.dt.timetz "pandas.Series.dt.timetz") | Returns numpy array of [`datetime.time`](https://docs.python.org/3/library/datetime.html#datetime.time "(in Python v3.15)")<br> objects with timezones. |
| [`Series.dt.year`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.year.html#pandas.Series.dt.year "pandas.Series.dt.year") | The year of the datetime. |
| [`Series.dt.month`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month.html#pandas.Series.dt.month "pandas.Series.dt.month") | The month as January=1, December=12. |
| [`Series.dt.day`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day.html#pandas.Series.dt.day "pandas.Series.dt.day") | The day of the datetime. |
| [`Series.dt.hour`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.hour.html#pandas.Series.dt.hour "pandas.Series.dt.hour") | The hours of the datetime. |
| [`Series.dt.minute`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.minute.html#pandas.Series.dt.minute "pandas.Series.dt.minute") | The minutes of the datetime. |
| [`Series.dt.second`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.second.html#pandas.Series.dt.second "pandas.Series.dt.second") | The seconds of the datetime. |
| [`Series.dt.microsecond`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.microsecond.html#pandas.Series.dt.microsecond "pandas.Series.dt.microsecond") | The microseconds of the datetime. |
| [`Series.dt.nanosecond`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanosecond.html#pandas.Series.dt.nanosecond "pandas.Series.dt.nanosecond") | The nanoseconds of the datetime. |
| [`Series.dt.dayofweek`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.dayofweek.html#pandas.Series.dt.dayofweek "pandas.Series.dt.dayofweek") | (DEPRECATED) The day of the week with Monday=0, Sunday=6. |
| [`Series.dt.day_of_week`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_of_week.html#pandas.Series.dt.day_of_week "pandas.Series.dt.day_of_week") | The day of the week with Monday=0, Sunday=6. |
| [`Series.dt.weekday`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.weekday.html#pandas.Series.dt.weekday "pandas.Series.dt.weekday") | (DEPRECATED) The day of the week with Monday=0, Sunday=6. |
| [`Series.dt.dayofyear`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.dayofyear.html#pandas.Series.dt.dayofyear "pandas.Series.dt.dayofyear") | (DEPRECATED) The ordinal day of the year. |
| [`Series.dt.day_of_year`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_of_year.html#pandas.Series.dt.day_of_year "pandas.Series.dt.day_of_year") | The ordinal day of the year. |
| [`Series.dt.days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days_in_month.html#pandas.Series.dt.days_in_month "pandas.Series.dt.days_in_month") | The number of days in the month. |
| [`Series.dt.quarter`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.quarter.html#pandas.Series.dt.quarter "pandas.Series.dt.quarter") | The quarter of the date. |
| [`Series.dt.is_month_start`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_start.html#pandas.Series.dt.is_month_start "pandas.Series.dt.is_month_start") | Indicates whether the date is the first day of the month. |
| [`Series.dt.is_month_end`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_month_end.html#pandas.Series.dt.is_month_end "pandas.Series.dt.is_month_end") | Indicates whether the date is the last day of the month. |
| [`Series.dt.is_quarter_start`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_start.html#pandas.Series.dt.is_quarter_start "pandas.Series.dt.is_quarter_start") | Indicator for whether the date is the first day of a quarter. |
| [`Series.dt.is_quarter_end`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_quarter_end.html#pandas.Series.dt.is_quarter_end "pandas.Series.dt.is_quarter_end") | Indicator for whether the date is the last day of a quarter. |
| [`Series.dt.is_year_start`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_year_start.html#pandas.Series.dt.is_year_start "pandas.Series.dt.is_year_start") | Indicate whether the date is the first day of a year. |
| [`Series.dt.is_year_end`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_year_end.html#pandas.Series.dt.is_year_end "pandas.Series.dt.is_year_end") | Indicate whether the date is the last day of the year. |
| [`Series.dt.is_leap_year`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.is_leap_year.html#pandas.Series.dt.is_leap_year "pandas.Series.dt.is_leap_year") | Boolean indicator if the date belongs to a leap year. |
| [`Series.dt.daysinmonth`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.daysinmonth.html#pandas.Series.dt.daysinmonth "pandas.Series.dt.daysinmonth") | (DEPRECATED) The number of days in the month. |
| [`Series.dt.days_in_month`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days_in_month.html#pandas.Series.dt.days_in_month "pandas.Series.dt.days_in_month") | The number of days in the month. |
| [`Series.dt.tz`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz.html#pandas.Series.dt.tz "pandas.Series.dt.tz") | Return the timezone. |
| [`Series.dt.freq`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.freq.html#pandas.Series.dt.freq "pandas.Series.dt.freq") | (DEPRECATED) Return a string representing a frequency generated by infer\_freq. |
| [`Series.dt.unit`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.unit.html#pandas.Series.dt.unit "pandas.Series.dt.unit") | The precision unit of the datetime data. |

#### Datetime methods[#](https://pandas.pydata.org/docs/reference/series.html#datetime-methods "Link to this heading")

|     |     |
| --- | --- |
| [`Series.dt.isocalendar`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.isocalendar.html#pandas.Series.dt.isocalendar "pandas.Series.dt.isocalendar")<br>() | Calculate year, week, and day according to the ISO 8601 standard. |
| [`Series.dt.to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_period.html#pandas.Series.dt.to_period "pandas.Series.dt.to_period")<br>(\[freq\]) | Cast to PeriodArray/PeriodIndex at a particular frequency. |
| [`Series.dt.to_pydatetime`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pydatetime.html#pandas.Series.dt.to_pydatetime "pandas.Series.dt.to_pydatetime")<br>() | Return the data as a Series of [`datetime.datetime`](https://docs.python.org/3/library/datetime.html#datetime.datetime "(in Python v3.15)")<br> objects. |
| [`Series.dt.tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_localize.html#pandas.Series.dt.tz_localize "pandas.Series.dt.tz_localize")<br>(tz\[, ambiguous, ...\]) | Localize tz-naive Datetime Array/Index to tz-aware Datetime Array/Index. |
| [`Series.dt.tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.tz_convert.html#pandas.Series.dt.tz_convert "pandas.Series.dt.tz_convert")<br>(tz) | Convert tz-aware Datetime Array/Index from one time zone to another. |
| [`Series.dt.normalize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.normalize.html#pandas.Series.dt.normalize "pandas.Series.dt.normalize")<br>() | Convert times to midnight. |
| [`Series.dt.strftime`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.strftime.html#pandas.Series.dt.strftime "pandas.Series.dt.strftime")<br>(date\_format) | Convert to Index using specified date\_format. |
| [`Series.dt.round`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.round.html#pandas.Series.dt.round "pandas.Series.dt.round")<br>(freq\[, ambiguous, nonexistent\]) | Perform round operation on the data to the specified freq. |
| [`Series.dt.floor`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.floor.html#pandas.Series.dt.floor "pandas.Series.dt.floor")<br>(freq\[, ambiguous, nonexistent\]) | Perform floor operation on the data to the specified freq. |
| [`Series.dt.ceil`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.ceil.html#pandas.Series.dt.ceil "pandas.Series.dt.ceil")<br>(freq\[, ambiguous, nonexistent\]) | Perform ceil operation on the data to the specified freq. |
| [`Series.dt.month_name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.month_name.html#pandas.Series.dt.month_name "pandas.Series.dt.month_name")<br>(\[locale\]) | Return the month names with specified locale. |
| [`Series.dt.day_name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_name.html#pandas.Series.dt.day_name "pandas.Series.dt.day_name")<br>(\[locale\]) | Return the day names with specified locale. |
| [`Series.dt.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.as_unit.html#pandas.Series.dt.as_unit "pandas.Series.dt.as_unit")<br>(unit\[, round\_ok\]) | Convert to a dtype with the given unit resolution. |

#### Period properties[#](https://pandas.pydata.org/docs/reference/series.html#period-properties "Link to this heading")

|     |     |
| --- | --- |
| [`Series.dt.qyear`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.qyear.html#pandas.Series.dt.qyear "pandas.Series.dt.qyear") | Fiscal year the Period lies in according to its starting-quarter. |
| [`Series.dt.start_time`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.start_time.html#pandas.Series.dt.start_time "pandas.Series.dt.start_time") | Get the Timestamp for the start of the period. |
| [`Series.dt.end_time`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.end_time.html#pandas.Series.dt.end_time "pandas.Series.dt.end_time") | Get the Timestamp for the end of the period. |

#### Timedelta properties[#](https://pandas.pydata.org/docs/reference/series.html#timedelta-properties "Link to this heading")

|     |     |
| --- | --- |
| [`Series.dt.days`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.days.html#pandas.Series.dt.days "pandas.Series.dt.days") | Number of days for each element. |
| [`Series.dt.seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.seconds.html#pandas.Series.dt.seconds "pandas.Series.dt.seconds") | Number of seconds (>= 0 and less than 1 day) for each element. |
| [`Series.dt.microseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.microseconds.html#pandas.Series.dt.microseconds "pandas.Series.dt.microseconds") | Number of microseconds (>= 0 and less than 1 second) for each element. |
| [`Series.dt.nanoseconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.nanoseconds.html#pandas.Series.dt.nanoseconds "pandas.Series.dt.nanoseconds") | Number of nanoseconds (>= 0 and less than 1 microsecond) for each element. |
| [`Series.dt.components`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.components.html#pandas.Series.dt.components "pandas.Series.dt.components") | Return a Dataframe of the components of the Timedeltas. |
| [`Series.dt.unit`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.unit.html#pandas.Series.dt.unit "pandas.Series.dt.unit") | The precision unit of the datetime data. |

#### Timedelta methods[#](https://pandas.pydata.org/docs/reference/series.html#timedelta-methods "Link to this heading")

|     |     |
| --- | --- |
| [`Series.dt.to_pytimedelta`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.to_pytimedelta.html#pandas.Series.dt.to_pytimedelta "pandas.Series.dt.to_pytimedelta")<br>() | Return an array of native [`datetime.timedelta`](https://docs.python.org/3/library/datetime.html#datetime.timedelta "(in Python v3.15)")<br> objects. |
| [`Series.dt.total_seconds`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.total_seconds.html#pandas.Series.dt.total_seconds "pandas.Series.dt.total_seconds")<br>() | Return total duration of each element expressed in seconds. |
| [`Series.dt.as_unit`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.as_unit.html#pandas.Series.dt.as_unit "pandas.Series.dt.as_unit")<br>(unit\[, round\_ok\]) | Convert to a dtype with the given unit resolution. |

### String handling[#](https://pandas.pydata.org/docs/reference/series.html#string-handling "Link to this heading")

`Series.str` can be used to access the values of the series as strings and apply several methods to it. These can be accessed like `Series.str.<function/property>`.

|     |     |
| --- | --- |
| [`Series.str.capitalize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.capitalize.html#pandas.Series.str.capitalize "pandas.Series.str.capitalize")<br>() | Convert strings in the Series/Index to be capitalized. |
| [`Series.str.casefold`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.casefold.html#pandas.Series.str.casefold "pandas.Series.str.casefold")<br>() | Convert strings in the Series/Index to be casefolded. |
| [`Series.str.cat`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.cat.html#pandas.Series.str.cat "pandas.Series.str.cat")<br>(\[others, sep, na\_rep, join\]) | Concatenate strings in the Series/Index with given separator. |
| [`Series.str.center`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.center.html#pandas.Series.str.center "pandas.Series.str.center")<br>(width\[, fillchar\]) | Pad left and right side of strings in the Series/Index. |
| [`Series.str.contains`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.contains.html#pandas.Series.str.contains "pandas.Series.str.contains")<br>(pat\[, case, flags, na, ...\]) | Test if pattern or regex is contained within a string of a Series or Index. |
| [`Series.str.count`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.count.html#pandas.Series.str.count "pandas.Series.str.count")<br>(pat\[, flags\]) | Count occurrences of pattern in each string of the Series/Index. |
| [`Series.str.decode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.decode.html#pandas.Series.str.decode "pandas.Series.str.decode")<br>(encoding\[, errors, dtype\]) | Decode character string in the Series/Index using indicated encoding. |
| [`Series.str.encode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.encode.html#pandas.Series.str.encode "pandas.Series.str.encode")<br>(encoding\[, errors\]) | Encode character string in the Series/Index using indicated encoding. |
| [`Series.str.endswith`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.endswith.html#pandas.Series.str.endswith "pandas.Series.str.endswith")<br>(pat\[, na\]) | Test if the end of each string element matches a pattern. |
| [`Series.str.extract`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extract.html#pandas.Series.str.extract "pandas.Series.str.extract")<br>(pat\[, flags, expand\]) | Extract capture groups in the regex pat as columns in a DataFrame. |
| [`Series.str.extractall`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.extractall.html#pandas.Series.str.extractall "pandas.Series.str.extractall")<br>(pat\[, flags\]) | Extract capture groups in the regex pat as columns in DataFrame. |
| [`Series.str.find`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.find.html#pandas.Series.str.find "pandas.Series.str.find")<br>(sub\[, start, end\]) | Return lowest indexes in each strings in the Series/Index. |
| [`Series.str.findall`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.findall.html#pandas.Series.str.findall "pandas.Series.str.findall")<br>(pat\[, flags\]) | Find all occurrences of pattern or regular expression in the Series/Index. |
| [`Series.str.fullmatch`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.fullmatch.html#pandas.Series.str.fullmatch "pandas.Series.str.fullmatch")<br>(pat\[, case, flags, na\]) | Determine if each string entirely matches a regular expression. |
| [`Series.str.get`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get.html#pandas.Series.str.get "pandas.Series.str.get")<br>(i) | Extract element from each component at specified position or with specified key. |
| [`Series.str.index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.index.html#pandas.Series.str.index "pandas.Series.str.index")<br>(sub\[, start, end\]) | Return lowest indexes in each string in Series/Index. |
| [`Series.str.isascii`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isascii.html#pandas.Series.str.isascii "pandas.Series.str.isascii")<br>() | Check whether all characters in each string are ascii. |
| [`Series.str.join`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.join.html#pandas.Series.str.join "pandas.Series.str.join")<br>(sep) | Join lists contained as elements in the Series/Index with passed delimiter. |
| [`Series.str.len`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.len.html#pandas.Series.str.len "pandas.Series.str.len")<br>() | Compute the length of each element in the Series/Index. |
| [`Series.str.ljust`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.ljust.html#pandas.Series.str.ljust "pandas.Series.str.ljust")<br>(width\[, fillchar\]) | Pad right side of strings in the Series/Index. |
| [`Series.str.lower`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html#pandas.Series.str.lower "pandas.Series.str.lower")<br>() | Convert strings in the Series/Index to lowercase. |
| [`Series.str.lstrip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lstrip.html#pandas.Series.str.lstrip "pandas.Series.str.lstrip")<br>(\[to\_strip\]) | Remove leading characters. |
| [`Series.str.match`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.match.html#pandas.Series.str.match "pandas.Series.str.match")<br>(pat\[, case, flags, na\]) | Determine if each string starts with a match of a regular expression. |
| [`Series.str.normalize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.normalize.html#pandas.Series.str.normalize "pandas.Series.str.normalize")<br>(form) | Return the Unicode normal form for the strings in the Series/Index. |
| [`Series.str.pad`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.pad.html#pandas.Series.str.pad "pandas.Series.str.pad")<br>(width\[, side, fillchar\]) | Pad strings in the Series/Index up to width. |
| [`Series.str.partition`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.partition.html#pandas.Series.str.partition "pandas.Series.str.partition")<br>(\[sep, expand\]) | Split the string at the first occurrence of sep. |
| [`Series.str.removeprefix`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.removeprefix.html#pandas.Series.str.removeprefix "pandas.Series.str.removeprefix")<br>(prefix) | Remove a prefix from an object series. |
| [`Series.str.removesuffix`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.removesuffix.html#pandas.Series.str.removesuffix "pandas.Series.str.removesuffix")<br>(suffix) | Remove a suffix from an object series. |
| [`Series.str.repeat`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.repeat.html#pandas.Series.str.repeat "pandas.Series.str.repeat")<br>(repeats) | Duplicate each string in the Series or Index. |
| [`Series.str.replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.replace.html#pandas.Series.str.replace "pandas.Series.str.replace")<br>(pat\[, repl, n, case, ...\]) | Replace each occurrence of pattern/regex in the Series/Index. |
| [`Series.str.rfind`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rfind.html#pandas.Series.str.rfind "pandas.Series.str.rfind")<br>(sub\[, start, end\]) | Return highest indexes in each strings in the Series/Index. |
| [`Series.str.rindex`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rindex.html#pandas.Series.str.rindex "pandas.Series.str.rindex")<br>(sub\[, start, end\]) | Return highest indexes in each string in Series/Index. |
| [`Series.str.rjust`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rjust.html#pandas.Series.str.rjust "pandas.Series.str.rjust")<br>(width\[, fillchar\]) | Pad left side of strings in the Series/Index. |
| [`Series.str.rpartition`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rpartition.html#pandas.Series.str.rpartition "pandas.Series.str.rpartition")<br>(\[sep, expand\]) | Split the string at the last occurrence of sep. |
| [`Series.str.rstrip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rstrip.html#pandas.Series.str.rstrip "pandas.Series.str.rstrip")<br>(\[to\_strip\]) | Remove trailing characters. |
| [`Series.str.slice`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice.html#pandas.Series.str.slice "pandas.Series.str.slice")<br>(\[start, stop, step\]) | Slice substrings from each element in the Series or Index. |
| [`Series.str.slice_replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.slice_replace.html#pandas.Series.str.slice_replace "pandas.Series.str.slice_replace")<br>(\[start, stop, repl\]) | Replace a positional slice of a string with another value. |
| [`Series.str.split`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html#pandas.Series.str.split "pandas.Series.str.split")<br>(\[pat, n, expand, regex\]) | Split strings around given separator/delimiter. |
| [`Series.str.rsplit`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.rsplit.html#pandas.Series.str.rsplit "pandas.Series.str.rsplit")<br>(\[pat, n, expand\]) | Split strings around given separator/delimiter. |
| [`Series.str.startswith`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.startswith.html#pandas.Series.str.startswith "pandas.Series.str.startswith")<br>(pat\[, na\]) | Test if the start of each string element matches a pattern. |
| [`Series.str.strip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.strip.html#pandas.Series.str.strip "pandas.Series.str.strip")<br>(\[to\_strip\]) | Remove leading and trailing characters. |
| [`Series.str.swapcase`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.swapcase.html#pandas.Series.str.swapcase "pandas.Series.str.swapcase")<br>() | Convert strings in the Series/Index to be swapcased. |
| [`Series.str.title`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.title.html#pandas.Series.str.title "pandas.Series.str.title")<br>() | Convert strings in the Series/Index to titlecase. |
| [`Series.str.translate`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.translate.html#pandas.Series.str.translate "pandas.Series.str.translate")<br>(table) | Map all characters in the string through the given mapping table. |
| [`Series.str.upper`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.upper.html#pandas.Series.str.upper "pandas.Series.str.upper")<br>() | Convert strings in the Series/Index to uppercase. |
| [`Series.str.wrap`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.wrap.html#pandas.Series.str.wrap "pandas.Series.str.wrap")<br>(width\[, expand\_tabs, ...\]) | Wrap strings in Series/Index at specified line width. |
| [`Series.str.zfill`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.zfill.html#pandas.Series.str.zfill "pandas.Series.str.zfill")<br>(width) | Pad strings in the Series/Index by prepending '0' characters. |
| [`Series.str.isalnum`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isalnum.html#pandas.Series.str.isalnum "pandas.Series.str.isalnum")<br>() | Check whether all characters in each string are alphanumeric. |
| [`Series.str.isalpha`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isalpha.html#pandas.Series.str.isalpha "pandas.Series.str.isalpha")<br>() | Check whether all characters in each string are alphabetic. |
| [`Series.str.isdigit`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isdigit.html#pandas.Series.str.isdigit "pandas.Series.str.isdigit")<br>() | Check whether all characters in each string are digits. |
| [`Series.str.isspace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isspace.html#pandas.Series.str.isspace "pandas.Series.str.isspace")<br>() | Check whether all characters in each string are whitespace. |
| [`Series.str.islower`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.islower.html#pandas.Series.str.islower "pandas.Series.str.islower")<br>() | Check whether all characters in each string are lowercase. |
| [`Series.str.isupper`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isupper.html#pandas.Series.str.isupper "pandas.Series.str.isupper")<br>() | Check whether all characters in each string are uppercase. |
| [`Series.str.istitle`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.istitle.html#pandas.Series.str.istitle "pandas.Series.str.istitle")<br>() | Check whether all characters in each string are titlecase. |
| [`Series.str.isnumeric`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isnumeric.html#pandas.Series.str.isnumeric "pandas.Series.str.isnumeric")<br>() | Check whether all characters in each string are numeric. |
| [`Series.str.isdecimal`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.isdecimal.html#pandas.Series.str.isdecimal "pandas.Series.str.isdecimal")<br>() | Check whether all characters in each string are decimal. |
| [`Series.str.get_dummies`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.get_dummies.html#pandas.Series.str.get_dummies "pandas.Series.str.get_dummies")<br>(\[sep, dtype\]) | Return DataFrame of dummy/indicator variables for Series. |

### Categorical accessor[#](https://pandas.pydata.org/docs/reference/series.html#categorical-accessor "Link to this heading")

Categorical-dtype specific methods and attributes are available under the `Series.cat` accessor.

|     |     |
| --- | --- |
| [`Series.cat.categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.categories.html#pandas.Series.cat.categories "pandas.Series.cat.categories") | The categories of this categorical. |
| [`Series.cat.ordered`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.ordered.html#pandas.Series.cat.ordered "pandas.Series.cat.ordered") | Whether the categories have an ordered relationship. |
| [`Series.cat.codes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.codes.html#pandas.Series.cat.codes "pandas.Series.cat.codes") | Return Series of codes as well as the index. |

|     |     |
| --- | --- |
| [`Series.cat.rename_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.rename_categories.html#pandas.Series.cat.rename_categories "pandas.Series.cat.rename_categories")<br>(new\_categories) | Rename categories. |
| [`Series.cat.reorder_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.reorder_categories.html#pandas.Series.cat.reorder_categories "pandas.Series.cat.reorder_categories")<br>(new\_categories) | Reorder categories as specified in new\_categories. |
| [`Series.cat.add_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.add_categories.html#pandas.Series.cat.add_categories "pandas.Series.cat.add_categories")<br>(new\_categories) | Add new categories. |
| [`Series.cat.remove_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_categories.html#pandas.Series.cat.remove_categories "pandas.Series.cat.remove_categories")<br>(removals) | Remove the specified categories. |
| [`Series.cat.remove_unused_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.remove_unused_categories.html#pandas.Series.cat.remove_unused_categories "pandas.Series.cat.remove_unused_categories")<br>() | Remove categories which are not used. |
| [`Series.cat.set_categories`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.set_categories.html#pandas.Series.cat.set_categories "pandas.Series.cat.set_categories")<br>(new\_categories\[, ...\]) | Set the categories to the specified new categories. |
| [`Series.cat.as_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.as_ordered.html#pandas.Series.cat.as_ordered "pandas.Series.cat.as_ordered")<br>() | Set the Categorical to be ordered. |
| [`Series.cat.as_unordered`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cat.as_unordered.html#pandas.Series.cat.as_unordered "pandas.Series.cat.as_unordered")<br>() | Set the Categorical to be unordered. |

### Sparse accessor[#](https://pandas.pydata.org/docs/reference/series.html#sparse-accessor "Link to this heading")

Sparse-dtype specific methods and attributes are provided under the `Series.sparse` accessor.

|     |     |
| --- | --- |
| [`Series.sparse.npoints`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.npoints.html#pandas.Series.sparse.npoints "pandas.Series.sparse.npoints") | The number of non- `fill_value` points. |
| [`Series.sparse.density`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.density.html#pandas.Series.sparse.density "pandas.Series.sparse.density") | The percent of non- `fill_value` points, as decimal. |
| [`Series.sparse.fill_value`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.fill_value.html#pandas.Series.sparse.fill_value "pandas.Series.sparse.fill_value") | Elements in data that are fill\_value are not stored. |
| [`Series.sparse.sp_values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.sp_values.html#pandas.Series.sparse.sp_values "pandas.Series.sparse.sp_values") | An ndarray containing the non- `fill_value` values. |

|     |     |
| --- | --- |
| [`Series.sparse.from_coo`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.from_coo.html#pandas.Series.sparse.from_coo "pandas.Series.sparse.from_coo")<br>(A\[, dense\_index\]) | Create a Series with sparse values from a scipy.sparse.coo\_matrix. |
| [`Series.sparse.to_coo`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sparse.to_coo.html#pandas.Series.sparse.to_coo "pandas.Series.sparse.to_coo")<br>(\[row\_levels, ...\]) | Create a scipy.sparse.coo\_matrix from a Series with MultiIndex. |

### List accessor[#](https://pandas.pydata.org/docs/reference/series.html#list-accessor "Link to this heading")

Arrow list-dtype specific methods and attributes are provided under the `Series.list` accessor.

|     |     |
| --- | --- |
| [`Series.list.flatten`](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.flatten.html#pandas.Series.list.flatten "pandas.Series.list.flatten")<br>() | Flatten list values. |
| [`Series.list.len`](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.len.html#pandas.Series.list.len "pandas.Series.list.len")<br>() | Return the length of each list in the Series. |
| [`Series.list.__getitem__`](https://pandas.pydata.org/docs/reference/api/pandas.Series.list.__getitem__.html#pandas.Series.list.__getitem__ "pandas.Series.list.__getitem__")<br>(key) | Index or slice lists in the Series. |

### Struct accessor[#](https://pandas.pydata.org/docs/reference/series.html#struct-accessor "Link to this heading")

Arrow struct-dtype specific methods and attributes are provided under the `Series.struct` accessor.

|     |     |
| --- | --- |
| [`Series.struct.dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.dtypes.html#pandas.Series.struct.dtypes "pandas.Series.struct.dtypes") | Return the dtype object of each child field of the struct. |

|     |     |
| --- | --- |
| [`Series.struct.field`](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.field.html#pandas.Series.struct.field "pandas.Series.struct.field")<br>(name\_or\_index) | Extract a child field of a struct as a Series. |
| [`Series.struct.explode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.struct.explode.html#pandas.Series.struct.explode "pandas.Series.struct.explode")<br>() | Extract all child fields of a struct as a DataFrame. |

### Flags[#](https://pandas.pydata.org/docs/reference/series.html#flags "Link to this heading")

Flags refer to attributes of the pandas object. Properties of the dataset (like the date it was recorded, the URL it was accessed from, etc.) should be stored in [`Series.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.Series.attrs.html#pandas.Series.attrs "pandas.Series.attrs")
.

|     |     |
| --- | --- |
| [`Flags`](https://pandas.pydata.org/docs/reference/api/pandas.Flags.html#pandas.Flags "pandas.Flags")<br>(obj, \*, allows\_duplicate\_labels) | Flags that apply to pandas objects. |

### Metadata[#](https://pandas.pydata.org/docs/reference/series.html#metadata "Link to this heading")

[`Series.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.Series.attrs.html#pandas.Series.attrs "pandas.Series.attrs")
 is a dictionary for storing global metadata for this Series.

Warning

`Series.attrs` is considered experimental and may change without warning.

|     |     |
| --- | --- |
| [`Series.attrs`](https://pandas.pydata.org/docs/reference/api/pandas.Series.attrs.html#pandas.Series.attrs "pandas.Series.attrs") | Dictionary of global attributes of this dataset. |

Plotting[#](https://pandas.pydata.org/docs/reference/series.html#plotting "Link to this heading")

--------------------------------------------------------------------------------------------------

`Series.plot` is both a callable method and a namespace attribute for specific plotting methods of the form `Series.plot.<kind>`.

|     |     |
| --- | --- |
| [`Series.plot`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.html#pandas.Series.plot "pandas.Series.plot")<br>(\[kind, ax, figsize, ....\]) | Series plotting accessor and method |

|     |     |
| --- | --- |
| [`Series.plot.area`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.area.html#pandas.Series.plot.area "pandas.Series.plot.area")<br>(\[x, y, stacked\]) | Make a stacked area plot. |
| [`Series.plot.bar`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.bar.html#pandas.Series.plot.bar "pandas.Series.plot.bar")<br>(\[x, y, color\]) | Make a vertical bar plot. |
| [`Series.plot.barh`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.barh.html#pandas.Series.plot.barh "pandas.Series.plot.barh")<br>(\[x, y, color\]) | Make a horizontal bar plot. |
| [`Series.plot.box`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.box.html#pandas.Series.plot.box "pandas.Series.plot.box")<br>(\[by\]) | Make a box plot of the DataFrame columns. |
| [`Series.plot.density`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.density.html#pandas.Series.plot.density "pandas.Series.plot.density")<br>(\[bw\_method, ind, weights\]) | Make a Kernel Density Estimate plot using Gaussian kernels. |
| [`Series.plot.hist`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.hist.html#pandas.Series.plot.hist "pandas.Series.plot.hist")<br>(\[by, bins\]) | Make one histogram of the DataFrame's columns. |
| [`Series.plot.kde`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.kde.html#pandas.Series.plot.kde "pandas.Series.plot.kde")<br>(\[bw\_method, ind, weights\]) | Make a Kernel Density Estimate plot using Gaussian kernels. |
| [`Series.plot.line`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.line.html#pandas.Series.plot.line "pandas.Series.plot.line")<br>(\[x, y, color\]) | Make a line plot of a Series or DataFrame. |
| [`Series.plot.pie`](https://pandas.pydata.org/docs/reference/api/pandas.Series.plot.pie.html#pandas.Series.plot.pie "pandas.Series.plot.pie")<br>(\[y\]) | Make a pie plot. |

|     |     |
| --- | --- |
| [`Series.hist`](https://pandas.pydata.org/docs/reference/api/pandas.Series.hist.html#pandas.Series.hist "pandas.Series.hist")<br>(\[by, ax, grid, xlabelsize, ...\]) | Draw histogram of the input series using matplotlib. |

Serialization / IO / conversion[#](https://pandas.pydata.org/docs/reference/series.html#serialization-io-conversion "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Series.from_arrow`](https://pandas.pydata.org/docs/reference/api/pandas.Series.from_arrow.html#pandas.Series.from_arrow "pandas.Series.from_arrow")<br>(data) | Construct a Series from an array-like Arrow object. |
| [`Series.to_pickle`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_pickle.html#pandas.Series.to_pickle "pandas.Series.to_pickle")<br>(path, \*\[, compression, ...\]) | Pickle (serialize) object to file. |
| [`Series.to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_csv.html#pandas.Series.to_csv "pandas.Series.to_csv")<br>(\[path\_or\_buf, sep, na\_rep, ...\]) | Write object to a comma-separated values (csv) file. |
| [`Series.to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_dict.html#pandas.Series.to_dict "pandas.Series.to_dict")<br>(\*\[, into\]) | Convert Series to {label -> value} dict or dict-like object. |
| [`Series.to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_excel.html#pandas.Series.to_excel "pandas.Series.to_excel")<br>(excel\_writer, \*\[, ...\]) | Write object to an Excel sheet. |
| [`Series.to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame "pandas.Series.to_frame")<br>(\[name\]) | Convert Series to DataFrame. |
| [`Series.to_xarray`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_xarray.html#pandas.Series.to_xarray "pandas.Series.to_xarray")<br>() | Return an xarray object from the pandas object. |
| [`Series.to_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_hdf.html#pandas.Series.to_hdf "pandas.Series.to_hdf")<br>(path\_or\_buf, \*, key\[, mode, ...\]) | Write the contained data to an HDF5 file using HDFStore. |
| [`Series.to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_sql.html#pandas.Series.to_sql "pandas.Series.to_sql")<br>(name, con, \*\[, schema, ...\]) | Write records stored in a DataFrame to a SQL database. |
| [`Series.to_json`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_json.html#pandas.Series.to_json "pandas.Series.to_json")<br>(\[path\_or\_buf, orient, ...\]) | Convert the object to a JSON string. |
| [`Series.to_string`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_string.html#pandas.Series.to_string "pandas.Series.to_string")<br>(\[buf, na\_rep, ...\]) | Render a string representation of the Series. |
| [`Series.to_clipboard`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_clipboard.html#pandas.Series.to_clipboard "pandas.Series.to_clipboard")<br>(\*\[, excel, sep\]) | Copy object to the system clipboard. |
| [`Series.to_latex`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_latex.html#pandas.Series.to_latex "pandas.Series.to_latex")<br>(\[buf, columns, header, ...\]) | Render object to a LaTeX tabular, longtable, or nested table. |
| [`Series.to_markdown`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_markdown.html#pandas.Series.to_markdown "pandas.Series.to_markdown")<br>(\[buf, mode, index, ...\]) | Print Series in Markdown-friendly format. |

On this page