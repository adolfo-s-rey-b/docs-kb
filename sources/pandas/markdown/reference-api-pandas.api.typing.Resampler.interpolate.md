[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.interpolate.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.typing.Resampler.interpolate.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.interpolate.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.typing.Resampler.interpolate.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.typing.Resampler.interpolate.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.typing.Resampler.interpolate.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.typing.Resampler.interpolate.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.typing.Resampler.interpolate.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.typing.Resampler.interpolate.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.typing.Resampler.interpolate.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.typing.Resampler.interpolate.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.typing.Resampler.interpolate.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.typing.Resampler.interpolate.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.typing.Resampler.interpolate.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.typing.Resampler.interpolate[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.interpolate.html#pandas-api-typing-resampler-interpolate "Link to this heading")

=====================================================================================================================================================================================================

final Resampler.interpolate(_method\='linear'_, _\*_, _axis\=0_, _limit\=None_, _limit\_direction\='forward'_, _limit\_area\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/resample.py#L850-L1058)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.typing.Resampler.interpolate.html#pandas.api.typing.Resampler.interpolate "Link to this definition")

Interpolate values between target timestamps according to different methods.

The original index is first reindexed to target timestamps (see `core.resample.Resampler.asfreq()`), then the interpolation of `NaN` values via `DataFrame.interpolate()` happens.

Parameters:

**method**str, default ‘linear’

Interpolation technique to use. One of:

*   ‘linear’: Ignore the index and treat the values as equally spaced. This is the only method supported on MultiIndexes.
    
*   ‘time’: Works on daily and higher resolution data to interpolate given length of interval.
    
*   ‘index’, ‘values’: use the actual numerical values of the index.
    
*   ‘pad’: Fill in NaNs using existing values.
    
*   ‘nearest’, ‘zero’, ‘slinear’, ‘quadratic’, ‘cubic’, ‘barycentric’, ‘polynomial’: Passed to scipy.interpolate.interp1d, whereas ‘spline’ is passed to scipy.interpolate.UnivariateSpline. These methods use the numerical values of the index. Both ‘polynomial’ and ‘spline’ require that you also specify an order (int), e.g. `df.interpolate(method='polynomial', order=5)`. Note that, slinear method in Pandas refers to the Scipy first order spline instead of Pandas first order spline.
    
*   ‘krogh’, ‘piecewise\_polynomial’, ‘spline’, ‘pchip’, ‘akima’, ‘cubicspline’: Wrappers around the SciPy interpolation methods of similar names. See Notes.
    
*   ‘from\_derivatives’: Refers to scipy.interpolate.BPoly.from\_derivatives.
    

**axis**{0 or ‘index’, 1 or ‘columns’, None}, default None

Axis to interpolate along. For Series this parameter is unused and defaults to 0.

**limit**int, optional

Maximum number of consecutive NaNs to fill. In other words, if there is a gap with more than this number of consecutive NaNs, it will only be partially filled, from the direction given by `limit_direction`. Must be greater than 0.

**limit\_direction**{‘forward’, ‘backward’, ‘both’}, Optional

Consecutive NaNs will be filled in this direction.

**limit\_area**{None, ‘inside’, ‘outside’}, default None

Restrict which NaNs are filled based on their position relative to the valid values.

*   `None`: No fill restriction.
    
*   ‘inside’: Only fill NaNs surrounded by valid values (interpolate).
    
*   ‘outside’: Only fill NaNs outside valid values (extrapolate).
    

**\*\*kwargs**optional

Keyword arguments to pass on to the interpolating function.

Returns:

DataFrame or Series

Interpolated values at the specified freq.

See also

`core.resample.Resampler.asfreq`

Return the values at the new freq, essentially a reindex.

`DataFrame.interpolate`

Fill NaN values using an interpolation method.

`DataFrame.bfill`

Backward fill NaN values in the resampled data.

`DataFrame.ffill`

Forward fill NaN values.

Notes

For high-frequent or non-equidistant time-series with timestamps the reindexing followed by interpolation may lead to information loss as shown in the last example.

Examples

\>>> start \= "2023-03-01T07:00:00"
\>>> timesteps \= pd.date\_range(start, periods\=5, freq\="s")
\>>> series \= pd.Series(data\=\[1, \-1, 2, 1, 3\], index\=timesteps)
\>>> series
2023-03-01 07:00:00    1
2023-03-01 07:00:01   -1
2023-03-01 07:00:02    2
2023-03-01 07:00:03    1
2023-03-01 07:00:04    3
Freq: s, dtype: int64

Copy to clipboard

Downsample the dataframe to 0.5Hz by providing the period time of 2s.

\>>> series.resample("2s").interpolate("linear")
2023-03-01 07:00:00    1
2023-03-01 07:00:02    2
2023-03-01 07:00:04    3
Freq: 2s, dtype: int64

Copy to clipboard

Upsample the dataframe to 2Hz by providing the period time of 500ms.

\>>> series.resample("500ms").interpolate("linear")
2023-03-01 07:00:00.000    1.0
2023-03-01 07:00:00.500    0.0
2023-03-01 07:00:01.000   -1.0
2023-03-01 07:00:01.500    0.5
2023-03-01 07:00:02.000    2.0
2023-03-01 07:00:02.500    1.5
2023-03-01 07:00:03.000    1.0
2023-03-01 07:00:03.500    2.0
2023-03-01 07:00:04.000    3.0
Freq: 500ms, dtype: float64

Copy to clipboard

Internal reindexing with `asfreq()` prior to interpolation leads to an interpolated timeseries on the basis of the reindexed timestamps (anchors). It is assured that all available datapoints from original series become anchors, so it also works for resampling-cases that lead to non-aligned timestamps, as in the following example:

\>>> series.resample("400ms").interpolate("linear")
2023-03-01 07:00:00.000    1.000000
2023-03-01 07:00:00.400    0.333333
2023-03-01 07:00:00.800   -0.333333
2023-03-01 07:00:01.200    0.000000
2023-03-01 07:00:01.600    1.000000
2023-03-01 07:00:02.000    2.000000
2023-03-01 07:00:02.400    1.666667
2023-03-01 07:00:02.800    1.333333
2023-03-01 07:00:03.200    1.666667
2023-03-01 07:00:03.600    2.333333
2023-03-01 07:00:04.000    3.000000
Freq: 400ms, dtype: float64

Copy to clipboard

Note that the series correctly decreases between two anchors `07:00:00` and `07:00:02`.

On this page