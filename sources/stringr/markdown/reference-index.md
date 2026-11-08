[Skip to content](https://stringr.tidyverse.org/reference/index.html#container)

![](https://stringr.tidyverse.org/logo.png)

Package index
=============

Pattern matching[](https://stringr.tidyverse.org/reference/index.html#pattern-matching)

----------------------------------------------------------------------------------------

### String[](https://stringr.tidyverse.org/reference/index.html#string)

`[str_count()](https://stringr.tidyverse.org/reference/str_count.html) `

Count number of matches

`[str_detect()](https://stringr.tidyverse.org/reference/str_detect.html) `

Detect the presence/absence of a match

`[str_escape()](https://stringr.tidyverse.org/reference/str_escape.html) `

Escape regular expression metacharacters

`[str_extract()](https://stringr.tidyverse.org/reference/str_extract.html) ` `[str_extract_all()](https://stringr.tidyverse.org/reference/str_extract.html) `

Extract the complete match

`[str_locate()](https://stringr.tidyverse.org/reference/str_locate.html) ` `[str_locate_all()](https://stringr.tidyverse.org/reference/str_locate.html) `

Find location of match

`[str_match()](https://stringr.tidyverse.org/reference/str_match.html) ` `[str_match_all()](https://stringr.tidyverse.org/reference/str_match.html) `

Extract components (capturing groups) from a match

`[str_replace()](https://stringr.tidyverse.org/reference/str_replace.html) ` `[str_replace_all()](https://stringr.tidyverse.org/reference/str_replace.html) `

Replace matches with new text

`[str_remove()](https://stringr.tidyverse.org/reference/str_remove.html) ` `[str_remove_all()](https://stringr.tidyverse.org/reference/str_remove.html) `

Remove matched patterns

`[str_split()](https://stringr.tidyverse.org/reference/str_split.html) ` `[str_split_1()](https://stringr.tidyverse.org/reference/str_split.html) ` `[str_split_fixed()](https://stringr.tidyverse.org/reference/str_split.html) ` `[str_split_i()](https://stringr.tidyverse.org/reference/str_split.html) `

Split up a string into pieces

`[str_starts()](https://stringr.tidyverse.org/reference/str_starts.html) ` `[str_ends()](https://stringr.tidyverse.org/reference/str_starts.html) `

Detect the presence/absence of a match at the start/end

`[fixed()](https://stringr.tidyverse.org/reference/modifiers.html) ` `[coll()](https://stringr.tidyverse.org/reference/modifiers.html) ` `[regex()](https://stringr.tidyverse.org/reference/modifiers.html) ` `[boundary()](https://stringr.tidyverse.org/reference/modifiers.html) `

Control matching behaviour with modifier functions

### Vector[](https://stringr.tidyverse.org/reference/index.html#vector)

Unlike other pattern matching functions, these functions operate on the original character vector, not the individual matches.

`[str_subset()](https://stringr.tidyverse.org/reference/str_subset.html) `

Find matching elements

`[str_which()](https://stringr.tidyverse.org/reference/str_which.html) `

Find matching indices

Combining strings[](https://stringr.tidyverse.org/reference/index.html#combining-strings)

------------------------------------------------------------------------------------------

`[str_c()](https://stringr.tidyverse.org/reference/str_c.html) `

Join multiple strings into one string

`[str_flatten()](https://stringr.tidyverse.org/reference/str_flatten.html) ` `[str_flatten_comma()](https://stringr.tidyverse.org/reference/str_flatten.html) `

Flatten a string

`[str_glue()](https://stringr.tidyverse.org/reference/str_glue.html) ` `[str_glue_data()](https://stringr.tidyverse.org/reference/str_glue.html) `

Interpolation with glue

Character based[](https://stringr.tidyverse.org/reference/index.html#character-based)

--------------------------------------------------------------------------------------

`[str_dup()](https://stringr.tidyverse.org/reference/str_dup.html) `

Duplicate a string

`[str_length()](https://stringr.tidyverse.org/reference/str_length.html) ` `[str_width()](https://stringr.tidyverse.org/reference/str_length.html) `

Compute the length/width

`[str_pad()](https://stringr.tidyverse.org/reference/str_pad.html) `

Pad a string to minimum width

`[str_sub()](https://stringr.tidyverse.org/reference/str_sub.html) ` ``[`str_sub<-`()](https://stringr.tidyverse.org/reference/str_sub.html) `` `[str_sub_all()](https://stringr.tidyverse.org/reference/str_sub.html) `

Get and set substrings using their positions

`[str_trim()](https://stringr.tidyverse.org/reference/str_trim.html) ` `[str_squish()](https://stringr.tidyverse.org/reference/str_trim.html) `

Remove whitespace

`[str_trunc()](https://stringr.tidyverse.org/reference/str_trunc.html) `

Truncate a string to maximum width

`[str_wrap()](https://stringr.tidyverse.org/reference/str_wrap.html) `

Wrap words into nicely formatted paragraphs

Locale aware[](https://stringr.tidyverse.org/reference/index.html#locale-aware)

--------------------------------------------------------------------------------

`[str_order()](https://stringr.tidyverse.org/reference/str_order.html) ` `[str_rank()](https://stringr.tidyverse.org/reference/str_order.html) ` `[str_sort()](https://stringr.tidyverse.org/reference/str_order.html) `

Order, rank, or sort a character vector

`[str_equal()](https://stringr.tidyverse.org/reference/str_equal.html) `

Determine if two strings are equivalent

`[str_to_upper()](https://stringr.tidyverse.org/reference/case.html) ` `[str_to_lower()](https://stringr.tidyverse.org/reference/case.html) ` `[str_to_title()](https://stringr.tidyverse.org/reference/case.html) ` `[str_to_sentence()](https://stringr.tidyverse.org/reference/case.html) `

Convert string to upper case, lower case, title case, or sentence case

`[str_unique()](https://stringr.tidyverse.org/reference/str_unique.html) `

Remove duplicated strings

Other helpers[](https://stringr.tidyverse.org/reference/index.html#other-helpers)

----------------------------------------------------------------------------------

`[invert_match()](https://stringr.tidyverse.org/reference/invert_match.html) `

Switch location of matches to location of non-matches

`[str_conv()](https://stringr.tidyverse.org/reference/str_conv.html) `

Specify the encoding of a string

`[str_like()](https://stringr.tidyverse.org/reference/str_like.html) ` `[str_ilike()](https://stringr.tidyverse.org/reference/str_like.html) `

Detect a pattern in the same way as `SQL`'s `LIKE` and `ILIKE` operators

`[str_replace_na()](https://stringr.tidyverse.org/reference/str_replace_na.html) `

Turn NA into "NA"

`[str_to_camel()](https://stringr.tidyverse.org/reference/str_to_camel.html) ` `[str_to_snake()](https://stringr.tidyverse.org/reference/str_to_camel.html) ` `[str_to_kebab()](https://stringr.tidyverse.org/reference/str_to_camel.html) `

Convert between different types of programming case

`[str_view()](https://stringr.tidyverse.org/reference/str_view.html) `

View strings and matches

`[word()](https://stringr.tidyverse.org/reference/word.html) `

Extract words from a sentence

Bundled data[](https://stringr.tidyverse.org/reference/index.html#bundled-data)

--------------------------------------------------------------------------------

`[sentences](https://stringr.tidyverse.org/reference/stringr-data.html) ` `[fruit](https://stringr.tidyverse.org/reference/stringr-data.html) ` `[words](https://stringr.tidyverse.org/reference/stringr-data.html) `

Sample character vectors for practicing string manipulations