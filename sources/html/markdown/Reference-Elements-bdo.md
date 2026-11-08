*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#mdn-search)
    

`<bdo>` HTML bidirectional text override element
================================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<bdo>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element overrides the current directionality of text, so that the text within is rendered in a different direction.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#try_it)

------------------------------------------------------------------------------------------

    <h1>Famous seaside songs</h1>
    
    <p>The English song "Oh I do like to be beside the seaside"</p>
    
    <p>
      Looks like this in Hebrew:
      <span dir="rtl">אה, אני אוהב להיות ליד חוף הים</span>
    </p>
    
    <p>
      In the computer's memory, this is stored as
      <bdo dir="ltr">אה, אני אוהב להיות ליד חוף הים</bdo>
    </p>
    

    html {
      font-family: sans-serif;
    }
    
    bdo {
      /* Add your styles here */
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#attributes)

--------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#dir)

The direction in which text should be rendered in this element's contents. Possible values are:

*   `ltr`: Indicates that the text should go in a left-to-right direction.
*   `rtl`: Indicates that the text should go in a right-to-left direction.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#usage_notes)

----------------------------------------------------------------------------------------------------

The text's characters are drawn from the starting point in the given direction; the individual characters' orientation is not affected (so characters don't get drawn backward, for example).

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#examples)

----------------------------------------------------------------------------------------------

html

    <!-- Switch text direction -->
    <p>This text will go left to right.</p>
    <p><bdo dir="rtl">This text will go right to left.</bdo></p>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)<br> Up to Gecko 1.9.2 (Firefox 4) inclusive, Firefox implements the `[HTMLSpanElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSpanElement) ` interface for this element. |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-bdo-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-bdo-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo#see_also)

----------------------------------------------------------------------------------------------

*   Related HTML element: [`<bdi>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdi)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/bdo/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/bdo/index.md?plain=1 "Folder: en-us/web/html/reference/elements/bdo (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbdo&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbdo%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbdo%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbdo%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F100cf25d92d3953f3c70ecaa2af637d5e42179d8%0A*+Document+last+modified%3A+2026-09-10T17%3A31%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")