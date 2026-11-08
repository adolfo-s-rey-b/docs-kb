[Skip to main content](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/07_reshape_table_layout.html)
[3.1 (stable)](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/getting_started/intro_tutorials/07_reshape_table_layout.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/07_reshape_table_layout.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/intro_tutorials/07_reshape_table_layout.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/getting_started/intro_tutorials/07_reshape_table_layout.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/getting_started/intro_tutorials/07_reshape_table_layout.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/intro_tutorials/07_reshape_table_layout.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/getting_started/intro_tutorials/07_reshape_table_layout.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/intro_tutorials/07_reshape_table_layout.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/getting_started/intro_tutorials/07_reshape_table_layout.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/intro_tutorials/07_reshape_table_layout.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/intro_tutorials/07_reshape_table_layout.html)

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

*   Titanic data
    
    This tutorial uses the Titanic data set, stored as CSV. The data consists of the following data columns:
    
    *   PassengerId: Id of every passenger.
        
    *   Survived: Indication whether passenger survived. `0` for no and `1` for yes.
        
    *   Pclass: One out of the 3 ticket classes: Class `1`, Class `2` and Class `3`.
        
    *   Name: Name of passenger.
        
    *   Sex: Gender of passenger.
        
    *   Age: Age of passenger in years.
        
    *   SibSp: Number of siblings or spouses aboard.
        
    *   Parch: Number of parents or children aboard.
        
    *   Ticket: Ticket number of passenger.
        
    *   Fare: Indicating the fare.
        
    *   Cabin: Cabin number of passenger.
        
    *   Embarked: Port of embarkation.
        
    
    [To raw data](https://github.com/pandas-dev/pandas/raw/main/doc/data/titanic.csv)
    
    In \[2\]: titanic \= pd.read\_csv("data/titanic.csv")
    
    In \[3\]: titanic.head()
    Out\[3\]: 
       PassengerId  Survived  Pclass  ...     Fare Cabin Embarked
    0            1         0       3  ...   7.2500   NaN        S
    1            2         1       1  ...  71.2833   C85        C
    2            3         1       3  ...   7.9250   NaN        S
    3            4         1       1  ...  53.1000  C123        S
    4            5         0       3  ...   8.0500   NaN        S
    
    \[5 rows x 12 columns\]
    
    Copy to clipboard
    
*   Air quality data
    
    This tutorial uses air quality data about 𝑁⁢𝑂2 and Particulate matter less than 2.5 micrometers, made available by [OpenAQ](https://openaq.org/)
     and using the [py-openaq](http://dhhagan.github.io/py-openaq/index.html)
     package. The `air_quality_long.csv` data set provides 𝑁⁢𝑂2 and 𝑃⁢𝑀25 values for the measurement stations _FR04014_, _BETR801_ and _London Westminster_ in respectively Paris, Antwerp and London.
    
    The air-quality data set has the following columns:
    
    *   city: city where the sensor is used, either Paris, Antwerp or London
        
    *   country: country where the sensor is used, either FR, BE or GB
        
    *   location: the id of the sensor, either _FR04014_, _BETR801_ or _London Westminster_
        
    *   parameter: the parameter measured by the sensor, either 𝑁⁢𝑂2 or Particulate matter
        
    *   value: the measured value
        
    *   unit: the unit of the measured parameter, in this case ‘µg/m³’
        
    
    and the index of the `DataFrame` is `datetime`, the datetime of the measurement.
    
    Note
    
    The air-quality data is provided in a so-called _long format_ data representation with each observation on a separate row and each variable a separate column of the data table. The long/narrow format is also known as the [tidy data format](https://www.jstatsoft.org/article/view/v059i10)
    .
    
    [To raw data](https://github.com/pandas-dev/pandas/tree/main/doc/data/air_quality_long.csv)
    
    In \[4\]: air\_quality \= pd.read\_csv(
       ...:    "data/air\_quality\_long.csv", index\_col\="date.utc", parse\_dates\=True
       ...: )
       ...: 
    
    In \[5\]: air\_quality.head()
    Out\[5\]: 
                                    city country location parameter  value   unit
    date.utc                                                                     
    2019-06-18 06:00:00+00:00  Antwerpen      BE  BETR801      pm25   18.0  µg/m³
    2019-06-17 08:00:00+00:00  Antwerpen      BE  BETR801      pm25    6.5  µg/m³
    2019-06-17 07:00:00+00:00  Antwerpen      BE  BETR801      pm25   18.5  µg/m³
    2019-06-17 06:00:00+00:00  Antwerpen      BE  BETR801      pm25   16.0  µg/m³
    2019-06-17 05:00:00+00:00  Antwerpen      BE  BETR801      pm25    7.5  µg/m³
    
    Copy to clipboard
    

How to reshape the layout of tables[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html#how-to-reshape-the-layout-of-tables "Link to this heading")

===============================================================================================================================================================================================

Sort table rows[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html#sort-table-rows "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------

*   I want to sort the Titanic data according to the age of the passengers.
    
    In \[6\]: titanic.sort\_values(by\="Age").head()
    Out\[6\]: 
         PassengerId  Survived  Pclass  ...     Fare Cabin Embarked
    803          804         1       3  ...   8.5167   NaN        C
    755          756         1       2  ...  14.5000   NaN        S
    644          645         1       3  ...  19.2583   NaN        C
    469          470         1       3  ...  19.2583   NaN        C
    78            79         1       2  ...  29.0000   NaN        S
    
    \[5 rows x 12 columns\]
    
    Copy to clipboard
    

*   I want to sort the Titanic data according to the cabin class and age in descending order.
    
    In \[7\]: titanic.sort\_values(by\=\['Pclass', 'Age'\], ascending\=False).head()
    Out\[7\]: 
         PassengerId  Survived  Pclass  ...    Fare Cabin Embarked
    851          852         0       3  ...  7.7750   NaN        S
    116          117         0       3  ...  7.7500   NaN        Q
    280          281         0       3  ...  7.7500   NaN        Q
    483          484         1       3  ...  9.5875   NaN        S
    326          327         0       3  ...  6.2375   NaN        S
    
    \[5 rows x 12 columns\]
    
    Copy to clipboard
    
    With [`DataFrame.sort_values()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.sort_values.html#pandas.DataFrame.sort_values "pandas.DataFrame.sort_values")
    , the rows in the table are sorted according to the defined column(s). The index will follow the row order.
    

To user guide

More details about sorting of tables is provided in the user guide section on [sorting data](https://pandas.pydata.org/docs/user_guide/basics.html#basics-sorting)
.

Long to wide table format[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html#long-to-wide-table-format "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let’s use a small subset of the air quality data set. We focus on 𝑁⁢𝑂2 data and only use the first two measurements of each location (i.e. the head of each group). The subset of data will be called `no2_subset`.

\# filter for no2 data only
In \[8\]: no2 \= air\_quality\[air\_quality\["parameter"\] \== "no2"\]

Copy to clipboard

\# use 2 measurements (head) for each location (groupby)
In \[9\]: no2\_subset \= no2.sort\_index().groupby(\["location"\]).head(2)

In \[10\]: no2\_subset
Out\[10\]: 
                                city country  ...  value   unit
date.utc                                      ...              
2019-04-09 01:00:00+00:00  Antwerpen      BE  ...   22.5  µg/m³
2019-04-09 01:00:00+00:00      Paris      FR  ...   24.4  µg/m³
2019-04-09 02:00:00+00:00     London      GB  ...   67.0  µg/m³
2019-04-09 02:00:00+00:00  Antwerpen      BE  ...   53.5  µg/m³
2019-04-09 02:00:00+00:00      Paris      FR  ...   27.4  µg/m³
2019-04-09 03:00:00+00:00     London      GB  ...   67.0  µg/m³

\[6 rows x 6 columns\]

Copy to clipboard

![../../_images/07_pivot.svg](https://pandas.pydata.org/docs/_images/07_pivot.svg)

*   I want the values for the three stations as separate columns next to each other.
    
    In \[11\]: no2\_subset.pivot(columns\="location", values\="value")
    Out\[11\]: 
    location                   BETR801  FR04014  London Westminster
    date.utc                                                       
    2019-04-09 01:00:00+00:00     22.5     24.4                 NaN
    2019-04-09 02:00:00+00:00     53.5     27.4                67.0
    2019-04-09 03:00:00+00:00      NaN      NaN                67.0
    
    Copy to clipboard
    
    The [`pivot()`](https://pandas.pydata.org/docs/reference/api/pandas.pivot.html#pandas.pivot "pandas.pivot")
     function is purely reshaping of the data: a single value for each index/column combination is required.
    

As pandas supports plotting of multiple columns (see [plotting tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/04_plotting.html#min-tut-04-plotting)
) out of the box, the conversion from _long_ to _wide_ table format enables the plotting of the different time series at the same time:

In \[12\]: no2.head()
Out\[12\]: 
                            city country location parameter  value   unit
date.utc                                                                 
2019-06-21 00:00:00+00:00  Paris      FR  FR04014       no2   20.0  µg/m³
2019-06-20 23:00:00+00:00  Paris      FR  FR04014       no2   21.8  µg/m³
2019-06-20 22:00:00+00:00  Paris      FR  FR04014       no2   26.5  µg/m³
2019-06-20 21:00:00+00:00  Paris      FR  FR04014       no2   24.9  µg/m³
2019-06-20 20:00:00+00:00  Paris      FR  FR04014       no2   21.4  µg/m³

Copy to clipboard

In \[13\]: no2.pivot(columns\="location", values\="value").plot()
Out\[13\]: <Axes: xlabel='date.utc'>

Copy to clipboard

![../../_images/7_reshape_columns.png](https://pandas.pydata.org/docs/_images/7_reshape_columns.png)

Note

When the `index` parameter is not defined, the existing index (row labels) is used.

To user guide

For more information about [`pivot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "pandas.DataFrame.pivot")
, see the user guide section on [pivoting DataFrame objects](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-reshaping)
.

Pivot table[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html#pivot-table "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------

![../../_images/07_pivot_table.svg](https://pandas.pydata.org/docs/_images/07_pivot_table.svg)

*   I want the mean concentrations for 𝑁⁢𝑂2 and 𝑃⁢𝑀2.5 in each of the stations in table form.
    
    In \[14\]: air\_quality.pivot\_table(
       ....:    values\="value", index\="location", columns\="parameter", aggfunc\="mean"
       ....: )
       ....: 
    Out\[14\]: 
    parameter                 no2       pm25
    location                                
    BETR801             26.950920  23.169492
    FR04014             29.374284        NaN
    London Westminster  29.740050  13.443568
    
    Copy to clipboard
    
    In the case of [`pivot()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html#pandas.DataFrame.pivot "pandas.DataFrame.pivot")
    , the data is only rearranged. When multiple values need to be aggregated (in this specific case, the values on different time steps), [`pivot_table()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table "pandas.DataFrame.pivot_table")
     can be used, providing an aggregation function (e.g. mean) on how to combine these values.
    

Pivot table is a well known concept in spreadsheet software. When interested in the row/column margins (subtotals) for each variable, set the `margins` parameter to `True`:

In \[15\]: air\_quality.pivot\_table(
   ....:    values\="value",
   ....:    index\="location",
   ....:    columns\="parameter",
   ....:    aggfunc\="mean",
   ....:    margins\=True,
   ....: )
   ....: 
Out\[15\]: 
parameter                 no2       pm25        All
location                                           
BETR801             26.950920  23.169492  24.982353
FR04014             29.374284        NaN  29.374284
London Westminster  29.740050  13.443568  21.491708
All                 29.430316  14.386849  24.222743

Copy to clipboard

To user guide

For more information about [`pivot_table()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table "pandas.DataFrame.pivot_table")
, see the user guide section on [pivot tables](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-pivot)
.

Note

In case you are wondering, [`pivot_table()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot_table.html#pandas.DataFrame.pivot_table "pandas.DataFrame.pivot_table")
 is indeed directly linked to [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")
. The same result can be derived by grouping on both `parameter` and `location`:

air\_quality.groupby(\["parameter", "location"\])\[\["value"\]\].mean()

Copy to clipboard

To user guide

Wide to long format[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/07_reshape_table_layout.html#wide-to-long-format "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------

Starting again from the wide format table created in the previous section, we add a new index to the `DataFrame` with [`reset_index()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.reset_index.html#pandas.DataFrame.reset_index "pandas.DataFrame.reset_index")
.

In \[16\]: no2\_pivoted \= no2.pivot(columns\="location", values\="value").reset\_index()

In \[17\]: no2\_pivoted.head()
Out\[17\]: 
location                  date.utc  BETR801  FR04014  London Westminster
0        2019-04-09 01:00:00+00:00     22.5     24.4                 NaN
1        2019-04-09 02:00:00+00:00     53.5     27.4                67.0
2        2019-04-09 03:00:00+00:00     54.5     34.2                67.0
3        2019-04-09 04:00:00+00:00     34.5     48.5                41.0
4        2019-04-09 05:00:00+00:00     46.5     59.5                41.0

Copy to clipboard

![../../_images/07_melt.svg](https://pandas.pydata.org/docs/_images/07_melt.svg)

*   I want to collect all air quality 𝑁⁢𝑂2 measurements in a single column (long format).
    
    In \[18\]: no\_2 \= no2\_pivoted.melt(id\_vars\="date.utc")
    
    In \[19\]: no\_2.head()
    Out\[19\]: 
                       date.utc location  value
    0 2019-04-09 01:00:00+00:00  BETR801   22.5
    1 2019-04-09 02:00:00+00:00  BETR801   53.5
    2 2019-04-09 03:00:00+00:00  BETR801   54.5
    3 2019-04-09 04:00:00+00:00  BETR801   34.5
    4 2019-04-09 05:00:00+00:00  BETR801   46.5
    
    Copy to clipboard
    
    The [`pandas.melt()`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html#pandas.melt "pandas.melt")
     method on a `DataFrame` converts the data table from wide format to long format. The column headers become the variable names in a newly created column.
    

The solution is the short version on how to apply [`pandas.melt()`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html#pandas.melt "pandas.melt")
. The method will _melt_ all columns NOT mentioned in `id_vars` together into two columns: A column with the column header names and a column with the values itself. The latter column gets by default the name `value`.

The parameters passed to [`pandas.melt()`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html#pandas.melt "pandas.melt")
 can be defined in more detail:

In \[20\]: no\_2 \= no2\_pivoted.melt(
   ....:    id\_vars\="date.utc",
   ....:    value\_vars\=\["BETR801", "FR04014", "London Westminster"\],
   ....:    value\_name\="NO\_2",
   ....:    var\_name\="id\_location",
   ....: )
   ....: 

In \[21\]: no\_2.head()
Out\[21\]: 
                   date.utc id\_location  NO\_2
0 2019-04-09 01:00:00+00:00     BETR801  22.5
1 2019-04-09 02:00:00+00:00     BETR801  53.5
2 2019-04-09 03:00:00+00:00     BETR801  54.5
3 2019-04-09 04:00:00+00:00     BETR801  34.5
4 2019-04-09 05:00:00+00:00     BETR801  46.5

Copy to clipboard

The additional parameters have the following effects:

*   `value_vars` defines which columns to _melt_ together
    
*   `value_name` provides a custom column name for the values column instead of the default column name `value`
    
*   `var_name` provides a custom column name for the column collecting the column header names. Otherwise it takes the index name or a default `variable`
    

Hence, the arguments `value_name` and `var_name` are just user-defined names for the two generated columns. The columns to melt are defined by `id_vars` and `value_vars`.

To user guide

Conversion from wide to long format with [`pandas.melt()`](https://pandas.pydata.org/docs/reference/api/pandas.melt.html#pandas.melt "pandas.melt")
 is explained in the user guide section on [reshaping by melt](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping-melt)
.

#### REMEMBER

*   Sorting by one or more columns is supported by `sort_values`.
    
*   The `pivot` function is purely restructuring of the data, `pivot_table` supports aggregations.
    
*   The reverse of `pivot` (long to wide format) is `melt` (wide to long format).
    

To user guide

A full overview is available in the user guide on the pages about [reshaping and pivoting](https://pandas.pydata.org/docs/user_guide/reshaping.html#reshaping)
.

On this page