[Skip to main content](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/user_guide/user_defined_functions.html)
[3.1 (stable)](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/user_guide/user_defined_functions.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/user_defined_functions.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/user_guide/user_defined_functions.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/user_guide/user_defined_functions.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/user_defined_functions.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/user_guide/user_defined_functions.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/user_guide/user_defined_functions.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/user_guide/user_defined_functions.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/user_guide/user_defined_functions.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/user_defined_functions.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/user_guide/user_defined_functions.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

User-Defined Functions (UDFs)[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#user-defined-functions-udfs "Link to this heading")

===========================================================================================================================================================

In pandas, User-Defined Functions (UDFs) provide a way to extend the library’s functionality by allowing users to apply custom computations to their data. While pandas comes with a set of built-in functions for data manipulation, UDFs offer flexibility when built-in methods are not sufficient. These functions can be applied at different levels: element-wise, row-wise, column-wise, or group-wise, and behave differently depending on the method used.

Here’s a simple example to illustrate a UDF applied to a Series:

In \[1\]: s \= pd.Series(\[1, 2, 3\])

\# Simple UDF that adds 1 to a value
In \[2\]: def add\_one(x):
   ...:    return x + 1
   ...: 

\# Apply the function element-wise using .map
In \[3\]: s.map(add\_one)
Out\[3\]: 
0    2
1    3
2    4
dtype: int64

Copy to clipboard

Why Not To Use User-Defined Functions[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#why-not-to-use-user-defined-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

While UDFs provide flexibility, they come with significant drawbacks, primarily related to performance and behavior. When using UDFs, pandas must perform inference on the result, and that inference could be incorrect. Furthermore, unlike vectorized operations, UDFs are slower because pandas can’t optimize their computations, leading to inefficient processing.

Note

In general, most tasks can and should be accomplished using pandas’ built-in methods or vectorized operations.

Despite their drawbacks, UDFs can be helpful when:

*   **Custom Computations Are Needed**: Implementing complex logic or domain-specific calculations that pandas’ built-in methods cannot handle.
    
*   **Extending pandas’ Functionality**: Applying external libraries or specialized algorithms unavailable in pandas.
    
*   **Handling Complex Grouped Operations**: Performing operations on grouped data that standard methods do not support.
    

For example:

from sklearn.linear\_model import LinearRegression

\# Sample data
df \= pd.DataFrame({
    'group': \['A', 'A', 'A', 'B', 'B', 'B'\],
    'x': \[1, 2, 3, 1, 2, 3\],
    'y': \[2, 4, 6, 1, 2, 1.5\]
})

\# Function to fit a model to each group
def fit\_model(group):
    model \= LinearRegression()
    model.fit(group\[\['x'\]\], group\['y'\])
    group\['y\_pred'\] \= model.predict(group\[\['x'\]\])
    return group

result \= df.groupby('group').apply(fit\_model)

Copy to clipboard

Methods that support User-Defined Functions[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#methods-that-support-user-defined-functions "Link to this heading")

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

User-Defined Functions can be applied across various pandas methods:

| Method | Function Input | Function Output | Description |
| --- | --- | --- | --- |
| [Series.map() and DataFrame.map()](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#udf-map) | Scalar | Scalar | Apply a function to each element |
| [Series.apply() and DataFrame.apply()](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#udf-apply)<br> (axis=0) | Column (Series) | Column (Series) | Apply a function to each column |
| [Series.apply() and DataFrame.apply()](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#udf-apply)<br> (axis=1) | Row (Series) | Row (Series) | Apply a function to each row |
| [Series.pipe() and DataFrame.pipe()](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#udf-pipe) | Series or DataFrame | Series or DataFrame | Chain functions together to apply to Series or DataFrame |
| [Series.filter() and DataFrame.filter()](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#udf-filter) | Series or DataFrame | Boolean mask | Function is called with the object and returns a boolean mask; rows where the mask is `False` are removed from the result |
| [Series.agg() and DataFrame.agg()](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#udf-agg) | Series or DataFrame | Scalar or Series | Aggregate and summarize values, e.g., sum or custom reducer |
| [Series.transform() and DataFrame.transform()](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#udf-transform)<br> (axis=0) | Column (Series) | Column (Series) | Same as `apply()` with (axis=0), but it raises an exception if the function changes the shape of the data |
| [Series.transform() and DataFrame.transform()](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#udf-transform)<br> (axis=1) | Row (Series) | Row (Series) | Same as `apply()` with (axis=1), but it raises an exception if the function changes the shape of the data |

When applying UDFs in pandas, it is essential to select the appropriate method based on your specific task. Each method has its strengths and is designed for different use cases. Understanding the purpose and behavior of each method will help you make informed decisions, ensuring more efficient and maintainable code.

Note

Some of these methods can also be applied to groupby, resample, and various window objects. See [Group by: split-apply-combine](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby)
, [resample()](https://pandas.pydata.org/docs/user_guide/timeseries.html#timeseries)
, [rolling()](https://pandas.pydata.org/docs/user_guide/window.html#window)
, [expanding()](https://pandas.pydata.org/docs/user_guide/window.html#window)
, and [ewm()](https://pandas.pydata.org/docs/user_guide/window.html#window)
 for details.

### [`Series.map()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.map.html#pandas.Series.map "pandas.Series.map")
 and [`DataFrame.map()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html#pandas.DataFrame.map "pandas.DataFrame.map")
[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#series-map-and-dataframe-map "Link to this heading")

The `map()` method is used specifically to apply element-wise UDFs. This means the function will be called for each element in the `Series` or `DataFrame`, with the individual value or the cell as the function argument.

In \[4\]: temperature\_celsius \= pd.DataFrame({
   ...:    "NYC": \[14, 21, 23\],
   ...:    "Los Angeles": \[22, 28, 31\],
   ...: })
   ...: 

In \[5\]: def to\_fahrenheit(value):
   ...:    return value \* (9 / 5) + 32
   ...: 

In \[6\]: temperature\_celsius.map(to\_fahrenheit)
Out\[6\]: 
    NYC  Los Angeles
0  57.2         71.6
1  69.8         82.4
2  73.4         87.8

Copy to clipboard

In this example, the function `to_fahrenheit` will be called 6 times, once for each value in the `DataFrame`. And the result of each call will be returned in the corresponding cell of the resulting `DataFrame`.

In general, `map` will be slow, as it will not make use of vectorization. Instead, a Python function call for each value will be required, which will slow down things significantly if working with medium or large data.

When to use: Use `map()` for applying element-wise UDFs to DataFrames or Series.

### [`Series.apply()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.apply.html#pandas.Series.apply "pandas.Series.apply")
 and [`DataFrame.apply()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")
[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#series-apply-and-dataframe-apply "Link to this heading")

The `apply()` method allows you to apply UDFs for a whole column or row. This is different from `map()` in that the function will be called for each column (or row), not for each individual value.

In \[7\]: temperature\_celsius \= pd.DataFrame({
   ...:    "NYC": \[14, 21, 23\],
   ...:    "Los Angeles": \[22, 28, 31\],
   ...: })
   ...: 

In \[8\]: def to\_fahrenheit(column):
   ...:    return column \* (9 / 5) + 32
   ...: 

In \[9\]: temperature\_celsius.apply(to\_fahrenheit)
Out\[9\]: 
    NYC  Los Angeles
0  57.2         71.6
1  69.8         82.4
2  73.4         87.8

Copy to clipboard

In the example, `to_fahrenheit` will be called only twice, as opposed to the 6 times with `map()`. This will be faster than using `map()`, since the operations for each column are vectorized, and the overhead of iterating over data in Python and calling Python functions is significantly reduced.

In some cases, the function may require all the data to be able to compute the result. So `apply()` is needed, since with `map()` the function can only access one element at a time.

In \[10\]: temperature \= pd.DataFrame({
   ....:    "NYC": \[14, 21, 23\],
   ....:    "Los Angeles": \[22, 28, 31\],
   ....: })
   ....: 

In \[11\]: def normalize(column):
   ....:    return column / column.mean()
   ....: 

In \[12\]: temperature.apply(normalize)
Out\[12\]: 
        NYC  Los Angeles
0  0.724138     0.814815
1  1.086207     1.037037
2  1.189655     1.148148

Copy to clipboard

In the example, the `normalize` function needs to compute the mean of the whole column in order to divide each element by it. So, we cannot call the function for each element, but we need the function to receive the whole column.

`apply()` can also execute a function by row, by specifying `axis=1`.

In \[13\]: temperature \= pd.DataFrame({
   ....:    "NYC": \[14, 21, 23\],
   ....:    "Los Angeles": \[22, 28, 31\],
   ....: })
   ....: 

In \[14\]: def hotter(row):
   ....:    return row\["Los Angeles"\] \- row\["NYC"\]
   ....: 

In \[15\]: temperature.apply(hotter, axis\=1)
Out\[15\]: 
0    8
1    7
2    8
dtype: int64

Copy to clipboard

In the example, the function `hotter` will be called 3 times, once for each row. And each call will receive the whole row as the argument, allowing computations that require more than one value in the row.

`apply` is also available for `SeriesGroupBy.apply()`, `DataFrameGroupBy.apply()`, `Rolling.apply()`, `Expanding.apply()` and `Resampler.apply()`. You can read more about `apply` in groupby operations [Flexible apply](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-apply)
.

When to use: `apply()` is suitable when no alternative vectorized method or UDF method is available, but consider optimizing performance with vectorized operations wherever possible.

### [`Series.pipe()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.pipe.html#pandas.Series.pipe "pandas.Series.pipe")
 and [`DataFrame.pipe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe "pandas.DataFrame.pipe")
[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#series-pipe-and-dataframe-pipe "Link to this heading")

The `pipe` method is similar to `map` and `apply`, but the function receives the whole `Series` or `DataFrame` it is called on.

In \[16\]: temperature \= pd.DataFrame({
   ....:    "NYC": \[14, 21, 23\],
   ....:    "Los Angeles": \[22, 28, 31\],
   ....: })
   ....: 

In \[17\]: def normalize(df):
   ....:    return df / df.mean().mean()
   ....: 

In \[18\]: temperature.pipe(normalize)
Out\[18\]: 
        NYC  Los Angeles
0  0.604317     0.949640
1  0.906475     1.208633
2  0.992806     1.338129

Copy to clipboard

This is equivalent to calling the `normalize` function with the `DataFrame` as the parameter.

In \[19\]: normalize(temperature)
Out\[19\]: 
        NYC  Los Angeles
0  0.604317     0.949640
1  0.906475     1.208633
2  0.992806     1.338129

Copy to clipboard

The main advantage of using `pipe` is readability. It allows method chaining and clearer code when calling multiple functions.

In \[20\]: temperature\_celsius \= pd.DataFrame({
   ....:    "NYC": \[14, 21, 23\],
   ....:    "Los Angeles": \[22, 28, 31\],
   ....: })
   ....: 

In \[21\]: def multiply\_by\_9(value):
   ....:    return value \* 9
   ....: 

In \[22\]: def divide\_by\_5(value):
   ....:    return value / 5
   ....: 

In \[23\]: def add\_32(value):
   ....:    return value + 32
   ....: 

\# Without \`pipe\`:
In \[24\]: fahrenheit \= add\_32(divide\_by\_5(multiply\_by\_9(temperature\_celsius)))

\# With \`pipe\`:
In \[25\]: fahrenheit \= (temperature\_celsius.pipe(multiply\_by\_9)
   ....:                                 .pipe(divide\_by\_5)
   ....:                                 .pipe(add\_32))
   ....: 

Copy to clipboard

`pipe` is also available for `SeriesGroupBy.pipe()`, `DataFrameGroupBy.pipe()` and `Resampler.pipe()`. You can read more about `pipe` in groupby operations in [Piping function calls](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-pipe)
.

When to use: Use `pipe()` when you need to create a pipeline of operations and want to keep the code readable and maintainable.

### [`Series.filter()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.filter.html#pandas.Series.filter "pandas.Series.filter")
 and [`DataFrame.filter()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html#pandas.DataFrame.filter "pandas.DataFrame.filter")
[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#series-filter-and-dataframe-filter "Link to this heading")

The `filter` method is used to select a subset of rows that match certain criteria. [`Series.filter()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.filter.html#pandas.Series.filter "pandas.Series.filter")
 and [`DataFrame.filter()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.filter.html#pandas.DataFrame.filter "pandas.DataFrame.filter")
 accept a callable that is passed the object and returns a boolean mask; the rows where the mask is True are kept. This is convenient in a method chain where the intermediate object has no name.

In \[26\]: df \= pd.DataFrame({"a": \[1, 2, 3\], "b": \[4, 5, 6\]})

In \[27\]: df.assign(c\=df\["a"\] + df\["b"\]).filter(lambda df: df\["c"\] \> 5)
Out\[27\]: 
   a  b  c
1  2  5  7
2  3  6  9

Copy to clipboard

You can read more about filtering with a boolean mask in [Filtering with DataFrame.filter](https://pandas.pydata.org/docs/user_guide/indexing.html#indexing-boolean-filter)
. `SeriesGroupBy.filter()` and `DataFrameGroupBy.filter()` instead call the function once per group; you can read more about `filter` in groupby operations in [Filtration](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-filter)
.

### [`Series.agg()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.agg.html#pandas.Series.agg "pandas.Series.agg")
 and [`DataFrame.agg()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.agg.html#pandas.DataFrame.agg "pandas.DataFrame.agg")
[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#series-agg-and-dataframe-agg "Link to this heading")

The `agg` method is used to aggregate a set of data points into a single one. The most common aggregation functions such as `min`, `max`, `mean`, `sum`, etc. are already implemented in pandas. `agg` allows to implement other custom aggregate functions.

In \[28\]: temperature \= pd.DataFrame({
   ....:    "NYC": \[14, 21, 23\],
   ....:    "Los Angeles": \[22, 28, 31\],
   ....: })
   ....: 

In \[29\]: def highest\_jump(column):
   ....:    return column.pct\_change().max()
   ....: 

In \[30\]: temperature.agg(highest\_jump)
Out\[30\]: 
NYC            0.500000
Los Angeles    0.272727
dtype: float64

Copy to clipboard

When to use: Use `agg()` for performing custom aggregations, where the operation returns a scalar value on each input.

### [`Series.transform()`](https://pandas.pydata.org/docs/reference/api/pandas.Series.transform.html#pandas.Series.transform "pandas.Series.transform")
 and [`DataFrame.transform()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.transform.html#pandas.DataFrame.transform "pandas.DataFrame.transform")
[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#series-transform-and-dataframe-transform "Link to this heading")

The `transform` method is similar to an aggregation, with the difference that the result is broadcasted to the original data.

In \[31\]: temperature \= pd.DataFrame({
   ....:    "NYC": \[14, 21, 23\],
   ....:    "Los Angeles": \[22, 28, 31\]},
   ....:    index\=pd.date\_range("2000-01-01", "2000-01-03"))
   ....: 

In \[32\]: def warm\_up\_all\_days(column):
   ....:    return pd.Series(column.max(), index\=column.index)
   ....: 

In \[33\]: temperature.transform(warm\_up\_all\_days)
Out\[33\]: 
            NYC  Los Angeles
2000-01-01   23           31
2000-01-02   23           31
2000-01-03   23           31

Copy to clipboard

In the example, the `warm_up_all_days` function computes the `max` like an aggregation, but instead of returning just the maximum value, it returns a `DataFrame` with the same shape as the original one with the values of each day replaced by the maximum temperature of the city.

`transform` is also available for `SeriesGroupBy.transform()`, `DataFrameGroupBy.transform()` and `Resampler.transform()`, where it’s more common. You can read more about `transform` in groupby operations in [Transformation](https://pandas.pydata.org/docs/user_guide/groupby.html#groupby-transform)
.

When to use: When you need to perform an aggregation that will be returned in the original structure of the DataFrame.

Performance[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#performance "Link to this heading")

-------------------------------------------------------------------------------------------------------------------------

While UDFs provide flexibility, their use is generally discouraged as they can introduce performance issues, especially when written in pure Python. To improve efficiency, consider using built-in `NumPy` or `pandas` functions instead of UDFs for common operations.

Note

If performance is critical, explore **vectorized operations** before resorting to UDFs.

### Vectorized Operations[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#vectorized-operations "Link to this heading")

Below is a comparison of using UDFs versus using Vectorized Operations:

\# User-defined function
def calc\_ratio(row):
    return 100 \* (row\["one"\] / row\["two"\])

df\["new\_col"\] \= df.apply(calc\_ratio, axis\=1)

\# Vectorized Operation
df\["new\_col2"\] \= 100 \* (df\["one"\] / df\["two"\])

Copy to clipboard

Measuring how long each operation takes:

User-defined function:  5.6435 secs
Vectorized:             0.0043 secs

Copy to clipboard

Vectorized operations in pandas are significantly faster than using [`DataFrame.apply()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html#pandas.DataFrame.apply "pandas.DataFrame.apply")
 with UDFs because they leverage highly optimized C functions via `NumPy` to process entire arrays at once. This approach avoids the overhead of looping through rows in Python and making separate function calls for each row, which is slow and inefficient. Additionally, `NumPy` arrays benefit from memory efficiency and CPU-level optimizations, making vectorized operations the preferred choice whenever possible.

### Improving Performance with UDFs[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#improving-performance-with-udfs "Link to this heading")

In scenarios where UDFs are necessary, there are still ways to mitigate their performance drawbacks. One approach is to use **Numba**, a Just-In-Time (JIT) compiler that can significantly speed up numerical Python code by compiling Python functions to optimized machine code at runtime.

By annotating your UDFs with `@numba.jit`, you can achieve performance closer to vectorized operations, especially for computationally heavy tasks.

Note

You may also refer to the user guide on [Enhancing performance](https://pandas.pydata.org/docs/user_guide/enhancingperf.html#enhancingperf-numba)
 for a more detailed guide to using **Numba**.

### Using [`DataFrame.pipe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe "pandas.DataFrame.pipe")
 for Composable Logic[#](https://pandas.pydata.org/docs/user_guide/user_defined_functions.html#using-dataframe-pipe-for-composable-logic "Link to this heading")

Another useful pattern for improving readability and composability, especially when mixing vectorized logic with UDFs, is to use the [`DataFrame.pipe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe "pandas.DataFrame.pipe")
 method.

[`DataFrame.pipe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe "pandas.DataFrame.pipe")
 doesn’t improve performance directly, but it enables cleaner method chaining by passing the entire object into a function. This is especially helpful when chaining custom transformations:

def add\_ratio\_column(df):
    df\["ratio"\] \= 100 \* (df\["one"\] / df\["two"\])
    return df

df \= (
    df
    .query("one > 0")
    .pipe(add\_ratio\_column)
    .dropna()
)

Copy to clipboard

This is functionally equivalent to calling `add_ratio_column(df)`, but keeps your code clean and composable. The function you pass to [`DataFrame.pipe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe "pandas.DataFrame.pipe")
 can use vectorized operations, row-wise UDFs, or any other logic; [`DataFrame.pipe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe "pandas.DataFrame.pipe")
 is agnostic.

Note

While [`DataFrame.pipe()`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pipe.html#pandas.DataFrame.pipe "pandas.DataFrame.pipe")
 does not improve performance on its own, it promotes clean, modular design and allows both vectorized and UDF-based logic to be composed in method chains.

On this page