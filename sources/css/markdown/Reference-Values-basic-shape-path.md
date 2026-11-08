*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#mdn-search)
    

`path()` CSS function
=====================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2020.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/313)

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`path()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions)
 accepts an [SVG path](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
 string, and is used in the [CSS shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
 and [CSS motion path](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Motion_path)
 modules to enable a shape to be drawn. The `path()` function is a [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 data type value. It can be used in the CSS [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 and [`clip-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/clip-path)
 properties and in the SVG [`d`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d)
 attribute.

There are some limitations to using the `path()` function. The path has to be defined as a single string, so a custom path can't be created using variables ([`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
 functions). Also, all the lengths in the path are implicitly defined in [pixel](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Numeric_data_types#absolute_length_units)
 (`px`) units; other units can't be used. The [`shape()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/shape)
 function offers more flexibility than the `path()` function.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#try_it)

----------------------------------------------------------------------------------------------------

    clip-path: path(
      "M  20  240 \
     L  20  80 L 160  80 \
     L 160  20 L 280 100 \
     L 160 180 L 160 120 \
     L  60 120 L  60 240 Z"
    );
    

    clip-path: path(
      "M 20 240 \
     C 20 0 300 0 300 240 Z"
    );
    

    <section class="default-example" id="default-example">
      <div class="transition-all" id="example-element"></div>
    </section>
    

    #default-example {
      background: #ffee99;
    }
    
    #example-element {
      background: linear-gradient(to bottom right, #ff5522, #0055ff);
      width: 100%;
      height: 100%;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#syntax)

----------------------------------------------------------------------------------------------------

css

    path("M 10 80 C 40 10, 65 10, 95 80 S 150 150, 180 80")
    
    /* When used in clip-path only */
    path(evenodd,"M 10 80 C 40 10, 65 10, 95 80 S 150 150, 180 80")
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#parameters)

[`<fill-rule>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill-rule)
 Optional

Defines what parts of the path are inside the shape. The possible values include:

*   `nonzero`: A point is considered inside the shape if a ray drawn from the point crosses more left-to-right than right-to-left path segments, resulting in a non-zero count. This is the default value when `<fill-rule>` is omitted.
    
*   `evenodd`: A point is considered to be inside the shape if a ray drawn from the point crosses an odd number of path segments. This means that for each time the ray enters the shape, it has not exited an equal number of times, indicating an odd count of entries without corresponding exits.
    

**Warning:** `<fill-rule>` is not supported in [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 and using it invalidates the property.

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)

A [data string](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d)
, contained in quotes, which defines an [SVG path](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/path)
. The SVG path data string contains [path commands](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d#path_commands)
 that implicitly use pixel units. An empty path is considered invalid.

### [Return value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#return_value)

Returns a [`<basic-shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape)
 value.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#formal_syntax)

------------------------------------------------------------------------------------------------------------------

<path()> =   
  path( [<'fill-rule'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 , [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 )    
  
[<fill-rule>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/fill-rule)
 =   
  nonzero  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  evenodd    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#examples)

--------------------------------------------------------------------------------------------------------

### [Using a `path()` function as an `offset-path` value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#using_a_path_function_as_an_offset-path_value)

A `path()` function has been provided as an [`offset-path`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/offset-path)
 value in the following example to create an elliptical path for a ball to move along.

html

    <div id="path">
      <div id="ball"></div>
    </div>
    <button>animate</button>
    

css

    #path {
      margin: 40px;
      width: 400px;
      height: 200px;
    
      /* draw the gray ramp */
      background: radial-gradient(at 50% 0%, transparent 70%, grey 70%, grey 100%);
    }
    
    #ball {
      width: 30px;
      height: 30px;
      background-color: red;
      border-radius: 50%;
    
      /* mark the elliptical path */
      offset-path: path("M 15 15 A 6 5.5 10 0 0 385 15");
    }
    

js

    const btn = document.querySelector("button");
    const ball = document.getElementById("ball");
    
    btn.addEventListener("click", () => {
      btn.setAttribute("disabled", true);
      setTimeout(() => btn.removeAttribute("disabled"), 6000);
    
      ball.animate(
        // animate the offset path
        { offsetDistance: [0, "100%"] },
        {
          duration: 1500,
          iterations: 4,
          easing: "cubic-bezier(.667,0.01,.333,.99)",
          direction: "alternate",
        },
      );
    });
    

### [Modify the value of the SVG path d attribute](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#modify_the_value_of_the_svg_path_d_attribute)

The `path()` can be used to modify the value of the SVG [`d` attribute](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/d)
, which can also be set to `none` in your CSS.

The "V" symbol will flip vertically when you hover over it, if `d` is supported as a CSS property.

#### CSS

css

    html,
    body,
    svg {
      height: 100%;
    }
    
    /* This path is displayed on hover */
    #svg_css_ex1:hover path {
      d: path("M20,80 L50,20 L80,80");
    }
    

#### HTML

html

    <svg id="svg_css_ex1" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
      <path fill="none" stroke="red" d="M20,20 L50,80 L80,20" />
    </svg>
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Shapes Module Level 1  <br>\# funcdef-basic-shape-path](https://drafts.csswg.org/css-shapes/#funcdef-basic-shape-path) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path#see_also)

--------------------------------------------------------------------------------------------------------

*   [`border-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-shape)
    , [`shape-outside`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/shape-outside)
    
*   [CSS shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes)
     module
*   [Overview of CSS shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shapes/Overview)
    
*   [The SVG `path` syntax: an illustrated guide](https://css-tricks.com/svg-path-syntax-illustrated-guide/ "External link (opens in new tab)")
     via CSS-tricks (2021)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/basic-shape/path/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/basic-shape/path/index.md?plain=1 "Folder: en-us/web/css/reference/values/basic-shape/path (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Fpath&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Fpath%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fbasic-shape%2Fpath%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fbasic-shape%2Fpath%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fcd0970bc03cf30a9a8089954cc542a17dbe9eba3%0A*+Document+last+modified%3A+2026-07-16T09%3A56%3A16.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")