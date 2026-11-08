*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Nesting_and_specificity#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Nesting_and_specificity#mdn-search)
    

CSS nesting and specificity
===========================

The [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
 of the `&` nesting selector is calculated using the largest specificity in the associated selector list. This is identical to how specificity is calculated when using the [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
 function.

[`&` nesting syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Nesting_and_specificity#nesting_syntax)

-----------------------------------------------------------------------------------------------------------------------------

[`:is()` syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Nesting_and_specificity#is_syntax)

--------------------------------------------------------------------------------------------------------------------

In this example, the id selector (`#a`) has a specificity of [`1-0-0`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity#selector_weight_categories)
, while the type selector (`b`) has a specificity of `0-0-1`. The [`&` nesting selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector)
 and `:is()` pseudo-class both take a specificity of `1-0-0`, even though the `#a` id selector is never used.

The `.foo` class selector has a specificity of `0-1-0`. This makes the total specificity `1-0-1` for `& i` and `0-1-1` for `.foo i`, meaning that `color: blue;` wins out.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Nesting_and_specificity#see_also)

-------------------------------------------------------------------------------------------------------------

*   [CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting)
     module
*   [`&` nesting selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector)
    
*   [Using CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Using)
    
*   [Nesting at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Nesting_and_specificity/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/nesting/nesting_and_specificity/index.md?plain=1 "Folder: en-us/web/css/guides/nesting/nesting_and_specificity (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FNesting%2FNesting_and_specificity&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fnesting%2Fnesting_and_specificity%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FNesting%2FNesting_and_specificity%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fnesting%2Fnesting_and_specificity%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")