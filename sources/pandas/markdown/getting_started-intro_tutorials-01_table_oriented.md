[Skip to main content](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/01_table_oriented.html)
[3.1 (stable)](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/getting_started/intro_tutorials/01_table_oriented.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/01_table_oriented.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/intro_tutorials/01_table_oriented.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/getting_started/intro_tutorials/01_table_oriented.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/getting_started/intro_tutorials/01_table_oriented.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/intro_tutorials/01_table_oriented.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/getting_started/intro_tutorials/01_table_oriented.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/intro_tutorials/01_table_oriented.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/getting_started/intro_tutorials/01_table_oriented.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/intro_tutorials/01_table_oriented.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/intro_tutorials/01_table_oriented.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

What kind of data does pandas handle?[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#what-kind-of-data-does-pandas-handle "Link to this heading")

============================================================================================================================================================================================

*   I want to start using pandas
    
    In \[1\]: import pandas as pd
    
    Copy to clipboard
    
    To load the pandas package and start working with it, import the package. The community agreed alias for pandas is `pd`, so loading pandas as `pd` is assumed standard practice for all of the pandas documentation.
    

pandas data table representation[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#pandas-data-table-representation "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![../../_images/01_table_dataframe.svg](https://pandas.pydata.org/docs/_images/01_table_dataframe.svg)

*   I want to store passenger data of the Titanic. For a number of passengers, I know the name (characters), age (integers) and sex (male/female) data.
    
    In \[2\]: df \= pd.DataFrame(
       ...:    {
       ...:        "Name": \[\
       ...:            "Braund, Mr. Owen Harris",\
       ...:            "Allen, Mr. William Henry",\
       ...:            "Bonnell, Miss Elizabeth",\
       ...:        \],
       ...:        "Age": \[22, 35, 58\],
       ...:        "Sex": \["male", "male", "female"\],
       ...:    }
       ...: )
       ...: 
    
    In \[3\]: df
    Out\[3\]: 
                           Name  Age     Sex
    0   Braund, Mr. Owen Harris   22    male
    1  Allen, Mr. William Henry   35    male
    2   Bonnell, Miss Elizabeth   58  female
    
    Copy to clipboard
    
    To manually store data in a table, create a `DataFrame`. When using a Python dictionary of lists, the dictionary keys will be used as column headers and the values in each list as columns of the `DataFrame`.
    

A [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 is a 2-dimensional data structure that can store data of different types (including characters, integers, floating point values, categorical data and more) in columns. It is similar to a spreadsheet, a SQL table or the `data.frame` in [R](https://www.r-project.org/)
.

*   The table has 3 columns, each of them with a column label. The column labels are respectively `Name`, `Age` and `Sex`.
    
*   The column `Name` consists of textual data with each value a string, the column `Age` are numbers and the column `Sex` is textual data.
    
*   The index labels each row. By default, this is a sequence of integers starting at 0.
    

In spreadsheet software, the table representation of our data would look very similar:

![../../_images/01_table_spreadsheet.png](https://pandas.pydata.org/docs/_images/01_table_spreadsheet.png)

Each column in a `DataFrame` is a `Series`[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#each-column-in-a-dataframe-is-a-series "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![../../_images/01_table_series.svg](https://pandas.pydata.org/docs/_images/01_table_series.svg)

*   I’m just interested in working with the data in the column `Age`
    
    In \[4\]: df\["Age"\]
    Out\[4\]: 
    0    22
    1    35
    2    58
    Name: Age, dtype: int64
    
    Copy to clipboard
    
    When selecting a single column of a pandas [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
    , the result is a pandas [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
    . To select the column, use the column label in between square brackets `[]`.
    

Note

If you are familiar with Python [dictionaries](https://docs.python.org/3/tutorial/datastructures.html#tut-dictionaries "(in Python v3.15)")
, the selection of a single column is very similar to the selection of dictionary values based on the key.

You can create a `Series` from scratch as well:

In \[5\]: ages \= pd.Series(\[22, 35, 58\], name\="Age")

In \[6\]: ages
Out\[6\]: 
0    22
1    35
2    58
Name: Age, dtype: int64

Copy to clipboard

A pandas `Series` has no column labels, as it is just a single column of a `DataFrame`. A Series does have row labels.

Do something with a DataFrame or Series[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#do-something-with-a-dataframe-or-series "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

*   I want to know the maximum Age of the passengers
    
    We can do this on the `DataFrame` by selecting the `Age` column and applying `max()`:
    
    In \[7\]: df\["Age"\].max()
    Out\[7\]: 58
    
    Copy to clipboard
    
    Or to the `Series`:
    
    In \[8\]: ages.max()
    Out\[8\]: 58
    
    Copy to clipboard
    

As illustrated by the `max()` method, you can _do_ things with a `DataFrame` or `Series`. pandas provides a lot of functionalities, each of them a _method_ you can apply to a `DataFrame` or `Series`. As methods are functions, do not forget to use parentheses `()`.

*   I’m interested in some basic statistics of the numerical data of my data table
    
    In \[9\]: df.describe()
    Out\[9\]: 
                 Age
    count   3.000000
    mean   38.333333
    std    18.230012
    min    22.000000
    25%    28.500000
    50%    35.000000
    75%    46.500000
    max    58.000000
    
    Copy to clipboard
    
    The [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe")
     method provides a quick overview of the numerical data in a `DataFrame`. As the `Name` and `Sex` columns are textual data, these are by default not taken into account by the [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe")
     method.
    

Many pandas operations return a `DataFrame` or a `Series`. The [`describe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.describe.html#pandas.DataFrame.describe "pandas.DataFrame.describe")
 method is an example of a pandas operation returning a pandas `Series` or a pandas `DataFrame`.

To user guide

Check more options on `describe` in the user guide section about [aggregations with describe](https://pandas.pydata.org/docs/user_guide/basics.html#basics-describe)

Note

This is just a starting point. Similar to spreadsheet software, pandas represents data as a table with columns and rows. Apart from the representation, the data manipulations and calculations you would do in spreadsheet software are also supported by pandas. Continue reading the next tutorials to get started!

#### REMEMBER

*   Import the package, aka `import pandas as pd`
    
*   A table of data is stored as a pandas `DataFrame`
    
*   Each column in a `DataFrame` is a `Series`
    
*   You can do things by applying a method on a `DataFrame` or `Series`
    

To user guide

A more extended explanation of `DataFrame` and `Series` is provided in the [introduction to data structures](https://pandas.pydata.org/docs/user_guide/dsintro.html#dsintro)
 page.

On this page