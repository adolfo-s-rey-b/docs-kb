*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target#mdn-search)
    

`:target` CSS pseudo-class
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:target`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 selects the _target element of the document_. When the document is loaded, the target element is derived using the document's [URL fragment identifier](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment#fragment)
.

css

    /* Selects document's target element */
    :target {
      border: 2px solid black;
    }
    

For example, the following URL has a fragment identifier (denoted by the _#_ sign) that marks the element with the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 of `setup` as the document's target element:

url

    http://www.example.com/help/#setup
    

The following element would be selected by a `:target` selector when the current URL is equal to the above:

html

    <section id="setup">Installation instructions</section>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target#syntax)

----------------------------------------------------------------------------------------------

css

    :target {
      /* ... */
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target#description)

--------------------------------------------------------------------------------------------------------

When an HTML document loads, the browser sets its target element. The element is identified using the URL fragment identifier. Without the URL fragment identifier, the document has no target element. The `:target` pseudo-class allows styling the document's target element. The element could be focused, highlighted, animated, etc.

The target element is set at document load and [`history.back()`](https://developer.mozilla.org/en-US/docs/Web/API/History/back)
, [`history.forward()`](https://developer.mozilla.org/en-US/docs/Web/API/History/forward)
, and [`history.go()`](https://developer.mozilla.org/en-US/docs/Web/API/History/go)
 method calls. But it is _not_ changed when [`history.pushState()`](https://developer.mozilla.org/en-US/docs/Web/API/History/pushState)
 and [`history.replaceState()`](https://developer.mozilla.org/en-US/docs/Web/API/History/replaceState)
 methods are called.

**Note:** Due to [a possible bug in the CSS specification](https://discourse.wicg.io/t/target-css-does-not-work-because-shadowroot-does-not-set-a-target-element/2070/ "External link (opens in new tab)")
, `:target` doesn't work within a [web component](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)
 because the [shadow root](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
 doesn't pass the target element down to the shadow tree.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target#examples)

--------------------------------------------------------------------------------------------------

### [A table of contents](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target#a_table_of_contents)

The `:target` pseudo-class can be used to highlight the portion of a page that has been linked to from a table of contents.

#### HTML

html

    <h3>Table of Contents</h3>
    <ol>
      <li><a href="#p1">Jump to the first paragraph!</a></li>
      <li><a href="#p2">Jump to the second paragraph!</a></li>
      <li>
        <a href="#nowhere">
          This link goes nowhere, because the target doesn't exist.
        </a>
      </li>
    </ol>
    
    <h3>My Fun Article</h3>
    <p id="p1">
      You can target <i>this paragraph</i> using a URL fragment. Click on the first
      link above to try out!
    </p>
    <p id="p2">
      This is <i>another paragraph</i>, also accessible from the second link above.
      Isn't that delightful?
    </p>
    

#### CSS

css

    p:target {
      background-color: gold;
    }
    
    /* Add a pseudo-element inside the target element */
    p:target::before {
      font: 70% sans-serif;
      content: "►";
      color: limegreen;
      margin-right: 0.25em;
    }
    
    /* Style italic elements within the target element */
    p:target i {
      color: red;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-target](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-target) |
| [Selectors Level 4  <br>\# target-pseudo](https://drafts.csswg.org/selectors/#target-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target#see_also)

--------------------------------------------------------------------------------------------------

*   [Using the :target pseudo-class in selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Using_:target)
    
*   [`::target-text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::target-text)
     (for highlighting text fragments)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 19, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_target/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_target (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Atarget&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_target%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Atarget%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_target%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F42f8ef9d26f9a76723a0379a2e7c946db496f27e%0A*+Document+last+modified%3A+2026-08-19T11%3A43%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")