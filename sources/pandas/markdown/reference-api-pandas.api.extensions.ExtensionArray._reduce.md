[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._reduce.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.ExtensionArray._reduce.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.ExtensionArray.\_reduce[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._reduce.html#pandas-api-extensions-extensionarray-reduce "Link to this heading")

====================================================================================================================================================================================================================

ExtensionArray.\_reduce(_name_, _\*_, _skipna\=True_, _keepdims\=False_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/arrays/base.py#L2414-L2494)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray._reduce.html#pandas.api.extensions.ExtensionArray._reduce "Link to this definition")

Return a scalar result of performing the reduction operation.

This method dispatches to the appropriate reduction method (e.g., sum, mean, min, max) based on the name parameter and returns the result.

Parameters:

**name**str

Name of the function, supported values are: { any, all, min, max, sum, mean, median, prod, std, var, sem, kurt, skew }.

**skipna**bool, default True

If True, skip NaN values.

**keepdims**bool, default False

If False, a scalar is returned. If True, the result has dimension with size one along the reduced axis.

**\*\*kwargs**

Additional keyword arguments passed to the reduction function. Currently, ddof is the only supported kwarg.

Returns:

scalar or ndarray:

The result of the reduction operation. The type of the result depends on keepdims: - If keepdims is False, a scalar value is returned. - If keepdims is True, the result is wrapped in a numpy array with a single element.

Raises:

**TypeError**subclass does not define operations

See also

`Series.min`

Return the minimum value.

`Series.max`

Return the maximum value.

`Series.sum`

Return the sum of values.

`Series.mean`

Return the mean of values.

`Series.median`

Return the median of values.

`Series.std`

Return the standard deviation.

`Series.var`

Return the variance.

`Series.prod`

Return the product of values.

`Series.sem`

Return the standard error of the mean.

`Series.kurt`

Return the kurtosis.

`Series.skew`

Return the skewness.

Examples

\>>> pd.array(\[1, 2, 3\]).\_reduce("min")
np.int64(1)
\>>> pd.array(\[1, 2, 3\]).\_reduce("max")
np.int64(3)
\>>> pd.array(\[1, 2, 3\]).\_reduce("sum")
np.int64(6)
\>>> pd.array(\[1, 2, 3\]).\_reduce("mean")
np.float64(2.0)
\>>> pd.array(\[1, 2, 3\]).\_reduce("median")
np.float64(2.0)

Copy to clipboard

On this page