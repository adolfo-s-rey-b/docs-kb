[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.ChainedAssignmentError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.ChainedAssignmentError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.ChainedAssignmentError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.ChainedAssignmentError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.ChainedAssignmentError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.ChainedAssignmentError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.ChainedAssignmentError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.ChainedAssignmentError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.ChainedAssignmentError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.ChainedAssignmentError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.ChainedAssignmentError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.ChainedAssignmentError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.ChainedAssignmentError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.ChainedAssignmentError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.ChainedAssignmentError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.ChainedAssignmentError.html#pandas-errors-chainedassignmenterror "Link to this heading")

============================================================================================================================================================================================

exception pandas.errors.ChainedAssignmentError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L687-L711)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.ChainedAssignmentError.html#pandas.errors.ChainedAssignmentError "Link to this definition")

Warning raised when trying to set using chained assignment.

With Copy-on-Write now always enabled, chained assignment can never work. In such a situation, we are always setting into a temporary object that is the result of an indexing operation (getitem), which under Copy-on-Write always behaves as a copy. Thus, assigning through a chain can never update the original Series or DataFrame.

For more information on Copy-on-Write, see [the user guide](https://pandas.pydata.org/docs/user_guide/migration.html#copy-on-write)
.

See also

`DataFrame.loc`

Access a group of rows and columns by label(s) or a boolean array.

`DataFrame.iloc`

Purely integer-location based indexing for selection by position.

`Series.loc`

Access a group of rows by label(s) or a boolean array.

Examples

\>>> df \= pd.DataFrame({"A": \[1, 1, 1, 2, 2\]}, columns\=\["A"\])
\>>> df\["A"\]\[0:3\] \= 10
... \# ChainedAssignmentError: ...

Copy to clipboard

On this page