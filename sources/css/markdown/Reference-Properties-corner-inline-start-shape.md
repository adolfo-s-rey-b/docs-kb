*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#mdn-search)
    

`corner-inline-start-shape` CSS property
========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/398)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#browser_compatibility)
 carefully before using this in production.

The **`corner-inline-start-shape`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the shape of both the corners on a box's inline-start edge, within their [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 area.

For a full description of corner shape behavior and multiple examples, see the [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 shorthand property page.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following logical properties:

*   [`corner-start-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-start-shape)
    
*   [`corner-end-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-end-start-shape)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#syntax)

-----------------------------------------------------------------------------------------------------------------

css

    /* Single keyword value set for both corners */
    corner-inline-start-shape: round;
    corner-inline-start-shape: bevel;
    
    /* Single superellipse() value set for both corners */
    corner-inline-start-shape: superellipse(0.5);
    corner-inline-start-shape: superellipse(-3);
    
    /* Block-start/inline-start corner, block-end/inline-start corner */
    corner-inline-start-shape: round bevel;
    corner-inline-start-shape: round superellipse(0.5);
    
    /* Global values */
    corner-inline-start-shape: inherit;
    corner-inline-start-shape: initial;
    corner-inline-start-shape: revert;
    corner-inline-start-shape: revert-layer;
    corner-inline-start-shape: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#values)

The `corner-inline-start-shape` property is specified using one or two [`<corner-shape-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)
 values:

*   If **one value** is used, it specifies the shape of **both inline-start** corners.
*   If **two values** are used, the first one specifies the shape of the **block-start/inline-start** corner, and the second one specifies the shape of the **block-end/inline-start** corner.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`corner-start-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-start-shape)<br>    : `round`<br>*   [`corner-start-end-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-end-shape)<br>    : `round` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`corner-start-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-start-shape)<br>    : The corresponding [superellipse()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)<br>     value.<br>*   [`corner-start-end-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-end-shape)<br>    : The corresponding [superellipse()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)<br>     value. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`corner-start-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-start-shape)<br>    : Animates as per [superellipse interpolation](https://drafts.csswg.org/css-borders/#superellipse-interpolation "External link (opens in new tab)")<br>    .<br>*   [`corner-start-end-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-end-shape)<br>    : Animates as per [superellipse interpolation](https://drafts.csswg.org/css-borders/#superellipse-interpolation "External link (opens in new tab)")<br>    . |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------------

corner-inline-start-shape =   
  [<'corner-top-left-shape'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-left-shape)
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#examples)

---------------------------------------------------------------------------------------------------------------------

You can find other related examples on the [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 reference page.

### [Basic `corner-inline-start-shape` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#basic_corner-inline-start-shape_usage)

#### HTML

The markup for this example contains a single [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element.

html

    <div></div>
    

#### CSS

We give the box some basic styles, which we've hidden for brevity. We also apply a [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
, a `border-radius` of 60 pixels, and a `corner-inline-start-shape` of `square bevel`.

    body {
      font-family: "Helvetica", "Arial", sans-serif;
      width: 240px;
      margin: 20px auto;
    }
    
    div {
      width: 100%;
      height: 180px;
      display: flex;
      justify-content: center;
      align-items: center;
      background-color: orange;
      background-image: linear-gradient(
        to bottom,
        rgb(255 255 255 / 0),
        rgb(255 255 255 / 0.5)
      );
    }
    

css

    div {
      box-shadow: 1px 1px 3px gray;
      border-radius: 60px;
      corner-inline-start-shape: square bevel;
    }
    

#### Result

The rendered result looks like this:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Borders and Box Decorations Module Level 4  <br>\# propdef-corner-inline-start-shape](https://drafts.csswg.org/css-borders/#propdef-corner-inline-start-shape) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
     shorthand property
*   [`corner-block-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-block-start-shape)
    , [`corner-block-end-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-block-end-shape)
    , and [`corner-inline-end-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-end-shape)
    
*   [`corner-top-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-shape)
    , [`corner-bottom-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-shape)
    , [`corner-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-left-shape)
    , and [`corner-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-right-shape)
    
*   [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
     shorthand property
*   [`border-start-start-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-start-start-radius)
     and [`border-end-start-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-end-start-radius)
    
*   [CSS borders and box decorations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations)
     module
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-inline-start-shape/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/corner-inline-start-shape/index.md?plain=1 "Folder: en-us/web/css/reference/properties/corner-inline-start-shape (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcorner-inline-start-shape&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcorner-inline-start-shape%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcorner-inline-start-shape%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcorner-inline-start-shape%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")