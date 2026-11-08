[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_index_accessor.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.api.extensions.register_index_accessor.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_index_accessor.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.api.extensions.register_index_accessor.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.api.extensions.register_index_accessor.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.api.extensions.register_index_accessor.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.api.extensions.register_index_accessor.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.api.extensions.register_index_accessor.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.api.extensions.register_index_accessor.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.api.extensions.register_index_accessor.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.api.extensions.register_index_accessor.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.api.extensions.register_index_accessor.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.api.extensions.register_index_accessor.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.api.extensions.register_index_accessor.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.api.extensions.register\_index\_accessor[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_index_accessor.html#pandas-api-extensions-register-index-accessor "Link to this heading")

=========================================================================================================================================================================================================================

pandas.api.extensions.register\_index\_accessor(_name_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/accessor.py#L457-L530)
[#](https://pandas.pydata.org/docs/reference/api/pandas.api.extensions.register_index_accessor.html#pandas.api.extensions.register_index_accessor "Link to this definition")

Register a custom accessor on Index objects.

Use as a decorator to add a custom namespace accessor to Index, allowing domain-specific methods to be called via `idx.<name>`.

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

This function allows you to register a custom-defined accessor class for Index. The requirements for the accessor class are as follows:

*   Must contain an init method that:
    
    *   accepts a single Index object
        
    *   raises an AttributeError if the Index object does not have correctly matching inputs for the accessor
        
*   Must contain a method for each access pattern.
    
    *   The methods should be able to take any argument signature.
        
    *   Accessible using the @property decorator if no additional arguments are needed.
        

Examples

An accessor that only accepts integers could have a class defined like this:

\>>> @pd.api.extensions.register\_index\_accessor("int\_accessor")
... class IntAccessor:
...     def \_\_init\_\_(self, pandas\_obj):
...         if not all(isinstance(x, int) for x in pandas\_obj):
...             raise AttributeError("The index must only be an integer value")
...         self.\_obj \= pandas\_obj
...
...     def even(self):
...         return \[x for x in self.\_obj if x % 2 \== 0\]
\>>> df \= pd.DataFrame.from\_dict(
...     {"row1": {"1": 1, "2": "a"}, "row2": {"1": 2, "2": "b"}}, orient\="index"
... )
\>>> df.index.int\_accessor
Traceback (most recent call last):
...
AttributeError: The index must only be an integer value.
\>>> df \= pd.DataFrame(
...     {"col1": \[1, 2, 3, 4\], "col2": \["a", "b", "c", "d"\]}, index\=\[1, 2, 5, 8\]
... )
\>>> df.index.int\_accessor.even()
\[2, 8\]

Copy to clipboard

On this page