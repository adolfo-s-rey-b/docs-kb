[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_dataframe_accessor.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.register_dataframe_accessor.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.register_dataframe_accessor.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.register\_dataframe\_accessor[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_dataframe_accessor.html#pandas-api-extensions-register-dataframe-accessor "Link to this heading")

=====================================================================================================================================================================================================================================

pandas.api.extensions.register\_dataframe\_accessor(_name_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L309-L382)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_dataframe_accessor.html#pandas.api.extensions.register_dataframe_accessor "Link to this definition")

Register a custom accessor on DataFrame objects.

Use as a decorator to add a custom namespace accessor to DataFrame, allowing domain-specific methods to be called via `df.<name>`.

Parameters:

**name**str

Name under which the accessor should be registered. A warning is issued if this name conflicts with a preexisting attribute.

Returns:

callable

A class decorator.

See also

[`register_dataframe_accessor`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_dataframe_accessor.html#pandas.api.extensions.register_dataframe_accessor "pandas.api.extensions.register_dataframe_accessor")

Register a custom accessor on DataFrame objects.

[`register_series_accessor`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_series_accessor.html#pandas.api.extensions.register_series_accessor "pandas.api.extensions.register_series_accessor")

Register a custom accessor on Series objects.

[`register_index_accessor`](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_index_accessor.html#pandas.api.extensions.register_index_accessor "pandas.api.extensions.register_index_accessor")

Register a custom accessor on Index objects.

Notes

This function allows you to register a custom-defined accessor class for DataFrame. The requirements for the accessor class are as follows:

*   Must contain an init method that:
    
    *   accepts a single DataFrame object
        
    *   raises an AttributeError if the DataFrame object does not have correctly matching inputs for the accessor
        
*   Must contain a method for each access pattern.
    
    *   The methods should be able to take any argument signature.
        
    *   Accessible using the @property decorator if no additional arguments are needed.
        

Examples

An accessor that only accepts integers could have a class defined like this:

\>>> @pd.api.extensions.register\_dataframe\_accessor("int\_accessor")
... class IntAccessor:
...     def \_\_init\_\_(self, pandas\_obj):
...         if not all(
...             pandas\_obj\[col\].dtype \== "int64" for col in pandas\_obj.columns
...         ):
...             raise AttributeError("All columns must contain integer values only")
...         self.\_obj \= pandas\_obj
...
...     def sum(self):
...         return self.\_obj.sum()
\>>> df \= pd.DataFrame(\[\[1, 2\], \["x", "y"\]\])
\>>> df.int\_accessor
Traceback (most recent call last):
...
AttributeError: All columns must contain integer values only.
\>>> df \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\])
\>>> df.int\_accessor.sum()
0    4
1    6
dtype: int64

Copy to clipboard

On this page