[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.pipe.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.io.formats.style.Styler.pipe.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.pipe.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.io.formats.style.Styler.pipe.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.io.formats.style.Styler.pipe.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.io.formats.style.Styler.pipe.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.io.formats.style.Styler.pipe.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.io.formats.style.Styler.pipe.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.io.formats.style.Styler.pipe.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.io.formats.style.Styler.pipe.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.io.formats.style.Styler.pipe.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.io.formats.style.Styler.pipe.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.io.formats.style.Styler.pipe.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.io.formats.style.Styler.pipe.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.io.formats.style.Styler.pipe[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.pipe.html#pandas-io-formats-style-styler-pipe "Link to this heading")

=========================================================================================================================================================================================

Styler.pipe(_func_, _\*args_, _\*\*kwargs_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/io/formats/style.py#L4085-L4209)
[#](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.pipe.html#pandas.io.formats.style.Styler.pipe "Link to this definition")

Apply `func(self, *args, **kwargs)`, and return the result.

This is useful for chaining multiple user-defined styling operations in a readable manner, rather than nesting function calls.

Parameters:

**func**function

Function to apply to the Styler. Alternatively, a `(callable, keyword)` tuple where `keyword` is a string indicating the keyword of `callable` that expects the Styler.

**\*args**optional

Arguments passed to func.

**\*\*kwargs**optional

A dictionary of keyword arguments passed into `func`.

Returns:

object

The value returned by `func`.

See also

`DataFrame.pipe`

Analogous method for DataFrame.

[`Styler.apply`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html#pandas.io.formats.style.Styler.apply "pandas.io.formats.style.Styler.apply")

Apply a CSS-styling function column-wise, row-wise, or table-wise.

Notes

Like `DataFrame.pipe()`, this method can simplify the application of several user-defined functions to a styler. Instead of writing:

f(g(df.style.format(precision\=3), arg1\=a), arg2\=b, arg3\=c)

Copy to clipboard

users can write:

(df.style.format(precision\=3).pipe(g, arg1\=a).pipe(f, arg2\=b, arg3\=c))

Copy to clipboard

In particular, this allows users to define functions that take a styler object, along with other parameters, and return the styler after making styling changes (such as calling [`Styler.apply()`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html#pandas.io.formats.style.Styler.apply "pandas.io.formats.style.Styler.apply")
 or [`Styler.set_properties()`](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_properties.html#pandas.io.formats.style.Styler.set_properties "pandas.io.formats.style.Styler.set_properties")
).

Examples

**Common Use**

A common usage pattern is to pre-define styling operations which can be easily applied to a generic styler in a single `pipe` call.

\>>> def some\_highlights(styler, min\_color\="red", max\_color\="blue"):
...     styler.highlight\_min(color\=min\_color, axis\=None)
...     styler.highlight\_max(color\=max\_color, axis\=None)
...     styler.highlight\_null()
...     return styler
\>>> df \= pd.DataFrame(\[\[1, 2, 3, pd.NA\], \[pd.NA, 4, 5, 6\]\], dtype\="Int64")
\>>> df.style.pipe(some\_highlights, min\_color\="green")

Copy to clipboard

![../../_images/df_pipe_hl.png](https://pandas.pydata.org/docs/_images/df_pipe_hl.png)

Since the method returns a `Styler` object it can be chained with other methods as if applying the underlying highlighters directly.

\>>> (
...     df.style.format("{:.1f}")
...     .pipe(some\_highlights, min\_color\="green")
...     .highlight\_between(left\=2, right\=5)
... )

Copy to clipboard

![../../_images/df_pipe_hl2.png](https://pandas.pydata.org/docs/_images/df_pipe_hl2.png)

**Advanced Use**

Sometimes it may be necessary to pre-define styling functions, but in the case where those functions rely on the styler, data or context. Since `Styler.use` and `Styler.export` are designed to be non-data dependent, they cannot be used for this purpose. Additionally the `Styler.apply` and `Styler.format` type methods are not context aware, so a solution is to use `pipe` to dynamically wrap this functionality.

Suppose we want to code a generic styling function that highlights the final level of a MultiIndex. The number of levels in the Index is dynamic so we need the `Styler` context to define the level.

\>>> def highlight\_last\_level(styler):
...     return styler.apply\_index(
...         lambda v: "background-color: pink; color: yellow",
...         axis\="columns",
...         level\=styler.columns.nlevels \- 1,
...     )
\>>> df.columns \= pd.MultiIndex.from\_product(\[\["A", "B"\], \["X", "Y"\]\])
\>>> df.style.pipe(highlight\_last\_level)

Copy to clipboard

![../../_images/df_pipe_applymap.png](https://pandas.pydata.org/docs/_images/df_pipe_applymap.png)

Additionally suppose we want to highlight a column header if there is any missing data in that column. In this case we need the data object itself to determine the effect on the column headers.

\>>> def highlight\_header\_missing(styler, level):
...     def dynamic\_highlight(s):
...         return np.where(
...             styler.data.isna().any(), "background-color: red;", ""
...         )
...
...     return styler.apply\_index(dynamic\_highlight, axis\=1, level\=level)
\>>> df.style.pipe(highlight\_header\_missing, level\=1)

Copy to clipboard

![../../_images/df_pipe_applydata.png](https://pandas.pydata.org/docs/_images/df_pipe_applydata.png)

On this page