*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#mdn-search)
    

`<line-style>` CSS type
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<line-style>`** [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 value type represents keyword values that define the style of a line, or the lack of a line. The `<line-style>` keyword values are used in the following longhand and shorthand [border](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
 and [gap decoration](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
 properties:

*   [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
    , [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
    
*   [`border-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block)
    , [`border-block-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-style)
    
*   [`border-block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end)
    , [`border-block-end-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style)
    
*   [`border-block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start)
    , [`border-block-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-style)
    
*   [`border-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom)
    , [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
    
*   [`border-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline)
    , [`border-inline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-style)
    
*   [`border-inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end)
    , [`border-inline-end-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-style)
    
*   [`border-inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start)
    , [`border-inline-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-style)
    
*   [`border-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left)
    , [`border-left-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style)
    
*   [`border-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right)
    , [`border-right-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style)
    
*   [`border-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top)
    , [`border-top-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
    
*   [`column-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule)
    , [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
    
*   [`row-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule)
    , [`row-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/row-rule-style)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#syntax)

----------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#values)

The `<line-style>` enumerated type is specified using one of the values listed below:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#none)

Displays no line. The [used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
 of the line width is `0` even if a width value is specified. In the case of table cell and border collapsing, the `none` value has the _lowest_ priority. If any other conflicting border is set, it will be displayed. The `none` value is similar to `hidden`.

[`hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#hidden)

Displays no line. The [used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
 of the line width is `0` even if a width value is specified. In the case of table cell and border collapsing, the `hidden` value has the _highest_ priority. If any other conflicting border is set, it won't be displayed. The `hidden` value is similar to `none`, but `hidden` is not a valid value for outline styles.

[`dotted`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#dotted)

Displays a series of round dots. The radius of the dots is half the computed value of the line's width. The spacing of the dots is not defined by the specification and is implementation-specific.

[`dashed`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#dashed)

Displays a series of short square-ended dashes or line segments. The exact size and length of the segments are not defined by the specification and are implementation-specific.

[`solid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#solid)

Displays a single, straight solid line.

[`double`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#double)

Displays two straight lines with some space between them. The length of the lines adds up to the pixel size defined by the line's width.

[`groove`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#groove)

Displays a border with a carved appearance. This value is the opposite of `ridge`.

[`ridge`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#ridge)

Displays a border with an extruded appearance. This value is the opposite of `groove`.

[`inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#inset)

Displays a border that makes the element appear embedded. This value is the opposite of `outset`. When applied to a table cell border and [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
 is set to `collapsed`, this value behaves like `groove`.

[`outset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#outset)

Displays a border that makes the element appear embossed. This value is the opposite of `inset`. When applied to a table cell with [`border-collapse`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-collapse)
 set to `collapsed`, this value behaves like `ridge`.

**Note:** When `<outline-style>` is used as the value type for [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
 and [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
 properties, it is similar to `<line-style>`, but does not support `hidden` and includes the `auto` value. When `auto` is set, the user-agent defined `<line-style>` value is used.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#formal_syntax)

------------------------------------------------------------------------------------------------------------

<line-style> =   
  none    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  hidden  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dotted  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  dashed  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  solid   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  double  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  groove  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ridge   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inset   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  outset    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#examples)

--------------------------------------------------------------------------------------------------

The first example demonstrates all the `<line-style>` keyword values. The second example demonstrates how some line style colors may display in unexpected ways.

### [Defining line styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#defining_line_styles)

This example shows all the `<line-style>` values as values for the CSS [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
 and [`column-rule-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-style)
 properties.

#### HTML

This example uses multiple [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, each with a class representing the `<line-style>` value that is being demonstrated.

#### CSS

In the CSS for this example, the border and the column-rule for all the `<p>` elements is defined to have a width of `7px` and the style value of `double`. For each paragraph, the `double` value is then overridden by specifying a different `<line-style>` value for the `border-style` and `column-rule-style` properties.

#### Result

Notice that the black border is not always black.

### [Defining line styles and colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#defining_line_styles_and_colors)

This example demonstrates line-style and color choice. With some `<line-style>` keyword values, the color of the line may not be what you expect. To create the required "3D" effect of `groove`, `ridge`, `inset`, and `outset` styles when displaying these values in black or white, user agents use different color calculations than any other color-line combinations.

#### CSS

The four sides of each `<div>` have a different `<line-style>` value, and each list item has a different [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value. We use [generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
 to display the CSS declared inline.

    body {
      display: flex;
      flex-wrap: wrap;
      gap: 1em;
      text-transform: uppercase;
      font-family: monospace;
    }
    

css

    div {
      border-width: 10px;
      border-style: inset groove ridge outset;
      padding: 5px;
    }
    

#### JavaScript

The JavaScript dynamically creates [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, each with a different `border-color` set.

js

    // prettier-ignore
    const colors = [\
      "#000000", "#000001", "#ffffff",\
      "#ff00ff", "#ffff00", "#00ffff",\
      "#cc33cc", "#cccc33", "#33cccc",\
      "#ff0000", "#00ff00", "#0000ff",\
      "#cc3333", "#33cc33", "#3333cc",\
      "#993333", "#339933", "#333399",\
    ];
    
    for (const c of colors) {
      const div = document.createElement("div");
      div.style.borderColor = c;
      div.textContent = c;
      document.body.appendChild(div);
    }
    

#### Result

Notice that the almost-black color of `#000001` may be different from the actual black, and the contrast between the dark and light edges is more noticeable when using lighter colors.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Backgrounds and Borders Module Level 3  <br>\# typedef-line-style](https://drafts.csswg.org/css-backgrounds/#typedef-line-style) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style#see_also)

--------------------------------------------------------------------------------------------------

*   [`<line-width>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-width)
     data type
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module
*   [CSS basic user interface](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface)
     module
*   [CSS gaps](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Gaps)
     module
*   [CSS multi-column layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Multicol_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/line-style/index.md?plain=1 "Folder: en-us/web/css/reference/values/line-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fline-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fline-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fline-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fline-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9c03ba87f9ff4123150d8f7dc457bd546bdab83%0A*+Document+last+modified%3A+2026-07-24T10%3A23%3A51.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")