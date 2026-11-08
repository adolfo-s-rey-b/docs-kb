*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#mdn-search)
    

`<abbr>` HTML abbreviation element
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<abbr>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents an abbreviation or acronym.

When including an abbreviation or acronym, provide a full expansion of the term in plain text on first use, along with the `<abbr>` to mark up the abbreviation. This informs the user what the abbreviation or acronym means.

The optional [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 attribute can provide an expansion for the abbreviation or acronym when a full expansion is not present. This provides a hint to user agents on how to announce/display the content while informing all users what the abbreviation means. If present, `title` must contain this full description and nothing else.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#try_it)

-------------------------------------------------------------------------------------------

    <p>
      You can use <abbr>CSS</abbr> (Cascading Style Sheets) to style your
      <abbr>HTML</abbr> (HyperText Markup Language). Using style sheets, you can
      keep your <abbr>CSS</abbr> presentation layer and <abbr>HTML</abbr> content
      layer separate. This is called "separation of concerns."
    </p>
    

    abbr {
      font-style: italic;
      color: chocolate;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#attributes)

---------------------------------------------------------------------------------------------------

This element only supports the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
. The [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 attribute has a specific semantic meaning when used with the `<abbr>` element; it _must_ contain a full human-readable description or expansion of the abbreviation. This text is often presented by browsers as a tooltip when the mouse cursor is hovered over the element.

Each `<abbr>` element you use is independent of all others; providing a `title` for one does not automatically attach the same expansion text to others with the same content text.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#usage_notes)

-----------------------------------------------------------------------------------------------------

### [Typical use cases](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#typical_use_cases)

It's certainly not required that all abbreviations be marked up using `<abbr>`. There are, though, a few cases where it's helpful to do so:

*   When an abbreviation is used and you want to provide an expansion or definition outside the flow of the document's content, use `<abbr>` with an appropriate [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
    .
*   To define an abbreviation which may be unfamiliar to the reader, present the term using `<abbr>` and inline text providing the definition. Include a `title` attribute only when the inline expansion or definition is not available.
*   When an abbreviation's presence in the text needs to be semantically noted, the `<abbr>` element is useful. This can be used, in turn, for styling or scripting purposes.
*   You can use `<abbr>` in concert with [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn)
     to establish definitions for terms which are abbreviations or acronyms. See the example [Defining an abbreviation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#defining_an_abbreviation)
     below.

### [Grammar considerations](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#grammar_considerations)

In languages with [grammatical number](https://en.wikipedia.org/wiki/Grammatical_number "External link (opens in new tab)")
 (that is, languages where the number of items affects the grammar of a sentence), use the same grammatical number in your `title` attribute as inside your `<abbr>` element. This is especially important in languages with more than two numbers, such as Arabic, but is also relevant in English.

[Default styling](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#default_styling)

-------------------------------------------------------------------------------------------------------------

The purpose of this element is purely for the convenience of the author and all browsers display it inline ([`display: inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
) by default, though its default styling varies from one browser to another:

Some browsers add a dotted underline to the content of the element. Others add a dotted underline while converting the contents to small caps. Others may not style it differently than a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 element. To control this styling, use [`text-decoration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration)
 and [`font-variant`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#accessibility)

---------------------------------------------------------------------------------------------------------

Spelling out the acronym or abbreviation in full the first time it is used on a page is beneficial for helping people understand it, especially if the content is technical or industry jargon.

Only include a `title` if expanding the abbreviation or acronym in the text is not possible. Having a difference between the announced word or phrase and what is displayed on the screen, especially if it's technical jargon the reader may not be familiar with, can be jarring.

html

    <p>
      JavaScript Object Notation (<abbr>JSON</abbr>) is a lightweight
      data-interchange format.
    </p>
    

This is especially helpful for people who are unfamiliar with the terminology or concepts discussed in the content, people who are new to the language, and people with cognitive concerns.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#examples)

-----------------------------------------------------------------------------------------------

### [Marking up an abbreviation semantically](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#marking_up_an_abbreviation_semantically)

To mark up an abbreviation without providing an expansion or description, use `<abbr>` without any attributes, as seen in this example.

#### HTML

html

    <p>Using <abbr>HTML</abbr> is fun and easy!</p>
    

#### Result

### [Styling abbreviations](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#styling_abbreviations)

You can use CSS to set a custom style to be used for abbreviations, as seen in this basic example.

#### HTML

html

    <p>Using <abbr>CSS</abbr>, you can style your abbreviations!</p>
    

#### CSS

css

    abbr {
      font-variant: all-small-caps;
    }
    

#### Result

### [Providing an expansion](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#providing_an_expansion)

Adding a [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 attribute lets you provide an expansion or definition for the abbreviation or acronym.

#### HTML

html

    <p>Ashok's joke made me <abbr title="Laugh Out Loud">LOL</abbr> big time.</p>
    

#### Result

### [Defining an abbreviation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#defining_an_abbreviation)

You can use `<abbr>` in tandem with [`<dfn>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn)
 to more formally define an abbreviation, as shown here.

#### HTML

html

    <p>
      <dfn id="html"><abbr title="HyperText Markup Language">HTML</abbr> </dfn> is a
      markup language used to create the semantics and structure of a web page.
    </p>
    
    <p>
      A <dfn id="spec">Specification</dfn> (<abbr>spec</abbr>) is a document that
      outlines in detail how a technology or API is intended to function and how it
      is accessed.
    </p>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content) |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content) |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | Any |
| DOM Interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-abbr-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-abbr-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr#see_also)

-----------------------------------------------------------------------------------------------

*   [Using the `<abbr>` element](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Advanced_text_features#abbreviations)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/abbr/index.md?plain=1 "Folder: en-us/web/html/reference/elements/abbr (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fabbr&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fabbr%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fabbr%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fabbr%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")