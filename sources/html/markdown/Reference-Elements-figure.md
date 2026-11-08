*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#mdn-search)
    

`<figure>` HTML figure with optional caption element
====================================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<figure>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents self-contained content, potentially with an optional caption, which is specified using the [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)
 element. The figure, its caption, and its contents are referenced as a single unit.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#try_it)

---------------------------------------------------------------------------------------------

    <figure>
      <img
        src="/shared-assets/images/examples/elephant.jpg"
        alt="Elephant at sunset" />
      <figcaption>An elephant at sunset</figcaption>
    </figure>
    

    figure {
      border: thin silver solid;
      display: flex;
      flex-flow: column;
      padding: 5px;
      max-width: 220px;
      margin: auto;
    }
    
    img {
      max-width: 220px;
      max-height: 150px;
    }
    
    figcaption {
      background-color: #222222;
      color: white;
      font: italic smaller sans-serif;
      padding: 3px;
      text-align: center;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#attributes)

-----------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#usage_notes)

-------------------------------------------------------------------------------------------------------

*   Usually a `<figure>` is an image, illustration, diagram, code snippet, etc., that is referenced in the main flow of a document, but that can be moved to another part of the document or to an appendix without affecting the main flow.
*   A caption can be associated with the `<figure>` element by inserting a [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)
     inside it (as the first or the last child). The first `<figcaption>` element found in the figure is presented as the figure's caption.
*   The `<figcaption>` provides the [accessible name](https://developer.mozilla.org/en-US/docs/Glossary/Accessible_name)
     for the parent `<figure>`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#examples)

-------------------------------------------------------------------------------------------------

### [Images](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#images)

html

    <!-- Just an image -->
    <figure>
      <img src="favicon-192x192.png" alt="The beautiful MDN logo." />
    </figure>
    
    <!-- Image with a caption -->
    <figure>
      <img src="favicon-192x192.png" alt="The beautiful MDN logo." />
      <figcaption>MDN Logo</figcaption>
    </figure>
    

#### Result

### [Code snippets](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#code_snippets)

html

    <figure>
      <figcaption>Get browser details using <code>navigator</code>.</figcaption>
      <pre>
    function NavigatorExample() {
      let txt = `Browser CodeName: ${navigator.appCodeName};\n`;
      txt += `Browser Name: ${navigator.appName};\n`;
      txt += `Browser Version: ${navigator.appVersion};\n`;
      txt += `Cookies Enabled: ${navigator.cookieEnabled};\n`;
      txt += `Platform: ${navigator.platform};\n`;
      txt += `User-agent header: ${navigator.userAgent};`;
      console.log("NavigatorExample", txt);
    }
      </pre>
    </figure>
    

#### Result

### [Quotations](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#quotations)

html

    <figure>
      <figcaption><b>Edsger Dijkstra:</b></figcaption>
      <blockquote>
        If debugging is the process of removing software bugs, then programming must
        be the process of putting them in.
      </blockquote>
    </figure>
    

#### Result

### [Poems](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#poems)

html

    <figure>
      <p>
        Bid me discourse, I will enchant thine ear,<br />
        Or like a fairy trip upon the green,<br />
        Or, like a nymph, with long dishevelled hair,<br />
        Dance on the sands, and yet no footing seen:<br />
        Love is a spirit all compact of fire,<br />
        Not gross to sink, but light, and will aspire.<br />
      </p>
      <figcaption><cite>Venus and Adonis</cite>, by William Shakespeare</figcaption>
    </figure>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)<br>. |
| Permitted content | A [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)<br> element, followed by [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>; or flow content followed by a [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)<br> element; or flow content. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Implicit ARIA role | [figure](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/figure_role) |
| Permitted ARIA roles | With no [figcaption](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)<br> descendant: [any](https://w3c.github.io/html-aria/#dfn-any-role "External link (opens in new tab)")<br>, otherwise no permitted roles |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-figure-element](https://html.spec.whatwg.org/multipage/grouping-content.html#the-figure-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure#see_also)

-------------------------------------------------------------------------------------------------

*   The [`<figcaption>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figcaption)
     element.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/figure/index.md?plain=1 "Folder: en-us/web/html/reference/elements/figure (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ffigure&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ffigure%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ffigure%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ffigure%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")