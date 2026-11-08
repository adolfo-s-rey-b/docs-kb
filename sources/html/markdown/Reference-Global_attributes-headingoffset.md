*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#mdn-search)
    

`headingoffset` HTML global attribute
=====================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/876)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#browser_compatibility)
 carefully before using this in production.

The **`headingoffset`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 increases the computed heading level of the [heading elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 inside the element it is set on, without changing the elements used to write them.

[Values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#values)

-------------------------------------------------------------------------------------------------------------

A valid non-negative integer between `0` and `8`, inclusive. A value that cannot be parsed as a non-negative integer is treated as an offset of `0`.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#description)

-----------------------------------------------------------------------------------------------------------------------

Each heading element has a **computed heading level**, which is the level assistive technologies expose to users. Without `headingoffset`, that level is the number in the element's name: `1` for [`<h1>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
, `2` for `<h2>`, and so on.

The `headingoffset` attribute adds to that number. To find the offset for a heading, the browser starts at the heading element itself, walks up through its ancestors – crossing shadow boundaries into the shadow host – and adds up every `headingoffset` value it finds. The offsets accumulate: an `<h1>` inside an element with `headingoffset="1"` that is itself inside an element with `headingoffset="2"` has a computed heading level of 4.

Because the walk starts at the heading element, an offset on the heading itself also counts: `<h1 headingoffset="2">` has a computed heading level of 3.

The walk stops at the first element that has the [`headingreset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset)
 attribute, after adding that element's own `headingoffset`.

The computed heading level never exceeds `9`, even in cases where offsets add up to more. Because HTML has no heading element above `<h6>`, heading levels of 7, 8, and 9 can be produced only by the `headingoffset` attribute or by the [`aria-level`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-level)
 attribute.

This attribute affects only the computed heading level. It does not change the following:

*   The element's name, so CSS selectors such as `h1` still match, and the default styling of the heading is unchanged.
*   The element's [ARIA role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/heading_role)
    , which stays `heading`.
*   An explicit `aria-level` attribute on the heading, which takes precedence over the computed heading level.

Because the offset comes from the heading and its ancestors, a reusable component can always use the same heading markup, such as an `<h1>` for its title. You can then use the same markup at any depth of a page without editing its headings. This also avoids the accessibility problem caused by picking a heading element for its font size.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#accessibility)

---------------------------------------------------------------------------------------------------------------------------

Screen reader users navigate by headings and rely on heading levels to understand how a page is structured. Use `headingoffset` to make those levels match the visual structure of the page, and check the result with a screen reader or the browser's accessibility inspector.

In browsers that do not support this attribute, headings keep the level of their element name, so the markup must still make sense without the offset.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#examples)

-----------------------------------------------------------------------------------------------------------------

### [Offsetting headings in a component](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#offsetting_headings_in_a_component)

In this example, the markup uses the same component structure twice – an `<article>` with an `<h1>` title. The second one is nested in a `<section>` that offsets its headings by one level.

The computed heading levels are:

*   `Insect guide`: level 1
*   `Beetles`: level 1
*   `Appendix`: level 2
*   `Beetles, revisited`: level 2

### [Accumulating offsets](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#accumulating_offsets)

Offsets from nested elements are added together, so this `<h2>` has a computed heading level of 5:

### [Stopping the offset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#stopping_the_offset)

An element with the [`headingreset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset)
 attribute stops the offsets of its ancestors from applying to its descendants. This is useful for content that is not part of the surrounding document structure, such as a dialog:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# heading-levels-&-offsets](https://html.spec.whatwg.org/multipage/sections.html#heading-levels-&-offsets) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`headingreset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset)
     global attribute
*   [`<h1>`–`<h6>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
     elements
*   [`aria-level`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-level)
     attribute
*   [ARIA: heading role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/heading_role)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/headingoffset/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/headingoffset (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fheadingoffset&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fheadingoffset%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fheadingoffset%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fheadingoffset%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff398f522d05bb8bfe739ac2417b00712b7888494%0A*+Document+last+modified%3A+2026-08-26T20%3A00%3A43.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")