*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading#mdn-search)
    

`:heading` CSS pseudo-class
===========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/384)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading#browser_compatibility)
 carefully before using this in production.

The **`:heading`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches all [heading elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 in a document.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading#syntax)

-----------------------------------------------------------------------------------------------

css

    :heading {
      /* ... */
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading#description)

---------------------------------------------------------------------------------------------------------

The `:heading` pseudo-class allows you to style all headings at once, rather than matching and styling them individually.

This pseudo-class matches only elements that by default are semantically recognized as headings (`<h1>` through `<h6>`). Elements with [`role="heading"`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/heading_role)
 are not matched; you can select those by using the `[role="heading"]` [attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
.

The `:heading` pseudo-class has the same [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity#how_is_specificity_calculated)
 as a class selector, that is, `0-1-0`. So `:heading` has a specificity of `0-1-0`, whereas `h1, h2, h3, h4, h5, h6` would have a specificity of `0-0-1` and `section:heading` would have a specificity of `0-1-1`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading#examples)

---------------------------------------------------------------------------------------------------

### [Styling all headings](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading#styling_all_headings)

In this example, we use the `:heading` pseudo-class to style multiple levels of headings.

#### HTML

The document contains headings at three different levels, along with [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 paragraph elements.

html

    <h1>Mastering CSS</h1>
    <h2>Chapter 1: Selectors</h2>
    <p>
      A CSS selector is the part of a CSS rule that describes what elements in a
      document the rule will match.
    </p>
    <h3>1.1 Pseudo-classes</h3>
    <p>
      CSS pseudo-classes enable selecting elements based on information that lies
      outside of the document tree.
    </p>
    

#### CSS

We set the heading elements to be italic and tomato red.

css

    :heading {
      color: tomato;
      font-style: italic;
    }
    

#### Results

The `:heading` pseudo-class applies the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 and [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
 to all the headings in the document, but not the paragraphs:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 5  <br>\# headings](https://drafts.csswg.org/selectors-5/#headings) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading#see_also)

---------------------------------------------------------------------------------------------------

*   [`:heading()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading_function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:heading/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_heading/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_heading (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aheading&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_heading%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aheading%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_heading%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")