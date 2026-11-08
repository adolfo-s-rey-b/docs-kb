[Skip to content](https://dplyr.tidyverse.org/reference/dplyr-locale.html#container)

![](https://dplyr.tidyverse.org/logo.png)

Locale used by `arrange()`
==========================

Source: [`R/locale.R`](https://github.com/tidyverse/dplyr/blob/main/R/locale.R)

`dplyr-locale.Rd`

This page documents details about the locale used by `[arrange()](https://dplyr.tidyverse.org/reference/arrange.html) ` when ordering character vectors.

### Default locale[](https://dplyr.tidyverse.org/reference/dplyr-locale.html#default-locale)

The default locale used by `[arrange()](https://dplyr.tidyverse.org/reference/arrange.html) ` is the C locale. This is used when `.locale = NULL` unless the deprecated `dplyr.legacy_locale` global option is set to `TRUE`. You can also force the C locale to be used unconditionally with `.locale = "C"`.

The C locale is not exactly the same as English locales, such as `"en"`. The main difference is that the C locale groups the English alphabet by _case_, while most English locales group the alphabet by _letter_. For example, `c("a", "b", "C", "B", "c")` will sort as `c("B", "C", "a", "b", "c")` in the C locale, with all uppercase letters coming before lowercase letters, but will sort as `c("a", "b", "B", "c", "C")` in an English locale. This often makes little practical difference during data analysis, because both return identical results when case is consistent between observations.

### Reproducibility[](https://dplyr.tidyverse.org/reference/dplyr-locale.html#reproducibility)

The C locale has the benefit of being completely reproducible across all supported R versions and operating systems with no extra effort.

If you set `.locale` to an option from `[stringi::stri_locale_list()](https://rdrr.io/pkg/stringi/man/stri_locale_list.html) `, then stringi must be installed by anyone who wants to run your code. If you utilize this in a package, then stringi should be placed in `Imports`.

### Legacy behavior[](https://dplyr.tidyverse.org/reference/dplyr-locale.html#legacy-behavior)

[![[Deprecated]](https://dplyr.tidyverse.org/reference/figures/lifecycle-deprecated.svg)](https://lifecycle.r-lib.org/articles/stages.html#deprecated)

Prior to dplyr 1.1.0, character columns were ordered in the system locale. Setting the global option `dplyr.legacy_locale` to `TRUE` retains this legacy behavior, but this has been deprecated. Update existing code to explicitly call `arrange(.locale = )` instead. Run `Sys.getlocale("LC_COLLATE")` to determine your system locale, and compare that against the list in `[stringi::stri_locale_list()](https://rdrr.io/pkg/stringi/man/stri_locale_list.html) ` to find an appropriate value for `.locale`, i.e. for American English, `"en_US"`.

Setting `.locale` directly will override any usage of `dplyr.legacy_locale`.

Examples[](https://dplyr.tidyverse.org/reference/dplyr-locale.html#ref-examples)

---------------------------------------------------------------------------------

    df <- tibble(x = c("a", "b", "C", "B", "c"))
    df
    #> # A tibble: 5 × 1
    #>   x    
    #>   <chr>
    #> 1 a    
    #> 2 b    
    #> 3 C    
    #> 4 B    
    #> 5 c    
    
    # Default locale is C, which groups the English alphabet by case, placing
    # uppercase letters before lowercase letters.
    arrange(df, x)
    #> # A tibble: 5 × 1
    #>   x    
    #>   <chr>
    #> 1 B    
    #> 2 C    
    #> 3 a    
    #> 4 b    
    #> 5 c    
    
    # The American English locale groups the alphabet by letter.
    # Explicitly override `.locale` with `"en"` for this ordering.
    arrange(df, x, .locale = "en")
    #> # A tibble: 5 × 1
    #>   x    
    #>   <chr>
    #> 1 a    
    #> 2 b    
    #> 3 B    
    #> 4 c    
    #> 5 C    
    
    # This Danish letter is expected to sort after `z`
    df <- tibble(x = c("o", "p", "\u00F8", "z"))
    df
    #> # A tibble: 4 × 1
    #>   x    
    #>   <chr>
    #> 1 o    
    #> 2 p    
    #> 3 ø    
    #> 4 z    
    
    # The American English locale sorts it right after `o`
    arrange(df, x, .locale = "en")
    #> # A tibble: 4 × 1
    #>   x    
    #>   <chr>
    #> 1 o    
    #> 2 ø    
    #> 3 p    
    #> 4 z    
    
    # Using `"da"` for Danish ordering gives the expected result
    arrange(df, x, .locale = "da")
    #> # A tibble: 4 × 1
    #>   x    
    #>   <chr>
    #> 1 o    
    #> 2 p    
    #> 3 z    
    #> 4 ø