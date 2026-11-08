*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#mdn-search)
    

`background-repeat` CSS property
================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`background-repeat`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property sets how background images are repeated. A background image can be repeated along the horizontal and vertical axes, or not repeated at all.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#try_it)

---------------------------------------------------------------------------------------------------------

    background-repeat: repeat-x;
    

    background-repeat: repeat;
    

    background-repeat: space;
    

    background-repeat: round;
    

    background-repeat: no-repeat;
    

    background-repeat: space repeat;
    

    <section id="default-example">
      <div id="example-element"></div>
    </section>
    

    #example-element {
      background: #cccccc url("/shared-assets/images/examples/moon.jpg") center /
        120px;
      min-width: 100%;
      min-height: 100%;
    }
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#constituent_properties)

-----------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`background-repeat-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-x)
    
*   [`background-repeat-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat-y)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    background-repeat: repeat;
    background-repeat: repeat-x;
    background-repeat: repeat-y;
    background-repeat: space;
    background-repeat: round;
    background-repeat: no-repeat;
    
    /* Two-value syntax: horizontal | vertical */
    background-repeat: repeat space;
    background-repeat: repeat repeat;
    background-repeat: round space;
    background-repeat: no-repeat round;
    
    /* Global values */
    background-repeat: inherit;
    background-repeat: initial;
    background-repeat: revert;
    background-repeat: revert-layer;
    background-repeat: unset;
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#description)

-------------------------------------------------------------------------------------------------------------------

The property accepts a comma-separated list of two [`<repeat-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#values)
 keyterms, or one keyterm as a shorthand for the two values. When two values are provided, the first value defines the horizontal repetition behavior and the second value defines the vertical behavior. Property values can be used to repeat only horizontally, vertically, or not at all.

The default value is `repeat repeat`. With this value, the background image maintains its intrinsic [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
, repeating both horizontally and vertically to cover the entire background paint area, with edge images being clipped to the size of the element. Which edges clipped depends on the value of the corresponding [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
 value. How many times they are repeated and how much the images on the edges are clipped depends on the size of the background painting area and the corresponding [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
 value.

The repeating images can be evenly spaced apart, ensuring the repeated image maintains its aspect ratio without being clipped. With the `space` value, if the background paint area has a different aspect ratio than the image or does not otherwise have a size that is a multiple of the background size in either direction, there will be areas not covered by the background image.

Alternatively, the repeated background image can be stretched to cover the entire area without clipping. With `round`, the repeated image is stretched to fill all the available space until there is room to add an additional repeated image if the aspect ratio of the background image is not the same as the paint area's aspect ratio. For example, given a background image that is 100px x 100px and a background paint area of 1099px x 750px, the image will be repeated 10 times in the horizontal direction and 7 times vertically, for a total of 70 repetitions, with each image stretched in both directions to be 109.9px x 105px, altering the image's aspect ratio and potentially distorting it. If the width of the paint area increases by 1px, becoming 1100px wide, an 11th image will fit horizontally for a total of 77 image repetitions, with each image being painted at 100px wide and 105px tall, stretched only in the vertical direction.

[Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#values)

---------------------------------------------------------------------------------------------------------

The property accepts a comma-separated list of two `<repeat-style>` keyterms or one keyterm as a shorthand for the two values. The first value is the horizontal repetition. The second value is the vertical behavior. If only a single value is set to a value other than `repeat-x` or `repeat-y`, that value is applied the both vertices. The values include:

[`repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#repeat)

The default value. The image is repeated as many times as needed to cover the entire background image painting area, with the edge image being clipped if the dimension of the painting area is not a multiple of the dimension of your background image.

[`no-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#no-repeat)

The image is not repeated (and hence the background image painting area will not necessarily be entirely covered). The position of the non-repeated background image is defined by the [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
 CSS property.

[`space`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#space)

The image is repeated as much as possible without clipping. The first and last images are pinned to either side of the element, and whitespace is distributed evenly between the images. The [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
 property is ignored unless only one image can be displayed without clipping. The only case where clipping happens using `space` is when there isn't enough room to display one image.

[`round`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#round)

As the allowed space increases in size, the repeated images will stretch (leaving no gaps) until there is room for another one to be added. This is the only `<repeat-style>` value that can lead to the distortion of the background image's [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
, which will occur if the aspect ratio of the background image differs from the aspect ratio of the background paint area.

[`repeat-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#repeat-x)

Shorthand for `repeat no-repeat`, the background image repeats horizontally only, with the edge image being clipped if the width of the paint area is not a multiple of the background image's width.

[`repeat-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#repeat-y)

Shorthand for `no-repeat repeat`, the background image repeats vertically only, with the edge image being clipped if the height of the paint area is not a multiple of the background image's height.

When one `<repeat-style>` keyterm is provided, the value is shorthand for the following two-value syntax:

| Single value | Two-value equivalent |
| --- | --- |
| `repeat-x` | `repeat no-repeat` |
| `repeat-y` | `no-repeat repeat` |
| `repeat` | `repeat repeat` |
| `space` | `space space` |
| `round` | `round round` |
| `no-repeat` | `no-repeat no-repeat` |

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `repeat` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | a list, each item consisting of two keywords, one per dimension |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

background-repeat =   
  <repeat-style>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<repeat-style> =   
  repeat-x           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  repeat-y           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  repeat-block       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  repeat-inline      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <repetition>[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
<repetition> =   
  repeat     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  space      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  round      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  no-repeat    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#examples)

-------------------------------------------------------------------------------------------------------------

### [Setting background-repeat](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#setting_background-repeat)

#### HTML

html

    <ol>
      <li>
        no-repeat
        <div class="one"></div>
      </li>
      <li>
        repeat
        <div class="two"></div>
      </li>
      <li>
        repeat-x
        <div class="three"></div>
      </li>
      <li>
        repeat-y
        <div class="four"></div>
      </li>
      <li>
        space
        <div class="five"></div>
      </li>
      <li>
        round
        <div class="six"></div>
      </li>
      <li>
        repeat-x, repeat-y (multiple images)
        <div class="seven"></div>
      </li>
    </ol>
    

#### CSS

css

    /* Shared for all DIVS in example */
    ol,
    li {
      margin: 0;
      padding: 0;
    }
    li {
      margin-bottom: 12px;
    }
    div {
      background-image: url("star-solid.gif");
      width: 160px;
      height: 70px;
    }
    
    /* Background repeats */
    .one {
      background-repeat: no-repeat;
    }
    .two {
      background-repeat: repeat;
    }
    .three {
      background-repeat: repeat-x;
    }
    .four {
      background-repeat: repeat-y;
    }
    .five {
      background-repeat: space;
    }
    .six {
      background-repeat: round;
    }
    
    /* Multiple images */
    .seven {
      background-image:
        url("star-solid.gif"), url("/shared-assets/images/examples/favicon32.png");
      background-repeat: repeat-x, repeat-y;
      height: 144px;
    }
    

#### Result

In this example, each list item is matched with a different value of `background-repeat`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# background-repeat](https://drafts.csswg.org/css-backgrounds/#background-repeat) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat#see_also)

-------------------------------------------------------------------------------------------------------------

*   The other [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
     shorthand components: [`background-attachment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
    , [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
    , [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    , [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    , [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
    , [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
     ([`background-position-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x)
     and [`background-position-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-y)
    ), and [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [Using multiple backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds)
    
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module
*   [Understanding aspect ratios](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/background-repeat/index.md?plain=1 "Folder: en-us/web/css/reference/properties/background-repeat (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-repeat&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-repeat%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-repeat%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-repeat%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")