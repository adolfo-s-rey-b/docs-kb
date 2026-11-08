*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial#mdn-search)
    

`initial` CSS keyword
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`initial`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 keyword applies the [initial (or default) value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
 of a property to an element. It can be applied to any CSS property, including the CSS shorthand property [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
. With `all` set to `initial`, all CSS properties can be restored to their respective initial values in one go instead of restoring each one separately.

On [inherited properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#inherited_properties)
, the initial value may be unexpected. You should consider using the [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
, [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
, [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
, [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
, or [`revert-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule)
 keywords instead.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial#examples)

-----------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial#basic_usage)

In this example, we use the `initial` keyword to reset an element's [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 and [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 property values.

#### HTML

#### CSS

We set `color` and `font-size` on the `<p>` element, then set those properties to `initial` on the [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
 element to reset them.

#### Result

With the `initial` keyword in this example, the `color` and `font-size` values on the `em` element are restored to the initial values for [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color#formal_definition)
 and [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#formal_definition)
, respectively.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Cascading and Inheritance Level 4  <br>\# initial](https://drafts.csswg.org/css-cascade/#initial) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial#see_also)

-----------------------------------------------------------------------------------------------

*   [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
    , [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
    , [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
    , [`revert-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule)
    , and [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
     keywords
*   [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
    
*   [Inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/initial/index.md?plain=1 "Folder: en-us/web/css/reference/values/initial (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Finitial&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Finitial%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Finitial%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Finitial%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0aa8517faf9d7d15c745ac94db7014d3a2d2085f%0A*+Document+last+modified%3A+2026-04-20T12%3A06%3A36.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")