[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas-dataframe "Link to this heading")

================================================================================================================================

class pandas.DataFrame(_data\=None_, _index\=None_, _columns\=None_, _dtype\=None_, _copy\=None_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/frame.py#L281-L20320)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "Link to this definition")

Two-dimensional, size-mutable, potentially heterogeneous tabular data.

Data structure also contains labeled axes (rows and columns). Arithmetic operations align on both row and column labels. Can be thought of as a dict-like container for Series objects. The primary pandas data structure.

Parameters:

**data**ndarray (structured or homogeneous), Iterable, dict, or DataFrame

Dict can contain Series, arrays, constants, dataclass or list-like objects. If data is a dict, column order follows insertion-order. If a dict contains Series which have an index defined, it is aligned by its index. This alignment also occurs if data is a Series or a DataFrame itself. Alignment is done on Series/DataFrame inputs.

If data is a list of dicts, column order follows insertion-order.

**index**Index or array-like

Index to use for resulting frame. Will default to RangeIndex if no indexing information part of input data and no index provided.

**columns**Index or array-like

Column labels to use for resulting frame when data does not have them, defaulting to RangeIndex(0, 1, 2, …, n). If data contains column labels, will perform column selection instead.

**dtype**dtype, default None

Data type to force. Only a single dtype is allowed. If None, infer. If `data` is DataFrame then is ignored. Missing values in `data` are not cast: for example, with `dtype=str` a `NaN` entry stays missing rather than becoming the string `"nan"`.

**copy**bool or None, default None

Copy data from inputs. For dict data, the default of None behaves like `copy=True`. For DataFrame or 2d ndarray input, the default of None behaves like `copy=False`. If data is a dict containing one or more Series (possibly of different dtypes), `copy=False` will ensure that these inputs are not copied.

See also

[`DataFrame.from_records`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records "pandas.DataFrame.from_records")

Constructor from tuples, also record arrays.

[`DataFrame.from_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#pandas.DataFrame.from_dict "pandas.DataFrame.from_dict")

From dicts of Series, arrays, or dicts.

[`read_csv`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")

Read a comma-separated values (csv) file into DataFrame.

[`read_table`](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html#pandas.read_table "pandas.read_table")

Read general delimited file into DataFrame.

[`read_clipboard`](https://pandas.pydata.org/docs/reference/api/pandas.read_clipboard.html#pandas.read_clipboard "pandas.read_clipboard")

Read text from clipboard into DataFrame.

Notes

Please reference the [User Guide](https://pandas.pydata.org/docs/user_guide/dsintro.html#basics-dataframe)
 for more information.

Examples

Constructing DataFrame from a dictionary.

\>>> d \= {"col1": \[1, 2\], "col2": \[3, 4\]}
\>>> df \= pd.DataFrame(data\=d)
\>>> df
   col1  col2
0     1     3
1     2     4

Copy to clipboard

Notice that the inferred dtype is int64.

\>>> df.dtypes
col1    int64
col2    int64
dtype: object

Copy to clipboard

To enforce a single dtype:

\>>> df \= pd.DataFrame(data\=d, dtype\=np.int8)
\>>> df.dtypes
col1    int8
col2    int8
dtype: object

Copy to clipboard

Constructing DataFrame from a dictionary including Series:

\>>> d \= {"col1": \[0, 1, 2, 3\], "col2": pd.Series(\[2, 3\], index\=\[2, 3\])}
\>>> pd.DataFrame(data\=d, index\=\[0, 1, 2, 3\])
   col1  col2
0     0   NaN
1     1   NaN
2     2   2.0
3     3   3.0

Copy to clipboard

Constructing DataFrame from numpy ndarray:

\>>> df2 \= pd.DataFrame(
...     np.array(\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]), columns\=\["a", "b", "c"\]
... )
\>>> df2
   a  b  c
0  1  2  3
1  4  5  6
2  7  8  9

Copy to clipboard

Constructing DataFrame from a numpy ndarray that has labeled columns:

\>>> data \= np.array(
...     \[(1, 2, 3), (4, 5, 6), (7, 8, 9)\],
...     dtype\=\[("a", "i4"), ("b", "i4"), ("c", "i4")\],
... )
\>>> df3 \= pd.DataFrame(data, columns\=\["c", "a"\])
\>>> df3
   c  a
0  3  1
1  6  4
2  9  7

Copy to clipboard

Constructing DataFrame from dataclass:

\>>> from dataclasses import make\_dataclass
\>>> Point \= make\_dataclass("Point", \[("x", int), ("y", int)\])
\>>> pd.DataFrame(\[Point(0, 0), Point(0, 3), Point(2, 3)\])
   x  y
0  0  0
1  0  3
2  2  3

Copy to clipboard

Constructing DataFrame from Series/DataFrame:

\>>> ser \= pd.Series(\[1, 2, 3\], index\=\["a", "b", "c"\])
\>>> df \= pd.DataFrame(data\=ser, index\=\["a", "c"\])
\>>> df
   0
a  1
c  3

Copy to clipboard

\>>> df1 \= pd.DataFrame(\[1, 2, 3\], index\=\["a", "b", "c"\], columns\=\["x"\])
\>>> df2 \= pd.DataFrame(data\=df1, index\=\["a", "c"\])
\>>> df2
   x
a  1
c  3

Copy to clipboard

Attributes

|     |     |
| --- | --- |
| [`T`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.T.html#pandas.DataFrame.T "pandas.DataFrame.T") | The transpose of the DataFrame. |
| [`at`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at.html#pandas.DataFrame.at "pandas.DataFrame.at") | Access a single value for a row/column label pair. |
| [`attrs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.attrs.html#pandas.DataFrame.attrs "pandas.DataFrame.attrs") | Dictionary of global attributes of this dataset. |
| [`axes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.axes.html#pandas.DataFrame.axes "pandas.DataFrame.axes") | Return a list representing the axes of the DataFrame. |
| [`columns`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.columns.html#pandas.DataFrame.columns "pandas.DataFrame.columns") | The column labels of the DataFrame. |
| [`dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dtypes.html#pandas.DataFrame.dtypes "pandas.DataFrame.dtypes") | Return the dtypes in the DataFrame. |
| [`empty`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.empty.html#pandas.DataFrame.empty "pandas.DataFrame.empty") | Indicator whether Series/DataFrame is empty. |
| `flags` | Get the properties associated with this pandas object. |
| [`iat`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iat.html#pandas.DataFrame.iat "pandas.DataFrame.iat") | Access a single value for a row/column pair by integer position. |
| [`iloc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iloc.html#pandas.DataFrame.iloc "pandas.DataFrame.iloc") | Purely integer-location based indexing for selection by position. |
| [`index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.index.html#pandas.DataFrame.index "pandas.DataFrame.index") | The index (row labels) of the DataFrame. |
| [`loc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.loc.html#pandas.DataFrame.loc "pandas.DataFrame.loc") | Access a group of rows and columns by label(s) or a boolean array. |
| [`ndim`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ndim.html#pandas.DataFrame.ndim "pandas.DataFrame.ndim") | Return an int representing the number of axes / array dimensions. |
| [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html#pandas.DataFrame.shape "pandas.DataFrame.shape") | Return a tuple representing the dimensionality of the DataFrame. |
| [`size`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.size.html#pandas.DataFrame.size "pandas.DataFrame.size") | Return an int representing the number of elements in this object. |
| [`style`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.style.html#pandas.DataFrame.style "pandas.DataFrame.style") | Returns a Styler object. |
| [`values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.values.html#pandas.DataFrame.values "pandas.DataFrame.values") | Return a Numpy representation of the DataFrame. |

Methods

|     |     |
| --- | --- |
| [`abs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.abs.html#pandas.DataFrame.abs "pandas.DataFrame.abs")<br>() | Return a Series/DataFrame with absolute numeric value of each element. |
| [`add`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add.html#pandas.DataFrame.add "pandas.DataFrame.add")<br>(other\[, axis, level, fill\_value\]) | Get Addition of dataframe and other, element-wise (binary operator add). |
| [`add_prefix`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_prefix.html#pandas.DataFrame.add_prefix "pandas.DataFrame.add_prefix")<br>(prefix\[, axis\]) | Prefix labels with string prefix. |
| [`add_suffix`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.add_suffix.html#pandas.DataFrame.add_suffix "pandas.DataFrame.add_suffix")<br>(suffix\[, axis\]) | Suffix labels with string suffix. |
| [`agg`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg "pandas.DataFrame.agg")<br>(\[func, axis\]) | Aggregate using one or more operations over the specified axis. |
| [`aggregate`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.aggregate.html#pandas.DataFrame.aggregate "pandas.DataFrame.aggregate")<br>(\[func, axis\]) | Aggregate using one or more operations over the specified axis. |
| [`align`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.align.html#pandas.DataFrame.align "pandas.DataFrame.align")<br>(other\[, join, axis, level, copy, ...\]) | Align two objects on their axes with the specified join method. |
| [`all`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.all.html#pandas.DataFrame.all "pandas.DataFrame.all")<br>(\*\[, axis, bool\_only, skipna\]) | Return whether all elements are True, potentially over an axis. |
| [`any`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.any.html#pandas.DataFrame.any "pandas.DataFrame.any")<br>(\*\[, axis, bool\_only, skipna\]) | Return whether any element is True, potentially over an axis. |
| [`apply`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")<br>(func\[, axis, raw, result\_type, args, ...\]) | Apply a function along an axis of the DataFrame. |
| [`asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.asfreq.html#pandas.DataFrame.asfreq "pandas.DataFrame.asfreq")<br>(freq\[, method, how, normalize, ...\]) | Convert time series to specified frequency. |
| [`asof`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.asof.html#pandas.DataFrame.asof "pandas.DataFrame.asof")<br>(where\[, subset\]) | Return the last row(s) without any NaNs before where. |
| [`assign`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.assign.html#pandas.DataFrame.assign "pandas.DataFrame.assign")<br>(\*\*kwargs) | Assign new columns to a DataFrame. |
| [`astype`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html#pandas.DataFrame.astype "pandas.DataFrame.astype")<br>(dtype\[, copy, errors\]) | Cast a pandas object to a specified dtype `dtype`. |
| [`at_time`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.at_time.html#pandas.DataFrame.at_time "pandas.DataFrame.at_time")<br>(time\[, asof, axis\]) | Select values at particular time of day (e.g., 9:30AM). |
| [`between_time`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.between_time.html#pandas.DataFrame.between_time "pandas.DataFrame.between_time")<br>(start\_time, end\_time\[, ...\]) | Select values between particular times of the day (e.g., 9:00-9:30 AM). |
| [`bfill`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.bfill.html#pandas.DataFrame.bfill "pandas.DataFrame.bfill")<br>(\*\[, axis, inplace, limit, limit\_area\]) | Fill NA/NaN values by using the next valid observation to fill the gap. |
| [`boxplot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.boxplot.html#pandas.DataFrame.boxplot "pandas.DataFrame.boxplot")<br>(\[column, by, ax, fontsize, rot, ...\]) | Make a box plot from DataFrame columns. |
| [`clip`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.clip.html#pandas.DataFrame.clip "pandas.DataFrame.clip")<br>(\[lower, upper, axis, inplace\]) | Trim values at input threshold(s). |
| [`combine`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine.html#pandas.DataFrame.combine "pandas.DataFrame.combine")<br>(other, func\[, fill\_value, overwrite\]) | Perform column-wise combine with another DataFrame. |
| [`combine_first`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.combine_first.html#pandas.DataFrame.combine_first "pandas.DataFrame.combine_first")<br>(other) | Update null elements with value in the same location in other. |
| [`compare`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.compare.html#pandas.DataFrame.compare "pandas.DataFrame.compare")<br>(other\[, align\_axis, keep\_shape, ...\]) | Compare to another DataFrame and show the differences. |
| [`convert_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.convert_dtypes.html#pandas.DataFrame.convert_dtypes "pandas.DataFrame.convert_dtypes")<br>(\[infer\_objects, ...\]) | Convert columns from numpy dtypes to the best dtypes that support `pd.NA`. |
| [`copy`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.copy.html#pandas.DataFrame.copy "pandas.DataFrame.copy")<br>(\[deep\]) | Make a copy of this object's indices and data. |
| [`corr`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html#pandas.DataFrame.corr "pandas.DataFrame.corr")<br>(\[method, min\_periods, numeric\_only\]) | Compute pairwise correlation of columns, excluding NA/null values. |
| [`corrwith`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corrwith.html#pandas.DataFrame.corrwith "pandas.DataFrame.corrwith")<br>(other\[, axis, drop, method, ...\]) | Compute pairwise correlation. |
| [`count`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.count.html#pandas.DataFrame.count "pandas.DataFrame.count")<br>(\[axis, numeric\_only\]) | Count non-NA cells for each column or row. |
| [`cov`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cov.html#pandas.DataFrame.cov "pandas.DataFrame.cov")<br>(\[min\_periods, ddof, numeric\_only\]) | Compute pairwise covariance of columns, excluding NA/null values. |
| [`cummax`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cummax.html#pandas.DataFrame.cummax "pandas.DataFrame.cummax")<br>(\[axis, skipna, numeric\_only\]) | Return cumulative maximum over a DataFrame or Series axis. |
| [`cummin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cummin.html#pandas.DataFrame.cummin "pandas.DataFrame.cummin")<br>(\[axis, skipna, numeric\_only\]) | Return cumulative minimum over a DataFrame or Series axis. |
| [`cumprod`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumprod.html#pandas.DataFrame.cumprod "pandas.DataFrame.cumprod")<br>(\[axis, skipna, numeric\_only\]) | Return cumulative product over a DataFrame or Series axis. |
| [`cumsum`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumsum.html#pandas.DataFrame.cumsum "pandas.DataFrame.cumsum")<br>(\[axis, skipna, numeric\_only\]) | Return cumulative sum over a DataFrame or Series axis. |
| [`describe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe")<br>(\[percentiles, include, exclude\]) | Generate descriptive statistics. |
| [`diff`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.diff.html#pandas.DataFrame.diff "pandas.DataFrame.diff")<br>(\[periods, axis\]) | First discrete difference of element. |
| [`div`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.div.html#pandas.DataFrame.div "pandas.DataFrame.div")<br>(other\[, axis, level, fill\_value\]) | Get Floating division of dataframe and other, element-wise (binary operator truediv). |
| `divide`(other\[, axis, level, fill\_value\]) | Get Floating division of dataframe and other, element-wise (binary operator truediv). |
| [`dot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dot.html#pandas.DataFrame.dot "pandas.DataFrame.dot")<br>(other) | Compute the matrix multiplication between the DataFrame and other. |
| [`drop`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop "pandas.DataFrame.drop")<br>(\[labels, axis, index, columns, level, ...\]) | Drop specified labels from rows or columns. |
| [`drop_duplicates`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "pandas.DataFrame.drop_duplicates")<br>(\[subset, keep, inplace, ...\]) | Return DataFrame with duplicate rows removed. |
| [`droplevel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.droplevel.html#pandas.DataFrame.droplevel "pandas.DataFrame.droplevel")<br>(level\[, axis\]) | Return Series/DataFrame with requested index / column level(s) removed. |
| [`dropna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.dropna.html#pandas.DataFrame.dropna "pandas.DataFrame.dropna")<br>(\*\[, axis, how, thresh, subset, ...\]) | Remove missing values. |
| [`duplicated`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.duplicated.html#pandas.DataFrame.duplicated "pandas.DataFrame.duplicated")<br>(\[subset, keep\]) | Return boolean Series denoting duplicate rows. |
| [`eq`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eq.html#pandas.DataFrame.eq "pandas.DataFrame.eq")<br>(other\[, axis, level\]) | Get Equal to of dataframe and other, element-wise (binary operator eq). |
| [`equals`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.equals.html#pandas.DataFrame.equals "pandas.DataFrame.equals")<br>(other) | Test whether two objects contain the same elements. |
| [`eval`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.eval.html#pandas.DataFrame.eval "pandas.DataFrame.eval")<br>(expr, \*\[, inplace\]) | Evaluate a string describing operations on DataFrame columns. |
| [`ewm`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ewm.html#pandas.DataFrame.ewm "pandas.DataFrame.ewm")<br>(\[com, span, halflife, alpha, ...\]) | Provide exponentially weighted (EW) calculations. |
| [`expanding`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.expanding.html#pandas.DataFrame.expanding "pandas.DataFrame.expanding")<br>(\[min\_periods, method\]) | Provide expanding window calculations. |
| [`explode`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.explode.html#pandas.DataFrame.explode "pandas.DataFrame.explode")<br>(column\[, ignore\_index\]) | Transform each element of a list-like to a row, replicating index values. |
| [`ffill`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ffill.html#pandas.DataFrame.ffill "pandas.DataFrame.ffill")<br>(\*\[, axis, inplace, limit, limit\_area\]) | Fill NA/NaN values by propagating the last valid observation to next valid. |
| [`fillna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.fillna.html#pandas.DataFrame.fillna "pandas.DataFrame.fillna")<br>(value, \*\[, axis, inplace, limit\]) | Fill NA/NaN values with value. |
| [`filter`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html#pandas.DataFrame.filter "pandas.DataFrame.filter")<br>(\[arg, like, regex, axis, items, cond, na\]) | Subset the rows or columns according to a boolean mask or the labels. |
| [`first_valid_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.first_valid_index.html#pandas.DataFrame.first_valid_index "pandas.DataFrame.first_valid_index")<br>() | Return index for first non-missing value or None, if no value is found. |
| [`floordiv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.floordiv.html#pandas.DataFrame.floordiv "pandas.DataFrame.floordiv")<br>(other\[, axis, level, fill\_value\]) | Get Integer division of dataframe and other, element-wise (binary operator floordiv). |
| [`from_arrow`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_arrow.html#pandas.DataFrame.from_arrow "pandas.DataFrame.from_arrow")<br>(data) | Construct a DataFrame from a tabular Arrow object. |
| [`from_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_dict.html#pandas.DataFrame.from_dict "pandas.DataFrame.from_dict")<br>(data\[, orient, dtype, columns\]) | Construct DataFrame from dict of array-like or dicts. |
| [`from_records`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.from_records.html#pandas.DataFrame.from_records "pandas.DataFrame.from_records")<br>(data\[, index, exclude, ...\]) | Convert structured or record ndarray to DataFrame. |
| [`ge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ge.html#pandas.DataFrame.ge "pandas.DataFrame.ge")<br>(other\[, axis, level\]) | Get Greater than or equal to of dataframe and other, element-wise (binary operator ge). |
| [`get`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.get.html#pandas.DataFrame.get "pandas.DataFrame.get")<br>(key\[, default\]) | Get item from object for given key (ex: DataFrame column). |
| [`groupby`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")<br>(\[by, level, as\_index, sort, ...\]) | Group DataFrame using a mapper or by a Series of columns. |
| [`gt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.gt.html#pandas.DataFrame.gt "pandas.DataFrame.gt")<br>(other\[, axis, level\]) | Get Greater than of dataframe and other, element-wise (binary operator gt). |
| [`head`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head "pandas.DataFrame.head")<br>(\[n\]) | Return the first n rows. |
| [`hist`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.hist.html#pandas.DataFrame.hist "pandas.DataFrame.hist")<br>(\[column, by, grid, xlabelsize, xrot, ...\]) | Make a histogram of the DataFrame's columns. |
| [`idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html#pandas.DataFrame.idxmax "pandas.DataFrame.idxmax")<br>(\[axis, skipna, numeric\_only\]) | Return index of first occurrence of maximum over requested axis. |
| [`idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmin.html#pandas.DataFrame.idxmin "pandas.DataFrame.idxmin")<br>(\[axis, skipna, numeric\_only\]) | Return index of first occurrence of minimum over requested axis. |
| [`infer_objects`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.infer_objects.html#pandas.DataFrame.infer_objects "pandas.DataFrame.infer_objects")<br>(\[copy\]) | Attempt to infer better dtypes for object columns. |
| [`info`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info")<br>(\[verbose, buf, max\_cols, memory\_usage, ...\]) | Print a concise summary of a DataFrame. |
| [`insert`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.insert.html#pandas.DataFrame.insert "pandas.DataFrame.insert")<br>(loc, column, value\[, allow\_duplicates\]) | Insert column into DataFrame at specified location. |
| [`interpolate`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html#pandas.DataFrame.interpolate "pandas.DataFrame.interpolate")<br>(\[method, axis, limit, inplace, ...\]) | Fill NaN values using an interpolation method. |
| [`isetitem`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isetitem.html#pandas.DataFrame.isetitem "pandas.DataFrame.isetitem")<br>(loc, value) | Set the given value in the column with position loc. |
| [`isin`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isin.html#pandas.DataFrame.isin "pandas.DataFrame.isin")<br>(values) | Whether each element in the DataFrame is contained in values. |
| [`isna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isna.html#pandas.DataFrame.isna "pandas.DataFrame.isna")<br>() | Detect missing values. |
| [`isnull`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.isnull.html#pandas.DataFrame.isnull "pandas.DataFrame.isnull")<br>() | DataFrame.isnull is an alias for DataFrame.isna. |
| [`items`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.items.html#pandas.DataFrame.items "pandas.DataFrame.items")<br>() | Iterate over (column name, Series) pairs. |
| [`iterrows`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.iterrows.html#pandas.DataFrame.iterrows "pandas.DataFrame.iterrows")<br>() | Iterate over DataFrame rows as (index, Series) pairs. |
| [`itertuples`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.itertuples.html#pandas.DataFrame.itertuples "pandas.DataFrame.itertuples")<br>(\[index, name\]) | Iterate over DataFrame rows as namedtuples. |
| [`join`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.join.html#pandas.DataFrame.join "pandas.DataFrame.join")<br>(other\[, on, how, lsuffix, rsuffix, ...\]) | Join columns of another DataFrame. |
| [`keys`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.keys.html#pandas.DataFrame.keys "pandas.DataFrame.keys")<br>() | Get the 'info axis' (see Indexing for more). |
| [`kurt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.kurt.html#pandas.DataFrame.kurt "pandas.DataFrame.kurt")<br>(\*\[, axis, skipna, numeric\_only\]) | Return unbiased kurtosis over requested axis. |
| [`kurtosis`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.kurtosis.html#pandas.DataFrame.kurtosis "pandas.DataFrame.kurtosis")<br>(\*\[, axis, skipna, numeric\_only\]) | Return unbiased kurtosis over requested axis. |
| [`last_valid_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.last_valid_index.html#pandas.DataFrame.last_valid_index "pandas.DataFrame.last_valid_index")<br>() | Return index for last non-missing value or None, if no value is found. |
| [`le`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.le.html#pandas.DataFrame.le "pandas.DataFrame.le")<br>(other\[, axis, level\]) | Get Less than or equal to of dataframe and other, element-wise (binary operator le). |
| [`lt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.lt.html#pandas.DataFrame.lt "pandas.DataFrame.lt")<br>(other\[, axis, level\]) | Get Less than of dataframe and other, element-wise (binary operator lt). |
| [`map`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas.DataFrame.map "pandas.DataFrame.map")<br>(func\[, na\_action\]) | Apply a function to a Dataframe elementwise. |
| [`mask`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mask.html#pandas.DataFrame.mask "pandas.DataFrame.mask")<br>(cond\[, other, inplace, axis, level\]) | Replace values where the condition is True. |
| [`max`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.max.html#pandas.DataFrame.max "pandas.DataFrame.max")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the maximum of the values over the requested axis. |
| [`mean`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mean.html#pandas.DataFrame.mean "pandas.DataFrame.mean")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the mean of the values over the requested axis. |
| [`median`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.median.html#pandas.DataFrame.median "pandas.DataFrame.median")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the median of the values over the requested axis. |
| [`melt`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.melt.html#pandas.DataFrame.melt "pandas.DataFrame.melt")<br>(\[id\_vars, value\_vars, var\_name, ...\]) | Unpivot DataFrame from wide to long format, optionally leaving identifiers set. |
| [`memory_usage`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.memory_usage.html#pandas.DataFrame.memory_usage "pandas.DataFrame.memory_usage")<br>(\[index, deep\]) | Return the memory usage of each column in bytes. |
| [`merge`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge "pandas.DataFrame.merge")<br>(right\[, how, on, left\_on, right\_on, ...\]) | Merge DataFrame or named Series objects with a database-style join. |
| [`min`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.min.html#pandas.DataFrame.min "pandas.DataFrame.min")<br>(\*\[, axis, skipna, numeric\_only\]) | Return the minimum of the values over the requested axis. |
| [`mod`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mod.html#pandas.DataFrame.mod "pandas.DataFrame.mod")<br>(other\[, axis, level, fill\_value\]) | Get Modulo of dataframe and other, element-wise (binary operator mod). |
| [`mode`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mode.html#pandas.DataFrame.mode "pandas.DataFrame.mode")<br>(\[axis, numeric\_only, dropna\]) | Get the mode(s) of each element along the selected axis. |
| [`mul`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.mul.html#pandas.DataFrame.mul "pandas.DataFrame.mul")<br>(other\[, axis, level, fill\_value\]) | Get Multiplication of dataframe and other, element-wise (binary operator mul). |
| `multiply`(other\[, axis, level, fill\_value\]) | Get Multiplication of dataframe and other, element-wise (binary operator mul). |
| [`ne`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ne.html#pandas.DataFrame.ne "pandas.DataFrame.ne")<br>(other\[, axis, level\]) | Get Not equal to of dataframe and other, element-wise (binary operator ne). |
| [`nlargest`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nlargest.html#pandas.DataFrame.nlargest "pandas.DataFrame.nlargest")<br>(n, columns\[, keep\]) | Return the first n rows ordered by columns in descending order. |
| [`notna`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notna.html#pandas.DataFrame.notna "pandas.DataFrame.notna")<br>() | Detect existing (non-missing) values. |
| [`notnull`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.notnull.html#pandas.DataFrame.notnull "pandas.DataFrame.notnull")<br>() | DataFrame.notnull is an alias for DataFrame.notna. |
| [`nsmallest`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nsmallest.html#pandas.DataFrame.nsmallest "pandas.DataFrame.nsmallest")<br>(n, columns\[, keep\]) | Return the first n rows ordered by columns in ascending order. |
| [`nunique`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.nunique.html#pandas.DataFrame.nunique "pandas.DataFrame.nunique")<br>(\[axis, dropna\]) | Count number of distinct elements in specified axis. |
| [`pct_change`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html#pandas.DataFrame.pct_change "pandas.DataFrame.pct_change")<br>(\[periods, fill\_method, freq\]) | Fractional change between the current and a prior element. |
| [`pipe`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe "pandas.DataFrame.pipe")<br>(func, \*args, \*\*kwargs) | Apply chainable functions that expect Series or DataFrames. |
| [`pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "pandas.DataFrame.pivot")<br>(\*, columns\[, index, values\]) | Return reshaped DataFrame organized by given index / column values. |
| [`pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table "pandas.DataFrame.pivot_table")<br>(\[values, index, columns, ...\]) | Create a spreadsheet-style pivot table as a DataFrame. |
| [`pop`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pop.html#pandas.DataFrame.pop "pandas.DataFrame.pop")<br>(item) | Return item and drop it from DataFrame. |
| [`pow`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pow.html#pandas.DataFrame.pow "pandas.DataFrame.pow")<br>(other\[, axis, level, fill\_value\]) | Get Exponential power of dataframe and other, element-wise (binary operator pow). |
| [`prod`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.prod.html#pandas.DataFrame.prod "pandas.DataFrame.prod")<br>(\*\[, axis, skipna, numeric\_only, min\_count\]) | Return the product of the values over the requested axis. |
| [`product`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.product.html#pandas.DataFrame.product "pandas.DataFrame.product")<br>(\*\[, axis, skipna, numeric\_only, ...\]) | Return the product of the values over the requested axis. |
| [`quantile`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.quantile.html#pandas.DataFrame.quantile "pandas.DataFrame.quantile")<br>(\[q, axis, numeric\_only, ...\]) | Return values at the given quantile over requested axis. |
| [`query`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.query.html#pandas.DataFrame.query "pandas.DataFrame.query")<br>(expr, \*\[, parser, engine, local\_dict, ...\]) | Query the columns of a DataFrame with a boolean expression. |
| [`radd`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.radd.html#pandas.DataFrame.radd "pandas.DataFrame.radd")<br>(other\[, axis, level, fill\_value\]) | Get Addition of dataframe and other, element-wise (binary operator radd). |
| [`rank`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rank.html#pandas.DataFrame.rank "pandas.DataFrame.rank")<br>(\[axis, method, numeric\_only, ...\]) | Compute numerical data ranks (1 through n) along axis. |
| [`rdiv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rdiv.html#pandas.DataFrame.rdiv "pandas.DataFrame.rdiv")<br>(other\[, axis, level, fill\_value\]) | Get Floating division of dataframe and other, element-wise (binary operator rtruediv). |
| [`reindex`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex.html#pandas.DataFrame.reindex "pandas.DataFrame.reindex")<br>(\[labels, index, columns, axis, ...\]) | Conform DataFrame to new index with optional filling logic. |
| [`reindex_like`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reindex_like.html#pandas.DataFrame.reindex_like "pandas.DataFrame.reindex_like")<br>(other\[, method, copy, limit, ...\]) | Return an object with matching indices as other object. |
| [`rename`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename "pandas.DataFrame.rename")<br>(\[mapper, index, columns, axis, copy, ...\]) | Rename columns or index labels. |
| [`rename_axis`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename_axis.html#pandas.DataFrame.rename_axis "pandas.DataFrame.rename_axis")<br>(\[mapper, index, columns, axis, ...\]) | Set the name of the axis for the index or columns. |
| [`reorder_levels`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reorder_levels.html#pandas.DataFrame.reorder_levels "pandas.DataFrame.reorder_levels")<br>(order\[, axis\]) | Rearrange index or column levels using input `order`. |
| [`replace`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html#pandas.DataFrame.replace "pandas.DataFrame.replace")<br>(\[to\_replace, value, inplace, regex\]) | Replace values given in to\_replace with value. |
| [`resample`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html#pandas.DataFrame.resample "pandas.DataFrame.resample")<br>(rule\[, closed, label, convention, ...\]) | Resample time-series data. |
| [`reset_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index "pandas.DataFrame.reset_index")<br>(\[level, drop, inplace, ...\]) | Reset the index, or a level of it. |
| [`rfloordiv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rfloordiv.html#pandas.DataFrame.rfloordiv "pandas.DataFrame.rfloordiv")<br>(other\[, axis, level, fill\_value\]) | Get Integer division of dataframe and other, element-wise (binary operator rfloordiv). |
| [`rmod`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rmod.html#pandas.DataFrame.rmod "pandas.DataFrame.rmod")<br>(other\[, axis, level, fill\_value\]) | Get Modulo of dataframe and other, element-wise (binary operator rmod). |
| [`rmul`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rmul.html#pandas.DataFrame.rmul "pandas.DataFrame.rmul")<br>(other\[, axis, level, fill\_value\]) | Get Multiplication of dataframe and other, element-wise (binary operator rmul). |
| [`rolling`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling "pandas.DataFrame.rolling")<br>(window\[, min\_periods, center, ...\]) | Provide rolling window calculations. |
| [`round`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html#pandas.DataFrame.round "pandas.DataFrame.round")<br>(\[decimals\]) | Round numeric columns in a DataFrame to a variable number of decimal places. |
| [`rpow`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rpow.html#pandas.DataFrame.rpow "pandas.DataFrame.rpow")<br>(other\[, axis, level, fill\_value\]) | Get Exponential power of dataframe and other, element-wise (binary operator rpow). |
| [`rsub`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rsub.html#pandas.DataFrame.rsub "pandas.DataFrame.rsub")<br>(other\[, axis, level, fill\_value\]) | Get Subtraction of dataframe and other, element-wise (binary operator rsub). |
| [`rtruediv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rtruediv.html#pandas.DataFrame.rtruediv "pandas.DataFrame.rtruediv")<br>(other\[, axis, level, fill\_value\]) | Get Floating division of dataframe and other, element-wise (binary operator rtruediv). |
| [`sample`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sample.html#pandas.DataFrame.sample "pandas.DataFrame.sample")<br>(\[n, frac, replace, weights, ...\]) | Return a random sample of items from an axis of object. |
| [`select`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select.html#pandas.DataFrame.select "pandas.DataFrame.select")<br>(\*args, \*\*kwargs) | Select a subset of columns from the DataFrame. |
| [`select_dtypes`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.select_dtypes.html#pandas.DataFrame.select_dtypes "pandas.DataFrame.select_dtypes")<br>(\[include, exclude\]) | Return a subset of the DataFrame's columns based on the column dtypes. |
| [`sem`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sem.html#pandas.DataFrame.sem "pandas.DataFrame.sem")<br>(\*\[, axis, skipna, ddof, numeric\_only\]) | Return unbiased standard error of the mean over requested axis. |
| [`set_axis`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_axis.html#pandas.DataFrame.set_axis "pandas.DataFrame.set_axis")<br>(labels, \*\[, axis, copy\]) | Assign desired index to given axis. |
| [`set_flags`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_flags.html#pandas.DataFrame.set_flags "pandas.DataFrame.set_flags")<br>(\*\[, copy, allows\_duplicate\_labels\]) | Return a new object with updated flags. |
| [`set_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.set_index.html#pandas.DataFrame.set_index "pandas.DataFrame.set_index")<br>(keys, \*\[, drop, append, inplace, ...\]) | Set the DataFrame index using existing columns. |
| [`shift`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shift.html#pandas.DataFrame.shift "pandas.DataFrame.shift")<br>(\[periods, freq, axis, fill\_value, suffix\]) | Shift index by desired number of periods with an optional time freq. |
| [`skew`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.skew.html#pandas.DataFrame.skew "pandas.DataFrame.skew")<br>(\*\[, axis, skipna, numeric\_only\]) | Return unbiased skew over requested axis. |
| [`sort_index`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_index.html#pandas.DataFrame.sort_index "pandas.DataFrame.sort_index")<br>(\*\[, axis, level, ascending, ...\]) | Sort object by labels (along an axis). |
| [`sort_values`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")<br>(by, \*\[, axis, ascending, ...\]) | Sort by the values along either axis. |
| [`squeeze`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.squeeze.html#pandas.DataFrame.squeeze "pandas.DataFrame.squeeze")<br>(\[axis\]) | Squeeze 1 dimensional axis objects into scalars. |
| [`stack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html#pandas.DataFrame.stack "pandas.DataFrame.stack")<br>(\[level, dropna, sort, future\_stack\]) | Stack the prescribed level(s) from columns to index. |
| [`std`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.std.html#pandas.DataFrame.std "pandas.DataFrame.std")<br>(\*\[, axis, skipna, ddof, numeric\_only\]) | Return sample standard deviation over requested axis. |
| [`sub`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sub.html#pandas.DataFrame.sub "pandas.DataFrame.sub")<br>(other\[, axis, level, fill\_value\]) | Get Subtraction of dataframe and other, element-wise (binary operator sub). |
| `subtract`(other\[, axis, level, fill\_value\]) | Get Subtraction of dataframe and other, element-wise (binary operator sub). |
| [`sum`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sum.html#pandas.DataFrame.sum "pandas.DataFrame.sum")<br>(\*\[, axis, skipna, numeric\_only, min\_count\]) | Return the sum of the values over the requested axis. |
| [`swaplevel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.swaplevel.html#pandas.DataFrame.swaplevel "pandas.DataFrame.swaplevel")<br>(\[i, j, axis\]) | Swap levels i and j in a [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")<br>. |
| [`tail`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail "pandas.DataFrame.tail")<br>(\[n\]) | Return the last n rows. |
| [`take`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.take.html#pandas.DataFrame.take "pandas.DataFrame.take")<br>(indices\[, axis\]) | Return the elements in the given _positional_ indices along an axis. |
| [`to_clipboard`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_clipboard.html#pandas.DataFrame.to_clipboard "pandas.DataFrame.to_clipboard")<br>(\*\[, excel, sep\]) | Copy object to the system clipboard. |
| [`to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")<br>(\[path\_or\_buf, sep, na\_rep, ...\]) | Write object to a comma-separated values (csv) file. |
| [`to_dict`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_dict.html#pandas.DataFrame.to_dict "pandas.DataFrame.to_dict")<br>(\[orient, into, index\]) | Convert the DataFrame to a dictionary. |
| [`to_excel`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html#pandas.DataFrame.to_excel "pandas.DataFrame.to_excel")<br>(excel\_writer, \*\[, sheet\_name, ...\]) | Write object to an Excel sheet. |
| [`to_feather`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_feather.html#pandas.DataFrame.to_feather "pandas.DataFrame.to_feather")<br>(path, \*\*kwargs) | Write a DataFrame to the binary Feather format. |
| [`to_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html#pandas.DataFrame.to_hdf "pandas.DataFrame.to_hdf")<br>(path\_or\_buf, \*, key\[, mode, ...\]) | Write the contained data to an HDF5 file using HDFStore. |
| [`to_html`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_html.html#pandas.DataFrame.to_html "pandas.DataFrame.to_html")<br>(\[buf, columns, col\_space, header, ...\]) | Render a DataFrame as an HTML table. |
| [`to_iceberg`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_iceberg.html#pandas.DataFrame.to_iceberg "pandas.DataFrame.to_iceberg")<br>(table\_identifier\[, catalog\_name, ...\]) | Write a DataFrame to an Apache Iceberg table. |
| [`to_json`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_json.html#pandas.DataFrame.to_json "pandas.DataFrame.to_json")<br>(\[path\_or\_buf, orient, date\_format, ...\]) | Convert the object to a JSON string. |
| [`to_latex`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_latex.html#pandas.DataFrame.to_latex "pandas.DataFrame.to_latex")<br>(\[buf, columns, header, index, ...\]) | Render object to a LaTeX tabular, longtable, or nested table. |
| [`to_markdown`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_markdown.html#pandas.DataFrame.to_markdown "pandas.DataFrame.to_markdown")<br>(\[buf, mode, index, storage\_options\]) | Print DataFrame in Markdown-friendly format. |
| [`to_numpy`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_numpy.html#pandas.DataFrame.to_numpy "pandas.DataFrame.to_numpy")<br>(\[dtype, copy, na\_value\]) | Convert the DataFrame to a NumPy array. |
| [`to_orc`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_orc.html#pandas.DataFrame.to_orc "pandas.DataFrame.to_orc")<br>(\[path, engine, index, engine\_kwargs\]) | Write a DataFrame to the Optimized Row Columnar (ORC) format. |
| [`to_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas.DataFrame.to_parquet "pandas.DataFrame.to_parquet")<br>(\[path, engine, compression, ...\]) | Write a DataFrame to the binary parquet format. |
| [`to_period`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_period.html#pandas.DataFrame.to_period "pandas.DataFrame.to_period")<br>(\[freq, axis, copy\]) | Convert DataFrame from DatetimeIndex to PeriodIndex. |
| [`to_pickle`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_pickle.html#pandas.DataFrame.to_pickle "pandas.DataFrame.to_pickle")<br>(path, \*\[, compression, protocol, ...\]) | Pickle (serialize) object to file. |
| [`to_records`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_records.html#pandas.DataFrame.to_records "pandas.DataFrame.to_records")<br>(\[index, column\_dtypes, index\_dtypes\]) | Convert DataFrame to a NumPy record array. |
| [`to_sql`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html#pandas.DataFrame.to_sql "pandas.DataFrame.to_sql")<br>(name, con, \*\[, schema, if\_exists, ...\]) | Write records stored in a DataFrame to a SQL database. |
| [`to_stata`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_stata.html#pandas.DataFrame.to_stata "pandas.DataFrame.to_stata")<br>(path, \*\[, convert\_dates, ...\]) | Export DataFrame object to Stata dta format. |
| [`to_string`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_string.html#pandas.DataFrame.to_string "pandas.DataFrame.to_string")<br>(\[buf, columns, col\_space, header, ...\]) | Render a DataFrame to a console-friendly tabular output. |
| [`to_timestamp`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_timestamp.html#pandas.DataFrame.to_timestamp "pandas.DataFrame.to_timestamp")<br>(\[freq, how, axis, copy\]) | Cast PeriodIndex to DatetimeIndex of timestamps, at _beginning_ of period. |
| [`to_xarray`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xarray.html#pandas.DataFrame.to_xarray "pandas.DataFrame.to_xarray")<br>() | Return an xarray object from the pandas object. |
| [`to_xml`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xml.html#pandas.DataFrame.to_xml "pandas.DataFrame.to_xml")<br>(\[path\_or\_buffer, index, root\_name, ...\]) | Render a DataFrame to an XML document. |
| [`transform`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html#pandas.DataFrame.transform "pandas.DataFrame.transform")<br>(func\[, axis\]) | Call `func` on self producing a DataFrame with the same axis shape as self. |
| [`transpose`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transpose.html#pandas.DataFrame.transpose "pandas.DataFrame.transpose")<br>(\*args\[, copy\]) | Transpose index and columns. |
| [`truediv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truediv.html#pandas.DataFrame.truediv "pandas.DataFrame.truediv")<br>(other\[, axis, level, fill\_value\]) | Get Floating division of dataframe and other, element-wise (binary operator truediv). |
| [`truncate`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.truncate.html#pandas.DataFrame.truncate "pandas.DataFrame.truncate")<br>(\[before, after, axis, copy\]) | Truncate a Series or DataFrame before and after some index value. |
| [`tz_convert`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tz_convert.html#pandas.DataFrame.tz_convert "pandas.DataFrame.tz_convert")<br>(tz\[, axis, level, copy\]) | Convert tz-aware axis to target time zone. |
| [`tz_localize`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tz_localize.html#pandas.DataFrame.tz_localize "pandas.DataFrame.tz_localize")<br>(tz\[, axis, level, copy, ...\]) | Localize time zone naive index of a Series or DataFrame to target time zone. |
| [`unstack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack "pandas.DataFrame.unstack")<br>(\[level, fill\_value, sort\]) | Pivot a level of the (necessarily hierarchical) index labels. |
| [`update`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.update.html#pandas.DataFrame.update "pandas.DataFrame.update")<br>(other\[, join, overwrite, ...\]) | Modify in place using non-NA values from another DataFrame. |
| [`value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.value_counts.html#pandas.DataFrame.value_counts "pandas.DataFrame.value_counts")<br>(\[subset, normalize, sort, ...\]) | Return a Series containing the frequency of each distinct row in the DataFrame. |
| [`var`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.var.html#pandas.DataFrame.var "pandas.DataFrame.var")<br>(\*\[, axis, skipna, ddof, numeric\_only\]) | Return unbiased variance over requested axis. |
| [`where`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.where.html#pandas.DataFrame.where "pandas.DataFrame.where")<br>(cond\[, other, inplace, axis, level\]) | Replace values where the condition is False. |
| [`xs`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.xs.html#pandas.DataFrame.xs "pandas.DataFrame.xs")<br>(key\[, axis, level, drop\_level\]) | Return cross-section from the Series/DataFrame. |

On this page