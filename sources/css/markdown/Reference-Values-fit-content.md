*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content#mdn-search)
    

`fit-content` CSS keyword
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The `fit-content` sizing keyword represents an element size that adapts to its content while staying within the limits of its container. The keyword ensures that the element is never smaller than its minimum intrinsic size ([`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
) or larger than its maximum intrinsic size ([`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
).

**Note:** This keyword is different from the [`fit-content()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content_function)
 function. The function is used for grid track sizing (for example in [`grid-template-columns`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-columns)
 and [`grid-auto-rows`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-auto-rows)
) and for laid-out box sizing for properties such as [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
, and [`max-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-height)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content#syntax)

-----------------------------------------------------------------------------------------------

css

    /* Used in sizing properties */
    width: fit-content;
    height: fit-content;
    inline-size: fit-content;
    block-size: fit-content;
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content#description)

---------------------------------------------------------------------------------------------------------

This keyword is used with sizing properties such as [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
, [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
, [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
, and [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
. When used on these properties, the calculated size refers to the element's [content box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#content-box)
.

When `fit-content` is set, the element grows or shrinks to fit its content, but stops expanding after the relevant dimension reaches the size limit of its container.

The `fit-content` size is calculated using the following formula:

min(max-content, max(min-content, stretch))

where, [`stretch`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width#stretch)
 matches the element's [margin box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#margin-box)
 to the width of its [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block#identifying_the_containing_block)
. The keyword is essentially equivalent to `fit-content(stretch)`.

You can enable animations to and from `fit-content` using the [`interpolate-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size)
 property and the [`calc-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
 function.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content#examples)

---------------------------------------------------------------------------------------------------

### [Sizing boxes with fit-content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content#sizing_boxes_with_fit-content)

#### HTML

html

    <div class="container">
      <div class="item">Item</div>
      <div class="item">Item with more text in it.</div>
      <div class="item">
        Item with more text in it, hopefully we have added enough text so the text
        will start to wrap.
      </div>
    </div>
    

#### CSS

css

    .container {
      border: 2px solid #cccccc;
      padding: 10px;
      width: 20em;
    }
    
    .item {
      width: fit-content;
      background-color: #8ca0ff;
      padding: 5px;
      margin-bottom: 1em;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 3  <br>\# valdef-width-fit-content](https://drafts.csswg.org/css-sizing/#valdef-width-fit-content) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content#see_also)

---------------------------------------------------------------------------------------------------

*   Related sizing keywords: [`min-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content)
    , [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
    
*   [CSS box sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/fit-content/index.md?plain=1 "Folder: en-us/web/css/reference/values/fit-content (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffit-content&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffit-content%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Ffit-content%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Ffit-content%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faaedffba9f47d6dce7967a4191963378026d9406%0A*+Document+last+modified%3A+2026-04-20T02%3A08%3A22.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")