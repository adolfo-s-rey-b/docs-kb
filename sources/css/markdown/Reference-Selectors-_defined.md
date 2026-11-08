*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined#mdn-search)
    

`:defined` CSS pseudo-class
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:defined`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents any element that has been defined. This includes any standard element built into the browser and custom elements that have been successfully defined (i.e., with the [`CustomElementRegistry.define()`](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry/define)
 method).

css

    /* Selects any defined element */
    :defined {
      font-style: italic;
    }
    
    /* Selects any instance of a specific custom element */
    custom-element:defined {
      display: block;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined#syntax)

-----------------------------------------------------------------------------------------------

css

    :defined {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined#examples)

---------------------------------------------------------------------------------------------------

### [Hiding elements until they are defined](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined#hiding_elements_until_they_are_defined)

In this demo, we define a basic custom element named `<custom-element>` and use the `:not(:defined)` and `:defined` selectors to style the element before and after it is defined. This is useful if you have a complex custom element that takes a while to load into the page — you might want to hide instances of the element until the definition is complete so that you don't end up with flashes of ugly unstyled elements on the page.

#### HTML

The following HTML code uses the custom element but the element hasn't been defined yet. We also include a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 that will define the custom element when clicked, allowing you to see its state before and after definition.

html

    <custom-element>
      <p>
        Loaded content: Lorem ipsum tel sed tellus eiusmod tellus. Aenean. Semper
        dolor sit nisi. Elit porttitor nisi sit vivamus.
      </p>
    </custom-element>
    
    <button id="btn">define the <code>&lt;custom-element&gt;</code></button>
    

#### CSS

    custom-element {
      display: block;
      border: 5px dashed grey;
      border-radius: 1rem;
      height: 100px;
      width: 400px;
      padding: 1rem;
      position: relative;
      user-select: none;
    }
    
    code {
      background: #cccccc;
    }
    
    #btn {
      margin-top: 1rem;
      cursor: pointer;
    }
    

In the following CSS, we use the `custom-element:not(:defined)` selector to select the element and color it gray while it is not defined and the `custom-element:defined` selector to select the element and color it black after it is defined.

css

    custom-element:not(:defined) {
      border-color: grey;
      color: grey;
    }
    
    custom-element:defined {
      background-color: wheat;
      border-color: black;
      color: black;
    }
    
    /* show loading message */
    custom-element:not(:defined)::before {
      content: "Loading...";
      position: absolute;
      inset: 0;
      align-content: center;
      text-align: center;
      font-size: 2rem;
      background-color: white;
      border-radius: 1rem;
    }
    
    /* remove the loading message */
    custom-element:defined::before {
      content: "";
    }
    

We have also used the [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
 pseudo-element to show a "Loading..." overlay message until the element is defined. After definition, it is removed by setting the [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 to an empty string.

The following JavaScript has been used to define the custom element. To allow you to see the state of the custom element before and after definition we run the [`define()`](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry/define "define()")
 method when the button is clicked.

js

    const btn = document.querySelector("#btn");
    
    btn.addEventListener("click", () => {
      customElements.define("custom-element", class extends HTMLElement {});
      btn.remove();
    });
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-defined](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-defined) |
| [Selectors Level 4  <br>\# defined-pseudo](https://drafts.csswg.org/selectors/#defined-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined#see_also)

---------------------------------------------------------------------------------------------------

*   [Web components](https://developer.mozilla.org/en-US/docs/Web/API/Web_components)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:defined/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_defined/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_defined (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Adefined&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_defined%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Adefined%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_defined%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F28f5f3b9b463fa842fa686ccc73c9e1d9b06282b%0A*+Document+last+modified%3A+2026-08-27T09%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")