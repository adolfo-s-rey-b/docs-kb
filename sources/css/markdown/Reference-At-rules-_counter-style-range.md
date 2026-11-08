*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#mdn-search)
    

`range` CSS at-rule descriptor
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`range`** descriptor lets the author specify one or more ranges of counter values for which the style is applied when defining custom counter styles with the [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
 at-rule. When the `range` descriptor is included, the defined counter will only be used for values in the set ranges. If the counter value is outside the specified range, the fallback style will be used to construct the representation of that marker.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    range: auto;
    
    /* Range values */
    range: 2 5;
    range: infinite 10;
    range: 6 infinite;
    range: infinite infinite;
    
    /* Multiple range values */
    range:
      2 5,
      8 10;
    range:
      infinite 6,
      10 infinite;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#values)

The value is a comma-separated list of ranges each including a lower and upper limit or the keyword `auto`.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#auto)

The entire set of numbers representable by the counter [`system`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system)
. Those range values depends on the counter system:

*   For `cyclic`, `numeric`, and `fixed` systems, the range is negative `infinity` to positive `infinity`.
*   For `alphabetic` and `symbolic` systems, the range is `1` to positive `infinity`.
*   For `additive` systems, the range is `0` to `positive` infinity.
*   When using `extend` to extend a system, the range is whatever `auto` would produce for the system being extended, including extensions of complex predefined styles, such as some Japanese, Korean, Chinese, and Ethiopian counter styles.

[`[ [ <integer> | infinite ]{2} ]#`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#integer_infinite_2)

Each range within the comma separated list of ranges includes two values, each being either an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 or the keyword `infinite`. If `infinite` is used as the first value in a range, it represents negative infinity; if it is used as the second value, it represents positive infinity. The first value of each range is the lower bound for the range and the second value is the upper bound, inclusive. If the lower bound of any range in the list is higher than the upper bound, the entire `range` descriptor is invalid and will be ignored.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#description)

--------------------------------------------------------------------------------------------------------------------

The value of the `range` descriptor can be either `auto` or a comma separated list of lower and upper bound ranges specified using negative or positive integers or the keyword `infinite`.

### [Understanding `auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#understanding_auto)

When the value is set to `auto`, the range is the default range for the counter system. If the `system` is `cyclic`, `numeric`, or `fixed`, the range will be from negative infinity to positive infinity. If the `system` is `alphabetic` or `symbolic`, the range will be from `1` to positive `infinity`. For `system: additive`, `auto` results in the range `0` to positive `infinity`.

When extending a counter, if `range` is set to `auto`, the range value will be the range of the `system` of the counter that is being extended, not the `range` value, if any, of that counter. For example, if counter "B" has the `system: extends A` set, with counter being an `alphabetic` counter, setting `range: auto` on "B" sets the range of "B" from `1` to `infinity`. This is the range of the `alphabetic` system, not necessarily the range set in the "A" counter style definition. With `range: auto` set on "B", the `range` is set to the default range of the `alphabetic` system, not the `range` value set in counter A's descriptor list.

### [`infinite` explained](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#infinite_explained)

When range is specified as integers (versus `auto`), the value `infinite` can be used to denote infinity. If _infinite_ is specified as the first value in a range, then it is interpreted as negative infinity. If used as the upper bound, the second value in the range pair, it is taken as positive infinity.

### [List of ranges](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#list_of_ranges)

The value of `range` is either `auto`, discussed above, or a comma separated list of one or more ranges. The range of the counter style is the union of all the ranges defined in the list.

Each range in the list of ranges takes two values. Those values are either an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 or the keyword `infinite`. The first value is the _lower bound_, inclusive. The second value is the _upper bound_, inclusive. For two integer values, the lower value must come first. If the lower bound of any range in the list is higher than the upper bound, the entire `range` descriptor is invalid and will be ignored. The `infinite` keyword will not invalidate the range, because the position of `infinite` determines its value; either negative or positive infinity based on whether it's the lower bound or upper bound, respectively.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

range =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <integer> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 infinite [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto                                
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#examples)

--------------------------------------------------------------------------------------------------------------

### [Setting counter style over a range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#setting_counter_style_over_a_range)

#### HTML

html

    <ul class="list">
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
      <li>Five</li>
      <li>Six</li>
      <li>Seven</li>
      <li>Eight</li>
      <li>Nine</li>
      <li>Ten</li>
    </ul>
    

#### CSS

css

    @counter-style range-multi-example {
      system: cyclic;
      symbols: "\25A0" "\25A1";
      range:
        2 4,
        7 9;
    }
    
    .list {
      list-style: range-multi-example;
    }
    

#### Result

The first range is the list of ranges includes 2, 3, and 4. The second includes 7, 8, and 9. The range is the union of these two ranges, or 2, 3, 4, 7, 8, and 9.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Counter Styles Level 3  <br>\# counter-style-range](https://drafts.csswg.org/css-counter-styles/#counter-style-range) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range#see_also)

--------------------------------------------------------------------------------------------------------------

*   Other [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
     descriptors: [`system`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system)
    , [`symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols)
    , [`additive-symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/additive-symbols)
    , [`negative`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/negative)
    , [`prefix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/prefix)
    , [`suffix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/suffix)
    , [`pad`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad)
    , [`speak-as`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as)
    , and [`fallback`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/fallback)
    
*   [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
    , [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
    , [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
    
*   [`symbols()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)
    : the functional notation for creating anonymous counter styles.
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@counter-style/range/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@counter-style/range (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40counter-style%2Frange&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40counter-style%2Frange%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40counter-style%2Frange%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40counter-style%2Frange%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")