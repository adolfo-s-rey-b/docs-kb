[Skip to main content](https://pandas.pydata.org/docs/reference/api/pandas.wide_to_long.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/reference/api/pandas.wide_to_long.html)
[3.1 (stable)](https://pandas.pydata.org/docs/reference/api/pandas.wide_to_long.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/reference/api/pandas.wide_to_long.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/reference/api/pandas.wide_to_long.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/reference/api/pandas.wide_to_long.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/reference/api/pandas.wide_to_long.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/reference/api/pandas.wide_to_long.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/reference/api/pandas.wide_to_long.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/reference/api/pandas.wide_to_long.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/reference/api/pandas.wide_to_long.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/reference/api/pandas.wide_to_long.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/reference/api/pandas.wide_to_long.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/reference/api/pandas.wide_to_long.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

pandas.wide\_to\_long[#](https://pandas.pydata.org/docs/reference/api/pandas.wide_to_long.html#pandas-wide-to-long "Link to this heading")

===========================================================================================================================================

pandas.wide\_to\_long(_df_, _stubnames_, _i_, _j_, _sep\=''_, _suffix\='\\\\d+'_)[\[source\]](https://github.com/pandas-dev/pandas/blob/v3.1.1/pandas/core/reshape/melt.py#L378-L686)
[#](https://pandas.pydata.org/docs/reference/api/pandas.wide_to_long.html#pandas.wide_to_long "Link to this definition")

Unpivot a DataFrame from wide to long format.

Less flexible but more user-friendly than melt.

With stubnames \[‘A’, ‘B’\], this function expects to find one or more group of columns with format A-suffix1, A-suffix2,…, B-suffix1, B-suffix2,… You specify what you want to call this suffix in the resulting long format with j (for example j=’year’)

Each row of these wide variables are assumed to be uniquely identified by i (can be a single column name or a list of column names)

All remaining variables in the data frame are left intact.

Parameters:

**df**DataFrame

The wide-format DataFrame.

**stubnames**str or list-like

The stub name(s). The wide format variables are assumed to start with the stub names.

**i**str or list-like

Column(s) to use as id variable(s).

**j**str

The name of the sub-observation variable. What you wish to name your suffix in the long format.

**sep**str, default “”

A character indicating the separation of the variable names in the wide format, to be stripped from the names in the long format. For example, if your column names are A-suffix1, A-suffix2, you can strip the hyphen by specifying sep=’-’.

**suffix**str, default ‘\\d+’

A regular expression capturing the wanted suffixes. ‘\\d+’ captures numeric suffixes. Suffixes with no numbers could be specified with the negated character class ‘\\D+’. You can also further disambiguate suffixes, for example, if your wide variables are of the form A-one, B-two,.., and you have an unrelated column A-rating, you can ignore the last one by specifying suffix=’(!?one|two)’. When all suffixes are numeric, they are cast to int64/float64.

Returns:

DataFrame

A DataFrame that contains each stub name as a variable, with new index (i, j).

See also

[`melt`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html#pandas.melt "pandas.melt")

Unpivot a DataFrame from wide to long format, optionally leaving identifiers set.

[`pivot`](https://pandas.pydata.org/docs/reference/api/pandas.pivot.html#pandas.pivot "pandas.pivot")

Create a spreadsheet-style pivot table as a DataFrame.

[`DataFrame.pivot`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "pandas.DataFrame.pivot")

Pivot without aggregation that can handle non-numeric data.

[`DataFrame.pivot_table`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table "pandas.DataFrame.pivot_table")

Generalization of pivot that can handle duplicate values for one index/column pair.

[`DataFrame.unstack`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.unstack.html#pandas.DataFrame.unstack "pandas.DataFrame.unstack")

Pivot based on the index values instead of a column.

Notes

All extra variables are left untouched. This simply uses pandas.melt under the hood, but is hard-coded to “do the right thing” in a typical case.

Examples

\>>> np.random.seed(123)
\>>> df \= pd.DataFrame(
...     {
...         "A1970": {0: "a", 1: "b", 2: "c"},
...         "A1980": {0: "d", 1: "e", 2: "f"},
...         "B1970": {0: 2.5, 1: 1.2, 2: 0.7},
...         "B1980": {0: 3.2, 1: 1.3, 2: 0.1},
...         "X": dict(zip(range(3), np.random.randn(3), strict\=True)),
...     }
... )
\>>> df\["id"\] \= df.index
\>>> df
  A1970 A1980  B1970  B1980         X  id
0     a     d    2.5    3.2 -1.085631   0
1     b     e    1.2    1.3  0.997345   1
2     c     f    0.7    0.1  0.282978   2
\>>> pd.wide\_to\_long(df, \["A", "B"\], i\="id", j\="year")
...
                X  A    B
id year
0  1970 -1.085631  a  2.5
1  1970  0.997345  b  1.2
2  1970  0.282978  c  0.7
0  1980 -1.085631  d  3.2
1  1980  0.997345  e  1.3
2  1980  0.282978  f  0.1

Copy to clipboard

With multiple id columns

\>>> df \= pd.DataFrame(
...     {
...         "famid": \[1, 1, 1, 2, 2, 2, 3, 3, 3\],
...         "birth": \[1, 2, 3, 1, 2, 3, 1, 2, 3\],
...         "ht1": \[2.8, 2.9, 2.2, 2, 1.8, 1.9, 2.2, 2.3, 2.1\],
...         "ht2": \[3.4, 3.8, 2.9, 3.2, 2.8, 2.4, 3.3, 3.4, 2.9\],
...     }
... )
\>>> df
   famid  birth  ht1  ht2
0      1      1  2.8  3.4
1      1      2  2.9  3.8
2      1      3  2.2  2.9
3      2      1  2.0  3.2
4      2      2  1.8  2.8
5      2      3  1.9  2.4
6      3      1  2.2  3.3
7      3      2  2.3  3.4
8      3      3  2.1  2.9
\>>> long\_format \= pd.wide\_to\_long(df, stubnames\="ht", i\=\["famid", "birth"\], j\="age")
\>>> long\_format
...
                  ht
famid birth age
1     1     1    2.8
            2    3.4
      2     1    2.9
            2    3.8
      3     1    2.2
            2    2.9
2     1     1    2.0
            2    3.2
      2     1    1.8
            2    2.8
      3     1    1.9
            2    2.4
3     1     1    2.2
            2    3.3
      2     1    2.3
            2    3.4
      3     1    2.1
            2    2.9

Copy to clipboard

Going from long back to wide just takes some creative use of unstack

\>>> wide\_format \= long\_format.unstack()
\>>> wide\_format.columns \= wide\_format.columns.map("{0\[0\]}{0\[1\]}".format)
\>>> wide\_format.reset\_index()
   famid  birth  ht1  ht2
0      1      1  2.8  3.4
1      1      2  2.9  3.8
2      1      3  2.2  2.9
3      2      1  2.0  3.2
4      2      2  1.8  2.8
5      2      3  1.9  2.4
6      3      1  2.2  3.3
7      3      2  2.3  3.4
8      3      3  2.1  2.9

Copy to clipboard

Less wieldy column names are also handled

\>>> np.random.seed(0)
\>>> df \= pd.DataFrame(
...     {
...         "A(weekly)-2010": np.random.rand(3),
...         "A(weekly)-2011": np.random.rand(3),
...         "B(weekly)-2010": np.random.rand(3),
...         "B(weekly)-2011": np.random.rand(3),
...         "X": np.random.randint(3, size\=3),
...     }
... )
\>>> df\["id"\] \= df.index
\>>> df
   A(weekly)-2010  A(weekly)-2011  B(weekly)-2010  B(weekly)-2011  X  id
0        0.548814        0.544883        0.437587        0.383442  0   0
1        0.715189        0.423655        0.891773        0.791725  1   1
2        0.602763        0.645894        0.963663        0.528895  1   2

Copy to clipboard

\>>> pd.wide\_to\_long(df, \["A(weekly)", "B(weekly)"\], i\="id", j\="year", sep\="-")
...
         X  A(weekly)  B(weekly)
id year
0  2010  0   0.548814   0.437587
1  2010  1   0.715189   0.891773
2  2010  1   0.602763   0.963663
0  2011  0   0.544883   0.383442
1  2011  1   0.423655   0.791725
2  2011  1   0.645894   0.528895

Copy to clipboard

If we have many columns, we could also use a regex to find our stubnames and pass that list on to wide\_to\_long

\>>> stubnames \= sorted(
...     set(
...         \[\
...             match\[0\]\
...             for match in df.columns.str.findall(r"\[A-B\]\\(.\*\\)").values\
...             if match != \[\]\
...         \]
...     )
... )
\>>> list(stubnames)
\['A(weekly)', 'B(weekly)'\]

Copy to clipboard

All of the above examples have integers as suffixes. It is possible to have non-integers as suffixes.

\>>> df \= pd.DataFrame(
...     {
...         "famid": \[1, 1, 1, 2, 2, 2, 3, 3, 3\],
...         "birth": \[1, 2, 3, 1, 2, 3, 1, 2, 3\],
...         "ht\_one": \[2.8, 2.9, 2.2, 2, 1.8, 1.9, 2.2, 2.3, 2.1\],
...         "ht\_two": \[3.4, 3.8, 2.9, 3.2, 2.8, 2.4, 3.3, 3.4, 2.9\],
...     }
... )
\>>> df
   famid  birth  ht\_one  ht\_two
0      1      1     2.8     3.4
1      1      2     2.9     3.8
2      1      3     2.2     2.9
3      2      1     2.0     3.2
4      2      2     1.8     2.8
5      2      3     1.9     2.4
6      3      1     2.2     3.3
7      3      2     2.3     3.4
8      3      3     2.1     2.9

Copy to clipboard

\>>> long\_format \= pd.wide\_to\_long(
...     df, stubnames\="ht", i\=\["famid", "birth"\], j\="age", sep\="\_", suffix\=r"\\w+"
... )
\>>> long\_format
...
                  ht
famid birth age
1     1     one  2.8
            two  3.4
      2     one  2.9
            two  3.8
      3     one  2.2
            two  2.9
2     1     one  2.0
            two  3.2
      2     one  1.8
            two  2.8
      3     one  1.9
            two  2.4
3     1     one  2.2
            two  3.3
      2     one  2.3
            two  3.4
      3     one  2.1
            two  2.9

Copy to clipboard

On this page