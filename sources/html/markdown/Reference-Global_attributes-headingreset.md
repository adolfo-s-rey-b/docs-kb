*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#mdn-search)
    

`headingreset` HTML global attribute
====================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/876)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#browser_compatibility)
 carefully before using this in production.

The **`headingreset`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 stops the [`headingoffset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset)
 values of ancestor elements from applying to the [heading elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 inside the element it is set on.

[Values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#values)

------------------------------------------------------------------------------------------------------------

This is a [boolean attribute](https://developer.mozilla.org/en-US/docs/Glossary/Boolean/HTML)
; it takes effect when it is present. A value for it is ignored, so `headingreset`, `headingreset=""`, and `headingreset="false"` all have the same effect.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#description)

----------------------------------------------------------------------------------------------------------------------

When a browser computes the [heading level](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#description)
 of a heading element, it walks up the ancestor chain and adds up the [`headingoffset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset)
 values it finds. The `headingreset` attribute stops that walk: offsets set on the element itself still count, but no ancestor above it contributes an offset.

Use this attribute for content that is not part of the structure of the surrounding document, such as a [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
, a popover, or markup inserted from another source. Their headings then take the level of their element name.

If the element carries both `headingoffset` and `headingreset`, its own offset applies and everything above it is discarded.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#examples)

----------------------------------------------------------------------------------------------------------------

### [Resetting heading levels in a dialog](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#resetting_heading_levels_in_a_dialog)

In this example, the `<section>` offsets its headings by `2`, so the heading directly inside it is at level 3. The `<dialog>` element has `headingreset`, so the section's offset never reaches the heading inside the dialog, which stays at level 1:

### [Using `headingreset` and `headingoffset` on the same element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#using_headingreset_and_headingoffset_on_the_same_element)

In this example, the outer offset of `3` never reaches the heading. Only the offset on the element with `headingreset` applies, so the heading is at level 2:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# heading-levels-&-offsets](https://html.spec.whatwg.org/multipage/sections.html#heading-levels-&-offsets) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`headingoffset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset)
     global attribute
*   [`<h1>`–`<h6>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
     elements
*   [`aria-level`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-level)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/headingreset/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/headingreset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fheadingreset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fheadingreset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fheadingreset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fheadingreset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff398f522d05bb8bfe739ac2417b00712b7888494%0A*+Document+last+modified%3A+2026-08-26T20%3A00%3A43.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")