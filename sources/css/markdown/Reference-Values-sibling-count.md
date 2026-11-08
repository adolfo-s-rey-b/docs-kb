*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count#mdn-search)
    

`sibling-count()` CSS function
==============================

Baseline 2026

Newly available

Since August 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`sibling-count()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 returns an integer representing the total number of sibling DOM elements (direct children of the parent) of the element on which it is used, including itself.

**Note:** The [`counter()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/counter)
 function provides a similar result but it returns a `<string>` (which is more suitable for [generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
, while `sibling-count()` returns an `<integer>` (which can be used for calculations).

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count#syntax)

-------------------------------------------------------------------------------------------------

css

    sibling-count()
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count#parameters)

The `sibling-count()` function doesn't accept parameters.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count#return_value)

An integer; the total number of sibling DOM elements including the element itself.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count#examples)

-----------------------------------------------------------------------------------------------------

### [Dynamic column count](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count#dynamic_column_count)

This example demonstrates setting the width of each item in a list based on the number of items, enabling placing each child in its own column.

#### HTML

We include a [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 container and several [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements children.

html

    <ul>
      <li>One</li>
      <li>Two</li>
      <li>Three</li>
      <li>Four</li>
      <li>Five</li>
    </ul>
    

#### CSS

We divide the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 of each list item by the number of direct children the list contains. We also set every odd element to have a [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 to better demonstrate the resulting effect.

css

    ul {
      list-style-type: none;
      padding: 0;
      margin: 0;
      text-align: center;
      display: flex;
    }
    
    li {
      width: calc(100% / sibling-count());
    }
    
    li:nth-of-type(odd) {
      background-color: rgb(0 0 0 / 0.05);
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 5  <br>\# funcdef-sibling-count](https://drafts.csswg.org/css-values-5/#funcdef-sibling-count) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count#see_also)

-----------------------------------------------------------------------------------------------------

*   [`sibling-index()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-index)
    
*   [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 18, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sibling-count/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/sibling-count/index.md?plain=1 "Folder: en-us/web/css/reference/values/sibling-count (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsibling-count&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsibling-count%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fsibling-count%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fsibling-count%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb760560abe30bd69ca968dac38528102f423b5ea%0A*+Document+last+modified%3A+2026-04-18T06%3A09%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")