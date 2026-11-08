[Skip to main content](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/getting_started/comparison/comparison_with_spss.html)
[3.1 (stable)](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/getting_started/comparison/comparison_with_spss.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/comparison/comparison_with_spss.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/comparison/comparison_with_spss.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/getting_started/comparison/comparison_with_spss.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/getting_started/comparison/comparison_with_spss.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/comparison/comparison_with_spss.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/getting_started/comparison/comparison_with_spss.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/comparison/comparison_with_spss.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/getting_started/comparison/comparison_with_spss.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/comparison/comparison_with_spss.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/comparison/comparison_with_spss.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Comparison with SPSS[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#comparison-with-spss "Link to this heading")

=========================================================================================================================================================

For potential users coming from [SPSS](https://www.ibm.com/spss)
, this page is meant to demonstrate how various SPSS operations would be performed using pandas.

If you’re new to pandas, you might want to first read through [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html#min)
 to familiarize yourself with the library.

As is customary, we import pandas and NumPy as follows:

In \[1\]: import pandas as pd

In \[2\]: import numpy as np

Copy to clipboard

Data structures[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#data-structures "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

### General terminology translation[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#general-terminology-translation "Link to this heading")

 
| pandas | SPSS |
| --- | --- |
| [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame") | data file |
| column | variable |
| row | case |
| groupby | split file |
| `NaN` | system-missing |

### [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#dataframe "Link to this heading")

A [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 in pandas is analogous to an SPSS data file - a two-dimensional data source with labeled columns that can be of different types. As will be shown in this document, almost any operation that can be performed in SPSS can also be accomplished in pandas.

### [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#series "Link to this heading")

A [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 is the data structure that represents one column of a [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
. SPSS doesn’t have a separate data structure for a single variable, but in general, working with a [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 is analogous to working with a variable in SPSS.

### [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#index "Link to this heading")

Every [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 and [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 has an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 – labels on the _rows_ of the data. SPSS does not have an exact analogue, as cases are simply numbered sequentially from 1. In pandas, if no index is specified, a [`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")
 is used by default (first row = 0, second row = 1, and so on).

While using a labeled [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 or [`MultiIndex`](https://pandas.pydata.org/docs/reference/api/pandas.MultiIndex.html#pandas.MultiIndex "pandas.MultiIndex")
 can enable sophisticated analyses and is ultimately an important part of pandas to understand, for this comparison we will essentially ignore the [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 and just treat the [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 as a collection of columns. Please see the [indexing documentation](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing)
 for much more on how to use an [`Index`](https://pandas.pydata.org/docs/reference/api/pandas.Index.html#pandas.Index "pandas.Index")
 effectively.

Copies vs. in place operations[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#copies-vs-in-place-operations "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Most pandas operations return copies of the `Series`/`DataFrame`. To make the changes “stick”, you’ll need to either assign to a new variable:

> sorted\_df \= df.sort\_values("col1")
> 
> Copy to clipboard

or overwrite the original one:

> df \= df.sort\_values("col1")
> 
> Copy to clipboard

Note

You will see an `inplace=True` or `copy=False` keyword argument available for some methods:

df.replace(5, inplace\=True)

Copy to clipboard

There is an active discussion about deprecating and removing `inplace` and `copy` for most methods (e.g. `dropna`) except for a very small subset of methods (including `replace`). Both keywords won’t be necessary anymore in the context of Copy-on-Write. The proposal can be found [here](https://github.com/pandas-dev/pandas/pull/51466)
.

Data input / output[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#data-input-output "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

### Reading external data[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#reading-external-data "Link to this heading")

Like SPSS, pandas provides utilities for reading in data from many formats. The `tips` dataset, found within the pandas tests ([csv](https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv)
) will be used in many of the following examples.

In SPSS, you would use File > Open > Data to import a CSV file:

FILE > OPEN > DATA
/TYPE=CSV
/FILE='tips.csv'
/DELIMITERS=","
/FIRSTCASE=2
/VARIABLES=col1 col2 col3.

Copy to clipboard

The pandas equivalent would use [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")
:

url \= (
    "https://raw.githubusercontent.com/pandas-dev"
    "/pandas/main/pandas/tests/io/data/csv/tips.csv"
)
tips \= pd.read\_csv(url)
tips

Copy to clipboard

Like SPSS’s data import wizard, `read_csv` can take a number of parameters to specify how the data should be parsed. For example, if the data was instead tab delimited, and did not have column names, the pandas command would be:

tips \= pd.read\_csv("tips.csv", sep\="\\t", header\=None)

\# alternatively, read\_table is an alias to read\_csv with tab delimiter
tips \= pd.read\_table("tips.csv", header\=None)

Copy to clipboard

Data operations[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#data-operations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

### Filtering[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#filtering "Link to this heading")

In SPSS, filtering is done through Data > Select Cases:

SELECT IF (total\_bill > 10).
EXECUTE.

Copy to clipboard

In pandas, boolean indexing can be used:

tips\[tips\["total\_bill"\] \> 10\]

Copy to clipboard

### Sorting[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#sorting "Link to this heading")

In SPSS, sorting is done through Data > Sort Cases:

SORT CASES BY sex total\_bill.
EXECUTE.

Copy to clipboard

In pandas, this would be written as:

tips.sort\_values(\["sex", "total\_bill"\])

Copy to clipboard

String processing[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#string-processing "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

### Finding length of string[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#finding-length-of-string "Link to this heading")

In SPSS:

COMPUTE length = LENGTH(time).
EXECUTE.

Copy to clipboard

You can find the length of a character string with [`Series.str.len()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.len.html#pandas.Series.str.len "pandas.Series.str.len")
. In Python 3, all strings are Unicode strings. `len` includes trailing blanks. Use `len` and `rstrip` to exclude trailing blanks.

In \[3\]: tips\["time"\].str.len()
Out\[3\]: 
67     6
92     6
111    6
145    5
135    5
      ..
182    6
156    6
59     6
212    6
170    6
Name: time, Length: 244, dtype: int64

In \[4\]: tips\["time"\].str.rstrip().str.len()
Out\[4\]: 
67     6
92     6
111    6
145    5
135    5
      ..
182    6
156    6
59     6
212    6
170    6
Name: time, Length: 244, dtype: int64

Copy to clipboard

### Changing case[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#changing-case "Link to this heading")

In SPSS:

COMPUTE upper = UPCASE(time).
COMPUTE lower = LOWER(time).
EXECUTE.

Copy to clipboard

The equivalent pandas methods are [`Series.str.upper()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.upper.html#pandas.Series.str.upper "pandas.Series.str.upper")
, [`Series.str.lower()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html#pandas.Series.str.lower "pandas.Series.str.lower")
, and [`Series.str.title()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.title.html#pandas.Series.str.title "pandas.Series.str.title")
.

In \[5\]: firstlast \= pd.DataFrame({"string": \["John Smith", "Jane Cook"\]})

In \[6\]: firstlast\["upper"\] \= firstlast\["string"\].str.upper()

In \[7\]: firstlast\["lower"\] \= firstlast\["string"\].str.lower()

In \[8\]: firstlast\["title"\] \= firstlast\["string"\].str.title()

In \[9\]: firstlast
Out\[9\]: 
       string       upper       lower       title
0  John Smith  JOHN SMITH  john smith  John Smith
1   Jane Cook   JANE COOK   jane cook   Jane Cook

Copy to clipboard

Merging[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#merging "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------

In SPSS, merging data files is done through Data > Merge Files.

The following tables will be used in the merge examples:

In \[10\]: df1 \= pd.DataFrame({"key": \["A", "B", "C", "D"\], "value": np.random.randn(4)})

In \[11\]: df1
Out\[11\]: 
  key     value
0   A  0.469112
1   B -0.282863
2   C -1.509059
3   D -1.135632

In \[12\]: df2 \= pd.DataFrame({"key": \["B", "D", "D", "E"\], "value": np.random.randn(4)})

In \[13\]: df2
Out\[13\]: 
  key     value
0   B  1.212112
1   D -0.173215
2   D  0.119209
3   E -1.044236

Copy to clipboard

pandas DataFrames have a [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge "pandas.DataFrame.merge")
 method, which provides similar functionality. The data does not have to be sorted ahead of time, and different join types are accomplished via the `how` keyword.

In \[14\]: inner\_join \= df1.merge(df2, on\=\["key"\], how\="inner")

In \[15\]: inner\_join
Out\[15\]: 
  key   value\_x   value\_y
0   B -0.282863  1.212112
1   D -1.135632 -0.173215
2   D -1.135632  0.119209

In \[16\]: left\_join \= df1.merge(df2, on\=\["key"\], how\="left")

In \[17\]: left\_join
Out\[17\]: 
  key   value\_x   value\_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209

In \[18\]: right\_join \= df1.merge(df2, on\=\["key"\], how\="right")

In \[19\]: right\_join
Out\[19\]: 
  key   value\_x   value\_y
0   B -0.282863  1.212112
1   D -1.135632 -0.173215
2   D -1.135632  0.119209
3   E       NaN -1.044236

In \[20\]: outer\_join \= df1.merge(df2, on\=\["key"\], how\="outer")

In \[21\]: outer\_join
Out\[21\]: 
  key   value\_x   value\_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
5   E       NaN -1.044236

Copy to clipboard

GroupBy operations[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#groupby-operations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------

### Split-file processing[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#split-file-processing "Link to this heading")

In SPSS, split-file analysis is done through Data > Split File:

SORT CASES BY sex.
SPLIT FILE BY sex.
DESCRIPTIVES VARIABLES=total\_bill tip
  /STATISTICS=MEAN STDDEV MIN MAX.

Copy to clipboard

The pandas equivalent would be:

tips.groupby("sex")\[\["total\_bill", "tip"\]\].agg(\["mean", "std", "min", "max"\])

Copy to clipboard

Missing data[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#missing-data "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------

SPSS uses the period (`.`) for numeric missing values and blank spaces for string missing values. pandas uses `NaN` (Not a Number) for numeric missing values and `None` or `NaN` for string missing values.

In pandas, [`Series.isna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html#pandas.Series.isna "pandas.Series.isna")
 and [`Series.notna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html#pandas.Series.notna "pandas.Series.notna")
 can be used to filter the rows.

In \[22\]: outer\_join\[outer\_join\["value\_x"\].isna()\]
Out\[22\]: 
  key  value\_x   value\_y
5   E      NaN -1.044236

In \[23\]: outer\_join\[outer\_join\["value\_x"\].notna()\]
Out\[23\]: 
  key   value\_x   value\_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209

Copy to clipboard

pandas provides [a variety of methods to work with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data)
. Here are some examples:

### Drop rows with missing values[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#drop-rows-with-missing-values "Link to this heading")

In \[24\]: outer\_join.dropna()
Out\[24\]: 
  key   value\_x   value\_y
1   B -0.282863  1.212112
3   D -1.135632 -0.173215
4   D -1.135632  0.119209

Copy to clipboard

### Forward fill from previous rows[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#forward-fill-from-previous-rows "Link to this heading")

In \[25\]: outer\_join.ffill()
Out\[25\]: 
  key   value\_x   value\_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059  1.212112
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
5   E -1.135632 -1.044236

Copy to clipboard

### Replace missing values with a specified value[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#replace-missing-values-with-a-specified-value "Link to this heading")

Using the mean:

In \[26\]: outer\_join\["value\_x"\].fillna(outer\_join\["value\_x"\].mean())
Out\[26\]: 
0    0.469112
1   -0.282863
2   -1.509059
3   -1.135632
4   -1.135632
5   -0.718815
Name: value\_x, dtype: float64

Copy to clipboard

Other considerations[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#other-considerations "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------

Output management[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spss.html#output-management "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------

While pandas does not have a direct equivalent to SPSS’s Output Management System (OMS), you can capture and export results in various ways:

\# Save summary statistics to CSV
tips.groupby('sex')\[\['total\_bill', 'tip'\]\].mean().to\_csv('summary.csv')

\# Save multiple results to Excel sheets
with pd.ExcelWriter('results.xlsx') as writer:
    tips.describe().to\_excel(writer, sheet\_name\='Descriptives')
    tips.groupby('sex').mean().to\_excel(writer, sheet\_name\='Means by Gender')

Copy to clipboard

On this page