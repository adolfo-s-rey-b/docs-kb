*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck#mdn-search)
    

`spellcheck` HTML global attribute
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`spellcheck`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is an [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute that defines whether the element may be checked for spelling errors.

**Note:** This attribute is merely a hint for the browser: browsers are not required to check for spelling errors. Typically non-editable elements are not checked for spelling errors, even if the `spellcheck` attribute is set to `true` and the browser supports spellchecking.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck#try_it)

----------------------------------------------------------------------------------------------------------

It may have the following values:

*   empty string or `true`, which indicates that the element should be, if possible, checked for spelling errors;
*   `false`, which indicates that the element should not be checked for spelling errors.

If this attribute is not set, its default value is element-type and browser-defined. This default value may also be _inherited_, which means that the element content will be checked for spelling errors only if its nearest ancestor has a _spellcheck_ state of `true`.

[Security and privacy concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck#security_and_privacy_concerns)

--------------------------------------------------------------------------------------------------------------------------------------------------------

Using spellchecking can have consequences for users' security and privacy. The specification does not regulate _how_ spellchecking is done and the content of the element may be sent to a third party for spellchecking results (see [enhanced spellchecking and "spell-jacking"](https://www.comparitech.com/blog/information-security/what-is-spell-jacking/ "External link (opens in new tab)")
).

You should consider setting `spellcheck` to `false` for elements that can contain sensitive information.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-spellcheck](https://html.spec.whatwg.org/multipage/interaction.html#attr-spellcheck) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck#see_also)

--------------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    .
*   [`autocorrect`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocorrect)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/spellcheck/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/spellcheck (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fspellcheck&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fspellcheck%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fspellcheck%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fspellcheck%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8d9cda4e9080e9c324a521f40c7e0704ef94ce07%0A*+Document+last+modified%3A+2026-07-03T08%3A23%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")