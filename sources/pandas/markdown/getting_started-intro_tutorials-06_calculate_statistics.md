[Skip to main content](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/06_calculate_statistics.html)
[3.1 (stable)](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/getting_started/intro_tutorials/06_calculate_statistics.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/06_calculate_statistics.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/intro_tutorials/06_calculate_statistics.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/getting_started/intro_tutorials/06_calculate_statistics.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/getting_started/intro_tutorials/06_calculate_statistics.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/intro_tutorials/06_calculate_statistics.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/getting_started/intro_tutorials/06_calculate_statistics.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/intro_tutorials/06_calculate_statistics.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/getting_started/intro_tutorials/06_calculate_statistics.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/intro_tutorials/06_calculate_statistics.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/intro_tutorials/06_calculate_statistics.html)

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
    

How to calculate summary statistics[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html#how-to-calculate-summary-statistics "Link to this heading")

===============================================================================================================================================================================================

Aggregating statistics[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html#aggregating-statistics "Link to this heading")

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

![../../_images/06_aggregate.svg](https://pandas.pydata.org/docs/_images/06_aggregate.svg)

*   What is the average age of the Titanic passengers?
    
    In \[4\]: titanic\["Age"\].mean()
    Out\[4\]: np.float64(29.69911764705882)
    
    Copy to clipboard
    

Different statistics are available and can be applied to columns with numerical data. Operations in general exclude missing data and operate across rows by default.

![../../_images/06_reduction.svg](https://pandas.pydata.org/docs/_images/06_reduction.svg)

*   What is the median age and ticket fare price of the Titanic passengers?
    
    In \[5\]: titanic\[\["Age", "Fare"\]\].median()
    Out\[5\]: 
    Age     28.0000
    Fare    14.4542
    dtype: float64
    
    Copy to clipboard
    
    The statistic applied to multiple columns of a `DataFrame` (the selection of two columns returns a `DataFrame`, see the [subset data tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html#min-tut-03-subset)
    ) is calculated for each numeric column.
    

The aggregating statistic can be calculated for multiple columns at the same time. Remember the `describe` function from the [first tutorial](https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html#min-tut-01-tableoriented)
?

In \[6\]: titanic\[\["Age", "Fare"\]\].describe()
Out\[6\]: 
              Age        Fare
count  714.000000  891.000000
mean    29.699118   32.204208
std     14.526497   49.693429
min      0.420000    0.000000
25%     20.125000    7.910400
50%     28.000000   14.454200
75%     38.000000   31.000000
max     80.000000  512.329200

Copy to clipboard

Instead of the predefined statistics, specific combinations of aggregating statistics for given columns can be defined using the [`DataFrame.agg()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg "pandas.DataFrame.agg")
 method:

In \[7\]: titanic.agg(
   ...:    {
   ...:        "Age": \["min", "max", "median", "skew"\],
   ...:        "Fare": \["min", "max", "median", "mean"\],
   ...:    }
   ...: )
   ...: 
Out\[7\]: 
              Age        Fare
min      0.420000    0.000000
max     80.000000  512.329200
median  28.000000   14.454200
skew     0.389108         NaN
mean          NaN   32.204208

Copy to clipboard

To user guide

Details about descriptive statistics are provided in the user guide section on [descriptive statistics](https://pandas.pydata.org/docs/user_guide/basics.html#basics-stats)
.

Aggregating statistics grouped by category[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html#aggregating-statistics-grouped-by-category "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![../../_images/06_groupby.svg](https://pandas.pydata.org/docs/_images/06_groupby.svg)

*   What is the average age for male versus female Titanic passengers?
    
    In \[8\]: titanic\[\["Sex", "Age"\]\].groupby("Sex").mean()
    Out\[8\]: 
                  Age
    Sex              
    female  27.915709
    male    30.726645
    
    Copy to clipboard
    
    As our interest is the average age for each gender, a subselection on these two columns is made first: `titanic[["Sex", "Age"]]`. Next, the [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")
     method is applied on the `Sex` column to make a group per category. The average age _for each gender_ is calculated and returned.
    

Calculating a given statistic (e.g. `mean` age) _for each category in a column_ (e.g. male/female in the `Sex` column) is a common pattern. The `groupby` method is used to support this type of operations. This fits in the more general `split-apply-combine` pattern:

*   **Split** the data into groups
    
*   **Apply** a function to each group independently
    
*   **Combine** the results into a data structure
    

The apply and combine steps are typically done together in pandas.

In the previous example, we explicitly selected the 2 columns first. If not, the `mean` method is applied to each column containing numerical columns by passing `numeric_only=True`:

In \[9\]: titanic.groupby("Sex").mean(numeric\_only\=True)
Out\[9\]: 
        PassengerId  Survived    Pclass  ...     SibSp     Parch       Fare
Sex                                      ...                               
female   431.028662  0.742038  2.159236  ...  0.694268  0.649682  44.479818
male     454.147314  0.188908  2.389948  ...  0.429809  0.235702  25.523893

\[2 rows x 7 columns\]

Copy to clipboard

It does not make much sense to get the average value of the `Pclass`. If we are only interested in the average age for each gender, the selection of columns (square brackets `[]` as usual) is supported on the grouped data as well:

In \[10\]: titanic.groupby("Sex")\["Age"\].mean()
Out\[10\]: 
Sex
female    27.915709
male      30.726645
Name: Age, dtype: float64

Copy to clipboard

![../../_images/06_groupby_select_detail.svg](https://pandas.pydata.org/docs/_images/06_groupby_select_detail.svg)

Note

The `Pclass` column contains numerical data but actually represents 3 categories (or factors) with respectively the labels ‘1’, ‘2’ and ‘3’. Calculating statistics on these does not make much sense. Therefore, pandas provides a `Categorical` data type to handle this type of data. More information is provided in the user guide [Categorical data](https://pandas.pydata.org/docs/user_guide/categorical.html#categorical)
 section.

*   What is the mean ticket fare price for each of the sex and cabin class combinations?
    
    In \[11\]: titanic.groupby(\["Sex", "Pclass"\])\["Fare"\].mean()
    Out\[11\]: 
    Sex     Pclass
    female  1         106.125798
            2          21.970121
            3          16.118810
    male    1          67.226127
            2          19.741782
            3          12.661633
    Name: Fare, dtype: float64
    
    Copy to clipboard
    
    Grouping can be done by multiple columns at the same time. Provide the column names as a list to the [`groupby()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html#pandas.DataFrame.groupby "pandas.DataFrame.groupby")
     method.
    

To user guide

A full description on the split-apply-combine approach is provided in the user guide section on [groupby operations](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby)
.

Count number of records by category[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/06_calculate_statistics.html#count-number-of-records-by-category "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![../../_images/06_valuecounts.svg](https://pandas.pydata.org/docs/_images/06_valuecounts.svg)

*   What is the number of passengers in each of the cabin classes?
    
    In \[12\]: titanic\["Pclass"\].value\_counts()
    Out\[12\]: 
    Pclass
    3    491
    1    216
    2    184
    Name: count, dtype: int64
    
    Copy to clipboard
    
    The [`value_counts()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.value_counts.html#pandas.Series.value_counts "pandas.Series.value_counts")
     method counts the number of records for each category in a column.
    

The function is a shortcut, it is actually a groupby operation in combination with counting the number of records within each group:

In \[13\]: titanic.groupby("Pclass")\["Pclass"\].count()
Out\[13\]: 
Pclass
1    216
2    184
3    491
Name: Pclass, dtype: int64

Copy to clipboard

Note

Both `size` and `count` can be used in combination with `groupby`. Whereas `size` includes `NaN` values and just provides the number of rows (size of the table), `count` excludes the missing values. In the `value_counts` method, use the `dropna` argument to include or exclude the `NaN` values.

To user guide

The user guide has a dedicated section on `value_counts` , see the page on [discretization](https://pandas.pydata.org/docs/user_guide/basics.html#basics-discretization)
.

#### REMEMBER

*   Aggregation statistics can be calculated on entire columns or rows.
    
*   `groupby` provides the power of the _split-apply-combine_ pattern.
    
*   `value_counts` is a convenient shortcut to count the number of entries in each category of a variable.
    

To user guide

A full description on the split-apply-combine approach is provided in the user guide pages about [groupby operations](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby)
.

On this page