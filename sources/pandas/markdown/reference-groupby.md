[Skip to main content](https://pandas.pydata.org/docs/reference/groupby.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/groupby.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/groupby.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/groupby.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/groupby.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/groupby.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/groupby.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/groupby.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/groupby.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/groupby.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/groupby.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/groupby.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/groupby.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/groupby.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

GroupBy[#](https://pandas.pydata.org/docs/reference/groupby.html#groupby "Link to this heading")

=================================================================================================

Note

For an overview, see [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby)
.

`pandas.api.typing.DataFrameGroupBy` and `pandas.api.typing.SeriesGroupBy` instances are returned by groupby calls [`pandas.DataFrame.groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")
 and [`pandas.Series.groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.groupby.html#pandas.Series.groupby "pandas.Series.groupby")
 respectively.

Indexing, iteration[#](https://pandas.pydata.org/docs/reference/groupby.html#indexing-iteration "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrameGroupBy.__iter__`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.__iter__.html#pandas.api.typing.DataFrameGroupBy.__iter__ "pandas.api.typing.DataFrameGroupBy.__iter__")<br>() | Groupby iterator. |
| [`SeriesGroupBy.__iter__`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.__iter__.html#pandas.api.typing.SeriesGroupBy.__iter__ "pandas.api.typing.SeriesGroupBy.__iter__")<br>() | Groupby iterator. |
| [`DataFrameGroupBy.groups`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.groups.html#pandas.api.typing.DataFrameGroupBy.groups "pandas.api.typing.DataFrameGroupBy.groups") | Dict {group name -> group labels}. |
| [`SeriesGroupBy.groups`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.groups.html#pandas.api.typing.SeriesGroupBy.groups "pandas.api.typing.SeriesGroupBy.groups") | Dict {group name -> group labels}. |
| [`DataFrameGroupBy.indices`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.indices.html#pandas.api.typing.DataFrameGroupBy.indices "pandas.api.typing.DataFrameGroupBy.indices") | Dict {group name -> group indices}. |
| [`SeriesGroupBy.indices`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.indices.html#pandas.api.typing.SeriesGroupBy.indices "pandas.api.typing.SeriesGroupBy.indices") | Dict {group name -> group indices}. |
| [`DataFrameGroupBy.get_group`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.get_group.html#pandas.api.typing.DataFrameGroupBy.get_group "pandas.api.typing.DataFrameGroupBy.get_group")<br>(name) | Construct DataFrame from group with provided name. |
| [`SeriesGroupBy.get_group`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.get_group.html#pandas.api.typing.SeriesGroupBy.get_group "pandas.api.typing.SeriesGroupBy.get_group")<br>(name) | Construct DataFrame from group with provided name. |

|     |     |
| --- | --- |
| [`Grouper`](https://pandas.pydata.org/docs/reference/api/pandas.Grouper.html#pandas.Grouper "pandas.Grouper")<br>(\*args, \*\*kwargs) | A Grouper allows the user to specify a groupby instruction for an object. |

Function application helper[#](https://pandas.pydata.org/docs/reference/groupby.html#function-application-helper "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`NamedAgg`](https://pandas.pydata.org/docs/reference/api/pandas.NamedAgg.html#pandas.NamedAgg "pandas.NamedAgg")<br>(column, aggfunc, \*args, \*\*kwargs) | Helper for column specific aggregation with control over output column names. |

Function application[#](https://pandas.pydata.org/docs/reference/groupby.html#function-application "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`SeriesGroupBy.apply`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.apply.html#pandas.api.typing.SeriesGroupBy.apply "pandas.api.typing.SeriesGroupBy.apply")<br>(func, \*args, \*\*kwargs) | Apply function `func` group-wise and combine the results together. |
| [`DataFrameGroupBy.apply`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.apply.html#pandas.api.typing.DataFrameGroupBy.apply "pandas.api.typing.DataFrameGroupBy.apply")<br>(func, \*args\[, ...\]) | Apply function `func` group-wise and combine the results together. |
| [`SeriesGroupBy.agg`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.agg.html#pandas.api.typing.SeriesGroupBy.agg "pandas.api.typing.SeriesGroupBy.agg")<br>(\[func, engine, engine\_kwargs\]) | Aggregate using one or more operations. |
| [`DataFrameGroupBy.agg`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.agg.html#pandas.api.typing.DataFrameGroupBy.agg "pandas.api.typing.DataFrameGroupBy.agg")<br>(\[func, engine, ...\]) | Aggregate using one or more operations. |
| [`SeriesGroupBy.aggregate`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.aggregate.html#pandas.api.typing.SeriesGroupBy.aggregate "pandas.api.typing.SeriesGroupBy.aggregate")<br>(\[func, engine, ...\]) | Aggregate using one or more operations. |
| [`DataFrameGroupBy.aggregate`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.aggregate.html#pandas.api.typing.DataFrameGroupBy.aggregate "pandas.api.typing.DataFrameGroupBy.aggregate")<br>(\[func, engine, ...\]) | Aggregate using one or more operations. |
| [`SeriesGroupBy.transform`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.transform.html#pandas.api.typing.SeriesGroupBy.transform "pandas.api.typing.SeriesGroupBy.transform")<br>(func, \*args\[, ...\]) | Call function producing a same-indexed Series on each group. |
| [`DataFrameGroupBy.transform`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.transform.html#pandas.api.typing.DataFrameGroupBy.transform "pandas.api.typing.DataFrameGroupBy.transform")<br>(\[func, engine, ...\]) | Call function producing a same-indexed DataFrame on each group. |
| [`SeriesGroupBy.pipe`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.pipe.html#pandas.api.typing.SeriesGroupBy.pipe "pandas.api.typing.SeriesGroupBy.pipe")<br>(func, \*args, \*\*kwargs) | Apply a `func` with arguments to this GroupBy object and return its result. |
| [`DataFrameGroupBy.pipe`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.pipe.html#pandas.api.typing.DataFrameGroupBy.pipe "pandas.api.typing.DataFrameGroupBy.pipe")<br>(func, \*args, \*\*kwargs) | Apply a `func` with arguments to this GroupBy object and return its result. |
| [`DataFrameGroupBy.filter`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.filter.html#pandas.api.typing.DataFrameGroupBy.filter "pandas.api.typing.DataFrameGroupBy.filter")<br>(func\[, dropna\]) | Filter elements from groups that don't satisfy a criterion. |
| [`SeriesGroupBy.filter`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.filter.html#pandas.api.typing.SeriesGroupBy.filter "pandas.api.typing.SeriesGroupBy.filter")<br>(func\[, dropna\]) | Filter elements from groups that don't satisfy a criterion. |

`DataFrameGroupBy` computations / descriptive stats[#](https://pandas.pydata.org/docs/reference/groupby.html#dataframegroupby-computations-descriptive-stats "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrameGroupBy.all`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.all.html#pandas.api.typing.DataFrameGroupBy.all "pandas.api.typing.DataFrameGroupBy.all")<br>(\[skipna\]) | Return True if all values in the group are truthful, else False. |
| [`DataFrameGroupBy.any`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.any.html#pandas.api.typing.DataFrameGroupBy.any "pandas.api.typing.DataFrameGroupBy.any")<br>(\[skipna\]) | Return True if any value in the group is truthful, else False. |
| [`DataFrameGroupBy.bfill`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.bfill.html#pandas.api.typing.DataFrameGroupBy.bfill "pandas.api.typing.DataFrameGroupBy.bfill")<br>(\[limit\]) | Backward fill the values. |
| [`DataFrameGroupBy.corr`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.corr.html#pandas.api.typing.DataFrameGroupBy.corr "pandas.api.typing.DataFrameGroupBy.corr")<br>(\[method, min\_periods, ...\]) | Compute pairwise correlation of columns, excluding NA/null values. |
| [`DataFrameGroupBy.corrwith`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.corrwith.html#pandas.api.typing.DataFrameGroupBy.corrwith "pandas.api.typing.DataFrameGroupBy.corrwith")<br>(other\[, drop, ...\]) | (DEPRECATED) Compute pairwise correlation. |
| [`DataFrameGroupBy.count`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.count.html#pandas.api.typing.DataFrameGroupBy.count "pandas.api.typing.DataFrameGroupBy.count")<br>() | Compute count of group, excluding missing values. |
| [`DataFrameGroupBy.cov`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.cov.html#pandas.api.typing.DataFrameGroupBy.cov "pandas.api.typing.DataFrameGroupBy.cov")<br>(\[min\_periods, ddof, ...\]) | Compute pairwise covariance of columns, excluding NA/null values. |
| [`DataFrameGroupBy.cumcount`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.cumcount.html#pandas.api.typing.DataFrameGroupBy.cumcount "pandas.api.typing.DataFrameGroupBy.cumcount")<br>(\[ascending\]) | Number each item in each group from 0 to the length of that group - 1. |
| [`DataFrameGroupBy.cummax`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.cummax.html#pandas.api.typing.DataFrameGroupBy.cummax "pandas.api.typing.DataFrameGroupBy.cummax")<br>(\[numeric\_only, skipna\]) | Cumulative max for each group. |
| [`DataFrameGroupBy.cummin`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.cummin.html#pandas.api.typing.DataFrameGroupBy.cummin "pandas.api.typing.DataFrameGroupBy.cummin")<br>(\[numeric\_only, skipna\]) | Cumulative min for each group. |
| [`DataFrameGroupBy.cumprod`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.cumprod.html#pandas.api.typing.DataFrameGroupBy.cumprod "pandas.api.typing.DataFrameGroupBy.cumprod")<br>(\[numeric\_only, skipna\]) | Cumulative product for each group. |
| [`DataFrameGroupBy.cumsum`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.cumsum.html#pandas.api.typing.DataFrameGroupBy.cumsum "pandas.api.typing.DataFrameGroupBy.cumsum")<br>(\[numeric\_only, skipna\]) | Cumulative sum for each group. |
| [`DataFrameGroupBy.describe`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.describe.html#pandas.api.typing.DataFrameGroupBy.describe "pandas.api.typing.DataFrameGroupBy.describe")<br>(\[percentiles, ...\]) | Generate descriptive statistics for each group. |
| [`DataFrameGroupBy.diff`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.diff.html#pandas.api.typing.DataFrameGroupBy.diff "pandas.api.typing.DataFrameGroupBy.diff")<br>(\[periods\]) | First discrete difference of element. |
| [`DataFrameGroupBy.ewm`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.ewm.html#pandas.api.typing.DataFrameGroupBy.ewm "pandas.api.typing.DataFrameGroupBy.ewm")<br>(\[com, span, halflife, ...\]) | Return an ewm grouper, providing ewm functionality per group. |
| [`DataFrameGroupBy.expanding`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.expanding.html#pandas.api.typing.DataFrameGroupBy.expanding "pandas.api.typing.DataFrameGroupBy.expanding")<br>(\[min\_periods, method\]) | Return an expanding grouper, providing expanding functionality per group. |
| [`DataFrameGroupBy.ffill`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.ffill.html#pandas.api.typing.DataFrameGroupBy.ffill "pandas.api.typing.DataFrameGroupBy.ffill")<br>(\[limit\]) | Forward fill the values. |
| [`DataFrameGroupBy.first`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.first.html#pandas.api.typing.DataFrameGroupBy.first "pandas.api.typing.DataFrameGroupBy.first")<br>(\[numeric\_only, ...\]) | Compute the first entry of each column within each group. |
| [`DataFrameGroupBy.head`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.head.html#pandas.api.typing.DataFrameGroupBy.head "pandas.api.typing.DataFrameGroupBy.head")<br>(\[n\]) | Return first n rows of each group. |
| [`DataFrameGroupBy.idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.idxmax.html#pandas.api.typing.DataFrameGroupBy.idxmax "pandas.api.typing.DataFrameGroupBy.idxmax")<br>(\[skipna, numeric\_only\]) | Return index of first occurrence of maximum in each group. |
| [`DataFrameGroupBy.idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.idxmin.html#pandas.api.typing.DataFrameGroupBy.idxmin "pandas.api.typing.DataFrameGroupBy.idxmin")<br>(\[skipna, numeric\_only\]) | Return index of first occurrence of minimum in each group. |
| [`DataFrameGroupBy.last`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.last.html#pandas.api.typing.DataFrameGroupBy.last "pandas.api.typing.DataFrameGroupBy.last")<br>(\[numeric\_only, ...\]) | Compute the last entry of each column within each group. |
| [`DataFrameGroupBy.max`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.max.html#pandas.api.typing.DataFrameGroupBy.max "pandas.api.typing.DataFrameGroupBy.max")<br>(\[numeric\_only, ...\]) | Compute max of group values. |
| [`DataFrameGroupBy.mean`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.mean.html#pandas.api.typing.DataFrameGroupBy.mean "pandas.api.typing.DataFrameGroupBy.mean")<br>(\[numeric\_only, ...\]) | Compute mean of groups, excluding missing values. |
| [`DataFrameGroupBy.median`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.median.html#pandas.api.typing.DataFrameGroupBy.median "pandas.api.typing.DataFrameGroupBy.median")<br>(\[numeric\_only, skipna\]) | Compute median of groups, excluding missing values. |
| [`DataFrameGroupBy.min`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.min.html#pandas.api.typing.DataFrameGroupBy.min "pandas.api.typing.DataFrameGroupBy.min")<br>(\[numeric\_only, ...\]) | Compute min of group values. |
| [`DataFrameGroupBy.ngroup`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.ngroup.html#pandas.api.typing.DataFrameGroupBy.ngroup "pandas.api.typing.DataFrameGroupBy.ngroup")<br>(\[ascending\]) | Number each group from 0 to the number of groups - 1. |
| [`DataFrameGroupBy.nth`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.nth.html#pandas.api.typing.DataFrameGroupBy.nth "pandas.api.typing.DataFrameGroupBy.nth") | (DEPRECATED) Take the nth row from each group if n is an int, otherwise a subset of rows. |
| [`DataFrameGroupBy.nunique`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.nunique.html#pandas.api.typing.DataFrameGroupBy.nunique "pandas.api.typing.DataFrameGroupBy.nunique")<br>(\[dropna\]) | Return DataFrame with counts of unique elements in each position. |
| [`DataFrameGroupBy.ohlc`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.ohlc.html#pandas.api.typing.DataFrameGroupBy.ohlc "pandas.api.typing.DataFrameGroupBy.ohlc")<br>() | Compute open, high, low and close values of a group, excluding missing values. |
| [`DataFrameGroupBy.pct_change`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.pct_change.html#pandas.api.typing.DataFrameGroupBy.pct_change "pandas.api.typing.DataFrameGroupBy.pct_change")<br>(\[periods, ...\]) | Calculate pct\_change of each value to previous entry in group. |
| [`DataFrameGroupBy.prod`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.prod.html#pandas.api.typing.DataFrameGroupBy.prod "pandas.api.typing.DataFrameGroupBy.prod")<br>(\[numeric\_only, ...\]) | Compute prod of group values. |
| [`DataFrameGroupBy.quantile`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.quantile.html#pandas.api.typing.DataFrameGroupBy.quantile "pandas.api.typing.DataFrameGroupBy.quantile")<br>(\[q, ...\]) | Return group values at the given quantile, a la numpy.percentile. |
| [`DataFrameGroupBy.rank`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.rank.html#pandas.api.typing.DataFrameGroupBy.rank "pandas.api.typing.DataFrameGroupBy.rank")<br>(\[method, ascending, ...\]) | Provide the rank of values within each group. |
| [`DataFrameGroupBy.resample`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.resample.html#pandas.api.typing.DataFrameGroupBy.resample "pandas.api.typing.DataFrameGroupBy.resample")<br>(rule\[, closed, ...\]) | Provide resampling within each group of a groupby. |
| [`DataFrameGroupBy.rolling`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.rolling.html#pandas.api.typing.DataFrameGroupBy.rolling "pandas.api.typing.DataFrameGroupBy.rolling")<br>(window\[, ...\]) | Return a rolling grouper, providing rolling functionality per group. |
| [`DataFrameGroupBy.sample`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.sample.html#pandas.api.typing.DataFrameGroupBy.sample "pandas.api.typing.DataFrameGroupBy.sample")<br>(\[n, frac, replace, ...\]) | Return a random sample of items from each group. |
| [`DataFrameGroupBy.sem`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.sem.html#pandas.api.typing.DataFrameGroupBy.sem "pandas.api.typing.DataFrameGroupBy.sem")<br>(\[ddof, numeric\_only, ...\]) | Compute standard error of the mean of groups, excluding missing values. |
| [`DataFrameGroupBy.shift`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.shift.html#pandas.api.typing.DataFrameGroupBy.shift "pandas.api.typing.DataFrameGroupBy.shift")<br>(\[periods, freq, ...\]) | Shift each group by periods observations. |
| [`DataFrameGroupBy.size`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.size.html#pandas.api.typing.DataFrameGroupBy.size "pandas.api.typing.DataFrameGroupBy.size")<br>() | Compute group sizes. |
| [`DataFrameGroupBy.skew`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.skew.html#pandas.api.typing.DataFrameGroupBy.skew "pandas.api.typing.DataFrameGroupBy.skew")<br>(\[skipna, numeric\_only\]) | Return unbiased skew within groups. |
| [`DataFrameGroupBy.kurt`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.kurt.html#pandas.api.typing.DataFrameGroupBy.kurt "pandas.api.typing.DataFrameGroupBy.kurt")<br>(\[skipna, numeric\_only\]) | Return unbiased kurtosis within groups. |
| [`DataFrameGroupBy.std`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.std.html#pandas.api.typing.DataFrameGroupBy.std "pandas.api.typing.DataFrameGroupBy.std")<br>(\[ddof, engine, ...\]) | Compute standard deviation of groups, excluding missing values. |
| [`DataFrameGroupBy.sum`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.sum.html#pandas.api.typing.DataFrameGroupBy.sum "pandas.api.typing.DataFrameGroupBy.sum")<br>(\[numeric\_only, ...\]) | Compute sum of group values. |
| [`DataFrameGroupBy.var`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.var.html#pandas.api.typing.DataFrameGroupBy.var "pandas.api.typing.DataFrameGroupBy.var")<br>(\[ddof, engine, ...\]) | Compute variance of groups, excluding missing values. |
| [`DataFrameGroupBy.tail`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.tail.html#pandas.api.typing.DataFrameGroupBy.tail "pandas.api.typing.DataFrameGroupBy.tail")<br>(\[n\]) | Return last n rows of each group. |
| [`DataFrameGroupBy.take`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.take.html#pandas.api.typing.DataFrameGroupBy.take "pandas.api.typing.DataFrameGroupBy.take")<br>(indices, \*\*kwargs) | Return the elements in the given _positional_ indices in each group. |
| [`DataFrameGroupBy.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.value_counts.html#pandas.api.typing.DataFrameGroupBy.value_counts "pandas.api.typing.DataFrameGroupBy.value_counts")<br>(\[subset, ...\]) | Return a Series or DataFrame containing counts of unique rows. |

`SeriesGroupBy` computations / descriptive stats[#](https://pandas.pydata.org/docs/reference/groupby.html#seriesgroupby-computations-descriptive-stats "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`SeriesGroupBy.all`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.all.html#pandas.api.typing.SeriesGroupBy.all "pandas.api.typing.SeriesGroupBy.all")<br>(\[skipna\]) | Return True if all values in the group are truthful, else False. |
| [`SeriesGroupBy.any`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.any.html#pandas.api.typing.SeriesGroupBy.any "pandas.api.typing.SeriesGroupBy.any")<br>(\[skipna\]) | Return True if any value in the group is truthful, else False. |
| [`SeriesGroupBy.bfill`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.bfill.html#pandas.api.typing.SeriesGroupBy.bfill "pandas.api.typing.SeriesGroupBy.bfill")<br>(\[limit\]) | Backward fill the values. |
| [`SeriesGroupBy.corr`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.corr.html#pandas.api.typing.SeriesGroupBy.corr "pandas.api.typing.SeriesGroupBy.corr")<br>(other\[, method, min\_periods\]) | Compute correlation between each group and another Series. |
| [`SeriesGroupBy.count`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.count.html#pandas.api.typing.SeriesGroupBy.count "pandas.api.typing.SeriesGroupBy.count")<br>() | Compute count of group, excluding missing values. |
| [`SeriesGroupBy.cov`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cov.html#pandas.api.typing.SeriesGroupBy.cov "pandas.api.typing.SeriesGroupBy.cov")<br>(other\[, min\_periods, ddof\]) | Compute covariance between each group and another Series. |
| [`SeriesGroupBy.cumcount`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cumcount.html#pandas.api.typing.SeriesGroupBy.cumcount "pandas.api.typing.SeriesGroupBy.cumcount")<br>(\[ascending\]) | Number each item in each group from 0 to the length of that group - 1. |
| [`SeriesGroupBy.cummax`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cummax.html#pandas.api.typing.SeriesGroupBy.cummax "pandas.api.typing.SeriesGroupBy.cummax")<br>(\[numeric\_only, skipna\]) | Cumulative max for each group. |
| [`SeriesGroupBy.cummin`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cummin.html#pandas.api.typing.SeriesGroupBy.cummin "pandas.api.typing.SeriesGroupBy.cummin")<br>(\[numeric\_only, skipna\]) | Cumulative min for each group. |
| [`SeriesGroupBy.cumprod`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cumprod.html#pandas.api.typing.SeriesGroupBy.cumprod "pandas.api.typing.SeriesGroupBy.cumprod")<br>(\[numeric\_only, skipna\]) | Cumulative product for each group. |
| [`SeriesGroupBy.cumsum`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.cumsum.html#pandas.api.typing.SeriesGroupBy.cumsum "pandas.api.typing.SeriesGroupBy.cumsum")<br>(\[numeric\_only, skipna\]) | Cumulative sum for each group. |
| [`SeriesGroupBy.describe`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.describe.html#pandas.api.typing.SeriesGroupBy.describe "pandas.api.typing.SeriesGroupBy.describe")<br>(\[percentiles, ...\]) | Generate descriptive statistics for each group. |
| [`SeriesGroupBy.diff`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.diff.html#pandas.api.typing.SeriesGroupBy.diff "pandas.api.typing.SeriesGroupBy.diff")<br>(\[periods\]) | First discrete difference of element. |
| [`SeriesGroupBy.ewm`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ewm.html#pandas.api.typing.SeriesGroupBy.ewm "pandas.api.typing.SeriesGroupBy.ewm")<br>(\[com, span, halflife, ...\]) | Return an ewm grouper, providing ewm functionality per group. |
| [`SeriesGroupBy.expanding`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.expanding.html#pandas.api.typing.SeriesGroupBy.expanding "pandas.api.typing.SeriesGroupBy.expanding")<br>(\[min\_periods, method\]) | Return an expanding grouper, providing expanding functionality per group. |
| [`SeriesGroupBy.ffill`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ffill.html#pandas.api.typing.SeriesGroupBy.ffill "pandas.api.typing.SeriesGroupBy.ffill")<br>(\[limit\]) | Forward fill the values. |
| [`SeriesGroupBy.first`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.first.html#pandas.api.typing.SeriesGroupBy.first "pandas.api.typing.SeriesGroupBy.first")<br>(\[numeric\_only, ...\]) | Compute the first entry of each column within each group. |
| [`SeriesGroupBy.head`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.head.html#pandas.api.typing.SeriesGroupBy.head "pandas.api.typing.SeriesGroupBy.head")<br>(\[n\]) | Return first n rows of each group. |
| [`SeriesGroupBy.last`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.last.html#pandas.api.typing.SeriesGroupBy.last "pandas.api.typing.SeriesGroupBy.last")<br>(\[numeric\_only, ...\]) | Compute the last entry of each column within each group. |
| [`SeriesGroupBy.idxmax`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.idxmax.html#pandas.api.typing.SeriesGroupBy.idxmax "pandas.api.typing.SeriesGroupBy.idxmax")<br>(\[skipna\]) | Return the row label of the maximum value. |
| [`SeriesGroupBy.idxmin`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.idxmin.html#pandas.api.typing.SeriesGroupBy.idxmin "pandas.api.typing.SeriesGroupBy.idxmin")<br>(\[skipna\]) | Return the row label of the minimum value. |
| [`SeriesGroupBy.is_monotonic_increasing`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_increasing.html#pandas.api.typing.SeriesGroupBy.is_monotonic_increasing "pandas.api.typing.SeriesGroupBy.is_monotonic_increasing") | Return whether each group's values are monotonically increasing. |
| [`SeriesGroupBy.is_monotonic_decreasing`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.is_monotonic_decreasing.html#pandas.api.typing.SeriesGroupBy.is_monotonic_decreasing "pandas.api.typing.SeriesGroupBy.is_monotonic_decreasing") | Return whether each group's values are monotonically decreasing. |
| [`SeriesGroupBy.max`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.max.html#pandas.api.typing.SeriesGroupBy.max "pandas.api.typing.SeriesGroupBy.max")<br>(\[numeric\_only, min\_count, ...\]) | Compute max of group values. |
| [`SeriesGroupBy.mean`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.mean.html#pandas.api.typing.SeriesGroupBy.mean "pandas.api.typing.SeriesGroupBy.mean")<br>(\[numeric\_only, skipna, ...\]) | Compute mean of groups, excluding missing values. |
| [`SeriesGroupBy.median`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.median.html#pandas.api.typing.SeriesGroupBy.median "pandas.api.typing.SeriesGroupBy.median")<br>(\[numeric\_only, skipna\]) | Compute median of groups, excluding missing values. |
| [`SeriesGroupBy.min`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.min.html#pandas.api.typing.SeriesGroupBy.min "pandas.api.typing.SeriesGroupBy.min")<br>(\[numeric\_only, min\_count, ...\]) | Compute min of group values. |
| [`SeriesGroupBy.ngroup`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ngroup.html#pandas.api.typing.SeriesGroupBy.ngroup "pandas.api.typing.SeriesGroupBy.ngroup")<br>(\[ascending\]) | Number each group from 0 to the number of groups - 1. |
| [`SeriesGroupBy.nlargest`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nlargest.html#pandas.api.typing.SeriesGroupBy.nlargest "pandas.api.typing.SeriesGroupBy.nlargest")<br>(\[n, keep\]) | Return the largest n elements. |
| [`SeriesGroupBy.nsmallest`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nsmallest.html#pandas.api.typing.SeriesGroupBy.nsmallest "pandas.api.typing.SeriesGroupBy.nsmallest")<br>(\[n, keep\]) | Return the smallest n elements. |
| [`SeriesGroupBy.nth`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nth.html#pandas.api.typing.SeriesGroupBy.nth "pandas.api.typing.SeriesGroupBy.nth") | (DEPRECATED) Take the nth row from each group if n is an int, otherwise a subset of rows. |
| [`SeriesGroupBy.nunique`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.nunique.html#pandas.api.typing.SeriesGroupBy.nunique "pandas.api.typing.SeriesGroupBy.nunique")<br>(\[dropna\]) | Return number of unique elements in the group. |
| [`SeriesGroupBy.unique`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.unique.html#pandas.api.typing.SeriesGroupBy.unique "pandas.api.typing.SeriesGroupBy.unique")<br>() | Return unique values for each group. |
| [`SeriesGroupBy.ohlc`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.ohlc.html#pandas.api.typing.SeriesGroupBy.ohlc "pandas.api.typing.SeriesGroupBy.ohlc")<br>() | Compute open, high, low and close values of a group, excluding missing values. |
| [`SeriesGroupBy.pct_change`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.pct_change.html#pandas.api.typing.SeriesGroupBy.pct_change "pandas.api.typing.SeriesGroupBy.pct_change")<br>(\[periods, ...\]) | Calculate pct\_change of each value to previous entry in group. |
| [`SeriesGroupBy.prod`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.prod.html#pandas.api.typing.SeriesGroupBy.prod "pandas.api.typing.SeriesGroupBy.prod")<br>(\[numeric\_only, ...\]) | Compute prod of group values. |
| [`SeriesGroupBy.quantile`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.quantile.html#pandas.api.typing.SeriesGroupBy.quantile "pandas.api.typing.SeriesGroupBy.quantile")<br>(\[q, interpolation, ...\]) | Return group values at the given quantile, a la numpy.percentile. |
| [`SeriesGroupBy.rank`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.rank.html#pandas.api.typing.SeriesGroupBy.rank "pandas.api.typing.SeriesGroupBy.rank")<br>(\[method, ascending, ...\]) | Provide the rank of values within each group. |
| [`SeriesGroupBy.resample`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.resample.html#pandas.api.typing.SeriesGroupBy.resample "pandas.api.typing.SeriesGroupBy.resample")<br>(rule\[, closed, ...\]) | Provide resampling within each group of a groupby. |
| [`SeriesGroupBy.rolling`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.rolling.html#pandas.api.typing.SeriesGroupBy.rolling "pandas.api.typing.SeriesGroupBy.rolling")<br>(window\[, min\_periods, ...\]) | Return a rolling grouper, providing rolling functionality per group. |
| [`SeriesGroupBy.sample`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.sample.html#pandas.api.typing.SeriesGroupBy.sample "pandas.api.typing.SeriesGroupBy.sample")<br>(\[n, frac, replace, ...\]) | Return a random sample of items from each group. |
| [`SeriesGroupBy.sem`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.sem.html#pandas.api.typing.SeriesGroupBy.sem "pandas.api.typing.SeriesGroupBy.sem")<br>(\[ddof, numeric\_only, skipna\]) | Compute standard error of the mean of groups, excluding missing values. |
| [`SeriesGroupBy.shift`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.shift.html#pandas.api.typing.SeriesGroupBy.shift "pandas.api.typing.SeriesGroupBy.shift")<br>(\[periods, freq, ...\]) | Shift each group by periods observations. |
| [`SeriesGroupBy.size`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.size.html#pandas.api.typing.SeriesGroupBy.size "pandas.api.typing.SeriesGroupBy.size")<br>() | Compute group sizes. |
| [`SeriesGroupBy.skew`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.skew.html#pandas.api.typing.SeriesGroupBy.skew "pandas.api.typing.SeriesGroupBy.skew")<br>(\[skipna, numeric\_only\]) | Return unbiased skew within groups. |
| [`SeriesGroupBy.kurt`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.kurt.html#pandas.api.typing.SeriesGroupBy.kurt "pandas.api.typing.SeriesGroupBy.kurt")<br>(\[skipna, numeric\_only\]) | Return unbiased kurtosis within groups. |
| [`SeriesGroupBy.std`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.std.html#pandas.api.typing.SeriesGroupBy.std "pandas.api.typing.SeriesGroupBy.std")<br>(\[ddof, engine, ...\]) | Compute standard deviation of groups, excluding missing values. |
| [`SeriesGroupBy.sum`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.sum.html#pandas.api.typing.SeriesGroupBy.sum "pandas.api.typing.SeriesGroupBy.sum")<br>(\[numeric\_only, min\_count, ...\]) | Compute sum of group values. |
| [`SeriesGroupBy.var`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.var.html#pandas.api.typing.SeriesGroupBy.var "pandas.api.typing.SeriesGroupBy.var")<br>(\[ddof, engine, ...\]) | Compute variance of groups, excluding missing values. |
| [`SeriesGroupBy.tail`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.tail.html#pandas.api.typing.SeriesGroupBy.tail "pandas.api.typing.SeriesGroupBy.tail")<br>(\[n\]) | Return last n rows of each group. |
| [`SeriesGroupBy.take`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.take.html#pandas.api.typing.SeriesGroupBy.take "pandas.api.typing.SeriesGroupBy.take")<br>(indices, \*\*kwargs) | Return the elements in the given _positional_ indices in each group. |
| [`SeriesGroupBy.value_counts`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.value_counts.html#pandas.api.typing.SeriesGroupBy.value_counts "pandas.api.typing.SeriesGroupBy.value_counts")<br>(\[normalize, ...\]) | Return a Series or DataFrame containing counts of unique rows. |

Plotting and visualization[#](https://pandas.pydata.org/docs/reference/groupby.html#plotting-and-visualization "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`DataFrameGroupBy.boxplot`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.boxplot.html#pandas.api.typing.DataFrameGroupBy.boxplot "pandas.api.typing.DataFrameGroupBy.boxplot")<br>(\[subplots, column, ...\]) | Make box plots from DataFrameGroupBy data. |
| [`DataFrameGroupBy.hist`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.hist.html#pandas.api.typing.DataFrameGroupBy.hist "pandas.api.typing.DataFrameGroupBy.hist")<br>(\[column, by, grid, ...\]) | Draw histogram of the DataFrame's columns for each group. |
| [`SeriesGroupBy.hist`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.hist.html#pandas.api.typing.SeriesGroupBy.hist "pandas.api.typing.SeriesGroupBy.hist")<br>(\[by, ax, grid, ...\]) | Draw histogram for each group's values using `Series.hist()` API. |
| [`DataFrameGroupBy.plot`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.DataFrameGroupBy.plot.html#pandas.api.typing.DataFrameGroupBy.plot "pandas.api.typing.DataFrameGroupBy.plot") | Make plots of groups from a DataFrame. |
| [`SeriesGroupBy.plot`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.SeriesGroupBy.plot.html#pandas.api.typing.SeriesGroupBy.plot "pandas.api.typing.SeriesGroupBy.plot") | Make plots of groups from a Series. |

On this page