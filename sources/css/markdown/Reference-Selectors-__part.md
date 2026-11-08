*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#mdn-search)
    

`::part()` CSS pseudo-element
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::part`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents any element within a [shadow tree](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
 that has a matching [`part`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/part)
 attribute.

css

    custom-element::part(foo) {
      /* Styles to apply to the `foo` part */
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#description)

-------------------------------------------------------------------------------------------------------

The global [`part`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/part)
 attribute makes a shadow tree element visible to its parent DOM. The part names declared using the `part` attribute are used as the parameter of the `::part()` pseudo-element. In this way, you can apply CSS styles to elements in the shadow tree from outside of it.

Part names are similar to CSS classes: multiple elements can have the same part name, and a single element can have multiple part names. All part names used in `::part()` pseudo-element must be present in the `part` value declared on the shadow tree element but the order of the part names doesn't matter, i.e., the selectors `::part(tab active)` and `::part(active tab)` are the same.

The `::part()` pseudo-element is only visible to the parent DOM. This means that when a shadow tree is nested, the parts are not visible to any ancestors other than the direct parent. The [`exportparts`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts)
 attribute solves this limitation by explicitly exporting already defined `part` names, making them globally stylable.

[Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 (such as `::part(label):hover`) can be appended to the `::part()` selector, but [structural pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes#tree-structural_pseudo-classes)
 that match based on tree information, such as `:empty` and `:last-child`, cannot be appended.

Additional pseudo-elements, such as `::before`, can be appended to the `::part()` selector, but additional `::part()` element can't be appended. For example, `::part(confirm-button)::part(active)` never matches anything, i.e, it is not the same as `::part(confirm-button active)`. This is because doing so would expose more structural information than is intended.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#syntax)

---------------------------------------------------------------------------------------------

css

    ::part(<ident>+) {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#examples)

-------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#html)

html

    <template id="tabbed-custom-element">
      <style>
        *,
        ::before,
        ::after {
          box-sizing: border-box;
          padding: 1rem;
        }
        :host {
          display: flex;
        }
      </style>
      <div part="tab active">Tab A</div>
      <div part="tab">Tab B</div>
      <div part="tab">Tab C</div>
    </template>
    
    <tabbed-custom-element></tabbed-custom-element>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#css)

css

    tabbed-custom-element::part(tab) {
      color: blue;
      border-bottom: transparent solid 4px;
    }
    
    tabbed-custom-element::part(tab):hover {
      background-color: black;
      color: white;
    }
    
    tabbed-custom-element::part(tab active) {
      border-color: blue !important;
    }
    

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#javascript)

js

    const template = document.querySelector("#tabbed-custom-element");
    globalThis.customElements.define(
      template.id,
      class extends HTMLElement {
        constructor() {
          super().attachShadow({ mode: "open" }).append(template.content);
        }
      },
    );
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shadow Module Level 1  <br>\# part](https://drafts.csswg.org/css-shadow/#part) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part#see_also)

-------------------------------------------------------------------------------------------------

*   [`part`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/part)
     attribute
*   [`:state()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state)
     pseudo-class function
*   [`exportparts`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts)
     attribute
*   [CSS shadow parts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_part/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_part (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Apart&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_part%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Apart%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_part%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")