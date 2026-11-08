*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#mdn-search)
    

`position-visibility` CSS property
==================================

Baseline 2026

Newly available

\*

Since January 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/245)

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`position-visibility`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property enables conditionally hiding an anchor-positioned element depending on, for example, whether it is overflowing its containing element or the viewport.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Single values */
    position-visibility: always;
    position-visibility: anchors-valid;
    position-visibility: anchors-visible;
    position-visibility: no-overflow;
    
    /* Global values */
    position-visibility: inherit;
    position-visibility: initial;
    position-visibility: revert;
    position-visibility: revert-layer;
    position-visibility: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#values)

This property is specified as one of the following keyword values:

[`always`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#always)

The positioned element is always displayed.

[`anchors-valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#anchors-valid)

If the positioned element's [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 value doesn't point to a valid anchor element, the positioned element will be strongly hidden.

[`anchors-visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#anchors-visible)

If the anchor is completely hidden, either by overflowing its containing element (or the viewport) or being covered by other elements, the positioned element will be strongly hidden.

[`no-overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#no-overflow)

If the positioned element starts to overflow its containing element or the viewport, it will be strongly hidden.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#description)

---------------------------------------------------------------------------------------------------------------------

In some situations, you might not want to display an anchor-positioned element. For example, if its associated anchor has been scrolled offscreen but the anchor-positioned element would otherwise still be partially or fully visible, it might be unclear what it refers to and take up space unnecessarily, so you may want to hide it altogether.

The `position-visibility` property can be used to `always` show the anchor-positioned element, or conditionally hide it in certain situations:

*   `anchors-visible`: The associated anchor element is completely hidden.
*   `anchors-valid`: The anchor-positioned element's `position-anchor` property doesn't reference a valid [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
     set on an anchor element in the same document.
*   `no-overflow`: The anchor-positioned element is partially or completely hidden.

When an element is hidden due to `position-visibility`, it is referred to as **strongly hidden**. This means that it will act as though it and its descendant elements have a [`visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
 value of `hidden` set, regardless of what their actual visibility value is.

`position-visibility` should only be used in situations in which hiding the positioned element altogether is preferred. In most cases, it makes more sense to attempt to change the placement of positioned elements when they start to overflow, to keep them on-screen and usable. This can be done with the [`position-try-fallbacks`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
 property and [`@position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try)
 at-rule. See the [Fallback options and conditional hiding for overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)
 guide for more information.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `anchors-visible` |
| Applies to | absolutely positioned elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

position-visibility =   
  always                                             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 anchor-valid [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 anchor-visible [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 no-overflow [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#examples)

---------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#basic_usage)

This example enables changing the value of an anchor positioned element's `position-visibility` property to demonstrate the effects of each value.

#### HTML

We specify two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements: an anchor element with a class of `anchor` and a positioned element with a class of `infobox`.

    <p>
      Malesuada nunc vel risus commodo viverra maecenas accumsan lacus. Vel elit
      scelerisque mauris pellentesque pulvinar pellentesque habitant morbi
      tristique.
    </p>
    
    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
      incididunt ut labore et dolore magna aliqua. Dui nunc mattis enim ut tellus
      elementum sagittis vitae et.
    </p>
    
    <p>
      Malesuada nunc vel risus commodo viverra maecenas accumsan lacus. Vel elit
      scelerisque mauris pellentesque pulvinar pellentesque habitant morbi
      tristique. Porta lorem mollis aliquam ut porttitor. Turpis cursus in hac
      habitasse platea dictumst quisque.
    </p>
    

html

    <div class="anchor">⚓︎</div>
    
    <div class="infobox">
      <p>This is an information box.</p>
    </div>
    

    <p>
      Nisi quis eleifend quam adipiscing vitae proin sagittis nisl rhoncus. In arcu
      cursus euismod quis viverra nibh cras pulvinar. Vulputate ut pharetra sit amet
      aliquam.
    </p>
    
    <p>
      Malesuada nunc vel risus commodo viverra maecenas accumsan lacus. Vel elit
      scelerisque mauris pellentesque pulvinar pellentesque habitant morbi
      tristique. Porta lorem mollis aliquam ut porttitor. Turpis cursus in hac
      habitasse platea dictumst quisque. Dolor sit amet consectetur adipiscing elit.
      Ornare lectus sit amet est placerat. Nulla aliquet porttitor lacus luctus
      accumsan.
    </p>
    
    <form>
      <fieldset>
        <legend>Choose position visibility</legend>
        <div>
          <label for="radio-always">always</label>
          <input
            type="radio"
            id="radio-always"
            name="position-visibility"
            value="always"
            checked />
        </div>
        <div>
          <label for="radio-anchors-visible">anchors-visible</label>
          <input
            type="radio"
            id="radio-anchors-visible"
            name="position-visibility"
            value="anchors-visible" />
        </div>
        <div>
          <label for="radio-no-overflow">no-overflow</label>
          <input
            type="radio"
            id="radio-no-overflow"
            name="position-visibility"
            value="no-overflow" />
        </div>
      </fieldset>
    </form>
    

The HTML also includes filler text to make the content taller than the viewport so scrolling is required. We've also included a [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
 with a group of [radio inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)
 with different `position-visibility` values. The markup for these is not shown for the sake of brevity.

#### CSS

We style an `anchor` `<div>` as an anchor element and tether the `infobox` `<div>` to it. The relevant CSS is as follows:

    body {
      width: 50%;
      margin: 0 auto;
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
    
    form {
      position: fixed;
      background: white;
      bottom: 2px;
      right: 2px;
    }
    
    .infobox {
      color: darkblue;
      background-color: azure;
      border: 1px solid #dddddd;
      padding: 10px;
      border-radius: 10px;
      font-size: 1rem;
    }
    

css

    .anchor {
      anchor-name: --my-anchor;
    }
    
    .infobox {
      position-anchor: --my-anchor;
      position: fixed;
      position-area: top span-all;
      margin-bottom: 5px;
      position-visibility: always;
    }
    

#### JavaScript

We include a [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event)
 event handler on the radio buttons so that, when a new value is selected, we update the infobox's `position-visibility` property value.

js

    const infobox = document.querySelector(".infobox");
    const radios = document.querySelectorAll('[name="position-visibility"]');
    
    for (const radio of radios) {
      radio.addEventListener("change", setPositionVisibility);
    }
    
    function setPositionVisibility(e) {
      infobox.style.positionVisibility = e.target.value;
    }
    

#### Result

Select different `position-visibility` values and then scroll the page up and down to see their effects. With `position-visibility: always` set, the positioned element will not be hidden. With `position-visibility: anchors-visible` set, the positioned element will only be visible when the anchor is partially or fully on-screen. With `position-visibility: no-overflow` set, the positioned element will be hidden as soon as it starts to overflow the viewport.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Anchor Positioning Module Level 1  <br>\# position-visibility](https://drafts.csswg.org/css-anchor-position-1/#position-visibility) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`anchor-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name)
    
*   [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
    
*   [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
    
*   [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
    
*   [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     module
*   [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
     guide
*   [Fallback options and conditional hiding for overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)
     guide

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-visibility/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/position-visibility/index.md?plain=1 "Folder: en-us/web/css/reference/properties/position-visibility (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fposition-visibility&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fposition-visibility%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fposition-visibility%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fposition-visibility%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")