[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.Series.map.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.Series.map.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.Series.map.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.Series.map.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.Series.map.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.Series.map.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.Series.map.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.Series.map.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.Series.map.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.Series.map.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.Series.map.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.Series.map.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.Series.map[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas-series-map "Link to this heading")

===================================================================================================================================

Series.map(_func\=None_, _na\_action\=None_, _engine\=None_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/series.py#L5018-L5190)
[#](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map "Link to this definition")

Map values of Series according to an input mapping or function.

Used for substituting each value in a Series with another value, that may be derived from a function, a `dict` or a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
.

Parameters:

**func**function, collections.abc.Mapping subclass or Series

Function or mapping correspondence.

**na\_action**{None, ‘ignore’}, default None

If ‘ignore’, propagate NaN values, without passing them to the mapping correspondence.

**engine**decorator, optional

Choose the execution engine to use to run the function. Only used for functions. If `map` is called with a mapping or `Series`, an exception will be raised. If `engine` is not provided the function will be executed by the regular Python interpreter.

Options include JIT compilers such as Numba, Bodo or Blosc2, which in some cases can speed up the execution. To use an executor you can provide the decorators `numba.jit`, `numba.njit`, `bodo.jit` or `blosc2.jit`. You can also provide the decorator with parameters, like `numba.jit(nogil=True)`.

Not all functions can be executed with all execution engines. In general, JIT compilers will require type stability in the function (no variable should change data type during the execution). And not all pandas and NumPy APIs are supported. Check the engine documentation for limitations.

Added in version 3.0.0.

**\*\*kwargs**

Additional keyword arguments to pass as keywords arguments to `func`.

Added in version 3.0.0.

Returns:

Series

Same index as caller.

See also

[`Series.apply`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#pandas.Series.apply "pandas.Series.apply")

For applying more complex functions on a Series.

[`Series.replace`](https://pandas.pydata.org/docs/reference/api/pandas.Series.replace.html#pandas.Series.replace "pandas.Series.replace")

Replace values given in to\_replace with value.

[`DataFrame.apply`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")

Apply a function row-/column-wise.

[`DataFrame.map`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas.DataFrame.map "pandas.DataFrame.map")

Apply a function elementwise on a whole DataFrame.

Notes

When `func` is a dictionary, values in Series that are not in the dictionary (as keys) are converted to `NaN`. However, if the dictionary is a `dict` subclass that defines `__missing__` (i.e. provides a method for default values), then this default is used rather than `NaN`.

Examples

\>>> s \= pd.Series(\["cat", "dog", np.nan, "rabbit"\])
\>>> s
0      cat
1      dog
2      NaN
3   rabbit
dtype: str

Copy to clipboard

`map` accepts a `dict` or a `Series`. Values that are not found in the `dict` are converted to `NaN`, unless the dict has a default value (e.g. `defaultdict`):

\>>> s.map({"cat": "kitten", "dog": "puppy"})
0   kitten
1    puppy
2      NaN
3      NaN
dtype: str

Copy to clipboard

It also accepts a function:

\>>> s.map("I am a {}".format)
0       I am a cat
1       I am a dog
2       I am a nan
3    I am a rabbit
dtype: str

Copy to clipboard

To avoid applying the function to missing values (and keep them as `NaN`) `na_action='ignore'` can be used:

\>>> s.map("I am a {}".format, na\_action\="ignore")
0     I am a cat
1     I am a dog
2            NaN
3  I am a rabbit
dtype: str

Copy to clipboard

For categorical data, the function is only applied to the categories:

\>>> s \= pd.Series(list("cabaa"))
\>>> s.map(print)
c
a
b
a
a
0    None
1    None
2    None
3    None
4    None
dtype: object

Copy to clipboard

\>>> s\_cat \= s.astype("category")
\>>> s\_cat.map(print)  \# function called once per unique category
a
b
c
0    None
1    None
2    None
3    None
4    None
dtype: object

Copy to clipboard

On this page