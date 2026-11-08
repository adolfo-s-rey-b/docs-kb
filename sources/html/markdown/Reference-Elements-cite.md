*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#mdn-search)
    

`<cite>` HTML citation element
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<cite>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is used to mark up the title of a creative work. The reference may be in an abbreviated form according to context-appropriate conventions related to citation metadata.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#try_it)

-------------------------------------------------------------------------------------------

    <figure>
      <blockquote>
        <p>
          It was a bright cold day in April, and the clocks were striking thirteen.
        </p>
      </blockquote>
      <figcaption>
        First sentence in
        <cite
          ><a href="http://www.george-orwell.org/1984/0.html"
            >Nineteen Eighty-Four</a
          ></cite
        >
        by George Orwell (Part 1, Chapter 1).
      </figcaption>
    </figure>
    

    cite {
      /* Add your styles here */
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#attributes)

---------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#usage_notes)

-----------------------------------------------------------------------------------------------------

In the context of the `<cite>` element, a creative work could be, for example, one of the following:

*   A book
*   A research paper
*   An essay
*   A poem
*   A musical score
*   A song
*   A play or film script
*   A film
*   A television show
*   A game
*   A sculpture
*   A painting
*   A theatrical production
*   A play
*   An opera
*   A musical
*   An exhibition
*   A legal case report
*   A computer program
*   A website
*   A web page
*   A blog post or comment
*   A forum post or comment
*   A tweet
*   A Facebook post
*   A written or oral statement
*   And so forth.

To include a reference to the source of quoted material which is contained within a [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
 or [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
 element, use the [`cite`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote#cite)
 attribute on the element.

Typically, browsers style the contents of a `<cite>` element in italics by default. To avoid this, apply the CSS [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
 property to the `<cite>` element.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#examples)

-----------------------------------------------------------------------------------------------

html

    <p>More information can be found in <cite>[ISO-0000]</cite>.</p>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)<br> Up to Gecko 1.9.2 (Firefox 4) inclusive, Firefox implements the [`HTMLSpanElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSpanElement)<br> interface for this element. |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-cite-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-cite-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite#see_also)

-----------------------------------------------------------------------------------------------

*   The element [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
     for long quotations.
*   The element [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
     for inline quotations and the [`cite`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q#cite)
     attribute.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/cite/index.md?plain=1 "Folder: en-us/web/html/reference/elements/cite (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fcite&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fcite%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fcite%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fcite%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")