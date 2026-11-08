*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#mdn-search)
    

`rect()` CSS function
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2024.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`rect()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 function creates a rectangle at the specified distance from the top and left edges of the containing block. It is a basic shape function of the [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
. You can use the `rect()` function in CSS properties such as [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 to create the rectangular path along which an element moves, in [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 to define the shape of the clipping region, and in [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
 to define the shape of an element's border.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#syntax)

----------------------------------------------------------------------------------------------------

css

    offset-path: rect(0 1% auto 3% round 0 1px);
    clip-path: rect(50px 70px 80% 20%);
    border-shape: rect(10px 500px 130px 20px round 20px);
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#values)

The inset rectangle is defined by specifying four offset values, starting with the top edge offset and going clockwise, and an optional `round` keyword with the `border-radius` parameter to add rounded corners to the rectangle. Each offset value can be either a `<length>`, a `<percentage>`, or the keyword `auto`.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#length-percentage)

Specifies the [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 value of the distance of the top, right, bottom, or left edge of the rectangle from the top or left edge of the containing block. The first (top) and third (bottom) values are distances from the top edge of the containing block, and the second (right) and fourth (left) values are distances from the left edge of the containing block. The second (right) and third (bottom) values are clamped by the fourth (left) and first (top) values, respectively, to prevent the bottom edge from crossing over the top edge and right edge from crossing over the left edge. For example, `rect(10px 0 0 20px)` is clamped to `rect(10px 20px 10px 20px)`.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#auto)

Makes the edge for which this value is used to coincide with the corresponding edge of the containing block. If `auto` is used for the first (top) or fourth (left) value, the value of `auto` is `0`, and if used for the second (right) or third (bottom) value, the value of `auto` is `100%`.

[`round <'border-radius'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#round_border-radius)

Specifies the radius of the rounded corners of the rectangle using the same syntax as the CSS [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 shorthand property. This parameter is optional.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#formal_syntax)

------------------------------------------------------------------------------------------------------------------

<rect()> =   
  rect( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 auto [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{4}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#examples)

--------------------------------------------------------------------------------------------------------

### [Creating offset-path using rect()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#creating_offset-path_using_rect)

In this example, the [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 property uses the `rect()` function to define the shape of the path on which the element, a red box in this case, moves. Three different scenarios are shown, each using different values for the `rect()` function. The arrow inside the boxes points to the right edge of the box.

html

    <div class="container">
      Rectangular path 1
      <div class="path rect-path-1">→</div>
    </div>
    <div class="container">
      Rectangular path 2
      <div class="path rect-path-2">→</div>
    </div>
    <div class="container">
      Rectangular path 3
      <div class="path rect-path-3">→</div>
    </div>
    

css

    .container {
      position: relative;
      display: inline-block;
      width: 200px;
      height: 200px;
      border: 1px solid black;
      margin: 15px;
      text-align: center;
    }
    
    .path {
      width: 40px;
      height: 40px;
      background-color: red;
      position: absolute;
      animation: move 10s linear infinite;
    }
    
    .rect-path-1 {
      offset-path: rect(50px 150px 200px 50px round 20%);
    }
    
    .rect-path-2 {
      offset-path: rect(50px auto 200px 50px round 20%);
    }
    
    .rect-path-3 {
      offset-path: rect(50px auto 200px auto);
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

*   The path 1 rectangle specifies the distances of the four edges (top, right, bottom, and left) from the containing block. The top and bottom values are distances from the top edge of the containing block. The right and left values are distances from the left edge of the containing block. In addition, the corner of the rectangle is rounded at `20%`, making the red box element follow the rounded corners as it moves along this path. Notice how the arrow inside the box follows curve at the rectangular path corners.
*   The path 2 rectangle is similar to the path 1 rectangle, except that the right value is `auto`, which is equal to the value `100%`. This causes the right edge of the rectangle to match the right edge of the containing block, creating a wider rectangle than path 1.
*   The path 3 rectangle specifies both the left and right edge parameters as `auto` and omits the `round <'border-radius'>` parameter. This creates a rectangle that has the width of the containing block and rectangular corners instead of rounded corners like in path 1 and path 2 rectangles. Notice the movement of the arrow inside this box at the corners.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shapes Module Level 1  <br>\# funcdef-basic-shape-rect](https://drafts.csswg.org/css-shapes-1/#funcdef-basic-shape-rect) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect#see_also)

--------------------------------------------------------------------------------------------------------

*   [`inset()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/inset)
     function
*   [`xywh()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/xywh)
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

This page was last modified on Jul 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/rect/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/basic-shape/rect/index.md?plain=1 "Folder: en-us/web/css/reference/values/basic-shape/rect (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Frect&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Frect%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Frect%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Frect%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcd0970bc03cf30a9a8089954cc542a17dbe9eba3%0A*+Document+last+modified%3A+2026-07-16T09%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")