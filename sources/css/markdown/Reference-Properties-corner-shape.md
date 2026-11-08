*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#mdn-search)
    

`corner-shape` CSS property
===========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/398)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#browser_compatibility)
 carefully before using this in production.

The **`corner-shape`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property specifies the shape of a box's corners, within the area specified by its [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 property value.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#constituent_properties)

------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following physical properties:

*   [`corner-top-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-left-shape)
    
*   [`corner-top-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape)
    
*   [`corner-bottom-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-left-shape)
    
*   [`corner-bottom-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-right-shape)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#syntax)

----------------------------------------------------------------------------------------------------

css

    /* Single value set for all four corners */
    corner-shape: bevel;
    
    /* top-left and bottom-right, top-right and bottom-left */
    corner-shape: notch superellipse(0.6);
    
    /* top-left, top-right and bottom-left, bottom-right */
    corner-shape: superellipse(-1.2) square squircle;
    
    /* top-left, top-right, bottom-right, bottom-left */
    corner-shape: scoop superellipse(-1.6) superellipse(-2.2) round;
    
    /* Global values */
    corner-shape: inherit;
    corner-shape: initial;
    corner-shape: revert;
    corner-shape: revert-layer;
    corner-shape: unset;
    

The `corner-shape` property may be specified using one, two, three, or four [`<corner-shape-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)
 values:

*   If **one** value is used, it specifies the shape of **all four corners**.
*   If **two** values are used, the first shape applies to the **top-left and bottom-right** corners, and the second to the **top-right and bottom-left corners**.
*   If **three** values are used, the first shape specifies the shape of the **top-left corner**, the second to the **top-right and bottom-left corners**, and the third to the **bottom-right corner**.
*   If four values are used, they specify the shape of the **top-left**, **top-right**, **bottom-right**, and **bottom-left** corners, in that order (clockwise).

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#values)

[`<corner-shape-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)

A [`superellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)
 or keyword equivalent describing the shape of the corner.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#description)

--------------------------------------------------------------------------------------------------------------

The `corner-shape` property is used to modify the shape of rounded corners created by the [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 property and its associated longhands. Already-rounded corners can be further customized in terms of the degree of rounding applied to them, allowing the creation of, for example, beveled, notched, and squircle corners. Borders, outlines, shadows, and background effects applied to the container will follow the defined corner shape.

If a `border-radius` is not applied to a container, or the `border-radius` resolves to `0`, `corner-shape` will have no effect.

The `corner-shape` shorthand property and its associated [`corner-*-shape` shorthands and longhands](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#corner--shape_shorthands_and_longhands)
 accept one to four [`<corner-shape-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)
 values. Each is specified directly as a [`superellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)
 function or a keyword describing a common shape. Each keyword is equivalent to a specific `superellipse()` value.

The default (initial) value of `corner-shape` is `round`, which gives the same effect as using `border-radius` on its own, without `corner-shape`. There is also a keyword value `square`, which gives the same effect as default square corners, effectively removing any `border-radius` applied. The `bevel` value has the effect of drawing a straight line between the two ends of a `border-radius`.

Different `corner-shape` values can be smoothly animated between, as the `superellipse()` equivalents of the keyword values are used as interpolation values.

The `corner-shape` shorthand is especially useful when you want all four borders to be the same, or you want to set different values using a single declaration. To set only one or two corner shapes at a time, use the `corner-*-shape` shorthands and longhands.

### [`corner-*-shape` shorthands and longhands](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#corner--shape_shorthands_and_longhands)

The `corner-shape` shorthand defines the shapes of all four corners in one declaration.

To set only one corner shape at a time, use the corner shape longhands:

*   Physical longhand corner shape properties:
    *   [`corner-bottom-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-left-shape)
        
    *   [`corner-bottom-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-right-shape)
        
    *   [`corner-top-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-left-shape)
        
    *   [`corner-top-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape)
        
*   Logical longhand corner shape properties:
    *   [`corner-start-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-start-shape)
        
    *   [`corner-start-end-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-end-shape)
        
    *   [`corner-end-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-end-start-shape)
        
    *   [`corner-end-end-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-end-end-shape)
        

To set two corner shapes at a time, use the side shorthands:

*   Physical side shorthand properties:
    *   [`corner-top-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-shape)
        
    *   [`corner-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-right-shape)
        
    *   [`corner-bottom-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-shape)
        
    *   [`corner-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-left-shape)
        
*   Logical side shorthand properties:
    *   [`corner-block-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-block-start-shape)
        
    *   [`corner-block-end-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-block-end-shape)
        
    *   [`corner-inline-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape)
        
    *   [`corner-inline-end-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-end-shape)
        

### [Constraining opposite corner shape radii](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#constraining_opposite_corner_shape_radii)

When opposite corners have `border-radius` and `corner-shape` values set that would cause the shapes to overlap, the browser constrains the values to prevent the overlap.

For example, the following values would cause the top-left and bottom-right corners to overlap, therefore the browser adjusts the first `border-radius` component to a value that avoids this.

css

    div {
      width: 480px;
      height: 200px;
      background-color: goldenrod;
      border-radius: 80% 20px;
      corner-shape: scoop;
    }
    

### [Properties that follow `corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#properties_that_follow_corner-shape)

The following properties all follow the shape of the corner when set on the container:

*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    
*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    
*   [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    
*   [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
    
*   [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    
*   [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
    

See [Demonstration of properties that follow the `corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#demonstration_of_properties_that_follow_the_corner-shape)
 for some examples.

### [Interaction with `border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#interaction_with_border-shape)

The `corner-shape` property has no effect when the [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
 property is set on an element. This is because `border-shape` is incompatible with `border-radius`: when `border-shape` is set, any specified `border-radius` is ignored; `corner-shape` depends on `border-radius` and therefore has no effect either.

If you want to use shaped corners in a `border-shape`, you will have to draw them directly as part of the shape.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`corner-top-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-left-shape)<br>    : `round`<br>*   [`corner-top-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape)<br>    : `round`<br>*   [`corner-bottom-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-left-shape)<br>    : `round`<br>*   [`corner-bottom-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-right-shape)<br>    : `round` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`corner-top-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-left-shape)<br>    : The corresponding [superellipse()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)<br>     value.<br>*   [`corner-top-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape)<br>    : The corresponding [superellipse()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)<br>     value.<br>*   [`corner-bottom-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-left-shape)<br>    : The corresponding [superellipse()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)<br>     value.<br>*   [`corner-bottom-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-right-shape)<br>    : The corresponding [superellipse()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)<br>     value. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`corner-top-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-left-shape)<br>    : Animates as per [superellipse interpolation](https://drafts.csswg.org/css-borders/#superellipse-interpolation "External link (opens in new tab)")<br>    .<br>*   [`corner-top-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape)<br>    : Animates as per [superellipse interpolation](https://drafts.csswg.org/css-borders/#superellipse-interpolation "External link (opens in new tab)")<br>    .<br>*   [`corner-bottom-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-left-shape)<br>    : Animates as per [superellipse interpolation](https://drafts.csswg.org/css-borders/#superellipse-interpolation "External link (opens in new tab)")<br>    .<br>*   [`corner-bottom-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-right-shape)<br>    : Animates as per [superellipse interpolation](https://drafts.csswg.org/css-borders/#superellipse-interpolation "External link (opens in new tab)")<br>    . |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#formal_syntax)

------------------------------------------------------------------------------------------------------------------

corner-shape =   
  [<'corner-top-left-shape'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-left-shape)
[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<corner-top-left-shape>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-left-shape)
 =   
  <corner-shape-value>    
  
[<corner-shape-value>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)
 =   
  round             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  scoop             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bevel             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  notch             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  square            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  squircle          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <superellipse()>    
  
[<superellipse()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)
 =   
  superellipse( [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  infinity                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  \-infinity )               

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#examples)

--------------------------------------------------------------------------------------------------------

### [Basic `corner-shape` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#basic_corner-shape_usage)

#### HTML

The markup for this example contains a single [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element.

html

    <div>Nice scooped corners</div>
    

#### CSS

We give the box a fixed [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
, a [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
, a `border-radius` of 30 pixels, and a `corner-shape` of `scoop`, along with some additional styles that we've hidden for brevity.

    body {
      font-family: "Helvetica", "Arial", sans-serif;
      width: 240px;
      margin: 20px auto;
    }
    
    div {
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: cyan;
      background-image: linear-gradient(
        to bottom,
        rgb(255 255 255 / 0),
        rgb(255 255 255 / 0.5)
      );
    }
    
    @supports not (corner-shape: scoop) {
      body {
        all: unset !important;
      }
    
      body::before {
        content: "Your browser does not support the 'corner-shape' property.";
        color: black;
        background-color: #ffcd33;
        display: block;
        width: 100%;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

css

    div {
      height: 180px;
      box-shadow: 1px 1px 3px gray;
      border-radius: 30px;
      corner-shape: scoop;
    }
    

#### Result

The rendered result looks like this:

Note how the `corner-shape` value of `scoop` gives the container concave corners — the curve is an inversion of the default `border-radius` curve. Note also how the background, border, and box shadow follow the shape of the curve.

### [Demonstration of properties that follow the `corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#demonstration_of_properties_that_follow_the_corner-shape)

#### HTML

The markup for this example contains a single [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element with some text content inside it.

html

    <div>
      Some styles follow the corner shape, such as border, outline, box-shadow,
      overflow, and backdrop-filter. This is useful for helping various aspects of
      your design to not clash. As shown, it can result in some interesting visual
      effects, so you should test your design carefully.
    </div>
    

#### CSS

To demonstrate how some styles follow the shape of a container's corners, we apply a [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 to the document `<body>`, then apply a `border-radius` of `40px` and a `corner-shape` of `scoop notch` to the `<div>`.

We then apply the following to the `<div>`:

*   A semi-transparent [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    .
*   A different color and style of [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
     on each edge.
*   A [`backdrop-filter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter)
     that inverts the `background-image` set on the `<body>`.
*   A `:hover` style so you can see that the clickable content area falls outside the corner shape.

Additional set up styles have been hidden for brevity.

    html {
      height: 100%;
    }
    
    body {
      font-family: "Helvetica", "Arial", sans-serif;
      height: inherit;
      margin: 0;
      display: flex;
      justify-content: center;
      align-items: center;
    }
    
    div {
      width: 240px;
      height: 180px;
    }
    
    @supports not (corner-shape: scoop notch) {
      :root::before {
        content: "Your browser does not support the 'corner-shape' property.";
        color: black;
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

css

    body {
      background: url("https://mdn.github.io/shared-assets/images/examples/leopard.jpg")
        no-repeat;
      background-size: cover;
    }
    
    div {
      border-radius: 40px;
      corner-shape: scoop notch;
      background-color: rgb(255 255 255 / 0.2);
      border-top: 3px solid blue;
      border-left: 6px dashed red;
      border-bottom: 9px solid yellow;
      border-right: 12px double green;
      backdrop-filter: invert(100%);
    }
    
    div:hover {
      background-color: white;
    }
    

#### Result

The rendered result looks like this:

Note how most of the set styles follow the shape of the `<div>` resulting from its `corner-shape` styles, but not all. The content is displayed relative to the original box, and the hover effect is still applied if you hover over the text sticking out past the top- and bottom-left corners.

### [Comparing `corner-shape` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#comparing_corner-shape_values)

In this demonstration, you can select different `corner-shape` values and set different [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 values on a container and compare the effects.

#### HTML

The markup for this example contains a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 picker from which different `corner-shape` values can be selected, an [`<input type="range">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 slider to select different `border-radius` values, and a [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element to create a container to apply those values to. The select [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 elements provide multiple keyword and [`superellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)
 value choices, broken into two groups using [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
 elements. In the case of the keyword values, we've also included the `superellipse()` value equivalent for each one, separated by a pipe character.

html

    <form>
      <div>
        <label for="corner-shape-choice">Choose a corner-shape value:</label>
        <select id="corner-shape-choice">
          <optgroup label="Keywords">
            <option value="square">square | superellipse(infinity)</option>
            <option selected value="squircle">squircle | superellipse(2)</option>
            <option value="round">round | superellipse(1)</option>
            <option value="bevel">bevel | superellipse(0)</option>
            <option value="scoop">scoop | superellipse(-1)</option>
            <option value="notch">notch | superellipse(-infinity)</option>
          </optgroup>
          <optgroup label="Functions">
            <option>superellipse(3)</option>
            <option>superellipse(1.5)</option>
            <option>superellipse(0.5)</option>
            <option>superellipse(-0.5)</option>
            <option>superellipse(-1.5)</option>
            <option>superellipse(-3)</option>
          </optgroup>
        </select>
      </div>
      <div>
        <label for="radius-slider">Choose a border-radius value:</label>
        <input
          type="range"
          id="radius-slider"
          min="0"
          value="45"
          max="90"
          step="1" />
      </div>
    </form>
    <section></section>
    

#### CSS

We apply a [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
 to the `<section>`. We also give the `<section>` and form elements some basic styles, which we've hidden for brevity.

    html {
      font-family: "Helvetica", "Arial", sans-serif;
    }
    
    body {
      width: fit-content;
      margin: 20px auto;
    }
    
    section {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 20px;
    }
    
    select {
      padding: 3px 5px;
    }
    
    form div:nth-of-type(2) {
      margin-top: 5px;
      display: flex;
    }
    
    section {
      width: 100%;
      height: 180px;
      background-color: gold;
      background-image: linear-gradient(
        to bottom,
        rgb(255 255 255 / 0),
        rgb(255 255 255 / 0.5)
      );
    }
    
    @supports not (corner-shape: scoop) {
      :root::before {
        content: "Your browser does not support the 'corner-shape' property.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

css

    section {
      box-shadow: 1px 1px 3px gray;
    }
    

    const rectangle = document.querySelector("section");
    const select = document.querySelector("select");
    const range = document.getElementById("radius-slider");
    
    function setCorners() {
      rectangle.style.cornerShape = select.value;
      const brValue = `${range.value}px`;
      rectangle.style.borderRadius = brValue;
      rectangle.innerHTML = `<div><code>corner-shape: ${select.value};</code><br><code>border-radius: ${brValue};</code></div>`;
    }
    
    select.addEventListener("change", setCorners);
    range.addEventListener("input", setCorners);
    setCorners();
    

The JavaScript that applies the user-selected values to the `<section>` has been hidden for brevity.

#### Result

The rendered result looks like this:

Try selecting different values to see how this affects the shape of the corners.

### [`superellipse()` value comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#superellipse_value_comparison)

In this example, we provide two [`<input type="range">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 sliders allowing you to cycle through many different `corner-shape` [`superellipse()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)
 values and [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 values to compare the effects of each on a container.

#### HTML

The markup for this example contains two `<input type="range">` elements from which different `corner-shape` `superellipse()` and `border-radius` values can be selected, and a [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 element to apply those values to.

html

    <form>
      <div>
        <label for="superellipse-slider">Choose a superellipse() value:</label>
        <input
          type="range"
          id="superellipse-slider"
          min="-5"
          value="0"
          max="5"
          step="0.1" />
      </div>
      <div>
        <label for="radius-slider">Choose a border-radius value:</label>
        <input
          type="range"
          id="radius-slider"
          min="0"
          value="45"
          max="90"
          step="1" />
      </div>
    </form>
    <section></section>
    

#### CSS

We apply a [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
 to the `<section>` element. Additional basic styles have been hidden for brevity.

    html {
      font-family: "Helvetica", "Arial", sans-serif;
    }
    
    body {
      width: fit-content;
      margin: 20px auto;
    }
    
    section {
      display: flex;
      justify-content: center;
      align-items: center;
      margin-top: 20px;
    }
    
    form div {
      margin-top: 5px;
      display: flex;
    }
    
    section {
      width: 100%;
      height: 180px;
      background-color: orange;
      background-image: linear-gradient(
        to bottom,
        rgb(255 255 255 / 0),
        rgb(255 255 255 / 0.5)
      );
    }
    
    @supports not (corner-shape: superellipse(0)) {
      :root::before {
        content: "Your browser does not support the 'corner-shape' property.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

css

    section {
      box-shadow: 1px 1px 3px gray;
    }
    

    const rectangle = document.querySelector("section");
    const superEllipseRange = document.getElementById("superellipse-slider");
    const borderRadiusRange = document.getElementById("radius-slider");
    
    function setCorners() {
      const seValue = `superellipse(${superEllipseRange.value})`;
      rectangle.style.cornerShape = seValue;
      const brValue = `${borderRadiusRange.value}px`;
      rectangle.style.borderRadius = brValue;
      rectangle.innerHTML = `<div><code>corner-shape: ${seValue};</code><br><code>border-radius: ${brValue};</code></div>`;
    }
    
    superEllipseRange.addEventListener("input", setCorners);
    borderRadiusRange.addEventListener("input", setCorners);
    setCorners();
    

The JavaScript that applies the user-selected values to the `<section>` has been hidden for brevity.

#### Result

The rendered result looks like this:

Try selecting different values to see how this affects the shape of the corners.

### [Animating `corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#animating_corner-shape)

In this example, we demonstrate how the `corner-shape` property can be animated.

#### HTML

html

    <div></div>
    

#### CSS

We create a set of [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 that animate smoothly between the `corner-shape` values of `square` and `notch`. We then apply an [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 based on those `@keyframes` to the `<div>` when its containing `<html>` element is hovered over or focused. Additional basic `<div>` styles have been hidden for brevity.

    body {
      width: 200px;
      margin: 20px auto;
    }
    
    div {
      width: 100%;
      height: 200px;
      background-color: green;
      background-image: linear-gradient(
        to bottom,
        rgb(255 255 255 / 0),
        rgb(255 255 255 / 0.5)
      );
      box-shadow: 1px 1px 3px gray;
      border-radius: 50%;
      corner-shape: square;
      outline: none;
    }
    
    @supports not (corner-shape: square) {
      :root::before {
        content: "Your browser does not support the 'corner-shape' property.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

css

    @keyframes corner-pulse {
      0% {
        corner-shape: square;
      }
    
      /* To make the starting point apparent, let us keep
      the shape the same for a small duration. */
      20% {
        corner-shape: square;
      }
    
      100% {
        corner-shape: notch;
      }
    }
    
    div {
      animation: corner-pulse infinite alternate 4s linear;
    }
    

#### Result

The rendered result looks like this:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Borders and Box Decorations Module Level 4  <br>\# propdef-corner-shape](https://drafts.csswg.org/css-borders/#propdef-corner-shape) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape#see_also)

--------------------------------------------------------------------------------------------------------

*   [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
    
*   [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
    
*   [CSS borders and box decorations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations)
     module
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/corner-shape/index.md?plain=1 "Folder: en-us/web/css/reference/properties/corner-shape (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcorner-shape&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcorner-shape%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcorner-shape%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcorner-shape%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")