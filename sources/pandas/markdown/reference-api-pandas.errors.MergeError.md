[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.errors.MergeError.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.errors.MergeError.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.errors.MergeError.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.errors.MergeError.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.errors.MergeError.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.errors.MergeError.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.errors.MergeError.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.errors.MergeError.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.errors.MergeError.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.errors.MergeError.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.errors.MergeError.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.errors.MergeError.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.errors.MergeError.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.errors.MergeError.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.errors.MergeError[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.MergeError.html#pandas-errors-mergeerror "Link to this heading")

========================================================================================================================================================

exception pandas.errors.MergeError[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/errors/__init__.py#L456-L484)
[#](https://pandas.pydata.org/docs/reference/api/pandas.errors.MergeError.html#pandas.errors.MergeError "Link to this definition")

Exception raised when merging data.

Subclass of `ValueError`.

See also

`DataFrame.join`

For joining DataFrames on their indexes.

`merge`

For merging two DataFrames on a common set of keys.

Examples

\>>> left \= pd.DataFrame(
...     {"a": \["a", "b", "b", "d"\], "b": \["cat", "dog", "weasel", "horse"\]},
...     index\=range(4),
... )
\>>> right \= pd.DataFrame(
...     {"a": \["a", "b", "c", "d"\], "c": \["meow", "bark", "chirp", "nay"\]},
...     index\=range(4),
... ).set\_index("a")
\>>> left.join(
...     right,
...     on\="a",
...     validate\="one\_to\_one",
... )
Traceback (most recent call last):
MergeError: Merge keys are not unique in left dataset; not a one-to-one merge

Copy to clipboard

On this page