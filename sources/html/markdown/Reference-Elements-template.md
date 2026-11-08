*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#mdn-search)
    

`<template>` HTML content template element
==========================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since November 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<template>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element serves as a mechanism for holding [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML)
 fragments, which can either be used later via JavaScript, generated immediately and inserted into a shadow DOM, or used as part of [out-of-order patching](https://developer.mozilla.org/en-US/docs/Glossary/out_of_order_patching)
 with `<template for="...">`.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#attributes)

-------------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`for`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#for)

The `for` attribute is used for out-of-order patching with `<template for="...">`, matching an equivalent `<?start id="...">` or `<?marker "...">` marker. See the [out-of-order patching section](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#out-of-order_patching)
 and [examples section](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#examples)
.

[`shadowrootmode`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootmode)

Creates a [shadow root](https://developer.mozilla.org/en-US/docs/Glossary/Shadow_tree)
 for the parent element. It is a declarative version of the [`Element.attachShadow()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow)
 method and accepts the same [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values.

[`open`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#open)

Exposes the internal shadow root DOM for JavaScript (recommended for most use cases).

[`closed`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#closed)

Hides the internal shadow root DOM from JavaScript.

**Note:** The HTML parser creates a [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
 object in the DOM for the first `<template>` in a node with this attribute set to an allowed value. If the attribute is not set, or not set to an allowed value — or if a `ShadowRoot` has already been declaratively created in the same parent — then an [`HTMLTemplateElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement)
 is constructed. A [`HTMLTemplateElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement)
 cannot subsequently be changed into a shadow root after parsing, for example, by setting [`HTMLTemplateElement.shadowRootMode`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement/shadowRootMode)
.

**Note:** You may find the non-standard `shadowroot` attribute in older tutorials and examples that used to be supported in Chrome 90-110. This attribute has since been removed and replaced by the standard `shadowrootmode` attribute.

[`shadowrootclonable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootclonable)

Sets the value of the [`clonable`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/clonable)
 property of a [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
 created using this element to `true`. If set, a clone of the shadow host (the parent element of this `<template>`) created with [`Node.cloneNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/cloneNode)
 or [`Document.importNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/importNode)
 will include a shadow root in the copy.

[`shadowrootcustomelementregistry`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootcustomelementregistry)

Sets the [`customElementRegistry`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/customElementRegistry)
 property of a [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
 created using this element to `null`, rather than the document's [custom element registry](https://developer.mozilla.org/en-US/docs/Web/API/Document/customElementRegistry)
. This allows a scoped [`CustomElementRegistry`](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry)
 to be attached later using [`CustomElementRegistry.initialize()`](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry/initialize)
.

[`shadowrootdelegatesfocus`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootdelegatesfocus)

Sets the value of the [`delegatesFocus`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/delegatesFocus)
 property of a [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
 created using this element to `true`. If this is set and a non-focusable element in the shadow tree is selected, then focus is delegated to the first focusable element in the tree. The value defaults to `false`.

[`shadowrootreferencetarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootreferencetarget)

Sets the value of the `referenceTarget` property of a [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
 created using this element. The value should be the ID of an element inside the shadow DOM. If set, target references to the host element from outside the shadow DOM will cause the referenced target element to become the effective target of the reference to the host element.

[`shadowrootserializable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootserializable)

Sets the value of the [`serializable`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/serializable)
 property of a [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
 created using this element to `true`. If set, the shadow root may be serialized by calling the [`Element.getHTML()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getHTML)
 or [`ShadowRoot.getHTML()`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/getHTML)
 methods with the `options.serializableShadowRoots` parameter set `true`. The value defaults to `false`.

[`shadowrootslotassignment`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootslotassignment)

Sets the [`slotAssignment`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot/slotAssignment)
 property of a [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
 created using this element. This is the declarative equivalent of the [`slotAssignment`](https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow#slotassignment)
 option of the [`Element.attachShadow()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow)
 method.

[`named`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#named)

Elements are automatically assigned to [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
 elements within this shadow root. This is the default value.

Elements with the [`slot` attribute](https://developer.mozilla.org/en-US/docs/Web/API/Element/slot)
 are assigned to the first [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
 in the template that has the corresponding `name` attribute. If multiple elements specify the same slot name, they are all added to the first slot in the template that has that name, and rendered in the order they are declared. All unnamed elements — elements that don't specify a `slot` attribute — are assigned to the default slot in the order they are declared. This is the first unnamed `<slot>` in the template.

[`manual`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#manual)

Elements are manually assigned to particular slot elements using [`HTMLSlotElement.assign()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSlotElement/assign)
. No automatic assignment takes place.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#usage_notes)

---------------------------------------------------------------------------------------------------------

This element has no permitted content, because everything nested inside it in the HTML source does not actually become the children of the `<template>` element. The [`Node.childNodes`](https://developer.mozilla.org/en-US/docs/Web/API/Node/childNodes)
 property of the `<template>` element is always empty, and you can only access said nested content via the special [`content`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement/content "content")
 property. However, if you call [`Node.appendChild()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)
 or similar methods on the `<template>` element, then you would be inserting children into the `<template>` element itself, which is a violation of its content model and does not actually update the [`DocumentFragment`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment)
 returned by the `content` property.

Due to the way the `<template>` element is parsed, all `<html>`, `<head>`, and `<body>` opening and closing tags inside the template are syntax errors and are ignored by the parser, so `<template><head><title>Test</title></head></template>` is the same as `<template><title>Test</title></template>`.

There are three main ways to use the `<template>` element.

### [Template document fragment](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#template_document_fragment)

By default, the element's content is not rendered. The corresponding [`HTMLTemplateElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement)
 interface includes a standard [`content`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement/content "content")
 property (without an equivalent content/markup attribute). This `content` property is read-only and holds a [`DocumentFragment`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment)
 that contains the DOM subtree represented by the template.

The [`Node.cloneNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/cloneNode)
 and [`Document.importNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/importNode)
 methods both create a copy of a node. The difference is that `importNode()` clones the node in the context of the calling document, whereas `cloneNode()` uses the document of the node being cloned. The document context determines the [`CustomElementRegistry`](https://developer.mozilla.org/en-US/docs/Web/API/CustomElementRegistry)
 for constructing any custom elements. For this reason, use `document.importNode()` to clone the `content` fragment so that custom element descendants are constructed using the definitions in the current document, rather than the separate document that owns the template content. See the [`Node.cloneNode()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/cloneNode)
 page's examples for more details.

Note that the `DocumentFragment` container itself should not have data attached to it. See the [Data on the DocumentFragment is not cloned](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#data_on_the_documentfragment_is_not_cloned)
 example for more details.

### [Declarative Shadow DOM](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#declarative_shadow_dom)

If the `<template>` element contains the [`shadowrootmode`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#shadowrootmode)
 attribute with a value of either `open` or `closed`, the HTML parser will immediately generate a shadow DOM. The element is replaced in the DOM by its content wrapped in a [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
, which is attached to the parent element. This is the declarative equivalent of calling [`Element.attachShadow()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/attachShadow)
 to attach a shadow root to an element.

If the element has any other value for `shadowrootmode`, or does not have the `shadowrootmode` attribute, the parser generates a [`HTMLTemplateElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement)
. Similarly, if there are multiple declarative shadow roots, only the first one is replaced by a [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
 — subsequent instances are parsed as [`HTMLTemplateElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement)
 objects.

Other attributes prefixed with `shadowroot` allow declarative customization of the `ShadowRoot`, such as controlling how slots are assigned.

### [Out-of-order patching](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#out-of-order_patching)

**Note:** This use case is still experimental and has limited browser support. See the [browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#browser_compatibility)
 table for browser support information.

Traditionally, HTML is delivered in order and read, processed, and displayed from top to bottom. To change that order, you can either hide or rearrange elements with CSS or update the DOM produced by the HTML afterwards with JavaScript. However, many pages are composed of multiple parts that may be ready to render at different times, or that may be more important to deliver to the user earlier.

The `<template>` element allows for delivering HTML [out-of-order](https://developer.mozilla.org/en-US/docs/Glossary/out_of_order_patching)
, which involves replacing [processing instruction](https://developer.mozilla.org/en-US/docs/Web/API/ProcessingInstruction)
 markers with the contents of the `<template>` element (also referred to as **patching**).

For example, a `<?marker name="my-identifier">` processing instruction marker can be patched with the contents of a `<template for="my-identifier">` element supplied much later in the HTML. See the [Using `<template for>` for patching](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#using_template_for_for_patching)
 example.

As well as the `<?marker>` processing instructions marker, a `<?start>` and `<?end>` pair can be used to contain temporary content (for example, `<?start name="my-identifier">Loading...<?end>`), which is temporarily shown until the `<template for="my-identifier">` is processed and the whole section is replaced. See the [Using `<template for>` for range patching](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#using_template_for_for_range_patching)
 example.

When written in HTML, processing instructions can be provided with or without the trailing `?`, and the browser will add it if not supplied when parsing the DOM. Both `<?start?>` and `<?start>` are therefore valid and parsed as `<?start?>`. XML is stricter and requires the trailing `?`.

If the `for` attribute does not match any marker processing instruction `name`, the `<template>` content will remain hidden in the DOM and won't be used in any patch.

To prevent components from updating unrelated parts of the DOM, `<template for="...">` elements can only patch markers inside the `<template>` parent's DOM tree. The only exception is `<template>` elements that are direct children of the `<body>` element — they can also patch `<head>` elements to allow updating `<title>` and other `<head>` elements.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#examples)

---------------------------------------------------------------------------------------------------

### [Generating table rows](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#generating_table_rows)

First we start with the HTML portion of the example.

html

    <table id="producttable">
      <thead>
        <tr>
          <th>UPC_Code</th>
          <th>Product_Name</th>
        </tr>
      </thead>
      <tbody>
        <!-- existing data could optionally be included here -->
      </tbody>
    </table>
    
    <template id="productrow">
      <tr>
        <td class="record"></td>
        <td></td>
      </tr>
    </template>
    

First, we have a table into which we will later insert content using JavaScript code. Then comes the template, which describes the structure of an HTML fragment representing a single table row.

Now that the table has been created and the template defined, we use JavaScript to insert rows into the table, with each row being constructed using the template as its basis.

js

    // Instantiate the table with the existing HTML tbody
    // and the row with the template
    const tbody = document.querySelector("tbody");
    const template = document.querySelector("#productrow");
    
    // Clone the new row and insert it into the table
    const clone = document.importNode(template.content, true);
    let td = clone.querySelectorAll("td");
    td[0].textContent = "1235646565";
    td[1].textContent = "Stuff";
    
    tbody.appendChild(clone);
    
    // Clone the new row and insert it into the table
    const clone2 = document.importNode(template.content, true);
    td = clone2.querySelectorAll("td");
    td[0].textContent = "0384928528";
    td[1].textContent = "Acme Kidney Beans 2";
    
    tbody.appendChild(clone2);
    

The result is the original HTML table, with two new rows appended to it via JavaScript:

    table {
      background: black;
    }
    
    table th,
    table td {
      background: white;
    }
    

### [Implementing a declarative shadow DOM](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#implementing_a_declarative_shadow_dom)

In this example, a hidden support warning is included at the beginning of the markup. This warning is later set to be displayed via JavaScript if the browser doesn't support the `shadowrootmode` attribute. Next, there are two [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 elements, each containing nested [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)
 elements with different behaviors. The first `<style>` element is global to the whole document. The second one is scoped to the shadow root generated in place of the `<template>` element because of the presence of the `shadowrootmode` attribute.

html

    <p hidden>
      ⛔ Your browser doesn't support <code>shadowrootmode</code> attribute yet.
    </p>
    <article>
      <style>
        p {
          padding: 8px;
          background-color: wheat;
        }
      </style>
      <p>I'm in the DOM.</p>
    </article>
    <article>
      <template shadowrootmode="open">
        <style>
          p {
            padding: 8px;
            background-color: plum;
          }
        </style>
        <p>I'm in the shadow DOM.</p>
      </template>
    </article>
    

js

    const isShadowRootModeSupported = Object.hasOwn(
      HTMLTemplateElement.prototype,
      "shadowRootMode",
    );
    
    document
      .querySelector("p[hidden]")
      .toggleAttribute("hidden", isShadowRootModeSupported);
    

### [Declarative Shadow DOM with delegated focus](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#declarative_shadow_dom_with_delegated_focus)

This example demonstrates how `shadowrootdelegatesfocus` is applied to a shadow root that is created declaratively, and the effect this has on focus.

The code first declares a shadow root inside a `<div>` element, using the `<template>` element with the `shadowrootmode` attribute. This displays both a non-focusable `<div>` containing text and a focusable `<input>` element. It also uses CSS to style elements with [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
 to blue, and to set the normal styling of the host element.

html

    <div>
      <template shadowrootmode="open">
        <style>
          :host {
            display: block;
            border: 1px dotted black;
            padding: 10px;
            margin: 10px;
          }
          :focus {
            outline: 2px solid blue;
          }
        </style>
        <div>Clickable Shadow DOM text</div>
        <input type="text" placeholder="Input inside Shadow DOM" />
      </template>
    </div>
    

The second code block is identical except that it sets the `shadowrootdelegatesfocus` attribute, which delegates focus to the first focusable element in the tree if a non-focusable element in the tree is selected.

html

    <div>
      <template shadowrootmode="open" shadowrootdelegatesfocus>
        <style>
          :host {
            display: block;
            border: 1px dotted black;
            padding: 10px;
            margin: 10px;
          }
          :focus {
            outline: 2px solid blue;
          }
        </style>
        <div>Clickable Shadow DOM text</div>
        <input type="text" placeholder="Input inside Shadow DOM" />
      </template>
    </div>
    

Last of all we use the following CSS to apply a red border to the parent `<div>` element when it has focus.

css

    div:focus {
      border: 2px solid red;
    }
    

The results are shown below. When the HTML is first rendered, the elements have no styling, as shown in the first image. For the shadow root that does not have `shadowrootdelegatesfocus` set you can click anywhere except the `<input>` and the focus does not change (if you select the `<input>` element it will look like the second image).

![Screenshot of code with no focus set](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template/template_with_no_focus.png)

For the shadow root with `shadowrootdelegatesfocus` set, clicking on the text (which is non-focusable) selects the `<input>` element, as this is the first focusable element in the tree. This also focuses the parent element as shown below.

![Screenshot of the code where the element has focus](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template/template_with_focus.png)

### [Declarative shadow DOM with named slot assignment](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#declarative_shadow_dom_with_named_slot_assignment)

This example shows how elements can be assigned to slots in a shadow DOM based on their [`slot` attribute](https://developer.mozilla.org/en-US/docs/Web/API/Element/slot)
 (matched against the slot's `name` attribute).

#### HTML

First we define an [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 element that presents title, metadata, and article body information.

The article contains a `<template>` element that will become a shadow root, because of the presence of the `shadowrootmode` attribute. We don't need to set its `shadowrootslotassignment` attribute because named slot assignment is the default.

The template defines elements that have named slots for "header" and "meta" information, and an unnamed slot for "body" information. The elements are styled differently so it is easy to differentiate them.

html

    <article id="host">
      <template shadowrootmode="open" shadowrootslotassignment="named">
        <style>
          .header {
            background-color: plum;
          }
          .meta {
            background-color: green;
          }
          .body {
            background-color: lightblue;
          }
        </style>
    
        <h2 class="header">
          <slot name="title"></slot>
        </h2>
    
        <div class="meta">
          <slot name="meta"></slot>
        </div>
    
        <div class="body">
          <slot></slot>
        </div>
      </template>
    
      <p>
        Text 1 with no slot attribute. Goes into default (unnamed) slot inside the
        "body" div.
      </p>
      <span slot="title">Text for the title slot</span>
      <span slot="meta">Text for the meta slot</span>
      <p>
        Text 2 with no slot attribute. Also goes into default (unnamed) slot inside
        the "body" div.
      </p>
    </article>
    

Inside the same host, below the template, we have four elements for populating the slots. The [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 elements have `slot` attributes that match the `name` attributes on slots in the template, and will populate the corresponding slots. The two [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 elements are unnamed, so are both inserted into the unnamed `<slot>` in the "body" element.

#### Results

The example below should show the content of the slots displayed in the appropriate sections.

### [Declarative shadow DOM with manual slot assignment](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#declarative_shadow_dom_with_manual_slot_assignment)

This example shows how elements can be assigned to slots in a shadow DOM using manual slot assignment.

With this approach, each element must manually be assigned to a particular slot. There is no default assignment, so any slot that is not assigned will be empty.

#### HTML

First we have a hidden support warning. This warning is later set to be displayed via JavaScript if the browser doesn't support the `shadowrootslotassignment` attribute.

html

    <p id="support-warning" hidden>
      ⛔ Your browser doesn't support the
      <code>shadowrootslotassignment</code> attribute yet.
    </p>
    

Next, we define an [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 element that presents title, metadata, and article body information. This contains a `<template>` element that will become a shadow root, because of the presence of the `shadowrootmode` attribute, and will use manual slot assignment because `shadowrootslotassignment="manual"` is set.

The template defines elements that have slots for "header", "meta", and "body" information, that can be separately referenced by their `id` attribute. The elements are styled differently so it is easy to differentiate them.

html

    <article id="host">
      <template shadowrootmode="open" shadowrootslotassignment="manual">
        <style>
          .header {
            background-color: plum;
          }
          .meta {
            background-color: green;
          }
          .body {
            background-color: lightblue;
          }
        </style>
    
        <h2 class="header">
          <slot id="titleSlot"></slot>
        </h2>
    
        <div class="meta">
          <slot id="metaSlot"></slot>
        </div>
    
        <div class="body">
          <slot id="bodySlot"></slot>
        </div>
      </template>
    
      <span id="text_title">Text for the title slot</span>
      <span id="text_meta">Text for the meta slot</span>
      <p id="text_body_1">Text 1 for body slot.</p>
      <p id="text_body_2">Text 2 for body slot.</p>
    </article>
    

Inside the same host, below the template, we have four elements for populating the slots. These are also identified by id.

#### JavaScript

The JavaScript for manual slot assignment is shown below. First the code gets the slots within the shadow root, then the text to be inserted, and finally assigns the text to the slot. Note that you can only assign a node once to any particular slot, and that if you assign multiple nodes to a single slot using [`HTMLSlotElement.assign()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSlotElement/assign)
, the order they are specified controls the order they are added.

js

    const host = document.querySelector("#host");
    const shadow = host.shadowRoot;
    
    // 1. Target your slots
    const titleSlot = shadow.querySelector("#titleSlot");
    const metaSlot = shadow.querySelector("#metaSlot");
    const bodySlot = shadow.querySelector("#bodySlot");
    
    // 2. Target the Elements to slot
    const body1Text = document.querySelector("#text_body_1");
    const body2Text = document.querySelector("#text_body_2");
    const titleText = document.querySelector("#text_title");
    const metaText = document.querySelector("#text_meta");
    
    // 3. Manually assign them
    titleSlot.assign(titleText);
    metaSlot.assign(metaText);
    bodySlot.assign(body2Text, body1Text);
    

The code displays the hidden support warning if slot assignment is not supported.

js

    const isShadowRootSlotAssignmentSupported = Object.hasOwn(
      HTMLTemplateElement.prototype,
      "shadowRootSlotAssignment",
    );
    
    document
      .querySelector("p[hidden]")
      .toggleAttribute("hidden", isShadowRootSlotAssignmentSupported);
    

#### Results

The example below should show the content of the slots displayed in the appropriate sections.

**Note:** If the `shadowrootslotassignment` attribute is not supported, a warning note is displayed and the browser will use `named` assignment. However, because none of the slots or elements to be inserted are named, all the elements will be inserted into the title slot (because this is the first unnamed slot, and hence is the "default" slot).

### [Data on the DocumentFragment is not cloned](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#data_on_the_documentfragment_is_not_cloned)

When a [`DocumentFragment`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment)
 value is passed, [`Node.appendChild`](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild)
 and similar methods move only the _child nodes_ of that value into the target node. Therefore, it is usually preferable to attach event handlers to the children of a `DocumentFragment`, rather than to the `DocumentFragment` itself.

Consider the following HTML and JavaScript:

#### HTML

html

    <div id="container"></div>
    
    <template id="template">
      <div>Click me</div>
    </template>
    

#### JavaScript

js

    const container = document.getElementById("container");
    const template = document.getElementById("template");
    
    function clickHandler(event) {
      event.target.append(" — Clicked this div");
    }
    
    const firstClone = document.importNode(template.content, true);
    firstClone.addEventListener("click", clickHandler);
    container.appendChild(firstClone);
    
    const secondClone = document.importNode(template.content, true);
    secondClone.children[0].addEventListener("click", clickHandler);
    container.appendChild(secondClone);
    

#### Result

Since `firstClone` is a `DocumentFragment`, only its children are added to `container` when `appendChild` is called; the event handlers of `firstClone` are not copied. In contrast, because an event handler is added to the first _child node_ of `secondClone`, the event handler is copied when `appendChild` is called, and clicking on it works as one would expect.

### [Using `<template for>` for patching](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#using_template_for_for_patching)

This example uses the `<?marker name="placeholder">` processing instruction as a placeholder and later on fills in the contents using `<template for="placeholder">`.

html

    <body>
      <div>
        <?marker name="placeholder">
      </div>
      ...
      <template for="placeholder">Lorem Ipsum...</template>
      ...
    </body>
    

Initially, this results in an empty `<div>` being rendered. It is then updated to the following after the `<template>` element is parsed and processed:

html

      <div>
        Lorem Ipsum...
      </div>
    

### [Using `<template for>` for range patching](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#using_template_for_for_range_patching)

This example uses the `<?start>` and `<?end>` processing instructions to contain placeholder content, which is initially displayed then replaced by the `<template for>` content later on.

html

    <body>
      <div>
        <?start name="placeholder">
        Loading...
        <?end>
      </div>
      ...
      <template for="placeholder">Lorem Ipsum...</template>
      ...
    </body>
    

Initially the `<div>` is rendered with the `Loading...` placeholder content. This is then updated to the following after the `<template>` is parsed and processed:

html

      <div>
        Lorem Ipsum...
      </div>
    

This example also demonstrates the lack of processing instruction children and nesting. The `<?start>` and `<?end>` processing instructions, although linked in terms of their relationship with `<template for>`, are separate [nodes](https://developer.mozilla.org/en-US/docs/Web/API/Node)
 and not opening and closing tags. They therefore do not contain the `Loading...` content as a child (as demonstrated by the lack of indentation).

### [Using `<template for>` for patching `<head>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#using_template_for_for_patching_head_elements)

This example shows that `<template for>` elements that are direct children of the `<body>` element can patch `<head>` markers.

html

    <head>
      ...
      <?start name="title"><title>Loading...</title><?end>
      <?start name="meta-description"><meta name="description" contents="Loading..."><?end>
      ...
    </head>
    <body>
      ...
      <template for="title"><title>The actual title of the page</title></template>
      <template for="meta-description"><meta name="description" contents="This is a meaningful description..."></template>
      ...
    </body>
    

Results in the following once the `<template>` elements have been parsed:

html

    <head>
      ...
      <title>The actual title of the page</title>
      <meta name="description" contents="This is a meaningful description...">
      ...
    </head>
    <body>
      ...
    </body>
    

### [Including markers in `<template for>` to allow contents to be repatched later](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#including_markers_in_template_for_to_allow_contents_to_be_repatched_later)

You can also insert markers inside `<template for>` elements, creating new placeholders to enable patching the same content multiple times. You can reuse existing `name` attributes.

For example, if you are building a [Single Page Application (SPA)](https://developer.mozilla.org/en-US/docs/Glossary/SPA)
 with `<template for>`, you may wish to allow the `<title>` to be patched on each route update, which could be achieved like this:

html

    <head>
      ...
      <?start name="title">
      <title>Loading...</title>
      <?end>
      ...
    </head>
    <body>
      ...
      <template for="title"><?start name="title"><title>The actual title of the page</title><?end></template>
      ...
    </body>
    

This will result in the following once the `<template>` element is parsed:

html

    <head>
      ...
      <?start name="title"><title>The actual title of the page</title><?end>
      ...
    </head>
    <body>
      ...
    </body>
    

Later on, a new `<template for="title">` could be inserted into the DOM to replace the `<title>` again.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#technical_summary)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Metadata content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#metadata_content)<br>, [flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [script-supporting element](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#script-supporting_elements) |
| Permitted content | Nothing (see [Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#usage_notes)<br>) |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [metadata content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#metadata_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, or [script-supporting elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#script-supporting_elements)<br>. Also allowed as a child of a [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)<br> element that does _not_ have a [`span`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup#span)<br> attribute. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLTemplateElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLTemplateElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-template-element](https://html.spec.whatwg.org/multipage/scripting.html#the-template-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template#see_also)

---------------------------------------------------------------------------------------------------

*   [`part`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/part)
     and [`exportparts`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/exportparts)
     HTML attributes
*   [`<slot>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/slot)
     HTML element
*   [`:has-slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has-slotted)
    , [`:host`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host)
    , [`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
    , and [`:host-context()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host-context)
     CSS pseudo-classes
*   [`::part`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
     and [`::slotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::slotted)
     CSS pseudo-elements
*   [`ShadowRoot`](https://developer.mozilla.org/en-US/docs/Web/API/ShadowRoot)
     interface
*   [Using templates and slots](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_templates_and_slots)
    
*   [CSS scoping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping)
     module
*   [Declarative Shadow DOM (with html)](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM#declaratively_with_html)
     in _Using Shadow DOM_
*   [Declarative shadow DOM](https://web.dev/articles/declarative-shadow-dom "External link (opens in new tab)")
     on web.dev (2023)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/template/index.md?plain=1 "Folder: en-us/web/html/reference/elements/template (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftemplate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftemplate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Ftemplate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Ftemplate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F19370346042efad9e179fbf1f55deeeadee98c40%0A*+Document+last+modified%3A+2026-10-12T23%3A34%3A38.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")