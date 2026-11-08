*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#mdn-search)
    

`<dl>` HTML description list element
====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<dl>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a description list. The element encloses a list of groups of terms (specified using the [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)
 element) and descriptions (provided by [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
 elements). Common uses for this element are to implement a glossary or to display metadata (a list of key-value pairs).

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#try_it)

-----------------------------------------------------------------------------------------

    <p>Cryptids of Cornwall:</p>
    
    <dl>
      <dt>Beast of Bodmin</dt>
      <dd>A large feline inhabiting Bodmin Moor.</dd>
    
      <dt>Morgawr</dt>
      <dd>A sea serpent.</dd>
    
      <dt>Owlman</dt>
      <dd>A giant owl-like creature.</dd>
    </dl>
    

    p,
    dt {
      font-weight: bold;
    }
    
    dl,
    dd {
      font-size: 0.9rem;
    }
    
    dd {
      margin-bottom: 1em;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#attributes)

-------------------------------------------------------------------------------------------------

This element also accepts the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`compact`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#compact)

This Boolean attribute hints that the list should be rendered in a compact style. The interpretation of this attribute is browser-specific. Use [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 instead: to give a similar effect as the `compact` attribute, the CSS property [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
 can be used with a value of `80%`.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#accessibility)

-------------------------------------------------------------------------------------------------------

Each screen reader exposes `<dl>` content differently, including total count, terms/definitions context, and navigation methods. These differences are not necessarily bugs. As of iOS 14, VoiceOver will announce that `<dl>` content is a list when navigating with the virtual cursor (not via the read-all command). VoiceOver does not support list navigation commands with `<dl>`. Be careful applying ARIA `term` and `definition` roles to `<dl>` constructs as VoiceOver (macOS and iOS) will adjust how they are announced.

*   [VoiceOver on iOS 14 Supports Description Lists](https://adrianroselli.com/2020/09/voiceover-on-ios-14-supports-description-lists.html "External link (opens in new tab)")
    
*   [Brief Note on Description List Support](https://adrianroselli.com/2022/12/brief-note-on-description-list-support.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#examples)

---------------------------------------------------------------------------------------------

### [Single term and description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#single_term_and_description)

html

    <dl>
      <dt>Firefox</dt>
      <dd>
        A free, open source, cross-platform, graphical web browser developed by the
        Mozilla Corporation and hundreds of volunteers.
      </dd>
    
      <!-- Other terms and descriptions -->
    </dl>
    

#### Result

### [Multiple terms, single description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#multiple_terms_single_description)

html

    <dl>
      <dt>Firefox</dt>
      <dt>Mozilla Firefox</dt>
      <dt>Fx</dt>
      <dd>
        A free, open source, cross-platform, graphical web browser developed by the
        Mozilla Corporation and hundreds of volunteers.
      </dd>
    
      <!-- Other terms and descriptions -->
    </dl>
    

#### Result

### [Single term, multiple descriptions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#single_term_multiple_descriptions)

html

    <dl>
      <dt>Firefox</dt>
      <dd>
        A free, open source, cross-platform, graphical web browser developed by the
        Mozilla Corporation and hundreds of volunteers.
      </dd>
      <dd>
        The Red Panda also known as the Lesser Panda, Wah, Bear Cat or Firefox, is a
        mostly herbivorous mammal, slightly larger than a domestic cat (60 cm long).
      </dd>
    
      <!-- Other terms and descriptions -->
    </dl>
    

#### Result

### [Multiple terms and descriptions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#multiple_terms_and_descriptions)

It is also possible to define multiple terms with multiple corresponding descriptions, by combining the examples above.

### [Metadata](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#metadata)

Description lists are useful for displaying metadata as a list of key-value pairs.

html

    <dl>
      <dt>Name</dt>
      <dd>Godzilla</dd>
      <dt>Born</dt>
      <dd>1952</dd>
      <dt>Birthplace</dt>
      <dd>Japan</dd>
      <dt>Color</dt>
      <dd>Green</dd>
    </dl>
    

#### Result

Tip: It can be handy to define a key-value separator in the CSS, such as:

css

    dt::after {
      content: ": ";
    }
    

### [Wrapping name-value groups in `div` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#wrapping_name-value_groups_in_div_elements)

HTML allows wrapping each name-value group in a `<dl>` element in a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element. This can be useful when using [microdata](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Microdata)
, or when [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 apply to a whole group, or for styling purposes.

html

    <dl>
      <div>
        <dt>Name</dt>
        <dd>Godzilla</dd>
      </div>
      <div>
        <dt>Born</dt>
        <dd>1952</dd>
      </div>
      <div>
        <dt>Birthplace</dt>
        <dd>Japan</dd>
      </div>
      <div>
        <dt>Color</dt>
        <dd>Green</dd>
      </div>
    </dl>
    

#### Result

[Notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#notes)

---------------------------------------------------------------------------------------

Do not use this element (nor [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 elements) to merely create indentation on a page. Although it works, this is a bad practice and obscures the meaning of description lists.

To change the indentation of a description term, use the [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 property.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#technical_summary)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, and if the `<dl>` element's children include one name-value group, palpable content. |
| Permitted content | Either: Zero or more groups each consisting of one or more [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)<br> elements followed by one or more [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)<br> elements, optionally intermixed with [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)<br> and [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)<br> elements.  <br>Or: (in [WHATWG](https://developer.mozilla.org/en-US/docs/Glossary/WHATWG)<br> HTML, [W3C](https://developer.mozilla.org/en-US/docs/Glossary/W3C)<br> HTML 5.2 and later) One or more [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)<br> elements, optionally intermixed with [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)<br> and [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)<br> elements. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | [`group`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/group_role)<br>, `[list](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/list_role) `, [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role) |
| DOM interface | [`HTMLDListElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDListElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-dl-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-dl-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl#see_also)

---------------------------------------------------------------------------------------------

*   [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)
    
*   [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/dl/index.md?plain=1 "Folder: en-us/web/html/reference/elements/dl (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdl&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdl%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdl%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdl%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")