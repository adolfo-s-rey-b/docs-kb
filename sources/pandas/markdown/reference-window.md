[Skip to main content](https://pandas.pydata.org/docs/reference/window.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/window.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/window.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/window.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/window.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/window.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/window.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/window.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/window.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/window.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/window.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/window.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/window.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/window.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Window[#](https://pandas.pydata.org/docs/reference/window.html#window "Link to this heading")

==============================================================================================

Note

For an overview, see [Windowing operations](https://pandas.pydata.org/docs/user_guide/window.html#window)
.

`pandas.api.typing.Rolling` instances are returned by `.rolling` calls: [`pandas.DataFrame.rolling()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rolling.html#pandas.DataFrame.rolling "pandas.DataFrame.rolling")
 and [`pandas.Series.rolling()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.rolling.html#pandas.Series.rolling "pandas.Series.rolling")
. `pandas.api.typing.Expanding` instances are returned by `.expanding` calls: [`pandas.DataFrame.expanding()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.expanding.html#pandas.DataFrame.expanding "pandas.DataFrame.expanding")
 and [`pandas.Series.expanding()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.expanding.html#pandas.Series.expanding "pandas.Series.expanding")
. `pandas.api.typing.ExponentialMovingWindow` instances are returned by `.ewm` calls: [`pandas.DataFrame.ewm()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.ewm.html#pandas.DataFrame.ewm "pandas.DataFrame.ewm")
 and [`pandas.Series.ewm()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.ewm.html#pandas.Series.ewm "pandas.Series.ewm")
.

Rolling window functions[#](https://pandas.pydata.org/docs/reference/window.html#rolling-window-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Rolling.count`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.count.html#pandas.api.typing.Rolling.count "pandas.api.typing.Rolling.count")<br>(\[numeric\_only\]) | Calculate the rolling count of non NaN observations. |
| [`Rolling.sum`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.sum.html#pandas.api.typing.Rolling.sum "pandas.api.typing.Rolling.sum")<br>(\[numeric\_only, engine, ...\]) | Calculate the rolling sum. |
| [`Rolling.mean`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.mean.html#pandas.api.typing.Rolling.mean "pandas.api.typing.Rolling.mean")<br>(\[numeric\_only, engine, ...\]) | Calculate the rolling mean. |
| [`Rolling.median`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.median.html#pandas.api.typing.Rolling.median "pandas.api.typing.Rolling.median")<br>(\[numeric\_only, engine, ...\]) | Calculate the rolling median. |
| [`Rolling.var`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.var.html#pandas.api.typing.Rolling.var "pandas.api.typing.Rolling.var")<br>(\[ddof, numeric\_only, engine, ...\]) | Calculate the rolling variance. |
| [`Rolling.std`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.std.html#pandas.api.typing.Rolling.std "pandas.api.typing.Rolling.std")<br>(\[ddof, numeric\_only, engine, ...\]) | Calculate the rolling standard deviation. |
| [`Rolling.min`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.min.html#pandas.api.typing.Rolling.min "pandas.api.typing.Rolling.min")<br>(\[numeric\_only, engine, ...\]) | Calculate the rolling minimum. |
| [`Rolling.max`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.max.html#pandas.api.typing.Rolling.max "pandas.api.typing.Rolling.max")<br>(\[numeric\_only, engine, ...\]) | Calculate the rolling maximum. |
| [`Rolling.first`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.first.html#pandas.api.typing.Rolling.first "pandas.api.typing.Rolling.first")<br>(\[numeric\_only\]) | Calculate the rolling First (left-most) element of the window. |
| [`Rolling.last`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.last.html#pandas.api.typing.Rolling.last "pandas.api.typing.Rolling.last")<br>(\[numeric\_only\]) | Calculate the rolling Last (right-most) element of the window. |
| [`Rolling.corr`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.corr.html#pandas.api.typing.Rolling.corr "pandas.api.typing.Rolling.corr")<br>(\[other, pairwise, ddof, ...\]) | Calculate the rolling correlation. |
| [`Rolling.cov`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.cov.html#pandas.api.typing.Rolling.cov "pandas.api.typing.Rolling.cov")<br>(\[other, pairwise, ddof, ...\]) | Calculate the rolling sample covariance. |
| [`Rolling.skew`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.skew.html#pandas.api.typing.Rolling.skew "pandas.api.typing.Rolling.skew")<br>(\[numeric\_only\]) | Calculate the rolling unbiased skewness. |
| [`Rolling.kurt`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.kurt.html#pandas.api.typing.Rolling.kurt "pandas.api.typing.Rolling.kurt")<br>(\[numeric\_only\]) | Calculate the rolling Fisher's definition of kurtosis without bias. |
| [`Rolling.apply`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.apply.html#pandas.api.typing.Rolling.apply "pandas.api.typing.Rolling.apply")<br>(func\[, raw, engine, ...\]) | Calculate the rolling custom aggregation function. |
| [`Rolling.pipe`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.pipe.html#pandas.api.typing.Rolling.pipe "pandas.api.typing.Rolling.pipe")<br>(func, \*args, \*\*kwargs) | Apply a `func` with arguments to this Rolling object and return its result. |
| [`Rolling.aggregate`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.aggregate.html#pandas.api.typing.Rolling.aggregate "pandas.api.typing.Rolling.aggregate")<br>(\[func\]) | Aggregate using one or more operations over the specified axis. |
| [`Rolling.quantile`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.quantile.html#pandas.api.typing.Rolling.quantile "pandas.api.typing.Rolling.quantile")<br>(q\[, interpolation, ...\]) | Calculate the rolling quantile. |
| [`Rolling.sem`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.sem.html#pandas.api.typing.Rolling.sem "pandas.api.typing.Rolling.sem")<br>(\[ddof, numeric\_only\]) | Calculate the rolling standard error of mean. |
| [`Rolling.rank`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.rank.html#pandas.api.typing.Rolling.rank "pandas.api.typing.Rolling.rank")<br>(\[method, ascending, pct, ...\]) | Calculate the rolling rank. |
| [`Rolling.nunique`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Rolling.nunique.html#pandas.api.typing.Rolling.nunique "pandas.api.typing.Rolling.nunique")<br>(\[numeric\_only\]) | Calculate the rolling nunique. |

Weighted window functions[#](https://pandas.pydata.org/docs/reference/window.html#weighted-window-functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Window.mean`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Window.mean.html#pandas.api.typing.Window.mean "pandas.api.typing.Window.mean")<br>(\[numeric\_only\]) | Calculate the rolling weighted window mean. |
| [`Window.sum`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Window.sum.html#pandas.api.typing.Window.sum "pandas.api.typing.Window.sum")<br>(\[numeric\_only\]) | Calculate the rolling weighted window sum. |
| [`Window.var`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Window.var.html#pandas.api.typing.Window.var "pandas.api.typing.Window.var")<br>(\[ddof, numeric\_only\]) | Calculate the rolling weighted window variance. |
| [`Window.std`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Window.std.html#pandas.api.typing.Window.std "pandas.api.typing.Window.std")<br>(\[ddof, numeric\_only\]) | Calculate the rolling weighted window standard deviation. |

Expanding window functions[#](https://pandas.pydata.org/docs/reference/window.html#expanding-window-functions "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`Expanding.count`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.count.html#pandas.api.typing.Expanding.count "pandas.api.typing.Expanding.count")<br>(\[numeric\_only\]) | Calculate the expanding count of non NaN observations. |
| [`Expanding.sum`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.sum.html#pandas.api.typing.Expanding.sum "pandas.api.typing.Expanding.sum")<br>(\[numeric\_only, engine, ...\]) | Calculate the expanding sum. |
| [`Expanding.mean`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.mean.html#pandas.api.typing.Expanding.mean "pandas.api.typing.Expanding.mean")<br>(\[numeric\_only, engine, ...\]) | Calculate the expanding mean. |
| [`Expanding.median`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.median.html#pandas.api.typing.Expanding.median "pandas.api.typing.Expanding.median")<br>(\[numeric\_only, engine, ...\]) | Calculate the expanding median. |
| [`Expanding.var`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.var.html#pandas.api.typing.Expanding.var "pandas.api.typing.Expanding.var")<br>(\[ddof, numeric\_only, engine, ...\]) | Calculate the expanding variance. |
| [`Expanding.std`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.std.html#pandas.api.typing.Expanding.std "pandas.api.typing.Expanding.std")<br>(\[ddof, numeric\_only, engine, ...\]) | Calculate the expanding standard deviation. |
| [`Expanding.min`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.min.html#pandas.api.typing.Expanding.min "pandas.api.typing.Expanding.min")<br>(\[numeric\_only, engine, ...\]) | Calculate the expanding minimum. |
| [`Expanding.max`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.max.html#pandas.api.typing.Expanding.max "pandas.api.typing.Expanding.max")<br>(\[numeric\_only, engine, ...\]) | Calculate the expanding maximum. |
| [`Expanding.first`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.first.html#pandas.api.typing.Expanding.first "pandas.api.typing.Expanding.first")<br>(\[numeric\_only\]) | Calculate the expanding First (left-most) element of the window. |
| [`Expanding.last`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.last.html#pandas.api.typing.Expanding.last "pandas.api.typing.Expanding.last")<br>(\[numeric\_only\]) | Calculate the expanding Last (right-most) element of the window. |
| [`Expanding.corr`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.corr.html#pandas.api.typing.Expanding.corr "pandas.api.typing.Expanding.corr")<br>(\[other, pairwise, ddof, ...\]) | Calculate the expanding correlation. |
| [`Expanding.cov`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.cov.html#pandas.api.typing.Expanding.cov "pandas.api.typing.Expanding.cov")<br>(\[other, pairwise, ddof, ...\]) | Calculate the expanding sample covariance. |
| [`Expanding.skew`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.skew.html#pandas.api.typing.Expanding.skew "pandas.api.typing.Expanding.skew")<br>(\[numeric\_only\]) | Calculate the expanding unbiased skewness. |
| [`Expanding.kurt`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.kurt.html#pandas.api.typing.Expanding.kurt "pandas.api.typing.Expanding.kurt")<br>(\[numeric\_only\]) | Calculate the expanding Fisher's definition of kurtosis without bias. |
| [`Expanding.apply`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.apply.html#pandas.api.typing.Expanding.apply "pandas.api.typing.Expanding.apply")<br>(func\[, raw, engine, ...\]) | Calculate the expanding custom aggregation function. |
| [`Expanding.pipe`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.pipe.html#pandas.api.typing.Expanding.pipe "pandas.api.typing.Expanding.pipe")<br>(func, \*args, \*\*kwargs) | Apply a `func` with arguments to this Expanding object and return its result. |
| [`Expanding.aggregate`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.aggregate.html#pandas.api.typing.Expanding.aggregate "pandas.api.typing.Expanding.aggregate")<br>(\[func\]) | Aggregate using one or more operations over the specified axis. |
| [`Expanding.quantile`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.quantile.html#pandas.api.typing.Expanding.quantile "pandas.api.typing.Expanding.quantile")<br>(q\[, interpolation, ...\]) | Calculate the expanding quantile. |
| [`Expanding.sem`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.sem.html#pandas.api.typing.Expanding.sem "pandas.api.typing.Expanding.sem")<br>(\[ddof, numeric\_only\]) | Calculate the expanding standard error of mean. |
| [`Expanding.rank`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.rank.html#pandas.api.typing.Expanding.rank "pandas.api.typing.Expanding.rank")<br>(\[method, ascending, pct, ...\]) | Calculate the expanding rank. |
| [`Expanding.nunique`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Expanding.nunique.html#pandas.api.typing.Expanding.nunique "pandas.api.typing.Expanding.nunique")<br>(\[numeric\_only\]) | Calculate the expanding nunique. |

Exponentially-weighted window functions[#](https://pandas.pydata.org/docs/reference/window.html#exponentially-weighted-window-functions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [`ExponentialMovingWindow.mean`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.mean.html#pandas.api.typing.ExponentialMovingWindow.mean "pandas.api.typing.ExponentialMovingWindow.mean")<br>(\[numeric\_only, ...\]) | Calculate the ewm (exponential weighted moment) mean. |
| [`ExponentialMovingWindow.sum`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.sum.html#pandas.api.typing.ExponentialMovingWindow.sum "pandas.api.typing.ExponentialMovingWindow.sum")<br>(\[numeric\_only, ...\]) | Calculate the ewm (exponential weighted moment) sum. |
| [`ExponentialMovingWindow.std`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.std.html#pandas.api.typing.ExponentialMovingWindow.std "pandas.api.typing.ExponentialMovingWindow.std")<br>(\[bias, numeric\_only\]) | Calculate the ewm (exponential weighted moment) standard deviation. |
| [`ExponentialMovingWindow.var`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.var.html#pandas.api.typing.ExponentialMovingWindow.var "pandas.api.typing.ExponentialMovingWindow.var")<br>(\[bias, numeric\_only\]) | Calculate the ewm (exponential weighted moment) variance. |
| [`ExponentialMovingWindow.corr`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.corr.html#pandas.api.typing.ExponentialMovingWindow.corr "pandas.api.typing.ExponentialMovingWindow.corr")<br>(\[other, ...\]) | Calculate the ewm (exponential weighted moment) sample correlation. |
| [`ExponentialMovingWindow.cov`](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.ExponentialMovingWindow.cov.html#pandas.api.typing.ExponentialMovingWindow.cov "pandas.api.typing.ExponentialMovingWindow.cov")<br>(\[other, ...\]) | Calculate the ewm (exponential weighted moment) sample covariance. |

Window indexer[#](https://pandas.pydata.org/docs/reference/window.html#window-indexer "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Base class for defining custom window boundaries.

|     |     |
| --- | --- |
| [`api.indexers.BaseIndexer`](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.BaseIndexer.html#pandas.api.indexers.BaseIndexer "pandas.api.indexers.BaseIndexer")<br>(\[index\_array, ...\]) | Base class for window bounds calculations. |
| [`api.indexers.FixedForwardWindowIndexer`](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.FixedForwardWindowIndexer.html#pandas.api.indexers.FixedForwardWindowIndexer "pandas.api.indexers.FixedForwardWindowIndexer")<br>(\[...\]) | Creates window boundaries for fixed-length windows that include the current row. |
| [`api.indexers.VariableOffsetWindowIndexer`](https://pandas.pydata.org/docs/reference/api/pandas.api.indexers.VariableOffsetWindowIndexer.html#pandas.api.indexers.VariableOffsetWindowIndexer "pandas.api.indexers.VariableOffsetWindowIndexer")<br>(\[...\]) | Calculate window boundaries based on a non-fixed offset such as a BusinessDay. |

On this page