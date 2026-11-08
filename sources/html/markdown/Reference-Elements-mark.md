*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#mdn-search)
    

`<mark>` HTML mark text element
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<mark>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents text which is **marked** or **highlighted** for reference or notation purposes due to the marked passage's relevance in the enclosing context.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#try_it)

-------------------------------------------------------------------------------------------

    <p>Search results for "salamander":</p>
    
    <hr />
    
    <p>
      Several species of <mark>salamander</mark> inhabit the temperate rainforest of
      the Pacific Northwest.
    </p>
    
    <p>
      Most <mark>salamander</mark>s are nocturnal, and hunt for insects, worms, and
      other small creatures.
    </p>
    

    mark {
      /* Add your styles here */
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#attributes)

---------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#usage_notes)

-----------------------------------------------------------------------------------------------------

Typical use cases for `<mark>` include:

*   When used in a quotation ([`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
    ) or block quote ([`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)
    ), it generally indicates text which is of special interest but is not marked in the original source material, or material which needs special scrutiny even though the original author didn't think it was of particular importance. Think of this like using a highlighter pen in a book to mark passages that you find of interest.
*   Otherwise, `<mark>` indicates a portion of the document's content which is likely to be relevant to the user's current activity. This might be used, for example, to indicate the words that matched a search operation.
*   Don't use `<mark>` for syntax highlighting purposes; instead, use the [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
     element with appropriate CSS applied to it.

**Note:** Don't confuse `<mark>` with the [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
 element; `<mark>` is used to denote content which has a degree of _relevance_, while `<strong>` indicates spans of text of _importance_.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#examples)

-----------------------------------------------------------------------------------------------

### [Marking text of interest](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#marking_text_of_interest)

In this first example, a `<mark>` element is used to mark some text within a quote which is of particular interest to the user.

html

    <blockquote>
      It is a period of civil war. Rebel spaceships, striking from a hidden base,
      have won their first victory against the evil Galactic Empire. During the
      battle, <mark>Rebel spies managed to steal secret plans</mark> to the Empire's
      ultimate weapon, the DEATH STAR, an armored space station with enough power to
      destroy an entire planet.
    </blockquote>
    

#### Result

### [Identifying context-sensitive passages](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#identifying_context-sensitive_passages)

This example demonstrates using `<mark>` to mark search results within a passage.

html

    <p>
      It is a dark time for the Rebellion. Although the Death Star has been
      destroyed, <mark class="match">Imperial</mark> troops have driven the Rebel
      forces from their hidden base and pursued them across the galaxy.
    </p>
    
    <p>
      Evading the dreaded <mark class="match">Imperial</mark> Starfleet, a group of
      freedom fighters led by Luke Skywalker has established a new secret base on
      the remote ice world of Hoth.
    </p>
    

To help distinguish the use of `<mark>` for search results from other potential usage, this example applies the custom class `"match"` to each match.

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-mark-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-mark-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/mark/index.md?plain=1 "Folder: en-us/web/html/reference/elements/mark (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmark&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmark%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmark%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmark%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F32eceacf42b6bff41d9605298eba143cb7e199a1%0A*+Document+last+modified%3A+2026-10-17T20%3A27%3A33.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")