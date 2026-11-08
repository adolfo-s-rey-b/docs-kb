*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts#mdn-search)
    

`exportparts` HTML global attribute
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`exportparts`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 allows you to select and style elements existing in nested [shadow trees](https://developer.mozilla.org/en-US/docs/Glossary/Shadow_tree)
, by exporting their `part` names.

The shadow tree is an isolated structure where identifiers, classes, and styles cannot be reached by selectors or queries belonging to a regular DOM. There are two HTML attributes that can be applied to shadow tree elements that enable targeting CSS styles from outside to shadow tree: `part` and `exportparts`.

The global [`part`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/part)
 attribute makes a shadow tree element visible to its parent DOM. A `part` name is used as the parameter of the [`::part()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
 pseudo-element. In this way, you can apply CSS styles to elements in the shadow tree from outside of it. However, the `::part()` pseudo-element is only visible to the parent DOM. This means that when a shadow tree is nested, the parts are not visible to any ancestors other than the direct parent. The `exportparts` attribute solves this limitation.

The `exportparts` attribute enables shadow tree parts to be visible outside the shadow DOM. This concept is referred to as "exporting". The `exportparts` attribute is placed on the element's _shadow host_, which is the element to which the _shadow tree_ is attached. The value of this attribute is a comma-separated list of `part` names present in the shadow tree. These names are made available to the DOMs outside the current structure.

html

    <template id="ancestor-component">
      <nested-component exportparts="part1, part2, part5"></nested-component>
    </template>
    

When exporting a `part`, you have the option to assign a different name to the part, as shown in the snippet below. The value of the `exportparts` attribute is really a comma-separated list of part-name mappings. So the `exportparts` attribute in the above code snippet is the equivalent of `exportparts="part1:part1, part2:part2, part5:part5`, indicating that each `part` is exported with the same name. In each mapping, the first string specifies the name of the part within the shadow tree, and the second string specifies the name with which the part will be exposed externally.

html

    <template id="ancestor-component">
      <nested-component
        exportparts="part1:exposed1, part2:exposed2"></nested-component>
    </template>
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts#examples)

---------------------------------------------------------------------------------------------------------------

### [Basic component](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts#basic_component)

To demonstrate how `exportparts` is used to enable targeting parts within nested components, we will create a component, and then nest it within another component.

#### HTML

First, let's create a card component that we will then wrap with another component. We also use the new element we created, populating the slots with plain text as content.

html

    <template id="card-component-template">
      <style>
        :host {
          display: block;
        }
      </style>
      <div class="base" part="base">
        <div part="header"><slot name="header_slot"></slot></div>
        <div part="body"><slot name="body_slot"></slot></div>
        <div part="footer"><slot name="footer_slot"></slot></div>
      </div>
    </template>
    
    <card-component>
      <p slot="header_slot">This is the header</p>
      <p slot="body_slot">This is the body</p>
      <p slot="footer_slot">This is the footer</p>
    </card-component>
    

#### JavaScript

We use JavaScript to define our web component defined in the HTML above:

js

    customElements.define(
      "card-component",
      class extends HTMLElement {
        constructor() {
          super(); // Always call super first in constructor
          const template = document.getElementById("card-component-template");
          const shadowRoot = this.attachShadow({
            mode: "open",
          });
          shadowRoot.appendChild(document.importNode(template.content, true));
        }
      },
    );
    

#### CSS

We style parts of the `<card-component>` shadow tree using the [`::part`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
 pseudo-element:

css

    ::part(body) {
      color: red;
      font-style: italic;
    }
    

#### Results

### [Nested component](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts#nested_component)

Continuing the above `<card-component>` example, we create a nested component by wrapping the `<card-component>` within another component; in this case, the `<card-wrapper>` component. We then export the parts from the nested component that we want to make stylable from outside the component's shadow tree with the `exportparts` attribute.

#### HTML

    <template id="card-component-template">
      <style>
        :host {
          display: block;
        }
      </style>
      <div class="base" part="base">
        <div part="header"><slot name="header_slot"></slot></div>
        <div part="body"><slot name="body_slot"></slot></div>
        <div part="footer"><slot name="footer_slot"></slot></div>
      </div>
    </template>
    

html

    <template id="card-wrapper">
      <style>
        :host {
          display: block;
        }
      </style>
      <card-component exportparts="base, header, body">
        <slot name="H" slot="header_slot"></slot>
        <slot name="B" slot="body_slot"></slot>
        <slot name="F" slot="footer_slot"></slot>
      </card-component>
    </template>
    

We include a `<card-wrapper>` custom element, and a `<card-component>` for comparison:

html

    <h2>Card wrapper</h2>
    
    <card-wrapper>
      <p slot="H">This is the header</p>
      <p slot="B">This is the body</p>
      <p slot="F">This is the footer</p>
    </card-wrapper>
    
    <h2>Card component</h2>
    
    <card-component>
      <p slot="header_slot">This is the header</p>
      <p slot="body_slot">This is the body</p>
      <p slot="footer_slot">This is the footer</p>
    </card-component>
    

#### JavaScript

    customElements.define(
      "card-component",
      class extends HTMLElement {
        constructor() {
          super(); // Always call super first in constructor
          const template = document.getElementById("card-component-template");
          const shadowRoot = this.attachShadow({
            mode: "open",
          });
          shadowRoot.appendChild(document.importNode(template.content, true));
        }
      },
    );
    

js

    customElements.define(
      "card-wrapper",
      class extends HTMLElement {
        constructor() {
          super(); // Always call super first in constructor
          const template = document.getElementById("card-wrapper");
          const shadowRoot = this.attachShadow({
            mode: "open",
          });
          shadowRoot.appendChild(document.importNode(template.content, true));
        }
      },
    );
    

#### CSS

Now, we can target parts of the `<card-component>` directly and when nested within a `<card-wrapper>` like so:

css

    h2 {
      background-color: #dedede;
    }
    
    card-wrapper,
    card-component {
      border: 1px dashed blue;
      width: fit-content;
    }
    
    ::part(body) {
      color: red;
      font-style: italic;
    }
    
    ::part(header),
    ::part(footer) {
      font-weight: bold;
    }
    

#### Results

Note `footer` is not bold when nested, as we did not include it in `exportparts`.

### [Exposing mapped parts](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts#exposing_mapped_parts)

To rename exported parts, we include a comma-separated list of mapped parts, with each mapped part including the original name and exported name separated by a colon (`:`):

#### HTML

We update the prior `<card-wrapper>` custom element with the remapping syntax (omitting `body` from the exported parts list):

    <template id="card-component-template">
      <div class="base" part="base">
        <div part="header"><slot name="header_slot"></slot></div>
        <div part="body"><slot name="body_slot"></slot></div>
        <div part="footer"><slot name="footer_slot"></slot></div>
      </div>
    </template>
    
    <card-wrapper>
      <p slot="H">This is the header</p>
      <p slot="B">This is the body</p>
      <p slot="F">This is the footer</p>
    </card-wrapper>
    

html

    <template id="card-wrapper">
      <card-component
        exportparts="
           base:card__base,
           header:card__header,
           footer:card__footer
         ">
        <span slot="header_slot"><slot name="H"></slot></span>
        <span slot="body_slot"><slot name="B"></slot></span>
        <span slot="footer_slot"><slot name="F"></slot></span>
      </card-component>
    </template>
    

#### JavaScript

    customElements.define(
      "card-component",
      class extends HTMLElement {
        constructor() {
          super(); // Always call super first in constructor
          const template = document.getElementById("card-component-template");
          const shadowRoot = this.attachShadow({
            mode: "open",
          });
          shadowRoot.appendChild(document.importNode(template.content, true));
        }
      },
    );
    

js

    customElements.define(
      "card-wrapper",
      class extends HTMLElement {
        constructor() {
          super(); // Always call super first in constructor
          const template = document.getElementById("card-wrapper");
          const shadowRoot = this.attachShadow({
            mode: "open",
          });
          shadowRoot.appendChild(document.importNode(template.content, true));
        }
      },
    );
    

#### CSS

In targeting the parts of the `<card-component>` from within the `<card-wrapper>`, we can only style the exported parts via their exposed part names:

css

    /* selects the exported parts name */
    ::part(card__header) {
      font-weight: bold;
    }
    /* selects nothing: these part names were not exported */
    ::part(footer),
    ::part(body) {
      font-weight: bold;
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shadow Module Level 1  <br>\# element-attrdef-html-global-exportparts](https://drafts.csswg.org/css-shadow/#element-attrdef-html-global-exportparts) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`part`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/part)
     HTML attribute
*   [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)
     and [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
     HTML elements
*   [`::part`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
     and [`::slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)
     pseudo-elements
*   [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
     pseudo-class
*   [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
     interface
*   [`Element.part`](https://developer.mozilla.org/en-US/docs/Web/API/Element/part)
     property
*   [Using templates and slots](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_templates_and_slots)
    
*   [CSS scoping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/exportparts/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/exportparts (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fexportparts&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fexportparts%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fexportparts%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fexportparts%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")