*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#mdn-search)
    

`<sup>` HTML superscript element
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<sup>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element specifies inline text which is to be displayed as superscript for solely typographical reasons. Superscripts are usually rendered with a raised baseline using smaller text.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#try_it)

------------------------------------------------------------------------------------------

    <p>
      The <em>Pythagorean theorem</em> is often expressed as the following equation:
    </p>
    
    <p>
      <var>a<sup>2</sup></var> + <var>b<sup>2</sup></var> = <var>c<sup>2</sup></var>
    </p>
    

    p {
      font:
        1rem "Fira Sans",
        sans-serif;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#attributes)

--------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#usage_notes)

----------------------------------------------------------------------------------------------------

The `<sup>` element should only be used for typographical reasons—that is, to change the position of the text to comply with typographical conventions or standards, rather than solely for presentation or appearance purposes.

For example, to style the [wordmark](https://en.wikipedia.org/wiki/Wordmark "External link (opens in new tab)")
 of a business or product which uses a raised baseline should be done using CSS (most likely [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
) rather than `<sup>`. This would be done using, for example, `vertical-align: super` or, to shift the baseline up 50%, `vertical-align: 50%`.

Appropriate use cases for `<sup>` include (but aren't necessarily limited to):

*   Displaying exponents, such as "x3". It may be worth considering the use of [MathML](https://developer.mozilla.org/en-US/docs/Web/MathML)
     for these, especially in more complex cases. See [Exponents](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#exponents)
     under [Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#examples)
     below.
*   Displaying [superior lettering](https://en.wikipedia.org/wiki/Superior_letter "External link (opens in new tab)")
    , which is used in some languages when rendering certain abbreviations. For example, in French, the word "mademoiselle" can be abbreviated "Mlle"; this is an acceptable use case. See [Superior lettering](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#superior_lettering)
     for examples.
*   Representing ordinal numbers, such as "4th" instead of "fourth." See [Ordinal numbers](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#ordinal_numbers)
     for examples.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#examples)

----------------------------------------------------------------------------------------------

### [Exponents](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#exponents)

Exponents, or powers of a number, are among the most common uses of superscripted text. For example:

html

    <p>
      One of the most common equations in all of physics is <var>E</var>=<var>m</var
      ><var>c</var><sup>2</sup>.
    </p>
    

#### Result

### [Superior lettering](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#superior_lettering)

Superior lettering is not technically the same thing as superscript. However, it is common to use `<sup>` to present superior lettering in HTML. Among the most common uses of superior lettering is the presentation of certain abbreviations in French:

html

    <p>Robert a présenté son rapport à M<sup>lle</sup> Bernard.</p>
    

#### Result

### [Ordinal numbers](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#ordinal_numbers)

Ordinal numbers, such as "fourth" in English or "quinto" in Spanish may be abbreviated using numerals and language-specific text rendered in superscript:

html

    <p>
      The ordinal number "fifth" can be abbreviated in various languages as follows:
    </p>
    <ul>
      <li>English: 5<sup>th</sup></li>
      <li>French: 5<sup>ème</sup></li>
    </ul>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[superscript](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/structural_roles#structural_roles_with_html_equivalents) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-sub-and-sup-elements](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-sub-and-sup-elements) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup#see_also)

----------------------------------------------------------------------------------------------

*   The [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub)
     HTML element that produces subscripts. Note that you cannot use `sub` and `sup` at the same time: you need to use [MathML](https://developer.mozilla.org/en-US/docs/Web/MathML)
     to produce both a superscript and a subscript next to the chemical symbol of an element, representing its atomic number and its nuclear number.
*   The [`<msub>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/msub)
    , [`<msup>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/msup)
    , and [`<msubsup>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/msubsup)
     MathML elements.
*   The CSS [`vertical-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/vertical-align)
     property.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/sup/index.md?plain=1 "Folder: en-us/web/html/reference/elements/sup (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsup&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsup%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsup%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsup%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")