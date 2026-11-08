*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#mdn-search)
    

`<small>` HTML side comment element
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<small>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents side-comments and small print, like copyright and legal text, independent of its styled presentation. By default, it renders text within it one font-size smaller, such as from `small` to `x-small`.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#try_it)

--------------------------------------------------------------------------------------------

    <p>
      MDN Web Docs is a learning platform for Web technologies and the software that
      powers the Web.
    </p>
    
    <hr />
    
    <p>
      <small
        >The content is licensed under a Creative Commons Attribution-ShareAlike 2.5
        Generic License.</small
      >
    </p>
    

    small {
      font-size: 0.7em;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#attributes)

----------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#examples)

------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#basic_usage)

html

    <p>
      This is the first sentence.
      <small>This whole sentence is in small letters.</small>
    </p>
    

#### Result

### [CSS alternative](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#css_alternative)

html

    <p>
      This is the first sentence.
      <span class="small">This whole sentence is in small letters.</span>
    </p>
    

css

    .small {
      font-size: 0.8em;
    }
    

#### Result

[Notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#notes)

------------------------------------------------------------------------------------------

Although the `<small>` element, like the [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
 and [`<i>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/i)
 elements, may be perceived to violate the principle of separation between structure and presentation, all three are valid in HTML. Authors are encouraged to use their best judgment when determining whether to use `<small>` or CSS.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content) |
| Tag omission | None; must have both a start tag and an end tag. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, or any element that accepts [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | `[generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) ` |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-small-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-small-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small#see_also)

------------------------------------------------------------------------------------------------

*   [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
    
*   [`<sub>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sub)
     and [`<sup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/sup)
    
*   [`<font>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/font)
    
*   [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/small/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/small/index.md?plain=1 "Folder: en-us/web/html/reference/elements/small (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsmall&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsmall%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fsmall%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fsmall%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F87adaa5384b1015690f3435ce0ba64ac097764eb%0A*+Document+last+modified%3A+2026-08-27T09%3A50%3A47.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")