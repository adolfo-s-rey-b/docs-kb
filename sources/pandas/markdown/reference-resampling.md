[Skip to main content](https://pandas.pydata.org/docs/reference/resampling.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/resampling.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/resampling.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/resampling.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/resampling.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/resampling.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/resampling.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/resampling.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/resampling.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/resampling.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/resampling.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/resampling.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/resampling.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/resampling.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Resampling[#](https://pandas.pydata.org/docs/reference/resampling.html#resampling "Link to this heading")

==========================================================================================================

Note

For an overview, see [Time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries)
.

`pandas.api.typing.Resampler` instances are returned by resample calls: [`pandas.DataFrame.resample()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.resample.html#pandas.DataFrame.resample "pandas.DataFrame.resample")
, [`pandas.Series.resample()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.resample.html#pandas.Series.resample "pandas.Series.resample")
.

Indexing, iteration[#](https://pandas.pydata.org/docs/reference/resampling.html#indexing-iteration "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Resampler.__iter__`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.__iter__.html#pandas.api.typing.Resampler.__iter__ "pandas.api.typing.Resampler.__iter__")<br>() | Groupby iterator. |
| [`Resampler.groups`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.groups.html#pandas.api.typing.Resampler.groups "pandas.api.typing.Resampler.groups") | Dict {group name -> group labels}. |
| [`Resampler.indices`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.indices.html#pandas.api.typing.Resampler.indices "pandas.api.typing.Resampler.indices") | Dict {group name -> group indices}. |
| [`Resampler.get_group`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.get_group.html#pandas.api.typing.Resampler.get_group "pandas.api.typing.Resampler.get_group")<br>(name) | Construct DataFrame from group with provided name. |

Function application[#](https://pandas.pydata.org/docs/reference/resampling.html#function-application "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Resampler.apply`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.apply.html#pandas.api.typing.Resampler.apply "pandas.api.typing.Resampler.apply")<br>(\[func\]) | Aggregate using one or more operations over the specified axis. |
| [`Resampler.aggregate`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.aggregate.html#pandas.api.typing.Resampler.aggregate "pandas.api.typing.Resampler.aggregate")<br>(\[func\]) | Aggregate using one or more operations over the specified axis. |
| [`Resampler.transform`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.transform.html#pandas.api.typing.Resampler.transform "pandas.api.typing.Resampler.transform")<br>(arg, \*args, \*\*kwargs) | Call function producing a like-indexed Series on each group. |
| [`Resampler.pipe`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.pipe.html#pandas.api.typing.Resampler.pipe "pandas.api.typing.Resampler.pipe")<br>(func, \*args, \*\*kwargs) | Apply a `func` with arguments to this Resampler object and return its result. |

Upsampling[#](https://pandas.pydata.org/docs/reference/resampling.html#upsampling "Link to this heading")

----------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Resampler.ffill`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.ffill.html#pandas.api.typing.Resampler.ffill "pandas.api.typing.Resampler.ffill")<br>(\[limit\]) | Forward fill the values. |
| [`Resampler.bfill`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.bfill.html#pandas.api.typing.Resampler.bfill "pandas.api.typing.Resampler.bfill")<br>(\[limit\]) | Backward fill the new missing values in the resampled data. |
| [`Resampler.nearest`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.nearest.html#pandas.api.typing.Resampler.nearest "pandas.api.typing.Resampler.nearest")<br>(\[limit\]) | Resample by using the nearest value. |
| [`Resampler.asfreq`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.asfreq.html#pandas.api.typing.Resampler.asfreq "pandas.api.typing.Resampler.asfreq")<br>(\[fill\_value\]) | Return the values at the new freq, essentially a reindex. |
| [`Resampler.interpolate`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.interpolate.html#pandas.api.typing.Resampler.interpolate "pandas.api.typing.Resampler.interpolate")<br>(\[method, axis, limit, ...\]) | Interpolate values between target timestamps according to different methods. |

Computations / descriptive stats[#](https://pandas.pydata.org/docs/reference/resampling.html#computations-descriptive-stats "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Resampler.count`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.count.html#pandas.api.typing.Resampler.count "pandas.api.typing.Resampler.count")<br>() | Compute count of group, excluding missing values. |
| [`Resampler.nunique`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.nunique.html#pandas.api.typing.Resampler.nunique "pandas.api.typing.Resampler.nunique")<br>() | Return number of unique elements in the group. |
| [`Resampler.first`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.first.html#pandas.api.typing.Resampler.first "pandas.api.typing.Resampler.first")<br>(\[numeric\_only, min\_count, ...\]) | Compute the first non-null entry of each column. |
| [`Resampler.last`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.last.html#pandas.api.typing.Resampler.last "pandas.api.typing.Resampler.last")<br>(\[numeric\_only, min\_count, skipna\]) | Compute the last non-null entry of each column. |
| [`Resampler.max`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.max.html#pandas.api.typing.Resampler.max "pandas.api.typing.Resampler.max")<br>(\[numeric\_only, min\_count\]) | Compute max value of group. |
| [`Resampler.mean`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.mean.html#pandas.api.typing.Resampler.mean "pandas.api.typing.Resampler.mean")<br>(\[numeric\_only\]) | Compute mean of groups, excluding missing values. |
| [`Resampler.median`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.median.html#pandas.api.typing.Resampler.median "pandas.api.typing.Resampler.median")<br>(\[numeric\_only\]) | Compute median of groups, excluding missing values. |
| [`Resampler.min`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.min.html#pandas.api.typing.Resampler.min "pandas.api.typing.Resampler.min")<br>(\[numeric\_only, min\_count\]) | Compute min value of group. |
| [`Resampler.ohlc`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.ohlc.html#pandas.api.typing.Resampler.ohlc "pandas.api.typing.Resampler.ohlc")<br>() | Compute open, high, low and close values of a group, excluding missing values. |
| [`Resampler.prod`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.prod.html#pandas.api.typing.Resampler.prod "pandas.api.typing.Resampler.prod")<br>(\[numeric\_only, min\_count\]) | Compute prod of group values. |
| [`Resampler.size`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.size.html#pandas.api.typing.Resampler.size "pandas.api.typing.Resampler.size")<br>() | Compute group sizes. |
| [`Resampler.sem`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.sem.html#pandas.api.typing.Resampler.sem "pandas.api.typing.Resampler.sem")<br>(\[ddof, numeric\_only\]) | Compute standard error of the mean of groups, excluding missing values. |
| [`Resampler.std`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.std.html#pandas.api.typing.Resampler.std "pandas.api.typing.Resampler.std")<br>(\[ddof, numeric\_only\]) | Compute standard deviation of groups, excluding missing values. |
| [`Resampler.sum`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.sum.html#pandas.api.typing.Resampler.sum "pandas.api.typing.Resampler.sum")<br>(\[numeric\_only, min\_count\]) | Compute sum of group values. |
| [`Resampler.var`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.var.html#pandas.api.typing.Resampler.var "pandas.api.typing.Resampler.var")<br>(\[ddof, numeric\_only\]) | Compute variance of groups, excluding missing values. |
| [`Resampler.quantile`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.quantile.html#pandas.api.typing.Resampler.quantile "pandas.api.typing.Resampler.quantile")<br>(\[q\]) | Return value at the given quantile. |

On this page