*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#mdn-search)
    

`<dfn>` HTML definition element
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<dfn>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element indicates a term to be defined. The `<dfn>` element should be used in a complete definition statement, where the full definition of the term can be one of the following:

*   The ancestor paragraph (a block of text, sometimes marked by a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
     element)
*   The [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)
    /[`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
     pairing
*   The nearest [section](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#sectioning_content)
     ancestor of the `<dfn>` element,

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#try_it)

------------------------------------------------------------------------------------------

    <p>
      A <dfn id="def-validator">validator</dfn> is a program that checks for syntax
      errors in code or documents.
    </p>
    

    dfn {
      /* Add your styles here */
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#attributes)

--------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

The [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
 attribute has special meaning, as noted below.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#usage_notes)

----------------------------------------------------------------------------------------------------

There are some not-entirely-obvious aspects to using the `<dfn>` element. We examine those here.

### [Specifying the term being defined](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#specifying_the_term_being_defined)

The term being defined is identified following these rules:

1.  If the `<dfn>` element has a [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/title)
     attribute, the value of the `title` attribute is considered to be the term being defined. The element must still have text within it, but that text may be an abbreviation (perhaps using [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
    ) or another form of the term.
2.  If the `<dfn>` contains a single child element and does not have any text content of its own, and the child element is an [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
     element with a `title` attribute itself, then the exact value of the `<abbr>` element's `title` is the term being defined.
3.  Otherwise, the text content of the `<dfn>` element is the term being defined. This is shown [in the first example below](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#basic_identification_of_a_term)
    .

**Note:** If the `<dfn>` element has a `title` attribute, it _must_ contain the term being defined and no other text.

### [Links to `<dfn>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#links_to_dfn_elements)

If you include an [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attribute on the `<dfn>` element, you can then link to it using [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 elements. Such links should be uses of the term, with the intent being that the reader can quickly navigate to the term's definition if they're not already aware of it, by clicking on the term's link.

This is shown in the example under [Links to definitions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#links_to_definitions)
 below.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#examples)

----------------------------------------------------------------------------------------------

Let's take a look at some examples of various usage scenarios.

### [Basic identification of a term](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#basic_identification_of_a_term)

This example uses a plain `<dfn>` element to identify the location of a term within the definition.

#### HTML

html

    <p>
      The <strong>HTML Definition element (<dfn>&lt;dfn&gt;</dfn>)</strong> is used
      to indicate the term being defined within the context of a definition phrase
      or sentence.
    </p>
    

Since the `<dfn>` element has no `title`, the text contents of the `<dfn>` element itself are used as the term being defined.

#### Result

### [Links to definitions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#links_to_definitions)

To add links to the definitions, you create the link the same way you always do, with the [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 element.

#### HTML

html

    <p>
      The
      <strong>HTML Definition element (<dfn id="definition-dfn">&lt;dfn&gt;</dfn>)</strong>
      is used to indicate the term being defined within the context of a definition
      phrase or sentence.
    </p>
    
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. Graece donan, Latine
      voluptatem vocant. Confecta res esset. Duo Reges: constructio interrete.
      Scrupulum, inquam, abeunti;
    </p>
    
    <p>
      Because of all of that, we decided to use the
      <code><a href="#definition-dfn">&lt;dfn&gt;</a></code> element for this
      project.
    </p>
    

Here we see the definition — now with an [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attribute, `"definition-dfn"`, which can be used as the target of a link. Later on, a link is created using `<a>` with the [`href`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#href)
 attribute set to `"#definition-dfn"` to set up the link back to the definition.

#### Result

### [Using abbreviations and definitions together](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#using_abbreviations_and_definitions_together)

In some cases, you may wish to use an abbreviation for a term when defining it. This can be done by using the `<dfn>` and [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
 elements in tandem, like this:

#### HTML

html

    <p>
      The <dfn><abbr title="Hubble Space Telescope">HST</abbr></dfn> is among the
      most productive scientific instruments ever constructed. It has been in orbit
      for over 20 years, scanning the sky and returning data and photographs of
      unprecedented quality and detail.
    </p>
    
    <p>
      Indeed, the <abbr title="Hubble Space Telescope">HST</abbr> has arguably done
      more to advance science than any device ever built.
    </p>
    

Note the `<abbr>` element nested inside the `<dfn>`. The former establishes that the term is an abbreviation ("HST") and specifies the full term ("Hubble Space Telescope") in its `title` attribute. The latter indicates that the abbreviated term represents a term being defined.

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)<br>. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, but no `<dfn>` element must be a descendant. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [`term`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/term_role) |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-dfn-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-dfn-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn#see_also)

----------------------------------------------------------------------------------------------

*   Elements related to definition lists: [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)
    , [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)
    , [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
    
*   [`<abbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/abbr)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dfn/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/dfn/index.md?plain=1 "Folder: en-us/web/html/reference/elements/dfn (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdfn&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdfn%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdfn%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdfn%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")