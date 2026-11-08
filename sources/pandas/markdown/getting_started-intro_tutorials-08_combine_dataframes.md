[Skip to main content](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/getting_started/intro_tutorials/08_combine_dataframes.html)
[3.1 (stable)](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/getting_started/intro_tutorials/08_combine_dataframes.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/intro_tutorials/08_combine_dataframes.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/intro_tutorials/08_combine_dataframes.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/getting_started/intro_tutorials/08_combine_dataframes.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/getting_started/intro_tutorials/08_combine_dataframes.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/intro_tutorials/08_combine_dataframes.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/getting_started/intro_tutorials/08_combine_dataframes.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/intro_tutorials/08_combine_dataframes.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/getting_started/intro_tutorials/08_combine_dataframes.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/intro_tutorials/08_combine_dataframes.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/intro_tutorials/08_combine_dataframes.html)

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

*   Air quality Nitrate data
    
    For this tutorial, air quality data about 𝑁⁢𝑂2 is used, made available by [OpenAQ](https://openaq.org/)
     and downloaded using the [py-openaq](http://dhhagan.github.io/py-openaq/index.html)
     package.
    
    The `air_quality_no2_long.csv` data set provides 𝑁⁢𝑂2 values for the measurement stations _FR04014_, _BETR801_ and _London Westminster_ in respectively Paris, Antwerp and London.
    
    [To raw data](https://github.com/pandas-dev/pandas/tree/main/doc/data/air_quality_no2_long.csv)
    
    In \[2\]: air\_quality\_no2 \= pd.read\_csv("data/air\_quality\_no2\_long.csv",
       ...:                              parse\_dates\=True)
       ...: 
    
    In \[3\]: air\_quality\_no2 \= air\_quality\_no2\[\["date.utc", "location",\
       ...:                                   "parameter", "value"\]\]
       ...: 
    
    In \[4\]: air\_quality\_no2.head()
    Out\[4\]: 
                        date.utc location parameter  value
    0  2019-06-21 00:00:00+00:00  FR04014       no2   20.0
    1  2019-06-20 23:00:00+00:00  FR04014       no2   21.8
    2  2019-06-20 22:00:00+00:00  FR04014       no2   26.5
    3  2019-06-20 21:00:00+00:00  FR04014       no2   24.9
    4  2019-06-20 20:00:00+00:00  FR04014       no2   21.4
    
    Copy to clipboard
    
*   Air quality Particulate matter data
    
    For this tutorial, air quality data about Particulate matter less than 2.5 micrometers is used, made available by [OpenAQ](https://openaq.org/)
     and downloaded using the [py-openaq](http://dhhagan.github.io/py-openaq/index.html)
     package.
    
    The `air_quality_pm25_long.csv` data set provides 𝑃⁢𝑀25 values for the measurement stations _FR04014_, _BETR801_ and _London Westminster_ in respectively Paris, Antwerp and London.
    
    [To raw data](https://github.com/pandas-dev/pandas/tree/main/doc/data/air_quality_pm25_long.csv)
    
    In \[5\]: air\_quality\_pm25 \= pd.read\_csv("data/air\_quality\_pm25\_long.csv",
       ...:                               parse\_dates\=True)
       ...: 
    
    In \[6\]: air\_quality\_pm25 \= air\_quality\_pm25\[\["date.utc", "location",\
       ...:                                     "parameter", "value"\]\]
       ...: 
    
    In \[7\]: air\_quality\_pm25.head()
    Out\[7\]: 
                        date.utc location parameter  value
    0  2019-06-18 06:00:00+00:00  BETR801      pm25   18.0
    1  2019-06-17 08:00:00+00:00  BETR801      pm25    6.5
    2  2019-06-17 07:00:00+00:00  BETR801      pm25   18.5
    3  2019-06-17 06:00:00+00:00  BETR801      pm25   16.0
    4  2019-06-17 05:00:00+00:00  BETR801      pm25    7.5
    
    Copy to clipboard
    

How to combine data from multiple tables[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html#how-to-combine-data-from-multiple-tables "Link to this heading")

=======================================================================================================================================================================================================

Concatenating objects[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html#concatenating-objects "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

![../../_images/08_concat_row.svg](https://pandas.pydata.org/docs/_images/08_concat_row.svg)

*   I want to combine the measurements of 𝑁⁢𝑂2 and 𝑃⁢𝑀25, two tables with a similar structure, in a single table.
    
    In \[8\]: air\_quality \= pd.concat(\[air\_quality\_pm25, air\_quality\_no2\], axis\=0)
    
    In \[9\]: air\_quality.head()
    Out\[9\]: 
                        date.utc location parameter  value
    0  2019-06-18 06:00:00+00:00  BETR801      pm25   18.0
    1  2019-06-17 08:00:00+00:00  BETR801      pm25    6.5
    2  2019-06-17 07:00:00+00:00  BETR801      pm25   18.5
    3  2019-06-17 06:00:00+00:00  BETR801      pm25   16.0
    4  2019-06-17 05:00:00+00:00  BETR801      pm25    7.5
    
    Copy to clipboard
    
    The [`concat()`](https://pandas.pydata.org/docs/reference/api/pandas.concat.html#pandas.concat "pandas.concat")
     function performs concatenation operations of multiple tables along one of the axes (row-wise or column-wise).
    

By default concatenation is along axis 0, so the resulting table combines the rows of the input tables. Let’s check the shape of the original and the concatenated tables to verify the operation:

In \[10\]: print('Shape of the \`\`air\_quality\_pm25\`\` table: ', air\_quality\_pm25.shape)
Shape of the \`\`air\_quality\_pm25\`\` table:  (1110, 4)

In \[11\]: print('Shape of the \`\`air\_quality\_no2\`\` table: ', air\_quality\_no2.shape)
Shape of the \`\`air\_quality\_no2\`\` table:  (2068, 4)

In \[12\]: print('Shape of the resulting \`\`air\_quality\`\` table: ', air\_quality.shape)
Shape of the resulting \`\`air\_quality\`\` table:  (3178, 4)

Copy to clipboard

Hence, the resulting table has 3178 = 1110 + 2068 rows.

Note

The **axis** argument will return in a number of pandas methods that can be applied **along an axis**. A `DataFrame` has two corresponding axes: the first running vertically downwards across rows (axis 0), and the second running horizontally across columns (axis 1). Most operations like concatenation or summary statistics are by default across rows (axis 0), but can be applied across columns as well.

Sorting the table on the datetime information also illustrates the combination of both tables, with the `parameter` column defining the origin of the table (either `no2` from table `air_quality_no2` or `pm25` from table `air_quality_pm25`):

In \[13\]: air\_quality \= air\_quality.sort\_values("date.utc")

In \[14\]: air\_quality.head()
Out\[14\]: 
                       date.utc            location parameter  value
100   2019-05-07 01:00:00+00:00             BETR801      pm25   12.5
1109  2019-05-07 01:00:00+00:00  London Westminster      pm25    8.0
1003  2019-05-07 01:00:00+00:00             FR04014       no2   25.0
1098  2019-05-07 01:00:00+00:00             BETR801       no2   50.5
2067  2019-05-07 01:00:00+00:00  London Westminster       no2   23.0

Copy to clipboard

In this specific example, the `parameter` column provided by the data ensures that each of the original tables can be identified. This is not always the case. The `concat` function provides a convenient solution with the `keys` argument, adding an additional (hierarchical) row index. For example:

In \[15\]: air\_quality\_ \= pd.concat(\[air\_quality\_pm25, air\_quality\_no2\], keys\=\["PM25", "NO2"\])

In \[16\]: air\_quality\_.head()
Out\[16\]: 
                         date.utc location parameter  value
PM25 0  2019-06-18 06:00:00+00:00  BETR801      pm25   18.0
     1  2019-06-17 08:00:00+00:00  BETR801      pm25    6.5
     2  2019-06-17 07:00:00+00:00  BETR801      pm25   18.5
     3  2019-06-17 06:00:00+00:00  BETR801      pm25   16.0
     4  2019-06-17 05:00:00+00:00  BETR801      pm25    7.5

Copy to clipboard

Note

The existence of multiple row/column indices at the same time has not been mentioned within these tutorials. _Hierarchical indexing_ or _MultiIndex_ is an advanced and powerful pandas feature to analyze higher dimensional data.

Multi-indexing is out of scope for this pandas introduction. For the moment, remember that the function `reset_index` can be used to convert any level of an index to a column, e.g. `air_quality.reset_index(level=0)`

To user guide

Feel free to dive into the world of multi-indexing at the user guide section on [advanced indexing](https://pandas.pydata.org/docs/user_guide/advanced.html#advanced)
.

To user guide

More options on table concatenation (row and column wise) and how `concat` can be used to define the logic (union or intersection) of the indexes on the other axes is provided at the section on [object concatenation](https://pandas.pydata.org/docs/user_guide/merging.html#merging-concat)
.

Join tables using a common identifier[#](https://pandas.pydata.org/docs/getting_started/intro_tutorials/08_combine_dataframes.html#join-tables-using-a-common-identifier "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

![../../_images/08_merge_left.svg](https://pandas.pydata.org/docs/_images/08_merge_left.svg)

*   Add the station coordinates, provided by the stations metadata table, to the corresponding rows in the measurements table.
    
    Warning
    
    The air quality measurement station coordinates are stored in a data file `air_quality_stations.csv`, downloaded using the [py-openaq](http://dhhagan.github.io/py-openaq/index.html)
     package.
    
    In \[17\]: stations\_coord \= pd.read\_csv("data/air\_quality\_stations.csv")
    
    In \[18\]: stations\_coord.head()
    Out\[18\]: 
      location  coordinates.latitude  coordinates.longitude
    0  BELAL01              51.23619                4.38522
    1  BELHB23              51.17030                4.34100
    2  BELLD01              51.10998                5.00486
    3  BELLD02              51.12038                5.02155
    4  BELR833              51.32766                4.36226
    
    Copy to clipboard
    
    Note
    
    The stations used in this example (FR04014, BETR801 and London Westminster) are just three entries enlisted in the metadata table. We only want to add the coordinates of these three to the measurements table, each on the corresponding rows of the `air_quality` table.
    
    In \[19\]: air\_quality.head()
    Out\[19\]: 
                           date.utc            location parameter  value
    100   2019-05-07 01:00:00+00:00             BETR801      pm25   12.5
    1109  2019-05-07 01:00:00+00:00  London Westminster      pm25    8.0
    1003  2019-05-07 01:00:00+00:00             FR04014       no2   25.0
    1098  2019-05-07 01:00:00+00:00             BETR801       no2   50.5
    2067  2019-05-07 01:00:00+00:00  London Westminster       no2   23.0
    
    Copy to clipboard
    
    In \[20\]: air\_quality \= pd.merge(air\_quality, stations\_coord, how\="left", on\="location")
    
    In \[21\]: air\_quality.head()
    Out\[21\]: 
                        date.utc  ...  coordinates.longitude
    0  2019-05-07 01:00:00+00:00  ...                4.43182
    1  2019-05-07 01:00:00+00:00  ...               -0.13193
    2  2019-05-07 01:00:00+00:00  ...                2.39390
    3  2019-05-07 01:00:00+00:00  ...                2.39390
    4  2019-05-07 01:00:00+00:00  ...                4.43182
    
    \[5 rows x 6 columns\]
    
    Copy to clipboard
    
    Using the [`merge()`](https://pandas.pydata.org/docs/reference/api/pandas.merge.html#pandas.merge "pandas.merge")
     function, for each of the rows in the `air_quality` table, the corresponding coordinates are added from the `air_quality_stations_coord` table. Both tables have the column `location` in common which is used as a key to combine the information. By choosing the `left` join, only the locations available in the `air_quality` (left) table, i.e. FR04014, BETR801 and London Westminster, end up in the resulting table. The `merge` function supports multiple join options similar to database-style operations.
    

*   Add the parameters’ full description and name, provided by the parameters metadata table, to the measurements table.
    
    Warning
    
    The air quality parameters metadata are stored in a data file `air_quality_parameters.csv`, downloaded using the [py-openaq](http://dhhagan.github.io/py-openaq/index.html)
     package.
    
    In \[22\]: air\_quality\_parameters \= pd.read\_csv("data/air\_quality\_parameters.csv")
    
    In \[23\]: air\_quality\_parameters.head()
    Out\[23\]: 
         id                                        description  name
    0    bc                                       Black Carbon    BC
    1    co                                    Carbon Monoxide    CO
    2   no2                                   Nitrogen Dioxide   NO2
    3    o3                                              Ozone    O3
    4  pm10  Particulate matter less than 10 micrometers in...  PM10
    
    Copy to clipboard
    
    In \[24\]: air\_quality \= pd.merge(air\_quality, air\_quality\_parameters,
       ....:                       how\='left', left\_on\='parameter', right\_on\='id')
       ....: 
    
    In \[25\]: air\_quality.head()
    Out\[25\]: 
                        date.utc  ...   name
    0  2019-05-07 01:00:00+00:00  ...  PM2.5
    1  2019-05-07 01:00:00+00:00  ...  PM2.5
    2  2019-05-07 01:00:00+00:00  ...    NO2
    3  2019-05-07 01:00:00+00:00  ...    NO2
    4  2019-05-07 01:00:00+00:00  ...    NO2
    
    \[5 rows x 9 columns\]
    
    Copy to clipboard
    
    Compared to the previous example, there is no common column name. However, the `parameter` column in the `air_quality` table and the `id` column in the `air_quality_parameters` table both provide the measured variable in a common format. The `left_on` and `right_on` arguments are used here (instead of just `on`) to make the link between the two tables.
    

To user guide

pandas also supports inner, outer, and right joins. More information on join/merge of tables is provided in the user guide section on [database style merging of tables](https://pandas.pydata.org/docs/user_guide/merging.html#merging-join)
. Or have a look at the [comparison with SQL](https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html#compare-with-sql-join)
 page.

#### REMEMBER

*   Multiple tables can be concatenated column-wise or row-wise using the `concat` function.
    
*   For database-like merging/joining of tables, use the `merge` function.
    

To user guide

See the user guide for a full description of the various [facilities to combine data tables](https://pandas.pydata.org/docs/user_guide/merging.html#merging)
.

On this page