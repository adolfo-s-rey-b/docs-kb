[Skip to main content](https://pandas.pydata.org/docs/getting_started/overview.html#main-content)

Back to top Ctrl+K

3.1 (stable)

[dev](https://pandas.pydata.org/docs/dev/getting_started/overview.html)
[3.1 (stable)](https://pandas.pydata.org/docs/getting_started/overview.html)
[3.0](https://pandas.pydata.org/pandas-docs/version/3.0/getting_started/overview.html)
[2.3](https://pandas.pydata.org/pandas-docs/version/2.3/getting_started/overview.html)
[2.2](https://pandas.pydata.org/pandas-docs/version/2.2/getting_started/overview.html)
[2.1](https://pandas.pydata.org/pandas-docs/version/2.1/getting_started/overview.html)
[2.0](https://pandas.pydata.org/pandas-docs/version/2.0/getting_started/overview.html)
[1.5](https://pandas.pydata.org/pandas-docs/version/1.5/getting_started/overview.html)
[1.4](https://pandas.pydata.org/pandas-docs/version/1.4/getting_started/overview.html)
[1.3](https://pandas.pydata.org/pandas-docs/version/1.3/getting_started/overview.html)
[1.2](https://pandas.pydata.org/pandas-docs/version/1.2/getting_started/overview.html)
[1.1](https://pandas.pydata.org/pandas-docs/version/1.1/getting_started/overview.html)
[1.0](https://pandas.pydata.org/pandas-docs/version/1.0/getting_started/overview.html)

*   System Settings
*   Light
*   Dark

*   [GitHub](https://github.com/pandas-dev/pandas)
    
*   [X](https://x.com/pandas_dev)
    
*   [Mastodon](https://fosstodon.org/@pandas_dev)
    

Collapse Sidebar Expand Sidebar

Package overview[#](https://pandas.pydata.org/docs/getting_started/overview.html#package-overview "Link to this heading")

==========================================================================================================================

pandas is a [Python](https://www.python.org/)
 package that provides fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive. It aims to be the fundamental high-level building block for Python’s practical, **real-world** data analysis. Additionally, it seeks to become **the most powerful and flexible open source data analysis/manipulation tool available in any language**. It is already well on its way toward this goal.

pandas is well suited for many different kinds of data:

> *   Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet
>     
> *   Ordered and unordered (not necessarily fixed-frequency) time series data.
>     
> *   Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels
>     
> *   Any other form of observational / statistical data sets. The data need not be labeled at all to be placed into a pandas data structure
>     

The two primary data structures of pandas, [`Series`](https://pandas.pydata.org/docs/reference/api/pandas.Series.html#pandas.Series "pandas.Series")
 (1-dimensional) and [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 (2-dimensional), handle the vast majority of typical use cases in finance, statistics, social science, and many areas of engineering. For R users, [`DataFrame`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html#pandas.DataFrame "pandas.DataFrame")
 provides everything that R’s `data.frame` provides and much more. pandas is built on top of [NumPy](https://numpy.org/)
 and is intended to integrate well within a scientific computing environment with many other 3rd party libraries.

Here are just a few of the things that pandas does well:

> *   Easy handling of **missing data** (represented as NaN) in floating point as well as non-floating point data
>     
> *   Size mutability: columns can be **inserted and deleted** from DataFrame and higher dimensional objects
>     
> *   Automatic and explicit **data alignment**: objects can be explicitly aligned to a set of labels, or the user can simply ignore the labels and let `Series`, `DataFrame`, etc. automatically align the data for you in computations
>     
> *   Powerful, flexible **group by** functionality to perform split-apply-combine operations on data sets, for both aggregating and transforming data
>     
> *   Make it **easy to convert** ragged, differently-indexed data in other Python and NumPy data structures into DataFrame objects
>     
> *   Intelligent label-based **slicing**, **fancy indexing**, and **subsetting** of large data sets
>     
> *   Intuitive **merging** and **joining** data sets
>     
> *   Flexible **reshaping** and pivoting of data sets
>     
> *   **Hierarchical** labeling of axes (possible to have multiple labels per tick)
>     
> *   Robust IO tools for loading data from **flat files** (CSV and delimited), Excel files, databases, and saving / loading data from the ultrafast **HDF5 format**
>     
> *   **Time series**\-specific functionality: date range generation and frequency conversion, moving window statistics, date shifting, and lagging.
>     

Many of these principles are here to address the shortcomings frequently experienced using other languages / scientific research environments. For data scientists, working with data is typically divided into multiple stages: munging and cleaning data, analyzing / modeling it, then organizing the results of the analysis into a form suitable for plotting or tabular display. pandas is the ideal tool for all of these tasks.

Some other notes

> *   pandas is **fast**. Many of the low-level algorithmic bits have been extensively tweaked in [Cython](https://cython.org/)
>      code. However, as with anything else generalization usually sacrifices performance. So if you focus on one feature for your application you may be able to create a faster specialized tool.
>     
> *   pandas is a dependency of [statsmodels](https://www.statsmodels.org/)
>     , making it an important part of the statistical computing ecosystem in Python.
>     
> *   pandas has been used extensively in production in financial applications.
>     

Data structures[#](https://pandas.pydata.org/docs/getting_started/overview.html#data-structures "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

  
| Dimensions | Name | Description |
| --- | --- | --- |
| 1   | Series | 1D labeled homogeneously-typed array |
| 2   | DataFrame | General 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed column |

### Why more than one data structure?[#](https://pandas.pydata.org/docs/getting_started/overview.html#why-more-than-one-data-structure "Link to this heading")

The best way to think about the pandas data structures is as flexible containers for lower dimensional data. For example, DataFrame is a container for Series, and Series is a container for scalars. We would like to be able to insert and remove objects from these containers in a dictionary-like fashion.

Also, we would like sensible default behaviors for the common API functions which take into account the typical orientation of time series and cross-sectional data sets. When using the N-dimensional array (ndarrays) to store 2- and 3-dimensional data, a burden is placed on the user to consider the orientation of the data set when writing functions; axes are considered more or less equivalent (except when C- or Fortran-contiguousness matters for performance). In pandas, the axes are intended to lend more semantic meaning to the data; i.e., for a particular data set, there is likely to be a “right” way to orient the data. The goal, then, is to reduce the amount of mental effort required to code up data transformations in downstream functions.

For example, with tabular data (DataFrame) it is more semantically helpful to think of the **index** (the rows) and the **columns** rather than axis 0 and axis 1. Iterating through the columns of the DataFrame thus results in more readable code:

for col in df.columns:
    series \= df\[col\]
    \# do something with series

Copy to clipboard

Mutability and copying of data[#](https://pandas.pydata.org/docs/getting_started/overview.html#mutability-and-copying-of-data "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------------------------------

All pandas data structures are value-mutable (the values they contain can be altered) but not always size-mutable. The length of a Series cannot be changed, but, for example, columns can be inserted into a DataFrame. However, the vast majority of methods produce new objects and leave the input data untouched. In general we like to **favor immutability** where sensible.

Getting support[#](https://pandas.pydata.org/docs/getting_started/overview.html#getting-support "Link to this heading")

------------------------------------------------------------------------------------------------------------------------

The first stop for pandas issues and ideas is the [GitHub Issue Tracker](https://github.com/pandas-dev/pandas/issues)
. If you have a general question, pandas community experts can answer through [Stack Overflow](https://stackoverflow.com/questions/tagged/pandas)
.

Community[#](https://pandas.pydata.org/docs/getting_started/overview.html#community "Link to this heading")

------------------------------------------------------------------------------------------------------------

pandas is actively supported today by a community of like-minded individuals around the world who contribute their valuable time and energy to help make open source pandas possible. Thanks to [all of our contributors](https://github.com/pandas-dev/pandas/graphs/contributors)
.

If you’re interested in contributing, please visit the [contributing guide](https://pandas.pydata.org/docs/development/contributing.html#contributing)
.

pandas is a [NumFOCUS](https://numfocus.org/sponsored-projects)
 sponsored project. This will help ensure the success of the development of pandas as a world-class open-source project and makes it possible to [donate](https://opencollective.com/pandas)
 to the project.

Project governance[#](https://pandas.pydata.org/docs/getting_started/overview.html#project-governance "Link to this heading")

------------------------------------------------------------------------------------------------------------------------------

The governance process that pandas project has used informally since its inception in 2008 is formalized in [Project Governance documents](https://github.com/pandas-dev/pandas/blob/main/web/pandas/about/governance.md)
. The documents clarify how decisions are made and how the various elements of our community interact, including the relationship between open source collaborative development and work that may be funded by for-profit or non-profit entities.

Wes McKinney is the Benevolent Dictator for Life (BDFL).

Development team[#](https://pandas.pydata.org/docs/getting_started/overview.html#development-team "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------

The list of the Core Team members and more detailed information can be found on the [pandas website](https://pandas.pydata.org/about/team.html)
.

Institutional partners[#](https://pandas.pydata.org/docs/getting_started/overview.html#institutional-partners "Link to this heading")

--------------------------------------------------------------------------------------------------------------------------------------

The information about current institutional partners can be found on [pandas website page](https://pandas.pydata.org/about/sponsors.html)
.

License[#](https://pandas.pydata.org/docs/getting_started/overview.html#license "Link to this heading")

--------------------------------------------------------------------------------------------------------

BSD 3-Clause License

Copyright (c) 2008-2011, AQR Capital Management, LLC, Lambda Foundry, Inc. and PyData Development Team
All rights reserved.

Copyright (c) 2011-2026, Open source contributors.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

\* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

\* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

\* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Copy to clipboard

On this page