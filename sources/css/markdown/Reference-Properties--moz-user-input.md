*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#mdn-search)
    

`-moz-user-input` CSS property
==============================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

In Mozilla applications, **`-moz-user-input`** determines if an element will accept user input.

As of Firefox 60, this property can no longer grant an element the ability to accept user input if it normally does not. It may only be used to disable user input.

The `user-input` property is currently not on a standards track.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    -moz-user-input: auto;
    -moz-user-input: none;
    
    /* Global values */
    -moz-user-input: inherit;
    -moz-user-input: initial;
    -moz-user-input: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#auto)

The element will respond to user input if it normally takes user input, such as a [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#none)

The element does not respond to user input, and it does not become [`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

\-moz-user-input =   
  auto  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#examples)

-----------------------------------------------------------------------------------------------------------

### [Disabling user input for an element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#disabling_user_input_for_an_element)

css

    input.example {
      /* The user will be able to select the text, but not change it. */
      -moz-user-input: none;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#specifications)

-----------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`-moz-user-focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus)
    
*   [`-moz-user-modify`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify)
    
*   [`-moz-user-select`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/-moz-user-input/index.md?plain=1 "Folder: en-us/web/css/reference/properties/-moz-user-input (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-moz-user-input&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-moz-user-input%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-moz-user-input%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-moz-user-input%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F22c0b3059ff71d769af670478cc41605581108d1%0A*+Document+last+modified%3A+2026-09-10T13%3A27%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")