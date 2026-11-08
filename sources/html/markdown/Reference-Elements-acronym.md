*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym#mdn-search)
    

`<acronym>` HTML acronym or abbreviation element
================================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<acronym>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element allows authors to clearly indicate a sequence of characters that compose an acronym or abbreviation for a word.

**Warning:** Don't use this element. Use the [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
 element instead.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym#attributes)

------------------------------------------------------------------------------------------------------

This element only has [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
, which are common to all elements.

[DOM Interface](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym#dom_interface)

------------------------------------------------------------------------------------------------------------

This element implements the [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)
 interface.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym#examples)

--------------------------------------------------------------------------------------------------

html

    <p>
      The <acronym title="World Wide Web">WWW</acronym> is only a component of the
      Internet.
    </p>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym#result)

[Default styling](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym#default_styling)

----------------------------------------------------------------------------------------------------------------

Though the purpose of this tag is purely for the convenience of the author, its default styling varies from one browser to another:

*   Opera, Firefox, Chrome, and some others add a dotted underline to the content of the element.
*   A few browsers not only add a dotted underline, but also put it in small caps; to avoid this styling, adding something like [`font-variant: none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
     in the CSS takes care of this case.

It is therefore recommended that web authors either explicitly style this element, or accept some cross-browser variation.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# acronym](https://html.spec.whatwg.org/multipage/obsolete.html#acronym) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym#see_also)

--------------------------------------------------------------------------------------------------

*   The [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
     HTML element

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/acronym/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/acronym/index.md?plain=1 "Folder: en-us/web/html/reference/elements/acronym (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Facronym&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Facronym%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Facronym%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Facronym%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")