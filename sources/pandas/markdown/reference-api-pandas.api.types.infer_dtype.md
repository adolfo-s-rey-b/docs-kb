[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.types.infer_dtype.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.types.infer_dtype.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.types.infer_dtype.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.types.infer_dtype.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.types.infer_dtype.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.types.infer_dtype.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.types.infer_dtype.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.types.infer_dtype.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.types.infer_dtype.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.types.infer_dtype.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.types.infer_dtype.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.types.infer_dtype.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.types.infer_dtype.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.types.infer_dtype.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.types.infer\_dtype[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.infer_dtype.html#pandas-api-types-infer-dtype "Link to this heading")

=====================================================================================================================================================================

pandas.api.types.infer\_dtype(_value_, _skipna\=True_)[#](https://pandas.pydata.org/docs/reference/api/pandas.api.types.infer_dtype.html#pandas.api.types.infer_dtype "Link to this definition")

Return a string label of the type of the elements in a list-like input.

This method inspects the elements of the provided input and determines classification of its data type. It is particularly useful for handling heterogeneous data inputs where explicit dtype conversion may not be possible or necessary.

Parameters:

**value**list, ndarray, or pandas type

The input data to infer the dtype.

**skipna**bool, default True

Ignore NaN values when inferring the type.

Returns:

str

Describing the common type of the input data.

Results can include:

*   string
    
*   bytes
    
*   floating
    
*   integer
    
*   integer-na
    
*   mixed-integer
    
*   mixed-integer-float
    
*   decimal
    
*   complex
    
*   categorical
    
*   boolean
    
*   datetime64
    
*   datetime
    
*   date
    
*   timedelta64
    
*   timedelta
    
*   time
    
*   period
    
*   interval
    
*   mixed
    
*   empty
    
*   unknown-array
    

Raises:

TypeError

If ndarray-like but cannot infer the dtype

See also

`api.types.is_scalar`

Check if the input is a scalar.

`api.types.is_list_like`

Check if the input is list-like.

`api.types.is_integer`

Check if the input is an integer.

`api.types.is_float`

Check if the input is a float.

`api.types.is_bool`

Check if the input is a boolean.

Notes

*   ‘mixed’ is the catchall for anything that is not otherwise specialized
    
*   ‘mixed-integer-float’ are floats and integers
    
*   ‘mixed-integer’ are integers mixed with non-integers
    
*   ‘integer-na’ are integers mixed with NaN, returned only when skipna=False
    
*   ‘empty’ is returned for inputs with no inferable values (e.g. an empty input, or all-NA with skipna=True)
    
*   ‘unknown-array’ is the catchall for something that _is_ an array (has a dtype attribute), but has a dtype unknown to pandas (e.g. external extension array)
    

Examples

\>>> from pandas.api.types import infer\_dtype
\>>> infer\_dtype(\['foo', 'bar'\])
'string'

Copy to clipboard

\>>> infer\_dtype(\['a', np.nan, 'b'\], skipna\=True)
'string'

Copy to clipboard

\>>> infer\_dtype(\['a', np.nan, 'b'\], skipna\=False)
'mixed'

Copy to clipboard

\>>> infer\_dtype(\[b'foo', b'bar'\])
'bytes'

Copy to clipboard

\>>> infer\_dtype(\[1, 2, 3\])
'integer'

Copy to clipboard

\>>> infer\_dtype(\[1, 2, 3.5\])
'mixed-integer-float'

Copy to clipboard

\>>> infer\_dtype(\[1.0, 2.0, 3.5\])
'floating'

Copy to clipboard

\>>> infer\_dtype(\['a', 1\])
'mixed-integer'

Copy to clipboard

\>>> from decimal import Decimal
\>>> infer\_dtype(\[Decimal(1), Decimal(2.0)\])
'decimal'

Copy to clipboard

\>>> infer\_dtype(\[True, False\])
'boolean'

Copy to clipboard

\>>> infer\_dtype(\[True, False, np.nan\])
'boolean'

Copy to clipboard

\>>> infer\_dtype(\[pd.Timestamp('20130101')\])
'datetime'

Copy to clipboard

\>>> import datetime
\>>> infer\_dtype(\[datetime.date(2013, 1, 1)\])
'date'

Copy to clipboard

\>>> infer\_dtype(\[np.datetime64('2013-01-01')\])
'datetime64'

Copy to clipboard

\>>> infer\_dtype(\[datetime.timedelta(0, 1, 1)\])
'timedelta'

Copy to clipboard

\>>> infer\_dtype(pd.Series(list('aabc')).astype('category'))
'categorical'

Copy to clipboard

On this page