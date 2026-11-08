[Skip to main content](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/getting_started/comparison/comparison_with_spreadsheets.html)
[3.1 (stable)](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/getting_started/comparison/comparison_with_spreadsheets.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/comparison/comparison_with_spreadsheets.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/comparison/comparison_with_spreadsheets.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/getting_started/comparison/comparison_with_spreadsheets.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/getting_started/comparison/comparison_with_spreadsheets.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/comparison/comparison_with_spreadsheets.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/getting_started/comparison/comparison_with_spreadsheets.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/comparison/comparison_with_spreadsheets.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/getting_started/comparison/comparison_with_spreadsheets.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/comparison/comparison_with_spreadsheets.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/comparison/comparison_with_spreadsheets.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Comparison with spreadsheets[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#comparison-with-spreadsheets "Link to this heading")

=================================================================================================================================================================================

Since many potential pandas users have some familiarity with spreadsheet programs like [Excel](https://support.microsoft.com/en-us/excel)
, this page is meant to provide some examples of how various spreadsheet operations would be performed using pandas. This page will use terminology and link to documentation for Excel, but much will be the same/similar in [Google Sheets](https://support.google.com/a/users/answer/9282959)
, [LibreOffice Calc](https://help.libreoffice.org/latest/en-US/text/scalc/main0000.html?DbPAR=CALC)
, [Apple Numbers](https://www.apple.com/numbers/compatibility/)
, and other Excel-compatible spreadsheet software.

If you’re new to pandas, you might want to first read through [10 Minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html#min)
 to familiarize yourself with the library.

As is customary, we import pandas and NumPy as follows:

In \[1\]: import pandas as pd

In \[2\]: import numpy as np

Copy to clipboard

Data structures[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#data-structures "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

### General terminology translation[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#general-terminology-translation "Link to this heading")

 
| pandas | Excel |
| --- | --- |
| `DataFrame` | worksheet |
| `Series` | column |
| `Index` | row headings |
| row | row |
| `NaN` | empty cell |

### `DataFrame`[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#dataframe "Link to this heading")

A `DataFrame` in pandas is analogous to an Excel worksheet. While an Excel workbook can contain multiple worksheets, pandas `DataFrame`s exist independently.

### `Series`[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#series "Link to this heading")

A `Series` is the data structure that represents one column of a `DataFrame`. Working with a `Series` is analogous to referencing a column of a spreadsheet.

### `Index`[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#index "Link to this heading")

Every `DataFrame` and `Series` has an `Index`, which are labels on the _rows_ of the data. In pandas, if no index is specified, a [`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")
 is used by default (first row = 0, second row = 1, and so on), analogous to row headings/numbers in spreadsheets.

In pandas, indexes can be set to one (or multiple) unique values, which is like having a column that is used as the row identifier in a worksheet. Unlike most spreadsheets, these `Index` values can actually be used to reference the rows. (Note that [this can be done in Excel with structured references](https://support.microsoft.com/en-us/office/using-structured-references-with-excel-tables-f5ed2452-2337-4f71-bed3-c8ae6d2b276e)
.) For example, in spreadsheets, you would reference the first row as `A1:Z1`, while in pandas you could use `populations.loc['Chicago']`.

Index values are also persistent, so if you re-order the rows in a `DataFrame`, the label for a particular row don’t change.

See the [indexing documentation](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing)
 for much more on how to use an `Index` effectively.

### Copies vs. in place operations[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#copies-vs-in-place-operations "Link to this heading")

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

Data input / output[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#data-input-output "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------

### Constructing a DataFrame from values[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#constructing-a-dataframe-from-values "Link to this heading")

In a spreadsheet, [values can be typed directly into cells](https://support.microsoft.com/en-us/office/enter-data-manually-in-worksheet-cells-c798181d-d75a-41b1-92ad-6c0800f80038)
.

A pandas `DataFrame` can be constructed in many different ways, but for a small number of values, it is often convenient to specify it as a Python dictionary, where the keys are the column names and the values are the data.

In \[3\]: df \= pd.DataFrame({"x": \[1, 3, 5\], "y": \[2, 4, 6\]})

In \[4\]: df
Out\[4\]: 
   x  y
0  1  2
1  3  4
2  5  6

Copy to clipboard

### Reading external data[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#reading-external-data "Link to this heading")

Both [Excel](https://support.microsoft.com/en-us/office/import-data-from-data-sources-power-query-be4330b3-5356-486c-a168-b68e9e616f5a)
 and [pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/02_read_write.html#min-tut-02-read-write)
 can import data from various sources in various formats.

#### CSV[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#csv "Link to this heading")

Let’s load and display the [tips](https://github.com/pandas-dev/pandas/blob/main/pandas/tests/io/data/csv/tips.csv)
 dataset from the pandas tests, which is a CSV file. In Excel, you would download and then [open the CSV](https://support.microsoft.com/en-us/office/import-or-export-text-txt-or-csv-files-5250ac4c-663c-47ce-937b-339e391393ba)
. In pandas, you pass the URL or local path of the CSV file to [`read_csv()`](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html#pandas.read_csv "pandas.read_csv")
:

In \[5\]: url \= (
   ...:    "https://raw.githubusercontent.com/pandas-dev"
   ...:    "/pandas/main/pandas/tests/io/data/csv/tips.csv"
   ...: )
   ...: 

In \[6\]: tips \= pd.read\_csv(url)

In \[7\]: tips
Out\[7\]: 
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

Like [Excel’s Text Import Wizard](https://support.microsoft.com/en-us/office/text-import-wizard-c5b02af6-fda1-4440-899f-f78bafe41857)
, `read_csv` can take a number of parameters to specify how the data should be parsed. For example, if the data was instead tab delimited, and did not have column names, the pandas command would be:

tips \= pd.read\_csv("tips.csv", sep\="\\t", header\=None)

\# alternatively, read\_table is an alias to read\_csv with tab delimiter
tips \= pd.read\_table("tips.csv", header\=None)

Copy to clipboard

#### Excel files[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#excel-files "Link to this heading")

Excel opens [various Excel file formats](https://support.microsoft.com/en-us/office/file-formats-that-are-supported-in-excel-0943ff2c-6014-4e8d-aaea-b83d51d46247)
 by double-clicking them, or using [the Open menu](https://support.microsoft.com/en-us/office/open-files-from-the-file-menu-97f087d8-3136-4485-8e86-c5b12a8c4176)
. In pandas, you use [special methods for reading and writing from/to Excel files](https://pandas.pydata.org/docs/user_guide/io.html#io-excel)
.

Let’s first [create a new Excel file](https://pandas.pydata.org/docs/user_guide/io.html#io-excel-writer)
 based on the `tips` dataframe in the above example:

tips.to\_excel("./tips.xlsx")

Copy to clipboard

Should you wish to subsequently access the data in the `tips.xlsx` file, you can read it into your module using

tips\_df \= pd.read\_excel("./tips.xlsx", index\_col\=0)

Copy to clipboard

You have just read in an Excel file using pandas!

### Limiting output[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#limiting-output "Link to this heading")

Spreadsheet programs will only show one screenful of data at a time and then allow you to scroll, so there isn’t really a need to limit output. In pandas, you’ll need to put a little more thought into controlling how your `DataFrame`s are displayed.

By default, pandas will truncate output of large `DataFrame`s to show the first and last rows. This can be overridden by [changing the pandas options](https://pandas.pydata.org/docs/user_guide/options.html#options)
, or using [`DataFrame.head()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html#pandas.DataFrame.head "pandas.DataFrame.head")
 or [`DataFrame.tail()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.tail.html#pandas.DataFrame.tail "pandas.DataFrame.tail")
.

In \[8\]: tips.head(5)
Out\[8\]: 
   total\_bill   tip     sex smoker  day    time  size
0       16.99  1.01  Female     No  Sun  Dinner     2
1       10.34  1.66    Male     No  Sun  Dinner     3
2       21.01  3.50    Male     No  Sun  Dinner     3
3       23.68  3.31    Male     No  Sun  Dinner     2
4       24.59  3.61  Female     No  Sun  Dinner     4

Copy to clipboard

### Exporting data[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#exporting-data "Link to this heading")

By default, desktop spreadsheet software will save to its respective file format (`.xlsx`, `.ods`, etc). You can, however, [save to other file formats](https://support.microsoft.com/en-us/office/save-a-workbook-in-another-file-format-6a16c862-4a36-48f9-a300-c2ca0065286e)
.

[pandas can create Excel files](https://pandas.pydata.org/docs/user_guide/io.html#io-excel-writer)
, [CSV](https://pandas.pydata.org/docs/user_guide/io.html#io-store-in-csv)
, or [a number of other formats](https://pandas.pydata.org/docs/user_guide/io.html#io)
.

Data operations[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#data-operations "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

### Operations on columns[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#operations-on-columns "Link to this heading")

In spreadsheets, [formulas](https://support.microsoft.com/en-us/office/overview-of-formulas-in-excel-ecfdc708-9162-49e8-b993-c311f47ca173)
 are often created in individual cells and then [dragged](https://support.microsoft.com/en-us/office/copy-a-formula-by-dragging-the-fill-handle-in-excel-for-mac-dd928259-622b-473f-9a33-83aa1a63e218)
 into other cells to compute them for other columns. In pandas, you’re able to do operations on whole columns directly.

pandas provides vectorized operations by specifying the individual `Series` in the `DataFrame`. New columns can be assigned in the same way. The [`DataFrame.drop()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop.html#pandas.DataFrame.drop "pandas.DataFrame.drop")
 method drops a column from the `DataFrame`.

In \[9\]: tips\["total\_bill"\] \= tips\["total\_bill"\] \- 2

In \[10\]: tips\["new\_bill"\] \= tips\["total\_bill"\] / 2

In \[11\]: tips
Out\[11\]: 
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

In \[12\]: tips \= tips.drop("new\_bill", axis\=1)

Copy to clipboard

Note that we aren’t having to tell it to do that subtraction cell-by-cell — pandas handles that for us. See [how to create new columns derived from existing columns](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html#min-tut-05-columns)
.

### Filtering[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#filtering "Link to this heading")

[In Excel, filtering is done through a graphical menu.](https://support.microsoft.com/en-us/office/filter-data-in-a-range-or-table-01832226-31b5-4568-8806-38c37dcc180e)

![Screenshot showing filtering of the total_bill column to values greater than 10](https://pandas.pydata.org/docs/_images/filter.png)

DataFrames can be filtered in multiple ways; the most intuitive of which is using [boolean indexing](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-boolean)
.

In \[13\]: tips\[tips\["total\_bill"\] \> 10\]
Out\[13\]: 
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

In \[14\]: is\_dinner \= tips\["time"\] \== "Dinner"

In \[15\]: is\_dinner
Out\[15\]: 
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

In \[16\]: is\_dinner.value\_counts()
Out\[16\]: 
time
True     176
False     68
Name: count, dtype: int64

In \[17\]: tips\[is\_dinner\]
Out\[17\]: 
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

### If/then logic[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#if-then-logic "Link to this heading")

Let’s say we want to make a `bucket` column with values of `low` and `high`, based on whether the `total_bill` is less or more than $10.

In spreadsheets, logical comparison can be done with [conditional formulas](https://support.microsoft.com/en-us/office/create-conditional-formulas-ca916c57-abd8-4b44-997c-c309b7307831)
. We’d use a formula of `=IF(A2 < 10, "low", "high")`, dragged to all cells in a new `bucket` column.

![Screenshot showing the formula from above in a bucket column of the tips spreadsheet](https://pandas.pydata.org/docs/_images/conditional.png)

The same operation in pandas can be accomplished using the `where` method from `numpy`.

In \[18\]: tips\["bucket"\] \= np.where(tips\["total\_bill"\] < 10, "low", "high")

In \[19\]: tips
Out\[19\]: 
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

### Date functionality[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#date-functionality "Link to this heading")

_This section will refer to “dates”, but timestamps are handled similarly._

We can think of date functionality in two parts: parsing, and output. In spreadsheets, date values are generally parsed automatically, though there is a [DATEVALUE](https://support.microsoft.com/en-us/office/datevalue-function-df8b07d4-7761-4a93-bc33-b7471bbff252)
 function if you need it. In pandas, you need to explicitly convert plain text to datetime objects, either [while reading from a CSV](https://pandas.pydata.org/docs/user_guide/io.html#io-read-csv-table-datetime)
 or [once in a DataFrame](https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html#min-tut-09-timeseries-properties)
.

Once parsed, spreadsheets display the dates in a default format, though [the format can be changed](https://support.microsoft.com/en-us/office/format-a-date-the-way-you-want-8e10019e-d5d8-47a1-ba95-db95123d273e)
. In pandas, you’ll generally want to keep dates as `datetime` objects while you’re doing calculations with them. Outputting _parts_ of dates (such as the year) is done through [date functions](https://support.microsoft.com/en-us/office/date-and-time-functions-reference-fd1b5961-c1ae-4677-be58-074152f97b81)
 in spreadsheets, and [datetime properties](https://pandas.pydata.org/docs/getting_started/intro_tutorials/09_timeseries.html#min-tut-09-timeseries-properties)
 in pandas.

Given `date1` and `date2` in columns `A` and `B` of a spreadsheet, you might have these formulas:

| column | formula |
| --- | --- |
| `date1_year` | `=YEAR(A2)` |
| `date2_month` | `=MONTH(B2)` |
| `date1_next` | `=DATE(YEAR(A2),MONTH(A2)+1,1)` |
| `months_between` | `=DATEDIF(A2,B2,"M")` |

The equivalent pandas operations are shown below.

In \[20\]: tips\["date1"\] \= pd.Timestamp("2013-01-15")

In \[21\]: tips\["date2"\] \= pd.Timestamp("2015-02-15")

In \[22\]: tips\["date1\_year"\] \= tips\["date1"\].dt.year

In \[23\]: tips\["date2\_month"\] \= tips\["date2"\].dt.month

In \[24\]: tips\["date1\_next"\] \= tips\["date1"\] + pd.offsets.MonthBegin()

In \[25\]: tips\["months\_between"\] \= tips\["date2"\].dt.to\_period("M") \- tips\[\
   ....:    "date1"\
   ....: \].dt.to\_period("M")
   ....: 

In \[26\]: tips\[\
   ....:    \["date1", "date2", "date1\_year", "date2\_month", "date1\_next", "months\_between"\]\
   ....: \]
   ....: 
Out\[26\]: 
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

See [Time series / date functionality](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries)
 for more details.

### Selection of columns[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#selection-of-columns "Link to this heading")

In spreadsheets, you can select columns you want by:

*   [Hiding columns](https://support.microsoft.com/en-us/office/hide-or-show-rows-or-columns-659c2cad-802e-44ee-a614-dde8443579f8)
    
*   [Deleting columns](https://support.microsoft.com/en-us/office/insert-or-delete-rows-and-columns-6f40e6e4-85af-45e0-b39d-65dd504a3246)
    
*   [Referencing a range](https://support.microsoft.com/en-us/office/create-or-change-a-cell-reference-c7b8b95d-c594-4488-947e-c835903cebaa)
     from one worksheet into another
    

Since spreadsheet columns are typically [named in a header row](https://support.microsoft.com/en-us/office/turn-excel-table-headers-on-or-off-c91d1742-312c-4480-820f-cf4b534c8b3b)
, renaming a column is simply a matter of changing the text in that first cell.

The same operations are expressed in pandas below.

#### Keep certain columns[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#keep-certain-columns "Link to this heading")

In \[27\]: tips\[\["sex", "total\_bill", "tip"\]\]
Out\[27\]: 
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

#### Drop a column[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#drop-a-column "Link to this heading")

In \[28\]: tips.drop("sex", axis\=1)
Out\[28\]: 
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

#### Rename a column[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#rename-a-column "Link to this heading")

In \[29\]: tips.rename(columns\={"total\_bill": "total\_bill\_2"})
Out\[29\]: 
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

### Sorting by values[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#sorting-by-values "Link to this heading")

Sorting in spreadsheets is accomplished via [the sort dialog](https://support.microsoft.com/en-us/office/sort-data-in-a-range-or-table-62d0b95d-2a90-4610-a6ae-2e545c4a4654)
.

![Screenshot of dialog from Excel showing sorting by the sex then total_bill columns](https://pandas.pydata.org/docs/_images/sort.png)

pandas has a [`DataFrame.sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")
 method, which takes a list of columns to sort by.

In \[30\]: tips \= tips.sort\_values(\["sex", "total\_bill"\])

In \[31\]: tips
Out\[31\]: 
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

String processing[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#string-processing "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------

### Finding length of string[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#finding-length-of-string "Link to this heading")

In spreadsheets, the number of characters in text can be found with the [LEN](https://support.microsoft.com/en-us/office/len-lenb-functions-29236f94-cedc-429d-affd-b5e33d2c67cb)
 function. This can be used with the [TRIM](https://support.microsoft.com/en-us/office/trim-function-410388fa-c5df-49c6-b16c-9e5630b479f9)
 function to remove extra whitespace.

\=LEN(TRIM(A2))

Copy to clipboard

You can find the length of a character string with [`Series.str.len()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.len.html#pandas.Series.str.len "pandas.Series.str.len")
. In Python 3, all strings are Unicode strings. `len` includes trailing blanks. Use `len` and `rstrip` to exclude trailing blanks.

In \[32\]: tips\["time"\].str.len()
Out\[32\]: 
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

In \[33\]: tips\["time"\].str.rstrip().str.len()
Out\[33\]: 
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

Note this will still include multiple spaces within the string, so isn’t 100% equivalent.

### Finding position of substring[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#finding-position-of-substring "Link to this heading")

The [FIND](https://support.microsoft.com/en-us/office/find-findb-functions-c7912941-af2a-4bdf-a553-d0d89b0a0628)
 spreadsheet function returns the position of a substring, with the first character being `1`.

![Screenshot of FIND formula being used in Excel](https://pandas.pydata.org/docs/_images/sort.png)

You can find the position of a character in a column of strings with the [`Series.str.find()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.find.html#pandas.Series.str.find "pandas.Series.str.find")
 method. `find` searches for the first position of the substring. If the substring is found, the method returns its position. If not found, it returns `-1`. Keep in mind that Python indexes are zero-based.

In \[34\]: tips\["sex"\].str.find("ale")
Out\[34\]: 
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

### Extracting substring by position[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#extracting-substring-by-position "Link to this heading")

Spreadsheets have a [MID](https://support.microsoft.com/en-us/office/mid-midb-functions-d5f9e25c-d7d6-472e-b568-4ecb12433028)
 formula for extracting a substring from a given position. To get the first character:

\=MID(A2,1,1)

Copy to clipboard

With pandas you can use `[]` notation to extract a substring from a string by position locations. Keep in mind that Python indexes are zero-based.

In \[35\]: tips\["sex"\].str\[0:1\]
Out\[35\]: 
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

### Extracting nth word[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#extracting-nth-word "Link to this heading")

In Excel, you might use the [Text to Columns Wizard](https://support.microsoft.com/en-us/office/split-text-into-different-columns-with-the-convert-text-to-columns-wizard-30b14928-5550-41f5-97ca-7a3e9c363ed7)
 for splitting text and retrieving a specific column. (Note [it’s possible to do so through a formula as well](https://exceljet.net/formula/extract-nth-word-from-text-string)
.)

The simplest way to extract words in pandas is to split the strings by spaces, then reference the word by index. Note there are more powerful approaches should you need them.

In \[36\]: firstlast \= pd.DataFrame({"String": \["John Smith", "Jane Cook"\]})

In \[37\]: firstlast\["First\_Name"\] \= firstlast\["String"\].str.split(" ", expand\=True)\[0\]

In \[38\]: firstlast\["Last\_Name"\] \= firstlast\["String"\].str.rsplit(" ", expand\=True)\[1\]

In \[39\]: firstlast
Out\[39\]: 
       String First\_Name Last\_Name
0  John Smith       John     Smith
1   Jane Cook       Jane      Cook

Copy to clipboard

### Changing case[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#changing-case "Link to this heading")

Spreadsheets provide [UPPER, LOWER, and PROPER functions](https://support.microsoft.com/en-us/office/change-the-case-of-text-01481046-0fa7-4f3b-a693-496795a7a44d)
 for converting text to upper, lower, and title case, respectively.

The equivalent pandas methods are [`Series.str.upper()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.upper.html#pandas.Series.str.upper "pandas.Series.str.upper")
, [`Series.str.lower()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.lower.html#pandas.Series.str.lower "pandas.Series.str.lower")
, and [`Series.str.title()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.title.html#pandas.Series.str.title "pandas.Series.str.title")
.

In \[40\]: firstlast \= pd.DataFrame({"string": \["John Smith", "Jane Cook"\]})

In \[41\]: firstlast\["upper"\] \= firstlast\["string"\].str.upper()

In \[42\]: firstlast\["lower"\] \= firstlast\["string"\].str.lower()

In \[43\]: firstlast\["title"\] \= firstlast\["string"\].str.title()

In \[44\]: firstlast
Out\[44\]: 
       string       upper       lower       title
0  John Smith  JOHN SMITH  john smith  John Smith
1   Jane Cook   JANE COOK   jane cook   Jane Cook

Copy to clipboard

Merging[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#merging "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------

The following tables will be used in the merge examples:

In \[45\]: df1 \= pd.DataFrame({"key": \["A", "B", "C", "D"\], "value": np.random.randn(4)})

In \[46\]: df1
Out\[46\]: 
  key     value
0   A  0.469112
1   B -0.282863
2   C -1.509059
3   D -1.135632

In \[47\]: df2 \= pd.DataFrame({"key": \["B", "D", "D", "E"\], "value": np.random.randn(4)})

In \[48\]: df2
Out\[48\]: 
  key     value
0   B  1.212112
1   D -0.173215
2   D  0.119209
3   E -1.044236

Copy to clipboard

In Excel, there are [merging of tables can be done through a VLOOKUP](https://support.microsoft.com/en-us/office/how-can-i-merge-two-or-more-tables-c80a9fce-c1ab-4425-bb96-497dd906d656)
.

![Screenshot showing a VLOOKUP formula between two tables in Excel, with some values being filled in and others with "#N/A"](https://pandas.pydata.org/docs/_images/vlookup.png)

pandas DataFrames have a [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html#pandas.DataFrame.merge "pandas.DataFrame.merge")
 method, which provides similar functionality. The data does not have to be sorted ahead of time, and different join types are accomplished via the `how` keyword.

In \[49\]: inner\_join \= df1.merge(df2, on\=\["key"\], how\="inner")

In \[50\]: inner\_join
Out\[50\]: 
  key   value\_x   value\_y
0   B -0.282863  1.212112
1   D -1.135632 -0.173215
2   D -1.135632  0.119209

In \[51\]: left\_join \= df1.merge(df2, on\=\["key"\], how\="left")

In \[52\]: left\_join
Out\[52\]: 
  key   value\_x   value\_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209

In \[53\]: right\_join \= df1.merge(df2, on\=\["key"\], how\="right")

In \[54\]: right\_join
Out\[54\]: 
  key   value\_x   value\_y
0   B -0.282863  1.212112
1   D -1.135632 -0.173215
2   D -1.135632  0.119209
3   E       NaN -1.044236

In \[55\]: outer\_join \= df1.merge(df2, on\=\["key"\], how\="outer")

In \[56\]: outer\_join
Out\[56\]: 
  key   value\_x   value\_y
0   A  0.469112       NaN
1   B -0.282863  1.212112
2   C -1.509059       NaN
3   D -1.135632 -0.173215
4   D -1.135632  0.119209
5   E       NaN -1.044236

Copy to clipboard

`merge` has a number of advantages over `VLOOKUP`:

*   The lookup value doesn’t need to be the first column of the lookup table
    
*   If multiple rows are matched, there will be one row for each match, instead of just the first
    
*   It will include all columns from the lookup table, instead of just a single specified column
    
*   It supports [more complex join operations](https://pandas.pydata.org/docs/user_guide/merging.html#merging-join)
    

Other considerations[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#other-considerations "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

### Fill Handle[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#fill-handle "Link to this heading")

Create a series of numbers following a set pattern in a certain set of cells. In a spreadsheet, this would be done by shift+drag after entering the first number or by entering the first two or three values and then dragging.

This can be achieved by creating a series and assigning it to the desired cells.

In \[57\]: df \= pd.DataFrame({"AAA": \[1\] \* 8, "BBB": list(range(0, 8))})

In \[58\]: df
Out\[58\]: 
   AAA  BBB
0    1    0
1    1    1
2    1    2
3    1    3
4    1    4
5    1    5
6    1    6
7    1    7

In \[59\]: series \= list(range(1, 5))

In \[60\]: series
Out\[60\]: \[1, 2, 3, 4\]

In \[61\]: df.loc\[2:5, "AAA"\] \= series

In \[62\]: df
Out\[62\]: 
   AAA  BBB
0    1    0
1    1    1
2    1    2
3    2    3
4    3    4
5    4    5
6    1    6
7    1    7

Copy to clipboard

### Drop Duplicates[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#drop-duplicates "Link to this heading")

Excel has built-in functionality for [removing duplicate values](https://support.microsoft.com/en-us/office/find-and-remove-duplicates-00e35bea-b46a-4d5d-b28e-66a552dc138d)
. This is supported in pandas via [`drop_duplicates()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html#pandas.DataFrame.drop_duplicates "pandas.DataFrame.drop_duplicates")
.

In \[63\]: df \= pd.DataFrame(
   ....:    {
   ....:        "class": \["A", "A", "A", "B", "C", "D"\],
   ....:        "student\_count": \[42, 35, 42, 50, 47, 45\],
   ....:        "all\_pass": \["Yes", "Yes", "Yes", "No", "No", "Yes"\],
   ....:    }
   ....: )
   ....: 

In \[64\]: df.drop\_duplicates()
Out\[64\]: 
  class  student\_count all\_pass
0     A             42      Yes
1     A             35      Yes
3     B             50       No
4     C             47       No
5     D             45      Yes

In \[65\]: df.drop\_duplicates(\["class", "student\_count"\])
Out\[65\]: 
  class  student\_count all\_pass
0     A             42      Yes
1     A             35      Yes
3     B             50       No
4     C             47       No
5     D             45      Yes

Copy to clipboard

### Pivot Tables[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#pivot-tables "Link to this heading")

[PivotTables](https://support.microsoft.com/en-us/office/create-a-pivottable-to-analyze-worksheet-data-a9a84538-bfe9-40a9-a8e9-f99134456576)
 from spreadsheets can be replicated in pandas through [Reshaping and pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping)
. Using the `tips` dataset again, let’s find the average gratuity by size of the party and sex of the server.

In Excel, we use the following configuration for the PivotTable:

![Screenshot showing a PivotTable in Excel, using sex as the column, size as the rows, then average tip as the values](https://pandas.pydata.org/docs/_images/pivot.png)

The equivalent in pandas:

In \[66\]: pd.pivot\_table(
   ....:    tips, values\="tip", index\=\["size"\], columns\=\["sex"\], aggfunc\=np.average
   ....: )
   ....: 
Out\[66\]: 
sex     Female      Male
size                    
1     1.276667  1.920000
2     2.528448  2.614184
3     3.250000  3.476667
4     4.021111  4.172143
5     5.140000  3.750000
6     4.600000  5.850000

Copy to clipboard

### Adding a row[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#adding-a-row "Link to this heading")

Assuming we are using a [`RangeIndex`](https://pandas.pydata.org/docs/reference/api/pandas.RangeIndex.html#pandas.RangeIndex "pandas.RangeIndex")
 (numbered `0`, `1`, etc.), we can use [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat "pandas.concat")
 to add a row to the bottom of a `DataFrame`.

In \[67\]: df
Out\[67\]: 
  class  student\_count all\_pass
0     A             42      Yes
1     A             35      Yes
2     A             42      Yes
3     B             50       No
4     C             47       No
5     D             45      Yes

In \[68\]: new\_row \= pd.DataFrame(\[\["E", 51, True\]\],
   ....:                       columns\=\["class", "student\_count", "all\_pass"\])
   ....: 

In \[69\]: pd.concat(\[df, new\_row\])
Out\[69\]: 
  class  student\_count all\_pass
0     A             42      Yes
1     A             35      Yes
2     A             42      Yes
3     B             50       No
4     C             47       No
5     D             45      Yes
0     E             51     True

Copy to clipboard

### Find and Replace[#](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_spreadsheets.html#find-and-replace "Link to this heading")

[Excel’s Find dialog](https://support.microsoft.com/en-us/office/find-or-replace-text-and-numbers-on-a-worksheet-0e304ca5-ecef-4808-b90f-fdb42f892e90)
 takes you to cells that match, one by one. In pandas, this operation is generally done for an entire column or `DataFrame` at once through [conditional expressions](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#min-tut-03-subset-rows-and-columns)
.

In \[70\]: tips
Out\[70\]: 
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

In \[71\]: tips \== "Sun"
Out\[71\]: 
     total\_bill    tip    sex  smoker    day   time   size
67        False  False  False   False  False  False  False
92        False  False  False   False  False  False  False
111       False  False  False   False  False  False  False
145       False  False  False   False  False  False  False
135       False  False  False   False  False  False  False
..          ...    ...    ...     ...    ...    ...    ...
182       False  False  False   False   True  False  False
156       False  False  False   False   True  False  False
59        False  False  False   False  False  False  False
212       False  False  False   False  False  False  False
170       False  False  False   False  False  False  False

\[244 rows x 7 columns\]

In \[72\]: tips\["day"\].str.contains("S")
Out\[72\]: 
67      True
92     False
111     True
145    False
135    False
       ...  
182     True
156     True
59      True
212     True
170     True
Name: day, Length: 244, dtype: bool

Copy to clipboard

pandas’ [`replace()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html#pandas.DataFrame.replace "pandas.DataFrame.replace")
 is comparable to Excel’s `Replace All`.

In \[73\]: tips.replace("Thu", "Thursday")
Out\[73\]: 
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

On this page