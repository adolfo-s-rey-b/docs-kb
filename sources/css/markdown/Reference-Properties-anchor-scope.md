*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#mdn-search)
    

`anchor-scope` CSS property
===========================

Baseline 2026

Newly available

Since January 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/245)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`anchor-scope`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property can be used to limit the scope in which a positioned element can be associated with anchor elements to a particular subtree.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Single values */
    anchor-scope: none;
    anchor-scope: all;
    anchor-scope: --anchor-name;
    
    /* Multiple <dashed-ident> values */
    anchor-scope: --anchor-name, --another-name;
    
    /* Global values */
    anchor-scope: inherit;
    anchor-scope: initial;
    anchor-scope: revert;
    anchor-scope: revert-layer;
    anchor-scope: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#values)

This property is specified as the keyword `none` or `all` or a comma-separated list of `<dashed-ident>` values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#none)

No anchor scope limiting happens on an element. This is the default value.

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#all)

Sets the scope so that _any_ `anchor-name` values set in the subtree can only be bound to by positioned elements in the same subtree.

[`<dashed-ident>#`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

One or more comma-separated [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
s representing anchor names. Sets the scope so that the specified `anchor-name` values, when set in the subtree, can only be bound to by positioned elements in the same subtree.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#description)

--------------------------------------------------------------------------------------------------------------

When multiple [anchor elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#associating_anchor_and_positioned_elements)
 on a page are given the same [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 value and a positioned element is associated with that anchor name (by specifying the name as its [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 property value), the positioned element will be associated with the _last_ anchor element in the source order with that anchor name.

This can be a problem in certain situations. For example, if a document contains multiple repeated components, each with a positioned element tethered to an anchor, all the positioned elements will be anchored to the last anchor on the page unless each component uses a different anchor name. This is likely not the desired behavior.

The `anchor-scope` property can fix this problem by limiting the visibility, or "scope", of an `anchor-name` value to a specific subtree. The result is that each positioned element can only be anchored to an element within the same subtree of the element that has the scope set on it.

*   `anchor-scope: all` sets the scope so that _any_ `anchor-name` values set in the subtree can only be bound to by positioned elements in the same subtree. Let's say we include multiple anchors in a document, all with `anchor-name: --my-anchor` set on them, and place them in separate containers. We will then set `anchor-scope: all` on each container. If we then include a positioned element inside one of the containers and give it `--my-anchor` as the value of its `position-anchor` property, it will be positioned relative to the anchor inside the same container.
    
    Furthermore, if we create another positioned element outside the containers and give it the same anchor name, or a different anchor name, it will not be anchor-positioned relative to any of the anchors, regardless of whether the anchors have those anchor names included inside their `anchor-name` values. `anchor-scope: all` limits the anchor scope for containers it is set on for _any_ anchors, regardless of `anchor-name`, to only positioned elements inside the same containers.
    
*   `anchor-scope: <dashed-ident>#` sets the scope so that the specified `anchor-name` values, when set in the subtree, can only be bound to by positioned elements in the same subtree. If we return to the same example described in the previous bullet, but change the `anchor-scope` value set on the containers to `--my-anchor`:
    
    *   Positioned elements with `position-anchor: --my-anchor` set on them will be limited to the scope imposed by the `anchor-scope` setting. They will only be positioned relative to the anchors if they are placed inside the containers.
        
    *   However, positioned elements with different `position-anchor` names — for example, `--another-anchor` — _can_ be positioned relative to one of the anchors, whether it is placed inside or outside the containers, provided you add the `--another-anchor` anchor name to the anchor's `anchor-name` property. The `anchor-scope` property only limits the scope for the `--my-anchor` anchor name, so it will have no effect on other anchor names.
        
        If multiple anchors are given the `--another-anchor` anchor name, the positioned elements with that `position-anchor` value will be positioned relative to the last anchor in the source order with that name.
        
*   `anchor-scope: none` is the default value, which specifies that no anchor scope is set. If multiple anchors exist in a document with the same `anchor-name`, and a positioned element is given this name as the value of its `position-anchor` property, it will be positioned relative to the last anchor element in the source order, regardless of where it is placed in the DOM hierarchy.
    

If you have, for example, three `anchor-name` values set inside a subtree (say, `--anchor1`, `--anchor2`, and `--anchor3`), setting `anchor-scope: --anchor1, --anchor2, --anchor3` on the top-level element of the subtree would be equivalent to setting `anchor-scope: all`.

Anchor scopes only affect [explicit anchor associations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#explicit_css_anchor_association)
, that is, those made between an anchor element with an `anchor-name` set on it, and a positioned element referencing the anchor element's anchor name in its `position-anchor` value. Anchor scopes do not affect [implicit anchor associations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#implicit_anchor_association)
.

For more information on anchor features and usage, see the [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 module and the [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
 guide.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#formal_syntax)

------------------------------------------------------------------------------------------------------------------

anchor-scope =   
  none            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  all             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor-name>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<anchor-name> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#examples)

--------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#basic_usage)

This example demonstrates how anchor scope works at a basic level. It shows how an anchor element inside a scoped container can be limited to only having positioned elements inside the same scoped container tethered to it.

#### HTML

We specify a [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element that we will set an anchor scope on. This contains two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, one to be turned into an anchor, and one to be an anchor-positioned element.

We also include a third `<div>` outside the `<section>`, which we will also turn into an anchor-positioned element.

html

    <section class="scoped">
      <div class="anchor">⚓︎</div>
      <div class="positioned">Positioned 1</div>
    </section>
    
    <div class="positioned">Positioned 2</div>
    

#### CSS

We first set `anchor-scope: --my-anchor` on the `<section>`. This limits its scope so that anchor element descendants of the `<section>` with a name of `--my-anchor` can only be bound to by positioned elements that are also descendants of the `<section>`.

To test this out, we declare the `anchor` `<div>` as an anchor element by setting an [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 of `--my-anchor` on it. We then absolutely position the `.positioned` elements, tether them to the anchor by setting their [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 values to `--my-anchor`, and position them to the right of the anchor by setting their [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 values to `right`:

    .scoped {
      padding: 20px;
      background: #eeeeee;
    }
    
    .anchor {
      font-size: 1.8rem;
      color: white;
      text-shadow: 1px 1px 1px black;
      background-color: blue;
      width: fit-content;
      padding: 3px;
    }
    
    .positioned {
      background: orange;
      width: fit-content;
      padding: 3px;
    }
    

css

    .scoped {
      anchor-scope: --my-anchor;
    }
    
    .anchor {
      anchor-name: --my-anchor;
    }
    
    .positioned {
      position: absolute;
      position-anchor: --my-anchor;
      position-area: right;
    }
    

#### Result

The example renders like so:

Note how the first positioned element is positioned to the right of the anchor. It is in scope for positioning relative to the `--my-anchor` anchor, as it is inside the `<section>` element where the `anchor-scope: --my-anchor` is set.

However, the second positioned element is not positioned relative to the anchor. It is not a descendant of the `<section>` element, so it is outside the anchor scope.

### [Comparing different `anchor-scope` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#comparing_different_anchor-scope_values)

This example demonstrates the effects of the different `anchor-scope` values by allowing you to apply different `anchor-scope` values to multiple containers, all containing anchors with the same `anchor-name` value.

#### HTML

We specify three [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 elements that we will set an anchor scope on. Each `<section>` contains two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, one to be turned into an anchor, and one to be an anchor-positioned element.

We also include an additional `<div>` outside the `<section>` elements, which we will also turn into an anchor-positioned element. This will have different anchor positioning settings from the others.

Finally, we include a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 containing three different [`<input type="radio">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)
 elements to allow different `anchor-scope` values to be set on the `<section>` elements.

html

    <section class="scoped">
      <div class="anchor">⚓︎</div>
      <div class="positioned">Positioned 1</div>
    </section>
    
    <section class="scoped">
      <div class="anchor">⚓︎</div>
      <div class="positioned">Positioned 2</div>
    </section>
    
    <section class="scoped">
      <div class="anchor">⚓︎</div>
      <div class="positioned">Positioned 3</div>
    </section>
    
    <div class="positioned2">Positioned 4</div>
    
    <form>
      <fieldset>
        <legend>Select an <code>anchor-scope</code> value</legend>
    
        <input type="radio" id="all" name="scope" value="all" checked />
        <label for="all"><code>all</code></label>
        <input type="radio" id="my-anchor" name="scope" value="--my-anchor" />
        <label for="my-anchor"><code>--my-anchor</code></label>
        <input type="radio" id="none" name="scope" value="none" />
        <label for="none"><code>none</code></label>
      </fieldset>
    </form>
    

#### CSS

We start by specifying our anchor elements as anchors by giving them two [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 values: `--my-anchor` and `--another-anchor`.

    body {
      display: flex;
      justify-content: center;
      gap: 50px;
      margin-top: 5px;
    }
    
    .scoped {
      padding: 20px;
      background: #eeeeee;
      border: 2px solid #dddddd;
      border-radius: 10px;
      width: 100px;
      height: 100px;
    }
    
    .anchor {
      font-size: 1.8rem;
      color: white;
      text-shadow: 1px 1px 1px black;
      background-color: blue;
      width: fit-content;
      padding: 3px;
    }
    
    .positioned,
    .positioned2 {
      border: 1px solid black;
      border-radius: 3px;
      width: fit-content;
      padding: 3px 6px;
      box-shadow: 3px 3px 3px rgb(0 0 0 / 0.2);
    }
    
    form {
      position: absolute;
      bottom: 5px;
      right: 5px;
    }
    

css

    .anchor {
      anchor-name: --my-anchor, --another-anchor;
    }
    

Next, we position our `.positioned` elements relative to an anchor element. We absolutely position them, give them a [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 value of `--my-anchor` to associate them with an anchor, and position them relative to the anchor with a [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 value of `right`.

The `.positioned2` element is positioned in a similar way, except that it is given the other available anchor name as its `position-anchor` value — `--another-anchor` — and it is positioned to the `bottom` of the anchor instead. We also give it a [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
 value of `5px`, so that if the anchor positioning is not working, it will be positioned to the bottom of the `<body>`. This element is not contained inside any scoped element, therefore it will only be anchor positioned when certain `anchor-scope` values are set on the scoped elements, as explained later on.

css

    .positioned {
      position: absolute;
      position-anchor: --my-anchor;
      position-area: right;
    }
    
    .positioned2 {
      position: absolute;
      bottom: 5px;
      position-anchor: --another-anchor;
      position-area: bottom;
    }
    

We handle setting `anchor-scope` on the `<section>` elements when different radio buttons are pressed using JavaScript, which has been hidden for brevity.

    const sections = document.querySelectorAll("section");
    const form = document.querySelector("form");
    
    function updateScope(val) {
      sections.forEach((section) => (section.style.anchorScope = val));
    }
    
    form.addEventListener("input", (e) => {
      updateScope(e.target.value);
    });
    
    updateScope("all");
    

#### Result

The example renders as follows:

Check out the initial positioning effect applied to the positioned elements with `anchor-scope: all` set on the `<section>` elements, and then try selecting the other available `anchor-scope` values to see what their effect is. You should observe the following:

*   `all`: The scope for positioning elements relative to anchor elements that are descendants of the `<section>` elements is limited to positioned elements that are themselves descendants of the `<section>` elements, regardless of the `anchor-name` value used to associate them. As a result, the positioned elements inside the `<section>` elements ("Positioned 1–3") are anchor-positioned as expected, but the positioned element outside the `<section>` elements ("Positioned 4") is not anchor-positioned. It is out of scope.
*   `--my-anchor`: The scope for positioning elements relative to anchor elements that are descendants of the `<section>` elements is limited to positioned elements that are themselves descendants of the `<section>` elements, only if the `--my-anchor` `anchor-name` is used to associate them. As a result, the positioned elements inside the `<section>` elements ("Positioned 1–3") are anchor-positioned as expected, and the positioned element outside the `<section>` elements ("Positioned 4") is also anchor-positioned as expected. In the former case, the positioned elements are inside the set scope, and in the latter case, the positioned element is not affected by the set scope, as it is using an anchor name outside the scope (`--another-anchor`). The "Positioned 4" element is positioned relative to the last anchor element in the source that has the matching anchor name.
*   `none`: As no anchor scope is set on the `<section>` elements, all of the positioned elements are positioned relative to the last anchor element in the source order.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Anchor Positioning Module Level 1  <br>\# propdef-anchor-scope](https://drafts.csswg.org/css-anchor-position-1/#propdef-anchor-scope) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope#see_also)

--------------------------------------------------------------------------------------------------------

*   [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
    
*   [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
    
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module
*   [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
     guide

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/anchor-scope/index.md?plain=1 "Folder: en-us/web/css/reference/properties/anchor-scope (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanchor-scope&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanchor-scope%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanchor-scope%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanchor-scope%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")