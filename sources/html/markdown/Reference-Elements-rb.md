*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#mdn-search)
    

`<rb>` HTML ruby base element
=============================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<rb>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is used to delimit the base text component of a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
 annotation, i.e., the text that is being annotated. One `<rb>` element should wrap each separate atomic segment of the base text.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#attributes)

-------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#usage_notes)

---------------------------------------------------------------------------------------------------

*   Ruby annotations are for showing pronunciation of East Asian characters, like using Japanese furigana or Taiwanese bopomofo characters. The `<rb>` element is used to separate out each segment of the ruby base text.
*   Even though `<rb>` is not a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)
    , it is common to just include the opening tag of each element in the source code, so that the ruby markup is less complex and easier to read. The browser can then fill in the full element in the rendered version.
*   You need to include one [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
     element for each base segment/`<rb>` element that you want to annotate.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#examples)

---------------------------------------------------------------------------------------------

### [Using rb](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#using_rb)

In this example, we provide an annotation for the original character equivalent of "Kanji":

html

    <ruby>
      <rb>漢</rb><rb>字 </rb><rp>(</rp><rt>kan</rt><rt>ji</rt><rp>)</rp>
    </ruby>
    

Note how we've included two `<rb>` elements, to delimit the two separate parts of the ruby base text. The annotation on the other hand is delimited by two [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
 elements.

#### Result

### [Separate annotations](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#separate_annotations)

Note that we could also write this example with the two base text parts annotated completely separately. In this case we don't need to include `<rb>` elements:

html

    <ruby>
      漢 <rp>(</rp><rt>Kan</rt><rp>)</rp> 字 <rp>(</rp><rt>ji</rt><rp>)</rp>
    </ruby>
    

#### Result

See the article about the [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
 element for further examples.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#technical_summary)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | As a child of a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)<br> element. |
| Tag omission | The end tag can be omitted if the element is immediately followed by an [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)<br>, [`<rtc>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc)<br>, or [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)<br> element or another `<rb>` element, or if there is no more content in the parent element. |
| Permitted parents | A [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)<br> element. |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# rb](https://html.spec.whatwg.org/multipage/obsolete.html#rb) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb#see_also)

---------------------------------------------------------------------------------------------

*   [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
    
*   [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
    
*   [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)
    
*   [`<rtc>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc)
    
*   [CSS ruby layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Ruby_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/rb/index.md?plain=1 "Folder: en-us/web/html/reference/elements/rb (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Frb&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Frb%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Frb%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Frb%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")