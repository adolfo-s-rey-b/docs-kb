*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#mdn-search)
    

`:heading()` CSS pseudo-class
=============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/384)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#browser_compatibility)
 carefully before using this in production.

The **`:heading()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 function represents all [heading elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 whose levels match a comma-separated list of integers. This allows you to style elements at specific heading levels at once, rather than matching and styling them individually.

**Note:** The `:heading()` functional pseudo-class has the same [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity#how_is_specificity_calculated)
 as a class selector, that is, `0-1-0`. For example, `section:heading()` has a specificity of `0-1-1`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#syntax)

--------------------------------------------------------------------------------------------------------

css

    :heading( <integer># ) {
      /* ... */
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#parameters)

The `:heading()` pseudo-class function takes a comma-separated list of [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
s that represent the heading levels to be styled.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#usage_notes)

------------------------------------------------------------------------------------------------------------------

The `:heading()` functional pseudo-class matches only elements that are semantically recognized as headings. It does not match elements that use [`role="heading"`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/heading_role)
 or ['aria-level'](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-level)
 attributes.

The heading level used by `:heading()` may be different from an element's [type selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors)
 in cases where the browser computes a different exposed heading level. For example, `h1:heading(3)` will match any `<h1>` element that is exposed as a level 3 heading.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#examples)

------------------------------------------------------------------------------------------------------------

### [Selecting specific heading levels](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#selecting_specific_heading_levels)

In this example, a comma-separated list of values is used to target headings at odd-numbered levels (`<h1>` and `<h3>`) and even-numbered levels (`<h2>` and `<h4>`).

html

    <h1>Heading 1</h1>
    <h2>Heading 2</h2>
    <h3>Heading 3</h3>
    <h4>Heading 4</h4>
    

css

    :heading(1, 3) {
      color: tomato;
    }
    :heading(2, 4) {
      color: slateblue;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 5  <br>\# headings](https://drafts.csswg.org/selectors-5/#headings) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function#see_also)

------------------------------------------------------------------------------------------------------------

*   [`:heading`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_heading_function/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_heading_function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aheading_function&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_heading_function%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aheading_function%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_heading_function%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")