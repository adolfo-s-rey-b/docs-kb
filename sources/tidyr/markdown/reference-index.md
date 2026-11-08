[Skip to content](https://tidyr.tidyverse.org/reference/index.html#container)

![](https://tidyr.tidyverse.org/logo.png)

Package index
=============

Pivoting[](https://tidyr.tidyverse.org/reference/index.html#pivoting)

----------------------------------------------------------------------

**Pivoting** changes the representation of a rectangular dataset, without changing the data inside of it. See `[vignette("pivot")](https://tidyr.tidyverse.org/articles/pivot.html) ` for more details and examples.

`[pivot_longer()](https://tidyr.tidyverse.org/reference/pivot_longer.html) `

Pivot data from wide to long

`[pivot_wider()](https://tidyr.tidyverse.org/reference/pivot_wider.html) `

Pivot data from long to wide

Rectangling[](https://tidyr.tidyverse.org/reference/index.html#rectangling)

----------------------------------------------------------------------------

**Rectangling** turns deeply nested lists into tidy tibbles. See `[vignette("rectangle")](https://tidyr.tidyverse.org/articles/rectangle.html) ` for more details and examples.

`[unnest_longer()](https://tidyr.tidyverse.org/reference/unnest_longer.html) `

Unnest a list-column into rows

`[unnest_wider()](https://tidyr.tidyverse.org/reference/unnest_wider.html) `

Unnest a list-column into columns

`[unnest()](https://tidyr.tidyverse.org/reference/unnest.html) `

Unnest a list-column of data frames into rows and columns

`[hoist()](https://tidyr.tidyverse.org/reference/hoist.html) `

Hoist values out of list-columns

Character vectors[](https://tidyr.tidyverse.org/reference/index.html#character-vectors)

----------------------------------------------------------------------------------------

Multiple variables are sometimes pasted together into a single column, and these tools help you separate back out into individual columns.

`[separate_longer_delim()](https://tidyr.tidyverse.org/reference/separate_longer_delim.html) ` `[separate_longer_position()](https://tidyr.tidyverse.org/reference/separate_longer_delim.html) ` experimental

Split a string into rows

`[separate_wider_delim()](https://tidyr.tidyverse.org/reference/separate_wider_delim.html) ` `[separate_wider_position()](https://tidyr.tidyverse.org/reference/separate_wider_delim.html) ` `[separate_wider_regex()](https://tidyr.tidyverse.org/reference/separate_wider_delim.html) ` experimental

Split a string into columns

`[unite()](https://tidyr.tidyverse.org/reference/unite.html) `

Unite multiple columns into one by pasting strings together

Missing values[](https://tidyr.tidyverse.org/reference/index.html#missing-values)

----------------------------------------------------------------------------------

Tools for converting between implicit (absent rows) and explicit (`NA`) missing values, and for handling explicit `NA`s.

`[complete()](https://tidyr.tidyverse.org/reference/complete.html) `

Complete a data frame with missing combinations of data

`[drop_na()](https://tidyr.tidyverse.org/reference/drop_na.html) `

Drop rows containing missing values

`[expand()](https://tidyr.tidyverse.org/reference/expand.html) ` `[crossing()](https://tidyr.tidyverse.org/reference/expand.html) ` `[nesting()](https://tidyr.tidyverse.org/reference/expand.html) `

Expand data frame to include all possible combinations of values

`[expand_grid()](https://tidyr.tidyverse.org/reference/expand_grid.html) `

Create a tibble from all combinations of inputs

`[fill()](https://tidyr.tidyverse.org/reference/fill.html) `

Fill in missing values with previous or next value

`[full_seq()](https://tidyr.tidyverse.org/reference/full_seq.html) `

Create the full sequence of values in a vector

`[replace_na()](https://tidyr.tidyverse.org/reference/replace_na.html) `

Replace NAs with specified values

Miscellanea[](https://tidyr.tidyverse.org/reference/index.html#miscellanea)

----------------------------------------------------------------------------

`[chop()](https://tidyr.tidyverse.org/reference/chop.html) ` `[unchop()](https://tidyr.tidyverse.org/reference/chop.html) `

Chop and unchop

`[pack()](https://tidyr.tidyverse.org/reference/pack.html) ` `[unpack()](https://tidyr.tidyverse.org/reference/pack.html) `

Pack and unpack

`[uncount()](https://tidyr.tidyverse.org/reference/uncount.html) `

"Uncount" a data frame

`[nest()](https://tidyr.tidyverse.org/reference/nest.html) `

Nest rows into a list-column of data frames

Data[](https://tidyr.tidyverse.org/reference/index.html#data)

--------------------------------------------------------------

`[billboard](https://tidyr.tidyverse.org/reference/billboard.html) `

Song rankings for Billboard top 100 in the year 2000

`[cms_patient_experience](https://tidyr.tidyverse.org/reference/cms_patient_experience.html) ` `[cms_patient_care](https://tidyr.tidyverse.org/reference/cms_patient_experience.html) `

Data from the Centers for Medicare & Medicaid Services

`[construction](https://tidyr.tidyverse.org/reference/construction.html) `

Completed construction in the US in 2018

`[fish_encounters](https://tidyr.tidyverse.org/reference/fish_encounters.html) `

Fish encounters

`[household](https://tidyr.tidyverse.org/reference/household.html) `

Household data

`[relig_income](https://tidyr.tidyverse.org/reference/relig_income.html) `

Pew religion and income survey

`[smiths](https://tidyr.tidyverse.org/reference/smiths.html) `

Some data about the Smith family

`[table1](https://tidyr.tidyverse.org/reference/table1.html) ` `[table2](https://tidyr.tidyverse.org/reference/table1.html) ` `[table3](https://tidyr.tidyverse.org/reference/table1.html) ` `[table4a](https://tidyr.tidyverse.org/reference/table1.html) ` `[table4b](https://tidyr.tidyverse.org/reference/table1.html) ` `[table5](https://tidyr.tidyverse.org/reference/table1.html) `

Example tabular representations

`[us_rent_income](https://tidyr.tidyverse.org/reference/us_rent_income.html) `

US rent and income data

`[who](https://tidyr.tidyverse.org/reference/who.html) ` `[who2](https://tidyr.tidyverse.org/reference/who.html) ` `[population](https://tidyr.tidyverse.org/reference/who.html) `

World Health Organization TB data

`[world_bank_pop](https://tidyr.tidyverse.org/reference/world_bank_pop.html) `

Population data from the World Bank

Superseded[](https://tidyr.tidyverse.org/reference/index.html#superseded)

--------------------------------------------------------------------------

Superseded functions have been replaced by superior solutions, but due to their widespread use will not go away. However, they will not get any new features and will only receive critical bug fixes.

`[extract()](https://tidyr.tidyverse.org/reference/extract.html) ` superseded

Extract a character column into multiple columns using regular expression groups

`[separate()](https://tidyr.tidyverse.org/reference/separate.html) ` superseded

Separate a character column into multiple columns with a regular expression or numeric locations

`[separate_rows()](https://tidyr.tidyverse.org/reference/separate_rows.html) ` superseded

Separate a collapsed column into multiple rows

`[spread()](https://tidyr.tidyverse.org/reference/spread.html) ` superseded

Spread a key-value pair across multiple columns

`[gather()](https://tidyr.tidyverse.org/reference/gather.html) ` superseded

Gather columns into key-value pairs

`[nest_legacy()](https://tidyr.tidyverse.org/reference/nest_legacy.html) ` `[unnest_legacy()](https://tidyr.tidyverse.org/reference/nest_legacy.html) ` superseded

Legacy versions of `[nest()](https://tidyr.tidyverse.org/reference/nest.html) ` and `[unnest()](https://tidyr.tidyverse.org/reference/unnest.html) `