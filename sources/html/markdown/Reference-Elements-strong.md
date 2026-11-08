*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#mdn-search)
    

`<strong>` HTML strong importance element
=========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<strong>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element indicates that its contents have strong importance, seriousness, or urgency. Browsers typically render the contents in bold type.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#try_it)

---------------------------------------------------------------------------------------------

    <p>
      ... the most important rule, the rule you can never forget, no matter how much
      he cries, no matter how much he begs:
      <strong>never feed him after midnight</strong>.
    </p>
    

    p {
      font-size: 1rem;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#attributes)

-----------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#usage_notes)

-------------------------------------------------------------------------------------------------------

The `<strong>` element is for content that is of "strong importance," including things of great seriousness or urgency (such as warnings). This could be a sentence that is of great importance to the whole page, or you could merely try to point out that some words are of greater importance compared to nearby content.

Typically this element is rendered by default using a bold font weight. However, it should _not_ be used to apply bold styling; use the CSS [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 property for that purpose. Use the [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
 element to draw attention to certain text without indicating a higher level of importance. Use the [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
 element to mark text that has stress emphasis.

Another accepted use for `<strong>` is to denote the labels of paragraphs which represent notes or warnings within the text of a page.

### [<b> vs. <strong>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#b_vs._strong)

It is often confusing to new developers why there are so many ways to express the same thing on a rendered website. [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
 and `<strong>` are perhaps one of the most common sources of confusion, causing developers to ask "Should I use `<b>` or `<strong>`? Don't they both do the same thing?"

Not exactly. The `<strong>` element is for content that is of greater importance, while the `<b>` element is used to draw attention to text without indicating that it's more important.

It may help to realize that both are valid and semantic elements in HTML and that it's a coincidence that they both have the same default styling (boldface) in most browsers (although some older browsers actually underline `<strong>`). Each element is meant to be used in certain types of scenarios, and if you want to bold text for decoration, you should instead actually use the CSS [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 property.

The intended meaning or purpose of the enclosed text should be what determines which element you use. Communicating meaning is what semantics are all about.

### [<em> vs. <strong>](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#em_vs._strong)

Adding to the confusion is the fact that while HTML 4 defined `<strong>` as indicating a stronger emphasis, HTML 5 defines `<strong>` as representing "strong importance for its contents." This is an important distinction to make.

While `<em>` is used to change the meaning of a sentence as spoken emphasis does ("I _love_ carrots" vs. "I love _carrots_"), `<strong>` is used to give portions of a sentence added importance (e.g., "**Warning!** This is **very dangerous.**") Both `<strong>` and `<em>` can be nested to increase the relative degree of importance or stress emphasis, respectively.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#examples)

-------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#basic_example)

html

    <p>
      Before proceeding, <strong>make sure you put on your safety goggles</strong>.
    </p>
    

#### Result

### [Labeling warnings](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#labeling_warnings)

html

    <p>
      <strong>Important:</strong> Before proceeding, make sure you add plenty of
      butter.
    </p>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None; must have both a start tag and an end tag. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, or any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | `[strong](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/structural_roles#structural_roles_with_html_equivalents) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-strong-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-strong-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong#see_also)

-------------------------------------------------------------------------------------------------

*   The [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
     element
*   The [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
     element
*   The [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
     property

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/strong/index.md?plain=1 "Folder: en-us/web/html/reference/elements/strong (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fstrong&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fstrong%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fstrong%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fstrong%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")