[Skip to content](https://tidyr.tidyverse.org/reference/who.html#container)

![](https://tidyr.tidyverse.org/logo.png)

World Health Organization TB data
=================================

Source: [`R/data.R`](https://github.com/tidyverse/tidyr/blob/main/R/data.R)

`who.Rd`

A subset of data from the World Health Organization Global Tuberculosis Report, and accompanying global populations. `who` uses the original codes from the World Health Organization. The column names for columns 5 through 60 are made by combining `new_` with:

*   the method of diagnosis (`rel` = relapse, `sn` = negative pulmonary smear, `sp` = positive pulmonary smear, `ep` = extrapulmonary),
    
*   gender (`f` = female, `m` = male), and
    
*   age group (`014` = 0-14 yrs of age, `1524` = 15-24, `2534` = 25-34, `3544` = 35-44 years of age, `4554` = 45-54, `5564` = 55-64, `65` = 65 years or older).
    

`who2` is a lightly modified version that makes teaching the basics easier by tweaking the variables to be slightly more consistent and dropping `iso2` and `iso3`. `newrel` is replaced by `new_rel`, and a `_` is added after the gender.

Usage[](https://tidyr.tidyverse.org/reference/who.html#ref-usage)

------------------------------------------------------------------

    who
    
    who2
    
    population

Format[](https://tidyr.tidyverse.org/reference/who.html#format)

----------------------------------------------------------------

### `who`[](https://tidyr.tidyverse.org/reference/who.html#who)

A data frame with 7,240 rows and 60 columns:

country

Country name

iso2, iso3

2 & 3 letter ISO country codes

year

Year

new\_sp\_m014 - new\_rel\_f65

Counts of new TB cases recorded by group. Column names encode three variables that describe the group.

### `who2`[](https://tidyr.tidyverse.org/reference/who.html#who-)

A data frame with 7,240 rows and 58 columns.

### `population`[](https://tidyr.tidyverse.org/reference/who.html#population)

A data frame with 4,060 rows and three columns:

country

Country name

year

Year

population

Population

Source[](https://tidyr.tidyverse.org/reference/who.html#source)

----------------------------------------------------------------

[https://www.who.int/teams/global-tuberculosis-programme/data](https://www.who.int/teams/global-tuberculosis-programme/data)