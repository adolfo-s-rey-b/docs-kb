*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#mdn-search)
    

`<i>` HTML idiomatic text element
=================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<i>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a range of text that is set off from the normal text for some reason, such as idiomatic text, technical terms, taxonomical designations, among others. Historically, these have been presented using italicized type, which is the original source of the `<i>` naming of this element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#try_it)

----------------------------------------------------------------------------------------

    <p>I looked at it and thought <i>This can't be real!</i></p>
    
    <p>
      <i>Musa</i> is one of two or three genera in the family <i>Musaceae</i>; it
      includes bananas and plantains.
    </p>
    
    <p>
      The term <i>bandwidth</i> describes the measure of how much information can
      pass through a data connection in a given amount of time.
    </p>
    

    i {
      /* Add your styles here */
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#attributes)

------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#usage_notes)

--------------------------------------------------------------------------------------------------

*   Use the `<i>` element for text that is set off from the normal prose for readability reasons. This would be a range of text with different semantic meaning than the surrounding text. Among the use cases for the `<i>` element are spans of text representing a different quality or mode of text, such as:
    
    *   Alternative voice or mood
    *   Taxonomic designations (such as the genus and species "_Homo sapiens_")
    *   Idiomatic terms from another language (such as "_et cetera_"); these should include the [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
         attribute to identify the language
    *   Technical terms
    *   Transliterations
    *   Thoughts (such as "She wondered, _What is this writer talking about, anyway?_")
    *   Ship or vessel names in Western writing systems (such as "They searched the docks for the _Empress of the Galaxy_, the ship to which they were assigned.")
*   In earlier versions of the HTML specification, the `<i>` element was merely a presentational element used to display text in italics, much like the `<b>` element was used to display text in bold letters. This is no longer true, as these tags now define semantics rather than typographic appearance. A browser will typically still display the contents of the `<i>` element in italic type, but is, by definition, no longer required to do so. To display text in italic type, authors should use the CSS [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
     property.
    
*   Be sure the text in question is not actually more appropriately marked up with another element.
    
    *   Use [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
         to indicate stress emphasis.
    *   Use [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
         to indicate importance, seriousness, or urgency.
    *   Use [`<mark>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/mark)
         to indicate relevance.
    *   Use [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
         to mark up the name of a work, such as a book, play, or song.
    *   Use [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn)
         to mark up the defining instance of a term.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#examples)

--------------------------------------------------------------------------------------------

This example demonstrates using the `<i>` element to mark text that is in another language.

html

    <p>
      The Latin phrase <i lang="la">Veni, vidi, vici</i> is often mentioned in
      music, art, and literature.
    </p>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#technical_summary)

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-i-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-i-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i#see_also)

--------------------------------------------------------------------------------------------

*   [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
    
*   Other italicized elements: [`<var>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var)
    , [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn)
    , [`<cite>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/cite)
    , [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/i/index.md?plain=1 "Folder: en-us/web/html/reference/elements/i (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fi&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fi%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fi%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fi%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")