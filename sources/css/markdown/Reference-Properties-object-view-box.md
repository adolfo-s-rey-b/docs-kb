*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#mdn-search)
    

`object-view-box` CSS property
==============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/177)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#browser_compatibility)
 carefully before using this in production.

The **`object-view-box`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines a rectangle as a viewable area (viewbox) within a [replaced element](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
, enabling the content of the replaced element to be zoomed or panned. It works similarly to the SVG [`viewBox`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/viewBox)
 attribute.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#try_it)

-------------------------------------------------------------------------------------------------------

    object-view-box: inset(0 0);
    

    object-view-box: inset(20%);
    

    object-view-box: xywh(95px 20px 60px 60px);
    

    object-view-box: rect(110px 120px 200px 45px);
    

    object-view-box: none;
    

    <section id="default-example">
      <img
        class="transition-all"
        id="example-element"
        src="/shared-assets/images/examples/plumeria-146x200.jpg"
        alt="A close-up of red flowers and buds on a branch." />
    </section>
    

    #example-element {
      height: 100%;
      width: 100%;
      border: 2px dotted #888888;
    }
    
    @supports not (object-view-box: none) {
      body::before {
        content: "Your browser does not support the 'object-view-box' property.";
        color: black;
        background-color: #ffcd33;
        display: block;
        width: 100%;
        text-align: center;
      }
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    object-view-box: none;
    
    /* <basic-shape-rect> functions */
    object-view-box: inset(20%);
    object-view-box: inset(20% 30%);
    object-view-box: inset(10px 0 25px 33px);
    object-view-box: xywh(95px 20px 60px 60px);
    object-view-box: rect(10px 30px 30px 10px);
    
    /* Global values */
    object-view-box: inherit;
    object-view-box: initial;
    object-view-box: revert;
    object-view-box: revert-layer;
    object-view-box: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#none)

The element does not have a view box. This is the default.

[`<basic-shape-rect>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape#syntax_for_rectangles_basic-shape-rect)

An [`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
, [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
, or [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
 function specifying a view box for an element with natural dimensions (replaced elements). Resolves to `none` otherwise.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#description)

-----------------------------------------------------------------------------------------------------------------

The `object-view-box` property can be used to crop or resize [replaced elements](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
, including images and videos. It works by showing a section of the content of the replaced element in the available space reserved for that element. The section of the replaced element that is displayed is defined by the value of the property. The available reserved space is determined by the element's default [extrinsic size](https://developer.mozilla.org/en-US/docs/Glossary/Extrinsic_size)
. The subsection of the content displayed can be presented zoomed-in, panned-out, or at its original size, while maintaining the content's intrinsic [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
.

The property value is a `<basic-shape-rect>`, one of the [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 functions limited to defining a rectangular shape. For example, the value can be a [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
 function:

css

    img {
      object-view-box: xywh(410px 0 400px 150px);
    }
    

In this case, the top left corner of the section of the image that will be displayed is `410px` from the left edge and `0` from the top, as defined by x and y coordinate parameters. The size of the section of the original image that will be displayed is `400px` wide by `150px` tall; the `w` and `h` components of the function. This 400x150 section of the image will be displayed in the space that was reserved for the image itself when the page was laid out. Whether the content section displayed is its original intrinsic size, zoomed in, or zoomed out depends on whether the viewbox is 400px x 150px, smaller, or larger than the image element's size, respectively.

![The leopard image cropped using object-view-box property, with a 400px by 150px viewbox displaying an unscaled section of the image](https://mdn.github.io/shared-assets/images/diagrams/css/object-view-box/object-view-box_xywh.jpg)

In this case, as the rectangular viewbox defined by the `object-view-box` property and the rectangular area of the `<img>` element are the same size, i.e., 400 x 150 pixels, the replaced element is not scaled.

Decrease the `w` and `h` values to create a zoomed-in effect; as the smaller image section is stretched, it has a zoomed-in effect.

Increase the `w` and `h` argument values to create a zoomed-out effect; as the larger image section is shrunk, it has a zoomed-out effect.

Animating the `x` and `y` coordinates creates a panning effect by moving the element's viewbox while the element itself remains in its original location.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | replaced elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | specified keyword, or computed function |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as if possible, otherwise discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

object-view-box =   
  none                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <basic-shape-rect>    
  
<basic-shape-rect> =   
  <inset()>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <rect()>   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <xywh()>     
  
[<inset()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
 =   
  inset( <length-percentage>[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 round [<'border-radius'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<rect()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
 =   
  rect( <top> , <right> , <bottom> , <left> )    
  
[<xywh()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
 =   
  xywh( <length-percentage>[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 <length-percentage \[0,∞\]>[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 round [<'border-radius'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    
  
[<border-radius>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 =   
  <length-percentage \[0,∞\]>[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 / <length-percentage \[0,∞\]>[{1,4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#examples)

-----------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#basic_usage)

This example demonstrates the basic usage and the effects of the `object-view-box` property, with examples using the three different `<basic-shape-rect>` functions.

#### HTML

We have three almost identical [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 elements wrapped in [`<figure>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/figure)
 elements; the only difference is their class names.

html

    <figure>
      <img
        class="intrinsic"
        src="https://mdn.github.io/shared-assets/images/examples/painted-hand.jpg"
        alt="Original scale section of a painted hand" />
      <figcaption>intrinsic</figcaption>
    </figure>
    <figure>
      <img
        class="zoom-in"
        src="https://mdn.github.io/shared-assets/images/examples/painted-hand.jpg"
        alt="Zoomed in section of a painted hand" />
      <figcaption>zoomed in</figcaption>
    </figure>
    <figure>
      <img
        class="zoom-out"
        src="https://mdn.github.io/shared-assets/images/examples/painted-hand.jpg"
        alt="Zoomed out section of a painted hand" />
      <figcaption>zoomed out</figcaption>
    </figure>
    

#### CSS

We style all the images to have the same width and height, then set each class, and therefore each image, to have a different `object-view-box` value. The intrinsic size of the painted hand image is `298px` by `332px`. We set the [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
 and [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
, setting the extrinsic size to `200px` by `200px`.

css

    img {
      width: 200px;
      height: 200px;
      border: 1px solid red;
    }
    

We set three different `object-view-box` property values using three different shape functions. The `intrinsic` element's [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
 function value displays a `200px` square section of the image content, starting from the `70px` from the left and `90px` from the top. The `zoom-in` element's [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
 function displays a `160px` square section of the original element, going from `110px` to `270px` from the top edge and `90px` to `250px` from the left edge. The `zoom-out` replaced element's [`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
 function displays a `298px` square section of the original element; showing the entire width of the image while cutting of a 17px from the top and bottom.

css

    .intrinsic {
      object-view-box: xywh(70px 90px 200px 200px);
    }
    
    .zoom-in {
      object-view-box: rect(110px 250px 270px 90px);
    }
    
    .zoom-out {
      object-view-box: inset(17px 0 17px 0);
    }
    

    @supports not (object-view-box: none) {
      body::before {
        content: "Your browser does not support the 'object-view-box' property.";
        color: black;
        background-color: #ffcd33;
        display: block;
        width: 100%;
        text-align: center;
      }
    }
    
    figure {
      display: inline-block;
      margin: 0;
    }
    
    figcaption {
      text-align: center;
    }
    

#### Results

The `intrinsic` version is showing an unscaled section of the image. The `zoom-in` version is showing a smaller section (`160px` square) of the image, scaled up to fit `200px` square viewbox. As the section is stretched, it looks zoomed in. The `zoom-out` version is showing a larger (`298px` square) section of the image, scaled down to fit `200px` square viewbox. As the section is shrunk, it looks zoomed out.

### [Live zoom-in using object-view-box property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#live_zoom-in_using_object-view-box_property)

This example demonstrates using the `object-view-box` property to zoom a section of a replaced element in and out, within a statically sized HTML element. In this case, the eye of the leopard, within a very large image, serves as the focal point of the zoom effect.

#### HTML

We include an [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element and a [`range`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element, with an associated [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
. The natural dimensions, or intrinsic size, of the original leopard image are `1244px` wide by `416px` tall, with an [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
 of `3:1`.

html

    <img
      src="https://mdn.github.io/shared-assets/images/examples/leopard.jpg"
      alt="leopard" />
    <p>
      <label for="box-size">Zoom-in: </label>
      <input type="range" id="box-size" min="115" max="380" value="150" />
    </p>
    <output></output>
    

#### CSS

We define a `--box-size` custom property, which is used as the height and width in the [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
 function, creating a square viewbox with an aspect ratio of `1:1`. The view box's offset point, the focal point in our zoom effect, is set at `500px` for the `x` coordinate and `30px` for the `y` coordinate, which corresponds to the top-left corner of the leopard's right eye.

    input {
      width: 350px;
    }
    
    output {
      text-align: center;
      background-color: #dedede;
      font-family: monospace;
      padding: 5px;
      display: block;
    }
    
    @supports not (object-view-box: none) {
      body::before {
        content: "Your browser does not support the 'object-view-box' property.";
        color: black;
        background-color: #ffcd33;
        display: block;
        width: 100%;
        text-align: center;
      }
    }
    

css

    img {
      width: 350px;
      height: 350px;
      border: 2px solid red;
    
      --box-size: 150px;
      object-view-box: xywh(500px 30px var(--box-size) var(--box-size));
    }
    

#### JavaScript

We add an event listener to the slider that updates the value of the `--boxSize` custom property when the user interacts with it. To increase the zoom-in effect when the slider is moved to the right, the slider's value is inverted by subtracting it from `500px`, as reducing the view box size increases the zoom-in effect.

js

    const img = document.querySelector("img");
    const zoom = document.getElementById("box-size");
    const output = document.querySelector("output");
    
    function update() {
      const size = 500 - zoom.value;
      img.style.setProperty("--box-size", `${size}px`);
      output.innerText = `object-view-box: xywh(500px 30px ${size}px ${size}px);`;
    }
    
    zoom.addEventListener("input", update);
    update();
    

#### Result

Move the slider to the right to increase the zoom-in effect and left to reduce it. The slider only affects the dimensions of the view box, while the x and y values, the origin point of the viewbox, remain constant. The size of the `<img>` element doesn't change either.

### [Panning using the object-view-box property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#panning_using_the_object-view-box_property)

This example demonstrates panning an image by animating the `object-view-box` property value.

#### HTML

The HTML includes a single image.

html

    <img
      src="https://mdn.github.io/shared-assets/images/examples/leopard.jpg"
      alt="leopard" />
    

#### CSS

We define an image size and keep the viewbox dimensions, the `w` and `h` components of the `xywh()` function, constant, as we animate the top and left positions, changing the position of the `x` and `y` parameters over five seconds.

css

    img {
      width: 350px;
      height: 350px;
    
      object-view-box: xywh(0 30px 400px 400px);
    
      animation: panning 5s linear infinite alternate;
    }
    
    @keyframes panning {
      from {
        object-view-box: xywh(0 -50px 400px 400px);
      }
      to {
        object-view-box: xywh(800px 68px 400px 400px);
      }
    }
    

    @supports not (object-view-box: none) {
      body::before {
        content: "Your browser does not support the 'object-view-box' property.";
        color: black;
        background-color: #ffcd33;
        display: block;
        width: 100%;
        text-align: center;
      }
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Images Module Level 5  <br>\# propdef-object-view-box](https://drafts.csswg.org/css-images-5/#propdef-object-view-box) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Using the CSS `object-view-box` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_object-view-box)
    
*   [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
    
*   [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
    
*   [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [Understanding aspect ratio](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)
    
*   [CSS images](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-view-box/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/object-view-box/index.md?plain=1 "Folder: en-us/web/css/reference/properties/object-view-box (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fobject-view-box&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fobject-view-box%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fobject-view-box%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fobject-view-box%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")