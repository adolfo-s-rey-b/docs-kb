*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#mdn-search)
    

`<p>` HTML paragraph element
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<p>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a paragraph. Paragraphs are usually represented in visual media as blocks of text separated from adjacent blocks by blank lines and/or first-line indentation, but HTML paragraphs can be any structural grouping of related content, such as images or form fields.

Paragraphs are [block-level elements](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content)
, and notably will automatically close if another block-level element is parsed before the closing `</p>` tag. See "Tag omission" below.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#try_it)

----------------------------------------------------------------------------------------

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#attributes)

------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

**Note:** The `align` attribute on `<p>` tags is obsolete and shouldn't be used.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#accessibility)

------------------------------------------------------------------------------------------------------

Breaking up content into paragraphs helps make a page more accessible. Screen-readers and other assistive technology provide shortcuts to let their users skip to the next or previous paragraph, letting them skim content like how white space lets visual users skip around.

Using empty `<p>` elements to add space between paragraphs is problematic for people who navigate with screen-reading technology. Screen readers may announce the paragraph's presence, but not any content contained within it — because there is none. This can confuse and frustrate the person using the screen reader.

If extra space is desired, use [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
 properties like [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 to create the effect:

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#examples)

--------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#html)

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#result)

[Styling paragraphs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#styling_paragraphs)

----------------------------------------------------------------------------------------------------------------

By default, browsers separate paragraphs with a single blank line. Alternate separation methods, such as first-line indentation, can be achieved with [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
:

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#html_2)

html

    <p>
      Separating paragraphs with blank lines is easiest for readers to scan, but
      they can also be separated by indenting their first lines. This is often used
      to take up less space, such as to save paper in print.
    </p>
    
    <p>
      Writing that is intended to be edited, such as school papers and rough drafts,
      uses both blank lines and indentation for separation. In finished works,
      combining both is considered redundant and amateurish.
    </p>
    
    <p>
      In very old writing, paragraphs were separated with a special character: ¶,
      the <i>pilcrow</i>. Nowadays, this is considered claustrophobic and hard to
      read.
    </p>
    
    <p>
      How hard to read? See for yourself:
      <button data-toggle-text="Oh no! Switch back!">
        Use pilcrow for paragraphs
      </button>
    </p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#css)

css

    p {
      margin: 0;
      text-indent: 3ch;
    }
    
    p.pilcrow {
      text-indent: 0;
      display: inline;
    }
    p.pilcrow + p.pilcrow::before {
      content: " ¶ ";
    }
    

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#javascript)

js

    document.querySelector("button").addEventListener("click", (event) => {
      document.querySelectorAll("p").forEach((paragraph) => {
        paragraph.classList.toggle("pilcrow");
      });
    
      [event.target.innerText, event.target.dataset.toggleText] = [\
        event.target.dataset.toggleText,\
        event.target.innerText,\
      ];
    });
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#result_2)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#technical_summary)

--------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | The start tag is required. The end tag may be omitted if the `<p>` element is immediately followed by an [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)<br>, [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)<br>, [`<aside>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/aside)<br>, [`<blockquote>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/blockquote)<br>, [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)<br>, [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)<br>, [`<dl>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dl)<br>, [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)<br>, [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)<br>, [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure)<br>, [`<footer>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/footer)<br>, [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)<br>, [h1](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h2](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h3](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h4](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h5](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [h6](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)<br>, [`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header)<br>, [`<hgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hgroup)<br>, [`<hr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr)<br>, [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)<br>, [`<menu>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/menu)<br>, [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)<br>, [`<ol>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ol)<br>, [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)<br>, [`<search>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/search)<br>, [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)<br>, [`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table)<br>, [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)<br> or another `<p>` element, or if there is no more content in the parent element and the parent element is not an [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)<br>, [`<audio>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/audio)<br>, [`<del>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/del)<br>, [`<ins>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ins)<br>, [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)<br>, [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript)<br> or [`<video>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/video)<br> element, or an autonomous custom element. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | [paragraph](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/structural_roles) |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLParagraphElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLParagraphElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#specifications)

--------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-p-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-p-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p#see_also)

--------------------------------------------------------------------------------------------

*   [`<hr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr)
    
*   [`<br>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/p/index.md?plain=1 "Folder: en-us/web/html/reference/elements/p (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fp&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fp%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fp%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fp%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")