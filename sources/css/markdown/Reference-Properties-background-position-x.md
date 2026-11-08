*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#mdn-search)
    

`background-position-x` CSS property
====================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2016.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`background-position-x`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the initial horizontal position for each background image. The position is relative to the position layer set by [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
.

The value of this property is overridden by any declaration of the [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
 or [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
 shorthand properties applied to the element after it.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#try_it)

-------------------------------------------------------------------------------------------------------------

    background-position-x: left;
    

    background-position-x: center;
    

    background-position-x: 25%;
    

    background-position-x: 2rem;
    

    background-position-x: right 32px;
    

    <section class="display-block" id="default-example">
      <div class="transition-all" id="example-element"></div>
    </section>
    

    #example-element {
      background-color: navajowhite;
      background-image: url("/shared-assets/images/examples/star.png");
      background-repeat: no-repeat;
      height: 100%;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    background-position-x: left;
    background-position-x: center;
    background-position-x: right;
    
    /* <percentage> values */
    background-position-x: 25%;
    
    /* <length> values */
    background-position-x: 0px;
    background-position-x: 1cm;
    background-position-x: 8em;
    
    /* Side-relative values */
    background-position-x: right 3px;
    background-position-x: left 25%;
    
    /* Multiple values */
    background-position-x: 0px, center;
    
    /* Global values */
    background-position-x: inherit;
    background-position-x: initial;
    background-position-x: revert;
    background-position-x: revert-layer;
    background-position-x: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#values)

This property is specified as one or more comma-separated values:

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#left)

Aligns the left edge of the background image with the left edge of the background position layer.

[`center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#center)

Aligns the center of the background image with the center of the background position layer.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#right)

Aligns the right edge of the background image with the right edge of the background position layer.

[`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)

The offset of the given background image's left vertical edge from the background position layer's left vertical edge. (Some browsers allow assigning the right edge for offset).

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)

The offset of the given background image's horizontal position relative to the container. A value of 0% means that the left edge of the background image is aligned with the left edge of the container, and a value of 100% means that the _right_ edge of the background image is aligned with the _right_ edge of the container, thus a value of 50% horizontally centers the background image.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0%` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | refer to width of background positioning area minus width of background image |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | A list, each item consisting of: an offset given as a combination of an absolute length and a percentage, plus an origin keyword |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a repeatable list |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

background-position-x =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 center [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 left [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 right [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-start [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x-end [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
! [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#examples)

-----------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#basic_example)

The following example shows a background image implementation, with background-position-x and background-position-y used to define the image's horizontal and vertical positions separately.

#### HTML

html

    <div></div>
    

#### CSS

css

    div {
      width: 300px;
      height: 300px;
      background-color: skyblue;
      background-image: url("https://mdn.dev/archives/media/attachments/2020/07/29/17350/3b4892b7e820122ac6dd7678891d4507/firefox.png");
      background-repeat: no-repeat;
      background-position-x: center;
      background-position-y: bottom;
    }
    

#### Result

### [Side-relative values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#side-relative_values)

The following example shows support for side-relative offset syntax, which allows the developer to offset the background from any edge.

#### HTML

html

    <div></div>
    

#### CSS

css

    div {
      width: 300px;
      height: 300px;
      background-color: seagreen;
      background-image: url("https://mdn.dev/archives/media/attachments/2020/07/29/17350/3b4892b7e820122ac6dd7678891d4507/firefox.png");
      background-repeat: no-repeat;
      background-position-x: right 20px;
      background-position-y: bottom 10px;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds Module Level 4  <br>\# propdef-background-position-x](https://drafts.csswg.org/css-backgrounds-4/#propdef-background-position-x) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
    
*   [`background-position-y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-y)
    
*   [Using multiple backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position-x/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/background-position-x/index.md?plain=1 "Folder: en-us/web/css/reference/properties/background-position-x (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-position-x&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-position-x%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbackground-position-x%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbackground-position-x%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")