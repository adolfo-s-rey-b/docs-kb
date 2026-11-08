[Skip to main content](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/05_add_columns.html)
[3.1 (stable)](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/getting_started/intro_tutorials/05_add_columns.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/05_add_columns.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/intro_tutorials/05_add_columns.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/getting_started/intro_tutorials/05_add_columns.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/getting_started/intro_tutorials/05_add_columns.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/intro_tutorials/05_add_columns.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/getting_started/intro_tutorials/05_add_columns.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/intro_tutorials/05_add_columns.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/getting_started/intro_tutorials/05_add_columns.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/intro_tutorials/05_add_columns.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/intro_tutorials/05_add_columns.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

In \[1\]: import pandas as pd

Copy to clipboard

Data used for this tutorial:

*   Air quality data
    
    For this tutorial, air quality data about 𝑁⁢𝑂2 is used, made available by [OpenAQ](https://openaq.org/)
     and using the [py-openaq](http://dhhagan.github.io/py-openaq/index.html)
     package. The `air_quality_no2.csv` data set provides 𝑁⁢𝑂2 values for the measurement stations _FR04014_, _BETR801_ and _London Westminster_ in respectively Paris, Antwerp and London.
    
    [To raw data](https://github.com/pandas-dev/pandas/tree/main/doc/data/air_quality_no2.csv)
    
    In \[2\]: air\_quality \= pd.read\_csv("data/air\_quality\_no2.csv", index\_col\=0, parse\_dates\=True)
    
    In \[3\]: air\_quality.head()
    Out\[3\]: 
                         station\_antwerp  station\_paris  station\_london
    datetime                                                           
    2019-05-07 02:00:00              NaN            NaN            23.0
    2019-05-07 03:00:00             50.5           25.0            19.0
    2019-05-07 04:00:00             45.0           27.7            19.0
    2019-05-07 05:00:00              NaN           50.4            16.0
    2019-05-07 06:00:00              NaN           61.9             NaN
    
    Copy to clipboard
    

How to create new columns derived from existing columns[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/05_add_columns.html#how-to-create-new-columns-derived-from-existing-columns "Link to this heading")

==============================================================================================================================================================================================================================

![../../_images/05_newcolumn_1.svg](https://pandas.pydata.org/docs/_images/05_newcolumn_1.svg)

*   I want to express the 𝑁⁢𝑂2 concentration of the station in London in mg/m3.
    
    (_If we assume temperature of 25 degrees Celsius and pressure of 1013 hPa, the conversion factor is 1.882_)
    
    In \[4\]: air\_quality\["london\_mg\_per\_cubic"\] \= air\_quality\["station\_london"\] \* 1.882
    
    In \[5\]: air\_quality.head()
    Out\[5\]: 
                         station\_antwerp  ...  london\_mg\_per\_cubic
    datetime                              ...                     
    2019-05-07 02:00:00              NaN  ...               43.286
    2019-05-07 03:00:00             50.5  ...               35.758
    2019-05-07 04:00:00             45.0  ...               35.758
    2019-05-07 05:00:00              NaN  ...               30.112
    2019-05-07 06:00:00              NaN  ...                  NaN
    
    \[5 rows x 4 columns\]
    
    Copy to clipboard
    
    To create a new column, use the square brackets `[]` with the new column name at the left side of the assignment.
    

Note

The calculation of the values is done **element-wise**. This means all values in the given column are multiplied by the value 1.882 at once. You do not need to use a loop to iterate each of the rows!

![../../_images/05_newcolumn_2.svg](https://pandas.pydata.org/docs/_images/05_newcolumn_2.svg)

*   I want to check the ratio of the values in Paris versus Antwerp and save the result in a new column.
    
    In \[6\]: air\_quality\["ratio\_paris\_antwerp"\] \= (
       ...:    air\_quality\["station\_paris"\] / air\_quality\["station\_antwerp"\]
       ...: )
       ...: 
    
    In \[7\]: air\_quality.head()
    Out\[7\]: 
                         station\_antwerp  ...  ratio\_paris\_antwerp
    datetime                              ...                     
    2019-05-07 02:00:00              NaN  ...                  NaN
    2019-05-07 03:00:00             50.5  ...             0.495050
    2019-05-07 04:00:00             45.0  ...             0.615556
    2019-05-07 05:00:00              NaN  ...                  NaN
    2019-05-07 06:00:00              NaN  ...                  NaN
    
    \[5 rows x 5 columns\]
    
    Copy to clipboard
    
    The calculation is again element-wise, so the `/` is applied _for the values in each row_.
    

Other mathematical operators (`+`, `-`, `*`, `/`, …) and logical operators (`<`, `>`, `==`, …) also work element-wise. The latter was already used in the [subset data tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#min-tut-03-subset)
 to filter rows of a table using a conditional expression.

If you need more advanced logic, you can use arbitrary Python code via [`apply()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")
.

*   I want to rename the data columns to the corresponding station identifiers used by [OpenAQ](https://openaq.org/)
    .
    
    In \[8\]: air\_quality\_renamed \= air\_quality.rename(
       ...:    columns\={
       ...:        "station\_antwerp": "BETR801",
       ...:        "station\_paris": "FR04014",
       ...:        "station\_london": "London Westminster",
       ...:    }
       ...: )
       ...: 
    
    Copy to clipboard
    
    In \[9\]: air\_quality\_renamed.head()
    Out\[9\]: 
                         BETR801  ...  ratio\_paris\_antwerp
    datetime                      ...                     
    2019-05-07 02:00:00      NaN  ...                  NaN
    2019-05-07 03:00:00     50.5  ...             0.495050
    2019-05-07 04:00:00     45.0  ...             0.615556
    2019-05-07 05:00:00      NaN  ...                  NaN
    2019-05-07 06:00:00      NaN  ...                  NaN
    
    \[5 rows x 5 columns\]
    
    Copy to clipboard
    
    The [`rename()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.rename.html#pandas.DataFrame.rename "pandas.DataFrame.rename")
     function can be used for both row labels and column labels. Provide a dictionary with the keys the current names and the values the new names to update the corresponding names.
    

The mapping should not be restricted to fixed names only, but can be a mapping function as well. For example, converting the column names to lowercase letters can be done using a function as well:

In \[10\]: air\_quality\_renamed \= air\_quality\_renamed.rename(columns\=str.lower)

In \[11\]: air\_quality\_renamed.head()
Out\[11\]: 
                     betr801  ...  ratio\_paris\_antwerp
datetime                      ...                     
2019-05-07 02:00:00      NaN  ...                  NaN
2019-05-07 03:00:00     50.5  ...             0.495050
2019-05-07 04:00:00     45.0  ...             0.615556
2019-05-07 05:00:00      NaN  ...                  NaN
2019-05-07 06:00:00      NaN  ...                  NaN

\[5 rows x 5 columns\]

Copy to clipboard

To user guide

Details about column or row label renaming is provided in the user guide section on [renaming labels](https://pandas.pydata.org/docs/user_guide/basics.html#basics-rename)
.

#### REMEMBER

*   Create a new column by assigning the output to the DataFrame with a new column name in between the `[]`.
    
*   Operations are element-wise, no need to loop over rows.
    
*   Use `rename` with a dictionary or function to rename row labels or column names.
    

To user guide

The user guide contains a separate section on [column addition and deletion](https://pandas.pydata.org/docs/user_guide/dsintro.html#basics-dataframe-sel-add-del)
.