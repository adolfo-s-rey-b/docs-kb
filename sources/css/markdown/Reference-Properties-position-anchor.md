*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#mdn-search)
    

`position-anchor` CSS property
==============================

Baseline 2026

Newly available

Since September 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/245)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`position-anchor`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the default **anchor element** for a positioned element. This default is used by [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 and [`position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try)
, and by anchor functions ([`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
 and [`anchor-size()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor-size)
) when no `<anchor-name>` argument is provided to those functions.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Single values */
    position-anchor: normal;
    position-anchor: auto;
    position-anchor: none;
    position-anchor: --anchor-name;
    position-anchor: match-parent;
    
    /* Global values */
    position-anchor: inherit;
    position-anchor: initial;
    position-anchor: revert;
    position-anchor: revert-layer;
    position-anchor: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#values)

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#normal)

If [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 is `none`, it behaves as `none`. Otherwise it behaves as `auto`.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#auto)

Associates a positioned element with its implicit anchor element, if it has one — for example as set by the non-standard HTML [`anchor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor)
 attribute.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#none)

The positioned element is not associated with an anchor element.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

The name of the anchor element to associate the positioned element with, as listed in the anchor element's [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 property. This is known as the **default anchor specifier**.

[`match-parent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#match-parent)

Uses the same default anchor element as the parent element, or the originating element if this is a [pseudo-element](https://developer.mozilla.org/en-US/docs/Glossary/Pseudo-element)
, provided that would be an acceptable anchor element (that is [part of the tree](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements#tree-abiding_pseudo-elements)
). Otherwise, it has no default anchor element.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#description)

-----------------------------------------------------------------------------------------------------------------

This property is only relevant to "positioned" elements — elements and pseudo-elements that have a [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 of `absolute` or `fixed` set.

To position an element relative to an anchor element, the positioned element requires three features: an association, a position, and a location. The `position-anchor` and [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
 properties provide an explicit association.

The anchor element accepts one or more `<dashed-ident>` anchor names set on it via the `anchor-name` property. When one of those names is then set as the value of the positioned element's `position-anchor` property, the two elements are associated.

If there are multiple anchor elements with the anchor name listed in the `position-anchor` property, the positioned element will be associated with the last anchor element in the source order with that anchor name.

To cancel a previously-made association between an anchor-positioned element and an anchor, you can set the anchor-positioned element's `position-anchor` value to `none`.

To tether a positioned element to its anchor, it must be placed relative to an anchor element using an anchor positioning feature, such as the [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
 function (set as a value on [inset properties](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
) or the [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 property.

When positioning elements relative to [implicit anchors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using#implicit_anchor_association)
 using `anchor()`, set `position-anchor: auto` on the anchor-positioned element to opt in to the implicit association. See [Popover anchor positioning](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#popover_anchor_positioning)
 for more information.

If the associated anchor is hidden, for example with [`display: none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 or [`visibility: hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
, or if it is part of the [skipped contents](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#skips_its_contents)
 of another element due to it having [`content-visibility: hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
 set on it, the anchor positioned element will not be displayed.

The `position-anchor` property is supported on all elements that are positioned, including [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 like [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
 and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
. Pseudo elements are implicitly anchored to the same element as the pseudo-element's originating element, unless otherwise specified.

For more information on anchor features and usage, see the [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 module and the [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
 guide.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | absolutely positioned elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

position-anchor =   
  normal         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor-name>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  match-parent     
  
<anchor-name> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#examples)

-----------------------------------------------------------------------------------------------------------

See the `anchor-name` documentation for [basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#basic_usage)
 and additional [`position-anchor` examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#examples)
.

### [Multiple positioned elements and anchors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#multiple_positioned_elements_and_anchors)

In this example, you can move multiple positioned elements around, associating them with different anchors. This example demonstrates how an anchor can be associated with multiple positioned elements, but an anchor-positioned element can only be associated with a single anchor at a time, the anchor defined by the `anchor-position` property.

#### HTML

We have four anchors and two positioned elements, distinguished with different `id` values. The positioned elements contain [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 boxes that allow you to choose which anchor you want to associate them with.

html

    <div id="anchor-container">
      <div class="anchor" id="anchor1">⚓︎</div>
      <div class="anchor" id="anchor2">⚓︎</div>
      <div class="anchor" id="anchor3">⚓︎</div>
      <div class="anchor" id="anchor4">⚓︎</div>
    </div>
    
    <div class="infobox" id="infobox1">
      <form>
        <label for="anchor1-anchor-select">Place infobox on:</label>
        <select id="anchor1-anchor-select">
          <option value="1">Anchor 1</option>
          <option value="2">Anchor 2</option>
          <option value="3">Anchor 3</option>
          <option value="4">Anchor 4</option>
        </select>
      </form>
    </div>
    
    <div class="infobox" id="infobox2">
      <form>
        <label for="anchor2-anchor-select">Place infobox on:</label>
        <select id="anchor2-anchor-select">
          <option value="1">Anchor 1</option>
          <option value="2">Anchor 2</option>
          <option value="3">Anchor 3</option>
          <option value="4">Anchor 4</option>
        </select>
      </form>
    </div>
    

#### CSS

We declare the first `anchor` `<div>` as an anchor using the `anchor-name` property, which is given two comma-separated anchor names, one for each positioned element. This is the initial state of the demo — both positioned elements will be tethered to the first anchor.

    body {
      height: 100vh;
    }
    
    #anchor-container {
      display: grid;
      height: 100%;
      grid-template-columns: 1fr 1fr;
      grid-auto-rows: 1fr 1fr;
      justify-items: center;
      align-items: center;
    }
    
    .anchor {
      font-size: 1.8rem;
      color: white;
      text-shadow: 1px 1px 1px black;
      background-color: hsl(240 100% 75%);
      width: fit-content;
      border-radius: 10px;
      border: 1px solid black;
      padding: 3px;
    }
    

css

    #anchor1 {
      anchor-name: --my-anchor1, --my-anchor2;
    }
    

Each of the positioned elements is given a `position-anchor` property with a value matching one of the two anchor names. The positioned elements are then given anchor-relative positioning information using a combination of inset, alignment, and margin properties.

    .infobox {
      color: darkblue;
      background-color: azure;
      border: 1px solid #dddddd;
      padding: 10px;
      border-radius: 10px;
      font-size: 1rem;
      width: 120px;
    }
    

css

    #infobox1 {
      position-anchor: --my-anchor1;
      position: fixed;
      left: anchor(right);
      align-self: anchor-center;
      margin-left: 10px;
    }
    
    #infobox2 {
      position-anchor: --my-anchor2;
      position: fixed;
      bottom: anchor(top);
      justify-self: anchor-center;
      margin-bottom: 15px;
    }
    

#### JavaScript

We dynamically change which anchor elements the `anchor-name` values are set on in response to different anchors being selected in the positioned elements' `<select>` menus. The key functionality here is the [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
 event handler, `updateAnchorNames()`. It sets both anchor names on one anchor, if the anchors chosen in the two `<select>` menus are the same. Otherwise, it sets a single anchor name on two separate anchors as appropriate.

js

    // Get references to the two select menus
    const select1 = document.querySelector("#anchor1-anchor-select");
    const select2 = document.querySelector("#anchor2-anchor-select");
    // Store references to all the anchors in a NodeList (array-like)
    const anchors = document.querySelectorAll("#anchor-container > div");
    
    // Set the same change event handler on both select menus
    select1.addEventListener("change", updateAnchorNames);
    select2.addEventListener("change", updateAnchorNames);
    
    function updateAnchorNames() {
      // Remove all anchor names from all anchors
      for (const anchor of anchors) {
        anchor.style.anchorName = "none";
      }
    
      // convert the select menu values to numbers, and remove one to
      // make them match the selected anchors' index positions in the NodeList
      const value1 = Number(select1.value) - 1;
      const value2 = Number(select2.value) - 1;
    
      if (value1 === value2) {
        // If the chosen anchors are both the same, set both anchor
        // names on the same anchor
        anchors[value1].style.anchorName = "--my-anchor1, --my-anchor2";
      } else {
        // If they are not the same, set the anchor names separately
        // on each selected anchor
        anchors[value1].style.anchorName = "--my-anchor1";
        anchors[value2].style.anchorName = "--my-anchor2";
      }
    }
    

#### Result

Select different values from the drop-down menus to change the anchors that the elements are positioned relative to.

### [Using a slider thumb as an anchor](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#using_a_slider_thumb_as_an_anchor)

In this example, an [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
 is positioned relative to an anchor that is the thumb of a range slider.

#### HTML

We include an [`<input type="range">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 element and an [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
 element to display the value of the range. The value displayed in the `<output>` element is updated via JavaScript as the slider value changes.

html

    <label for="slider">Change the value:</label>
    <input type="range" min="0" max="100" value="25" id="slider" />
    <output>25</output>
    

#### CSS

We give the thumb, represented by the [`::-webkit-slider-thumb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-slider-thumb)
 and [`::-moz-range-thumb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-range-thumb)
 pseudo-elements, an anchor name of `--thumb`. We then set that name as the value of the `<output>` element's `position-anchor` property, and give it a [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 value of `fixed`. These steps associated the `<output>` with the thumb.

Finally, we use [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
 and [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
 properties with [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
 values to position the `<output>` relative to the thumb.

    body {
      display: grid;
      place-items: center;
      height: 100vh;
      font-size: 1.4rem;
      font-family: sans-serif;
    }
    input {
      width: 33vw;
    }
    output {
      background: cyan;
      border: 2px solid darkblue;
      padding: 3px 6px;
      border-radius: 10px;
      font-size: 1.2rem;
    }
    

css

    input::-webkit-slider-thumb {
      anchor-name: --thumb;
    }
    
    input::-moz-range-thumb {
      anchor-name: --thumb;
    }
    
    output {
      position-anchor: --thumb;
      position: absolute;
      left: anchor(right);
      bottom: anchor(top);
    }
    

#### JavaScript

We include an event listener that updates the content of the `<output>` element when the value of the `<input>` changes:

js

    const input = document.querySelector("input");
    const output = document.querySelector("output");
    
    input.addEventListener("input", (event) => {
      output.innerText = `${input.value}`;
    });
    

#### Results

The output is anchored to the thumb. Change the value and the output will remain above and to the right of the thumb, no matter where it is along the slider.

**Note:** The anchor positioning CSS for this demo currently doesn't work in Firefox. The slider's thumb can be targeted via the [`::-moz-range-thumb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-range-thumb)
 pseudo-element in Firefox, but it is currently not available as an anchor (see [Firefox bug 1993699](https://bugzil.la/1993699 "External link (opens in new tab)")
).

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Anchor Positioning Module Level 1  <br>\# position-anchor](https://drafts.csswg.org/css-anchor-position-1/#position-anchor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
    
*   [`anchor-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-scope)
    
*   HTML [`anchor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/anchor)
     attribute
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module
*   [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
     guide

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/position-anchor/index.md?plain=1 "Folder: en-us/web/css/reference/properties/position-anchor (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fposition-anchor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fposition-anchor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fposition-anchor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fposition-anchor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F93149226b6b94a770731d262508f5c4aa10bcbed%0A*+Document+last+modified%3A+2026-10-20T20%3A12%3A59.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")