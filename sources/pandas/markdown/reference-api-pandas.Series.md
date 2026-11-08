[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas-series "Link to this heading")

=======================================================================================================================

class pandas.Series(_data\=None_, _index\=None_, _dtype\=None_, _name\=None_, _copy\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L218-L10358)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "Link to this definition")

One-dimensional ndarray with axis labels (including time series).

Labels need not be unique but must be a hashable type. The object supports both integer- and label-based indexing and provides a host of methods for performing operations involving the index. Statistical methods from ndarray have been overridden to automatically exclude missing data (currently represented as NaN).

Operations between Series (+, -, /, \*, \*\*) align values based on their associated index values– they need not be the same length. The result index will be the sorted union of the two indexes.

Parameters:

**data**array-like, Iterable, dict, or scalar value

Contains data stored in Series. If data is a dict, argument order is maintained. Unordered sets are not supported.

**index**array-like or Index (1d)

Values must be hashable and have the same length as data. Non-unique index values are allowed. Will default to RangeIndex (0, 1, 2, …, n) if not provided. If data is dict-like and index is None, then the keys in the data are used as the index. If the index is not None, the resulting Series is reindexed with the index values.

**dtype**str, numpy.dtype, or ExtensionDtype, optional

Data type for the output Series. If not specified, this will be inferred from data. See the [user guide](https://pandas.pydata.org/docs/user_guide/basics.html#basics-dtypes)
 for more usages.

**name**Hashable, default None

The name to give to the Series.

**copy**bool, default None

Whether to copy input data, only relevant for array, Series, and Index inputs (for other input, e.g. a list, a new array is created anyway). Defaults to True for array input and False for Index/Series. Even when False for Index/Series, a shallow copy of the data is made. Set to False to avoid copying array input at your own risk (if you know the input data won’t be modified elsewhere). Set to True to force copying Series/Index input up front.

See also

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")

Two-dimensional, size-mutable, potentially heterogeneous tabular data.

[`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")

Immutable sequence used for indexing and alignment.

Notes

Please reference the [User Guide](https://pandas.pydata.org/docs/user_guide/dsintro.html#basics-series)
 for more information.

NumPy arrays with `dtype=object` may be inferred to a more specific dtype (e.g. strings or datetimes) rather than keeping object dtype, similar to passing a Python list. Pass `dtype=object` when you need object dtype. The same inference rules apply when building an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 from such an array.

Examples

Constructing Series from a dictionary with an Index specified

\>>> d \= {"a": 1, "b": 2, "c": 3}
\>>> ser \= pd.Series(data\=d, index\=\["a", "b", "c"\])
\>>> ser
a   1
b   2
c   3
dtype: int64

Copy to clipboard

The keys of the dictionary match with the Index values, hence the Index values have no effect.

\>>> d \= {"a": 1, "b": 2, "c": 3}
\>>> ser \= pd.Series(data\=d, index\=\["x", "y", "z"\])
\>>> ser
x   NaN
y   NaN
z   NaN
dtype: float64

Copy to clipboard

Note that the Index is first built with the keys from the dictionary. After this the Series is reindexed with the given Index values, hence we get all NaN as a result.

Constructing Series from a list with copy=False.

\>>> r \= \[1, 2\]
\>>> ser \= pd.Series(r, copy\=False)
\>>> ser.iloc\[0\] \= 999
\>>> r
\[1, 2\]
\>>> ser
0    999
1      2
dtype: int64

Copy to clipboard

Due to input data type the Series has a copy of the original data even though copy=False, so the data is unchanged.

Constructing Series from a 1d ndarray with copy=False.

\>>> r \= np.array(\[1, 2\])
\>>> ser \= pd.Series(r, copy\=False)
\>>> ser.iloc\[0\] \= 999
\>>> r
array(\[999,   2\])
\>>> ser
0    999
1      2
dtype: int64

Copy to clipboard

Due to input data type the Series has a view on the original data, so the data is changed as well.

Attributes

|     |     |
| --- | --- |
| [`T`](https://pandas.pydata.org/docs/reference/api/pandas.Series.T.html#pandas.Series.T "pandas.Series.T") | Return the transpose, which is by definition self. |
| [`array`](https://pandas.pydata.org/docs/reference/api/pandas.Series.array.html#pandas.Series.array "pandas.Series.array") | The ExtensionArray of the data backing this Series or Index. |
| [`at`](https://pandas.pydata.org/docs/reference/api/pandas.Series.at.html#pandas.Series.at "pandas.Series.at") | Access a single value for a row/column label pair. |
| [`attrs`](https://pandas.pydata.org/docs/reference/api/pandas.Series.attrs.html#pandas.Series.attrs "pandas.Series.attrs") | Dictionary of global attributes of this dataset. |
| `axes` | Return a list of the row axis labels. |
| [`dtype`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtype.html#pandas.Series.dtype "pandas.Series.dtype") | Return the dtype object of the underlying data. |
| [`dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dtypes.html#pandas.Series.dtypes "pandas.Series.dtypes") | Return the dtype object of the underlying data. |
| [`empty`](https://pandas.pydata.org/docs/reference/api/pandas.Series.empty.html#pandas.Series.empty "pandas.Series.empty") | Indicator whether Index is empty. |
| [`flags`](https://pandas.pydata.org/docs/reference/api/pandas.Series.flags.html#pandas.Series.flags "pandas.Series.flags") | Get the properties associated with this pandas object. |
| [`hasnans`](https://pandas.pydata.org/docs/reference/api/pandas.Series.hasnans.html#pandas.Series.hasnans "pandas.Series.hasnans") | Return True if there are any NaNs. |
| [`iat`](https://pandas.pydata.org/docs/reference/api/pandas.Series.iat.html#pandas.Series.iat "pandas.Series.iat") | Access a single value for a row/column pair by integer position. |
| [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.Series.iloc.html#pandas.Series.iloc "pandas.Series.iloc") | Purely integer-location based indexing for selection by position. |
| [`index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.index.html#pandas.Series.index "pandas.Series.index") | The index (axis labels) of the Series. |
| [`is_monotonic_decreasing`](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_decreasing.html#pandas.Series.is_monotonic_decreasing "pandas.Series.is_monotonic_decreasing") | Return True if values in the object are monotonically decreasing. |
| [`is_monotonic_increasing`](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_monotonic_increasing.html#pandas.Series.is_monotonic_increasing "pandas.Series.is_monotonic_increasing") | Return True if values in the object are monotonically increasing. |
| [`is_unique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.is_unique.html#pandas.Series.is_unique "pandas.Series.is_unique") | Return True if values in the object are unique. |
| [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.Series.loc.html#pandas.Series.loc "pandas.Series.loc") | Access a group of rows and columns by label(s) or a boolean array. |
| [`name`](https://pandas.pydata.org/docs/reference/api/pandas.Series.name.html#pandas.Series.name "pandas.Series.name") | Return the name of the Series. |
| [`nbytes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nbytes.html#pandas.Series.nbytes "pandas.Series.nbytes") | Return the number of bytes in the underlying data. |
| [`ndim`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ndim.html#pandas.Series.ndim "pandas.Series.ndim") | Number of dimensions of the underlying data, by definition 1. |
| [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.Series.shape.html#pandas.Series.shape "pandas.Series.shape") | Return a tuple of the shape of the underlying data. |
| [`size`](https://pandas.pydata.org/docs/reference/api/pandas.Series.size.html#pandas.Series.size "pandas.Series.size") | Return the number of elements in the underlying data. |
| [`values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.values.html#pandas.Series.values "pandas.Series.values") | Return Series as ndarray or ndarray-like depending on the dtype. |

Methods

|     |     |
| --- | --- |
| [`abs`](https://pandas.pydata.org/docs/reference/api/pandas.Series.abs.html#pandas.Series.abs "pandas.Series.abs")<br>() | Return a Series/DataFrame with absolute numeric value of each element. |
| [`add`](https://pandas.pydata.org/docs/reference/api/pandas.Series.add.html#pandas.Series.add "pandas.Series.add")<br>(other\[, level, fill\_value, axis\]) | Return Addition of series and other, element-wise (binary operator add). |
| [`add_prefix`](https://pandas.pydata.org/docs/reference/api/pandas.Series.add_prefix.html#pandas.Series.add_prefix "pandas.Series.add_prefix")<br>(prefix\[, axis\]) | Prefix labels with string prefix. |
| [`add_suffix`](https://pandas.pydata.org/docs/reference/api/pandas.Series.add_suffix.html#pandas.Series.add_suffix "pandas.Series.add_suffix")<br>(suffix\[, axis\]) | Suffix labels with string suffix. |
| [`agg`](https://pandas.pydata.org/docs/reference/api/pandas.Series.agg.html#pandas.Series.agg "pandas.Series.agg")<br>(\[func, axis\]) | Aggregate using one or more operations over the specified axis. |
| [`aggregate`](https://pandas.pydata.org/docs/reference/api/pandas.Series.aggregate.html#pandas.Series.aggregate "pandas.Series.aggregate")<br>(\[func, axis\]) | Aggregate using one or more operations over the specified axis. |
| [`align`](https://pandas.pydata.org/docs/reference/api/pandas.Series.align.html#pandas.Series.align "pandas.Series.align")<br>(other\[, join, axis, level, copy, ...\]) | Align two objects on their axes with the specified join method. |
| [`all`](https://pandas.pydata.org/docs/reference/api/pandas.Series.all.html#pandas.Series.all "pandas.Series.all")<br>(\*\[, axis, bool\_only, skipna\]) | Return whether all elements are True, potentially over an axis. |
| [`any`](https://pandas.pydata.org/docs/reference/api/pandas.Series.any.html#pandas.Series.any "pandas.Series.any")<br>(\*\[, axis, bool\_only, skipna\]) | Return whether any element is True, potentially over an axis. |
| [`apply`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#pandas.Series.apply "pandas.Series.apply")<br>(func\[, args, by\_row\]) | Invoke function on values of Series. |
| [`argmax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmax.html#pandas.Series.argmax "pandas.Series.argmax")<br>(\[axis, skipna\]) | Return int position of the largest value in the Series. |
| [`argmin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.argmin.html#pandas.Series.argmin "pandas.Series.argmin")<br>(\[axis, skipna\]) | Return int position of the smallest value in the Series. |
| [`argsort`](https://pandas.pydata.org/docs/reference/api/pandas.Series.argsort.html#pandas.Series.argsort "pandas.Series.argsort")<br>(\[axis, kind, order, stable\]) | Return the integer indices that would sort the Series values. |
| [`asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.Series.asfreq.html#pandas.Series.asfreq "pandas.Series.asfreq")<br>(freq\[, method, how, normalize, ...\]) | Convert time series to specified frequency. |
| [`asof`](https://pandas.pydata.org/docs/reference/api/pandas.Series.asof.html#pandas.Series.asof "pandas.Series.asof")<br>(where\[, subset\]) | Return the last row(s) without any NaNs before where. |
| [`astype`](https://pandas.pydata.org/docs/reference/api/pandas.Series.astype.html#pandas.Series.astype "pandas.Series.astype")<br>(dtype\[, copy, errors\]) | Cast a pandas object to a specified dtype `dtype`. |
| [`at_time`](https://pandas.pydata.org/docs/reference/api/pandas.Series.at_time.html#pandas.Series.at_time "pandas.Series.at_time")<br>(time\[, asof, axis\]) | Select values at particular time of day (e.g., 9:30AM). |
| [`autocorr`](https://pandas.pydata.org/docs/reference/api/pandas.Series.autocorr.html#pandas.Series.autocorr "pandas.Series.autocorr")<br>(\[lag\]) | Compute the lag-N autocorrelation. |
| [`between`](https://pandas.pydata.org/docs/reference/api/pandas.Series.between.html#pandas.Series.between "pandas.Series.between")<br>(left, right\[, inclusive\]) | Return boolean Series equivalent to left <= series <= right. |
| [`between_time`](https://pandas.pydata.org/docs/reference/api/pandas.Series.between_time.html#pandas.Series.between_time "pandas.Series.between_time")<br>(start\_time, end\_time\[, ...\]) | Select values between particular times of the day (e.g., 9:00-9:30 AM). |
| [`bfill`](https://pandas.pydata.org/docs/reference/api/pandas.Series.bfill.html#pandas.Series.bfill "pandas.Series.bfill")<br>(\*\[, axis, inplace, limit, limit\_area\]) | Fill NA/NaN values by using the next valid observation to fill the gap. |
| [`case_when`](https://pandas.pydata.org/docs/reference/api/pandas.Series.case_when.html#pandas.Series.case_when "pandas.Series.case_when")<br>(caselist) | Replace values where the conditions are True. |
| [`clip`](https://pandas.pydata.org/docs/reference/api/pandas.Series.clip.html#pandas.Series.clip "pandas.Series.clip")<br>(\[lower, upper, axis, inplace\]) | Trim values at input threshold(s). |
| [`combine`](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine.html#pandas.Series.combine "pandas.Series.combine")<br>(other, func\[, fill\_value\]) | Combine the Series with a Series or scalar according to func. |
| [`combine_first`](https://pandas.pydata.org/docs/reference/api/pandas.Series.combine_first.html#pandas.Series.combine_first "pandas.Series.combine_first")<br>(other) | Update null elements with value in the same location in 'other'. |
| [`compare`](https://pandas.pydata.org/docs/reference/api/pandas.Series.compare.html#pandas.Series.compare "pandas.Series.compare")<br>(other\[, align\_axis, keep\_shape, ...\]) | Compare to another Series and show the differences. |
| [`convert_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.Series.convert_dtypes.html#pandas.Series.convert_dtypes "pandas.Series.convert_dtypes")<br>(\[infer\_objects, ...\]) | Convert columns from numpy dtypes to the best dtypes that support `pd.NA`. |
| [`copy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.copy.html#pandas.Series.copy "pandas.Series.copy")<br>(\[deep\]) | Make a copy of this object's indices and data. |
| [`corr`](https://pandas.pydata.org/docs/reference/api/pandas.Series.corr.html#pandas.Series.corr "pandas.Series.corr")<br>(other\[, method, min\_periods\]) | Compute correlation with other Series, excluding missing values. |
| [`count`](https://pandas.pydata.org/docs/reference/api/pandas.Series.count.html#pandas.Series.count "pandas.Series.count")<br>() | Return number of non-NA/null observations in the Series. |
| [`cov`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cov.html#pandas.Series.cov "pandas.Series.cov")<br>(other\[, min\_periods, ddof\]) | Compute covariance with Series, excluding missing values. |
| [`cummax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummax.html#pandas.Series.cummax "pandas.Series.cummax")<br>(\[axis, skipna\]) | Return cumulative maximum over a Series. |
| [`cummin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cummin.html#pandas.Series.cummin "pandas.Series.cummin")<br>(\[axis, skipna\]) | Return cumulative minimum over a Series. |
| [`cumprod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cumprod.html#pandas.Series.cumprod "pandas.Series.cumprod")<br>(\[axis, skipna\]) | Return cumulative product over a Series. |
| [`cumsum`](https://pandas.pydata.org/docs/reference/api/pandas.Series.cumsum.html#pandas.Series.cumsum "pandas.Series.cumsum")<br>(\[axis, skipna\]) | Return cumulative sum over a Series. |
| [`describe`](https://pandas.pydata.org/docs/reference/api/pandas.Series.describe.html#pandas.Series.describe "pandas.Series.describe")<br>(\[percentiles, include, exclude\]) | Generate descriptive statistics. |
| [`diff`](https://pandas.pydata.org/docs/reference/api/pandas.Series.diff.html#pandas.Series.diff "pandas.Series.diff")<br>(\[periods\]) | First discrete difference of Series elements. |
| [`div`](https://pandas.pydata.org/docs/reference/api/pandas.Series.div.html#pandas.Series.div "pandas.Series.div")<br>(other\[, level, fill\_value, axis\]) | Return Floating division of series and other, element-wise (binary operator truediv). |
| `divide`(other\[, level, fill\_value, axis\]) | Return Floating division of series and other, element-wise (binary operator truediv). |
| [`divmod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.divmod.html#pandas.Series.divmod "pandas.Series.divmod")<br>(other\[, level, fill\_value, axis\]) | Return Integer division and modulo of series and other, element-wise (binary operator divmod). |
| [`dot`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dot.html#pandas.Series.dot "pandas.Series.dot")<br>(other) | Compute the dot product between the Series and the columns of other. |
| [`drop`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop.html#pandas.Series.drop "pandas.Series.drop")<br>(\[labels, axis, index, columns, level, ...\]) | Return Series with specified index labels removed. |
| [`drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.Series.drop_duplicates.html#pandas.Series.drop_duplicates "pandas.Series.drop_duplicates")<br>(\*\[, keep, inplace, ignore\_index\]) | Return Series with duplicate values removed. |
| [`droplevel`](https://pandas.pydata.org/docs/reference/api/pandas.Series.droplevel.html#pandas.Series.droplevel "pandas.Series.droplevel")<br>(level\[, axis\]) | Return Series/DataFrame with requested index / column level(s) removed. |
| [`dropna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.dropna.html#pandas.Series.dropna "pandas.Series.dropna")<br>(\*\[, axis, inplace, how, ignore\_index\]) | Return a new Series with missing values removed. |
| [`duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.Series.duplicated.html#pandas.Series.duplicated "pandas.Series.duplicated")<br>(\[keep\]) | Indicate duplicate Series values. |
| [`eq`](https://pandas.pydata.org/docs/reference/api/pandas.Series.eq.html#pandas.Series.eq "pandas.Series.eq")<br>(other\[, level, fill\_value, axis\]) | Return Equal to of series and other, element-wise (binary operator eq). |
| [`equals`](https://pandas.pydata.org/docs/reference/api/pandas.Series.equals.html#pandas.Series.equals "pandas.Series.equals")<br>(other) | Test whether two objects contain the same elements. |
| [`ewm`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ewm.html#pandas.Series.ewm "pandas.Series.ewm")<br>(\[com, span, halflife, alpha, ...\]) | Provide exponentially weighted (EW) calculations. |
| [`expanding`](https://pandas.pydata.org/docs/reference/api/pandas.Series.expanding.html#pandas.Series.expanding "pandas.Series.expanding")<br>(\[min\_periods, method\]) | Provide expanding window calculations. |
| [`explode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.explode.html#pandas.Series.explode "pandas.Series.explode")<br>(\[ignore\_index\]) | Transform each element of a list-like to a row. |
| [`factorize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.factorize.html#pandas.Series.factorize "pandas.Series.factorize")<br>(\[sort, use\_na\_sentinel\]) | Encode the object as an enumerated type or categorical variable. |
| [`ffill`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ffill.html#pandas.Series.ffill "pandas.Series.ffill")<br>(\*\[, axis, inplace, limit, limit\_area\]) | Fill NA/NaN values by propagating the last valid observation to next valid. |
| [`fillna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.fillna.html#pandas.Series.fillna "pandas.Series.fillna")<br>(value, \*\[, axis, inplace, limit\]) | Fill NA/NaN values with value. |
| [`filter`](https://pandas.pydata.org/docs/reference/api/pandas.Series.filter.html#pandas.Series.filter "pandas.Series.filter")<br>(\[arg, like, regex, axis, items, cond, na\]) | Subset the rows or columns according to a boolean mask or the labels. |
| [`first_valid_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.first_valid_index.html#pandas.Series.first_valid_index "pandas.Series.first_valid_index")<br>() | Return index for first non-missing value or None, if no value is found. |
| [`floordiv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.floordiv.html#pandas.Series.floordiv "pandas.Series.floordiv")<br>(other\[, level, fill\_value, axis\]) | Return Integer division of series and other, element-wise (binary operator floordiv). |
| [`from_arrow`](https://pandas.pydata.org/docs/reference/api/pandas.Series.from_arrow.html#pandas.Series.from_arrow "pandas.Series.from_arrow")<br>(data) | Construct a Series from an array-like Arrow object. |
| [`ge`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ge.html#pandas.Series.ge "pandas.Series.ge")<br>(other\[, level, fill\_value, axis\]) | Return Greater than or equal to of series and other, element-wise (binary operator ge). |
| [`get`](https://pandas.pydata.org/docs/reference/api/pandas.Series.get.html#pandas.Series.get "pandas.Series.get")<br>(key\[, default\]) | Get item from object for given key (ex: DataFrame column). |
| [`groupby`](https://pandas.pydata.org/docs/reference/api/pandas.Series.groupby.html#pandas.Series.groupby "pandas.Series.groupby")<br>(\[by, level, as\_index, sort, ...\]) | Group Series using a mapper or by a Series of columns. |
| [`gt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.gt.html#pandas.Series.gt "pandas.Series.gt")<br>(other\[, level, fill\_value, axis\]) | Return Greater than of series and other, element-wise (binary operator gt). |
| [`head`](https://pandas.pydata.org/docs/reference/api/pandas.Series.head.html#pandas.Series.head "pandas.Series.head")<br>(\[n\]) | Return the first n rows. |
| [`hist`](https://pandas.pydata.org/docs/reference/api/pandas.Series.hist.html#pandas.Series.hist "pandas.Series.hist")<br>(\[by, ax, grid, xlabelsize, xrot, ...\]) | Draw histogram of the input series using matplotlib. |
| [`idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmax.html#pandas.Series.idxmax "pandas.Series.idxmax")<br>(\[axis, skipna\]) | Return the row label of the maximum value. |
| [`idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.idxmin.html#pandas.Series.idxmin "pandas.Series.idxmin")<br>(\[axis, skipna\]) | Return the row label of the minimum value. |
| [`infer_objects`](https://pandas.pydata.org/docs/reference/api/pandas.Series.infer_objects.html#pandas.Series.infer_objects "pandas.Series.infer_objects")<br>(\[copy\]) | Attempt to infer better dtypes for object columns. |
| [`info`](https://pandas.pydata.org/docs/reference/api/pandas.Series.info.html#pandas.Series.info "pandas.Series.info")<br>(\[verbose, buf, max\_cols, memory\_usage, ...\]) | Print a concise summary of a Series. |
| [`interpolate`](https://pandas.pydata.org/docs/reference/api/pandas.Series.interpolate.html#pandas.Series.interpolate "pandas.Series.interpolate")<br>(\[method, axis, limit, inplace, ...\]) | Fill NaN values using an interpolation method. |
| [`isin`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isin.html#pandas.Series.isin "pandas.Series.isin")<br>(values) | Whether elements in Series are contained in values. |
| [`isna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html#pandas.Series.isna "pandas.Series.isna")<br>() | Detect missing values. |
| [`isnull`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isnull.html#pandas.Series.isnull "pandas.Series.isnull")<br>() | Series.isnull is an alias for Series.isna. |
| [`item`](https://pandas.pydata.org/docs/reference/api/pandas.Series.item.html#pandas.Series.item "pandas.Series.item")<br>() | Return the first element of the underlying data as a Python scalar. |
| [`items`](https://pandas.pydata.org/docs/reference/api/pandas.Series.items.html#pandas.Series.items "pandas.Series.items")<br>() | Lazily iterate over (index, value) tuples. |
| [`keys`](https://pandas.pydata.org/docs/reference/api/pandas.Series.keys.html#pandas.Series.keys "pandas.Series.keys")<br>() | Return alias for index. |
| [`kurt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.kurt.html#pandas.Series.kurt "pandas.Series.kurt")<br>(\*\[, axis, skipna, numeric\_only\]) | Return unbiased kurtosis over requested axis. |
| [`kurtosis`](https://pandas.pydata.org/docs/reference/api/pandas.Series.kurtosis.html#pandas.Series.kurtosis "pandas.Series.kurtosis")<br>(\*\[, axis, skipna, numeric\_only\]) | Return unbiased kurtosis over requested axis. |
| [`last_valid_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.last_valid_index.html#pandas.Series.last_valid_index "pandas.Series.last_valid_index")<br>() | Return index for last non-missing value or None, if no value is found. |
| [`le`](https://pandas.pydata.org/docs/reference/api/pandas.Series.le.html#pandas.Series.le "pandas.Series.le")<br>(other\[, level, fill\_value, axis\]) | Return Less than or equal to of series and other, element-wise (binary operator le). |
| [`lt`](https://pandas.pydata.org/docs/reference/api/pandas.Series.lt.html#pandas.Series.lt "pandas.Series.lt")<br>(other\[, level, fill\_value, axis\]) | Return Less than of series and other, element-wise (binary operator lt). |
| [`map`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map "pandas.Series.map")<br>(\[func, na\_action, engine\]) | Map values of Series according to an input mapping or function. |
| [`mask`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mask.html#pandas.Series.mask "pandas.Series.mask")<br>(cond\[, other, inplace, axis, level\]) | Replace values where the condition is True. |
| [`max`](https://pandas.pydata.org/docs/reference/api/pandas.Series.max.html#pandas.Series.max "pandas.Series.max")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the maximum of the values over the requested axis. |
| [`mean`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mean.html#pandas.Series.mean "pandas.Series.mean")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the mean of the values over the requested axis. |
| [`median`](https://pandas.pydata.org/docs/reference/api/pandas.Series.median.html#pandas.Series.median "pandas.Series.median")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the median of the values over the requested axis. |
| [`memory_usage`](https://pandas.pydata.org/docs/reference/api/pandas.Series.memory_usage.html#pandas.Series.memory_usage "pandas.Series.memory_usage")<br>(\[index, deep\]) | Return the memory usage of the Series. |
| [`min`](https://pandas.pydata.org/docs/reference/api/pandas.Series.min.html#pandas.Series.min "pandas.Series.min")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the minimum of the values over the requested axis. |
| [`mod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mod.html#pandas.Series.mod "pandas.Series.mod")<br>(other\[, level, fill\_value, axis\]) | Return Modulo of series and other, element-wise (binary operator mod). |
| [`mode`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mode.html#pandas.Series.mode "pandas.Series.mode")<br>(\[dropna\]) | Return the mode(s) of the Series. |
| [`mul`](https://pandas.pydata.org/docs/reference/api/pandas.Series.mul.html#pandas.Series.mul "pandas.Series.mul")<br>(other\[, level, fill\_value, axis\]) | Return Multiplication of series and other, element-wise (binary operator mul). |
| `multiply`(other\[, level, fill\_value, axis\]) | Return Multiplication of series and other, element-wise (binary operator mul). |
| [`ne`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ne.html#pandas.Series.ne "pandas.Series.ne")<br>(other\[, level, fill\_value, axis\]) | Return Not equal to of series and other, element-wise (binary operator ne). |
| [`nlargest`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nlargest.html#pandas.Series.nlargest "pandas.Series.nlargest")<br>(\[n, keep\]) | Return the largest n elements. |
| [`notna`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html#pandas.Series.notna "pandas.Series.notna")<br>() | Detect existing (non-missing) values. |
| [`notnull`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notnull.html#pandas.Series.notnull "pandas.Series.notnull")<br>() | Series.notnull is an alias for Series.notna. |
| [`nsmallest`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nsmallest.html#pandas.Series.nsmallest "pandas.Series.nsmallest")<br>(\[n, keep\]) | Return the smallest n elements. |
| [`nunique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.nunique.html#pandas.Series.nunique "pandas.Series.nunique")<br>(\[dropna\]) | Return number of unique elements in the object. |
| [`pct_change`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pct_change.html#pandas.Series.pct_change "pandas.Series.pct_change")<br>(\[periods, fill\_method, freq\]) | Fractional change between the current and a prior element. |
| [`pipe`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pipe.html#pandas.Series.pipe "pandas.Series.pipe")<br>(func, \*args, \*\*kwargs) | Apply chainable functions that expect Series or DataFrames. |
| [`pop`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pop.html#pandas.Series.pop "pandas.Series.pop")<br>(item) | Return item and drops from series. |
| [`pow`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pow.html#pandas.Series.pow "pandas.Series.pow")<br>(other\[, level, fill\_value, axis\]) | Return Exponential power of series and other, element-wise (binary operator pow). |
| [`prod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.prod.html#pandas.Series.prod "pandas.Series.prod")<br>(\*\[, axis, skipna, numeric\_only, min\_count\]) | Return the product of the values over the requested axis. |
| [`product`](https://pandas.pydata.org/docs/reference/api/pandas.Series.product.html#pandas.Series.product "pandas.Series.product")<br>(\*\[, axis, skipna, numeric\_only, ...\]) | Return the product of the values over the requested axis. |
| [`quantile`](https://pandas.pydata.org/docs/reference/api/pandas.Series.quantile.html#pandas.Series.quantile "pandas.Series.quantile")<br>(\[q, interpolation\]) | Return value at the given quantile. |
| [`radd`](https://pandas.pydata.org/docs/reference/api/pandas.Series.radd.html#pandas.Series.radd "pandas.Series.radd")<br>(other\[, level, fill\_value, axis\]) | Return Addition of series and other, element-wise (binary operator radd). |
| [`rank`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rank.html#pandas.Series.rank "pandas.Series.rank")<br>(\[axis, method, numeric\_only, ...\]) | Compute numerical data ranks (1 through n) along axis. |
| [`rdiv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rdiv.html#pandas.Series.rdiv "pandas.Series.rdiv")<br>(other\[, level, fill\_value, axis\]) | Return Floating division of series and other, element-wise (binary operator rtruediv). |
| [`rdivmod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rdivmod.html#pandas.Series.rdivmod "pandas.Series.rdivmod")<br>(other\[, level, fill\_value, axis\]) | Return Integer division and modulo of series and other, element-wise (binary operator rdivmod). |
| [`reindex`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex.html#pandas.Series.reindex "pandas.Series.reindex")<br>(\[index, axis, method, copy, level, ...\]) | Conform Series to new index with optional filling logic. |
| [`reindex_like`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reindex_like.html#pandas.Series.reindex_like "pandas.Series.reindex_like")<br>(other\[, method, copy, limit, ...\]) | Return an object with matching indices as other object. |
| [`rename`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename.html#pandas.Series.rename "pandas.Series.rename")<br>(\[index, axis, copy, inplace, level, ...\]) | Alter Series index labels or name. |
| [`rename_axis`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rename_axis.html#pandas.Series.rename_axis "pandas.Series.rename_axis")<br>(\[mapper, index, axis, copy, inplace\]) | Set the name of the axis for the index. |
| [`reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reorder_levels.html#pandas.Series.reorder_levels "pandas.Series.reorder_levels")<br>(order) | Rearrange index levels using input order. |
| [`repeat`](https://pandas.pydata.org/docs/reference/api/pandas.Series.repeat.html#pandas.Series.repeat "pandas.Series.repeat")<br>(repeats\[, axis\]) | Repeat elements of a Series. |
| [`replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html#pandas.Series.replace "pandas.Series.replace")<br>(\[to\_replace, value, inplace, regex\]) | Replace values given in to\_replace with value. |
| [`resample`](https://pandas.pydata.org/docs/reference/api/pandas.Series.resample.html#pandas.Series.resample "pandas.Series.resample")<br>(rule\[, closed, label, convention, ...\]) | Resample time-series data. |
| [`reset_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.reset_index.html#pandas.Series.reset_index "pandas.Series.reset_index")<br>(\[level, drop, name, inplace, ...\]) | Generate a new DataFrame or Series with the index reset. |
| [`rfloordiv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rfloordiv.html#pandas.Series.rfloordiv "pandas.Series.rfloordiv")<br>(other\[, level, fill\_value, axis\]) | Return Integer division of series and other, element-wise (binary operator rfloordiv). |
| [`rmod`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rmod.html#pandas.Series.rmod "pandas.Series.rmod")<br>(other\[, level, fill\_value, axis\]) | Return Modulo of series and other, element-wise (binary operator rmod). |
| [`rmul`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rmul.html#pandas.Series.rmul "pandas.Series.rmul")<br>(other\[, level, fill\_value, axis\]) | Return Multiplication of series and other, element-wise (binary operator rmul). |
| [`rolling`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html#pandas.Series.rolling "pandas.Series.rolling")<br>(window\[, min\_periods, center, ...\]) | Provide rolling window calculations. |
| [`round`](https://pandas.pydata.org/docs/reference/api/pandas.Series.round.html#pandas.Series.round "pandas.Series.round")<br>(\[decimals\]) | Round each value in a Series to the given number of decimals. |
| [`rpow`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rpow.html#pandas.Series.rpow "pandas.Series.rpow")<br>(other\[, level, fill\_value, axis\]) | Return Exponential power of series and other, element-wise (binary operator rpow). |
| [`rsub`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rsub.html#pandas.Series.rsub "pandas.Series.rsub")<br>(other\[, level, fill\_value, axis\]) | Return Subtraction of series and other, element-wise (binary operator rsub). |
| [`rtruediv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rtruediv.html#pandas.Series.rtruediv "pandas.Series.rtruediv")<br>(other\[, level, fill\_value, axis\]) | Return Floating division of series and other, element-wise (binary operator rtruediv). |
| [`sample`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sample.html#pandas.Series.sample "pandas.Series.sample")<br>(\[n, frac, replace, weights, ...\]) | Return a random sample of items from an axis of object. |
| [`searchsorted`](https://pandas.pydata.org/docs/reference/api/pandas.Series.searchsorted.html#pandas.Series.searchsorted "pandas.Series.searchsorted")<br>(value\[, side, sorter\]) | Find indices where elements should be inserted to maintain order. |
| [`sem`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sem.html#pandas.Series.sem "pandas.Series.sem")<br>(\*\[, axis, skipna, ddof, numeric\_only\]) | Return unbiased standard error of the mean over requested axis. |
| [`set_axis`](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_axis.html#pandas.Series.set_axis "pandas.Series.set_axis")<br>(labels, \*\[, axis, copy\]) | Assign desired index to given axis. |
| [`set_flags`](https://pandas.pydata.org/docs/reference/api/pandas.Series.set_flags.html#pandas.Series.set_flags "pandas.Series.set_flags")<br>(\*\[, copy, allows\_duplicate\_labels\]) | Return a new object with updated flags. |
| [`shift`](https://pandas.pydata.org/docs/reference/api/pandas.Series.shift.html#pandas.Series.shift "pandas.Series.shift")<br>(\[periods, freq, axis, fill\_value, suffix\]) | Shift index by desired number of periods with an optional time freq. |
| [`skew`](https://pandas.pydata.org/docs/reference/api/pandas.Series.skew.html#pandas.Series.skew "pandas.Series.skew")<br>(\*\[, axis, skipna, numeric\_only\]) | Return unbiased skew over requested axis. |
| [`sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_index.html#pandas.Series.sort_index "pandas.Series.sort_index")<br>(\*\[, axis, level, ascending, ...\]) | Sort Series by index labels. |
| [`sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sort_values.html#pandas.Series.sort_values "pandas.Series.sort_values")<br>(\*\[, axis, ascending, inplace, ...\]) | Sort by the values. |
| [`squeeze`](https://pandas.pydata.org/docs/reference/api/pandas.Series.squeeze.html#pandas.Series.squeeze "pandas.Series.squeeze")<br>(\[axis\]) | Squeeze 1 dimensional axis objects into scalars. |
| [`std`](https://pandas.pydata.org/docs/reference/api/pandas.Series.std.html#pandas.Series.std "pandas.Series.std")<br>(\*\[, axis, skipna, ddof, numeric\_only\]) | Return sample standard deviation. |
| [`sub`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sub.html#pandas.Series.sub "pandas.Series.sub")<br>(other\[, level, fill\_value, axis\]) | Return Subtraction of series and other, element-wise (binary operator sub). |
| `subtract`(other\[, level, fill\_value, axis\]) | Return Subtraction of series and other, element-wise (binary operator sub). |
| [`sum`](https://pandas.pydata.org/docs/reference/api/pandas.Series.sum.html#pandas.Series.sum "pandas.Series.sum")<br>(\*\[, axis, skipna, numeric\_only, min\_count\]) | Return the sum of the values over the requested axis. |
| [`swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.Series.swaplevel.html#pandas.Series.swaplevel "pandas.Series.swaplevel")<br>(\[i, j, copy\]) | Swap levels i and j in a [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")<br>. |
| [`tail`](https://pandas.pydata.org/docs/reference/api/pandas.Series.tail.html#pandas.Series.tail "pandas.Series.tail")<br>(\[n\]) | Return the last n rows. |
| [`take`](https://pandas.pydata.org/docs/reference/api/pandas.Series.take.html#pandas.Series.take "pandas.Series.take")<br>(indices\[, axis\]) | Return the elements in the given _positional_ indices along an axis. |
| [`to_clipboard`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_clipboard.html#pandas.Series.to_clipboard "pandas.Series.to_clipboard")<br>(\*\[, excel, sep\]) | Copy object to the system clipboard. |
| [`to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_csv.html#pandas.Series.to_csv "pandas.Series.to_csv")<br>(\[path\_or\_buf, sep, na\_rep, ...\]) | Write object to a comma-separated values (csv) file. |
| [`to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_dict.html#pandas.Series.to_dict "pandas.Series.to_dict")<br>(\*\[, into\]) | Convert Series to {label -> value} dict or dict-like object. |
| [`to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_excel.html#pandas.Series.to_excel "pandas.Series.to_excel")<br>(excel\_writer, \*\[, sheet\_name, ...\]) | Write object to an Excel sheet. |
| [`to_frame`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_frame.html#pandas.Series.to_frame "pandas.Series.to_frame")<br>(\[name\]) | Convert Series to DataFrame. |
| [`to_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_hdf.html#pandas.Series.to_hdf "pandas.Series.to_hdf")<br>(path\_or\_buf, \*, key\[, mode, ...\]) | Write the contained data to an HDF5 file using HDFStore. |
| [`to_json`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_json.html#pandas.Series.to_json "pandas.Series.to_json")<br>(\[path\_or\_buf, orient, date\_format, ...\]) | Convert the object to a JSON string. |
| [`to_latex`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_latex.html#pandas.Series.to_latex "pandas.Series.to_latex")<br>(\[buf, columns, header, index, ...\]) | Render object to a LaTeX tabular, longtable, or nested table. |
| [`to_list`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_list.html#pandas.Series.to_list "pandas.Series.to_list")<br>() | Return a list of the values. |
| [`to_markdown`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_markdown.html#pandas.Series.to_markdown "pandas.Series.to_markdown")<br>(\[buf, mode, index, storage\_options\]) | Print Series in Markdown-friendly format. |
| [`to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_numpy.html#pandas.Series.to_numpy "pandas.Series.to_numpy")<br>(\[dtype, copy, na\_value\]) | A NumPy ndarray representing the values in this Series or Index. |
| [`to_period`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_period.html#pandas.Series.to_period "pandas.Series.to_period")<br>(\[freq, copy\]) | Convert Series from DatetimeIndex to PeriodIndex. |
| [`to_pickle`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_pickle.html#pandas.Series.to_pickle "pandas.Series.to_pickle")<br>(path, \*\[, compression, protocol, ...\]) | Pickle (serialize) object to file. |
| [`to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_sql.html#pandas.Series.to_sql "pandas.Series.to_sql")<br>(name, con, \*\[, schema, if\_exists, ...\]) | Write records stored in a DataFrame to a SQL database. |
| [`to_string`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_string.html#pandas.Series.to_string "pandas.Series.to_string")<br>(\[buf, na\_rep, float\_format, ...\]) | Render a string representation of the Series. |
| [`to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_timestamp.html#pandas.Series.to_timestamp "pandas.Series.to_timestamp")<br>(\[freq, how, copy\]) | Cast to DatetimeIndex of Timestamps, at _beginning_ of period. |
| [`to_xarray`](https://pandas.pydata.org/docs/reference/api/pandas.Series.to_xarray.html#pandas.Series.to_xarray "pandas.Series.to_xarray")<br>() | Return an xarray object from the pandas object. |
| `tolist`() | Return a list of the values. |
| [`transform`](https://pandas.pydata.org/docs/reference/api/pandas.Series.transform.html#pandas.Series.transform "pandas.Series.transform")<br>(func\[, axis\]) | Call `func` on self producing a Series with the same axis shape as self. |
| `transpose`(\*args, \*\*kwargs) | Return the transpose, which is by definition self. |
| [`truediv`](https://pandas.pydata.org/docs/reference/api/pandas.Series.truediv.html#pandas.Series.truediv "pandas.Series.truediv")<br>(other\[, level, fill\_value, axis\]) | Return Floating division of series and other, element-wise (binary operator truediv). |
| [`truncate`](https://pandas.pydata.org/docs/reference/api/pandas.Series.truncate.html#pandas.Series.truncate "pandas.Series.truncate")<br>(\[before, after, axis, copy\]) | Truncate a Series or DataFrame before and after some index value. |
| [`tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_convert.html#pandas.Series.tz_convert "pandas.Series.tz_convert")<br>(tz\[, axis, level, copy\]) | Convert tz-aware axis to target time zone. |
| [`tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.Series.tz_localize.html#pandas.Series.tz_localize "pandas.Series.tz_localize")<br>(tz\[, axis, level, copy, ...\]) | Localize time zone naive index of a Series or DataFrame to target time zone. |
| [`unique`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unique.html#pandas.Series.unique "pandas.Series.unique")<br>() | Return unique values of Series object. |
| [`unstack`](https://pandas.pydata.org/docs/reference/api/pandas.Series.unstack.html#pandas.Series.unstack "pandas.Series.unstack")<br>(\[level, fill\_value, sort\]) | Unstack, also known as pivot, Series with MultiIndex to produce DataFrame. |
| [`update`](https://pandas.pydata.org/docs/reference/api/pandas.Series.update.html#pandas.Series.update "pandas.Series.update")<br>(other) | Modify Series in place using values from passed Series. |
| [`value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts "pandas.Series.value_counts")<br>(\[normalize, sort, ascending, ...\]) | Return a Series containing counts of unique values. |
| [`var`](https://pandas.pydata.org/docs/reference/api/pandas.Series.var.html#pandas.Series.var "pandas.Series.var")<br>(\*\[, axis, skipna, ddof, numeric\_only\]) | Return unbiased variance over requested axis. |
| [`where`](https://pandas.pydata.org/docs/reference/api/pandas.Series.where.html#pandas.Series.where "pandas.Series.where")<br>(cond\[, other, inplace, axis, level\]) | Replace values where the condition is False. |
| [`xs`](https://pandas.pydata.org/docs/reference/api/pandas.Series.xs.html#pandas.Series.xs "pandas.Series.xs")<br>(key\[, axis, level, drop\_level\]) | Return cross-section from the Series/DataFrame. |

On this page