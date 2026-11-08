*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#mdn-search)
    

`<h1>–<h6>` HTML section heading elements
=========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<h1>`** to **`<h6>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 elements represent six levels of section headings. `<h1>` is the highest section level and `<h6>` is the lowest. By default, all heading elements create a [block-level](https://developer.mozilla.org/en-US/docs/Glossary/Block-level_content)
 box in the layout, starting on a new line and taking up the full width available in their containing block.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#try_it)

-------------------------------------------------------------------------------------------------------

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#attributes)

---------------------------------------------------------------------------------------------------------------

These elements only include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

The [`headingoffset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingoffset)
 and [`headingreset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/headingreset)
 global attributes can be used to adjust the computed heading level of these elements.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#usage_notes)

-----------------------------------------------------------------------------------------------------------------

*   Heading information can be used by user agents to construct a table of contents for a document automatically.
*   Do not use heading elements to resize text. Instead, use the [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
     [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
     property.
*   Do not skip heading levels: always start from `<h1>`, followed by `<h2>` and so on.

### [Avoid using multiple `<h1>` elements on one page](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#avoid_using_multiple_h1_elements_on_one_page)

While using multiple `<h1>` elements on one page is allowed by the HTML standard (as long as they are not [nested](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#nesting)
), this is not considered a best practice. A page should generally have a single `<h1>` element that describes the content of the page (similar to the document's [`<title>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/title)
 element).

**Note:** Nesting multiple `<h1>` elements in nested [sectioning elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#content_sectioning)
 was allowed in older versions of the HTML standard. However, this was never considered a best practice and is now non-conforming. Read more in [There Is No Document Outline Algorithm](https://adrianroselli.com/2016/08/there-is-no-document-outline-algorithm.html "External link (opens in new tab)")
.

Prefer using only one `<h1>` per page and [nest headings](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#nesting)
 without skipping levels.

### [Specifying a uniform font size for `<h1>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#specifying_a_uniform_font_size_for_h1)

Before May 2025, the [HTML standard](https://html.spec.whatwg.org/multipage/rendering.html#sections-and-headings "External link (opens in new tab)")
 specified that `<h1>` elements in a `<section>`, `<article>`, `<aside>`, or `<nav>` element should render as an `<h2>` (smaller [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 with an adjusted [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
), or as an `<h3>` if nested another level, and so on. This special context-dependent default style has now been [removed](https://github.com/whatwg/html/issues/7867 "External link (opens in new tab)")
.

To ensure consistent `<h1>` rendering for browsers that implement the old context-dependent default style, use the following style rule:

Alternatively, to avoid overwriting other style rules that target `<h1>` you can use [`:where()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:where)
, which has zero specificity:

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#accessibility)

---------------------------------------------------------------------------------------------------------------------

### [Navigation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#navigation)

A common navigation technique for users of screen reading software is to quickly jump from heading to heading in order to determine the content of the page. Because of this, it is important to not skip one or more heading levels. Doing so may create confusion, as the person navigating this way may be left wondering where the missing heading is.

**Don't do this:**

**Prefer this:**

#### Nesting

Headings may be nested as subsections to reflect the organization of the content of the page. Most screen readers can also generate an ordered list of all the headings on a page, which can help a person quickly determine the content hierarchy and navigate to different headings.

Given the following page structure:

Screen readers would generate a list like this:

1.  `h1` Beetles
    1.  `h2` Etymology
        
    2.  `h2` Distribution and Diversity
        
    3.  `h2` Evolution
        
        1.  `h3` Late Paleozoic
        2.  `h3` Jurassic
        3.  `h3` Cretaceous
        4.  `h3` Cenozoic
    4.  `h2` External Morphology
        
        1.  `h3` Head
            
            1.  `h4` Mouthparts
        2.  `h3` Thorax
            
            1.  `h4` Prothorax
            2.  `h4` Pterothorax
        3.  `h3` Legs
            
        4.  `h3` Wings
            
        5.  `h3` Abdomen
            

When headings are nested, heading levels may be "skipped" when closing a subsection.

*   [Headings • Page Structure • WAI Web Accessibility Tutorials](https://www.w3.org/WAI/tutorials/page-structure/headings/ "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 1.3 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.3_%E2%80%94_create_content_that_can_be_presented_in_different_ways)
    
*   [Understanding Success Criterion 1.3.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/content-structure-separation-programmatic.html "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 2.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Operable#guideline_2.4_%E2%80%94_navigable_provide_ways_to_help_users_navigate_find_content_and_determine_where_they_are)
    
*   [Understanding Success Criterion 2.4.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/navigation-mechanisms-skip.html "External link (opens in new tab)")
    
*   [Understanding Success Criterion 2.4.6 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/navigation-mechanisms-descriptive.html "External link (opens in new tab)")
    
*   [Understanding Success Criterion 2.4.10 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/navigation-mechanisms-headings.html "External link (opens in new tab)")
    

### [Labeling section content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#labeling_section_content)

Another common navigation technique for users of screen reading software is to generate a list of [sectioning content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements#content_sectioning)
 and use it to determine the page's layout.

Sectioning content can be labeled using a combination of the [`aria-labelledby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby)
 and [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attributes, with the label concisely describing the purpose of the section. This technique is useful for situations where there is more than one sectioning element on the same page.

#### Sectioning content examples

In this example, screen reading technology would announce that there are two [`<nav>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/nav)
 sections, one called "Primary navigation" and one called "Footer navigation". If labels were not provided, the person using screen reading software may have to investigate each `nav` element's contents to determine their purpose.

*   [Using the aria-labelledby attribute](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby)
    
*   [Labeling Regions • Page Structure • W3C WAI Web Accessibility Tutorials](https://www.w3.org/WAI/tutorials/page-structure/labels/#using-aria-labelledby "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#examples)

-----------------------------------------------------------------------------------------------------------

### [All headings](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#all_headings)

The following code shows all the heading levels, in use.

### [Example page](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#example_page)

The following code shows a few headings with some content under them.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#technical_summary)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, heading content, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | [heading](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/heading_role) |
| Permitted ARIA roles | [`tab`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tab_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role)<br> or [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role) |
| DOM interface | [`HTMLHeadingElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLHeadingElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-h1,-h2,-h3,-h4,-h5,-and-h6-elements](https://html.spec.whatwg.org/multipage/sections.html#the-h1,-h2,-h3,-h4,-h5,-and-h6-elements) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

### [html.elements.h1](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#html.elements.h1)

### [html.elements.h2](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#html.elements.h2)

### [html.elements.h3](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#html.elements.h3)

### [html.elements.h4](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#html.elements.h4)

### [html.elements.h5](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#html.elements.h5)

### [html.elements.h6](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#html.elements.h6)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
    
*   [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
    
*   [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/heading_elements/index.md?plain=1 "Folder: en-us/web/html/reference/elements/heading_elements (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2FHeading_Elements&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fheading_elements%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2FHeading_Elements%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fheading_elements%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff398f522d05bb8bfe739ac2417b00712b7888494%0A*+Document+last+modified%3A+2026-08-26T20%3A00%3A43.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")