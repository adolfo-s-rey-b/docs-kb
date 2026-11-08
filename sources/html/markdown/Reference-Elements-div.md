*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#mdn-search)
    

`<div>` HTML content division element
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<div>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is the generic container for flow content. It has no effect on the content or layout until styled in some way using [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
 (e.g., styling is directly applied to it, or some kind of layout model like [Flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 is applied to its parent element).

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#try_it)

------------------------------------------------------------------------------------------

    <div class="warning">
      <img
        src="/shared-assets/images/examples/leopard.jpg"
        alt="An intimidating leopard." />
      <p>Beware of the leopard</p>
    </div>
    

    .warning {
      border: 10px ridge red;
      background-color: yellow;
      padding: 0.5rem;
      display: flex;
      flex-direction: column;
    }
    
    .warning img {
      width: 100%;
    }
    
    .warning p {
      font: small-caps bold 1.2rem sans-serif;
      text-align: center;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#attributes)

--------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

**Note:** The `align` attribute is obsolete; do not use it anymore. Instead, you should use CSS properties or techniques such as [CSS Grid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 or [CSS Flexbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox)
 to align and position `<div>` elements on the page.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#usage_notes)

----------------------------------------------------------------------------------------------------

As a "pure" container, the `<div>` element does not inherently represent anything. Instead, it's used to group content so it can be easily styled using the [`class`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class)
 or [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attributes, marking a section of a document as being written in a different language (using the [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 attribute), and so on.

The `<div>` element should be used only when no other semantic element (such as [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 or [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
) is appropriate.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#accessibility)

--------------------------------------------------------------------------------------------------------

The `<div>` element has [an implicit role of `generic`](https://w3c.github.io/aria/#generic "External link (opens in new tab)")
, and not none. This may affect certain ARIA combination declarations that expect a direct descendant element with a certain role to function properly.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#examples)

----------------------------------------------------------------------------------------------

### [A basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#a_basic_example)

html

    <div>
      <p>
        Any kind of content here. Such as &lt;p&gt;, &lt;table&gt;. You name it!
      </p>
    </div>
    

#### Result

### [A styled example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#a_styled_example)

This example creates a shadowed box by applying a style to the `<div>` using CSS. Note the use of the [`class`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class)
 attribute on the `<div>` to apply the style named `"shadowbox"` to the element.

#### HTML

html

    <div class="shadowbox">
      <p>Here's a very interesting note displayed in a lovely shadowed box.</p>
    </div>
    

#### CSS

css

    .shadowbox {
      width: 15em;
      border: 1px solid #333333;
      box-shadow: 8px 8px 5px #444444;
      padding: 8px 12px;
      background-image: linear-gradient(180deg, white, #dddddd 40%, #cccccc);
    }
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)<br>. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>.  <br>Or (in [WHATWG](https://developer.mozilla.org/en-US/docs/Glossary/WHATWG)<br> HTML): If the parent is a [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)<br> element: one or more [`<dt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dt)<br> elements followed by one or more [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)<br> elements, optionally intermixed with [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)<br> and [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)<br> elements. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>.  <br>Or (in [WHATWG](https://developer.mozilla.org/en-US/docs/Glossary/WHATWG)<br> HTML): [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)<br> element. |
| Implicit ARIA role | `[generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLDivElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLDivElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-div-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-div-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div#see_also)

----------------------------------------------------------------------------------------------

*   Semantic sectioning elements: [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
    , [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
    , [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
    , [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)
    , [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)
    
*   [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
     element for styling of phrasing content

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/div/index.md?plain=1 "Folder: en-us/web/html/reference/elements/div (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdiv&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdiv%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fdiv%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fdiv%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F100cf25d92d3953f3c70ecaa2af637d5e42179d8%0A*+Document+last+modified%3A+2026-09-10T17%3A31%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")