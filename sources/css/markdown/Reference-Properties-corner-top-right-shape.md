*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#mdn-search)
    

`corner-top-right-shape` CSS property
=====================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/398)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#browser_compatibility)
 carefully before using this in production.

The **`corner-top-right-shape`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the shape of a box's top-right corner, within its [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
 area.

For a full description of corner shape behavior and multiple examples, see the [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 shorthand property page.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#syntax)

--------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    corner-top-right-shape: scoop;
    corner-top-right-shape: square;
    
    /* superellipse() function values */
    corner-top-right-shape: superellipse(2.2);
    corner-top-right-shape: superellipse(-2.5);
    
    /* Global values */
    corner-top-right-shape: inherit;
    corner-top-right-shape: initial;
    corner-top-right-shape: revert;
    corner-top-right-shape: revert-layer;
    corner-top-right-shape: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#values)

The `corner-top-right-shape` property is specified using a [`<corner-shape-value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/corner-shape-value)
 value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `round` |
| Applies to | all elements. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | The corresponding [superellipse()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/superellipse)<br> value. |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Animates as per [superellipse interpolation](https://drafts.csswg.org/css-borders/#superellipse-interpolation "External link (opens in new tab)")<br>. |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

corner-top-right-shape =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#examples)

------------------------------------------------------------------------------------------------------------------

You can find other related examples on the [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 reference page.

### [Basic `corner-top-right-shape` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#basic_corner-top-right-shape_usage)

#### HTML

The markup for this example contains a single [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element.

html

    <div></div>
    

#### CSS

We give the box some basic styles, which we've hidden for brevity. We also apply a [`box-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-shadow)
, a `border-radius` of 60 pixels, and a `corner-top-right-shape` of `bevel`.

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
      background-color: green;
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
      corner-top-right-shape: bevel;
    }
    

#### Result

The rendered result looks like this:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Borders and Box Decorations Module Level 4  <br>\# propdef-corner-top-right-shape](https://drafts.csswg.org/css-borders/#propdef-corner-top-right-shape) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`corner-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
     shorthand property
*   [`corner-top-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-left-shape)
    , [`corner-bottom-left-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-left-shape)
    , and [`corner-bottom-right-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-bottom-right-shape)
    
*   [`corner-start-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-start-shape)
    , [`corner-start-end-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-start-end-shape)
    , [`corner-end-start-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-end-start-shape)
    , and [`corner-end-end-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-end-end-shape)
    
*   [`border-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-radius)
     shorthand property
*   [`border-top-right-radius`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-right-radius)
    
*   [CSS borders and box decorations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Borders_and_box_decorations)
     module
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-top-right-shape/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/corner-top-right-shape/index.md?plain=1 "Folder: en-us/web/css/reference/properties/corner-top-right-shape (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcorner-top-right-shape&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcorner-top-right-shape%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcorner-top-right-shape%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcorner-top-right-shape%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")