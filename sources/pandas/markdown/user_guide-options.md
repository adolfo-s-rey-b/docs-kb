[Skip to main content](https://pandas.pydata.org/docs/user_guide/options.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/user_guide/options.html)
[3.1 (stable)](https://pandas.pydata.org/docs/user_guide/options.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/user_guide/options.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/options.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/user_guide/options.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/user_guide/options.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/options.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/user_guide/options.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/user_guide/options.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/user_guide/options.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/user_guide/options.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/options.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/user_guide/options.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Options and settings[#](https://pandas.pydata.org/docs/user_guide/options.html#options-and-settings "Link to this heading")

============================================================================================================================

Overview[#](https://pandas.pydata.org/docs/user_guide/options.html#overview "Link to this heading")

----------------------------------------------------------------------------------------------------

pandas has an options API to configure and customize global behavior related to [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 display, data behavior and more.

Options have a full “dotted-style”, case-insensitive name (e.g. `display.max_rows`). You can get/set options directly as attributes of the top-level `options` attribute:

In \[1\]: import pandas as pd

In \[2\]: pd.options.display.max\_rows
Out\[2\]: 15

In \[3\]: pd.options.display.max\_rows \= 999

In \[4\]: pd.options.display.max\_rows
Out\[4\]: 999

Copy to clipboard

The API is composed of 5 relevant functions, available directly from the `pandas` namespace:

*   [`get_option()`](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#pandas.get_option "pandas.get_option")
     / [`set_option()`](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas.set_option "pandas.set_option")
     - get/set the value of a single option.
    
*   [`reset_option()`](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#pandas.reset_option "pandas.reset_option")
     - reset one or more options to their default value.
    
*   [`describe_option()`](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#pandas.describe_option "pandas.describe_option")
     - print the descriptions of one or more options.
    
*   [`option_context()`](https://pandas.pydata.org/docs/reference/api/pandas.option_context.html#pandas.option_context "pandas.option_context")
     - execute a codeblock with a set of options that revert to prior settings after execution.
    

Note

Developers can check out [pandas/core/config\_init.py](https://github.com/pandas-dev/pandas/blob/main/pandas/core/config_init.py)
 for more information.

All of the functions above accept a regexp pattern (`re.search` style) as an argument, to match an unambiguous substring:

In \[5\]: pd.get\_option("display.chop\_threshold")

In \[6\]: pd.set\_option("display.chop\_threshold", 2)

In \[7\]: pd.get\_option("display.chop\_threshold")
Out\[7\]: 2

In \[8\]: pd.set\_option("chop", 4)

In \[9\]: pd.get\_option("display.chop\_threshold")
Out\[9\]: 4

Copy to clipboard

The following will **not work** because it matches multiple option names, e.g. `display.max_colwidth`, `display.max_rows`, `display.max_columns`:

In \[10\]: pd.get\_option("max")
\---------------------------------------------------------------------------
OptionError                               Traceback (most recent call last)
Cell In\[10\], line 1
\----> 1 pd.get\_option("max")

File ~/work/pandas/pandas/pandas/\_config/config.py:190, in get\_option(pat)
    146 def get\_option(pat: str) \-> Any:
    147     """
    148     Retrieve the value of the specified option.
    149 
   (...)    188     4
    189     """
\--> 190     return \_get\_option\_impl(pat)

File ~/work/pandas/pandas/pandas/\_config/config.py:194, in \_get\_option\_impl(pat, warn)
    193 def \_get\_option\_impl(pat: str, warn: bool \= True) \-> Any:
\--> 194     key \= \_get\_single\_key(pat, warn\=warn)
    196     \# walk the nested dict
    197     root, k \= \_get\_root(key)

File ~/work/pandas/pandas/pandas/\_config/config.py:135, in \_get\_single\_key(pat, warn, extra\_stacklevel)
    133     raise OptionError(f"No such keys(s): {pat!r}")
    134 if len(keys) \> 1:
\--> 135     raise OptionError("Pattern matched multiple keys")
    136 key \= keys\[0\]
    138 if warn:

OptionError: Pattern matched multiple keys

Copy to clipboard

Warning

Using this form of shorthand may cause your code to break if new options with similar names are added in future versions.

Available options[#](https://pandas.pydata.org/docs/user_guide/options.html#available-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

You can get a list of available options and their descriptions with [`describe_option()`](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#pandas.describe_option "pandas.describe_option")
. When called with no argument [`describe_option()`](https://pandas.pydata.org/docs/reference/api/pandas.describe_option.html#pandas.describe_option "pandas.describe_option")
 will print out the descriptions for all available options.

In \[11\]: pd.describe\_option()
compute.use\_bottleneck : bool
    Use the bottleneck library to accelerate if it is installed,
    the default is True
    Valid values: False,True
    \[default: True\] \[currently: True\]
compute.use\_numba : bool
    Use the numba engine option for select operations if it is installed,
    the default is False
    Valid values: False,True
    \[default: False\] \[currently: False\]
compute.use\_numexpr : bool
    Use the numexpr library to accelerate computation if it is installed,
    the default is True
    Valid values: False,True
    \[default: True\] \[currently: True\]
display.chop\_threshold : float or None
    if set to a float value, all float values smaller than the given threshold
    will be displayed as exactly 0 by repr and friends.
    \[default: None\] \[currently: None\]
display.colheader\_justify : 'left'/'right'
    Controls the justification of column headers. used by DataFrameFormatter.
    \[default: right\] \[currently: right\]
display.date\_dayfirst : boolean
    When True, parses ambiguous dates with the day first, eg 20/01/2005.
    This affects parsing only, not how dates are displayed, and applies to
    the Period constructor and partial-string indexing on a DatetimeIndex.
    Timestamp, to\_datetime and read\_csv take their own dayfirst keyword and
    are unaffected.
    \[default: False\] \[currently: False\]
display.date\_yearfirst : boolean
    When True, parses ambiguous dates with the year first, eg 2005/01/20.
    This affects parsing only, not how dates are displayed, and applies to
    the Period constructor and partial-string indexing on a DatetimeIndex.
    Timestamp, to\_datetime and read\_csv take their own yearfirst keyword and
    are unaffected.
    \[default: False\] \[currently: False\]
display.encoding : str/unicode
    Defaults to the detected encoding of the console.
    Specifies the encoding to be used for strings returned by to\_string,
    these are generally strings meant to be displayed on the console.
    \[default: utf-8\] \[currently: utf8\]
display.expand\_frame\_repr : boolean
    Whether to print out the full DataFrame repr for wide DataFrames across
    multiple lines, \`max\_columns\` is still respected, but the output will
    wrap-around across multiple "pages" if its width exceeds \`display.width\`.
    \[default: True\] \[currently: True\]
display.float\_format : callable
    The callable should accept a floating point number and return
    a string with the desired format of the number. This is used
    in some places like SeriesFormatter.
    See formats.format.EngFormatter for an example.
    \[default: None\] \[currently: None\]
display.html.border : int
    A \`\`border=value\`\` attribute is inserted in the \`\`<table>\`\` tag
    for the DataFrame HTML repr.
    \[default: 1\] \[currently: 1\]
display.html.table\_schema : boolean
    Whether to publish a Table Schema representation for frontends
    that support it.
    (default: False)
    \[default: False\] \[currently: False\]
display.html.use\_mathjax : boolean
    When True, Jupyter notebook will process table contents using MathJax,
    rendering mathematical expressions enclosed by the dollar symbol.
    (default: True)
    \[default: True\] \[currently: True\]
display.large\_repr : 'truncate'/'info'
    For DataFrames exceeding max\_rows/max\_cols, the repr (and HTML repr) can
    show a truncated table, or switch to the view from
    df.info() (the behaviour in earlier versions of pandas).
    \[default: truncate\] \[currently: truncate\]
display.max\_categories : int
    This sets the maximum number of categories pandas should output when
    printing out a \`Categorical\` or a Series of dtype "category".
    \[default: 8\] \[currently: 8\]
display.max\_columns : int
    If max\_cols is exceeded, switch to truncate view. Depending on
    \`large\_repr\`, objects are either centrally truncated or printed as
    a summary view.

    'None' value means unlimited. Beware that printing a large number of
    columns could cause your rendering environment (the browser, etc.) to
    crash.

    In case python/IPython is running in a terminal and \`large\_repr\`
    equals 'truncate' this can be set to 0 or None and pandas will auto-detect
    the width of the terminal and print a truncated object which fits
    the screen width. The IPython notebook, IPython qtconsole, or IDLE
    do not run in a terminal and hence it is not possible to do
    correct auto-detection and defaults to 20.
    \[default: 0\] \[currently: 0\]
display.max\_colwidth : int or None
    The maximum width in characters of a column in the repr of
    a pandas data structure. When the column overflows, a "..."
    placeholder is embedded in the output. A 'None' value means unlimited.
    \[default: 50\] \[currently: 50\]
display.max\_dir\_items : int
    The number of items that will be added to \`dir(...)\`. 'None' value means
    unlimited. Because dir is cached, changing this option will not immediately
    affect already existing dataframes until a column is deleted or added.

    This is for instance used to suggest columns from a dataframe to tab
    completion.
    \[default: 100\] \[currently: 100\]
display.max\_info\_columns : int
    max\_info\_columns is used in DataFrame.info method to decide if
    per column information will be printed.
    \[default: 100\] \[currently: 100\]
display.max\_info\_rows : int
    df.info() will usually show null-counts for each column.
    For large frames this can be quite slow. max\_info\_rows and max\_info\_cols
    limit this null check only to frames with smaller dimensions than
    specified.
    \[default: 1690785\] \[currently: 1690785\]
display.max\_rows : int
    If max\_rows is exceeded, switch to truncate view. Depending on
    \`large\_repr\`, objects are either centrally truncated or printed as
    a summary view.

    'None' value means unlimited. Beware that printing a large number of rows
    could cause your rendering environment (the browser, etc.) to crash.

    In case python/IPython is running in a terminal and \`large\_repr\`
    equals 'truncate' this can be set to 0 and pandas will auto-detect
    the height of the terminal and print a truncated object which fits
    the screen height. The IPython notebook, IPython qtconsole, or
    IDLE do not run in a terminal and hence it is not possible to do
    correct auto-detection.
    \[default: 60\] \[currently: 60\]
display.max\_seq\_items : int or None
    When pretty-printing a long sequence, no more than \`max\_seq\_items\`
    will be printed. If items are omitted, they will be denoted by the
    addition of "..." to the resulting string.

    If set to None, the number of items to be printed is unlimited.
    \[default: 100\] \[currently: 100\]
display.memory\_usage : bool, string or None
    This specifies if the memory usage of a DataFrame should be displayed when
    df.info() is called. Valid values True,False,'deep'
    \[default: True\] \[currently: True\]
display.min\_rows : int
    The numbers of rows to show in a truncated view (when \`max\_rows\` is
    exceeded). Ignored when \`max\_rows\` is set to None or 0. When set to
    None, follows the value of \`max\_rows\`.
    \[default: 10\] \[currently: 10\]
display.multi\_sparse : boolean
    "sparsify" MultiIndex display (don't display repeated
    elements in outer levels within groups)
    \[default: True\] \[currently: True\]
display.notebook\_repr\_html : boolean
    When True, IPython notebook will use html representation for
    pandas objects (if it is available).
    \[default: True\] \[currently: True\]
display.pprint\_nest\_depth : int
    Controls the number of nested levels to process when pretty-printing
    \[default: 3\] \[currently: 3\]
display.precision : int
    Floating point output precision in terms of number of places after the
    decimal, for regular formatting as well as scientific notation. Similar
    to \`\`precision\`\` in :meth:\`numpy.set\_printoptions\`.
    \[default: 6\] \[currently: 6\]
display.show\_dimensions : boolean or 'truncate'
    Whether to print out dimensions at the end of DataFrame repr.
    If 'truncate' is specified, only print out the dimensions if the
    frame is truncated (e.g. not display all rows and/or columns)
    \[default: truncate\] \[currently: truncate\]
display.unicode.ambiguous\_as\_wide : boolean
    Whether to treat characters whose Unicode East Asian Width is ambiguous
    as double-width. Only used when \`\`display.unicode.east\_asian\_width\`\` is
    True (default: False)
    \[default: False\] \[currently: False\]
display.unicode.east\_asian\_width : boolean
    Whether to use the Unicode East Asian Width to calculate the display text
    width, so that double-width characters such as CJK characters and most
    emoji are aligned correctly.
    Enabling this may affect performance (default: False)
    \[default: False\] \[currently: False\]
display.width : int
    Width of the display in characters. In case python/IPython is running in
    a terminal this can be set to None and pandas will correctly auto-detect
    the width.
    Note that the IPython notebook, IPython qtconsole, or IDLE do not run in a
    terminal and hence it is not possible to correctly detect the width.
    \[default: 80\] \[currently: 80\]
future.distinguish\_nan\_and\_na Whether to treat NaN entries as distinct from pd.NA in numpy-nullable and pyarrow float dtypes. By default treats both interchangeable as missing values (NaN will be coerced to NA). See discussion in https://github.com/pandas-dev/pandas/issues/32265
    \[default: False\] \[currently: False\]
future.infer\_freq\_returns\_offset Whether pd.infer\_freq and .inferred\_freq return a BaseOffset object instead of a string, which will be the default in a future version of pandas. Set to True to opt in to the future behavior, or False to keep the old behavior and silence the warning.
    \[default: None\] \[currently: None\]
future.infer\_string Whether to infer a sequence of str objects as str dtype rather than object dtype. This has been the default since pandas 3.0. This option is deprecated and will be removed in pandas 4.0, at which point str dtype will always be inferred.
    \[default: True\] \[currently: True\]
    (Deprecated, use \`\` instead.)
future.no\_silent\_downcasting This option is deprecated and will be removed in a future version. It has no effect.
    \[default: False\] \[currently: False\]
    (Deprecated, use \`\` instead.)
future.python\_scalars Whether to return Python scalars instead of NumPy or PyArrow scalars. Values from object dtype data where the operation coerces them to NumPy floats remain NumPy scalars. Currently experimental, setting to True is not recommended for end users.
    \[default: False\] \[currently: False\]
io.excel.ods.reader : string
    The default Excel reader engine for 'ods' files. Available options:
    auto, odf, calamine.
    \[default: auto\] \[currently: auto\]
io.excel.ods.writer : string
    The default Excel writer engine for 'ods' files. Available options:
    auto, odf.
    \[default: auto\] \[currently: auto\]
io.excel.xls.reader : string
    The default Excel reader engine for 'xls' files. Available options:
    auto, xlrd, calamine.
    \[default: auto\] \[currently: auto\]
io.excel.xlsb.reader : string
    The default Excel reader engine for 'xlsb' files. Available options:
    auto, pyxlsb, calamine.
    \[default: auto\] \[currently: auto\]
io.excel.xlsm.reader : string
    The default Excel reader engine for 'xlsm' files. Available options:
    auto, xlrd, openpyxl, calamine.
    \[default: auto\] \[currently: auto\]
io.excel.xlsm.writer : string
    The default Excel writer engine for 'xlsm' files. Available options:
    auto, openpyxl.
    \[default: auto\] \[currently: auto\]
io.excel.xlsx.reader : string
    The default Excel reader engine for 'xlsx' files. Available options:
    auto, xlrd, openpyxl, calamine.
    \[default: auto\] \[currently: auto\]
io.excel.xlsx.writer : string
    The default Excel writer engine for 'xlsx' files. Available options:
    auto, openpyxl, xlsxwriter.
    \[default: auto\] \[currently: auto\]
io.hdf.default\_format : format
    default format writing format, if None, then
    put will default to 'fixed' and append will default to 'table'
    \[default: None\] \[currently: None\]
io.hdf.dropna\_table : boolean
    drop ALL nan rows when appending to a table
    \[default: False\] \[currently: False\]
    (Deprecated, use \`\` instead.)
io.parquet.engine : string
    The default parquet reader/writer engine. Available options:
    'auto', 'pyarrow', 'fastparquet', the default is 'auto'
    \[default: auto\] \[currently: auto\]
io.sql.engine : string
    The default sql reader/writer engine. Available options:
    'auto', 'sqlalchemy', the default is 'auto'
    \[default: auto\] \[currently: auto\]
mode.chained\_assignment : string
    No longer used. This option has had no effect since SettingWithCopyWarning
    was removed in pandas 3.0. This option will be removed in pandas 4.0.
    \[default: warn\] \[currently: warn\]
    (Deprecated, use \`\` instead.)
mode.copy\_on\_write : bool
    Use new copy-view behaviour using Copy-on-Write. No longer used,
    pandas now always uses Copy-on-Write behavior. This option will
    be removed in pandas 4.0.
    \[default: True\] \[currently: True\]
    (Deprecated, use \`\` instead.)
mode.max\_threads : int or None
    Maximum number of worker threads for parallel operations (e.g. \`\`read\_csv\`\`
    for large files).  \`\`None\`\` (the default) means use \`\`min(os.cpu\_count(), 6)\`\`,
    further limited to the CPUs available to the process (CPU affinity and cgroup
    limits).  Set to \`\`1\`\` to disable parallel execution, or to a fixed number to
    raise the cap or to limit thread usage when pandas is embedded in a larger
    parallel workflow.  Ignored on Emscripten/Pyodide, which cannot spawn threads.
    \[default: None\] \[currently: None\]
mode.performance\_warnings : boolean
    Whether to show or hide PerformanceWarnings.
    \[default: True\] \[currently: True\]
mode.sim\_interactive : boolean
    Whether to simulate interactive mode for purposes of testing
    \[default: False\] \[currently: False\]
mode.string\_storage : string
    The default storage for StringDtype.
    \[default: auto\] \[currently: auto\]
plotting.backend : str
    The plotting backend to use. The default value is "matplotlib", the
    backend provided with pandas. Other backends can be specified by
    providing the name of the module that implements the backend.
    \[default: matplotlib\] \[currently: matplotlib\]
plotting.matplotlib.register\_converters : bool or 'auto'.
    Whether to register converters with matplotlib's units registry for
    dates, times, datetimes, and Periods. Toggling to False will remove
    the converters, restoring any converters that pandas overwrote.
    \[default: auto\] \[currently: auto\]
styler.format.decimal : str
    The character representation for the decimal separator for floats and complex.
    This option affects only \`\`Styler\`\` rendering (e.g. \`\`DataFrame.style\`\`), not
    the default Series/DataFrame repr, which is controlled by the \`\`display.\*\`\`
    options.
    \[default: .\] \[currently: .\]
styler.format.escape : str, optional
    Whether to escape certain characters according to the given context; html or latex.
    This option affects only \`\`Styler\`\` rendering (e.g. \`\`DataFrame.style\`\`), not
    the default Series/DataFrame repr, which is controlled by the \`\`display.\*\`\`
    options.
    \[default: None\] \[currently: None\]
styler.format.formatter : str, callable, dict, optional
    A formatter object to be used as default within \`\`Styler.format\`\`.
    \[default: None\] \[currently: None\]
styler.format.na\_rep : str, optional
    The string representation for values identified as missing.
    This option affects only \`\`Styler\`\` rendering (e.g. \`\`DataFrame.style\`\`), not
    the default Series/DataFrame repr, which is controlled by the \`\`display.\*\`\`
    options.
    \[default: None\] \[currently: None\]
styler.format.precision : int
    The precision for floats and complex numbers.
    This option affects only \`\`Styler\`\` rendering (e.g. \`\`DataFrame.style\`\`), not
    the default Series/DataFrame repr, which is controlled by the \`\`display.\*\`\`
    options.
    \[default: 6\] \[currently: 6\]
styler.format.thousands : str, optional
    The character representation for thousands separator for floats, int and complex.
    This option affects only \`\`Styler\`\` rendering (e.g. \`\`DataFrame.style\`\`), not
    the default Series/DataFrame repr, which is controlled by the \`\`display.\*\`\`
    options.
    \[default: None\] \[currently: None\]
styler.html.mathjax : bool
    If False will render special CSS classes to table attributes that indicate Mathjax
    will not be used in Jupyter Notebook.
    \[default: True\] \[currently: True\]
styler.latex.environment : str
    The environment to replace \`\`\\begin{table}\`\`. If "longtable" is used results
    in a specific longtable environment format.
    \[default: None\] \[currently: None\]
styler.latex.hrules : bool
    Whether to add horizontal rules on top and bottom and below the headers.
    \[default: False\] \[currently: False\]
styler.latex.multicol\_align : {"r", "c", "l", "naive-l", "naive-r"}
    The specifier for horizontal alignment of sparsified LaTeX multicolumns. Pipe
    decorators can also be added to non-naive values to draw vertical
    rules, e.g. "\\|r" will draw a rule on the left side of right aligned merged cells.
    \[default: r\] \[currently: r\]
styler.latex.multirow\_align : {"c", "t", "b"}
    The specifier for vertical alignment of sparsified LaTeX multirows.
    \[default: c\] \[currently: c\]
styler.render.encoding : str
    The encoding used for output HTML and LaTeX files.
    \[default: utf-8\] \[currently: utf-8\]
styler.render.max\_columns : int, optional
    The maximum number of columns that will be rendered. May still be reduced to
    satisfy \`\`max\_elements\`\`, which takes precedence. Not applied to LaTeX.
    \[default: None\] \[currently: None\]
styler.render.max\_elements : int
    The maximum number of data-cell (<td>) elements that will be rendered before
    trimming will occur over columns, rows or both if needed. Not applied to LaTeX.
    \[default: 262144\] \[currently: 262144\]
styler.render.max\_rows : int, optional
    The maximum number of rows that will be rendered. May still be reduced to
    satisfy \`\`max\_elements\`\`, which takes precedence. Not applied to LaTeX.
    \[default: None\] \[currently: None\]
styler.render.repr : str
    Determine which output to use in Jupyter Notebook in {"html", "latex"}.
    \[default: html\] \[currently: html\]
styler.sparse.columns : bool
    Whether to sparsify the display of hierarchical columns. Setting to False will
    display each explicit level element in a hierarchical key for each column.
    \[default: True\] \[currently: True\]
styler.sparse.index : bool
    Whether to sparsify the display of a hierarchical index. Setting to False will
    display each explicit level element in a hierarchical key for each row.
    \[default: True\] \[currently: True\]

Copy to clipboard

Getting and setting options[#](https://pandas.pydata.org/docs/user_guide/options.html#getting-and-setting-options "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------

As described above, [`get_option()`](https://pandas.pydata.org/docs/reference/api/pandas.get_option.html#pandas.get_option "pandas.get_option")
 and [`set_option()`](https://pandas.pydata.org/docs/reference/api/pandas.set_option.html#pandas.set_option "pandas.set_option")
 are available from the pandas namespace. To change an option, call `set_option('option regex', new_value)`.

In \[12\]: pd.get\_option("mode.sim\_interactive")
Out\[12\]: False

In \[13\]: pd.set\_option("mode.sim\_interactive", True)

In \[14\]: pd.get\_option("mode.sim\_interactive")
Out\[14\]: True

Copy to clipboard

Note

The option `'mode.sim_interactive'` is mostly used for debugging purposes.

You can use [`reset_option()`](https://pandas.pydata.org/docs/reference/api/pandas.reset_option.html#pandas.reset_option "pandas.reset_option")
 to revert to a setting’s default value

In \[15\]: pd.get\_option("display.max\_rows")
Out\[15\]: 60

In \[16\]: pd.set\_option("display.max\_rows", 999)

In \[17\]: pd.get\_option("display.max\_rows")
Out\[17\]: 999

In \[18\]: pd.reset\_option("display.max\_rows")

In \[19\]: pd.get\_option("display.max\_rows")
Out\[19\]: 60

Copy to clipboard

It’s also possible to reset multiple options at once (using a regex):

In \[20\]: pd.reset\_option("^display")

Copy to clipboard

[`option_context()`](https://pandas.pydata.org/docs/reference/api/pandas.option_context.html#pandas.option_context "pandas.option_context")
 context manager has been exposed through the top-level API, allowing you to execute code with given option values. Option values are restored automatically when you exit the `with` block:

In \[21\]: with pd.option\_context("display.max\_rows", 10, "display.max\_columns", 5):
   ....:    print(pd.get\_option("display.max\_rows"))
   ....:    print(pd.get\_option("display.max\_columns"))
   ....: 
10
5

In \[22\]: print(pd.get\_option("display.max\_rows"))
60

In \[23\]: print(pd.get\_option("display.max\_columns"))
0

Copy to clipboard

Setting startup options in Python/IPython environment[#](https://pandas.pydata.org/docs/user_guide/options.html#setting-startup-options-in-python-ipython-environment "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Using startup scripts for the Python/IPython environment to import pandas and set options makes working with pandas more efficient. To do this, create a `.py` or `.ipy` script in the startup directory of the desired profile. An example where the startup folder is in a default IPython profile can be found at:

$IPYTHONDIR/profile\_default/startup

Copy to clipboard

More information can be found in the [IPython documentation](https://ipython.readthedocs.io/en/stable/interactive/tutorial.html#startup-files)
. An example startup script for pandas is displayed below:

import pandas as pd

pd.set\_option("display.max\_rows", 999)
pd.set\_option("display.precision", 5)

Copy to clipboard

Frequently used options[#](https://pandas.pydata.org/docs/user_guide/options.html#frequently-used-options "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------

The following is a demonstrates the more frequently used display options.

`display.max_rows` and `display.max_columns` sets the maximum number of rows and columns displayed when a frame is pretty-printed. Truncated lines are replaced by an ellipsis.

In \[24\]: df \= pd.DataFrame(np.random.randn(7, 2))

In \[25\]: pd.set\_option("display.max\_rows", 7)

In \[26\]: df
Out\[26\]: 
          0         1
0  0.469112 -0.282863
1 -1.509059 -1.135632
2  1.212112 -0.173215
3  0.119209 -1.044236
4 -0.861849 -2.104569
5 -0.494929  1.071804
6  0.721555 -0.706771

In \[27\]: pd.set\_option("display.max\_rows", 5)

In \[28\]: df
Out\[28\]: 
           0         1
0   0.469112 -0.282863
1  -1.509059 -1.135632
..       ...       ...
5  -0.494929  1.071804
6   0.721555 -0.706771

\[7 rows x 2 columns\]

In \[29\]: pd.reset\_option("display.max\_rows")

Copy to clipboard

Once the `display.max_rows` is exceeded, the `display.min_rows` options determines how many rows are shown in the truncated repr.

In \[30\]: pd.set\_option("display.max\_rows", 8)

In \[31\]: pd.set\_option("display.min\_rows", 4)

\# below max\_rows -> all rows shown
In \[32\]: df \= pd.DataFrame(np.random.randn(7, 2))

In \[33\]: df
Out\[33\]: 
          0         1
0 -1.039575  0.271860
1 -0.424972  0.567020
2  0.276232 -1.087401
3 -0.673690  0.113648
4 -1.478427  0.524988
5  0.404705  0.577046
6 -1.715002 -1.039268

\# above max\_rows -> only min\_rows (4) rows shown
In \[34\]: df \= pd.DataFrame(np.random.randn(9, 2))

In \[35\]: df
Out\[35\]: 
           0         1
0  -0.370647 -1.157892
1  -1.344312  0.844885
..       ...       ...
7   0.276662 -0.472035
8  -0.013960 -0.362543

\[9 rows x 2 columns\]

In \[36\]: pd.reset\_option("display.max\_rows")

In \[37\]: pd.reset\_option("display.min\_rows")

Copy to clipboard

`display.expand_frame_repr` allows for the representation of a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 to stretch across pages, wrapped over the all the columns.

In \[38\]: df \= pd.DataFrame(np.random.randn(5, 10))

In \[39\]: pd.set\_option("expand\_frame\_repr", True)

In \[40\]: df
Out\[40\]: 
          0         1         2  ...         7         8         9
0 -0.006154 -0.923061  0.895717  ...  1.340309 -1.170299 -0.226169
1  0.410835  0.813850  0.132003  ... -1.436737 -1.413681  1.607920
2  1.024180  0.569605  0.875906  ... -0.078638  0.545952 -1.219217
3 -1.226825  0.769804 -1.281247  ...  0.341734  0.959726 -1.110336
4 -0.619976  0.149748 -0.732339  ...  0.301624 -2.179861 -1.369849

\[5 rows x 10 columns\]

In \[41\]: pd.set\_option("expand\_frame\_repr", False)

In \[42\]: df
Out\[42\]: 
          0         1         2         3         4         5         6         7         8         9
0 -0.006154 -0.923061  0.895717  0.805244 -1.206412  2.565646  1.431256  1.340309 -1.170299 -0.226169
1  0.410835  0.813850  0.132003 -0.827317 -0.076467 -1.187678  1.130127 -1.436737 -1.413681  1.607920
2  1.024180  0.569605  0.875906 -2.211372  0.974466 -2.006747 -0.410001 -0.078638  0.545952 -1.219217
3 -1.226825  0.769804 -1.281247 -0.727707 -0.121306 -0.097883  0.695775  0.341734  0.959726 -1.110336
4 -0.619976  0.149748 -0.732339  0.687738  0.176444  0.403310 -0.154951  0.301624 -2.179861 -1.369849

In \[43\]: pd.reset\_option("expand\_frame\_repr")

Copy to clipboard

`display.large_repr` displays a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 that exceed `max_columns` or `max_rows` as a truncated frame or summary.

In \[44\]: df \= pd.DataFrame(np.random.randn(10, 10))

In \[45\]: pd.set\_option("display.max\_rows", 5)

In \[46\]: pd.set\_option("large\_repr", "truncate")

In \[47\]: df
Out\[47\]: 
           0         1         2  ...         7         8         9
0  -0.954208  1.462696 -1.743161  ...  0.995761  2.396780  0.014871
1   3.357427 -0.317441 -1.236269  ...  0.380396  0.084844  0.432390
..       ...       ...       ...  ...       ...       ...       ...
8  -0.303421 -0.858447  0.306996  ...  0.476720  0.473424 -0.242861
9  -0.014805 -0.284319  0.650776  ...  1.613616  0.464000  0.227371

\[10 rows x 10 columns\]

In \[48\]: pd.set\_option("large\_repr", "info")

In \[49\]: df
Out\[49\]: 
<class 'pandas.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 10 columns):
 #   Column  Non-Null Count  Dtype  
\---  ------  --------------  -----  
 0   0       10 non-null     float64
 1   1       10 non-null     float64
 2   2       10 non-null     float64
 3   3       10 non-null     float64
 4   4       10 non-null     float64
 5   5       10 non-null     float64
 6   6       10 non-null     float64
 7   7       10 non-null     float64
 8   8       10 non-null     float64
 9   9       10 non-null     float64
dtypes: float64(10)
memory usage: 932.0 bytes

In \[50\]: pd.reset\_option("large\_repr")

In \[51\]: pd.reset\_option("display.max\_rows")

Copy to clipboard

`display.max_colwidth` sets the maximum width of columns. Cells of this length or longer will be truncated with an ellipsis.

In \[52\]: df \= pd.DataFrame(
   ....:    np.array(
   ....:        \[\
   ....:            \["foo", "bar", "bim", "uncomfortably long string"\],\
   ....:            \["horse", "cow", "banana", "apple"\],\
   ....:        \]
   ....:    )
   ....: )
   ....: 

In \[53\]: pd.set\_option("max\_colwidth", 40)

In \[54\]: df
Out\[54\]: 
       0    1       2                          3
0    foo  bar     bim  uncomfortably long string
1  horse  cow  banana                      apple

In \[55\]: pd.set\_option("max\_colwidth", 6)

In \[56\]: df
Out\[56\]: 
       0    1      2      3
0    foo  bar    bim  un...
1  horse  cow  ba...  apple

In \[57\]: pd.reset\_option("max\_colwidth")

Copy to clipboard

`display.max_info_columns` sets a threshold for the number of columns displayed when calling [`info()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info")
.

In \[58\]: df \= pd.DataFrame(np.random.randn(10, 10))

In \[59\]: pd.set\_option("max\_info\_columns", 11)

In \[60\]: df.info()
<class 'pandas.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 10 columns):
 #   Column  Non-Null Count  Dtype  
\---  ------  --------------  -----  
 0   0       10 non-null     float64
 1   1       10 non-null     float64
 2   2       10 non-null     float64
 3   3       10 non-null     float64
 4   4       10 non-null     float64
 5   5       10 non-null     float64
 6   6       10 non-null     float64
 7   7       10 non-null     float64
 8   8       10 non-null     float64
 9   9       10 non-null     float64
dtypes: float64(10)
memory usage: 932.0 bytes

In \[61\]: pd.set\_option("max\_info\_columns", 5)

In \[62\]: df.info()
<class 'pandas.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Columns: 10 entries, 0 to 9
dtypes: float64(10)
memory usage: 932.0 bytes

In \[63\]: pd.reset\_option("max\_info\_columns")

Copy to clipboard

`display.max_info_rows`: [`info()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info")
 will usually show null-counts for each column. For a large [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
, this can be quite slow. `max_info_rows` and `max_info_cols` limit this null check to the specified rows and columns respectively. The [`info()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.html#pandas.DataFrame.info "pandas.DataFrame.info")
 keyword argument `show_counts=True` will override this.

In \[64\]: df \= pd.DataFrame(np.random.choice(\[0, 1, np.nan\], size\=(10, 10)))

In \[65\]: df
Out\[65\]: 
     0    1    2    3    4    5    6    7    8    9
0  0.0  NaN  1.0  NaN  NaN  0.0  NaN  0.0  NaN  1.0
1  1.0  NaN  1.0  1.0  1.0  1.0  NaN  0.0  0.0  NaN
2  0.0  NaN  1.0  0.0  0.0  NaN  NaN  NaN  NaN  0.0
3  NaN  NaN  NaN  0.0  1.0  1.0  NaN  1.0  NaN  1.0
4  0.0  NaN  NaN  NaN  0.0  NaN  NaN  NaN  1.0  0.0
5  0.0  1.0  1.0  1.0  1.0  0.0  NaN  NaN  1.0  0.0
6  1.0  1.0  1.0  NaN  1.0  NaN  1.0  0.0  NaN  NaN
7  0.0  0.0  1.0  0.0  1.0  0.0  1.0  1.0  0.0  NaN
8  NaN  NaN  NaN  0.0  NaN  NaN  NaN  NaN  1.0  NaN
9  0.0  NaN  0.0  NaN  NaN  0.0  NaN  1.0  1.0  0.0

In \[66\]: pd.set\_option("max\_info\_rows", 11)

In \[67\]: df.info()
<class 'pandas.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 10 columns):
 #   Column  Non-Null Count  Dtype  
\---  ------  --------------  -----  
 0   0       8 non-null      float64
 1   1       3 non-null      float64
 2   2       7 non-null      float64
 3   3       6 non-null      float64
 4   4       7 non-null      float64
 5   5       6 non-null      float64
 6   6       2 non-null      float64
 7   7       6 non-null      float64
 8   8       6 non-null      float64
 9   9       6 non-null      float64
dtypes: float64(10)
memory usage: 932.0 bytes

In \[68\]: pd.set\_option("max\_info\_rows", 5)

In \[69\]: df.info()
<class 'pandas.DataFrame'>
RangeIndex: 10 entries, 0 to 9
Data columns (total 10 columns):
 #   Column  Dtype  
\---  ------  -----  
 0   0       float64
 1   1       float64
 2   2       float64
 3   3       float64
 4   4       float64
 5   5       float64
 6   6       float64
 7   7       float64
 8   8       float64
 9   9       float64
dtypes: float64(10)
memory usage: 932.0 bytes

In \[70\]: pd.reset\_option("max\_info\_rows")

Copy to clipboard

`display.precision` sets the output display precision in terms of decimal places.

In \[71\]: df \= pd.DataFrame(np.random.randn(5, 5))

In \[72\]: pd.set\_option("display.precision", 7)

In \[73\]: df
Out\[73\]: 
           0          1          2          3          4
0 -1.1506406 -0.7983341 -0.5576966  0.3813531  1.3371217
1 -1.5310949  1.3314582 -0.5713290 -0.0266708 -1.0856630
2 -1.1147378 -0.0582158 -0.4867681  1.6851483  0.1125723
3 -1.4953086  0.8984347 -0.1482168 -1.5960698  0.1596530
4  0.2621358  0.0362196  0.1847350 -0.2550694 -0.2710197

In \[74\]: pd.set\_option("display.precision", 4)

In \[75\]: df
Out\[75\]: 
        0       1       2       3       4
0 -1.1506 -0.7983 -0.5577  0.3814  1.3371
1 -1.5311  1.3315 -0.5713 -0.0267 -1.0857
2 -1.1147 -0.0582 -0.4868  1.6851  0.1126
3 -1.4953  0.8984 -0.1482 -1.5961  0.1597
4  0.2621  0.0362  0.1847 -0.2551 -0.2710

Copy to clipboard

`display.chop_threshold` sets the rounding threshold to zero when displaying a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 or [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
. This setting does not change the precision at which the number is stored.

In \[76\]: df \= pd.DataFrame(np.random.randn(6, 6))

In \[77\]: pd.set\_option("chop\_threshold", 0)

In \[78\]: df
Out\[78\]: 
        0       1       2       3       4       5
0  1.2884  0.2946 -1.1658  0.8470 -0.6856  0.6091
1 -0.3040  0.6256 -0.0593  0.2497  1.1039 -1.0875
2  1.9980 -0.2445  0.1362  0.8863 -1.3507 -0.8863
3 -1.0133  1.9209 -0.3882 -2.3144  0.6655  0.4026
4  0.3996 -1.7660  0.8504  0.3881  0.9923  0.7441
5 -0.7398 -1.0549 -0.1796  0.6396  1.5850  1.9067

In \[79\]: pd.set\_option("chop\_threshold", 0.5)

In \[80\]: df
Out\[80\]: 
        0       1       2       3       4       5
0  1.2884  0.0000 -1.1658  0.8470 -0.6856  0.6091
1  0.0000  0.6256  0.0000  0.0000  1.1039 -1.0875
2  1.9980  0.0000  0.0000  0.8863 -1.3507 -0.8863
3 -1.0133  1.9209  0.0000 -2.3144  0.6655  0.0000
4  0.0000 -1.7660  0.8504  0.0000  0.9923  0.7441
5 -0.7398 -1.0549  0.0000  0.6396  1.5850  1.9067

In \[81\]: pd.reset\_option("chop\_threshold")

Copy to clipboard

`display.colheader_justify` controls the justification of the headers. The options are `'right'`, and `'left'`.

In \[82\]: df \= pd.DataFrame(
   ....:    np.array(\[np.random.randn(6), np.random.randint(1, 9, 6) \* 0.1, np.zeros(6)\]).T,
   ....:    columns\=\["A", "B", "C"\],
   ....:    dtype\="float",
   ....: )
   ....: 

In \[83\]: pd.set\_option("colheader\_justify", "right")

In \[84\]: df
Out\[84\]: 
        A    B    C
0  0.1040  0.1  0.0
1  0.1741  0.5  0.0
2 -0.4395  0.4  0.0
3 -0.7413  0.8  0.0
4 -0.0797  0.4  0.0
5 -0.9229  0.3  0.0

In \[85\]: pd.set\_option("colheader\_justify", "left")

In \[86\]: df
Out\[86\]: 
   A       B    C  
0  0.1040  0.1  0.0
1  0.1741  0.5  0.0
2 -0.4395  0.4  0.0
3 -0.7413  0.8  0.0
4 -0.0797  0.4  0.0
5 -0.9229  0.3  0.0

In \[87\]: pd.reset\_option("colheader\_justify")

Copy to clipboard

Number formatting[#](https://pandas.pydata.org/docs/user_guide/options.html#number-formatting "Link to this heading")

----------------------------------------------------------------------------------------------------------------------

pandas also allows you to set how numbers are displayed in the console. Use `display.precision` to control the number of decimal places:

In \[88\]: import numpy as np

In \[89\]: pd.set\_option("display.precision", 2)

In \[90\]: s \= pd.Series(np.random.randn(5), index\=\["a", "b", "c", "d", "e"\])

In \[91\]: s / 1.0e3
Out\[91\]: 
a    3.04e-04
b   -7.21e-04
c   -6.23e-04
d    6.48e-04
e   -1.94e-03
dtype: float64

In \[92\]: s / 1.0e6
Out\[92\]: 
a    3.04e-07
b   -7.21e-07
c   -6.23e-07
d    6.48e-07
e   -1.94e-06
dtype: float64

Copy to clipboard

Use [`round()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.round.html#pandas.DataFrame.round "pandas.DataFrame.round")
 to specifically control rounding of an individual [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")

Unicode formatting[#](https://pandas.pydata.org/docs/user_guide/options.html#unicode-formatting "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

Warning

Enabling this option makes printing DataFrame and Series slower. Use only when it is actually required.

Some Unicode characters, such as Chinese, Japanese and Korean characters and most emoji, are displayed twice as wide as Latin characters. If a DataFrame or Series contains these characters, the default output mode may not align them properly.

In \[93\]: df \= pd.DataFrame({"国籍": \["UK", "日本"\], "名前": \["Alice", "しのぶ"\], "emoji": \["💾", "🤓🤘"\]})

In \[94\]: df
Out\[94\]: 
   国籍     名前 emoji
0  UK  Alice     💾
1  日本    しのぶ    🤓🤘

Copy to clipboard

Enabling `display.unicode.east_asian_width` allows pandas to check each character’s [East Asian Width](https://unicode.org/reports/tr11/)
 property, which despite its name also marks most emoji as wide. These characters can be aligned properly by setting this option to `True`.

In \[95\]: pd.set\_option("display.unicode.east\_asian\_width", True)

In \[96\]: df
Out\[96\]: 
   国籍    名前 emoji
0    UK   Alice    💾
1  日本  しのぶ  🤓🤘

Copy to clipboard

In addition, Unicode characters whose width is “ambiguous” can either be 1 or 2 characters wide depending on the terminal setting or encoding. The option `display.unicode.ambiguous_as_wide` can be used to handle the ambiguity.

By default, an “ambiguous” character’s width, such as “¡” (inverted exclamation) in the example below, is taken to be 1.

In \[97\]: df \= pd.DataFrame({"a": \["xxx", "¡¡"\], "b": \["yyy", "¡¡"\]})

In \[98\]: df
Out\[98\]: 
     a    b
0  xxx  yyy
1   ¡¡   ¡¡

Copy to clipboard

Enabling `display.unicode.ambiguous_as_wide` makes pandas interpret these characters’ widths to be 2. (Note that this option will only be effective when `display.unicode.east_asian_width` is enabled.)

However, setting this option incorrectly for your terminal will cause these characters to be aligned incorrectly:

In \[99\]: pd.set\_option("display.unicode.ambiguous\_as\_wide", True)

In \[100\]: df
Out\[100\]: 
      a     b
0   xxx   yyy
1  ¡¡  ¡¡

Copy to clipboard

Table schema display[#](https://pandas.pydata.org/docs/user_guide/options.html#table-schema-display "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

[`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 and [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 will publish a Table Schema representation by default. This can be enabled globally with the `display.html.table_schema` option:

In \[101\]: pd.set\_option("display.html.table\_schema", True)

Copy to clipboard

Only `'display.max_rows'` are serialized and published.

On this page