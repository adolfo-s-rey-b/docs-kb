*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc#mdn-search)
    

`<rtc>` HTML ruby text container element
========================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<rtc>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element embraces semantic annotations of characters presented in a ruby of [`<rb>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb)
 elements used inside of [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
 element. [`<rb>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb)
 elements can have both pronunciation ([`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
) and semantic (`<rtc>`) annotations.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc#try_it)

------------------------------------------------------------------------------------------

    <ruby lang="zh-Hant">
      <rbc>
        <rb>馬</rb><rp>(</rp><rt>mǎ</rt><rp>)</rp>
        <rb>來</rb><rp>(</rp><rt>lái</rt><rp>)</rp>
        <rb>西</rb><rp>(</rp><rt>xī</rt><rp>)</rp>
        <rb>亞</rb><rp>(</rp><rt>yà</rt><rp>)</rp>
      </rbc>
      <rtc lang="en">
        <rp>(</rp><rt>Malaysia</rt><rp>)</rp>
      </rtc>
    </ruby>
    

    ruby {
      font-size: 2em;
      ruby-position: under;
    }
    
    rtc {
      ruby-position: over;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc#attributes)

--------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc#examples)

----------------------------------------------------------------------------------------------

html

    <div class="info">
      <ruby>
        <rbc>
          <rb>旧</rb><rt>jiù</rt> <rb>金</rb><rt>jīn</rt> <rb>山</rb><rt>shān</rt>
        </rbc>
        <rtc>San Francisco</rtc>
      </ruby>
    </div>
    

    .info {
      padding-top: 10px;
      font-size: 36px;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br> or [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)<br> elements. |
| Tag omission | The closing tag can be omitted if it is immediately followed by a [`<rb>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb)<br>, `<rtc>` or [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)<br> element opening tag or by its parent closing tag. |
| Permitted parents | A [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)<br> element. |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# rtc](https://html.spec.whatwg.org/multipage/obsolete.html#rtc) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc#see_also)

----------------------------------------------------------------------------------------------

*   [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
    
*   [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)
    
*   [`<rb>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rb)
    
*   [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
    
*   [CSS ruby layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Ruby_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rtc/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/rtc/index.md?plain=1 "Folder: en-us/web/html/reference/elements/rtc (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Frtc&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Frtc%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Frtc%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Frtc%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")