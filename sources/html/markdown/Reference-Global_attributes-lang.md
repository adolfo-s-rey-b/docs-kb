*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang#mdn-search)
    

`lang` HTML global attribute
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`lang`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 helps define the language of an element: the language that non-editable elements are written in, or the language that the editable elements should be written in by the user. The attribute contains a single [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
.

**Note:** The language is in an unknown state if there's no indication of language anywhere. It is recommended to always specify an appropriate value for this attribute, especially due to [accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang#accessibility_concerns)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang#try_it)

----------------------------------------------------------------------------------------------------

[Values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang#values)

----------------------------------------------------------------------------------------------------

The attribute contains a single [BCP 47 language tag](https://developer.mozilla.org/en-US/docs/Glossary/BCP_47_language_tag)
. If the attribute value is the _empty string_ (`lang=""`), the language is set to _unknown_; if the language tag is not valid according to BCP47, it is set to _invalid_.

If the `xml:lang` attribute is also specified, the HTML spec requires the `lang` and `xml:lang` attributes' values to be equal case-insensitively. The `xml:lang` attribute takes priority.

For the CSS pseudo-class [`:lang`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang)
, two invalid language names are different if their names are different. So while `:lang(es)` matches both `lang="es-ES"` and `lang="es-419"`, `:lang(xyzzy)` would _not_ match `lang="xyzzy-Zorp!"`.

### [Inheritance](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang#inheritance)

If an element has no `lang` or `xml:lang` attribute, it inherits the language of its [parent element](https://developer.mozilla.org/en-US/docs/Web/API/Node/parentElement)
, or the [`host`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/host "host")
 if the parent node is a [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
. If no ancestor sets a language, the language can also be specified by [`<meta http-equiv="content-language">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#content-language)
 or the HTTP [`Content-Language`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Language)
 header. If no single content language can be determined from these cues, the default is the empty string (with _unknown_ as the content language).

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang#accessibility_concerns)

------------------------------------------------------------------------------------------------------------------------------------

WCAG Success Criterion 3.1.1 **requires** that a page language is specified in a way which may be 'programmatically determined' (i.e., via the **`lang`** attribute).

WCAG Success Criterion 3.1.2 requires that pages with **parts** in different languages have the languages of those parts specified too. Again, the **`lang`** attribute is the correct mechanism for this.

The purpose of these requirements is primarily to allow assistive technologies such as screen readers to invoke the correct pronunciation.

For example, the language menu on this site (MDN) includes a **`lang`** attribute for each entry:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-lang](https://html.spec.whatwg.org/multipage/dom.html#attr-lang) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang#see_also)

--------------------------------------------------------------------------------------------------------

*   All [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
    .
*   [`Content-Language` HTTP Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Language)
    
*   HTML [`translate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/translate)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/lang/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/lang (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Flang&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Flang%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Flang%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Flang%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F8ed465762d06fa17f7cc6adb3e2be9b57df03e9b%0A*+Document+last+modified%3A+2026-09-08T07%3A38%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")