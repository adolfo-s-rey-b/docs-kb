*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#mdn-search)
    

`<ratio>` CSS type
==================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<ratio>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 describes the proportional relationship between two values. It mostly represents the aspect ratio, which relates width to height. For example, the `<ratio>` is used as a value for the `aspect-ratio` media feature in [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 media queries, the `aspect-ratio` size feature in [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
 container queries, and as a value for the CSS [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
 property.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#syntax)

-----------------------------------------------------------------------------------------

The `<ratio>` data type is a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 followed by a forward slash ('/', Unicode `U+002F SOLIDUS`) and a second [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
. Both numbers must be positive. Spaces before and after the slash are optional. The first number represents the width, while the second represents the height. In addition a single [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 as a value is allowable.

Two ratios are compared using the quotients' numeric values. For example, 16/16 is less than 16/9 because it resolves to 1 while the second resolves to 1.7. This means a tall screen's aspect ratio is smaller than a wide screen's, and portrait images have smaller aspect ratios than landscape images.

### [Common aspect ratios](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#common_aspect_ratios)

| Ratio |     | Usage |
| --- | --- | --- |
| `4/3` or `1.33333` | ![A rectangle that is three units tall and four units wide](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio/ratio4_3.png) | Traditional TV format in the twentieth century. |
| `16/9` or `1.7777778` | ![A rectangle that is nine units tall and sixteen units wide](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio/ratio16_9.png) | Modern "widescreen" TV format. |
| `185/100` or `1.85` | ![A rectangle that is 1 unit tall and 1.85 units wide](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio/ratio1_1.85.png) | The most common movie format since the 1960s. |
| `239/100` or `2.39` | ![A rectangle that is 1 unit tall and 2.39 units wide](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio/ratio1_2.39.png) | "Widescreen," anamorphic movie format. |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#formal_syntax)

-------------------------------------------------------------------------------------------------------

<ratio> =   
  [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#examples)

---------------------------------------------------------------------------------------------

### [Use in a media query](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#use_in_a_media_query)

css

    @media screen and (aspect-ratio >= 16/9) {
      /* … */
    }
    

### [Use in a @container size query](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#use_in_a_container_size_query)

css

    @container (aspect-ratio > 1) and (width < 20em) {
      /* … */
    }
    

### [Use as a CSS property value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#use_as_a_css_property_value)

css

    .square {
      aspect-ratio: 1 / 1;
    }
    .circle {
      aspect-ratio: 1;
      border-radius: 50%;
    }
    .portrait {
      aspect-ratio: 5 / 7;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# ratio-value](https://drafts.csswg.org/css-values-4/#ratio-value) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio#see_also)

---------------------------------------------------------------------------------------------

*   [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/aspect-ratio)
     media descriptor
*   [Understanding aspect ratios](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)
    
*   [CSS container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
     guide
*   [Using container size and style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries)
     guide
*   [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
     module
*   [CSS containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment)
     module
*   [CSS box sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing)
     module
*   [CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/ratio/index.md?plain=1 "Folder: en-us/web/css/reference/values/ratio (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fratio&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fratio%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fratio%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fratio%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc88e03530319b73272fd4f9a9f6ebe878f026004%0A*+Document+last+modified%3A+2026-04-20T01%3A40%3A53.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")