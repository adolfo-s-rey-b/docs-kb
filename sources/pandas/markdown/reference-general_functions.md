[Skip to main content](https://pandas.pydata.org/docs/reference/general_functions.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/general_functions.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/general_functions.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/general_functions.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/general_functions.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/general_functions.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/general_functions.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/general_functions.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/general_functions.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/general_functions.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/general_functions.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/general_functions.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/general_functions.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/general_functions.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

General functions[#](https://pandas.pydata.org/docs/reference/general_functions.html#general-functions "Link to this heading")

===============================================================================================================================

Note

For an overview, see [Reshaping and pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping)
.

Data manipulations[#](https://pandas.pydata.org/docs/reference/general_functions.html#data-manipulations "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`melt`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html#pandas.melt "pandas.melt")<br>(frame\[, id\_vars, value\_vars, var\_name, ...\]) | Unpivot a DataFrame from wide to long format, optionally leaving identifiers set. |
| [`pivot`](https://pandas.pydata.org/docs/reference/api/pandas.pivot.html#pandas.pivot "pandas.pivot")<br>(data, \*, columns\[, index, values\]) | Return reshaped DataFrame organized by given index / column values. |
| [`pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.pivot_table.html#pandas.pivot_table "pandas.pivot_table")<br>(data\[, values, index, columns, ...\]) | Create a spreadsheet-style pivot table as a DataFrame. |
| [`crosstab`](https://pandas.pydata.org/docs/reference/api/pandas.crosstab.html#pandas.crosstab "pandas.crosstab")<br>(index, columns\[, values, rownames, ...\]) | Compute a simple cross tabulation of two (or more) factors. |
| [`cut`](https://pandas.pydata.org/docs/reference/api/pandas.cut.html#pandas.cut "pandas.cut")<br>(x, bins\[, right, labels, retbins, ...\]) | Bin values into discrete intervals. |
| [`qcut`](https://pandas.pydata.org/docs/reference/api/pandas.qcut.html#pandas.qcut "pandas.qcut")<br>(x, q\[, labels, retbins, precision, ...\]) | Quantile-based discretization function. |
| [`merge`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html#pandas.merge "pandas.merge")<br>(left, right\[, how, on, left\_on, ...\]) | Merge DataFrame or named Series objects with a database-style join. |
| [`merge_ordered`](https://pandas.pydata.org/docs/reference/api/pandas.merge_ordered.html#pandas.merge_ordered "pandas.merge_ordered")<br>(left, right\[, on, left\_on, ...\]) | Perform a merge for ordered data with optional filling/interpolation. |
| [`merge_asof`](https://pandas.pydata.org/docs/reference/api/pandas.merge_asof.html#pandas.merge_asof "pandas.merge_asof")<br>(left, right\[, on, left\_on, ...\]) | Perform a merge by key distance. |
| [`concat`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat "pandas.concat")<br>(objs, \*\[, axis, join, ignore\_index, ...\]) | Concatenate pandas objects along a particular axis. |
| [`get_dummies`](https://pandas.pydata.org/docs/reference/api/pandas.get_dummies.html#pandas.get_dummies "pandas.get_dummies")<br>(data\[, prefix, prefix\_sep, ...\]) | Convert categorical variable into dummy/indicator variables. |
| [`from_dummies`](https://pandas.pydata.org/docs/reference/api/pandas.from_dummies.html#pandas.from_dummies "pandas.from_dummies")<br>(data\[, sep, default\_category\]) | Create a categorical `DataFrame` from a `DataFrame` of dummy variables. |
| [`factorize`](https://pandas.pydata.org/docs/reference/api/pandas.factorize.html#pandas.factorize "pandas.factorize")<br>(values\[, sort, use\_na\_sentinel, ...\]) | Encode the object as an enumerated type or categorical variable. |
| [`unique`](https://pandas.pydata.org/docs/reference/api/pandas.unique.html#pandas.unique "pandas.unique")<br>(values) | Return unique values based on a hash table. |
| [`lreshape`](https://pandas.pydata.org/docs/reference/api/pandas.lreshape.html#pandas.lreshape "pandas.lreshape")<br>(data, groups\[, dropna\]) | Reshape wide-format data to long. |
| [`wide_to_long`](https://pandas.pydata.org/docs/reference/api/pandas.wide_to_long.html#pandas.wide_to_long "pandas.wide_to_long")<br>(df, stubnames, i, j\[, sep, suffix\]) | Unpivot a DataFrame from wide to long format. |

Top-level missing data[#](https://pandas.pydata.org/docs/reference/general_functions.html#top-level-missing-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`isna`](https://pandas.pydata.org/docs/reference/api/pandas.isna.html#pandas.isna "pandas.isna")<br>(obj) | Detect missing values for an array-like object. |
| [`isnull`](https://pandas.pydata.org/docs/reference/api/pandas.isnull.html#pandas.isnull "pandas.isnull")<br>(obj) | Detect missing values for an array-like object. |
| [`notna`](https://pandas.pydata.org/docs/reference/api/pandas.notna.html#pandas.notna "pandas.notna")<br>(obj) | Detect non-missing values for an array-like object. |
| [`notnull`](https://pandas.pydata.org/docs/reference/api/pandas.notnull.html#pandas.notnull "pandas.notnull")<br>(obj) | Detect non-missing values for an array-like object. |

Top-level dealing with numeric data[#](https://pandas.pydata.org/docs/reference/general_functions.html#top-level-dealing-with-numeric-data "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`to_numeric`](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html#pandas.to_numeric "pandas.to_numeric")<br>(arg\[, errors, downcast, ...\]) | Convert argument to a numeric type. |

Top-level dealing with datetimelike data[#](https://pandas.pydata.org/docs/reference/general_functions.html#top-level-dealing-with-datetimelike-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`to_datetime`](https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html#pandas.to_datetime "pandas.to_datetime")<br>(arg\[, errors, dayfirst, ...\]) | Convert argument to datetime. |
| [`to_timedelta`](https://pandas.pydata.org/docs/reference/api/pandas.to_timedelta.html#pandas.to_timedelta "pandas.to_timedelta")<br>(arg\[, unit, errors\]) | Convert argument to timedelta. |
| [`date_range`](https://pandas.pydata.org/docs/reference/api/pandas.date_range.html#pandas.date_range "pandas.date_range")<br>(\[start, end, periods, freq, tz, ...\]) | Return a fixed frequency DatetimeIndex. |
| [`bdate_range`](https://pandas.pydata.org/docs/reference/api/pandas.bdate_range.html#pandas.bdate_range "pandas.bdate_range")<br>(\[start, end, periods, freq, tz, ...\]) | Return a fixed frequency DatetimeIndex with business day as the default. |
| [`period_range`](https://pandas.pydata.org/docs/reference/api/pandas.period_range.html#pandas.period_range "pandas.period_range")<br>(\[start, end, periods, freq, name\]) | Return a fixed frequency PeriodIndex. |
| [`timedelta_range`](https://pandas.pydata.org/docs/reference/api/pandas.timedelta_range.html#pandas.timedelta_range "pandas.timedelta_range")<br>(\[start, end, periods, freq, ...\]) | Return a fixed frequency TimedeltaIndex with day as the default. |
| [`infer_freq`](https://pandas.pydata.org/docs/reference/api/pandas.infer_freq.html#pandas.infer_freq "pandas.infer_freq")<br>(index) | (DEPRECATED) Infer the most likely frequency given the input index. |

Top-level dealing with Interval data[#](https://pandas.pydata.org/docs/reference/general_functions.html#top-level-dealing-with-interval-data "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`interval_range`](https://pandas.pydata.org/docs/reference/api/pandas.interval_range.html#pandas.interval_range "pandas.interval_range")<br>(\[start, end, periods, freq, ...\]) | Return a fixed frequency IntervalIndex. |

Top-level evaluation[#](https://pandas.pydata.org/docs/reference/general_functions.html#top-level-evaluation "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`col`](https://pandas.pydata.org/docs/reference/api/pandas.col.html#pandas.col "pandas.col")<br>(col\_name) | Generate deferred object representing a column of a DataFrame. |
| [`eval`](https://pandas.pydata.org/docs/reference/api/pandas.eval.html#pandas.eval "pandas.eval")<br>(expr\[, parser, engine, local\_dict, ...\]) | Evaluate a Python expression as a string using various backends. |

|     |     |
| --- | --- |
| [`api.typing.Expression`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expression.html#pandas.api.typing.Expression "pandas.api.typing.Expression")<br>(func, repr\_str\[, ...\]) | Class representing a deferred expression evaluated against a DataFrame. |

Datetime formats[#](https://pandas.pydata.org/docs/reference/general_functions.html#datetime-formats "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`tseries.api.guess_datetime_format`](https://pandas.pydata.org/docs/reference/api/pandas.tseries.api.guess_datetime_format.html#pandas.tseries.api.guess_datetime_format "pandas.tseries.api.guess_datetime_format")<br>(dt\_str\[, ...\]) | Guess the datetime format of a given datetime string. |

Hashing[#](https://pandas.pydata.org/docs/reference/general_functions.html#hashing "Link to this heading")

-----------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`util.hash_array`](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_array.html#pandas.util.hash_array "pandas.util.hash_array")<br>(vals\[, encoding, hash\_key, ...\]) | Given a 1d array, return an array of deterministic integers. |
| [`util.hash_pandas_object`](https://pandas.pydata.org/docs/reference/api/pandas.util.hash_pandas_object.html#pandas.util.hash_pandas_object "pandas.util.hash_pandas_object")<br>(obj\[, index, ...\]) | Return a data hash of the Index/Series/DataFrame. |

Importing from other DataFrame libraries[#](https://pandas.pydata.org/docs/reference/general_functions.html#importing-from-other-dataframe-libraries "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`api.interchange.from_dataframe`](https://pandas.pydata.org/docs/reference/api/pandas.api.interchange.from_dataframe.html#pandas.api.interchange.from_dataframe "pandas.api.interchange.from_dataframe")<br>(df\[, allow\_copy\]) | Build a `pd.DataFrame` from any DataFrame supporting the interchange protocol. |

On this page