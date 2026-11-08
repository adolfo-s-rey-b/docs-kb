[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xarray.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.DataFrame.to_xarray.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xarray.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.DataFrame.to_xarray.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.DataFrame.to_xarray.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.DataFrame.to_xarray.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.DataFrame.to_xarray.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.DataFrame.to_xarray.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.DataFrame.to_xarray.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.DataFrame.to_xarray.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.DataFrame.to_xarray.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.DataFrame.to_xarray.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.DataFrame.to_xarray.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.DataFrame.to_xarray.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.DataFrame.to\_xarray[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xarray.html#pandas-dataframe-to-xarray "Link to this heading")

===============================================================================================================================================================

DataFrame.to\_xarray()[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/generic.py#L3261-L3353)
[#](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_xarray.html#pandas.DataFrame.to_xarray "Link to this definition")

Return an xarray object from the pandas object.

This method converts a pandas object to an xarray object, which is useful for working with labeled multi-dimensional data.

Returns:

xarray.DataArray or xarray.Dataset

Data in the pandas structure converted to Dataset if the object is a DataFrame, or a DataArray if the object is a Series.

See also

[`DataFrame.to_hdf`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_hdf.html#pandas.DataFrame.to_hdf "pandas.DataFrame.to_hdf")

Write DataFrame to an HDF5 file.

[`DataFrame.to_parquet`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_parquet.html#pandas.DataFrame.to_parquet "pandas.DataFrame.to_parquet")

Write a DataFrame to the binary parquet format.

Notes

See the [xarray docs](https://xarray.pydata.org/en/stable/)

Examples

\>>> df \= pd.DataFrame(
...     \[\
...         ("falcon", "bird", 389.0, 2),\
...         ("parrot", "bird", 24.0, 2),\
...         ("lion", "mammal", 80.5, 4),\
...         ("monkey", "mammal", np.nan, 4),\
...     \],
...     columns\=\["name", "class", "max\_speed", "num\_legs"\],
... )
\>>> df
     name   class  max\_speed  num\_legs
0  falcon    bird      389.0         2
1  parrot    bird       24.0         2
2    lion  mammal       80.5         4
3  monkey  mammal        NaN         4

Copy to clipboard

\>>> df.to\_xarray()
<xarray.Dataset>
Dimensions:    (index: 4)
Coordinates:
  \* index      (index) int64 32B 0 1 2 3
Data variables:
    name       (index) object 32B 'falcon' 'parrot' 'lion' 'monkey'
    class      (index) object 32B 'bird' 'bird' 'mammal' 'mammal'
    max\_speed  (index) float64 32B 389.0 24.0 80.5 nan
    num\_legs   (index) int64 32B 2 2 4 4

Copy to clipboard

\>>> df\["max\_speed"\].to\_xarray()
<xarray.DataArray 'max\_speed' (index: 4)>
array(\[389. ,  24. ,  80.5,   nan\])
Coordinates:
  \* index    (index) int64 0 1 2 3

Copy to clipboard

\>>> dates \= pd.to\_datetime(
...     \["2018-01-01", "2018-01-01", "2018-01-02", "2018-01-02"\]
... )
\>>> df\_multiindex \= pd.DataFrame(
...     {
...         "date": dates,
...         "animal": \["falcon", "parrot", "falcon", "parrot"\],
...         "speed": \[350, 18, 361, 15\],
...     }
... )
\>>> df\_multiindex \= df\_multiindex.set\_index(\["date", "animal"\])

Copy to clipboard

\>>> df\_multiindex
                   speed
date       animal
2018-01-01 falcon    350
           parrot     18
2018-01-02 falcon    361
           parrot     15

Copy to clipboard

\>>> df\_multiindex.to\_xarray()
<xarray.Dataset>
Dimensions:  (date: 2, animal: 2)
Coordinates:
  \* date     (date) datetime64\[s\] 2018-01-01 2018-01-02
  \* animal   (animal) object 'falcon' 'parrot'
Data variables:
    speed    (date, animal) int64 350 18 361 15

Copy to clipboard

On this page