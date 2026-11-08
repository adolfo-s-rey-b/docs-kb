*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#mdn-search)
    

`<ruby>` HTML ruby annotation element
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<ruby>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents small annotations that are rendered above, below, or next to base text, usually used for showing the pronunciation of East Asian characters. It can also be used for annotating other kinds of text, but this usage is less common.

The term _ruby_ originated as [a unit of measurement used by typesetters](https://en.wikipedia.org/wiki/Agate_(typography) "External link (opens in new tab)")
, representing the smallest size that text can be printed on newsprint while remaining legible.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#try_it)

-------------------------------------------------------------------------------------------

    <ruby> 明日 <rp>(</rp><rt>Ashita</rt><rp>)</rp> </ruby>
    

    ruby {
      font-size: 2em;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#attributes)

---------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#examples)

-----------------------------------------------------------------------------------------------

### [Example 1: Character](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#example_1_character)

html

    <ruby>
      漢 <rp>(</rp><rt>Kan</rt><rp>)</rp> 字 <rp>(</rp><rt>ji</rt><rp>)</rp>
    </ruby>
    

#### Result

### [Example 2: Word](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#example_2_word)

html

    <ruby> 明日 <rp>(</rp><rt>Ashita</rt><rp>)</rp> </ruby>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | One or more groups, each consisting of two parts:<br><br>1.  The base text, which is either:<br>    *   [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>        , but with no `<ruby>` elements and with no `<ruby>` element descendants, or<br>    *   A single `<ruby>` element that itself has no `<ruby>` element descendants.<br>2.  The annotations for the base text, which is either:<br>    *   One or more [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)<br>         elements, or<br>    *   An [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)<br>         element followed by one or more [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)<br>         elements, each of which is itself followed by an [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)<br>         element (that is, `rp, rt, rp, rt, ..., rp`). |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-ruby-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-ruby-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby#see_also)

-----------------------------------------------------------------------------------------------

*   [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
    
*   [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)
    
*   [`ruby-overhang`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang)
    
*   [`text-transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform)
    : full-size-kana
*   [CSS ruby layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Ruby_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/ruby/index.md?plain=1 "Folder: en-us/web/html/reference/elements/ruby (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fruby&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fruby%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fruby%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fruby%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")