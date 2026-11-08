*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#mdn-search)
    

`<wbr>` HTML line break opportunity element
===========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<wbr>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a word break opportunity—a position within text where the browser may optionally break a line, though its line-breaking rules would not otherwise create a break at that location.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#try_it)

------------------------------------------------------------------------------------------

    <div id="example-paragraphs">
      <p>Fernstraßenbauprivatfinanzierungsgesetz</p>
      <p>Fernstraßen<wbr />bau<wbr />privat<wbr />finanzierungs<wbr />gesetz</p>
      <p>Fernstraßen&shy;bau&shy;privat&shy;finanzierungs&shy;gesetz</p>
    </div>
    

    #example-paragraphs {
      background-color: white;
      overflow: hidden;
      resize: horizontal;
      width: 9rem;
      border: 2px dashed #999999;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#attributes)

--------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#notes)

----------------------------------------------------------------------------------------

`<wbr>` behaves like the `U+200B ZERO-WIDTH SPACE` code point. In particular, it behaves like a Unicode bidi BN code point, meaning it has no effect on [bidi](https://developer.mozilla.org/en-US/docs/Glossary/BiDi)
\-ordering: `<div dir=rtl>123,<wbr>456</div>` displays, when not broken on two lines, `123,456` and not `456,123`.

For the same reason, the `<wbr>` element does not introduce a hyphen at the line break point. To make a hyphen appear only at the end of a line, use the soft hyphen character entity (`&shy;`) instead.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#examples)

----------------------------------------------------------------------------------------------

_[The Yahoo Style Guide](https://web.archive.org/web/20121014054923/http://styleguide.yahoo.com/ "External link (opens in new tab)")
_ recommends [breaking a URL _before_ punctuation](https://web.archive.org/web/20121105171040/http://styleguide.yahoo.com/editing/treat-abbreviations-capitalization-and-titles-consistently/website-names-and-addresses "External link (opens in new tab)")
, to avoid leaving a punctuation mark at the end of the line, which the reader might mistake for the end of the URL.

html

    <p>
      http://this<wbr />.is<wbr />.a<wbr />.really<wbr />.long<wbr />.example<wbr />.com/With<wbr />/deeper<wbr />/level<wbr />/pages<wbr />/deeper<wbr />/level<wbr />/pages<wbr />/deeper<wbr />/level<wbr />/pages<wbr />/deeper<wbr />/level<wbr />/pages<wbr />/deeper<wbr />/level<wbr />/pages
    </p>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Permitted content | Empty |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-wbr-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-wbr-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr#see_also)

----------------------------------------------------------------------------------------------

*   [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
    
*   [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
    
*   [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
    
*   The [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br)
     element

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 3, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/wbr/index.md?plain=1 "Folder: en-us/web/html/reference/elements/wbr (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fwbr&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fwbr%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fwbr%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fwbr%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb7de5fa065848c0d703b6763df7a15d1eb908c91%0A*+Document+last+modified%3A+2026-06-03T11%3A05%3A58.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")