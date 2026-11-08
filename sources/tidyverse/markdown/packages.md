Tidyverse packages
==================

Installation and use[](https://tidyverse.org/packages/#installation-and-use)

-----------------------------------------------------------------------------

*   Install all the packages in the tidyverse by running `install.packages("tidyverse")`.
    
*   Run `library(tidyverse)` to load the core tidyverse and make it available in your current R session.
    

Learn more about the tidyverse package at [https://tidyverse.tidyverse.org](https://tidyverse.tidyverse.org/)
.

Core tidyverse[](https://tidyverse.org/packages/#core-tidyverse)

-----------------------------------------------------------------

The core tidyverse includes the packages that you’re likely to use in everyday data analyses. As of tidyverse 1.3.0, the following packages are included in the core tidyverse:

[![](https://tidyverse.org/css/images/hex/ggplot2.png)](https://ggplot2.tidyverse.org/)

### [ggplot2](https://ggplot2.tidyverse.org/)

ggplot2 is a system for declaratively creating graphics, based on The Grammar of Graphics. You provide the data, tell ggplot2 how to map variables to aesthetics, what graphical primitives to use, and it takes care of the details. [Go to docs...](https://ggplot2.tidyverse.org/)

[![](https://tidyverse.org/css/images/hex/dplyr.png)](https://dplyr.tidyverse.org/)

### [dplyr](https://dplyr.tidyverse.org/)

dplyr provides a grammar of data manipulation, providing a consistent set of verbs that solve the most common data manipulation challenges. [Go to docs...](https://dplyr.tidyverse.org/)

[![](https://tidyverse.org/css/images/hex/tidyr.png)](https://tidyr.tidyverse.org/)

### [tidyr](https://tidyr.tidyverse.org/)

tidyr provides a set of functions that help you get to tidy data. Tidy data is data with a consistent form: in brief, every variable goes in a column, and every column is a variable. [Go to docs...](https://tidyr.tidyverse.org/)

[![](https://tidyverse.org/css/images/hex/readr.png)](https://readr.tidyverse.org/)

### [readr](https://readr.tidyverse.org/)

readr provides a fast and friendly way to read rectangular data (like csv, tsv, and fwf). It is designed to flexibly parse many types of data found in the wild, while still cleanly failing when data unexpectedly changes.  [Go to docs...](https://readr.tidyverse.org/)

[![](https://tidyverse.org/css/images/hex/purrr.png)](https://purrr.tidyverse.org/)

### [purrr](https://purrr.tidyverse.org/)

purrr enhances R’s functional programming (FP) toolkit by providing a complete and consistent set of tools for working with functions and vectors. Once you master the basic concepts, purrr allows you to replace many for loops with code that is easier to write and more expressive. [Go to docs...](https://purrr.tidyverse.org/)

[![](https://tidyverse.org/css/images/hex/tibble.png)](https://tibble.tidyverse.org/)

### [tibble](https://tibble.tidyverse.org/)

tibble is a modern re-imagining of the data frame, keeping what time has proven to be effective, and throwing out what it has not. Tibbles are data.frames that are lazy and surly: they do less and complain more forcing you to confront problems earlier, typically leading to cleaner, more expressive code. [Go to docs...](https://tibble.tidyverse.org/)

[![](https://tidyverse.org/css/images/hex/stringr.png)](https://stringr.tidyverse.org/)

### [stringr](https://stringr.tidyverse.org/)

stringr provides a cohesive set of functions designed to make working with strings as easy as possible. It is built on top of stringi, which uses the ICU C library to provide fast, correct implementations of common string manipulations. [Go to docs...](https://stringr.tidyverse.org/)

[![](https://tidyverse.org/css/images/hex/forcats.png)](https://forcats.tidyverse.org/)

### [forcats](https://forcats.tidyverse.org/)

forcats provides a suite of useful tools that solve common problems with factors. R uses factors to handle categorical variables, variables that have a fixed and known set of possible values. [Go to docs...](https://forcats.tidyverse.org/)

[![](https://tidyverse.org/css/images/hex/lubridate.png)](https://lubridate.tidyverse.org/)

### [lubridate](https://lubridate.tidyverse.org/)

lubridate provides a set of functions for working with date-times, extending and improving on R's existing support for them. [Go to docs...](https://lubridate.tidyverse.org/)

The tidyverse also includes many other packages with more specialised usage. They are not loaded automatically with `library(tidyverse)`, so you’ll need to load each one with its own call to `library()`.

Import[](https://tidyverse.org/packages/#import)

-------------------------------------------------

As well as [readr](https://readr.tidyverse.org/)
, for reading flat files, the tidyverse package installs a number of other packages for reading data:

*   [DBI](https://dbi.r-dbi.org/)
     for relational databases. (Maintained by [Kirill Müller](https://www.cynkra.com/)
    .) You’ll need to pair DBI with a database specific backends like [RSQLite](https://rsqlite.r-dbi.org/)
    , [RMariaDB](https://rmariadb.r-dbi.org/)
    , [RPostgres](https://rpostgres.r-dbi.org/)
    , or [odbc](https://github.com/r-dbi/odbc)
    . Learn more at [https://db.rstudio.com](https://db.rstudio.com/)
    .
    
*   [haven](https://haven.tidyverse.org/)
     for SPSS, Stata, and SAS data.
    
*   [httr](https://httr.r-lib.org/)
     for web APIs.
    
*   [readxl](https://readxl.tidyverse.org/)
     for `.xls` and `.xlsx` sheets.
    
*   [googlesheets4](https://googlesheets4.tidyverse.org/)
     for [Google Sheets](https://docs.google.com/spreadsheets/)
     via the [Sheets API v4](https://developers.google.com/sheets/api/)
    .
    
*   [googledrive](https://googledrive.tidyverse.org/)
     for [Google Drive](https://drive.google.com/)
     files.
    
*   [rvest](https://rvest.tidyverse.org/)
     for web scraping.
    
*   [jsonlite](https://github.com/jeroen/jsonlite#jsonlite)
     for JSON. (Maintained by [Jeroen Ooms](https://github.com/jeroen)
    .)
    
*   [xml2](https://xml2.r-lib.org/)
     for XML.
    

Wrangle[](https://tidyverse.org/packages/#wrangle)

---------------------------------------------------

In addition to [tidyr](https://tidyr.tidyverse.org/)
, [dplyr](https://dplyr.tidyverse.org/)
, and the three specialized packages already in core tidyverse ( [stringr](https://stringr.tidyverse.org/)
, [forcats](https://forcats.tidyverse.org/)
 and [lubridate](https://lubridate.tidyverse.org/)
), there are two others which are designed to work with specific types of data:

*   [hms](https://hms.tidyverse.org/)
     for time-of-day values.
*   [blob](https://blob.tidyverse.org/)
     for storing blob (binary) data.

### dplyr backends[](https://tidyverse.org/packages/#dplyr-backends)

There are also three packages that allow you to interface with different backends using the same dplyr syntax:

*   [dbplyr](https://dbplyr.tidyverse.org/)
     allows you to use remote database tables by converting dplyr code into SQL.
*   [dtplyr](https://dtplyr.tidyverse.org/)
     provides a [data.table](http://r-datatable.com/)
     backend by automatically translating to the equivalent, but usually much faster, data.table code.
*   [duckplyr](https://duckplyr.tidyverse.org/)
     runs existing dplyr code using [DuckDB](https://duckdb.org/)
     where possible, allowing for fast analysis of larger-than-memory datasets straight from local files or from the web.

Program[](https://tidyverse.org/packages/#program)

---------------------------------------------------

In addition to [purrr](https://purrr.tidyverse.org/)
, which provides very consistent and natural methods for iterating on R objects, there are two additional tidyverse packages that help with general programming challenges:

*   [magrittr](https://magrittr.tidyverse.org/)
     provides the pipe, `%>%` used throughout the tidyverse. It also provide a number of more specialised piping operators (like `%$%` and `%<>%`) that can be useful in other places.
    
*   [glue](https://glue.tidyverse.org/)
     provides an alternative to `paste()` that makes it easier to combine data and strings.
    

Model[](https://tidyverse.org/packages/#model)

-----------------------------------------------

Modeling with the tidyverse uses the collection of [tidymodels packages](https://www.tidymodels.org/)
, which largely replace the [modelr](https://modelr.tidyverse.org/)
 package used in [R4DS](https://r4ds.had.co.nz/)
. These packages provide a comprehensive foundation for creating and using models of all types. Visit the [_Getting Started_](https://www.tidymodels.org/start/)
 guide or, for more detailed examples, go straight to the [_Learn_](https://www.tidymodels.org/learn/)
 page.

Get help[](https://tidyverse.org/packages/#get-help)

-----------------------------------------------------

If you’re asking for R help, reporting a bug, or requesting a new feature, you’re more likely to succeed if you include a good reproducible example, which is precisely what the [reprex](https://reprex.tidyverse.org/)
 package is meant for. You can learn more about reprex, along with other tips on how to help others help you in the [help section](https://www.tidyverse.org/help/)
.

Contents

The tidyverse is proudly supported by[](https://posit.co/)

[Privacy policy](https://www.tidyverse.org/google_privacy_policy)
[](https://github.com/tidyverse)
[](https://twitter.com/hashtag/rstats)