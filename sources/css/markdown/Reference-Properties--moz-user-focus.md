*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#mdn-search)
    

`-moz-user-focus` CSS property
==============================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`-moz-user-focus`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property is used to indicate whether an element can have the focus.

By setting its value to `ignore`, you can disable focusing the element, which means that the user will not be able to activate the element, and the element will be skipped in the tab sequence. The default is `none`, which disables focussing on the element and removes focus on other elements if there is an attempt to select the element.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#syntax)

-------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#values)

This property is specified as one of the following keyword values:

[`ignore`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#ignore)

The element does not accept keyboard focus and will be skipped in the tab order.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#normal)

The element can accept keyboard focus.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#none)

The element does not accept keyboard focus. Attempting to select the element removes focus from any other element.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

\-moz-user-focus =   
  ignore  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  normal  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#examples)

-----------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#css)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#specifications)

-----------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`-moz-user-input`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input)
    
*   [`user-modify`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify)
    
*   [`-moz-user-select`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/-moz-user-focus/index.md?plain=1 "Folder: en-us/web/css/reference/properties/-moz-user-focus (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-moz-user-focus&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-moz-user-focus%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-moz-user-focus%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-moz-user-focus%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F22c0b3059ff71d769af670478cc41605581108d1%0A*+Document+last+modified%3A+2026-09-10T13%3A27%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")