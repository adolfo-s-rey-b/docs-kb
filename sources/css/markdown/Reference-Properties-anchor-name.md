*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#mdn-search)
    

`anchor-name` CSS property
==========================

Baseline 2026

Newly available

\*

Since January 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/245)

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`anchor-name`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property enables defining an element as an **anchor element** by giving it one or more identifying **anchor names**. Each name can then be set as the value of a positioned element's [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 property to associate it with the anchor.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Single values */
    anchor-name: none;
    anchor-name: --name;
    
    /* Multiple values */
    anchor-name: --name, --another-name;
    
    /* Global values */
    anchor-name: inherit;
    anchor-name: initial;
    anchor-name: revert;
    anchor-name: revert-layer;
    anchor-name: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#values)

This property is specified as a single value from the following list:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#none)

The default value. Setting `anchor-name: none` on an element means that it is not defined as an anchor element. If the element was previously defined as an anchor and associated with a positioned element, setting `anchor-name: none` disassociates the two.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

One or more comma-separated arbitrary custom identifiers defining the name or names of the anchor, which can then be referenced in a [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 property.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#description)

-------------------------------------------------------------------------------------------------------------

To position an element relative to an anchor element, the positioned element requires three features: an association, a position, and a location. The `anchor-name` and [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 properties provide an explicit association.

The anchor element accepts one or more `<dashed-ident>` anchor names set on it via the `anchor-name` property. When one of those names is then set as the value of the `position-anchor` property of an element that has its [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 set to `absolute` or `fixed`, the two elements are associated. The two elements become tethered by setting a location on the associated element relative to the anchor, making it an "anchor-positioned" element.

If multiple anchor elements have the same anchor name set on them, and that name is referenced by the `position-anchor` property value of a positioned element, that positioned element will be associated with the last anchor element with that anchor name in the source order.

Anchor positioning changes the [containing block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Display/Containing_block)
 of anchor-positioned elements, making its `position` relative to its anchor rather than to the nearest positioned ancestor element.

To tether and place a positioned element in a specific location relative to an anchor element, an anchor positioning feature is needed, such as the [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
 function (set within an [inset property's](https://developer.mozilla.org/en-US/docs/Glossary/Inset_properties)
 value) or the [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 property.

You cannot associate a positioned element with an anchor element if the anchor is hidden, such as with [`display: none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 or [`visibility: hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
, or if the anchor is part of the [skipped contents](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#skips_its_contents)
 of another element due to it having [`content-visibility: hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
 set on it.

The `anchor-name` property is supported on all elements that generate a principal box. This means that [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
, including generated content created using [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)
 and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)
, and UI features like the [`range` input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 thumb ([`::-webkit-slider-thumb`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-slider-thumb)
) can be anchor elements. Pseudo elements are implicitly anchored to the same element as the pseudo-element's originating element, unless otherwise specified.

For more information on anchor features and usage, see the [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 module and the [Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
 guide.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | All elements that generate a [principal box](https://drafts.csswg.org/css-display-4/#principal-box "External link (opens in new tab)") |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

anchor-name =   
  none            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <anchor-name>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<anchor-name> =   
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#examples)

-------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#basic_usage)

This example tethers a positioned element to an anchor, positioning the element to the right of the anchor.

#### HTML

We specify two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements; an anchor element with a class of `anchor` and a positioned element with a class of `infobox`.

We also include some filler text around the two `<div>`s to make the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 taller so that it will scroll.

html

    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
      incididunt ut labore et dolore magna aliqua. Dui nunc mattis enim ut tellus
      elementum sagittis vitae et.
    </p>
    
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
    

#### CSS

We first declare the `anchor` `<div>` as an anchor element by setting an anchor name on it via the `anchor-name` property:

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
    

css

    .anchor {
      anchor-name: --my-anchor;
    }
    

We associate the second `<div>` with the anchor element by setting its anchor name as the value of the positioned element's [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 property. We then set the positioned element's:

*   [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
     property to `fixed`, converting it to an _anchor-positioned element_ so it can be positioned relative to the anchor's position on the page.
*   [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
     and [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
     properties to [`anchor()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/anchor)
     functions with values of `right` and `top` respectively. This positions the infobox's left edge flush to the right edge of its anchor, and its top edge relative to the top edge of its anchor.
*   [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
     to `10px`, creating space between the anchor positioned element and its anchor.

    .infobox {
      color: darkblue;
      background-color: azure;
      border: 1px solid #dddddd;
      padding: 10px;
      border-radius: 10px;
      font-size: 1rem;
    }
    

css

    .infobox {
      position-anchor: --my-anchor;
      position: fixed;
      left: anchor(right);
      top: anchor(top);
      margin-left: 10px;
    }
    

#### Result

Scroll the page to see how the infobox is positioned relative to the anchor. As the anchor scrolls upwards, the positioned element moves along with it.

### [Multiple positioned elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#multiple_positioned_elements)

This example demonstrates how you can associate multiple positioned elements with one anchor.

#### HTML

The HTML is the same as for the previous example, except this time we have multiple positioned element `<div>`s with different [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
s to identify them.

html

    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
      incididunt ut labore et dolore magna aliqua. Dui nunc mattis enim ut tellus
      elementum sagittis vitae et.
    </p>
    
    <div class="anchor">⚓︎</div>
    
    <div class="infobox" id="infobox1">
      <p>This is an information box.</p>
    </div>
    
    <div class="infobox" id="infobox2">
      <p>This is another information box.</p>
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
    

#### CSS

We declare the `anchor` `<div>` as an anchor element using the `anchor-name` property, giving it an anchor name as before.

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
    

css

    .anchor {
      anchor-name: --my-anchor;
    }
    

Each of the two positioned elements are associated with the anchor element by setting its anchor name as the positioned element's [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
 property value. Both are also given `fixed` positioning, making them **anchor positioned elements**. The positioned elements are then positioned in different places relative to the anchor using a combination of inset properties as seen above and [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 / [`justify-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-self)
 properties with a value of `anchor-center`, centrally aligning the infobox to the center of the anchor in the inline/block directions respectively.

    .infobox {
      color: darkblue;
      background-color: azure;
      border: 1px solid #dddddd;
      padding: 10px;
      border-radius: 10px;
      font-size: 1rem;
    }
    

css

    .infobox {
      position-anchor: --my-anchor;
      position: fixed;
    }
    
    #infobox1 {
      left: anchor(right);
      align-self: anchor-center;
      margin-left: 10px;
    }
    
    #infobox2 {
      bottom: anchor(top);
      justify-self: anchor-center;
      margin-bottom: 15px;
    }
    

#### Result

Scroll the page to see how both of the infoboxes are tethered to the anchor.

### [Multiple anchor names](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#multiple_anchor_names)

This example demonstrates how an anchor element can have more than one anchor name.

#### HTML

The HTML is the same as for the previous example.

    <p>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
      incididunt ut labore et dolore magna aliqua. Dui nunc mattis enim ut tellus
      elementum sagittis vitae et.
    </p>
    
    <div class="anchor">⚓︎</div>
    
    <div class="infobox" id="infobox1">
      <p>This is an information box.</p>
    </div>
    
    <div class="infobox" id="infobox2">
      <p>This is another information box.</p>
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
    

#### CSS

The CSS is the same as the previous example too, except we include two comma-separated names in the target's `anchor-name` property value and each positioned element has a different value for `position-anchor`.

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
      anchor-name: --anchor1, --anchor2;
    }
    
    .infobox {
      position: fixed;
    }
    
    #infobox1 {
      position-anchor: --anchor1;
      left: anchor(right);
      align-self: anchor-center;
      margin-left: 10px;
    }
    
    #infobox2 {
      position-anchor: --anchor2;
      bottom: anchor(top);
      justify-self: anchor-center;
      margin-bottom: 15px;
    }
    

#### Result

Scroll the page to see how both of the infoboxes are tethered to the anchor.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Anchor Positioning Module Level 1  <br>\# name](https://drafts.csswg.org/css-anchor-position-1/#name) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name#see_also)

-------------------------------------------------------------------------------------------------------

*   [`position-anchor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-anchor)
    
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

This page was last modified on Aug 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/anchor-name/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/anchor-name/index.md?plain=1 "Folder: en-us/web/css/reference/properties/anchor-name (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanchor-name&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanchor-name%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanchor-name%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanchor-name%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F737b931225e92e0cba47e57a150878b1a78ee45a%0A*+Document+last+modified%3A+2026-08-24T15%3A52%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")