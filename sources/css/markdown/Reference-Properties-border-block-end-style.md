*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#mdn-search)
    

`border-block-end-style` CSS property
=====================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`border-block-end-style`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property defines the style of the logical block-end border of an element, which maps to a physical border style depending on the element's writing mode, directionality, and text orientation. It corresponds to the [`border-top-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
, [`border-right-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style)
, [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
, or [`border-left-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style)
 property depending on the values defined for [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
, [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
, and [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#try_it)

--------------------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#syntax)

--------------------------------------------------------------------------------------------------------------

Related properties are [`border-block-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-start-style)
, [`border-inline-start-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-start-style)
, and [`border-inline-end-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-inline-end-style)
, which define the other border styles of the element.

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#values)

[`<line-style>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)

The line style of the border. See [`border-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-style)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#formal_definition)

------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#formal_syntax)

----------------------------------------------------------------------------------------------------------------------------

border-block-end-style =   
  <line-style>    
  
[<line-style>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/line-style)
 =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#examples)

------------------------------------------------------------------------------------------------------------------

### [Dashed border with vertical text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#dashed_border_with_vertical_text)

#### HTML

#### CSS

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Logical Properties and Values Module Level 1  <br>\# border-style](https://drafts.csswg.org/css-logical/#border-style) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style#see_also)

------------------------------------------------------------------------------------------------------------------

*   [CSS Logical Properties and Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values)
    
*   This property maps to one of the physical border properties: [`border-top-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-top-style)
    , [`border-right-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-right-style)
    , [`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
    , and [`border-left-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-left-style)
    .
*   [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
    , [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
    , [`text-orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-orientation)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-block-end-style/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/border-block-end-style/index.md?plain=1 "Folder: en-us/web/css/reference/properties/border-block-end-style (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-block-end-style&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-block-end-style%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fborder-block-end-style%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fborder-block-end-style%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe9c03ba87f9ff4123150d8f7dc457bd546bdab83%0A*+Document+last+modified%3A+2026-07-24T10%3A23%3A51.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")