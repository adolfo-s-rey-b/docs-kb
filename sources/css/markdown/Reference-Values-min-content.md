*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content#mdn-search)
    

`min-content` CSS keyword
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The `min-content` sizing keyword represents the [minimum intrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Intrinsic_Size#minimum_intrinsic_size)
 of an element. The keyword shrinks the element to the smallest possible size without causing avoidable overflow of its content. For text content, this keyword causes the content to wrap at every opportunity (such as spaces between words), and the element will be only as wide as the longest word.

The [`interpolate-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interpolate-size)
 property and [`calc-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc-size)
 function can be used to enable animations to and from `min-content`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content#syntax)

-----------------------------------------------------------------------------------------------

css

    /* Used as a length value */
    width: min-content;
    inline-size: min-content;
    height: min-content;
    block-size: min-content;
    
    /* Used in grid tracks */
    grid-template-columns: 200px 1fr min-content;
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content#examples)

---------------------------------------------------------------------------------------------------

### [Sizing boxes with min-content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content#sizing_boxes_with_min-content)

#### HTML

html

    <div class="item">Item</div>
    <div class="item">Item with more text in it.</div>
    

#### CSS

css

    .item {
      width: min-content;
      background-color: #8ca0ff;
      padding: 5px;
      margin-bottom: 1em;
    }
    

#### Result

### [Sizing grid columns with min-content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content#sizing_grid_columns_with_min-content)

#### HTML

html

    <div id="container">
      <div>Item</div>
      <div>Item with more text in it.</div>
      <div>Flexible item</div>
    </div>
    

#### CSS

css

    #container {
      display: grid;
      grid-template-columns: min-content min-content 1fr;
      grid-gap: 5px;
      box-sizing: border-box;
      height: 200px;
      width: 100%;
      background-color: #8cffa0;
      padding: 10px;
    }
    
    #container > div {
      background-color: #8ca0ff;
      padding: 5px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Box Sizing Module Level 3  <br>\# valdef-width-min-content](https://drafts.csswg.org/css-sizing-3/#valdef-width-min-content) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content#see_also)

---------------------------------------------------------------------------------------------------

*   Related sizing keywords: [`max-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max-content)
    , [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
    
*   [CSS box sizing](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min-content/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/min-content/index.md?plain=1 "Folder: en-us/web/css/reference/values/min-content (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fmin-content&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fmin-content%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fmin-content%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fmin-content%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Faaedffba9f47d6dce7967a4191963378026d9406%0A*+Document+last+modified%3A+2026-04-20T02%3A08%3A22.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")