*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#mdn-search)
    

`<tt>` HTML teletype text element
=================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<tt>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element creates inline text which is presented using the [user agent's](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 default monospace font face. This element was created for the purpose of rendering text as it would be displayed on a fixed-width display such as a teletype, text-only screen, or line printer.

The terms **non-proportional**, **monotype**, and **monospace** are used interchangeably and have the same general meaning: they describe a typeface whose characters are all the same number of pixels wide.

This element is obsolete, however. You should use the more semantically helpful [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
, [`<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd)
, [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
, or [`<var>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var)
 elements for inline text that needs to be presented in monospace type, or the [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
 tag for content that should be presented as a separate block.

**Note:** If none of the semantic elements are appropriate for your use case (for example, if you need to show some content in a non-proportional font), you should consider using the [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 element, styling it as desired using CSS. The [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
 property is a good place to start.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#attributes)

-------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#examples)

---------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#basic_example)

This example uses `<tt>` to show text entered into, and output by, a terminal application.

html

    <p>
      Enter the following at the telnet command prompt:
      <code>set localecho</code><br />
    
      The telnet client should display: <tt>Local Echo is on</tt>
    </p>
    

#### Result

### [Overriding the default font](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#overriding_the_default_font)

You can override the browser's default font—if the browser permits you to do so, which it isn't required to do—using CSS:

#### CSS

css

    tt {
      font-family: "Lucida Console", "Menlo", "Monaco", "Courier New", monospace;
    }
    

#### HTML

html

    <p>
      Enter the following at the telnet command prompt:
      <code>set localecho</code><br />
    
      The telnet client should display: <tt>Local Echo is on</tt>
    </p>
    

#### Result

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#usage_notes)

---------------------------------------------------------------------------------------------------

The `<tt>` element is, by default, rendered using the browser's default non-proportional font. You can override this using CSS by creating a rule using the `tt` selector, as seen in the example [Overriding the default font](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#overriding_the_default_font)
 above.

**Note:** User-configured changes to the default monospace font setting may take precedence over your CSS.

Although this element wasn't officially deprecated in HTML 4.01, its use was discouraged in favor of the semantic elements and/or CSS. The `<tt>` element is obsolete in HTML 5.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#technical_summary)

---------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# tt](https://html.spec.whatwg.org/multipage/obsolete.html#tt) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt#see_also)

---------------------------------------------------------------------------------------------

*   The semantic [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
    , [`<var>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/var)
    , [`<kbd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd)
    , and [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
     elements
*   The [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
     element for displaying preformatted text blocks

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/tt/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/tt/index.md?plain=1 "Folder: en-us/web/html/reference/elements/tt (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftt&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftt%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftt%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftt%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")