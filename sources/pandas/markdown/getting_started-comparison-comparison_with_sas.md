[Skip to main content](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/getting_started/comparison/comparison_with_sas.html)
[3.1 (stable)](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/getting_started/comparison/comparison_with_sas.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/comparison/comparison_with_sas.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/comparison/comparison_with_sas.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/getting_started/comparison/comparison_with_sas.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/getting_started/comparison/comparison_with_sas.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/comparison/comparison_with_sas.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/getting_started/comparison/comparison_with_sas.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/comparison/comparison_with_sas.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/getting_started/comparison/comparison_with_sas.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/comparison/comparison_with_sas.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/comparison/comparison_with_sas.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Comparison with SAS[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#comparison-with-sas "Link to this heading")

======================================================================================================================================================

For potential users coming from [SAS](https://en.wikipedia.org/wiki/SAS_(software))
 this page is meant to demonstrate how different SAS operations would be performed in pandas.

If you’re new to pandas, you might want to first read through [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html#min)
 to familiarize yourself with the library.

As is customary, we import pandas and NumPy as follows:

In \[1\]: import pandas as pd

In \[2\]: import numpy as np

Copy to clipboard

Data structures[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#data-structures "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

### General terminology translation[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#general-terminology-translation "Link to this heading")

 
| pandas | SAS |
| --- | --- |
| `DataFrame` | data set |
| column | variable |
| row | observation |
| groupby | BY-group |
| `NaN` | `.` |

### `DataFrame`[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#dataframe "Link to this heading")

A `DataFrame` in pandas is analogous to a SAS data set - a two-dimensional data source with labeled columns that can be of different types. As will be shown in this document, almost any operation that can be applied to a data set using SAS’s `DATA` step, can also be accomplished in pandas.

### `Series`[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#series "Link to this heading")

A `Series` is the data structure that represents one column of a `DataFrame`. SAS doesn’t have a separate data structure for a single column, but in general, working with a `Series` is analogous to referencing a column in the `DATA` step.

### `Index`[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#index "Link to this heading")

Every `DataFrame` and `Series` has an `Index` - which are labels on the _rows_ of the data. SAS does not have an exactly analogous concept. A data set’s rows are essentially unlabeled, other than an implicit integer index that can be accessed during the `DATA` step (`_N_`).

In pandas, if no index is specified, an integer index is also used by default (first row = 0, second row = 1, and so on). While using a labeled `Index` or `MultiIndex` can enable sophisticated analyses and is ultimately an important part of pandas to understand, for this comparison we will essentially ignore the `Index` and just treat the `DataFrame` as a collection of columns. Please see the [indexing documentation](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing)
 for much more on how to use an `Index` effectively.

### Copies vs. in place operations[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#copies-vs-in-place-operations "Link to this heading")

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

Data input / output[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#data-input-output "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------------

### Constructing a DataFrame from values[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#constructing-a-dataframe-from-values "Link to this heading")

A SAS data set can be built from specified values by placing the data after a `datalines` statement and specifying the column names.

data df;
    input x y;
    datalines;
    1 2
    3 4
    5 6
    ;
run;

Copy to clipboard

A pandas `DataFrame` can be constructed in many different ways, but for a small number of values, it is often convenient to specify it as a Python dictionary, where the keys are the column names and the values are the data.

In \[1\]: df \= pd.DataFrame({"x": \[1, 3, 5\], "y": \[2, 4, 6\]})

In \[2\]: df
Out\[2\]: 
   x  y
0  1  2
1  3  4
2  5  6

Copy to clipboard

### Reading external data[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#reading-external-data "Link to this heading")

Like SAS, pandas provides utilities for reading in data from many formats. The `tips` dataset, found within the pandas tests ([csv](https://raw.githubusercontent.com/pandas-dev/pandas/main/pandas/tests/io/data/csv/tips.csv)
) will be used in many of the following examples.

SAS provides `PROC IMPORT` to read csv data into a data set.

proc import datafile='tips.csv' dbms=csv out\=tips replace;
    getnames=yes;
run;

Copy to clipboard

The pandas method is [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")
, which works similarly.

In \[3\]: url \= (
   ...:    "https://raw.githubusercontent.com/pandas-dev/"
   ...:    "pandas/main/pandas/tests/io/data/csv/tips.csv"
   ...: )
   ...: 

In \[4\]: tips \= pd.read\_csv(url)

In \[5\]: tips
Out\[5\]: 
     total\_bill   tip     sex smoker   day    time  size
0         16.99  1.01  Female     No   Sun  Dinner     2
1         10.34  1.66    Male     No   Sun  Dinner     3
2         21.01  3.50    Male     No   Sun  Dinner     3
3         23.68  3.31    Male     No   Sun  Dinner     2
4         24.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       29.03  5.92    Male     No   Sat  Dinner     3
240       27.18  2.00  Female    Yes   Sat  Dinner     2
241       22.67  2.00    Male    Yes   Sat  Dinner     2
242       17.82  1.75    Male     No   Sat  Dinner     2
243       18.78  3.00  Female     No  Thur  Dinner     2

\[244 rows x 7 columns\]

Copy to clipboard

Like `PROC IMPORT`, `read_csv` can take a number of parameters to specify how the data should be parsed. For example, if the data was instead tab delimited, and did not have column names, the pandas command would be:

tips \= pd.read\_csv("tips.csv", sep\="\\t", header\=None)

\# alternatively, read\_table is an alias to read\_csv with tab delimiter
tips \= pd.read\_table("tips.csv", header\=None)

Copy to clipboard

In addition to text/csv, pandas supports a variety of other data formats such as Excel, HDF5, and SQL databases. These are all read via a `pd.read_*` function. See the [IO documentation](https://pandas.pydata.org/docs/user_guide/io.html#io)
 for more details.

### Limiting output[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#limiting-output "Link to this heading")

By default, pandas will truncate output of large `DataFrame`s to show the first and last rows. This can be overridden by [changing the pandas options](https://pandas.pydata.org/docs/user_guide/options.html#options)
, or using [`DataFrame.head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head "pandas.DataFrame.head")
 or [`DataFrame.tail()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail "pandas.DataFrame.tail")
.

In \[1\]: tips.head(5)
Out\[1\]: 
   total\_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4

Copy to clipboard

The equivalent in SAS would be:

proc print data=df(obs=5);
run;

Copy to clipboard

### Exporting data[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#exporting-data "Link to this heading")

The inverse of `PROC IMPORT` in SAS is `PROC EXPORT`

proc export data=tips outfile='tips2.csv' dbms=csv;
run;

Copy to clipboard

Similarly in pandas, the opposite of `read_csv` is [`to_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html#pandas.DataFrame.to_csv "pandas.DataFrame.to_csv")
, and other data formats follow a similar api.

tips.to\_csv("tips2.csv")

Copy to clipboard

Data operations[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#data-operations "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------------

### Operations on columns[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#operations-on-columns "Link to this heading")

In the `DATA` step, arbitrary math expressions can be used on new or existing columns.

data tips;
    set tips;
    total\_bill = total\_bill - 2;
    new\_bill = total\_bill / 2;
run;

Copy to clipboard

pandas provides vectorized operations by specifying the individual `Series` in the `DataFrame`. New columns can be assigned in the same way. The [`DataFrame.drop()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop "pandas.DataFrame.drop")
 method drops a column from the `DataFrame`.

In \[1\]: tips\["total\_bill"\] \= tips\["total\_bill"\] \- 2

In \[2\]: tips\["new\_bill"\] \= tips\["total\_bill"\] / 2

In \[3\]: tips
Out\[3\]: 
     total\_bill   tip     sex smoker   day    time  size  new\_bill
0         14.99  1.01  Female     No   Sun  Dinner     2     7.495
1          8.34  1.66    Male     No   Sun  Dinner     3     4.170
2         19.01  3.50    Male     No   Sun  Dinner     3     9.505
3         21.68  3.31    Male     No   Sun  Dinner     2    10.840
4         22.59  3.61  Female     No   Sun  Dinner     4    11.295
..          ...   ...     ...    ...   ...     ...   ...       ...
239       27.03  5.92    Male     No   Sat  Dinner     3    13.515
240       25.18  2.00  Female    Yes   Sat  Dinner     2    12.590
241       20.67  2.00    Male    Yes   Sat  Dinner     2    10.335
242       15.82  1.75    Male     No   Sat  Dinner     2     7.910
243       16.78  3.00  Female     No  Thur  Dinner     2     8.390

\[244 rows x 8 columns\]

In \[4\]: tips \= tips.drop("new\_bill", axis\=1)

Copy to clipboard

### Filtering[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#filtering "Link to this heading")

Filtering in SAS is done with an `if` or `where` statement, on one or more columns.

data tips;
    set tips;
    if total\_bill > 10;
run;

data tips;
    set tips;
    where total\_bill > 10;
    /\* equivalent in this case - where happens before the
       DATA step begins and can also be used in PROC statements \*/
run;

Copy to clipboard

DataFrames can be filtered in multiple ways; the most intuitive of which is using [boolean indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-boolean)
.

In \[1\]: tips\[tips\["total\_bill"\] \> 10\]
Out\[1\]: 
     total\_bill   tip     sex smoker   day    time  size
0         14.99  1.01  Female     No   Sun  Dinner     2
2         19.01  3.50    Male     No   Sun  Dinner     3
3         21.68  3.31    Male     No   Sun  Dinner     2
4         22.59  3.61  Female     No   Sun  Dinner     4
5         23.29  4.71    Male     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       27.03  5.92    Male     No   Sat  Dinner     3
240       25.18  2.00  Female    Yes   Sat  Dinner     2
241       20.67  2.00    Male    Yes   Sat  Dinner     2
242       15.82  1.75    Male     No   Sat  Dinner     2
243       16.78  3.00  Female     No  Thur  Dinner     2

\[204 rows x 7 columns\]

Copy to clipboard

The above statement is simply passing a `Series` of `True`/`False` objects to the DataFrame, returning all rows with `True`.

In \[2\]: is\_dinner \= tips\["time"\] \== "Dinner"

In \[3\]: is\_dinner
Out\[3\]: 
0      True
1      True
2      True
3      True
4      True
       ... 
239    True
240    True
241    True
242    True
243    True
Name: time, Length: 244, dtype: bool

In \[4\]: is\_dinner.value\_counts()
Out\[4\]: 
time
True     176
False     68
Name: count, dtype: int64

In \[5\]: tips\[is\_dinner\]
Out\[5\]: 
     total\_bill   tip     sex smoker   day    time  size
0         14.99  1.01  Female     No   Sun  Dinner     2
1          8.34  1.66    Male     No   Sun  Dinner     3
2         19.01  3.50    Male     No   Sun  Dinner     3
3         21.68  3.31    Male     No   Sun  Dinner     2
4         22.59  3.61  Female     No   Sun  Dinner     4
..          ...   ...     ...    ...   ...     ...   ...
239       27.03  5.92    Male     No   Sat  Dinner     3
240       25.18  2.00  Female    Yes   Sat  Dinner     2
241       20.67  2.00    Male    Yes   Sat  Dinner     2
242       15.82  1.75    Male     No   Sat  Dinner     2
243       16.78  3.00  Female     No  Thur  Dinner     2

\[176 rows x 7 columns\]

Copy to clipboard

### If/then logic[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#if-then-logic "Link to this heading")

In SAS, if/then logic can be used to create new columns.

data tips;
    set tips;
    format bucket $4.;

    if total\_bill < 10 then bucket = 'low';
    else bucket = 'high';
run;

Copy to clipboard

The same operation in pandas can be accomplished using the `where` method from `numpy`.

In \[1\]: tips\["bucket"\] \= np.where(tips\["total\_bill"\] < 10, "low", "high")

In \[2\]: tips
Out\[2\]: 
     total\_bill   tip     sex smoker   day    time  size bucket
0         14.99  1.01  Female     No   Sun  Dinner     2   high
1          8.34  1.66    Male     No   Sun  Dinner     3    low
2         19.01  3.50    Male     No   Sun  Dinner     3   high
3         21.68  3.31    Male     No   Sun  Dinner     2   high
4         22.59  3.61  Female     No   Sun  Dinner     4   high
..          ...   ...     ...    ...   ...     ...   ...    ...
239       27.03  5.92    Male     No   Sat  Dinner     3   high
240       25.18  2.00  Female    Yes   Sat  Dinner     2   high
241       20.67  2.00    Male    Yes   Sat  Dinner     2   high
242       15.82  1.75    Male     No   Sat  Dinner     2   high
243       16.78  3.00  Female     No  Thur  Dinner     2   high

\[244 rows x 8 columns\]

Copy to clipboard

### Date functionality[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#date-functionality "Link to this heading")

SAS provides a variety of functions to do operations on date/datetime columns.

data tips;
    set tips;
    format date1 date2 date1\_plusmonth mmddyy10.;
    date1 = mdy(1, 15, 2013);
    date2 = mdy(2, 15, 2015);
    date1\_year = year(date1);
    date2\_month = month(date2);
    \* shift date to beginning of next interval;
    date1\_next = intnx('MONTH', date1, 1);
    \* count intervals between dates;
    months\_between = intck('MONTH', date1, date2);
run;

Copy to clipboard

The equivalent pandas operations are shown below. In addition to these functions pandas supports other Time Series features not available in Base SAS (such as resampling and custom offsets) - see the [timeseries documentation](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries)
 for more details.

In \[1\]: tips\["date1"\] \= pd.Timestamp("2013-01-15")

In \[2\]: tips\["date2"\] \= pd.Timestamp("2015-02-15")

In \[3\]: tips\["date1\_year"\] \= tips\["date1"\].dt.year

In \[4\]: tips\["date2\_month"\] \= tips\["date2"\].dt.month

In \[5\]: tips\["date1\_next"\] \= tips\["date1"\] + pd.offsets.MonthBegin()

In \[6\]: tips\["months\_between"\] \= tips\["date2"\].dt.to\_period("M") \- tips\[\
   ...:    "date1"\
   ...: \].dt.to\_period("M")
   ...: 

In \[7\]: tips\[\
   ...:    \["date1", "date2", "date1\_year", "date2\_month", "date1\_next", "months\_between"\]\
   ...: \]
   ...: 
Out\[7\]: 
         date1      date2  date1\_year  date2\_month date1\_next    months\_between
0   2013-01-15 2015-02-15        2013            2 2013-02-01  <25 \* MonthEnds>
1   2013-01-15 2015-02-15        2013            2 2013-02-01  <25 \* MonthEnds>
2   2013-01-15 2015-02-15        2013            2 2013-02-01  <25 \* MonthEnds>
3   2013-01-15 2015-02-15        2013            2 2013-02-01  <25 \* MonthEnds>
4   2013-01-15 2015-02-15        2013            2 2013-02-01  <25 \* MonthEnds>
..         ...        ...         ...          ...        ...               ...
239 2013-01-15 2015-02-15        2013            2 2013-02-01  <25 \* MonthEnds>
240 2013-01-15 2015-02-15        2013            2 2013-02-01  <25 \* MonthEnds>
241 2013-01-15 2015-02-15        2013            2 2013-02-01  <25 \* MonthEnds>
242 2013-01-15 2015-02-15        2013            2 2013-02-01  <25 \* MonthEnds>
243 2013-01-15 2015-02-15        2013            2 2013-02-01  <25 \* MonthEnds>

\[244 rows x 6 columns\]

Copy to clipboard

### Selection of columns[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#selection-of-columns "Link to this heading")

SAS provides keywords in the `DATA` step to select, drop, and rename columns.

data tips;
    set tips;
    keep sex total\_bill tip;
run;

data tips;
    set tips;
    drop sex;
run;

data tips;
    set tips;
    rename total\_bill=total\_bill\_2;
run;

Copy to clipboard

The same operations are expressed in pandas below.

#### Keep certain columns[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#keep-certain-columns "Link to this heading")

In \[1\]: tips\[\["sex", "total\_bill", "tip"\]\]
Out\[1\]: 
        sex  total\_bill   tip
0    Female       14.99  1.01
1      Male        8.34  1.66
2      Male       19.01  3.50
3      Male       21.68  3.31
4    Female       22.59  3.61
..      ...         ...   ...
239    Male       27.03  5.92
240  Female       25.18  2.00
241    Male       20.67  2.00
242    Male       15.82  1.75
243  Female       16.78  3.00

\[244 rows x 3 columns\]

Copy to clipboard

#### Drop a column[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#drop-a-column "Link to this heading")

In \[2\]: tips.drop("sex", axis\=1)
Out\[2\]: 
     total\_bill   tip smoker   day    time  size
0         14.99  1.01     No   Sun  Dinner     2
1          8.34  1.66     No   Sun  Dinner     3
2         19.01  3.50     No   Sun  Dinner     3
3         21.68  3.31     No   Sun  Dinner     2
4         22.59  3.61     No   Sun  Dinner     4
..          ...   ...    ...   ...     ...   ...
239       27.03  5.92     No   Sat  Dinner     3
240       25.18  2.00    Yes   Sat  Dinner     2
241       20.67  2.00    Yes   Sat  Dinner     2
242       15.82  1.75     No   Sat  Dinner     2
243       16.78  3.00     No  Thur  Dinner     2

\[244 rows x 6 columns\]

Copy to clipboard

#### Rename a column[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#rename-a-column "Link to this heading")

In \[3\]: tips.rename(columns\={"total\_bill": "total\_bill\_2"})
Out\[3\]: 
     total\_bill\_2   tip     sex smoker   day    time  size
0           14.99  1.01  Female     No   Sun  Dinner     2
1            8.34  1.66    Male     No   Sun  Dinner     3
2           19.01  3.50    Male     No   Sun  Dinner     3
3           21.68  3.31    Male     No   Sun  Dinner     2
4           22.59  3.61  Female     No   Sun  Dinner     4
..            ...   ...     ...    ...   ...     ...   ...
239         27.03  5.92    Male     No   Sat  Dinner     3
240         25.18  2.00  Female    Yes   Sat  Dinner     2
241         20.67  2.00    Male    Yes   Sat  Dinner     2
242         15.82  1.75    Male     No   Sat  Dinner     2
243         16.78  3.00  Female     No  Thur  Dinner     2

\[244 rows x 7 columns\]

Copy to clipboard

### Sorting by values[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#sorting-by-values "Link to this heading")

Sorting in SAS is accomplished via `PROC SORT`

proc sort data=tips;
    by sex total\_bill;
run;

Copy to clipboard

pandas has a [`DataFrame.sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")
 method, which takes a list of columns to sort by.

In \[1\]: tips \= tips.sort\_values(\["sex", "total\_bill"\])

In \[2\]: tips
Out\[2\]: 
     total\_bill    tip     sex smoker   day    time  size
67         1.07   1.00  Female    Yes   Sat  Dinner     1
92         3.75   1.00  Female    Yes   Fri  Dinner     2
111        5.25   1.00  Female     No   Sat  Dinner     1
145        6.35   1.50  Female     No  Thur   Lunch     2
135        6.51   1.25  Female     No  Thur   Lunch     2
..          ...    ...     ...    ...   ...     ...   ...
182       43.35   3.50    Male    Yes   Sun  Dinner     3
156       46.17   5.00    Male     No   Sun  Dinner     6
59        46.27   6.73    Male     No   Sat  Dinner     4
212       46.33   9.00    Male     No   Sat  Dinner     4
170       48.81  10.00    Male    Yes   Sat  Dinner     3

\[244 rows x 7 columns\]

Copy to clipboard

String processing[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#string-processing "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------

### Finding length of string[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#finding-length-of-string "Link to this heading")

SAS determines the length of a character string with the [LENGTHN](https://support.sas.com/documentation/cdl/en/lrdict/64316/HTML/default/viewer.htm#a002284668.htm)
 and [LENGTHC](https://support.sas.com/documentation/cdl/en/lrdict/64316/HTML/default/viewer.htm#a002283942.htm)
 functions. `LENGTHN` excludes trailing blanks and `LENGTHC` includes trailing blanks.

data \_null\_;
set tips;
put(LENGTHN(time));
put(LENGTHC(time));
run;

Copy to clipboard

You can find the length of a character string with [`Series.str.len()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.len.html#pandas.Series.str.len "pandas.Series.str.len")
. In Python 3, all strings are Unicode strings. `len` includes trailing blanks. Use `len` and `rstrip` to exclude trailing blanks.

In \[1\]: tips\["time"\].str.len()
Out\[1\]: 
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

In \[2\]: tips\["time"\].str.rstrip().str.len()
Out\[2\]: 
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

### Finding position of substring[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#finding-position-of-substring "Link to this heading")

SAS determines the position of a character in a string with the [FINDW](https://support.sas.com/documentation/cdl/en/lrdict/64316/HTML/default/viewer.htm#a002978282.htm)
 function. `FINDW` takes the string defined by the first argument and searches for the first position of the substring you supply as the second argument.

data \_null\_;
set tips;
put(FINDW(sex,'ale'));
run;

Copy to clipboard

You can find the position of a character in a column of strings with the [`Series.str.find()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.find.html#pandas.Series.str.find "pandas.Series.str.find")
 method. `find` searches for the first position of the substring. If the substring is found, the method returns its position. If not found, it returns `-1`. Keep in mind that Python indexes are zero-based.

In \[1\]: tips\["sex"\].str.find("ale")
Out\[1\]: 
67     3
92     3
111    3
145    3
135    3
      ..
182    1
156    1
59     1
212    1
170    1
Name: sex, Length: 244, dtype: int64

Copy to clipboard

### Extracting substring by position[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#extracting-substring-by-position "Link to this heading")

SAS extracts a substring from a string based on its position with the [SUBSTR](https://support.sas.com/documentation/cdl/en/imlug/66845/HTML/default/viewer.htm#imlug_langref_sect455.htm)
 function.

data \_null\_;
set tips;
put(substr(sex,1,1));
run;

Copy to clipboard

With pandas you can use `[]` notation to extract a substring from a string by position locations. Keep in mind that Python indexes are zero-based.

In \[1\]: tips\["sex"\].str\[0:1\]
Out\[1\]: 
67     F
92     F
111    F
145    F
135    F
      ..
182    M
156    M
59     M
212    M
170    M
Name: sex, Length: 244, dtype: str

Copy to clipboard

### Extracting nth word[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#extracting-nth-word "Link to this heading")

The SAS [SCAN](https://support.sas.com/documentation/cdl/en/lrdict/64316/HTML/default/viewer.htm#a000214639.htm)
 function returns the nth word from a string. The first argument is the string you want to parse and the second argument specifies which word you want to extract.

data firstlast;
input String $60.;
First\_Name = scan(string, 1);
Last\_Name = scan(string, -1);
datalines2;
John Smith;
Jane Cook;
;;;
run;

Copy to clipboard

The simplest way to extract words in pandas is to split the strings by spaces, then reference the word by index. Note there are more powerful approaches should you need them.

In \[1\]: firstlast \= pd.DataFrame({"String": \["John Smith", "Jane Cook"\]})

In \[2\]: firstlast\["First\_Name"\] \= firstlast\["String"\].str.split(" ", expand\=True)\[0\]

In \[3\]: firstlast\["Last\_Name"\] \= firstlast\["String"\].str.rsplit(" ", expand\=True)\[1\]

In \[4\]: firstlast
Out\[4\]: 
       String First\_Name Last\_Name
0  John Smith       John     Smith
1   Jane Cook       Jane      Cook

Copy to clipboard

### Changing case[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#changing-case "Link to this heading")

The SAS [UPCASE](https://support.sas.com/documentation/cdl/en/lrdict/64316/HTML/default/viewer.htm#a000245965.htm)
 [LOWCASE](https://support.sas.com/documentation/cdl/en/lrdict/64316/HTML/default/viewer.htm#a000245912.htm)
 and [PROPCASE](https://support.sas.com/documentation/cdl/en/lrdict/64316/HTML/default/a002598106.htm)
 functions change the case of the argument.

data firstlast;
input String $60.;
string\_up = UPCASE(string);
string\_low = LOWCASE(string);
string\_prop = PROPCASE(string);
datalines2;
John Smith;
Jane Cook;
;;;
run;

Copy to clipboard

The equivalent pandas methods are [`Series.str.upper()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.upper.html#pandas.Series.str.upper "pandas.Series.str.upper")
, [`Series.str.lower()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html#pandas.Series.str.lower "pandas.Series.str.lower")
, and [`Series.str.title()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.title.html#pandas.Series.str.title "pandas.Series.str.title")
.

In \[1\]: firstlast \= pd.DataFrame({"string": \["John Smith", "Jane Cook"\]})

In \[2\]: firstlast\["upper"\] \= firstlast\["string"\].str.upper()

In \[3\]: firstlast\["lower"\] \= firstlast\["string"\].str.lower()

In \[4\]: firstlast\["title"\] \= firstlast\["string"\].str.title()

In \[5\]: firstlast
Out\[5\]: 
       string       upper       lower       title
0  John Smith  JOHN SMITH  john smith  John Smith
1   Jane Cook   JANE COOK   jane cook   Jane Cook

Copy to clipboard

Merging[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#merging "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

The following tables will be used in the merge examples:

In \[1\]: df1 \= pd.DataFrame({"key": \["A", "B", "C", "D"\], "value": np.random.randn(4)})

In \[2\]: df1
Out\[2\]: 
  key     value
0   A  0.469112
1   B -0.282863
2   C -1.509059
3   D -1.135632

In \[3\]: df2 \= pd.DataFrame({"key": \["B", "D", "D", "E"\], "value": np.random.randn(4)})

In \[4\]: df2
Out\[4\]: 
  key     value
0   B  1.212112
1   D -0.173215
2   D  0.119209
3   E -1.044236

Copy to clipboard

In SAS, data must be explicitly sorted before merging. Different types of joins are accomplished using the `in=` dummy variables to track whether a match was found in one or both input frames.

proc sort data=df1;
    by key;
run;

proc sort data=df2;
    by key;
run;

data left\_join inner\_join right\_join outer\_join;
    merge df1(in\=a) df2(in\=b);

    if a and b then output inner\_join;
    if a then output left\_join;
    if b then output right\_join;
    if a or b then output outer\_join;
run;

Copy to clipboard

pandas DataFrames have a [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge "pandas.DataFrame.merge")
 method, which provides similar functionality. The data does not have to be sorted ahead of time, and different join types are accomplished via the `how` keyword.

In \[1\]: inner\_join \= df1.merge(df2, on\=\["key"\], how\="inner")

In \[2\]: inner\_join
Out\[2\]: 
  key   value\_x   value\_y
0   B -0.282863  1.212112
1   D -1.135632 -0.173215
2   D -1.135632  0.119209

In \[3\]: left\_join \= df1.merge(df2, on\=\["key"\], how\="left")

In \[4\]: left\_join
Out\[4\]: 
  key   value\_x   value\_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209

In \[5\]: right\_join \= df1.merge(df2, on\=\["key"\], how\="right")

In \[6\]: right\_join
Out\[6\]: 
  key   value\_x   value\_y
0   B -0.282863  1.212112
1   D -1.135632 -0.173215
2   D -1.135632  0.119209
3   E       NaN -1.044236

In \[7\]: outer\_join \= df1.merge(df2, on\=\["key"\], how\="outer")

In \[8\]: outer\_join
Out\[8\]: 
  key   value\_x   value\_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
5   E       NaN -1.044236

Copy to clipboard

Missing data[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#missing-data "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------------------

Both pandas and SAS have a representation for missing data.

pandas represents missing data with the special float value `NaN` (not a number). Many of the semantics are the same; for example missing data propagates through numeric operations, and is ignored by default for aggregations.

In \[1\]: outer\_join
Out\[1\]: 
  key   value\_x   value\_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
5   E       NaN -1.044236

In \[2\]: outer\_join\["value\_x"\] + outer\_join\["value\_y"\]
Out\[2\]: 
0         NaN
1    0.929249
2         NaN
3   -1.308847
4   -1.016424
5         NaN
dtype: float64

In \[3\]: outer\_join\["value\_x"\].sum()
Out\[3\]: np.float64(-3.5940742896293765)

Copy to clipboard

One difference is that missing data cannot be compared to its sentinel value. For example, in SAS you could do this to filter missing values.

data outer\_join\_nulls;
    set outer\_join;
    if value\_x = .;
run;

data outer\_join\_no\_nulls;
    set outer\_join;
    if value\_x ^= .;
run;

Copy to clipboard

In pandas, [`Series.isna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.isna.html#pandas.Series.isna "pandas.Series.isna")
 and [`Series.notna()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.notna.html#pandas.Series.notna "pandas.Series.notna")
 can be used to filter the rows.

In \[1\]: outer\_join\[outer\_join\["value\_x"\].isna()\]
Out\[1\]: 
  key  value\_x   value\_y
5   E      NaN -1.044236

In \[2\]: outer\_join\[outer\_join\["value\_x"\].notna()\]
Out\[2\]: 
  key   value\_x   value\_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209

Copy to clipboard

pandas provides [a variety of methods to work with missing data](https://pandas.pydata.org/docs/user_guide/missing_data.html#missing-data)
. Here are some examples:

### Drop rows with missing values[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#drop-rows-with-missing-values "Link to this heading")

In \[3\]: outer\_join.dropna()
Out\[3\]: 
  key   value\_x   value\_y
1   B -0.282863  1.212112
3   D -1.135632 -0.173215
4   D -1.135632  0.119209

Copy to clipboard

### Forward fill from previous rows[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#forward-fill-from-previous-rows "Link to this heading")

In \[4\]: outer\_join.ffill()
Out\[4\]: 
  key   value\_x   value\_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059  1.212112
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
5   E -1.135632 -1.044236

Copy to clipboard

### Replace missing values with a specified value[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#replace-missing-values-with-a-specified-value "Link to this heading")

Using the mean:

In \[5\]: outer\_join\["value\_x"\].fillna(outer\_join\["value\_x"\].mean())
Out\[5\]: 
0    0.469112
1   -0.282863
2   -1.509059
3   -1.135632
4   -1.135632
5   -0.718815
Name: value\_x, dtype: float64

Copy to clipboard

GroupBy[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#groupby "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

### Aggregation[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#aggregation "Link to this heading")

SAS’s `PROC SUMMARY` can be used to group by one or more key variables and compute aggregations on numeric columns.

proc summary data=tips nway;
    class sex smoker;
    var total\_bill tip;
    output out\=tips\_summed sum=;
run;

Copy to clipboard

pandas provides a flexible `groupby` mechanism that allows similar aggregations. See the [groupby documentation](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby)
 for more details and examples.

In \[1\]: tips\_summed \= tips.groupby(\["sex", "smoker"\])\[\["total\_bill", "tip"\]\].sum()

In \[2\]: tips\_summed
Out\[2\]: 
               total\_bill     tip
sex    smoker                    
Female No          869.68  149.77
       Yes         527.27   96.74
Male   No         1725.75  302.00
       Yes        1217.07  183.07

Copy to clipboard

### Transformation[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#transformation "Link to this heading")

In SAS, if the group aggregations need to be used with the original frame, it must be merged back together. For example, to subtract the mean for each observation by smoker group.

proc summary data=tips missing nway;
    class smoker;
    var total\_bill;
    output out\=smoker\_means mean(total\_bill)=group\_bill;
run;

proc sort data=tips;
    by smoker;
run;

data tips;
    merge tips(in\=a) smoker\_means(in\=b);
    by smoker;
    adj\_total\_bill = total\_bill - group\_bill;
    if a and b;
run;

Copy to clipboard

pandas provides a [Transformation](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-transform)
 mechanism that allows these type of operations to be succinctly expressed in one operation.

In \[1\]: gb \= tips.groupby("smoker")\["total\_bill"\]

In \[2\]: tips\["adj\_total\_bill"\] \= tips\["total\_bill"\] \- gb.transform("mean")

In \[3\]: tips
Out\[3\]: 
     total\_bill    tip     sex smoker   day    time  size  adj\_total\_bill
67         1.07   1.00  Female    Yes   Sat  Dinner     1      -17.686344
92         3.75   1.00  Female    Yes   Fri  Dinner     2      -15.006344
111        5.25   1.00  Female     No   Sat  Dinner     1      -11.938278
145        6.35   1.50  Female     No  Thur   Lunch     2      -10.838278
135        6.51   1.25  Female     No  Thur   Lunch     2      -10.678278
..          ...    ...     ...    ...   ...     ...   ...             ...
182       43.35   3.50    Male    Yes   Sun  Dinner     3       24.593656
156       46.17   5.00    Male     No   Sun  Dinner     6       28.981722
59        46.27   6.73    Male     No   Sat  Dinner     4       29.081722
212       46.33   9.00    Male     No   Sat  Dinner     4       29.141722
170       48.81  10.00    Male    Yes   Sat  Dinner     3       30.053656

\[244 rows x 8 columns\]

Copy to clipboard

### By group processing[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#by-group-processing "Link to this heading")

In addition to aggregation, pandas `groupby` can be used to replicate most other by group processing from SAS. For example, this `DATA` step reads the data by sex/smoker group and filters to the first entry for each.

proc sort data=tips;
   by sex smoker;
run;

data tips\_first;
    set tips;
    by sex smoker;
    if FIRST.sex or FIRST.smoker then output;
run;

Copy to clipboard

In pandas this would be written as:

In \[4\]: tips.groupby(\["sex", "smoker"\]).first()
Out\[4\]: 
               total\_bill   tip   day    time  size  adj\_total\_bill
sex    smoker                                                      
Female No            5.25  1.00   Sat  Dinner     1      -11.938278
       Yes           1.07  1.00   Sat  Dinner     1      -17.686344
Male   No            5.51  2.00  Thur   Lunch     2      -11.678278
       Yes           5.25  5.15   Sun  Dinner     2      -13.506344

Copy to clipboard

Other considerations[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#other-considerations "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------

### Disk vs memory[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#disk-vs-memory "Link to this heading")

pandas operates exclusively in memory, where a SAS data set exists on disk. This means that the size of data able to be loaded in pandas is limited by your machine’s memory, but also that the operations on that data may be faster.

If out of core processing is needed, one possibility is the [dask.dataframe](https://docs.dask.org/en/latest/dataframe.html)
 library (currently in development) which provides a subset of pandas functionality for an on-disk `DataFrame`

### Data interop[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sas.html#data-interop "Link to this heading")

pandas provides a [`read_sas()`](https://pandas.pydata.org/docs/reference/api/pandas.read_sas.html#pandas.read_sas "pandas.read_sas")
 method that can read SAS data saved in the XPORT or SAS7BDAT binary format.

libname xportout xport 'transport-file.xpt';
data xportout.tips;
    set tips(rename\=(total\_bill=tbill));
    \* xport variable names limited to 6 characters;
run;

Copy to clipboard

df \= pd.read\_sas("transport-file.xpt")
df \= pd.read\_sas("binary-file.sas7bdat")

Copy to clipboard

You can also specify the file format directly. By default, pandas will try to infer the file format based on its extension.

df \= pd.read\_sas("transport-file.xpt", format\="xport")
df \= pd.read\_sas("binary-file.sas7bdat", format\="sas7bdat")

Copy to clipboard

XPORT is a relatively limited format and the parsing of it is not as optimized as some of the other pandas readers. An alternative way to interop data between SAS and pandas is to serialize to csv.

\# version 0.17, 10M rows

In \[8\]: %time df = pd.read\_sas('big.xpt')
Wall time: 14.6 s

In \[9\]: %time df = pd.read\_csv('big.csv')
Wall time: 4.86 s

Copy to clipboard

On this page