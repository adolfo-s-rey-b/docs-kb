*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#mdn-search)
    

`<var>` HTML variable element
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<var>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents the name of a variable in a mathematical expression or a programming context. It's typically presented using an italicized version of the current typeface, although that behavior is browser-dependent.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#try_it)

------------------------------------------------------------------------------------------

    <p>
      The volume of a box is <var>l</var> × <var>w</var> × <var>h</var>, where
      <var>l</var> represents the length, <var>w</var> the width and
      <var>h</var> the height of the box.
    </p>
    

    var {
      font-weight: bold;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#attributes)

--------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#usage_notes)

----------------------------------------------------------------------------------------------------

### [Related elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#related_elements)

Other elements that are used in contexts in which `<var>` is commonly used include:

*   [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
    : The HTML Code element
*   [`<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd)
    : The HTML Keyboard input element
*   [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
    : The HTML Sample Output element

If you encounter code that is mistakenly using `<var>` for style purposes rather than semantic purposes, you should either use a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 with appropriate CSS or, an appropriate semantic element among the following:

*   [`<em>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/em)
    
*   [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)
    
*   [`<q>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/q)
    

### [Default style](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#default_style)

Most browsers apply [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
 to `"italic"` when rendering `<var>`. This can be overridden in CSS, like this:

css

    var {
      font-style: normal;
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#examples)

----------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#basic_example)

Here's a basic example, using `<var>` to denote variable names in a mathematical equation.

html

    <p>An algebraic equation: <var>x</var> = <var>y</var> + 2</p>
    

#### Result

### [Overriding the default style](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#overriding_the_default_style)

Using CSS, you can override the default style for the `<var>` element. In this example, variable names are rendered in bold, using Courier if it's available, otherwise it falls back to the default monospace font.

#### CSS

css

    var {
      font:
        bold 15px "Courier",
        "Courier New",
        monospace;
    }
    

#### HTML

html

    <p>
      The variables <var>minSpeed</var> and <var>maxSpeed</var> control the minimum
      and maximum speed of the apparatus in revolutions per minute (RPM).
    </p>
    

This HTML uses `<var>` to enclose the names of two variables.

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-var-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-var-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/var/index.md?plain=1 "Folder: en-us/web/html/reference/elements/var (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fvar&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fvar%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fvar%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fvar%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")