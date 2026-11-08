*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#mdn-search)
    

`<summary>` HTML disclosure summary element
===========================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<summary>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element specifies a summary, caption, or legend for a [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
 element's disclosure box. Clicking the `<summary>` element toggles the state of the parent `<details>` element open and closed.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#try_it)

----------------------------------------------------------------------------------------------

    <details>
      <summary>
        I have keys but no doors. I have space but no room. You can enter but can't
        leave. What am I?
      </summary>
      A keyboard.
    </details>
    

    details {
      border: 1px solid #aaaaaa;
      border-radius: 4px;
      padding: 0.5em 0.5em 0;
    }
    
    summary {
      font-weight: bold;
      margin: -0.5em -0.5em 0;
      padding: 0.5em;
    }
    
    details[open] {
      padding: 0.5em;
    }
    
    details[open] summary {
      border-bottom: 1px solid #aaaaaa;
      margin-bottom: 0.5em;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#attributes)

------------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#usage_notes)

--------------------------------------------------------------------------------------------------------

The `<summary>` element's contents can be any heading content, plain text, or HTML that can be used within a paragraph.

A `<summary>` element may _only_ be used as the first child of a `<details>` element. When the user clicks on the summary, the parent `<details>` element is toggled open or closed, and then a [`toggle`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/toggle_event "toggle")
 event is sent to the `<details>` element, which can be used to let you know when this state change occurs.

The content of the `<details>` provides the [accessible description](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_description)
 for the `<summary>`.

### [Default label text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#default_label_text)

If a `<details>` element's first child is not a `<summary>` element, the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 will use a default string (typically "Details") as the label for the disclosure box.

### [Default style](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#default_style)

Per the HTML specification, the default style for `<summary>` elements includes `display: list-item`. This makes it possible to change or remove the icon displayed as the disclosure widget next to the label from the default, which is typically a triangle.

You can also change the style to `display: block` to remove the disclosure triangle.

See the [Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#browser_compatibility)
 section for details, as not all browsers support full functionality of this element yet.

For WebKit-based browsers, such as Safari, it is possible to control the icon display through the non-standard CSS pseudo-element `::-webkit-details-marker`. To remove the disclosure triangle, use `summary::-webkit-details-marker { display: none }`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#examples)

--------------------------------------------------------------------------------------------------

Below are some examples showing `<summary>` in use. You can find more examples in the documentation for the [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
 element.

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#basic_example)

A basic example showing the use of `<summary>` in a [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
 element:

html

    <details open>
      <summary>Overview</summary>
      <ol>
        <li>Cash on hand: $500.00</li>
        <li>Current invoice: $75.30</li>
        <li>Due date: 5/6/19</li>
      </ol>
    </details>
    

#### Result

### [Summaries as headings](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#summaries_as_headings)

You can use heading elements in `<summary>`, like this:

html

    <details open>
      <summary><h4>Overview</h4></summary>
      <ol>
        <li>Cash on hand: $500.00</li>
        <li>Current invoice: $75.30</li>
        <li>Due date: 5/6/19</li>
      </ol>
    </details>
    

#### Result

This currently has some spacing issues that could be addressed using CSS.

**Warning:** The role assigned to the `<summary>` element varies across browsers. Some still assign it a default [`button`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role)
 role, which removes all roles from its children. This inconsistency can cause issues for users of assistive technologies such as screen readers (`<h4>` in the previous example will have its role removed and will not be treated as a heading for these users). You should test your `<summary>` implementation on multiple platforms to ensure there's consistent accessibility support.

### [HTML in summaries](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#html_in_summaries)

This example adds some semantics to the `<summary>` element to indicate the label as important:

html

    <details open>
      <summary><strong>Overview</strong></summary>
      <ol>
        <li>Cash on hand: $500.00</li>
        <li>Current invoice: $75.30</li>
        <li>Due date: 5/6/19</li>
      </ol>
    </details>
    

#### Result

### [Changing the summary's icon](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#changing_the_summarys_icon)

The `<summary>` element's marker, the disclosure triangle, can be customized with CSS. The marker can be targeted using the [`::marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::marker)
 pseudo-element. which accepts the [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
 shorthand property and its longhand component properties, such as [`list-style-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-type)
. This enables changing the triangle to an image (usually with [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
) or a string (including emojis). In this example, we replace the content of one disclosure widget and remove the icon from another by setting `list-style: none` before adding a custom disclosure icon via generated content.

#### CSS

In the first disclosure widget, we style the `::marker`, changing the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 based on the `<details>` element's `[open]` attribute. For the second widget, we remove the marker with `list-style` properties, then add styled generated content with the [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
 pseudo-element. We also include styles for `::-webkit-details-marker` to target Safari. The selector for the browser-specific pseudo-element is included in an [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
 pseudo-class so it doesn't invalidate the selector list.

css

    details {
      font-size: 1rem;
      font-family: "Open Sans", "Calibri", sans-serif;
      border: solid;
      padding: 2px 6px;
      margin-bottom: 1em;
    }
    
    details:first-of-type summary::marker,
    :is(::-webkit-details-marker) {
      content: "+ ";
      font-family: monospace;
      color: red;
      font-weight: bold;
    }
    
    details[open]:first-of-type summary::marker {
      content: "− ";
    }
    
    details:last-of-type summary {
      list-style: none;
      &::after {
        content: "+";
        color: white;
        background-color: darkgreen;
        border-radius: 1em;
        font-weight: bold;
        padding: 0 5px;
        margin-inline-start: 5px;
      }
      [open] &::after {
        content: "−";
      }
    }
    details:last-of-type summary::-webkit-details-marker {
      display: none;
    }
    

The CSS includes the `[open]` [attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
, matching only when the `open` attribute is present (when the `<details>` are open). The [`:first-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
 and [`:last-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-of-type)
 pseudo-classes target the first and sibling elements of the same type. We included the prefixed `-webkit-` pseudo-element within a [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
 pseudo-class as it takes a [forgiving selector list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Selector_list#forgiving_selector_list)
, so if the prefixed pseudo-element is invalid in a browser, the whole selector block will not be invalid. We also used CSS [nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector)
. See the [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
 module.

#### HTML

html

    <h1>Quotes from Helen Keller</h1>
    
    <details>
      <summary>On women's rights</summary>
      <p>
        <q>We have prayed, we have coaxed, we have begged, for the vote, with the
          hope that men, out of chivalry, would bestow equal rights upon women and
          take them into partnership in the affairs of the state. We hoped that
          their common sense would triumph over prejudices and stupidity. We thought
          their boasted sense of justice would overcome the errors that so often
          fetter the human spirit; but we have always gone away empty-handed. We
          shall beg no more.</q>
      </p>
    </details>
    
    <details>
      <summary>On optimism</summary>
      <p>
        <q>Optimism is the faith that leads to achievement; nothing can be done
          without hope.</q>
      </p>
    </details>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#technical_summary)

--------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | none |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, optionally intermixed with [Heading content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#heading_content) |
| Tag omission | None; both the start tag and the end tag are mandatory. |
| Permitted parents | The [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)<br> element. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-summary-element](https://html.spec.whatwg.org/multipage/interactive-elements.html#the-summary-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary#see_also)

--------------------------------------------------------------------------------------------------

*   [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/summary/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/summary/index.md?plain=1 "Folder: en-us/web/html/reference/elements/summary (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsummary&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsummary%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsummary%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsummary%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")