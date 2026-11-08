*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#mdn-search)
    

`<sub>` HTML subscript element
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<sub>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element specifies inline text which should be displayed as subscript for solely typographical reasons. Subscripts are typically rendered with a lowered baseline using smaller text.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#try_it)

------------------------------------------------------------------------------------------

    <p>
      Almost every developer's favorite molecule is
      C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>, also known as
      "caffeine."
    </p>
    

    p {
      font:
        1rem "Fira Sans",
        sans-serif;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#attributes)

--------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#usage_notes)

----------------------------------------------------------------------------------------------------

The `<sub>` element should be used only for typographical reasons—that is, to change the position of the text to comply with typographical conventions or standards, rather than solely for presentation or appearance purposes.

For example, using `<sub>` to style the name of a company which uses altered baselines in their [wordmark](https://en.wikipedia.org/wiki/Wordmark "External link (opens in new tab)")
 would not be appropriate; instead, CSS should be used. For example, you could use the [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
 property with a declaration like `vertical-align: sub` or, to more precisely control the baseline shift, `vertical-align: -25%`.

Appropriate use cases for `<sub>` include (but aren't necessarily limited to):

*   Marking up footnote numbers. See [Footnote numbers](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#footnote_numbers)
     for an example.
*   Marking up the subscript in mathematical variable numbers (although you may also consider using a [MathML](https://developer.mozilla.org/en-US/docs/Web/MathML)
     formula for this). See [Variable subscripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#variable_subscripts)
    .
*   Denoting the number of atoms of a given element within a chemical formula (such as every developer's best friend, C8H10N4O2, otherwise known as "caffeine"). See [Chemical formulas](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#chemical_formulas)
    .

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#examples)

----------------------------------------------------------------------------------------------

### [Footnote numbers](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#footnote_numbers)

Traditional footnotes are denoted using numbers which are rendered in subscript. This is a common use case for `<sub>`:

html

    <p>
      According to the computations by Nakamura, Johnson, and Mason<sub>1</sub> this
      will result in the complete annihilation of both particles.
    </p>
    

#### Result

### [Variable subscripts](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#variable_subscripts)

In mathematics, families of variables related to the same concept (such as distances along the same axis) are represented using the same variable name with a subscript following. For example:

html

    <p>
      The horizontal coordinates' positions along the X-axis are represented as
      <var>x<sub>1</sub></var> … <var>x<sub>n</sub></var>.
    </p>
    

#### Result

### [Chemical formulas](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#chemical_formulas)

When writing a chemical formula, such as H2O, the number of atoms of a given element within the described molecule is represented using a subscripted number; in the case of water, the subscripted "2" indicates that there are two atoms of hydrogen in the molecule.

Another example:

html

    <p>
      Almost every developer's favorite molecule is
      C<sub>8</sub>H<sub>10</sub>N<sub>4</sub>O<sub>2</sub>, which is commonly known
      as "caffeine."
    </p>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[subscript](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/structural_roles#structural_roles_with_html_equivalents) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-sub-and-sup-elements](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-sub-and-sup-elements) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub#see_also)

----------------------------------------------------------------------------------------------

*   The [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup)
     HTML element that produces superscript. Note that you cannot use `sup` and `sub` both at the same time: you need to use [MathML](https://developer.mozilla.org/en-US/docs/Web/MathML)
     to produce both a superscript directly above a subscript next to the chemical symbol of an element, representing its atomic number and its nuclear number.
*   The [`<msub>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/msub)
    , [`<msup>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/msup)
    , and [`<msubsup>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/msubsup)
     MathML elements.
*   The CSS [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
     property.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/sub/index.md?plain=1 "Folder: en-us/web/html/reference/elements/sub (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsub&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsub%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsub%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsub%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")