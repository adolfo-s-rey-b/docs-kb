*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#mdn-search)
    

`box-orient` CSS property
=========================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Warning:** This is a property of the original CSS flexible box layout Module draft, and has been replaced by a newer standard. See [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts)
 for information about the current standard.

The **`box-orient`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether an element lays out its contents horizontally or vertically.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    box-orient: horizontal;
    box-orient: vertical;
    box-orient: inline-axis;
    box-orient: block-axis;
    
    /* Global values */
    box-orient: inherit;
    box-orient: initial;
    box-orient: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#values)

This property is specified as one of the following keyword values:

[`horizontal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#horizontal)

The box lays out its contents horizontally.

[`vertical`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#vertical)

The box lays out its contents vertically.

[`inline-axis` (HTML)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#inline-axis)

The box displays its children along the inline axis.

[`block-axis` (HTML)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#block-axis)

The box displays its children along the block axis.

The inline and block axes are the writing-mode dependent keywords which, in English, map to `horizontal` and `vertical` respectively.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#description)

------------------------------------------------------------------------------------------------------------

HTML DOM elements lay out their contents along the inline-axis by default. This CSS property will only apply to HTML elements with a CSS [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 value of `box` or `inline-box`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `inline-axis` |
| Applies to | elements with a CSS [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)<br> value of `box` or `inline-box` |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#formal_syntax)

----------------------------------------------------------------------------------------------------------------

box-orient =   
  horizontal   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  vertical     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline-axis  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block-axis     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#examples)

------------------------------------------------------------------------------------------------------

### [Setting horizontal box orientation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#setting_horizontal_box_orientation)

Here, the `box-orient` property will cause the two [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 sections in the example to display in the same line.

#### HTML

html

    <div class="example">
      <p>I will be to the left of my sibling.</p>
      <p>I will be to the right of my sibling.</p>
    </div>
    

#### CSS

css

    div.example {
      display: -moz-box; /* Mozilla */
      display: -webkit-box; /* WebKit */
      display: box; /* As specified */
    
      /* Children should be oriented vertically */
      -moz-box-orient: horizontal; /* Mozilla */
      -webkit-box-orient: horizontal; /* WebKit */
      box-orient: horizontal; /* As specified */
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#specifications)

------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient#see_also)

------------------------------------------------------------------------------------------------------

*   [`box-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-direction)
    
*   [`box-pack`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-pack)
    
*   [`box-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-align)
    
*   [`flex-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-direction)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/box-orient/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/box-orient/index.md?plain=1 "Folder: en-us/web/css/reference/properties/box-orient (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-orient&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-orient%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fbox-orient%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fbox-orient%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")