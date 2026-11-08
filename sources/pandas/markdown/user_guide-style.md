[Skip to main content](https://pandas.pydata.org/docs/user_guide/style.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/user_guide/style.html)
[3.1 (stable)](https://pandas.pydata.org/docs/user_guide/style.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/user_guide/style.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/user_guide/style.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/user_guide/style.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/user_guide/style.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/user_guide/style.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/user_guide/style.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/user_guide/style.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/user_guide/style.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/user_guide/style.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/user_guide/style.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/user_guide/style.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Table Visualization[#](https://pandas.pydata.org/docs/user_guide/style.html#Table-Visualization "Link to this heading")

========================================================================================================================

This section demonstrates visualization of tabular data using the [Styler](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html)
 class. For information on visualization with charting please see [Chart Visualization](https://pandas.pydata.org/docs/user_guide/visualization.html)
. This document is written as a Jupyter Notebook, and can be viewed or downloaded [here](https://nbviewer.org/github/pandas-dev/pandas/blob/main/doc/source/user_guide/style.ipynb)
.

Styler Object and Customising the Display[#](https://pandas.pydata.org/docs/user_guide/style.html#Styler-Object-and-Customising-the-Display "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Styling and output display customisation should be performed **after** the data in a DataFrame has been processed. The Styler is **not** dynamically updated if further changes to the DataFrame are made. The `DataFrame.style` attribute is a property that returns a [Styler](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html)
 object. It has a `_repr_html_` method defined on it so it is rendered automatically in Jupyter Notebook.

The Styler, which can be used for large data but is primarily designed for small data, currently has the ability to output to these formats:

*   HTML
    
*   LaTeX
    
*   String (and CSV by extension)
    
*   Excel
    
*   (JSON is not currently available)
    

The first three of these have display customisation methods designed to format and customise the output. These include:

*   Formatting values, the index and columns headers, using [.format()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format.html)
     and [.format\_index()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html)
    ,
    
*   Renaming the index or column header labels, using [.relabel\_index()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.relabel_index.html)
    
*   Hiding certain columns, the index and/or column headers, or index names, using [.hide()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html)
    
*   Concatenating similar DataFrames, using [.concat()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.concat.html)
    

Formatting the Display[#](https://pandas.pydata.org/docs/user_guide/style.html#Formatting-the-Display "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

### Formatting Values[#](https://pandas.pydata.org/docs/user_guide/style.html#Formatting-Values "Link to this heading")

The [Styler](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html)
 distinguishes the _display_ value from the _actual_ value, in both data values and index or columns headers. To control the display value, the text is printed in each cell as a string, and we can use the [.format()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format.html)
 and [.format\_index()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.format_index.html)
 methods to manipulate this according to a [format spec string](https://docs.python.org/3/library/string.html#format-specification-mini-language)
 or a callable that takes a single value and returns a string. It is possible to define this for the whole table, or index, or for individual columns, or MultiIndex levels. We can also overwrite index names.

Additionally, the format function has a **precision** argument to specifically help format floats, as well as **decimal** and **thousands** separators to support other locales, an **na\_rep** argument to display missing data, and an **escape** and **hyperlinks** arguments to help displaying safe-HTML or safe-LaTeX. The default formatter is configured to adopt pandas’ global options such as `styler.format.precision` option, controllable using `with pd.option_context('format.precision', 2):`

\[1\]:

Copy to clipboard

import pandas as pd
import numpy as np

df \= pd.DataFrame(
    {"strings": \["Adam", "Mike"\], "ints": \[1, 3\], "floats": \[1.123, 1000.23\]}
)
df.style.format(precision\=3, thousands\=".", decimal\=",").format\_index(
    str.upper, axis\=1
).relabel\_index(\["row 1", "row 2"\], axis\=0)

Copy to clipboard

\[1\]:

Copy to clipboard

|     | STRINGS | INTS | FLOATS |
| --- | --- | --- | --- |
| row 1 | Adam | 1   | 1,123 |
| row 2 | Mike | 3   | 1.000,230 |

Using Styler to manipulate the display is a useful feature because maintaining the indexing and data values for other purposes gives greater control. You do not have to overwrite your DataFrame to display it how you like. Here is a more comprehensive example of using the formatting functions whilst still relying on the underlying data for indexing and calculations.

\[2\]:

Copy to clipboard

weather\_df \= pd.DataFrame(
    np.random.default\_rng().random((10, 2)) \* 5,
    index\=pd.date\_range(start\="2021-01-01", periods\=10),
    columns\=\["Tokyo", "Beijing"\],
)

def rain\_condition(v):
    if v < 1.75:
        return "Dry"
    elif v < 2.75:
        return "Rain"
    return "Heavy Rain"

def make\_pretty(styler):
    styler.set\_caption("Weather Conditions")
    styler.format(rain\_condition)
    styler.format\_index(lambda v: v.strftime("%A"))
    styler.background\_gradient(axis\=None, vmin\=1, vmax\=5, cmap\="YlGnBu")
    return styler

weather\_df

Copy to clipboard

\[2\]:

Copy to clipboard

|     | Tokyo | Beijing |
| --- | --- | --- |
| 2021-01-01 | 3.505840 | 1.360278 |
| 2021-01-02 | 4.868388 | 2.019062 |
| 2021-01-03 | 0.193992 | 3.612673 |
| 2021-01-04 | 3.802126 | 3.454835 |
| 2021-01-05 | 1.903940 | 0.398498 |
| 2021-01-06 | 4.214982 | 0.937454 |
| 2021-01-07 | 2.524028 | 3.168416 |
| 2021-01-08 | 1.092395 | 2.205170 |
| 2021-01-09 | 4.551873 | 4.468072 |
| 2021-01-10 | 4.455735 | 4.483489 |

\[3\]:

Copy to clipboard

weather\_df.loc\["2021-01-04":"2021-01-08"\].style.pipe(make\_pretty)

Copy to clipboard

\[3\]:

Copy to clipboard

|     |     |     |
| --- | --- | --- |Weather Conditions
|     | Tokyo | Beijing |
| --- | --- | --- |
| Monday | Heavy Rain | Heavy Rain |
| Tuesday | Rain | Dry |
| Wednesday | Heavy Rain | Dry |
| Thursday | Rain | Heavy Rain |
| Friday | Dry | Rain |

### Hiding Data[#](https://pandas.pydata.org/docs/user_guide/style.html#Hiding-Data "Link to this heading")

The index and column headers can be completely hidden, as well subselecting rows or columns that one wishes to exclude. Both these options are performed using the same methods.

The index can be hidden from rendering by calling [.hide()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html)
 without any arguments, which might be useful if your index is integer based. Similarly column headers can be hidden by calling [.hide(axis=”columns”)](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html)
 without any further arguments.

Specific rows or columns can be hidden from rendering by calling the same [.hide()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html)
 method and passing in a row/column label, a list-like or a slice of row/column labels to for the `subset` argument.

Hiding does not change the integer arrangement of CSS classes, e.g. hiding the first two columns of a DataFrame means the column class indexing will still start at `col2`, since `col0` and `col1` are simply ignored.

\[4\]:

Copy to clipboard

df \= pd.DataFrame(np.random.default\_rng().standard\_normal((5, 5)))
df.style.hide(subset\=\[0, 2, 4\], axis\=0).hide(subset\=\[0, 2, 4\], axis\=1)

Copy to clipboard

\[4\]:

Copy to clipboard

|     | 1   | 3   |
| --- | --- | --- |
| 1   | 1.377970 | 1.214077 |
| 3   | 0.175492 | 0.127444 |

To invert the function to a **show** functionality it is best practice to compose a list of hidden items.

\[5\]:

Copy to clipboard

show \= \[0, 2, 4\]
df.style.hide(\[row for row in df.index if row not in show\], axis\=0).hide(
    \[col for col in df.columns if col not in show\], axis\=1
)

Copy to clipboard

\[5\]:

Copy to clipboard

|     | 0   | 2   | 4   |
| --- | --- | --- | --- |
| 0   | 0.534579 | \-2.198992 | 1.620373 |
| 2   | \-0.571371 | 0.265066 | 0.169907 |
| 4   | 0.097859 | 1.659162 | \-2.788493 |

### Concatenating DataFrame Outputs[#](https://pandas.pydata.org/docs/user_guide/style.html#Concatenating-DataFrame-Outputs "Link to this heading")

Two or more Stylers can be concatenated together provided they share the same columns. This is very useful for showing summary statistics for a DataFrame, and is often used in combination with DataFrame.agg.

Since the objects concatenated are Stylers they can independently be styled as will be shown below and their concatenation preserves those styles.

\[6\]:

Copy to clipboard

summary\_styler \= (
    df.agg(\["sum", "mean"\]).style.format(precision\=3).relabel\_index(\["Sum", "Average"\])
)
df.style.format(precision\=1).concat(summary\_styler)

Copy to clipboard

\[6\]:

Copy to clipboard

|     | 0   | 1   | 2   | 3   | 4   |
| --- | --- | --- | --- | --- | --- |
| 0   | 0.5 | 0.0 | \-2.2 | 0.5 | 1.6 |
| 1   | 0.2 | 1.4 | 0.2 | 1.2 | 0.9 |
| 2   | \-0.6 | \-1.5 | 0.3 | \-0.6 | 0.2 |
| 3   | \-0.1 | 0.2 | 1.2 | 0.1 | \-0.5 |
| 4   | 0.1 | 0.1 | 1.7 | 1.5 | \-2.8 |
| Sum | 0.161 | 0.092 | 1.174 | 2.791 | \-0.534 |
| Average | 0.032 | 0.018 | 0.235 | 0.558 | \-0.107 |

Styler Object and HTML[#](https://pandas.pydata.org/docs/user_guide/style.html#Styler-Object-and-HTML "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

The [Styler](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html)
 was originally constructed to support the wide array of HTML formatting options. Its HTML output creates an HTML `<table>` and leverages CSS styling language to manipulate many parameters including colors, fonts, borders, background, etc. See [here](https://www.w3schools.com/html/html_tables.asp)
 for more information on styling HTML tables. This allows a lot of flexibility out of the box, and even enables web developers to integrate DataFrames into their existing user interface designs.

Below we demonstrate the default output, which looks very similar to the standard DataFrame HTML representation. But the HTML here has already attached some CSS classes to each cell, even if we haven’t yet created any styles. We can view these by calling the [.to\_html()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_html.html)
 method, which returns the raw HTML as string, which is useful for further processing or adding to a file - read on in [More about CSS and HTML](https://pandas.pydata.org/docs/user_guide/style.html#More-About-CSS-and-HTML)
. This section will also provide a walkthrough for how to convert this default output to represent a DataFrame output that is more communicative. For example how we can build `s`:

\[7\]:

Copy to clipboard

idx \= pd.Index(\["Tumour (Positive)", "Non-Tumour (Negative)"\], name\="Actual Label:")
cols \= pd.MultiIndex.from\_product(
    \[\["Decision Tree", "Regression", "Random"\], \["Tumour", "Non-Tumour"\]\],
    names\=\["Model:", "Predicted:"\],
)
df \= pd.DataFrame(
    \[\[38.0, 2.0, 18.0, 22.0, 21, np.nan\], \[19, 439, 6, 452, 226, 232\]\],
    index\=idx,
    columns\=cols,
)
df.style

Copy to clipboard

\[7\]:

Copy to clipboard

| Model: | Decision Tree |     | Regression |     | Random |     |
| --- | --- | --- | --- | --- | --- | --- |
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour | Tumour | Non-Tumour |
| --- | --- | --- | --- | --- | --- | --- |
| Actual Label: |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
| Tumour (Positive) | 38.000000 | 2.000000 | 18.000000 | 22.000000 | 21  | nan |
| Non-Tumour (Negative) | 19.000000 | 439.000000 | 6.000000 | 452.000000 | 226 | 232.000000 |

\[9\]:

Copy to clipboard

s

Copy to clipboard

\[9\]:

Copy to clipboard

|     |     |     |     |     |
| --- | --- | --- | --- | --- |Confusion matrix for multiple cancer prediction models.
| Model: | Decision Tree |     | Regression |     |
| --- | --- | --- | --- | --- |
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour |
| --- | --- | --- | --- | --- |
| Actual Label: |     |     |     |     |
| --- | --- | --- | --- | --- |
| Tumour (Positive) | 38  | 2   | 18  | 22  |
| Non-Tumour (Negative) | 19  | 439 | 6   | 452 |

The first step we have taken is the create the Styler object from the DataFrame and then select the range of interest by hiding unwanted columns with [.hide()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.hide.html)
.

\[10\]:

Copy to clipboard

s \= df.style.format("{:.0f}").hide(
    \[("Random", "Tumour"), ("Random", "Non-Tumour")\], axis\="columns"
)
s

Copy to clipboard

\[10\]:

Copy to clipboard

| Model: | Decision Tree |     | Regression |     |
| --- | --- | --- | --- | --- |
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour |
| --- | --- | --- | --- | --- |
| Actual Label: |     |     |     |     |
| --- | --- | --- | --- | --- |
| Tumour (Positive) | 38  | 2   | 18  | 22  |
| Non-Tumour (Negative) | 19  | 439 | 6   | 452 |

Methods to Add Styles[#](https://pandas.pydata.org/docs/user_guide/style.html#Methods-to-Add-Styles "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

There are **3 primary methods of adding custom CSS styles** to [Styler](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html)
:

*   Using [.set\_table\_styles()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
     to control broader areas of the table with specified internal CSS. Although table styles allow the flexibility to add CSS selectors and properties controlling all individual parts of the table, they are unwieldy for individual cell specifications. Also, note that table styles cannot be exported to Excel.
    
*   Using [.set\_td\_classes()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
     to directly link either external CSS classes to your data cells or link the internal CSS classes created by [.set\_table\_styles()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
    . See [here](https://pandas.pydata.org/docs/user_guide/style.html#Setting-Classes-and-Linking-to-External-CSS)
    . These cannot be used on column header rows or indexes, and also won’t export to Excel.
    
*   Using the [.apply()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html)
     and [.map()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html)
     functions to add direct internal CSS to specific data cells. See [here](https://pandas.pydata.org/docs/user_guide/style.html#Styler-Functions)
    . As of v1.4.0 there are also methods that work directly on column header rows or indexes: [.apply\_index()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply_index.html)
     and [.map\_index()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map_index.html)
    . Note that only these methods add styles that will export to Excel. These methods work in a similar way to [DataFrame.apply()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.apply.html)
     and [DataFrame.map()](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.map.html)
    .
    

Table Styles[#](https://pandas.pydata.org/docs/user_guide/style.html#Table-Styles "Link to this heading")

----------------------------------------------------------------------------------------------------------

Table styles are flexible enough to control all individual parts of the table, including column headers and indexes. However, they can be unwieldy to type for individual data cells or for any kind of conditional formatting, so we recommend that table styles are used for broad styling, such as entire rows or columns at a time.

Table styles are also used to control features which can apply to the whole table at once such as creating a generic hover functionality. The `:hover` pseudo-selector, as well as other pseudo-selectors, can only be used this way.

To replicate the normal format of CSS selectors and properties (attribute value pairs), e.g.

tr:hover {
  background-color: #ffff99;
}

Copy to clipboard

the necessary format to pass styles to [.set\_table\_styles()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
 is as a list of dicts, each with a CSS-selector tag and CSS-properties. Properties can either be a list of 2-tuples, or a regular CSS-string, for example:

\[12\]:

Copy to clipboard

cell\_hover \= {  \# for row hover use <tr> instead of <td>
    "selector": "td:hover",
    "props": \[("background-color", "#ffffb3")\],
}
index\_names \= {
    "selector": ".index\_name",
    "props": "font-style: italic; color: darkgrey; font-weight:normal;",
}
headers \= {
    "selector": "th:not(.index\_name)",
    "props": "background-color: #000066; color: white;",
}
s.set\_table\_styles(\[cell\_hover, index\_names, headers\])

Copy to clipboard

\[12\]:

Copy to clipboard

| Model: | Decision Tree |     | Regression |     |
| --- | --- | --- | --- | --- |
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour |
| --- | --- | --- | --- | --- |
| Actual Label: |     |     |     |     |
| --- | --- | --- | --- | --- |
| Tumour (Positive) | 38  | 2   | 18  | 22  |
| Non-Tumour (Negative) | 19  | 439 | 6   | 452 |

Next we just add a couple more styling artifacts targeting specific parts of the table. Be careful here, since we are _chaining methods_ we need to explicitly instruct the method **not to** `overwrite` the existing styles.

\[14\]:

Copy to clipboard

s.set\_table\_styles(
    \[\
        {"selector": "th.col\_heading", "props": "text-align: center;"},\
        {"selector": "th.col\_heading.level0", "props": "font-size: 1.5em;"},\
        {"selector": "td", "props": "text-align: center; font-weight: bold;"},\
    \],
    overwrite\=False,
)

Copy to clipboard

\[14\]:

Copy to clipboard

| Model: | Decision Tree |     | Regression |     |
| --- | --- | --- | --- | --- |
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour |
| --- | --- | --- | --- | --- |
| Actual Label: |     |     |     |     |
| --- | --- | --- | --- | --- |
| Tumour (Positive) | 38  | 2   | 18  | 22  |
| Non-Tumour (Negative) | 19  | 439 | 6   | 452 |

As a convenience method (_since version 1.2.0_) we can also pass a **dict** to [.set\_table\_styles()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_styles.html)
 which contains row or column keys. Behind the scenes Styler just indexes the keys and adds relevant `.col<m>` or `.row<n>` classes as necessary to the given CSS selectors.

\[16\]:

Copy to clipboard

s.set\_table\_styles(
    {
        ("Regression", "Tumour"): \[\
            {"selector": "th", "props": "border-left: 1px solid white"},\
            {"selector": "td", "props": "border-left: 1px solid #000066"},\
        \]
    },
    overwrite\=False,
    axis\=0,
)

Copy to clipboard

\[16\]:

Copy to clipboard

| Model: | Decision Tree |     | Regression |     |
| --- | --- | --- | --- | --- |
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour |
| --- | --- | --- | --- | --- |
| Actual Label: |     |     |     |     |
| --- | --- | --- | --- | --- |
| Tumour (Positive) | 38  | 2   | 18  | 22  |
| Non-Tumour (Negative) | 19  | 439 | 6   | 452 |

Setting Classes and Linking to External CSS[#](https://pandas.pydata.org/docs/user_guide/style.html#Setting-Classes-and-Linking-to-External-CSS "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------------------------

If you have designed a website then it is likely you will already have an external CSS file that controls the styling of table and cell objects within it. You may want to use these native files rather than duplicate all the CSS in python (and duplicate any maintenance work).

### Table Attributes[#](https://pandas.pydata.org/docs/user_guide/style.html#Table-Attributes "Link to this heading")

It is very easy to add a `class` to the main `<table>` using [.set\_table\_attributes()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_table_attributes.html)
. This method can also attach inline styles - read more in [CSS Hierarchies](https://pandas.pydata.org/docs/user_guide/style.html#CSS-Hierarchies)
.

\[18\]:

Copy to clipboard

out \= s.set\_table\_attributes('class="my-table-cls"').to\_html()
print(out\[out.find("<table") :\]\[:109\])

Copy to clipboard

<table id="T\_xyz01" class="my-table-cls">
  <thead>
    <tr>
      <th class="index\_name level0" >Model:</th>

Copy to clipboard

### Data Cell CSS Classes[#](https://pandas.pydata.org/docs/user_guide/style.html#Data-Cell-CSS-Classes "Link to this heading")

_New in version 1.2.0_

The [.set\_td\_classes()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_td_classes.html)
 method accepts a DataFrame with matching indices and columns to the underlying [Styler](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.html)
’s DataFrame. That DataFrame will contain strings as css-classes to add to individual data cells: the `<td>` elements of the `<table>`. Rather than use external CSS we will create our classes internally and add them to table style. We will save adding the borders until the [section on tooltips](https://pandas.pydata.org/docs/user_guide/style.html#Tooltips-and-Captions)
.

\[19\]:

Copy to clipboard

s.set\_table\_styles(
    \[  \# create internal CSS classes\
        {"selector": ".true", "props": "background-color: #e6ffe6;"},\
        {"selector": ".false", "props": "background-color: #ffe6e6;"},\
    \],
    overwrite\=False,
)
cell\_color \= pd.DataFrame(
    \[\["true ", "false ", "true ", "false "\], \["false ", "true ", "false ", "true "\]\],
    index\=df.index,
    columns\=df.columns\[:4\],
)
s.set\_td\_classes(cell\_color)

Copy to clipboard

\[19\]:

Copy to clipboard

| Model: | Decision Tree |     | Regression |     |
| --- | --- | --- | --- | --- |
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour |
| --- | --- | --- | --- | --- |
| Actual Label: |     |     |     |     |
| --- | --- | --- | --- | --- |
| Tumour (Positive) | 38  | 2   | 18  | 22  |
| Non-Tumour (Negative) | 19  | 439 | 6   | 452 |

Styler Functions[#](https://pandas.pydata.org/docs/user_guide/style.html#Styler-Functions "Link to this heading")

------------------------------------------------------------------------------------------------------------------

### Acting on Data[#](https://pandas.pydata.org/docs/user_guide/style.html#Acting-on-Data "Link to this heading")

We use the following methods to pass your style functions. Both of those methods take a function (and some other keyword arguments) and apply it to the DataFrame in a certain way, rendering CSS styles.

*   [.map()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map.html)
     (elementwise): accepts a function that takes a single value and returns a string with the CSS attribute-value pair.
    
*   [.apply()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply.html)
     (column-/row-/table-wise): accepts a function that takes a Series or DataFrame and returns a Series, DataFrame, or numpy array with an identical shape where each element is a string with a CSS attribute-value pair. This method passes each column or row of your DataFrame one-at-a-time or the entire table at once, depending on the `axis` keyword argument. For columnwise use `axis=0`, rowwise use `axis=1`, and for the entire table at once use `axis=None`.
    

This method is powerful for applying multiple, complex logic to data cells. We create a new DataFrame to demonstrate this.

\[21\]:

Copy to clipboard

df2 \= pd.DataFrame(
    np.random.default\_rng(0).standard\_normal((10, 4)), columns\=\["A", "B", "C", "D"\]
)
df2.style

Copy to clipboard

\[21\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | 0.640423 | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | 1.042513 |
| 5   | \-0.128535 | 1.366463 | \-0.665195 | 0.351510 |
| 6   | 0.903470 | 0.094012 | \-0.743499 | \-0.921725 |
| 7   | \-0.457726 | 0.220195 | \-1.009618 | \-0.209176 |
| 8   | \-0.159225 | 0.540846 | 0.214659 | 0.355373 |
| 9   | \-0.653829 | \-0.129614 | 0.783975 | 1.493431 |

For example we can build a function that colors text if it is negative, and chain this with a function that partially fades cells of negligible value. Since this looks at each element in turn we use `map`.

\[22\]:

Copy to clipboard

def style\_negative(v, props\=""):
    return props if v < 0 else None

s2 \= df2.style.map(style\_negative, props\="color:red;").map(
    lambda v: "opacity: 20%;" if (v < 0.3) and (v \> \-0.3) else None
)
s2

Copy to clipboard

\[22\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | 0.640423 | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | 1.042513 |
| 5   | \-0.128535 | 1.366463 | \-0.665195 | 0.351510 |
| 6   | 0.903470 | 0.094012 | \-0.743499 | \-0.921725 |
| 7   | \-0.457726 | 0.220195 | \-1.009618 | \-0.209176 |
| 8   | \-0.159225 | 0.540846 | 0.214659 | 0.355373 |
| 9   | \-0.653829 | \-0.129614 | 0.783975 | 1.493431 |

We can also build a function that highlights the maximum value across rows, cols, and the DataFrame all at once. In this case we use `apply`. Below we highlight the maximum in a column.

\[24\]:

Copy to clipboard

def highlight\_max(s, props\=""):
    return np.where(s \== np.nanmax(s.values), props, "")

s2.apply(highlight\_max, props\="color:white;background-color:darkblue", axis\=0)

Copy to clipboard

\[24\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | 0.640423 | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | 1.042513 |
| 5   | \-0.128535 | 1.366463 | \-0.665195 | 0.351510 |
| 6   | 0.903470 | 0.094012 | \-0.743499 | \-0.921725 |
| 7   | \-0.457726 | 0.220195 | \-1.009618 | \-0.209176 |
| 8   | \-0.159225 | 0.540846 | 0.214659 | 0.355373 |
| 9   | \-0.653829 | \-0.129614 | 0.783975 | 1.493431 |

We can use the same function across the different axes, highlighting here the DataFrame maximum in purple, and row maximums in pink.

\[26\]:

Copy to clipboard

s2.apply(highlight\_max, props\="color:white;background-color:pink;", axis\=1).apply(
    highlight\_max, props\="color:white;background-color:purple", axis\=None
)

Copy to clipboard

\[26\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | 0.640423 | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | 1.042513 |
| 5   | \-0.128535 | 1.366463 | \-0.665195 | 0.351510 |
| 6   | 0.903470 | 0.094012 | \-0.743499 | \-0.921725 |
| 7   | \-0.457726 | 0.220195 | \-1.009618 | \-0.209176 |
| 8   | \-0.159225 | 0.540846 | 0.214659 | 0.355373 |
| 9   | \-0.653829 | \-0.129614 | 0.783975 | 1.493431 |

This last example shows how some styles have been overwritten by others. In general the most recent style applied is active but you can read more in the [section on CSS hierarchies](https://pandas.pydata.org/docs/user_guide/style.html#CSS-Hierarchies)
. You can also apply these styles to more granular parts of the DataFrame - read more in section on [subset slicing](https://pandas.pydata.org/docs/user_guide/style.html#Finer-Control-with-Slicing)
.

It is possible to replicate some of this functionality using just classes but it can be more cumbersome. See [item 3) of Optimization](https://pandas.pydata.org/docs/user_guide/style.html#Optimization)

_Debugging Tip_: If you’re having trouble writing your style function, try just passing it into `DataFrame.apply`. Internally, `Styler.apply` uses `DataFrame.apply` so the result should be the same, and with `DataFrame.apply` you will be able to inspect the CSS string output of your intended function in each cell.

### Acting on the Index and Column Headers[#](https://pandas.pydata.org/docs/user_guide/style.html#Acting-on-the-Index-and-Column-Headers "Link to this heading")

Similar application is achieved for headers by using:

*   [.map\_index()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.map_index.html)
     (elementwise): accepts a function that takes a single value and returns a string with the CSS attribute-value pair.
    
*   [.apply\_index()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.apply_index.html)
     (level-wise): accepts a function that takes a Series and returns a Series, or numpy array with an identical shape where each element is a string with a CSS attribute-value pair. This method passes each level of your Index one-at-a-time. To style the index use `axis=0` and to style the column headers use `axis=1`.
    

You can select a `level` of a `MultiIndex` but currently no similar `subset` application is available for these methods.

\[28\]:

Copy to clipboard

s2.map\_index(lambda v: "color:pink;" if v \> 4 else "color:darkblue;", axis\=0)
s2.apply\_index(
    lambda s: np.where(s.isin(\["A", "B"\]), "color:pink;", "color:darkblue;"), axis\=1
)

Copy to clipboard

\[28\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | 0.640423 | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | 1.042513 |
| 5   | \-0.128535 | 1.366463 | \-0.665195 | 0.351510 |
| 6   | 0.903470 | 0.094012 | \-0.743499 | \-0.921725 |
| 7   | \-0.457726 | 0.220195 | \-1.009618 | \-0.209176 |
| 8   | \-0.159225 | 0.540846 | 0.214659 | 0.355373 |
| 9   | \-0.653829 | \-0.129614 | 0.783975 | 1.493431 |

Tooltips and Captions[#](https://pandas.pydata.org/docs/user_guide/style.html#Tooltips-and-Captions "Link to this heading")

----------------------------------------------------------------------------------------------------------------------------

Table captions can be added with the [.set\_caption()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_caption.html)
 method. You can use table styles to control the CSS relevant to the caption.

\[29\]:

Copy to clipboard

s.set\_caption(
    "Confusion matrix for multiple cancer prediction models."
).set\_table\_styles(
    \[{"selector": "caption", "props": "caption-side: bottom; font-size:1.25em;"}\],
    overwrite\=False,
)

Copy to clipboard

\[29\]:

Copy to clipboard

|     |     |     |     |     |
| --- | --- | --- | --- | --- |Confusion matrix for multiple cancer prediction models.
| Model: | Decision Tree |     | Regression |     |
| --- | --- | --- | --- | --- |
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour |
| --- | --- | --- | --- | --- |
| Actual Label: |     |     |     |     |
| --- | --- | --- | --- | --- |
| Tumour (Positive) | 38  | 2   | 18  | 22  |
| Non-Tumour (Negative) | 19  | 439 | 6   | 452 |

Adding tooltips (_since version 1.3.0_) can be done using the [.set\_tooltips()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_tooltips.html)
 method in the same way you can add CSS classes to data cells by providing a string based DataFrame with intersecting indices and columns. You don’t have to specify a `css_class` name or any css `props` for the tooltips, since there are standard defaults, but the option is there if you want more visual control.

\[31\]:

Copy to clipboard

tt \= pd.DataFrame(
    \[\
        \[\
            "This model has a very strong true positive rate",\
            "This model's total number of false negatives is too high",\
        \]\
    \],
    index\=\["Tumour (Positive)"\],
    columns\=df.columns\[\[0, 3\]\],
)
s.set\_tooltips(
    tt,
    props\="visibility: hidden; position: absolute; z-index: 1; "
    "border: 1px solid #000066;"
    "background-color: white; color: #000066; font-size: 0.8em;"
    "transform: translate(0px, -24px); padding: 0.6em; "
    "border-radius: 0.5em;",
)

Copy to clipboard

\[31\]:

Copy to clipboard

|     |     |     |     |     |
| --- | --- | --- | --- | --- |Confusion matrix for multiple cancer prediction models.
| Model: | Decision Tree |     | Regression |     |
| --- | --- | --- | --- | --- |
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour |
| --- | --- | --- | --- | --- |
| Actual Label: |     |     |     |     |
| --- | --- | --- | --- | --- |
| Tumour (Positive) | 38  | 2   | 18  | 22  |
| Non-Tumour (Negative) | 19  | 439 | 6   | 452 |

The only thing left to do for our table is to add the highlighting borders to draw the audience attention to the tooltips. We will create internal CSS classes as before using table styles. **Setting classes always overwrites** so we need to make sure we add the previous classes.

\[33\]:

Copy to clipboard

s.set\_table\_styles(
    \[  \# create internal CSS classes\
        {"selector": ".border-red", "props": "border: 2px dashed red;"},\
        {"selector": ".border-green", "props": "border: 2px dashed green;"},\
    \],
    overwrite\=False,
)
cell\_border \= pd.DataFrame(
    \[\["border-green ", " ", " ", "border-red "\], \[" ", " ", " ", " "\]\],
    index\=df.index,
    columns\=df.columns\[:4\],
)
s.set\_td\_classes(cell\_color + cell\_border)

Copy to clipboard

\[33\]:

Copy to clipboard

|     |     |     |     |     |
| --- | --- | --- | --- | --- |Confusion matrix for multiple cancer prediction models.
| Model: | Decision Tree |     | Regression |     |
| --- | --- | --- | --- | --- |
| Predicted: | Tumour | Non-Tumour | Tumour | Non-Tumour |
| --- | --- | --- | --- | --- |
| Actual Label: |     |     |     |     |
| --- | --- | --- | --- | --- |
| Tumour (Positive) | 38  | 2   | 18  | 22  |
| Non-Tumour (Negative) | 19  | 439 | 6   | 452 |

Finer Control with Slicing[#](https://pandas.pydata.org/docs/user_guide/style.html#Finer-Control-with-Slicing "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

The examples we have shown so far for the `Styler.apply` and `Styler.map` functions have not demonstrated the use of the `subset` argument. This is a useful argument which permits a lot of flexibility: it allows you to apply styles to specific rows or columns, without having to code that logic into your `style` function.

The value passed to `subset` behaves similar to slicing a DataFrame;

*   A scalar is treated as a column label
    
*   A list (or Series or NumPy array) is treated as multiple column labels
    
*   A tuple is treated as `(row_indexer, column_indexer)`
    

Consider using `pd.IndexSlice` to construct the tuple for the last one. We will create a MultiIndexed DataFrame to demonstrate the functionality.

\[35\]:

Copy to clipboard

df3 \= pd.DataFrame(
    np.random.default\_rng().standard\_normal((4, 4)),
    pd.MultiIndex.from\_product(\[\["A", "B"\], \["r1", "r2"\]\]),
    columns\=\["c1", "c2", "c3", "c4"\],
)
df3

Copy to clipboard

\[35\]:

Copy to clipboard

|     |     | c1  | c2  | c3  | c4  |
| --- | --- | --- | --- | --- | --- |
| A   | r1  | 1.659801 | 0.514933 | \-0.117619 | \-1.451866 |
| r2  | \-0.439634 | 1.374616 | \-0.349268 | 0.237399 |
| B   | r1  | \-0.533508 | 0.099571 | \-1.088552 | \-0.391217 |
| r2  | \-0.541924 | \-1.357582 | \-0.025377 | 0.829804 |

We will use subset to highlight the maximum in the third and fourth columns with red text. We will highlight the subset sliced region in yellow.

\[36\]:

Copy to clipboard

slice\_ \= \["c3", "c4"\]
df3.style.apply(
    highlight\_max, props\="color:red;", axis\=0, subset\=slice\_
).set\_properties(\*\*{"background-color": "#ffffb3"}, subset\=slice\_)

Copy to clipboard

\[36\]:

Copy to clipboard

|     |     | c1  | c2  | c3  | c4  |
| --- | --- | --- | --- | --- | --- |
| A   | r1  | 1.659801 | 0.514933 | \-0.117619 | \-1.451866 |
| r2  | \-0.439634 | 1.374616 | \-0.349268 | 0.237399 |
| B   | r1  | \-0.533508 | 0.099571 | \-1.088552 | \-0.391217 |
| r2  | \-0.541924 | \-1.357582 | \-0.025377 | 0.829804 |

If combined with the `IndexSlice` as suggested then it can index across both dimensions with greater flexibility.

\[37\]:

Copy to clipboard

idx \= pd.IndexSlice
slice\_ \= idx\[idx\[:, "r1"\], idx\["c2":"c4"\]\]
df3.style.apply(
    highlight\_max, props\="color:red;", axis\=0, subset\=slice\_
).set\_properties(\*\*{"background-color": "#ffffb3"}, subset\=slice\_)

Copy to clipboard

\[37\]:

Copy to clipboard

|     |     | c1  | c2  | c3  | c4  |
| --- | --- | --- | --- | --- | --- |
| A   | r1  | 1.659801 | 0.514933 | \-0.117619 | \-1.451866 |
| r2  | \-0.439634 | 1.374616 | \-0.349268 | 0.237399 |
| B   | r1  | \-0.533508 | 0.099571 | \-1.088552 | \-0.391217 |
| r2  | \-0.541924 | \-1.357582 | \-0.025377 | 0.829804 |

This also provides the flexibility to sub select rows when used with the `axis=1`.

\[38\]:

Copy to clipboard

slice\_ \= idx\[idx\[:, "r2"\], :\]
df3.style.apply(
    highlight\_max, props\="color:red;", axis\=1, subset\=slice\_
).set\_properties(\*\*{"background-color": "#ffffb3"}, subset\=slice\_)

Copy to clipboard

\[38\]:

Copy to clipboard

|     |     | c1  | c2  | c3  | c4  |
| --- | --- | --- | --- | --- | --- |
| A   | r1  | 1.659801 | 0.514933 | \-0.117619 | \-1.451866 |
| r2  | \-0.439634 | 1.374616 | \-0.349268 | 0.237399 |
| B   | r1  | \-0.533508 | 0.099571 | \-1.088552 | \-0.391217 |
| r2  | \-0.541924 | \-1.357582 | \-0.025377 | 0.829804 |

There is also scope to provide **conditional filtering**.

Suppose we want to highlight the maximum across columns 2 and 4 only in the case that the sum of columns 1 and 3 is less than -2.0 _(essentially excluding rows_ `(:,'r2')`_)_.

\[39\]:

Copy to clipboard

slice\_ \= idx\[idx\[(df3\["c1"\] + df3\["c3"\]) < \-2.0\], \["c2", "c4"\]\]
df3.style.apply(
    highlight\_max, props\="color:red;", axis\=1, subset\=slice\_
).set\_properties(\*\*{"background-color": "#ffffb3"}, subset\=slice\_)

Copy to clipboard

\[39\]:

Copy to clipboard

|     |     | c1  | c2  | c3  | c4  |
| --- | --- | --- | --- | --- | --- |
| A   | r1  | 1.659801 | 0.514933 | \-0.117619 | \-1.451866 |
| r2  | \-0.439634 | 1.374616 | \-0.349268 | 0.237399 |
| B   | r1  | \-0.533508 | 0.099571 | \-1.088552 | \-0.391217 |
| r2  | \-0.541924 | \-1.357582 | \-0.025377 | 0.829804 |

Only label-based slicing is supported right now, not positional, and not callables.

If your style function uses a `subset` or `axis` keyword argument, consider wrapping your function in a `functools.partial`, partialing out that keyword.

my\_func2 \= functools.partial(my\_func, subset\=42)

Copy to clipboard

Optimization[#](https://pandas.pydata.org/docs/user_guide/style.html#Optimization "Link to this heading")

----------------------------------------------------------------------------------------------------------

Generally, for smaller tables and most cases, the rendered HTML does not need to be optimized, and we don’t really recommend it. There are two cases where it is worth considering:

*   If you are rendering and styling a very large HTML table, certain browsers have performance issues.
    
*   If you are using `Styler` to dynamically create part of online user interfaces and want to improve network performance.
    

Here we recommend the following steps to implement:

### 1\. Remove UUID and cell\_ids[#](https://pandas.pydata.org/docs/user_guide/style.html#1.-Remove-UUID-and-cell_ids "Link to this heading")

Ignore the `uuid` and set `cell_ids` to `False`. This will prevent unnecessary HTML.

This is sub-optimal:

\[40\]:

Copy to clipboard

df4 \= pd.DataFrame(\[\[1, 2\], \[3, 4\]\])
s4 \= df4.style

Copy to clipboard

This is better:

\[41\]:

Copy to clipboard

from pandas.io.formats.style import Styler

s4 \= Styler(df4, uuid\_len\=0, cell\_ids\=False)

Copy to clipboard

### 2\. Use table styles[#](https://pandas.pydata.org/docs/user_guide/style.html#2.-Use-table-styles "Link to this heading")

Use table styles where possible (e.g. for all cells or rows or columns at a time) since the CSS is nearly always more efficient than other formats.

This is sub-optimal:

\[42\]:

Copy to clipboard

props \= 'font-family: "Times New Roman", Times, serif; color: #e83e8c; font-size:1.3em;'
df4.style.map(lambda x: props, subset\=\[1\])

Copy to clipboard

\[42\]:

Copy to clipboard

|     | 0   | 1   |
| --- | --- | --- |
| 0   | 1   | 2   |
| 1   | 3   | 4   |

This is better:

\[43\]:

Copy to clipboard

df4.style.set\_table\_styles(\[{"selector": "td.col1", "props": props}\])

Copy to clipboard

\[43\]:

Copy to clipboard

|     | 0   | 1   |
| --- | --- | --- |
| 0   | 1   | 2   |
| 1   | 3   | 4   |

### 3\. Set classes instead of using Styler functions[#](https://pandas.pydata.org/docs/user_guide/style.html#3.-Set-classes-instead-of-using-Styler-functions "Link to this heading")

For large DataFrames where the same style is applied to many cells it can be more efficient to declare the styles as classes and then apply those classes to data cells, rather than directly applying styles to cells. It is, however, probably still easier to use the Styler function api when you are not concerned about optimization.

This is sub-optimal:

\[44\]:

Copy to clipboard

df2.style.apply(
    highlight\_max, props\="color:white;background-color:darkblue;", axis\=0
).apply(highlight\_max, props\="color:white;background-color:pink;", axis\=1).apply(
    highlight\_max, props\="color:white;background-color:purple", axis\=None
)

Copy to clipboard

\[44\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | 0.640423 | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | 1.042513 |
| 5   | \-0.128535 | 1.366463 | \-0.665195 | 0.351510 |
| 6   | 0.903470 | 0.094012 | \-0.743499 | \-0.921725 |
| 7   | \-0.457726 | 0.220195 | \-1.009618 | \-0.209176 |
| 8   | \-0.159225 | 0.540846 | 0.214659 | 0.355373 |
| 9   | \-0.653829 | \-0.129614 | 0.783975 | 1.493431 |

This is better:

\[45\]:

Copy to clipboard

build \= lambda x: pd.DataFrame(x, index\=df2.index, columns\=df2.columns)
cls1 \= build(df2.apply(highlight\_max, props\="cls-1 ", axis\=0))
cls2 \= build(
    df2.apply(highlight\_max, props\="cls-2 ", axis\=1, result\_type\="expand").values
)
cls3 \= build(highlight\_max(df2, props\="cls-3 "))
df2.style.set\_table\_styles(
    \[\
        {"selector": ".cls-1", "props": "color:white;background-color:darkblue;"},\
        {"selector": ".cls-2", "props": "color:white;background-color:pink;"},\
        {"selector": ".cls-3", "props": "color:white;background-color:purple;"},\
    \]
).set\_td\_classes(cls1 + cls2 + cls3)

Copy to clipboard

\[45\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | 0.640423 | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | 1.042513 |
| 5   | \-0.128535 | 1.366463 | \-0.665195 | 0.351510 |
| 6   | 0.903470 | 0.094012 | \-0.743499 | \-0.921725 |
| 7   | \-0.457726 | 0.220195 | \-1.009618 | \-0.209176 |
| 8   | \-0.159225 | 0.540846 | 0.214659 | 0.355373 |
| 9   | \-0.653829 | \-0.129614 | 0.783975 | 1.493431 |

### 4\. Don’t use tooltips[#](https://pandas.pydata.org/docs/user_guide/style.html#4.-Don't-use-tooltips "Link to this heading")

Tooltips require `cell_ids` to work and they generate extra HTML elements for _every_ data cell.

### 5\. If every byte counts use string replacement[#](https://pandas.pydata.org/docs/user_guide/style.html#5.-If-every-byte-counts-use-string-replacement "Link to this heading")

You can remove unnecessary HTML, or shorten the default class names by replacing the default css dict. You can read a little more about CSS [below](https://pandas.pydata.org/docs/user_guide/style.html#More-About-CSS-and-HTML)
.

\[46\]:

Copy to clipboard

my\_css \= {
    "row\_heading": "",
    "col\_heading": "",
    "index\_name": "",
    "col": "c",
    "row": "r",
    "col\_trim": "",
    "row\_trim": "",
    "level": "l",
    "data": "",
    "blank": "",
}
html \= Styler(df4, uuid\_len\=0, cell\_ids\=False)
html.set\_table\_styles(
    \[\
        {"selector": "td", "props": props},\
        {"selector": ".c1", "props": "color:green;"},\
        {"selector": ".l0", "props": "color:blue;"},\
    \],
    css\_class\_names\=my\_css,
)
print(html.to\_html())

Copy to clipboard

<style type="text/css">
#T\_ td {
  font-family: "Times New Roman", Times, serif;
  color: #e83e8c;
  font-size: 1.3em;
}
#T\_ .c1 {
  color: green;
}
#T\_ .l0 {
  color: blue;
}
</style>
<table id="T\_">
  <thead>
    <tr>
      <th class=" l0" >&nbsp;</th>
      <th class=" l0 c0" >0</th>
      <th class=" l0 c1" >1</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th class=" l0 r0" >0</th>
      <td class=" r0 c0" >1</td>
      <td class=" r0 c1" >2</td>
    </tr>
    <tr>
      <th class=" l0 r1" >1</th>
      <td class=" r1 c0" >3</td>
      <td class=" r1 c1" >4</td>
    </tr>
  </tbody>
</table>

Copy to clipboard

\[47\]:

Copy to clipboard

html

Copy to clipboard

\[47\]:

Copy to clipboard

|     | 0   | 1   |
| --- | --- | --- |
| 0   | 1   | 2   |
| 1   | 3   | 4   |

Builtin Styles[#](https://pandas.pydata.org/docs/user_guide/style.html#Builtin-Styles "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Some styling functions are common enough that we’ve “built them in” to the `Styler`, so you don’t have to write them and apply them yourself. The current list of such functions is:

*   [.highlight\_null](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_null.html)
    : for use with identifying missing data.
    
*   [.highlight\_min](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_min.html)
     and [.highlight\_max](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_max.html)
    : for use with identifying extremities in data.
    
*   [.highlight\_between](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_between.html)
     and [.highlight\_quantile](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.highlight_quantile.html)
    : for use with identifying classes within data.
    
*   [.background\_gradient](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.background_gradient.html)
    : a flexible method for highlighting cells based on their, or other, values on a numeric scale.
    
*   [.text\_gradient](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
    : similar method for highlighting text based on their, or other, values on a numeric scale.
    
*   [.bar](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.bar.html)
    : to display mini-charts within cell backgrounds.
    

The individual documentation on each function often gives more examples of their arguments.

### Highlight Null[#](https://pandas.pydata.org/docs/user_guide/style.html#Highlight-Null "Link to this heading")

\[48\]:

Copy to clipboard

df2.iloc\[0, 2\] \= np.nan
df2.iloc\[4, 3\] \= np.nan
df2.loc\[:4\].style.highlight\_null(color\="yellow")

Copy to clipboard

\[48\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | nan | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | nan |

### Highlight Min or Max[#](https://pandas.pydata.org/docs/user_guide/style.html#Highlight-Min-or-Max "Link to this heading")

\[49\]:

Copy to clipboard

df2.loc\[:4\].style.highlight\_max(
    axis\=1, props\=("color:white; font-weight:bold; background-color:darkblue;")
)

Copy to clipboard

\[49\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | nan | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | nan |

### Highlight Between[#](https://pandas.pydata.org/docs/user_guide/style.html#Highlight-Between "Link to this heading")

This method accepts ranges as float, or NumPy arrays or Series provided the indexes match.

\[50\]:

Copy to clipboard

left \= pd.Series(\[1.0, 0.0, 1.0\], index\=\["A", "B", "D"\])
df2.loc\[:4\].style.highlight\_between(
    left\=left, right\=1.5, axis\=1, props\="color:white; background-color:purple;"
)

Copy to clipboard

\[50\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | nan | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | nan |

### Highlight Quantile[#](https://pandas.pydata.org/docs/user_guide/style.html#Highlight-Quantile "Link to this heading")

Useful for detecting the highest or lowest percentile values

\[51\]:

Copy to clipboard

df2.loc\[:4\].style.highlight\_quantile(q\_left\=0.85, axis\=None, color\="yellow")

Copy to clipboard

\[51\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | nan | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | nan |

### Background Gradient and Text Gradient[#](https://pandas.pydata.org/docs/user_guide/style.html#Background-Gradient-and-Text-Gradient "Link to this heading")

You can create “heatmaps” with the `background_gradient` and `text_gradient` methods. These require matplotlib, and we’ll use [Seaborn](https://seaborn.pydata.org/)
 to get a nice colormap.

\[52\]:

Copy to clipboard

import seaborn as sns

cm \= sns.light\_palette("green", as\_cmap\=True)

df2.style.background\_gradient(cmap\=cm)

Copy to clipboard

\[52\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | nan | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | nan |
| 5   | \-0.128535 | 1.366463 | \-0.665195 | 0.351510 |
| 6   | 0.903470 | 0.094012 | \-0.743499 | \-0.921725 |
| 7   | \-0.457726 | 0.220195 | \-1.009618 | \-0.209176 |
| 8   | \-0.159225 | 0.540846 | 0.214659 | 0.355373 |
| 9   | \-0.653829 | \-0.129614 | 0.783975 | 1.493431 |

\[53\]:

Copy to clipboard

df2.style.text\_gradient(cmap\=cm)

Copy to clipboard

\[53\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | nan | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | nan |
| 5   | \-0.128535 | 1.366463 | \-0.665195 | 0.351510 |
| 6   | 0.903470 | 0.094012 | \-0.743499 | \-0.921725 |
| 7   | \-0.457726 | 0.220195 | \-1.009618 | \-0.209176 |
| 8   | \-0.159225 | 0.540846 | 0.214659 | 0.355373 |
| 9   | \-0.653829 | \-0.129614 | 0.783975 | 1.493431 |

[.background\_gradient](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.background_gradient.html)
 and [.text\_gradient](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.text_gradient.html)
 have a number of keyword arguments to customise the gradients and colors. See the documentation.

### Set properties[#](https://pandas.pydata.org/docs/user_guide/style.html#Set-properties "Link to this heading")

Use `Styler.set_properties` when the style doesn’t actually depend on the values. This is just a simple wrapper for `.map` where the function returns the same properties for all cells.

\[54\]:

Copy to clipboard

df2.loc\[:4\].style.set\_properties(
    \*\*{"background-color": "black", "color": "lawngreen", "border-color": "white"}
)

Copy to clipboard

\[54\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | nan | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | nan |

### Bar charts[#](https://pandas.pydata.org/docs/user_guide/style.html#Bar-charts "Link to this heading")

You can include “bar charts” in your DataFrame.

\[55\]:

Copy to clipboard

df2.style.bar(subset\=\["A", "B"\], color\="#d65f5f")

Copy to clipboard

\[55\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.125730 | \-0.132105 | nan | 0.104900 |
| 1   | \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| 2   | \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| 3   | \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| 4   | \-0.544259 | \-0.316300 | 0.411631 | nan |
| 5   | \-0.128535 | 1.366463 | \-0.665195 | 0.351510 |
| 6   | 0.903470 | 0.094012 | \-0.743499 | \-0.921725 |
| 7   | \-0.457726 | 0.220195 | \-1.009618 | \-0.209176 |
| 8   | \-0.159225 | 0.540846 | 0.214659 | 0.355373 |
| 9   | \-0.653829 | \-0.129614 | 0.783975 | 1.493431 |

Additional keyword arguments give more control on centering and positioning, and you can pass a list of `[color_negative, color_positive]` to highlight lower and higher values or a matplotlib colormap.

To showcase an example here’s how you can change the above with the new `align` option, combined with setting `vmin` and `vmax` limits, the `width` of the figure, and underlying css `props` of cells, leaving space to display the text and the bars. We also use `text_gradient` to color the text the same as the bars using a matplotlib colormap (although in this case the visualization is probably better without this additional effect).

\[56\]:

Copy to clipboard

df2.style.format("{:.3f}", na\_rep\="").bar(
    align\=0,
    vmin\=-2.5,
    vmax\=2.5,
    cmap\="bwr",
    height\=50,
    width\=60,
    props\="width: 120px; border-right: 1px solid black;",
).text\_gradient(cmap\="bwr", vmin\=-2.5, vmax\=2.5)

Copy to clipboard

\[56\]:

Copy to clipboard

|     | A   | B   | C   | D   |
| --- | --- | --- | --- | --- |
| 0   | 0.126 | \-0.132 |     | 0.105 |
| 1   | \-0.536 | 0.362 | 1.304 | 0.947 |
| 2   | \-0.704 | \-1.265 | \-0.623 | 0.041 |
| 3   | \-2.325 | \-0.219 | \-1.246 | \-0.732 |
| 4   | \-0.544 | \-0.316 | 0.412 |     |
| 5   | \-0.129 | 1.366 | \-0.665 | 0.352 |
| 6   | 0.903 | 0.094 | \-0.743 | \-0.922 |
| 7   | \-0.458 | 0.220 | \-1.010 | \-0.209 |
| 8   | \-0.159 | 0.541 | 0.215 | 0.355 |
| 9   | \-0.654 | \-0.130 | 0.784 | 1.493 |

The following example aims to give a highlight of the behavior of the new align options:

\[58\]:

Copy to clipboard

HTML(head)

Copy to clipboard

\[58\]:

Copy to clipboard

AlignAll NegativeBoth Neg and PosAll PositiveLarge Positiveleft

|     |
| --- |
| \-100 |
| \-60 |
| \-30 |
| \-20 |

|     |
| --- |
| \-10 |
| \-5 |
| 0   |
| 90  |

|     |
| --- |
| 10  |
| 20  |
| 50  |
| 100 |

|     |
| --- |
| 100 |
| 103 |
| 101 |
| 102 |

right

|     |
| --- |
| \-100 |
| \-60 |
| \-30 |
| \-20 |

|     |
| --- |
| \-10 |
| \-5 |
| 0   |
| 90  |

|     |
| --- |
| 10  |
| 20  |
| 50  |
| 100 |

|     |
| --- |
| 100 |
| 103 |
| 101 |
| 102 |

zero

|     |
| --- |
| \-100 |
| \-60 |
| \-30 |
| \-20 |

|     |
| --- |
| \-10 |
| \-5 |
| 0   |
| 90  |

|     |
| --- |
| 10  |
| 20  |
| 50  |
| 100 |

|     |
| --- |
| 100 |
| 103 |
| 101 |
| 102 |

mid

|     |
| --- |
| \-100 |
| \-60 |
| \-30 |
| \-20 |

|     |
| --- |
| \-10 |
| \-5 |
| 0   |
| 90  |

|     |
| --- |
| 10  |
| 20  |
| 50  |
| 100 |

|     |
| --- |
| 100 |
| 103 |
| 101 |
| 102 |

mean

|     |
| --- |
| \-100 |
| \-60 |
| \-30 |
| \-20 |

|     |
| --- |
| \-10 |
| \-5 |
| 0   |
| 90  |

|     |
| --- |
| 10  |
| 20  |
| 50  |
| 100 |

|     |
| --- |
| 100 |
| 103 |
| 101 |
| 102 |

99

|     |
| --- |
| \-100 |
| \-60 |
| \-30 |
| \-20 |

|     |
| --- |
| \-10 |
| \-5 |
| 0   |
| 90  |

|     |
| --- |
| 10  |
| 20  |
| 50  |
| 100 |

|     |
| --- |
| 100 |
| 103 |
| 101 |
| 102 |

Sharing styles[#](https://pandas.pydata.org/docs/user_guide/style.html#Sharing-styles "Link to this heading")

--------------------------------------------------------------------------------------------------------------

Say you have a lovely style built up for a DataFrame, and now you want to apply the same style to a second DataFrame. Export the style with `df1.style.export`, and import it on the second DataFrame with `df1.style.set`

\[59\]:

Copy to clipboard

style1 \= (
    df2.style.map(style\_negative, props\="color:red;")
    .map(lambda v: "opacity: 20%;" if (v < 0.3) and (v \> \-0.3) else None)
    .set\_table\_styles(\[{"selector": "th", "props": "color: blue;"}\])
    .hide(axis\="index")
)
style1

Copy to clipboard

\[59\]:

Copy to clipboard

| A   | B   | C   | D   |
| --- | --- | --- | --- |
| 0.125730 | \-0.132105 | nan | 0.104900 |
| \-0.535669 | 0.361595 | 1.304000 | 0.947081 |
| \-0.703735 | \-1.265421 | \-0.623274 | 0.041326 |
| \-2.325031 | \-0.218792 | \-1.245911 | \-0.732267 |
| \-0.544259 | \-0.316300 | 0.411631 | nan |
| \-0.128535 | 1.366463 | \-0.665195 | 0.351510 |
| 0.903470 | 0.094012 | \-0.743499 | \-0.921725 |
| \-0.457726 | 0.220195 | \-1.009618 | \-0.209176 |
| \-0.159225 | 0.540846 | 0.214659 | 0.355373 |
| \-0.653829 | \-0.129614 | 0.783975 | 1.493431 |

\[60\]:

Copy to clipboard

style2 \= df3.style
style2.use(style1.export())
style2

Copy to clipboard

\[60\]:

Copy to clipboard

| c1  | c2  | c3  | c4  |
| --- | --- | --- | --- |
| 1.659801 | 0.514933 | \-0.117619 | \-1.451866 |
| \-0.439634 | 1.374616 | \-0.349268 | 0.237399 |
| \-0.533508 | 0.099571 | \-1.088552 | \-0.391217 |
| \-0.541924 | \-1.357582 | \-0.025377 | 0.829804 |

Notice that you’re able to share the styles even though they’re data aware. The styles are re-evaluated on the new DataFrame they’ve been `use`d upon.

Limitations[#](https://pandas.pydata.org/docs/user_guide/style.html#Limitations "Link to this heading")

--------------------------------------------------------------------------------------------------------

*   DataFrame only (use `Series.to_frame().style`)
    
*   The index and columns do not need to be unique, but certain styling functions can only work with unique indexes.
    
*   No large repr, and construction performance isn’t great; although we have some [HTML optimizations](https://pandas.pydata.org/docs/user_guide/style.html#Optimization)
    
*   You can only apply styles, you can’t insert new HTML entities, except via subclassing.
    

Other Fun and Useful Stuff[#](https://pandas.pydata.org/docs/user_guide/style.html#Other-Fun-and-Useful-Stuff "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

Here are a few interesting examples.

### Widgets[#](https://pandas.pydata.org/docs/user_guide/style.html#Widgets "Link to this heading")

`Styler` interacts pretty well with widgets. If you’re viewing this online instead of running the notebook yourself, you’re missing out on interactively adjusting the color palette.

\[61\]:

Copy to clipboard

from ipywidgets import widgets

@widgets.interact
def f(h\_neg\=(0, 359, 1), h\_pos\=(0, 359), s\=(0.0, 99.9), l\_post\=(0.0, 99.9)):
    return df2.style.background\_gradient(
        cmap\=sns.palettes.diverging\_palette(
            h\_neg\=h\_neg, h\_pos\=h\_pos, s\=s, l\=l\_post, as\_cmap\=True
        )
    )

Copy to clipboard

### Magnify[#](https://pandas.pydata.org/docs/user_guide/style.html#Magnify "Link to this heading")

\[62\]:

Copy to clipboard

def magnify():
    return \[\
        {"selector": "th", "props": \[("font-size", "4pt")\]},\
        {"selector": "td", "props": \[("padding", "0em 0em")\]},\
        {"selector": "th:hover", "props": \[("font-size", "12pt")\]},\
        {\
            "selector": "tr:hover td:hover",\
            "props": \[("max-width", "200px"), ("font-size", "12pt")\],\
        },\
    \]

Copy to clipboard

\[63\]:

Copy to clipboard

cmap \= sns.diverging\_palette(5, 250, as\_cmap\=True)
bigdf \= pd.DataFrame(np.random.default\_rng(25).standard\_normal((20, 25))).cumsum()

bigdf.style.background\_gradient(cmap, axis\=1).set\_properties(
    \*\*{"max-width": "80px", "font-size": "1pt"}
).set\_caption("Hover to magnify").format(precision\=2).set\_table\_styles(magnify())

Copy to clipboard

\[63\]:

Copy to clipboard

|     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |Hover to magnify
|     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | 0.35 | \-0.00 | \-0.53 | \-2.28 | 0.02 | 0.93 | 1.04 | \-0.54 | 2.23 | 1.94 | \-0.23 | \-0.16 | 0.96 | \-0.25 | 0.22 | 1.22 | 1.19 | \-0.53 | \-0.46 | \-0.55 | \-0.01 | 0.07 | \-0.39 | 0.77 | 0.05 |
| 1   | 0.37 | \-1.97 | \-1.92 | \-2.97 | 0.38 | 0.06 | 2.60 | \-0.39 | 2.49 | 2.06 | 0.26 | 0.77 | 0.41 | 1.31 | \-0.55 | 1.74 | 0.98 | \-0.70 | 0.21 | \-0.35 | 1.59 | \-0.43 | 0.13 | 1.36 | 2.16 |
| 2   | 1.98 | \-1.27 | \-0.24 | \-2.12 | \-0.40 | 0.39 | 3.83 | \-0.91 | 4.01 | 2.42 | \-0.36 | 1.23 | \-1.16 | 0.62 | \-1.60 | 2.24 | \-0.04 | \-2.26 | 0.52 | \-0.83 | 0.87 | \-1.03 | 1.17 | 1.53 | 1.41 |
| 3   | 4.78 | \-0.78 | 1.67 | \-1.07 | 0.96 | \-0.48 | 3.26 | \-0.27 | 3.93 | 2.50 | 0.72 | \-1.07 | \-1.49 | 2.16 | \-2.07 | 2.28 | 0.34 | \-1.94 | 0.83 | \-1.76 | 1.20 | \-1.63 | 2.75 | 0.90 | 1.67 |
| 4   | 4.58 | 0.35 | 1.79 | \-0.36 | 0.40 | \-0.86 | 2.31 | \-0.44 | 3.65 | 1.36 | \-0.53 | \-0.91 | \-1.67 | 1.45 | \-2.99 | 1.17 | 0.44 | \-2.48 | 0.20 | \-2.32 | 0.73 | \-1.94 | 2.84 | \-0.86 | 1.41 |
| 5   | 3.38 | \-0.02 | 3.04 | \-2.28 | \-0.89 | \-1.38 | 0.01 | 1.95 | 3.01 | 2.98 | \-0.62 | 0.27 | \-0.86 | 1.15 | \-2.49 | 0.51 | \-0.04 | \-0.99 | \-0.67 | \-3.24 | 3.28 | \-2.33 | 3.14 | 0.78 | 0.92 |
| 6   | 2.81 | 1.80 | 3.02 | \-2.01 | \-1.23 | \-0.85 | \-1.57 | 2.12 | 4.01 | 3.94 | \-1.13 | 0.91 | 1.28 | 1.27 | \-1.81 | 0.15 | \-1.77 | \-0.25 | \-1.63 | \-3.94 | 3.34 | \-2.35 | 3.01 | 1.90 | 1.05 |
| 7   | 2.85 | 0.72 | 3.92 | \-3.29 | \-3.49 | \-1.67 | \-0.87 | 2.46 | 5.28 | 4.34 | \-0.76 | 1.24 | 0.64 | 0.81 | \-2.27 | 0.34 | \-2.71 | \-0.67 | \-1.35 | \-4.01 | 3.06 | \-2.55 | 1.78 | 0.54 | 0.25 |
| 8   | 3.80 | 1.51 | 4.19 | \-2.67 | \-2.71 | \-4.04 | \-1.42 | 3.30 | 7.04 | 4.52 | 0.96 | 2.40 | 0.78 | \-0.24 | \-3.28 | 0.28 | \-2.51 | \-0.74 | \-0.74 | \-3.44 | 3.11 | \-2.12 | 2.07 | \-1.35 | \-1.03 |
| 9   | 4.11 | 2.27 | 4.29 | \-2.97 | \-2.50 | \-3.58 | \-1.25 | 1.32 | 7.36 | 5.25 | 1.08 | 4.60 | \-0.64 | \-2.05 | 0.09 | \-0.72 | \-4.96 | \-1.31 | 0.09 | \-4.16 | 2.68 | \-1.37 | 4.02 | \-0.59 | \-0.72 |
| 10  | 3.67 | 3.02 | 7.08 | \-4.10 | \-3.57 | \-3.95 | \-0.53 | 1.94 | 7.14 | 4.78 | 2.44 | 5.06 | 0.69 | \-2.28 | 1.23 | \-1.56 | \-2.90 | \-1.71 | \-0.27 | \-3.72 | 2.50 | \-1.97 | 4.47 | \-1.23 | 1.21 |
| 11  | 2.98 | 3.85 | 6.33 | \-5.84 | \-5.90 | \-3.91 | \-1.94 | 2.08 | 6.33 | 4.70 | 2.41 | 6.84 | 0.50 | \-3.68 | \-1.10 | \-0.67 | \-2.80 | \-0.28 | \-1.88 | \-3.91 | 1.67 | \-1.48 | 4.15 | 0.17 | 0.79 |
| 12  | 2.76 | 3.21 | 6.80 | \-4.75 | \-5.36 | \-4.53 | \-3.00 | 1.17 | 6.52 | 4.20 | 2.25 | 7.97 | 0.98 | \-3.45 | \-1.59 | \-0.86 | \-3.09 | \-0.24 | \-2.08 | \-3.73 | 1.03 | \-0.18 | 4.54 | 0.48 | 1.69 |
| 13  | 1.69 | 2.02 | 5.31 | \-5.51 | \-4.79 | \-4.34 | \-1.42 | \-0.24 | 6.96 | 2.92 | 0.97 | 6.70 | 2.18 | \-3.38 | \-0.33 | \-0.77 | \-2.39 | 0.42 | \-1.53 | \-3.59 | 1.98 | 0.01 | 4.61 | 0.52 | 1.11 |
| 14  | 0.17 | 1.26 | 7.10 | \-5.35 | \-5.81 | \-4.61 | \-0.45 | 1.61 | 5.10 | 1.31 | \-1.18 | 6.09 | 1.25 | \-2.23 | 0.32 | \-1.33 | \-0.08 | \-0.19 | \-1.21 | \-2.83 | 0.97 | 0.13 | 4.89 | 0.36 | 1.83 |
| 15  | 0.01 | 0.61 | 7.94 | \-5.85 | \-5.35 | \-5.10 | 0.14 | 1.76 | 3.89 | 1.72 | \-1.61 | 7.86 | 0.71 | \-1.38 | \-1.95 | \-1.84 | \-1.88 | \-0.14 | \-2.02 | \-1.45 | 1.68 | 1.62 | 3.97 | \-1.88 | 1.80 |
| 16  | 1.42 | 0.91 | 9.86 | \-6.10 | \-6.02 | \-4.56 | 1.24 | 1.38 | 3.25 | 1.05 | 0.38 | 5.77 | 1.92 | \-1.51 | \-0.36 | \-1.01 | \-3.01 | 0.10 | \-2.50 | \-1.99 | 0.29 | 2.91 | 2.07 | \-1.64 | 3.87 |
| 17  | 1.94 | 2.55 | 10.78 | \-4.77 | \-6.87 | \-4.38 | 1.74 | 1.63 | 2.34 | 0.06 | 0.41 | 6.21 | 2.20 | \-3.13 | \-0.88 | \-1.57 | \-2.59 | \-0.76 | \-2.38 | \-3.21 | \-0.11 | 3.62 | 2.91 | \-2.87 | 3.98 |
| 18  | 1.27 | 4.45 | 11.25 | \-4.68 | \-4.93 | \-7.30 | 0.92 | 2.30 | 2.34 | 0.52 | \-0.15 | 6.01 | 2.52 | \-1.89 | 1.37 | \-2.65 | \-1.98 | \-2.85 | \-2.78 | \-2.81 | \-0.86 | 3.93 | 2.83 | \-1.04 | 4.17 |
| 19  | 0.72 | 2.89 | 10.94 | \-3.85 | \-2.50 | \-7.04 | 0.77 | 2.27 | 2.83 | 1.63 | 0.94 | 6.26 | 3.07 | \-1.99 | 2.65 | \-4.04 | \-0.91 | \-2.69 | \-2.70 | \-2.49 | \-0.86 | 3.16 | 2.88 | \-0.85 | 4.54 |

### Sticky Headers[#](https://pandas.pydata.org/docs/user_guide/style.html#Sticky-Headers "Link to this heading")

If you display a large matrix or DataFrame in a notebook, but you want to always see the column and row headers you can use the [.set\_sticky](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.set_sticky.html)
 method which manipulates the table styles CSS.

\[64\]:

Copy to clipboard

bigdf \= pd.DataFrame(np.random.default\_rng().standard\_normal((16, 100)))
bigdf.style.set\_sticky(axis\="index")

Copy to clipboard

\[64\]:

Copy to clipboard

|     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  | 26  | 27  | 28  | 29  | 30  | 31  | 32  | 33  | 34  | 35  | 36  | 37  | 38  | 39  | 40  | 41  | 42  | 43  | 44  | 45  | 46  | 47  | 48  | 49  | 50  | 51  | 52  | 53  | 54  | 55  | 56  | 57  | 58  | 59  | 60  | 61  | 62  | 63  | 64  | 65  | 66  | 67  | 68  | 69  | 70  | 71  | 72  | 73  | 74  | 75  | 76  | 77  | 78  | 79  | 80  | 81  | 82  | 83  | 84  | 85  | 86  | 87  | 88  | 89  | 90  | 91  | 92  | 93  | 94  | 95  | 96  | 97  | 98  | 99  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0   | \-1.816604 | \-1.619676 | 1.280907 | \-0.026415 | 1.504284 | \-1.947485 | 0.780365 | 0.661235 | 0.218289 | \-0.063191 | \-0.015122 | \-0.654707 | \-0.364068 | 0.090752 | 1.305758 | 0.078078 | 0.553281 | 0.014795 | 1.785274 | \-0.648312 | 0.149203 | 1.066797 | 0.473161 | 2.001401 | \-1.590238 | \-0.282872 | \-0.226834 | 1.326742 | 0.832926 | \-0.011032 | 1.393877 | 2.014904 | \-1.130241 | \-1.233198 | \-0.038330 | 1.092759 | \-1.828636 | \-0.284084 | \-0.703338 | 0.866848 | 0.859109 | 0.387679 | \-1.329482 | 1.677111 | 0.444431 | 0.909255 | 0.513445 | \-0.046383 | \-0.593879 | 0.662674 | 0.292191 | \-0.145522 | \-0.925229 | 0.288505 | 0.489941 | 1.957376 | \-0.584195 | 1.311926 | 0.397697 | \-0.195479 | 0.312129 | \-0.497070 | 0.078476 | 1.135587 | \-0.011334 | \-1.686022 | \-1.267288 | \-0.533045 | 0.504978 | \-1.911780 | \-0.429098 | 0.338318 | \-1.122197 | 0.082224 | \-0.409991 | 0.442469 | \-0.633271 | 0.993756 | 1.065327 | 0.066451 | 0.066169 | \-1.257866 | \-0.494030 | \-0.358759 | \-0.120930 | 0.749859 | 0.459647 | \-0.885768 | 0.193838 | \-0.237908 | \-0.478721 | \-0.477605 | \-0.764423 | 1.072452 | \-1.538598 | \-0.832546 | \-0.408681 | 1.259980 | 0.521161 | \-1.069782 |
| 1   | \-1.382811 | 0.403518 | \-0.020652 | 0.012074 | 0.096782 | \-1.606717 | 0.686440 | \-1.313665 | 0.753952 | 0.776121 | 0.263419 | \-1.584506 | \-0.809877 | \-0.712843 | 0.333292 | 0.298647 | \-1.003437 | 0.831951 | 0.728462 | \-0.425536 | \-1.287568 | 0.704144 | 0.488621 | 0.621798 | 0.287315 | \-0.591077 | \-1.043738 | 0.673015 | 0.919043 | \-0.326372 | 1.655275 | 0.313743 | \-0.486307 | \-0.113653 | 0.242847 | 0.921620 | \-0.685129 | \-0.226805 | 1.701097 | \-0.406930 | 0.498517 | \-0.895233 | 0.867077 | 0.424190 | 1.164959 | \-0.422365 | 2.111368 | \-0.173341 | 1.247538 | \-1.553029 | 1.226462 | 0.593049 | 1.359216 | \-1.755068 | \-0.071694 | 0.263921 | 1.346575 | 0.428274 | \-1.617786 | \-0.061535 | 0.162645 | 0.268454 | 0.754233 | \-0.153495 | \-1.014691 | \-0.206654 | 0.064006 | \-1.171504 | \-1.513371 | \-0.968971 | \-0.286180 | 0.607660 | 0.871069 | 0.869030 | 1.106125 | 0.877278 | \-0.257861 | 0.953779 | 0.028636 | 0.985071 | 1.368027 | \-3.557308 | \-1.776187 | 2.153103 | \-3.187064 | 0.177048 | \-0.089252 | \-0.706958 | \-1.646462 | \-0.147763 | 0.051084 | 1.613329 | \-0.883413 | 0.011041 | \-0.847485 | 0.842730 | 0.136301 | 1.815106 | \-1.398780 | \-0.639113 |
| 2   | \-0.159582 | \-0.497279 | 0.107177 | 0.760978 | 1.269089 | \-1.795061 | 0.031094 | \-0.274248 | 0.105435 | \-2.116092 | \-0.082721 | 0.699645 | \-1.575069 | \-0.037534 | 1.868069 | \-0.823959 | 0.285640 | \-0.520791 | 0.701296 | \-0.887850 | \-1.854127 | 0.404042 | \-0.819149 | 1.437661 | \-1.463543 | \-1.348649 | 3.277478 | 2.547804 | \-1.254143 | \-0.522623 | 0.675212 | 0.820393 | 1.470512 | 0.521458 | \-0.357868 | \-0.134012 | \-0.118804 | \-0.076112 | \-0.398441 | 0.022043 | 1.871867 | 0.510832 | \-0.001008 | 1.043979 | 0.202252 | \-0.694230 | 0.307778 | 0.529419 | \-1.170342 | 0.096281 | 2.651506 | 0.057062 | \-0.111685 | \-1.392431 | \-0.923218 | \-0.520036 | \-0.348218 | \-0.655606 | \-0.290017 | 0.490949 | \-0.115716 | 0.078608 | \-0.011831 | 0.760267 | 0.540008 | \-0.411652 | 0.008585 | 0.018604 | \-0.938361 | \-0.437349 | \-0.788962 | 1.069637 | \-0.314938 | \-0.057428 | \-0.422226 | 0.055650 | 0.466995 | \-2.129229 | 0.901112 | \-1.524620 | 1.815687 | 1.309169 | \-1.765746 | 0.519251 | \-0.237543 | \-1.101488 | \-1.857653 | \-2.030481 | 0.376486 | \-1.906132 | \-0.228330 | \-0.239640 | 1.383169 | \-0.375881 | \-0.348501 | \-0.786358 | \-1.042514 | \-0.425238 | \-0.996423 | \-0.609625 |
| 3   | 0.819316 | 1.331691 | \-0.154671 | 0.548303 | \-0.115874 | 0.034913 | 1.064890 | 0.377019 | 1.112761 | 0.462723 | \-0.243830 | 0.672322 | 1.218809 | \-1.382614 | \-1.224092 | 1.945308 | 0.564812 | 0.751757 | \-0.167616 | \-0.841158 | \-1.062605 | 1.330277 | 1.550985 | 0.927476 | 0.485424 | \-2.953384 | 0.001898 | 0.596797 | 0.504031 | 1.962707 | 0.013863 | 0.147747 | 0.077385 | 1.380456 | \-1.024031 | \-1.012451 | 1.073276 | 0.199474 | \-0.636604 | 0.119683 | 0.766159 | \-0.369019 | \-0.502480 | \-2.441807 | 0.591698 | 0.036384 | \-0.638833 | 1.351646 | 0.503343 | \-0.854087 | \-0.970353 | \-0.993211 | 1.836232 | 0.859789 | \-0.641732 | 1.211223 | 1.503241 | \-0.161712 | 0.268744 | \-1.160029 | \-0.191270 | \-0.595466 | 1.688434 | 2.350668 | \-0.964043 | 0.455822 | \-0.552546 | 0.183908 | 0.143984 | 0.834694 | 0.921678 | \-1.422249 | 0.226858 | \-1.132449 | \-0.145471 | 0.326857 | \-1.292863 | \-1.093173 | 1.350410 | 0.021411 | 0.104345 | 1.868744 | 1.095889 | 0.036845 | \-0.437690 | 0.706520 | 0.383796 | \-1.763506 | \-1.474575 | \-0.766710 | \-0.327029 | 0.799385 | 1.207821 | \-1.063907 | 1.664232 | \-1.579153 | \-2.889208 | 1.162354 | \-1.856726 | 0.367348 |
| 4   | 1.135280 | 0.154405 | \-1.690605 | 1.002838 | 0.997144 | \-0.639369 | 0.706240 | \-1.521397 | 0.928532 | \-0.066317 | 0.095305 | \-0.154145 | 0.176643 | 0.045652 | 0.386674 | 1.597488 | \-0.277950 | \-1.722428 | 1.308709 | \-1.355986 | \-1.176332 | 0.112544 | \-0.441502 | \-1.270590 | \-0.661008 | 1.330522 | 0.320135 | 1.167157 | \-1.364080 | \-0.220546 | 3.105750 | \-2.058362 | \-1.026274 | \-1.603823 | 0.843136 | \-1.978339 | 0.997299 | \-0.103197 | \-1.128308 | \-0.174338 | 0.411705 | \-0.972353 | 1.419469 | 0.610046 | \-0.188489 | \-1.130513 | 0.844059 | 1.224542 | \-0.436722 | \-3.069639 | 0.116501 | \-0.845159 | 1.586514 | \-1.484485 | 1.821135 | \-0.846458 | 0.198123 | 0.794855 | 0.862032 | \-0.034138 | \-0.492395 | 0.973250 | 0.901593 | 0.263111 | \-2.007821 | \-0.661586 | 0.063412 | 1.130984 | 0.233232 | \-1.174803 | \-0.875338 | 1.610706 | 0.299095 | \-0.290738 | 1.178792 | \-0.850622 | 1.504558 | 0.102695 | \-0.180380 | \-0.937365 | \-0.460620 | 0.362044 | 0.096921 | \-0.385210 | \-0.982422 | \-1.992112 | \-1.444678 | \-0.872915 | \-0.062038 | \-0.489576 | 0.670010 | \-0.001386 | \-0.731642 | \-1.024347 | \-0.378050 | 1.921468 | \-0.660317 | \-1.173823 | \-0.134648 | 0.923213 |
| 5   | \-0.356665 | \-0.966282 | 0.252394 | 0.495761 | 0.636330 | \-2.099039 | 0.306130 | \-0.028424 | 0.206351 | \-0.675954 | \-0.173781 | \-0.659855 | 0.739561 | 1.183141 | 0.470638 | \-1.290471 | \-0.601876 | \-1.678546 | 1.322868 | 0.270965 | \-1.654688 | 0.287904 | \-0.034230 | 2.260975 | \-0.458285 | \-0.416963 | \-0.791426 | \-0.193350 | \-1.792184 | \-1.318831 | \-0.776932 | 0.892524 | 1.638030 | 0.648060 | 0.050024 | \-0.079406 | \-0.168819 | \-0.528180 | 0.509640 | 0.389127 | \-1.753933 | \-0.856515 | 0.249594 | 0.470054 | \-0.870691 | 0.196685 | 0.419023 | 2.032849 | 1.801612 | \-0.579914 | 0.717563 | 0.423161 | 0.270556 | \-0.694673 | 0.387542 | \-0.276376 | \-1.052244 | \-2.330456 | 0.487283 | \-0.282307 | \-0.862809 | \-0.964048 | 0.006596 | 0.981186 | 0.222281 | 0.450658 | \-1.037929 | 0.242039 | 1.604181 | \-0.044079 | \-0.002931 | 0.890995 | \-0.498676 | 0.125733 | 0.170164 | 0.114292 | \-0.114529 | 0.643665 | 1.550666 | \-1.196385 | \-1.005633 | 0.987484 | \-2.474021 | \-0.942943 | 2.542174 | 2.005077 | \-2.240966 | 2.877203 | 0.288686 | \-0.074685 | \-0.195066 | \-0.156439 | \-0.786641 | 0.319762 | 1.421286 | 0.066732 | 1.170977 | 0.820487 | 2.648986 | \-0.209079 |
| 6   | \-0.749591 | 1.131690 | \-0.828222 | 0.650511 | \-1.565665 | \-0.155689 | \-0.233177 | 0.173176 | 1.329346 | 0.868886 | 0.776473 | 0.688853 | 1.776149 | 0.037287 | 0.451512 | \-0.719932 | \-0.382848 | 0.036005 | \-0.184394 | \-1.017601 | 0.945876 | 0.059931 | \-1.157834 | 0.478029 | \-0.038687 | 0.662824 | \-0.239063 | 1.090865 | \-0.130192 | 0.472693 | \-1.933048 | \-0.608379 | 0.869687 | 0.226225 | \-0.160558 | \-0.879435 | 0.306166 | \-1.147555 | 0.415554 | \-0.422111 | 0.471486 | \-0.982343 | \-0.946057 | 0.806259 | \-0.658906 | 0.737453 | \-0.057951 | \-0.549889 | \-0.636656 | \-0.548671 | \-0.575404 | \-0.099271 | 2.593643 | \-0.155903 | 1.853823 | \-0.259022 | 0.606196 | \-1.434706 | \-0.782503 | \-0.327437 | \-0.864812 | \-0.237751 | \-2.423010 | \-1.128286 | \-0.494937 | \-0.477452 | \-1.281871 | \-0.259802 | 0.079020 | 1.154653 | 0.264920 | 0.290462 | 0.011565 | \-1.463453 | \-0.799214 | 1.749990 | 0.079577 | \-0.741525 | 0.343831 | 0.523582 | 1.181326 | 0.953577 | \-1.179192 | \-0.978718 | 0.200574 | \-0.040077 | \-0.320622 | \-1.298582 | \-0.321176 | \-0.892720 | 0.261124 | \-0.736350 | \-0.061693 | 0.545805 | \-1.435774 | \-0.193081 | 0.243715 | 1.721250 | \-0.420792 | 1.055831 |
| 7   | 0.502827 | \-0.217032 | 0.776575 | \-1.429009 | \-1.022916 | 1.128800 | 0.736995 | \-2.015919 | \-0.798160 | \-1.162292 | 0.423827 | \-0.204595 | \-1.546579 | \-0.056928 | \-0.491460 | 0.789149 | \-0.701279 | \-1.328249 | 0.905490 | \-2.317994 | \-0.687140 | 1.770423 | \-1.214158 | \-0.128554 | 0.863697 | \-0.501916 | \-0.249389 | \-0.822525 | 0.606922 | 1.070422 | 0.012283 | \-0.181826 | 0.366801 | 1.598871 | 2.095979 | \-1.393260 | 0.795446 | 0.322609 | \-1.150727 | \-1.018983 | 0.089334 | 0.040401 | \-1.284350 | \-1.774508 | \-1.185096 | \-1.395004 | \-0.238120 | 0.711092 | 0.950707 | 1.051353 | 0.174049 | 1.261710 | \-0.990400 | \-0.013817 | \-0.487245 | 0.988920 | 0.196469 | 0.627224 | \-0.559631 | \-0.187514 | 0.018345 | \-0.424565 | 0.221240 | \-0.315089 | 0.061901 | 0.259872 | 0.715757 | \-0.519667 | 0.135466 | \-0.334678 | 1.222096 | 0.076765 | \-0.974797 | 0.526380 | \-0.914822 | 0.261372 | 0.974278 | \-0.009076 | 0.013396 | \-1.689943 | 1.103502 | \-1.197549 | 2.344155 | 1.146182 | \-0.185935 | 0.686092 | \-0.136343 | 0.322569 | \-1.151059 | \-0.470254 | \-0.689035 | 0.829976 | \-0.298176 | \-0.113427 | \-1.129214 | \-1.695072 | 0.519424 | 0.229655 | 2.277886 | 0.265250 |
| 8   | 1.140159 | 0.421843 | \-0.343562 | \-0.876320 | 0.331853 | 1.044824 | 0.194269 | 1.070443 | \-2.407457 | 0.080689 | \-0.598584 | \-0.111730 | 0.244424 | 0.233870 | 0.487043 | 0.566249 | 1.335058 | 0.259083 | \-0.605676 | 1.168961 | \-0.976273 | 0.295315 | 0.114293 | \-0.154712 | \-1.313154 | \-0.088516 | \-1.171459 | 0.606761 | 1.074177 | \-0.974144 | 1.395917 | 1.317325 | \-0.800204 | \-0.029009 | \-2.244747 | 0.744557 | \-0.312767 | \-0.986406 | \-0.167304 | 0.628170 | \-0.228609 | \-0.147294 | 0.562133 | 0.283782 | \-0.788987 | 0.430063 | 0.452746 | 1.897825 | \-0.417987 | 0.492007 | 0.093273 | \-0.072178 | \-0.350011 | 0.120502 | 0.926225 | 0.786423 | \-1.296064 | 0.825564 | \-0.578341 | \-0.644492 | \-0.415373 | 1.142916 | \-1.252773 | 0.000250 | \-0.943390 | \-1.316790 | 0.771537 | \-0.060666 | \-1.115891 | \-0.037260 | 0.336697 | \-0.419495 | 0.844290 | \-0.406384 | 0.726910 | 0.801403 | \-1.774039 | 1.299428 | 0.319577 | 1.344228 | \-0.910131 | 0.152672 | 2.961074 | 0.857680 | 0.678394 | \-1.122245 | 0.017110 | \-1.073681 | \-1.176131 | 0.015466 | \-2.781098 | \-0.522587 | \-0.973759 | \-0.765304 | 0.373246 | \-0.329447 | 0.585703 | \-0.550335 | \-1.373650 | \-1.374684 |
| 9   | 0.473210 | \-2.375967 | \-0.751571 | 1.340774 | \-0.292321 | \-0.298160 | 0.650556 | 0.957706 | \-1.089526 | \-0.091775 | 1.043711 | \-0.070319 | 0.558694 | 0.288969 | 0.685963 | 0.998607 | 0.173647 | 0.960728 | \-0.696101 | 0.156879 | \-0.490952 | 0.475577 | \-1.304201 | 0.838231 | \-1.762388 | \-1.082789 | \-0.722490 | 0.432377 | \-0.133981 | 1.401917 | \-1.989990 | \-0.598459 | \-0.344521 | 0.019051 | 0.431813 | \-0.391747 | \-0.071103 | 0.285028 | \-0.502880 | \-1.343417 | 0.781904 | \-0.167854 | 0.146754 | \-1.585850 | 0.375186 | 0.520943 | \-0.925393 | \-0.197976 | 0.797735 | \-0.931065 | \-0.158778 | 0.529645 | \-0.720138 | \-0.654246 | 0.603385 | 0.285248 | \-1.065553 | 0.070157 | 0.363451 | \-0.191448 | 1.098395 | \-1.390976 | \-0.935790 | 0.514811 | \-0.189333 | \-0.294067 | \-1.791306 | 0.400007 | 0.251203 | 0.877140 | 0.099326 | \-2.536606 | \-0.517072 | 0.264774 | 0.934519 | \-0.880935 | \-0.496924 | \-0.075644 | \-0.851056 | 1.558560 | \-1.413553 | 0.194210 | \-1.164501 | \-0.125958 | 0.582427 | 0.534269 | \-0.327974 | 0.708747 | 0.251884 | \-0.080712 | \-0.480917 | 0.749453 | \-1.230035 | \-0.726606 | \-1.711782 | 0.624504 | 0.116664 | \-0.971840 | 1.372728 | 0.002035 |
| 10  | 1.302712 | 2.082694 | \-1.677985 | \-1.555907 | \-0.523275 | 0.839967 | \-2.604440 | 0.106786 | 1.118424 | 1.416623 | 1.176300 | \-0.570607 | 0.016937 | \-1.320549 | \-0.688524 | \-1.085140 | 0.849085 | 0.365578 | \-0.916659 | 1.103257 | 1.197104 | \-0.005171 | 1.272970 | 1.508463 | \-0.791778 | \-1.286589 | \-1.363629 | \-1.275104 | \-0.995168 | \-0.732797 | 1.011776 | \-0.599023 | 1.921324 | \-0.191943 | 0.253868 | \-0.556763 | 0.057446 | \-1.573751 | \-0.547084 | 1.346639 | 0.363929 | 1.608864 | 2.059999 | \-0.348148 | 1.266174 | 0.901752 | \-1.901187 | \-0.045168 | \-0.633390 | 2.238007 | 0.051228 | 0.852666 | \-0.836563 | 1.546189 | \-0.787396 | \-0.570315 | \-0.740769 | 1.802785 | 1.239590 | 0.596627 | 2.355694 | 0.538054 | 0.285362 | \-1.808742 | \-1.277903 | \-1.634502 | \-1.489241 | 0.059391 | 1.265560 | \-1.177802 | 0.233532 | \-1.976658 | \-2.173126 | \-0.067194 | 2.062263 | \-1.986836 | 1.372906 | \-0.364234 | 1.010591 | 0.747427 | 0.757398 | 0.683171 | 0.628683 | 0.332984 | \-1.273558 | \-0.775635 | 1.000520 | \-0.068911 | \-0.829279 | \-0.466159 | \-0.100714 | 0.663795 | 1.254263 | 0.544026 | \-0.152562 | \-1.063864 | \-0.766474 | 1.521726 | 0.025230 | 0.263135 |
| 11  | 0.703585 | 1.086720 | \-0.698876 | 2.317539 | 0.138207 | 0.423882 | \-1.111176 | \-0.094467 | 0.952610 | \-0.293499 | 0.667840 | \-0.375226 | \-0.147251 | \-0.637145 | 1.517303 | 3.132466 | 1.371238 | 0.210585 | 1.693381 | \-0.379665 | 0.266554 | \-0.185872 | \-1.818437 | 2.506759 | \-0.397273 | 0.385640 | \-1.042844 | 0.624709 | \-0.451187 | 1.083564 | \-0.676813 | 0.514574 | 2.275493 | \-0.766653 | 0.678269 | 0.534969 | \-1.899356 | 1.014444 | 0.223053 | \-0.945507 | 0.940518 | 0.568774 | 1.411102 | \-0.364688 | 0.889829 | \-0.119186 | 1.361843 | 1.212419 | \-0.224461 | 1.436537 | \-1.776686 | \-0.895706 | \-1.037786 | 0.313883 | 0.005282 | \-0.069917 | \-0.609770 | 0.171258 | \-0.866273 | 0.155435 | \-1.182975 | 0.330804 | 0.389467 | \-0.164819 | \-0.008973 | 0.802583 | 2.266305 | 0.319811 | \-1.924570 | \-0.234520 | 0.841021 | \-0.575380 | 1.100507 | \-0.042184 | \-0.636172 | \-0.625081 | \-0.262145 | 1.063613 | 0.562741 | 1.179673 | 0.431427 | \-0.045187 | \-0.373604 | \-1.130172 | 0.031504 | \-0.648830 | \-1.804172 | \-0.596727 | 0.183587 | \-0.611858 | 0.580205 | 0.544385 | \-1.399456 | \-0.665399 | 1.639616 | 0.451873 | 0.022969 | \-0.616657 | 1.512779 | \-1.122630 |
| 12  | 1.164710 | \-0.777462 | 1.667639 | \-1.088535 | 1.060841 | \-0.901320 | 0.796235 | 1.090697 | \-0.556709 | 0.887566 | 1.271675 | \-0.417219 | \-1.441265 | \-1.402080 | 0.190661 | 0.372360 | 0.497639 | \-0.726344 | \-1.084341 | \-1.778875 | \-0.166976 | 0.301156 | 0.341455 | 0.768867 | \-0.148901 | 0.478981 | 0.318396 | 0.136812 | \-0.414197 | 0.173897 | 1.888839 | 0.613031 | 1.621105 | \-1.508925 | \-0.485501 | \-0.218566 | 0.619560 | \-0.515451 | 0.984699 | 0.433396 | 0.211493 | 1.142100 | 0.055450 | 0.286748 | \-0.478570 | \-0.579152 | \-0.919767 | 0.061121 | \-2.901697 | \-1.185319 | \-0.199465 | \-3.358236 | 1.644457 | 1.152189 | 0.712913 | 0.606704 | \-0.530227 | 0.487737 | 1.984403 | 1.835091 | \-0.406201 | 0.954839 | \-1.292238 | \-0.647831 | \-0.331870 | 1.114978 | \-1.556536 | \-0.479194 | 1.762067 | \-0.673566 | 0.028405 | \-1.571476 | \-0.129625 | \-0.289627 | \-0.826554 | 0.531009 | 1.509519 | 0.007885 | \-0.276068 | 0.533845 | \-0.274268 | 0.342263 | \-0.231432 | 0.685758 | 0.894081 | 0.264197 | 0.025119 | 0.665642 | \-0.137437 | 1.487287 | \-0.225209 | \-0.470140 | 0.787341 | 0.198537 | \-0.316717 | 0.679350 | \-0.765168 | 0.085950 | \-1.035197 | \-1.632781 |
| 13  | \-0.934022 | \-0.040694 | 1.167349 | \-1.190301 | 0.659704 | \-2.747159 | 0.699066 | \-0.598891 | \-2.389625 | 1.278752 | \-0.204705 | 1.368727 | \-1.007521 | 0.049473 | 0.516073 | \-1.507334 | \-0.538353 | 0.049752 | \-1.735942 | 0.293528 | 1.310537 | 0.612638 | 1.895059 | \-0.970561 | \-0.449245 | \-0.988250 | 1.381542 | 0.014603 | \-1.056730 | 0.097341 | 1.688274 | 1.086608 | 0.196618 | \-0.723343 | \-1.292527 | \-0.919669 | 1.576322 | 0.004880 | 0.071091 | \-0.330820 | \-0.290122 | \-0.806495 | 0.030540 | \-0.421577 | 0.455043 | \-1.166432 | 1.907502 | 0.176228 | 1.327814 | 0.481270 | \-0.136838 | 0.605676 | \-0.135607 | \-0.941975 | 1.041375 | 1.700154 | 0.542979 | \-0.596294 | \-1.016533 | 1.340196 | \-0.380741 | \-0.234488 | \-0.026382 | 1.399027 | \-0.682410 | 0.393615 | \-0.648677 | 1.938602 | 0.451682 | \-0.425101 | \-0.639269 | \-0.242342 | 0.090562 | \-0.719265 | 1.512436 | \-0.988682 | 1.802555 | 1.837977 | \-1.656185 | \-1.125617 | 0.955744 | \-0.345026 | \-0.741394 | 0.252191 | 0.189325 | 1.466398 | \-2.101633 | 0.697772 | \-0.262199 | \-0.565488 | 1.522020 | \-1.386808 | 0.029429 | 0.597618 | \-0.791023 | \-1.197469 | 0.147968 | \-0.466924 | 2.310563 | 1.106685 |
| 14  | \-1.781068 | \-1.228565 | 2.367484 | 0.478429 | \-0.653350 | \-0.168068 | \-0.480661 | 0.197105 | \-0.949376 | 1.925986 | 0.298537 | \-0.206352 | \-0.979744 | \-0.744148 | \-0.139285 | \-1.261164 | 0.446535 | 0.568097 | 1.702812 | 0.671052 | \-0.599890 | 0.093166 | \-0.340463 | \-0.339369 | 1.989692 | 1.406806 | \-0.367648 | 1.339758 | 1.771004 | 0.359098 | \-0.298364 | \-0.139448 | \-1.741361 | \-1.570463 | \-0.840369 | \-0.121304 | \-0.843416 | \-0.540409 | 0.354715 | 1.672383 | 0.385298 | 1.118102 | 1.270384 | 0.918830 | 0.391359 | 0.506434 | \-0.203019 | 0.991611 | \-0.868176 | 0.068244 | \-0.564428 | 0.540511 | \-0.043091 | \-1.489450 | 0.484375 | 0.206646 | \-0.814915 | \-0.429202 | \-0.283868 | 1.881487 | \-0.832137 | 0.573218 | 1.480981 | \-0.054202 | 0.685618 | \-0.026086 | 0.133507 | 0.489659 | 1.548035 | \-0.610755 | 0.934192 | \-0.243997 | \-2.110242 | 1.449234 | \-0.091584 | \-1.749582 | \-1.533301 | 0.629799 | \-1.655075 | \-2.572022 | \-0.029369 | \-0.443355 | \-0.650839 | \-0.169573 | \-0.988550 | \-0.804586 | 1.231931 | \-0.542490 | 1.395549 | 1.328407 | 0.554684 | 0.440731 | \-0.681191 | 0.586516 | \-0.230103 | \-0.594544 | \-0.054775 | 0.416148 | \-1.637474 | \-0.278996 |
| 15  | \-1.426027 | \-0.796887 | \-0.533244 | \-0.454206 | \-0.176671 | 0.078048 | 1.294698 | \-0.868407 | \-1.309142 | 0.949318 | \-0.719067 | \-0.285576 | \-0.364888 | 0.527303 | 1.008922 | \-2.788126 | 0.066559 | 0.695167 | \-0.201521 | 0.696496 | 0.424995 | 0.903076 | 0.226559 | 0.389885 | 0.349896 | \-1.687575 | \-1.688522 | \-0.113054 | 1.568585 | 0.500880 | 0.404757 | \-0.774242 | 2.427805 | 0.659742 | 0.723677 | \-0.710790 | \-1.257576 | \-0.827174 | 1.073705 | 1.415423 | \-1.086741 | \-0.448521 | 0.714920 | \-0.817697 | 0.813939 | \-1.318669 | \-1.321715 | \-0.955649 | 0.386657 | 1.625277 | 0.100724 | \-1.356867 | 2.015564 | 0.282621 | \-0.100701 | 1.397511 | 1.479562 | 0.196954 | \-0.407965 | \-0.026595 | 0.887757 | 0.490851 | \-0.655784 | 1.533915 | \-0.249060 | 0.689923 | \-1.367955 | 1.375355 | 0.919708 | 1.177626 | \-0.848278 | 1.408821 | 0.054024 | \-0.587595 | \-0.575131 | \-0.947471 | \-0.796451 | \-1.080850 | \-0.703180 | \-0.427878 | 1.027534 | 0.692969 | \-1.048125 | \-0.614451 | 0.251322 | \-1.002167 | \-1.691401 | 0.085313 | 0.603232 | 0.528476 | \-0.693425 | \-1.256650 | 0.019255 | 1.771643 | \-1.065027 | \-2.055516 | \-1.194088 | \-1.083951 | \-0.570143 | \-0.061593 |

It is also possible to stick MultiIndexes and even only specific levels.

\[65\]:

Copy to clipboard

bigdf.index \= pd.MultiIndex.from\_product(\[\["A", "B"\], \[0, 1\], \[0, 1, 2, 3\]\])
bigdf.style.set\_sticky(axis\="index", pixel\_size\=18, levels\=\[1, 2\])

Copy to clipboard

\[65\]:

Copy to clipboard

|     |     |     | 0   | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  | 11  | 12  | 13  | 14  | 15  | 16  | 17  | 18  | 19  | 20  | 21  | 22  | 23  | 24  | 25  | 26  | 27  | 28  | 29  | 30  | 31  | 32  | 33  | 34  | 35  | 36  | 37  | 38  | 39  | 40  | 41  | 42  | 43  | 44  | 45  | 46  | 47  | 48  | 49  | 50  | 51  | 52  | 53  | 54  | 55  | 56  | 57  | 58  | 59  | 60  | 61  | 62  | 63  | 64  | 65  | 66  | 67  | 68  | 69  | 70  | 71  | 72  | 73  | 74  | 75  | 76  | 77  | 78  | 79  | 80  | 81  | 82  | 83  | 84  | 85  | 86  | 87  | 88  | 89  | 90  | 91  | 92  | 93  | 94  | 95  | 96  | 97  | 98  | 99  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A   | 0   | 0   | \-1.816604 | \-1.619676 | 1.280907 | \-0.026415 | 1.504284 | \-1.947485 | 0.780365 | 0.661235 | 0.218289 | \-0.063191 | \-0.015122 | \-0.654707 | \-0.364068 | 0.090752 | 1.305758 | 0.078078 | 0.553281 | 0.014795 | 1.785274 | \-0.648312 | 0.149203 | 1.066797 | 0.473161 | 2.001401 | \-1.590238 | \-0.282872 | \-0.226834 | 1.326742 | 0.832926 | \-0.011032 | 1.393877 | 2.014904 | \-1.130241 | \-1.233198 | \-0.038330 | 1.092759 | \-1.828636 | \-0.284084 | \-0.703338 | 0.866848 | 0.859109 | 0.387679 | \-1.329482 | 1.677111 | 0.444431 | 0.909255 | 0.513445 | \-0.046383 | \-0.593879 | 0.662674 | 0.292191 | \-0.145522 | \-0.925229 | 0.288505 | 0.489941 | 1.957376 | \-0.584195 | 1.311926 | 0.397697 | \-0.195479 | 0.312129 | \-0.497070 | 0.078476 | 1.135587 | \-0.011334 | \-1.686022 | \-1.267288 | \-0.533045 | 0.504978 | \-1.911780 | \-0.429098 | 0.338318 | \-1.122197 | 0.082224 | \-0.409991 | 0.442469 | \-0.633271 | 0.993756 | 1.065327 | 0.066451 | 0.066169 | \-1.257866 | \-0.494030 | \-0.358759 | \-0.120930 | 0.749859 | 0.459647 | \-0.885768 | 0.193838 | \-0.237908 | \-0.478721 | \-0.477605 | \-0.764423 | 1.072452 | \-1.538598 | \-0.832546 | \-0.408681 | 1.259980 | 0.521161 | \-1.069782 |
| 1   | \-1.382811 | 0.403518 | \-0.020652 | 0.012074 | 0.096782 | \-1.606717 | 0.686440 | \-1.313665 | 0.753952 | 0.776121 | 0.263419 | \-1.584506 | \-0.809877 | \-0.712843 | 0.333292 | 0.298647 | \-1.003437 | 0.831951 | 0.728462 | \-0.425536 | \-1.287568 | 0.704144 | 0.488621 | 0.621798 | 0.287315 | \-0.591077 | \-1.043738 | 0.673015 | 0.919043 | \-0.326372 | 1.655275 | 0.313743 | \-0.486307 | \-0.113653 | 0.242847 | 0.921620 | \-0.685129 | \-0.226805 | 1.701097 | \-0.406930 | 0.498517 | \-0.895233 | 0.867077 | 0.424190 | 1.164959 | \-0.422365 | 2.111368 | \-0.173341 | 1.247538 | \-1.553029 | 1.226462 | 0.593049 | 1.359216 | \-1.755068 | \-0.071694 | 0.263921 | 1.346575 | 0.428274 | \-1.617786 | \-0.061535 | 0.162645 | 0.268454 | 0.754233 | \-0.153495 | \-1.014691 | \-0.206654 | 0.064006 | \-1.171504 | \-1.513371 | \-0.968971 | \-0.286180 | 0.607660 | 0.871069 | 0.869030 | 1.106125 | 0.877278 | \-0.257861 | 0.953779 | 0.028636 | 0.985071 | 1.368027 | \-3.557308 | \-1.776187 | 2.153103 | \-3.187064 | 0.177048 | \-0.089252 | \-0.706958 | \-1.646462 | \-0.147763 | 0.051084 | 1.613329 | \-0.883413 | 0.011041 | \-0.847485 | 0.842730 | 0.136301 | 1.815106 | \-1.398780 | \-0.639113 |
| 2   | \-0.159582 | \-0.497279 | 0.107177 | 0.760978 | 1.269089 | \-1.795061 | 0.031094 | \-0.274248 | 0.105435 | \-2.116092 | \-0.082721 | 0.699645 | \-1.575069 | \-0.037534 | 1.868069 | \-0.823959 | 0.285640 | \-0.520791 | 0.701296 | \-0.887850 | \-1.854127 | 0.404042 | \-0.819149 | 1.437661 | \-1.463543 | \-1.348649 | 3.277478 | 2.547804 | \-1.254143 | \-0.522623 | 0.675212 | 0.820393 | 1.470512 | 0.521458 | \-0.357868 | \-0.134012 | \-0.118804 | \-0.076112 | \-0.398441 | 0.022043 | 1.871867 | 0.510832 | \-0.001008 | 1.043979 | 0.202252 | \-0.694230 | 0.307778 | 0.529419 | \-1.170342 | 0.096281 | 2.651506 | 0.057062 | \-0.111685 | \-1.392431 | \-0.923218 | \-0.520036 | \-0.348218 | \-0.655606 | \-0.290017 | 0.490949 | \-0.115716 | 0.078608 | \-0.011831 | 0.760267 | 0.540008 | \-0.411652 | 0.008585 | 0.018604 | \-0.938361 | \-0.437349 | \-0.788962 | 1.069637 | \-0.314938 | \-0.057428 | \-0.422226 | 0.055650 | 0.466995 | \-2.129229 | 0.901112 | \-1.524620 | 1.815687 | 1.309169 | \-1.765746 | 0.519251 | \-0.237543 | \-1.101488 | \-1.857653 | \-2.030481 | 0.376486 | \-1.906132 | \-0.228330 | \-0.239640 | 1.383169 | \-0.375881 | \-0.348501 | \-0.786358 | \-1.042514 | \-0.425238 | \-0.996423 | \-0.609625 |
| 3   | 0.819316 | 1.331691 | \-0.154671 | 0.548303 | \-0.115874 | 0.034913 | 1.064890 | 0.377019 | 1.112761 | 0.462723 | \-0.243830 | 0.672322 | 1.218809 | \-1.382614 | \-1.224092 | 1.945308 | 0.564812 | 0.751757 | \-0.167616 | \-0.841158 | \-1.062605 | 1.330277 | 1.550985 | 0.927476 | 0.485424 | \-2.953384 | 0.001898 | 0.596797 | 0.504031 | 1.962707 | 0.013863 | 0.147747 | 0.077385 | 1.380456 | \-1.024031 | \-1.012451 | 1.073276 | 0.199474 | \-0.636604 | 0.119683 | 0.766159 | \-0.369019 | \-0.502480 | \-2.441807 | 0.591698 | 0.036384 | \-0.638833 | 1.351646 | 0.503343 | \-0.854087 | \-0.970353 | \-0.993211 | 1.836232 | 0.859789 | \-0.641732 | 1.211223 | 1.503241 | \-0.161712 | 0.268744 | \-1.160029 | \-0.191270 | \-0.595466 | 1.688434 | 2.350668 | \-0.964043 | 0.455822 | \-0.552546 | 0.183908 | 0.143984 | 0.834694 | 0.921678 | \-1.422249 | 0.226858 | \-1.132449 | \-0.145471 | 0.326857 | \-1.292863 | \-1.093173 | 1.350410 | 0.021411 | 0.104345 | 1.868744 | 1.095889 | 0.036845 | \-0.437690 | 0.706520 | 0.383796 | \-1.763506 | \-1.474575 | \-0.766710 | \-0.327029 | 0.799385 | 1.207821 | \-1.063907 | 1.664232 | \-1.579153 | \-2.889208 | 1.162354 | \-1.856726 | 0.367348 |
| 1   | 0   | 1.135280 | 0.154405 | \-1.690605 | 1.002838 | 0.997144 | \-0.639369 | 0.706240 | \-1.521397 | 0.928532 | \-0.066317 | 0.095305 | \-0.154145 | 0.176643 | 0.045652 | 0.386674 | 1.597488 | \-0.277950 | \-1.722428 | 1.308709 | \-1.355986 | \-1.176332 | 0.112544 | \-0.441502 | \-1.270590 | \-0.661008 | 1.330522 | 0.320135 | 1.167157 | \-1.364080 | \-0.220546 | 3.105750 | \-2.058362 | \-1.026274 | \-1.603823 | 0.843136 | \-1.978339 | 0.997299 | \-0.103197 | \-1.128308 | \-0.174338 | 0.411705 | \-0.972353 | 1.419469 | 0.610046 | \-0.188489 | \-1.130513 | 0.844059 | 1.224542 | \-0.436722 | \-3.069639 | 0.116501 | \-0.845159 | 1.586514 | \-1.484485 | 1.821135 | \-0.846458 | 0.198123 | 0.794855 | 0.862032 | \-0.034138 | \-0.492395 | 0.973250 | 0.901593 | 0.263111 | \-2.007821 | \-0.661586 | 0.063412 | 1.130984 | 0.233232 | \-1.174803 | \-0.875338 | 1.610706 | 0.299095 | \-0.290738 | 1.178792 | \-0.850622 | 1.504558 | 0.102695 | \-0.180380 | \-0.937365 | \-0.460620 | 0.362044 | 0.096921 | \-0.385210 | \-0.982422 | \-1.992112 | \-1.444678 | \-0.872915 | \-0.062038 | \-0.489576 | 0.670010 | \-0.001386 | \-0.731642 | \-1.024347 | \-0.378050 | 1.921468 | \-0.660317 | \-1.173823 | \-0.134648 | 0.923213 |
| 1   | \-0.356665 | \-0.966282 | 0.252394 | 0.495761 | 0.636330 | \-2.099039 | 0.306130 | \-0.028424 | 0.206351 | \-0.675954 | \-0.173781 | \-0.659855 | 0.739561 | 1.183141 | 0.470638 | \-1.290471 | \-0.601876 | \-1.678546 | 1.322868 | 0.270965 | \-1.654688 | 0.287904 | \-0.034230 | 2.260975 | \-0.458285 | \-0.416963 | \-0.791426 | \-0.193350 | \-1.792184 | \-1.318831 | \-0.776932 | 0.892524 | 1.638030 | 0.648060 | 0.050024 | \-0.079406 | \-0.168819 | \-0.528180 | 0.509640 | 0.389127 | \-1.753933 | \-0.856515 | 0.249594 | 0.470054 | \-0.870691 | 0.196685 | 0.419023 | 2.032849 | 1.801612 | \-0.579914 | 0.717563 | 0.423161 | 0.270556 | \-0.694673 | 0.387542 | \-0.276376 | \-1.052244 | \-2.330456 | 0.487283 | \-0.282307 | \-0.862809 | \-0.964048 | 0.006596 | 0.981186 | 0.222281 | 0.450658 | \-1.037929 | 0.242039 | 1.604181 | \-0.044079 | \-0.002931 | 0.890995 | \-0.498676 | 0.125733 | 0.170164 | 0.114292 | \-0.114529 | 0.643665 | 1.550666 | \-1.196385 | \-1.005633 | 0.987484 | \-2.474021 | \-0.942943 | 2.542174 | 2.005077 | \-2.240966 | 2.877203 | 0.288686 | \-0.074685 | \-0.195066 | \-0.156439 | \-0.786641 | 0.319762 | 1.421286 | 0.066732 | 1.170977 | 0.820487 | 2.648986 | \-0.209079 |
| 2   | \-0.749591 | 1.131690 | \-0.828222 | 0.650511 | \-1.565665 | \-0.155689 | \-0.233177 | 0.173176 | 1.329346 | 0.868886 | 0.776473 | 0.688853 | 1.776149 | 0.037287 | 0.451512 | \-0.719932 | \-0.382848 | 0.036005 | \-0.184394 | \-1.017601 | 0.945876 | 0.059931 | \-1.157834 | 0.478029 | \-0.038687 | 0.662824 | \-0.239063 | 1.090865 | \-0.130192 | 0.472693 | \-1.933048 | \-0.608379 | 0.869687 | 0.226225 | \-0.160558 | \-0.879435 | 0.306166 | \-1.147555 | 0.415554 | \-0.422111 | 0.471486 | \-0.982343 | \-0.946057 | 0.806259 | \-0.658906 | 0.737453 | \-0.057951 | \-0.549889 | \-0.636656 | \-0.548671 | \-0.575404 | \-0.099271 | 2.593643 | \-0.155903 | 1.853823 | \-0.259022 | 0.606196 | \-1.434706 | \-0.782503 | \-0.327437 | \-0.864812 | \-0.237751 | \-2.423010 | \-1.128286 | \-0.494937 | \-0.477452 | \-1.281871 | \-0.259802 | 0.079020 | 1.154653 | 0.264920 | 0.290462 | 0.011565 | \-1.463453 | \-0.799214 | 1.749990 | 0.079577 | \-0.741525 | 0.343831 | 0.523582 | 1.181326 | 0.953577 | \-1.179192 | \-0.978718 | 0.200574 | \-0.040077 | \-0.320622 | \-1.298582 | \-0.321176 | \-0.892720 | 0.261124 | \-0.736350 | \-0.061693 | 0.545805 | \-1.435774 | \-0.193081 | 0.243715 | 1.721250 | \-0.420792 | 1.055831 |
| 3   | 0.502827 | \-0.217032 | 0.776575 | \-1.429009 | \-1.022916 | 1.128800 | 0.736995 | \-2.015919 | \-0.798160 | \-1.162292 | 0.423827 | \-0.204595 | \-1.546579 | \-0.056928 | \-0.491460 | 0.789149 | \-0.701279 | \-1.328249 | 0.905490 | \-2.317994 | \-0.687140 | 1.770423 | \-1.214158 | \-0.128554 | 0.863697 | \-0.501916 | \-0.249389 | \-0.822525 | 0.606922 | 1.070422 | 0.012283 | \-0.181826 | 0.366801 | 1.598871 | 2.095979 | \-1.393260 | 0.795446 | 0.322609 | \-1.150727 | \-1.018983 | 0.089334 | 0.040401 | \-1.284350 | \-1.774508 | \-1.185096 | \-1.395004 | \-0.238120 | 0.711092 | 0.950707 | 1.051353 | 0.174049 | 1.261710 | \-0.990400 | \-0.013817 | \-0.487245 | 0.988920 | 0.196469 | 0.627224 | \-0.559631 | \-0.187514 | 0.018345 | \-0.424565 | 0.221240 | \-0.315089 | 0.061901 | 0.259872 | 0.715757 | \-0.519667 | 0.135466 | \-0.334678 | 1.222096 | 0.076765 | \-0.974797 | 0.526380 | \-0.914822 | 0.261372 | 0.974278 | \-0.009076 | 0.013396 | \-1.689943 | 1.103502 | \-1.197549 | 2.344155 | 1.146182 | \-0.185935 | 0.686092 | \-0.136343 | 0.322569 | \-1.151059 | \-0.470254 | \-0.689035 | 0.829976 | \-0.298176 | \-0.113427 | \-1.129214 | \-1.695072 | 0.519424 | 0.229655 | 2.277886 | 0.265250 |
| B   | 0   | 0   | 1.140159 | 0.421843 | \-0.343562 | \-0.876320 | 0.331853 | 1.044824 | 0.194269 | 1.070443 | \-2.407457 | 0.080689 | \-0.598584 | \-0.111730 | 0.244424 | 0.233870 | 0.487043 | 0.566249 | 1.335058 | 0.259083 | \-0.605676 | 1.168961 | \-0.976273 | 0.295315 | 0.114293 | \-0.154712 | \-1.313154 | \-0.088516 | \-1.171459 | 0.606761 | 1.074177 | \-0.974144 | 1.395917 | 1.317325 | \-0.800204 | \-0.029009 | \-2.244747 | 0.744557 | \-0.312767 | \-0.986406 | \-0.167304 | 0.628170 | \-0.228609 | \-0.147294 | 0.562133 | 0.283782 | \-0.788987 | 0.430063 | 0.452746 | 1.897825 | \-0.417987 | 0.492007 | 0.093273 | \-0.072178 | \-0.350011 | 0.120502 | 0.926225 | 0.786423 | \-1.296064 | 0.825564 | \-0.578341 | \-0.644492 | \-0.415373 | 1.142916 | \-1.252773 | 0.000250 | \-0.943390 | \-1.316790 | 0.771537 | \-0.060666 | \-1.115891 | \-0.037260 | 0.336697 | \-0.419495 | 0.844290 | \-0.406384 | 0.726910 | 0.801403 | \-1.774039 | 1.299428 | 0.319577 | 1.344228 | \-0.910131 | 0.152672 | 2.961074 | 0.857680 | 0.678394 | \-1.122245 | 0.017110 | \-1.073681 | \-1.176131 | 0.015466 | \-2.781098 | \-0.522587 | \-0.973759 | \-0.765304 | 0.373246 | \-0.329447 | 0.585703 | \-0.550335 | \-1.373650 | \-1.374684 |
| 1   | 0.473210 | \-2.375967 | \-0.751571 | 1.340774 | \-0.292321 | \-0.298160 | 0.650556 | 0.957706 | \-1.089526 | \-0.091775 | 1.043711 | \-0.070319 | 0.558694 | 0.288969 | 0.685963 | 0.998607 | 0.173647 | 0.960728 | \-0.696101 | 0.156879 | \-0.490952 | 0.475577 | \-1.304201 | 0.838231 | \-1.762388 | \-1.082789 | \-0.722490 | 0.432377 | \-0.133981 | 1.401917 | \-1.989990 | \-0.598459 | \-0.344521 | 0.019051 | 0.431813 | \-0.391747 | \-0.071103 | 0.285028 | \-0.502880 | \-1.343417 | 0.781904 | \-0.167854 | 0.146754 | \-1.585850 | 0.375186 | 0.520943 | \-0.925393 | \-0.197976 | 0.797735 | \-0.931065 | \-0.158778 | 0.529645 | \-0.720138 | \-0.654246 | 0.603385 | 0.285248 | \-1.065553 | 0.070157 | 0.363451 | \-0.191448 | 1.098395 | \-1.390976 | \-0.935790 | 0.514811 | \-0.189333 | \-0.294067 | \-1.791306 | 0.400007 | 0.251203 | 0.877140 | 0.099326 | \-2.536606 | \-0.517072 | 0.264774 | 0.934519 | \-0.880935 | \-0.496924 | \-0.075644 | \-0.851056 | 1.558560 | \-1.413553 | 0.194210 | \-1.164501 | \-0.125958 | 0.582427 | 0.534269 | \-0.327974 | 0.708747 | 0.251884 | \-0.080712 | \-0.480917 | 0.749453 | \-1.230035 | \-0.726606 | \-1.711782 | 0.624504 | 0.116664 | \-0.971840 | 1.372728 | 0.002035 |
| 2   | 1.302712 | 2.082694 | \-1.677985 | \-1.555907 | \-0.523275 | 0.839967 | \-2.604440 | 0.106786 | 1.118424 | 1.416623 | 1.176300 | \-0.570607 | 0.016937 | \-1.320549 | \-0.688524 | \-1.085140 | 0.849085 | 0.365578 | \-0.916659 | 1.103257 | 1.197104 | \-0.005171 | 1.272970 | 1.508463 | \-0.791778 | \-1.286589 | \-1.363629 | \-1.275104 | \-0.995168 | \-0.732797 | 1.011776 | \-0.599023 | 1.921324 | \-0.191943 | 0.253868 | \-0.556763 | 0.057446 | \-1.573751 | \-0.547084 | 1.346639 | 0.363929 | 1.608864 | 2.059999 | \-0.348148 | 1.266174 | 0.901752 | \-1.901187 | \-0.045168 | \-0.633390 | 2.238007 | 0.051228 | 0.852666 | \-0.836563 | 1.546189 | \-0.787396 | \-0.570315 | \-0.740769 | 1.802785 | 1.239590 | 0.596627 | 2.355694 | 0.538054 | 0.285362 | \-1.808742 | \-1.277903 | \-1.634502 | \-1.489241 | 0.059391 | 1.265560 | \-1.177802 | 0.233532 | \-1.976658 | \-2.173126 | \-0.067194 | 2.062263 | \-1.986836 | 1.372906 | \-0.364234 | 1.010591 | 0.747427 | 0.757398 | 0.683171 | 0.628683 | 0.332984 | \-1.273558 | \-0.775635 | 1.000520 | \-0.068911 | \-0.829279 | \-0.466159 | \-0.100714 | 0.663795 | 1.254263 | 0.544026 | \-0.152562 | \-1.063864 | \-0.766474 | 1.521726 | 0.025230 | 0.263135 |
| 3   | 0.703585 | 1.086720 | \-0.698876 | 2.317539 | 0.138207 | 0.423882 | \-1.111176 | \-0.094467 | 0.952610 | \-0.293499 | 0.667840 | \-0.375226 | \-0.147251 | \-0.637145 | 1.517303 | 3.132466 | 1.371238 | 0.210585 | 1.693381 | \-0.379665 | 0.266554 | \-0.185872 | \-1.818437 | 2.506759 | \-0.397273 | 0.385640 | \-1.042844 | 0.624709 | \-0.451187 | 1.083564 | \-0.676813 | 0.514574 | 2.275493 | \-0.766653 | 0.678269 | 0.534969 | \-1.899356 | 1.014444 | 0.223053 | \-0.945507 | 0.940518 | 0.568774 | 1.411102 | \-0.364688 | 0.889829 | \-0.119186 | 1.361843 | 1.212419 | \-0.224461 | 1.436537 | \-1.776686 | \-0.895706 | \-1.037786 | 0.313883 | 0.005282 | \-0.069917 | \-0.609770 | 0.171258 | \-0.866273 | 0.155435 | \-1.182975 | 0.330804 | 0.389467 | \-0.164819 | \-0.008973 | 0.802583 | 2.266305 | 0.319811 | \-1.924570 | \-0.234520 | 0.841021 | \-0.575380 | 1.100507 | \-0.042184 | \-0.636172 | \-0.625081 | \-0.262145 | 1.063613 | 0.562741 | 1.179673 | 0.431427 | \-0.045187 | \-0.373604 | \-1.130172 | 0.031504 | \-0.648830 | \-1.804172 | \-0.596727 | 0.183587 | \-0.611858 | 0.580205 | 0.544385 | \-1.399456 | \-0.665399 | 1.639616 | 0.451873 | 0.022969 | \-0.616657 | 1.512779 | \-1.122630 |
| 1   | 0   | 1.164710 | \-0.777462 | 1.667639 | \-1.088535 | 1.060841 | \-0.901320 | 0.796235 | 1.090697 | \-0.556709 | 0.887566 | 1.271675 | \-0.417219 | \-1.441265 | \-1.402080 | 0.190661 | 0.372360 | 0.497639 | \-0.726344 | \-1.084341 | \-1.778875 | \-0.166976 | 0.301156 | 0.341455 | 0.768867 | \-0.148901 | 0.478981 | 0.318396 | 0.136812 | \-0.414197 | 0.173897 | 1.888839 | 0.613031 | 1.621105 | \-1.508925 | \-0.485501 | \-0.218566 | 0.619560 | \-0.515451 | 0.984699 | 0.433396 | 0.211493 | 1.142100 | 0.055450 | 0.286748 | \-0.478570 | \-0.579152 | \-0.919767 | 0.061121 | \-2.901697 | \-1.185319 | \-0.199465 | \-3.358236 | 1.644457 | 1.152189 | 0.712913 | 0.606704 | \-0.530227 | 0.487737 | 1.984403 | 1.835091 | \-0.406201 | 0.954839 | \-1.292238 | \-0.647831 | \-0.331870 | 1.114978 | \-1.556536 | \-0.479194 | 1.762067 | \-0.673566 | 0.028405 | \-1.571476 | \-0.129625 | \-0.289627 | \-0.826554 | 0.531009 | 1.509519 | 0.007885 | \-0.276068 | 0.533845 | \-0.274268 | 0.342263 | \-0.231432 | 0.685758 | 0.894081 | 0.264197 | 0.025119 | 0.665642 | \-0.137437 | 1.487287 | \-0.225209 | \-0.470140 | 0.787341 | 0.198537 | \-0.316717 | 0.679350 | \-0.765168 | 0.085950 | \-1.035197 | \-1.632781 |
| 1   | \-0.934022 | \-0.040694 | 1.167349 | \-1.190301 | 0.659704 | \-2.747159 | 0.699066 | \-0.598891 | \-2.389625 | 1.278752 | \-0.204705 | 1.368727 | \-1.007521 | 0.049473 | 0.516073 | \-1.507334 | \-0.538353 | 0.049752 | \-1.735942 | 0.293528 | 1.310537 | 0.612638 | 1.895059 | \-0.970561 | \-0.449245 | \-0.988250 | 1.381542 | 0.014603 | \-1.056730 | 0.097341 | 1.688274 | 1.086608 | 0.196618 | \-0.723343 | \-1.292527 | \-0.919669 | 1.576322 | 0.004880 | 0.071091 | \-0.330820 | \-0.290122 | \-0.806495 | 0.030540 | \-0.421577 | 0.455043 | \-1.166432 | 1.907502 | 0.176228 | 1.327814 | 0.481270 | \-0.136838 | 0.605676 | \-0.135607 | \-0.941975 | 1.041375 | 1.700154 | 0.542979 | \-0.596294 | \-1.016533 | 1.340196 | \-0.380741 | \-0.234488 | \-0.026382 | 1.399027 | \-0.682410 | 0.393615 | \-0.648677 | 1.938602 | 0.451682 | \-0.425101 | \-0.639269 | \-0.242342 | 0.090562 | \-0.719265 | 1.512436 | \-0.988682 | 1.802555 | 1.837977 | \-1.656185 | \-1.125617 | 0.955744 | \-0.345026 | \-0.741394 | 0.252191 | 0.189325 | 1.466398 | \-2.101633 | 0.697772 | \-0.262199 | \-0.565488 | 1.522020 | \-1.386808 | 0.029429 | 0.597618 | \-0.791023 | \-1.197469 | 0.147968 | \-0.466924 | 2.310563 | 1.106685 |
| 2   | \-1.781068 | \-1.228565 | 2.367484 | 0.478429 | \-0.653350 | \-0.168068 | \-0.480661 | 0.197105 | \-0.949376 | 1.925986 | 0.298537 | \-0.206352 | \-0.979744 | \-0.744148 | \-0.139285 | \-1.261164 | 0.446535 | 0.568097 | 1.702812 | 0.671052 | \-0.599890 | 0.093166 | \-0.340463 | \-0.339369 | 1.989692 | 1.406806 | \-0.367648 | 1.339758 | 1.771004 | 0.359098 | \-0.298364 | \-0.139448 | \-1.741361 | \-1.570463 | \-0.840369 | \-0.121304 | \-0.843416 | \-0.540409 | 0.354715 | 1.672383 | 0.385298 | 1.118102 | 1.270384 | 0.918830 | 0.391359 | 0.506434 | \-0.203019 | 0.991611 | \-0.868176 | 0.068244 | \-0.564428 | 0.540511 | \-0.043091 | \-1.489450 | 0.484375 | 0.206646 | \-0.814915 | \-0.429202 | \-0.283868 | 1.881487 | \-0.832137 | 0.573218 | 1.480981 | \-0.054202 | 0.685618 | \-0.026086 | 0.133507 | 0.489659 | 1.548035 | \-0.610755 | 0.934192 | \-0.243997 | \-2.110242 | 1.449234 | \-0.091584 | \-1.749582 | \-1.533301 | 0.629799 | \-1.655075 | \-2.572022 | \-0.029369 | \-0.443355 | \-0.650839 | \-0.169573 | \-0.988550 | \-0.804586 | 1.231931 | \-0.542490 | 1.395549 | 1.328407 | 0.554684 | 0.440731 | \-0.681191 | 0.586516 | \-0.230103 | \-0.594544 | \-0.054775 | 0.416148 | \-1.637474 | \-0.278996 |
| 3   | \-1.426027 | \-0.796887 | \-0.533244 | \-0.454206 | \-0.176671 | 0.078048 | 1.294698 | \-0.868407 | \-1.309142 | 0.949318 | \-0.719067 | \-0.285576 | \-0.364888 | 0.527303 | 1.008922 | \-2.788126 | 0.066559 | 0.695167 | \-0.201521 | 0.696496 | 0.424995 | 0.903076 | 0.226559 | 0.389885 | 0.349896 | \-1.687575 | \-1.688522 | \-0.113054 | 1.568585 | 0.500880 | 0.404757 | \-0.774242 | 2.427805 | 0.659742 | 0.723677 | \-0.710790 | \-1.257576 | \-0.827174 | 1.073705 | 1.415423 | \-1.086741 | \-0.448521 | 0.714920 | \-0.817697 | 0.813939 | \-1.318669 | \-1.321715 | \-0.955649 | 0.386657 | 1.625277 | 0.100724 | \-1.356867 | 2.015564 | 0.282621 | \-0.100701 | 1.397511 | 1.479562 | 0.196954 | \-0.407965 | \-0.026595 | 0.887757 | 0.490851 | \-0.655784 | 1.533915 | \-0.249060 | 0.689923 | \-1.367955 | 1.375355 | 0.919708 | 1.177626 | \-0.848278 | 1.408821 | 0.054024 | \-0.587595 | \-0.575131 | \-0.947471 | \-0.796451 | \-1.080850 | \-0.703180 | \-0.427878 | 1.027534 | 0.692969 | \-1.048125 | \-0.614451 | 0.251322 | \-1.002167 | \-1.691401 | 0.085313 | 0.603232 | 0.528476 | \-0.693425 | \-1.256650 | 0.019255 | 1.771643 | \-1.065027 | \-2.055516 | \-1.194088 | \-1.083951 | \-0.570143 | \-0.061593 |

### HTML Escaping[#](https://pandas.pydata.org/docs/user_guide/style.html#HTML-Escaping "Link to this heading")

Suppose you have to display HTML within HTML, that can be a bit of pain when the renderer can’t distinguish. You can use the `escape` formatting option to handle this, and even use it within a formatter that contains HTML itself.

Note that if you’re using `Styler` on untrusted, user-provided input to serve HTML then you should escape the input to prevent security vulnerabilities. See the Jinja2 documentation for more.

\[66\]:

Copy to clipboard

df4 \= pd.DataFrame(\[\["<div></div>", '"&other"', "<span></span>"\]\])
df4.style

Copy to clipboard

\[66\]:

Copy to clipboard

|     | 0   | 1   | 2   |
| --- | --- | --- | --- |
| 0   |     | "&other" |     |

\[67\]:

Copy to clipboard

df4.style.format(escape\="html")

Copy to clipboard

\[67\]:

Copy to clipboard

|     | 0   | 1   | 2   |
| --- | --- | --- | --- |
| 0   | <div></div> | "&other" | <span></span> |

\[68\]:

Copy to clipboard

df4.style.format(
    '<a href="https://pandas.pydata.org" target="\_blank">{}</a>', escape\="html"
)

Copy to clipboard

\[68\]:

Copy to clipboard

|     | 0   | 1   | 2   |
| --- | --- | --- | --- |
| 0   | [<div></div>](https://pandas.pydata.org/) | ["&other"](https://pandas.pydata.org/) | [<span></span>](https://pandas.pydata.org/) |

Export to Excel[#](https://pandas.pydata.org/docs/user_guide/style.html#Export-to-Excel "Link to this heading")

----------------------------------------------------------------------------------------------------------------

Some support (_since version 0.20.0_) is available for exporting styled `DataFrames` to Excel worksheets using the `OpenPyXL` or `XlsxWriter` engines. CSS2.2 properties handled include:

*   `background-color`
    
*   `border-style` properties
    
*   `border-width` properties
    
*   `border-color` properties
    
*   `color`
    
*   `font-family`
    
*   `font-style`
    
*   `font-weight`
    
*   `text-align`
    
*   `text-decoration`
    
*   `vertical-align`
    
*   `white-space: nowrap`
    
*   Shorthand and side-specific border properties are supported (e.g. `border-style` and `border-left-style`) as well as the `border` shorthands for all sides (`border: 1px solid green`) or specified sides (`border-left: 1px solid green`). Using a `border` shorthand will override any border properties set before it (See [CSS Working Group](https://drafts.csswg.org/css-backgrounds/#border-shorthands)
     for more details)
    
*   Only CSS2 named colors and hex colors of the form `#rgb` or `#rrggbb` are currently supported.
    
*   The following pseudo CSS properties are also available to set Excel specific style properties:
    
    *   `number-format`
        
    *   `border-style` (for Excel-specific styles: “hair”, “mediumDashDot”, “dashDotDot”, “mediumDashDotDot”, “dashDot”, “slantDashDot”, or “mediumDashed”)
        

Table level styles, and data cell CSS-classes are not included in the export to Excel: individual cells must have their properties mapped by the `Styler.apply` and/or `Styler.map` methods.

\[69\]:

Copy to clipboard

df2.style.map(style\_negative, props\="color:red;").highlight\_max(axis\=0).to\_excel(
    "styled.xlsx", engine\="openpyxl"
)

Copy to clipboard

A screenshot of the output:

![Excel spreadsheet with styled DataFrame](https://pandas.pydata.org/docs/_images/style-excel.png)

Export to LaTeX[#](https://pandas.pydata.org/docs/user_guide/style.html#Export-to-LaTeX "Link to this heading")

----------------------------------------------------------------------------------------------------------------

There is support (_since version 1.3.0_) to export `Styler` to LaTeX. The documentation for the [.to\_latex](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_latex.html)
 method gives further detail and numerous examples.

More About CSS and HTML[#](https://pandas.pydata.org/docs/user_guide/style.html#More-About-CSS-and-HTML "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------

Cascading Style Sheet (CSS) language, which is designed to influence how a browser renders HTML elements, has its own peculiarities. It never reports errors: it just silently ignores them and doesn’t render your objects how you intend so can sometimes be frustrating. Here is a very brief primer on how `Styler` creates HTML and interacts with CSS, with advice on common pitfalls to avoid.

### CSS Classes and Ids[#](https://pandas.pydata.org/docs/user_guide/style.html#CSS-Classes-and-Ids "Link to this heading")

The precise structure of the CSS `class` attached to each cell is as follows.

*   Cells with Index and Column names include `index_name` and `level<k>` where `k` is its level in a MultiIndex
    
*   Index label cells include
    
    *   `row_heading`
        
    *   `level<k>` where `k` is the level in a MultiIndex
        
    *   `row<m>` where `m` is the numeric position of the row
        
*   Column label cells include
    
    *   `col_heading`
        
    *   `level<k>` where `k` is the level in a MultiIndex
        
    *   `col<n>` where `n` is the numeric position of the column
        
*   Data cells include
    
    *   `data`
        
    *   `row<m>`, where `m` is the numeric position of the cell.
        
    *   `col<n>`, where `n` is the numeric position of the cell.
        
*   Blank cells include `blank`
    
*   Trimmed cells include `col_trim` or `row_trim`
    

The structure of the `id` is `T_uuid_level<k>_row<m>_col<n>` where `level<k>` is used only on headings, and headings will only have either `row<m>` or `col<n>` whichever is needed. By default we’ve also prepended each row/column identifier with a UUID unique to each DataFrame so that the style from one doesn’t collide with the styling from another within the same notebook or page. You can read more about the use of UUIDs in [Optimization](https://pandas.pydata.org/docs/user_guide/style.html#Optimization)
.

We can see example of the HTML by calling the [.to\_html()](https://pandas.pydata.org/docs/reference/api/pandas.io.formats.style.Styler.to_html.html)
 method.

\[70\]:

Copy to clipboard

print(
    pd.DataFrame(
        \[\[1, 2\], \[3, 4\]\], index\=\["i1", "i2"\], columns\=\["c1", "c2"\]
    ).style.to\_html()
)

Copy to clipboard

<style type="text/css">
</style>
<table id="T\_7d43d">
  <thead>
    <tr>
      <th class="blank level0" >&nbsp;</th>
      <th id="T\_7d43d\_level0\_col0" class="col\_heading level0 col0" >c1</th>
      <th id="T\_7d43d\_level0\_col1" class="col\_heading level0 col1" >c2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th id="T\_7d43d\_level0\_row0" class="row\_heading level0 row0" >i1</th>
      <td id="T\_7d43d\_row0\_col0" class="data row0 col0" >1</td>
      <td id="T\_7d43d\_row0\_col1" class="data row0 col1" >2</td>
    </tr>
    <tr>
      <th id="T\_7d43d\_level0\_row1" class="row\_heading level0 row1" >i2</th>
      <td id="T\_7d43d\_row1\_col0" class="data row1 col0" >3</td>
      <td id="T\_7d43d\_row1\_col1" class="data row1 col1" >4</td>
    </tr>
  </tbody>
</table>

Copy to clipboard

### CSS Hierarchies[#](https://pandas.pydata.org/docs/user_guide/style.html#CSS-Hierarchies "Link to this heading")

The examples have shown that when CSS styles overlap, the one that comes last in the HTML render, takes precedence. So the following yield different results:

\[71\]:

Copy to clipboard

df4 \= pd.DataFrame(\[\["text"\]\])
df4.style.map(lambda x: "color:green;").map(lambda x: "color:red;")

Copy to clipboard

\[71\]:

Copy to clipboard

|     | 0   |
| --- | --- |
| 0   | text |

\[72\]:

Copy to clipboard

df4.style.map(lambda x: "color:red;").map(lambda x: "color:green;")

Copy to clipboard

\[72\]:

Copy to clipboard

|     | 0   |
| --- | --- |
| 0   | text |

This is only true for CSS rules that are equivalent in hierarchy, or importance. You can read more about [CSS specificity here](https://www.w3schools.com/css/css_specificity.asp)
 but for our purposes it suffices to summarize the key points:

A CSS importance score for each HTML element is derived by starting at zero and adding:

*   1000 for an inline style attribute
    
*   100 for each ID
    
*   10 for each attribute, class or pseudo-class
    
*   1 for each element name or pseudo-element
    

Let’s use this to describe the action of the following configurations

\[73\]:

Copy to clipboard

df4.style.set\_uuid("a\_").set\_table\_styles(
    \[{"selector": "td", "props": "color:red;"}\]
).map(lambda x: "color:green;")

Copy to clipboard

\[73\]:

Copy to clipboard

|     | 0   |
| --- | --- |
| 0   | text |

This text is red because the generated selector `#T_a_ td` is worth 101 (ID plus element), whereas `#T_a_row0_col0` is only worth 100 (ID), so is considered inferior even though in the HTML it comes after the previous.

\[74\]:

Copy to clipboard

df4.style.set\_uuid("b\_").set\_table\_styles(
    \[\
        {"selector": "td", "props": "color:red;"},\
        {"selector": ".cls-1", "props": "color:blue;"},\
    \]
).map(lambda x: "color:green;").set\_td\_classes(pd.DataFrame(\[\["cls-1"\]\]))

Copy to clipboard

\[74\]:

Copy to clipboard

|     | 0   |
| --- | --- |
| 0   | text |

In the above case the text is blue because the selector `#T_b_ .cls-1` is worth 110 (ID plus class), which takes precedence.

\[75\]:

Copy to clipboard

df4.style.set\_uuid("c\_").set\_table\_styles(
    \[\
        {"selector": "td", "props": "color:red;"},\
        {"selector": ".cls-1", "props": "color:blue;"},\
        {"selector": "td.data", "props": "color:yellow;"},\
    \]
).map(lambda x: "color:green;").set\_td\_classes(pd.DataFrame(\[\["cls-1"\]\]))

Copy to clipboard

\[75\]:

Copy to clipboard

|     | 0   |
| --- | --- |
| 0   | text |

Now we have created another table style this time the selector `T_c_ td.data` (ID plus element plus class) gets bumped up to 111.

If your style fails to be applied, and its really frustrating, try the `!important` trump card.

\[76\]:

Copy to clipboard

df4.style.set\_uuid("d\_").set\_table\_styles(
    \[\
        {"selector": "td", "props": "color:red;"},\
        {"selector": ".cls-1", "props": "color:blue;"},\
        {"selector": "td.data", "props": "color:yellow;"},\
    \]
).map(lambda x: "color:green !important;").set\_td\_classes(pd.DataFrame(\[\["cls-1"\]\]))

Copy to clipboard

\[76\]:

Copy to clipboard

|     | 0   |
| --- | --- |
| 0   | text |

Finally got that green text after all!

Extensibility[#](https://pandas.pydata.org/docs/user_guide/style.html#Extensibility "Link to this heading")

------------------------------------------------------------------------------------------------------------

The core of pandas is, and will remain, its “high-performance, easy-to-use data structures”. With that in mind, we hope that `DataFrame.style` accomplishes two goals

*   Provide an API that is pleasing to use interactively and is “good enough” for many tasks
    
*   Provide the foundations for dedicated libraries to build on
    

If you build a great library on top of this, let us know and we’ll [link](https://pandas.pydata.org/community/ecosystem.html)
 to it.

### Subclassing[#](https://pandas.pydata.org/docs/user_guide/style.html#Subclassing "Link to this heading")

If the default template doesn’t quite suit your needs, you can subclass Styler and extend or override the template. We’ll show an example of extending the default template to insert a custom header before each table.

\[77\]:

Copy to clipboard

from jinja2 import Environment, ChoiceLoader, FileSystemLoader
from IPython.display import HTML
from pandas.io.formats.style import Styler

Copy to clipboard

We’ll use the following template:

\[78\]:

Copy to clipboard

with open("templates/myhtml.tpl") as f\_html:
    print(f\_html.read())

Copy to clipboard

{% extends "html\_table.tpl" %}
{% block table %}
<h1>{{ table\_title|default("My Table") }}</h1>
{{ super() }}
{% endblock table %}

Copy to clipboard

Now that we’ve created a template, we need to set up a subclass of `Styler` that knows about it.

\[79\]:

Copy to clipboard

class MyStyler(Styler):
    env \= Environment(
        loader\=ChoiceLoader(
            \[\
                FileSystemLoader("templates"),  \# contains ours\
                Styler.loader,  \# the default\
            \]
        )
    )
    template\_html\_table \= env.get\_template("myhtml.tpl")

Copy to clipboard

Notice that we include the original loader in our environment’s loader. That’s because we extend the original template, so the Jinja environment needs to be able to find it.

Now we can use that custom styler. It’s `__init__` takes a DataFrame.

\[80\]:

Copy to clipboard

MyStyler(df3)

Copy to clipboard

\[80\]:

Copy to clipboard

My Table
========

|     |     | c1  | c2  | c3  | c4  |
| --- | --- | --- | --- | --- | --- |
| A   | r1  | 1.659801 | 0.514933 | \-0.117619 | \-1.451866 |
| r2  | \-0.439634 | 1.374616 | \-0.349268 | 0.237399 |
| B   | r1  | \-0.533508 | 0.099571 | \-1.088552 | \-0.391217 |
| r2  | \-0.541924 | \-1.357582 | \-0.025377 | 0.829804 |

Our custom template accepts a `table_title` keyword. We can provide the value in the `.to_html` method.

\[81\]:

Copy to clipboard

HTML(MyStyler(df3).to\_html(table\_title\="Extending Example"))

Copy to clipboard

\[81\]:

Copy to clipboard

Extending Example
=================

|     |     | c1  | c2  | c3  | c4  |
| --- | --- | --- | --- | --- | --- |
| A   | r1  | 1.659801 | 0.514933 | \-0.117619 | \-1.451866 |
| r2  | \-0.439634 | 1.374616 | \-0.349268 | 0.237399 |
| B   | r1  | \-0.533508 | 0.099571 | \-1.088552 | \-0.391217 |
| r2  | \-0.541924 | \-1.357582 | \-0.025377 | 0.829804 |

For convenience, we provide the `Styler.from_custom_template` method that does the same as the custom subclass.

\[82\]:

Copy to clipboard

EasyStyler \= Styler.from\_custom\_template("templates", "myhtml.tpl")
HTML(EasyStyler(df3).to\_html(table\_title\="Another Title"))

Copy to clipboard

\[82\]:

Copy to clipboard

Another Title
=============

|     |     | c1  | c2  | c3  | c4  |
| --- | --- | --- | --- | --- | --- |
| A   | r1  | 1.659801 | 0.514933 | \-0.117619 | \-1.451866 |
| r2  | \-0.439634 | 1.374616 | \-0.349268 | 0.237399 |
| B   | r1  | \-0.533508 | 0.099571 | \-1.088552 | \-0.391217 |
| r2  | \-0.541924 | \-1.357582 | \-0.025377 | 0.829804 |

#### Template Structure[#](https://pandas.pydata.org/docs/user_guide/style.html#Template-Structure "Link to this heading")

Here’s the template structure for the both the style generation template and the table generation template:

Style template:

\[84\]:

Copy to clipboard

HTML(style\_structure)

Copy to clipboard

\[84\]:

Copy to clipboard

before\_style

style

<style type="text/css">

table\_styles

before\_cellstyle

cellstyle

</style>

Table template:

\[86\]:

Copy to clipboard

HTML(table\_structure)

Copy to clipboard

\[86\]:

Copy to clipboard

before\_table

table

<table ...>

caption

thead

before\_head\_rows

head\_tr (loop over headers)

after\_head\_rows

tbody

before\_rows

tr (loop over data rows)

after\_rows

</table>

after\_table

See the template in the [GitHub repo](https://github.com/pandas-dev/pandas)
 for more details.

On this page