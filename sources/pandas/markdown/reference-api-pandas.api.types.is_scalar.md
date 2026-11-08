[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_scalar.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.is_scalar.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_scalar.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.is_scalar.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.is_scalar.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.is_scalar.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.is_scalar.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.is_scalar.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.is_scalar.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.is_scalar.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.is_scalar.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.is_scalar.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.is_scalar.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.is_scalar.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.is\_scalar[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_scalar.html#pandas-api-types-is-scalar "Link to this heading")

===============================================================================================================================================================

pandas.api.types.is\_scalar(_val_)[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.is_scalar.html#pandas.api.types.is_scalar "Link to this definition")

Return True if given object is scalar.

This function determines whether a given Python object is a scalar value rather than a collection. Scalars include numeric types, strings, bytes, dates, timedeltas, intervals, periods, and `None`.

Parameters:

**val**object

This includes:

*   numpy array scalar (e.g. np.int64)
    
*   Python builtin numerics
    
*   Python builtin byte arrays and strings
    
*   None
    
*   datetime.datetime
    
*   datetime.timedelta
    
*   Period
    
*   decimal.Decimal
    
*   Interval
    
*   DateOffset
    
*   Fraction
    
*   Number.
    

Returns:

bool

Return True if given object is scalar.

See also

`api.types.is_list_like`

Check if the input is list-like.

`api.types.is_integer`

Check if the input is an integer.

`api.types.is_float`

Check if the input is a float.

`api.types.is_bool`

Check if the input is a boolean.

Examples

\>>> import datetime
\>>> dt \= datetime.datetime(2018, 10, 3)
\>>> pd.api.types.is\_scalar(dt)
True

Copy to clipboard

\>>> pd.api.types.is\_scalar(\[2, 3\])
False

Copy to clipboard

\>>> pd.api.types.is\_scalar({0: 1, 2: 3})
False

Copy to clipboard

\>>> pd.api.types.is\_scalar((0, 2))
False

Copy to clipboard

pandas supports PEP 3141 numbers:

\>>> from fractions import Fraction
\>>> pd.api.types.is\_scalar(Fraction(3, 5))
True

Copy to clipboard

On this page