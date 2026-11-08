*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#mdn-search)
    

`xywh()` CSS function
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2024.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`xywh()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 function creates a rectangle using the specified distances from the left (`x`) and top (`y`) edges of the containing block and the specified width (`w`) and height (`h`) of the rectangle. It is a basic shape function of the [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
. You can use the `xywh()` function in CSS properties such as [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 to create the rectangular path along which an element moves, in [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 to define the shape of the clipping region, and in [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
 to define the shape of an element's border.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#syntax)

----------------------------------------------------------------------------------------------------

css

    offset-path: xywh(0 1% 2px 3% round 0 1px 2% 3px);
    clip-path: xywh(1px 2% 3px 4em round 0 1% 2px 3em);
    border-shape: xywh(5% 5% 90% 90% round 20px);
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#values)

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#length-percentage)

Specifies the [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 values for the `x` and `y` coordinates of the rectangle.

[`<length-percentage [0,∞]>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#length-percentage_0%E2%88%9E)

Specifies non-negative [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 values for the width and height of the rectangle. The minimum value can be zero, and the maximum value has no limit.

[`round <'border-radius'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#round_border-radius)

Specifies the radius of the rounded corners of the rectangle using the same syntax as the CSS [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 shorthand property. This parameter is optional.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#formal_syntax)

------------------------------------------------------------------------------------------------------------------

<xywh()> =   
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#examples)

--------------------------------------------------------------------------------------------------------

### [Creating offset-path using xywh()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#creating_offset-path_using_xywh)

In the example below, the [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 property uses the `xywh()` function to define the shape of the path on which the element, a magenta box in this case, moves. Two different scenarios are shown, each with different values for the `xywh()` function. The arrow inside the boxes points to the right edge of the box.

html

    <div class="container">
      Rectangular path 1
      <div class="path xywh-path-1">→</div>
    </div>
    <div class="container">
      Rectangular path 2
      <div class="path xywh-path-2">→</div>
    </div>
    

css

    .container {
      position: relative;
      display: inline-block;
      width: 200px;
      height: 200px;
      border: 1px solid black;
      margin: 30px;
      text-align: center;
    }
    
    .path {
      width: 50px;
      height: 50px;
      position: absolute;
      background-color: magenta;
      animation: move 10s linear infinite;
    }
    
    .xywh-path-1 {
      offset-path: xywh(20px 20px 100% 100% round 10%);
    }
    
    .xywh-path-2 {
      offset-path: xywh(20px 30% 150% 200%);
    }
    
    @keyframes move {
      0% {
        offset-distance: 0%;
      }
      100% {
        offset-distance: 100%;
      }
    }
    

#### Result

*   The path 1 rectangle is offset by `20px` from the left and top edges of the containing block. This path rectangle has the same dimension as the containing block, that is, the width is `100%` of the width of the containing block, and the height is `100%` of the height of the containing block. Notice how the arrow inside the box follows the `10%` curve (defined by `round 10%`) at the rectangular path corners.
*   As the upper limit of both width and height in `xywh()` is infinity, setting the height to `200%` in the path 2 rectangle makes the generated rectangle twice as tall as the containing block. Notice how the arrow inside the box behaves at the corners when no `round <'border-radius'>` is specified.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shapes Module Level 1  <br>\# funcdef-basic-shape-xywh](https://drafts.csswg.org/css-shapes-1/#funcdef-basic-shape-xywh) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh#see_also)

--------------------------------------------------------------------------------------------------------

*   [`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
     function
*   [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect)
     function
*   [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
     property
*   [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
     property
*   [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
     property
*   [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
     data type
*   [CSS shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
     module
*   [Guide to basic shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Using_shape-outside)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/basic-shape/xywh/index.md?plain=1 "Folder: en-us/web/css/reference/values/basic-shape/xywh (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Fxywh&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Fxywh%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Fxywh%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Fxywh%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcd0970bc03cf30a9a8089954cc542a17dbe9eba3%0A*+Document+last+modified%3A+2026-07-16T09%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")