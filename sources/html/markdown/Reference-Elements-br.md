*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#mdn-search)
    

`<br>` HTML line break element
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<br>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element produces a line break in text (carriage-return). It is useful for writing a poem or an address, where the division of lines is significant.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#try_it)

-----------------------------------------------------------------------------------------

    <p>
      O'er all the hilltops<br />
      Is quiet now,<br />
      In all the treetops<br />
      Hearest thou<br />
      Hardly a breath;<br />
      The birds are asleep in the trees:<br />
      Wait, soon like these<br />
      Thou too shalt rest.
    </p>
    

    p {
      font-size: 1rem;
      font-family: sans-serif;
      margin: 20px;
    }
    

As you can see from the above example, a `<br>` element is included at each point where we want the text to break. The text after the `<br>` begins again at the start of the next line of the text block.

**Note:** Do not use `<br>` to create margins between paragraphs; wrap them in [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements and use the [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 property to control their size.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#attributes)

-------------------------------------------------------------------------------------------------

This element's attributes include the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#deprecated_attributes)

[`clear`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#clear)

Indicates where to begin the next line after the break.

[Styling with CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#styling_with_css)

-------------------------------------------------------------------------------------------------------------

The `<br>` element has a single, well-defined purpose — to create a line break in a block of text. As such, it has no dimensions or visual output of its own, and there is very little you can do to style it.

You can set a [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 on `<br>` elements themselves to increase the spacing between the lines of text in the block, but this is a bad practice — you should use the [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
 property that was designed for that purpose.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#accessibility)

-------------------------------------------------------------------------------------------------------

Creating separate paragraphs of text using `<br>` is not only bad practice, it is problematic for people who navigate with the aid of screen reading technology. Screen readers may announce the presence of the element, but not any content contained within `<br>`s. This can be a confusing and frustrating experience for the person using the screen reader.

Use `<p>` elements, and use CSS properties like [`margin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 to control their spacing.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#examples)

---------------------------------------------------------------------------------------------

### [Basic br](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#basic_br)

In the following example we use `<br>` elements to create line breaks between the different lines of a postal address:

html

    Mozilla<br />
    331 E. Evelyn Avenue<br />
    Mountain View, CA<br />
    94041<br />
    USA<br />
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#technical_summary)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. In XHTML documents, write this element as `<br />`. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | [`none`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/none_role)<br>, [`presentation`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/presentation_role) |
| DOM interface | [`HTMLBRElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLBRElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-br-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-br-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br#see_also)

---------------------------------------------------------------------------------------------

*   [`<address>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/address)
     element
*   [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
     element
*   [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr)
     element

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/br/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/br/index.md?plain=1 "Folder: en-us/web/html/reference/elements/br (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbr&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbr%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbr%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbr%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")