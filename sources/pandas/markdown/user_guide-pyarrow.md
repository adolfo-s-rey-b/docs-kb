[Skip to main content](https://pandas.pydata.org/docs/user_guide/pyarrow.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/user_guide/pyarrow.html)
[3.1 (stable)](https://pandas.pydata.org/docs/user_guide/pyarrow.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/user_guide/pyarrow.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/pyarrow.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/user_guide/pyarrow.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/user_guide/pyarrow.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/pyarrow.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/user_guide/pyarrow.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/user_guide/pyarrow.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/user_guide/pyarrow.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/user_guide/pyarrow.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/pyarrow.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/user_guide/pyarrow.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

PyArrow Functionality[#](https://pandas.pydata.org/docs/user_guide/pyarrow.html#pyarrow-functionality "Link to this heading")

==============================================================================================================================

pandas can utilize [PyArrow](https://arrow.apache.org/docs/python/index.html)
 to extend functionality and improve the performance of various APIs. This includes:

*   More extensive [data types](https://arrow.apache.org/docs/python/api/datatypes.html)
     compared to NumPy
    
*   Missing data support (NA) for all data types
    
*   Performant IO reader integration
    
*   Facilitate interoperability with other dataframe libraries based on the Apache Arrow specification (e.g. polars, cuDF)
    

To use this functionality, please ensure you have [installed the minimum supported PyArrow version.](https://pandas.pydata.org/docs/getting_started/install.html#install-optional-dependencies)

Data Structure Integration[#](https://pandas.pydata.org/docs/user_guide/pyarrow.html#data-structure-integration "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

A [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
, [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
, or the columns of a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 can be directly backed by a [`pyarrow.ChunkedArray`](https://arrow.apache.org/docs/python/generated/pyarrow.ChunkedArray.html#pyarrow.ChunkedArray "(in Apache Arrow v26.0.1)")
 which is similar to a NumPy array. To construct these from the main pandas data structures, you can pass in a string of the type followed by `[pyarrow]`, e.g. `"int64[pyarrow]"` into the `dtype` parameter

In \[1\]: ser \= pd.Series(\[\-1.5, 0.2, None\], dtype\="float32\[pyarrow\]")

In \[2\]: ser
Out\[2\]: 
0    -1.5
1     0.2
2    <NA>
dtype: float\[pyarrow\]

In \[3\]: idx \= pd.Index(\[True, None\], dtype\="bool\[pyarrow\]")

In \[4\]: idx
Out\[4\]: Index(\[True, <NA>\], dtype='bool\[pyarrow\]')

In \[5\]: df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\], dtype\="uint64\[pyarrow\]")

In \[6\]: df
Out\[6\]: 
   0  1
0  1  2
1  3  4

Copy to clipboard

Note

The string alias `"string[pyarrow]"` maps to `pd.StringDtype("pyarrow")` which is not equivalent to specifying `dtype=pd.ArrowDtype(pa.string())`. Generally, operations on the data will behave similarly except `pd.StringDtype("pyarrow")` can return NumPy-backed nullable types while `pd.ArrowDtype(pa.string())` will return [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
.

In \[7\]: import pyarrow as pa

In \[8\]: data \= list("abc")

In \[9\]: ser\_sd \= pd.Series(data, dtype\="string\[pyarrow\]")

In \[10\]: ser\_ad \= pd.Series(data, dtype\=pd.ArrowDtype(pa.string()))

In \[11\]: ser\_ad.dtype \== ser\_sd.dtype
Out\[11\]: False

In \[12\]: ser\_sd.str.contains("a")
Out\[12\]: 
0     True
1    False
2    False
dtype: boolean

In \[13\]: ser\_ad.str.contains("a")
Out\[13\]: 
0     True
1    False
2    False
dtype: bool\[pyarrow\]

Copy to clipboard

For PyArrow types that accept parameters, you can pass in a PyArrow type with those parameters into [`ArrowDtype`](https://pandas.pydata.org/docs/reference/api/pandas.ArrowDtype.html#pandas.ArrowDtype "pandas.ArrowDtype")
 to use in the `dtype` parameter.

In \[14\]: import pyarrow as pa

In \[15\]: list\_str\_type \= pa.list\_(pa.string())

In \[16\]: ser \= pd.Series(\[\["hello"\], \["there"\]\], dtype\=pd.ArrowDtype(list\_str\_type))

In \[17\]: ser
Out\[17\]: 
0    \['hello'\]
1    \['there'\]
dtype: list<item: string>\[pyarrow\]

Copy to clipboard

In \[18\]: from datetime import time

In \[19\]: idx \= pd.Index(\[time(12, 30), None\], dtype\=pd.ArrowDtype(pa.time64("us")))

In \[20\]: idx
Out\[20\]: Index(\[12:30:00, <NA>\], dtype='time64\[us\]\[pyarrow\]')

Copy to clipboard

In \[21\]: from decimal import Decimal

In \[22\]: decimal\_type \= pd.ArrowDtype(pa.decimal128(3, scale\=2))

In \[23\]: data \= \[\[Decimal("3.19"), None\], \[None, Decimal("-1.23")\]\]

In \[24\]: df \= pd.DataFrame(data, dtype\=decimal\_type)

In \[25\]: df
Out\[25\]: 
      0      1
0  3.19   <NA>
1  <NA>  -1.23

Copy to clipboard

If you already have an [`pyarrow.Array`](https://arrow.apache.org/docs/python/generated/pyarrow.Array.html#pyarrow.Array "(in Apache Arrow v26.0.1)")
 or [`pyarrow.ChunkedArray`](https://arrow.apache.org/docs/python/generated/pyarrow.ChunkedArray.html#pyarrow.ChunkedArray "(in Apache Arrow v26.0.1)")
, you can pass it into [`arrays.ArrowExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.arrays.ArrowExtensionArray.html#pandas.arrays.ArrowExtensionArray "pandas.arrays.ArrowExtensionArray")
 to construct the associated [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
, [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 or [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 object.

In \[26\]: pa\_array \= pa.array(
   ....:    \[{"1": "2"}, {"10": "20"}, None\],
   ....:    type\=pa.map\_(pa.string(), pa.string()),
   ....: )
   ....: 

In \[27\]: ser \= pd.Series(pd.arrays.ArrowExtensionArray(pa\_array))

In \[28\]: ser
Out\[28\]: 
0      \[('1', '2')\]
1    \[('10', '20')\]
2              <NA>
dtype: map<string, string>\[pyarrow\]

Copy to clipboard

To retrieve a pyarrow [`pyarrow.ChunkedArray`](https://arrow.apache.org/docs/python/generated/pyarrow.ChunkedArray.html#pyarrow.ChunkedArray "(in Apache Arrow v26.0.1)")
 from a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 or [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
, you can call the pyarrow array constructor on the [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 or [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
.

In \[29\]: ser \= pd.Series(\[1, 2, None\], dtype\="uint8\[pyarrow\]")

In \[30\]: pa.array(ser)
Out\[30\]: 
<pyarrow.lib.UInt8Array object at 0x7fa1fd0caa40>
\[\
  1,\
  2,\
  null\
\]

In \[31\]: idx \= pd.Index(ser)

In \[32\]: pa.array(idx)
Out\[32\]: 
<pyarrow.lib.UInt8Array object at 0x7fa1fd23e8c0>
\[\
  1,\
  2,\
  null\
\]

Copy to clipboard

To convert a [`pyarrow.Table`](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html#pyarrow.Table "(in Apache Arrow v26.0.1)")
 to a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
, you can call the [`pyarrow.Table.to_pandas()`](https://arrow.apache.org/docs/python/generated/pyarrow.Table.html#pyarrow.Table.to_pandas "(in Apache Arrow v26.0.1)")
 method with `types_mapper=pd.ArrowDtype`.

In \[33\]: table \= pa.table(\[pa.array(\[1, 2, 3\], type\=pa.int64())\], names\=\["a"\])

In \[34\]: df \= table.to\_pandas(types\_mapper\=pd.ArrowDtype)

In \[35\]: df
Out\[35\]: 
   a
0  1
1  2
2  3

In \[36\]: df.dtypes
Out\[36\]: 
a    int64\[pyarrow\]
dtype: object

Copy to clipboard

Operations[#](https://pandas.pydata.org/docs/user_guide/pyarrow.html#operations "Link to this heading")

--------------------------------------------------------------------------------------------------------

PyArrow data structure integration is implemented through pandas’ [`ExtensionArray`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.ExtensionArray.html#pandas.api.extensions.ExtensionArray "pandas.api.extensions.ExtensionArray")
 [interface](https://pandas.pydata.org/docs/development/extending.html#extending-extension-types)
; therefore, supported functionality exists where this interface is integrated within the pandas API. Additionally, this functionality is accelerated with PyArrow [compute functions](https://arrow.apache.org/docs/python/api/compute.html)
 where available. This includes:

*   Numeric aggregations
    
*   Numeric arithmetic
    
*   Numeric rounding
    
*   Logical and comparison functions
    
*   String functionality
    
*   Datetime functionality
    

The following are just some examples of operations that are accelerated by native PyArrow compute functions.

In \[37\]: import pyarrow as pa

In \[38\]: ser \= pd.Series(\[\-1.545, 0.211, None\], dtype\="float32\[pyarrow\]")

In \[39\]: ser.mean()
Out\[39\]: \-0.6669999808073044

In \[40\]: ser + ser
Out\[40\]: 
0    -3.09
1    0.422
2     <NA>
dtype: float\[pyarrow\]

In \[41\]: ser \> (ser + 1)
Out\[41\]: 
0    False
1    False
2     <NA>
dtype: bool\[pyarrow\]

In \[42\]: ser.dropna()
Out\[42\]: 
0   -1.545
1    0.211
dtype: float\[pyarrow\]

In \[43\]: ser.isna()
Out\[43\]: 
0    False
1    False
2     True
dtype: bool

In \[44\]: ser.fillna(0)
Out\[44\]: 
0   -1.545
1    0.211
2      0.0
dtype: float\[pyarrow\]

Copy to clipboard

In \[45\]: ser\_str \= pd.Series(\["a", "b", None\], dtype\=pd.ArrowDtype(pa.string()))

In \[46\]: ser\_str.str.startswith("a")
Out\[46\]: 
0     True
1    False
2     <NA>
dtype: bool\[pyarrow\]

Copy to clipboard

In \[47\]: from datetime import datetime

In \[48\]: pa\_type \= pd.ArrowDtype(pa.timestamp("ns"))

In \[49\]: ser\_dt \= pd.Series(\[datetime(2022, 1, 1), None\], dtype\=pa\_type)

In \[50\]: ser\_dt.dt.strftime("%Y-%m")
Out\[50\]: 
0    2022-01
1       <NA>
dtype: string\[pyarrow\]

Copy to clipboard

I/O Reading[#](https://pandas.pydata.org/docs/user_guide/pyarrow.html#i-o-reading "Link to this heading")

----------------------------------------------------------------------------------------------------------

PyArrow also provides IO reading functionality that has been integrated into several pandas IO readers. The following functions provide an `engine` keyword that can dispatch to PyArrow to accelerate reading from an IO source.

*   [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")
    
*   [`read_feather()`](https://pandas.pydata.org/docs/reference/api/pandas.read_feather.html#pandas.read_feather "pandas.read_feather")
    
*   [`read_json()`](https://pandas.pydata.org/docs/reference/api/pandas.read_json.html#pandas.read_json "pandas.read_json")
    
*   [`read_orc()`](https://pandas.pydata.org/docs/reference/api/pandas.read_orc.html#pandas.read_orc "pandas.read_orc")
    
*   [`read_parquet()`](https://pandas.pydata.org/docs/reference/api/pandas.read_parquet.html#pandas.read_parquet "pandas.read_parquet")
    
*   [`read_table()`](https://pandas.pydata.org/docs/reference/api/pandas.read_table.html#pandas.read_table "pandas.read_table")
     (experimental)
    

In \[51\]: import io

In \[52\]: data \= io.StringIO("""a,b,c
   ....:   1,2.5,True
   ....:   3,4.5,False
   ....: """)
   ....: 

In \[53\]: df \= pd.read\_csv(data, engine\="pyarrow")

In \[54\]: df
Out\[54\]: 
   a    b      c
0  1  2.5   True
1  3  4.5  False

Copy to clipboard

By default, these functions and all other IO reader functions return NumPy-backed data. These readers can return PyArrow-backed data by specifying the parameter `dtype_backend="pyarrow"`. A reader does not need to set `engine="pyarrow"` to necessarily return PyArrow-backed data.

In \[55\]: import io

In \[56\]: data \= io.StringIO("""a,b,c,d,e,f,g,h,i
   ....:    1,2.5,True,a,,,,,
   ....:    3,4.5,False,b,6,7.5,True,a,
   ....: """)
   ....: 

In \[57\]: df\_pyarrow \= pd.read\_csv(data, dtype\_backend\="pyarrow")

In \[58\]: df\_pyarrow.dtypes
Out\[58\]: 
a     int64\[pyarrow\]
b    double\[pyarrow\]
c      bool\[pyarrow\]
d    string\[pyarrow\]
e     int64\[pyarrow\]
f    double\[pyarrow\]
g      bool\[pyarrow\]
h    string\[pyarrow\]
i      null\[pyarrow\]
dtype: object

Copy to clipboard

Several non-IO reader functions can also use the `dtype_backend` argument to return PyArrow-backed data including:

*   [`to_numeric()`](https://pandas.pydata.org/docs/reference/api/pandas.to_numeric.html#pandas.to_numeric "pandas.to_numeric")
    
*   [`DataFrame.convert_dtypes()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.convert_dtypes.html#pandas.DataFrame.convert_dtypes "pandas.DataFrame.convert_dtypes")
    
*   [`Series.convert_dtypes()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.convert_dtypes.html#pandas.Series.convert_dtypes "pandas.Series.convert_dtypes")
    

On this page