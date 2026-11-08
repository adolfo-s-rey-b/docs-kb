*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#mdn-search)
    

`inherits` CSS at-rule descriptor
=================================

Baseline 2024

Newly available

Since July 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`inherits`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 descriptor of the [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 controls whether or not the registered [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 inherits by default. It is a required descriptor; if missing or invalid, the entire `@property` rule is invalid and ignored.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#syntax)

--------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#values)

[`true`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#true)

The property inherits by default.

[`false`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#false)

The property does not inherit by default.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

inherits =   
  true   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  false    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#examples)

------------------------------------------------------------------------------------------------------------

### [Setting inheritance behavior of a custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#setting_inheritance_behavior_of_a_custom_property)

This example shows how to define a custom property `--my-color` that does not inherit its value from its parent elements:

Using [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
 [`CSS.registerProperty()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/registerProperty_static "CSS.registerProperty()")
:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Properties and Values API Level 1  <br>\# inherits-descriptor](https://drafts.css-houdini.org/css-properties-values-api/#inherits-descriptor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits#see_also)

------------------------------------------------------------------------------------------------------------

*   Other [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
     descriptors: [`initial-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value)
     and [`syntax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)
    
*   [Registering CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Registering_properties)
    
*   [CSS Properties and Values API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Properties_and_Values_API)
    
*   [CSS Painting API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Painting_API)
    
*   [CSS Typed Object Model](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Typed_OM_API)
    
*   [Houdini APIs](https://developer.mozilla.org/en-US/docs/Web/API/Houdini_APIs)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@property/inherits/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@property/inherits (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40property%2Finherits&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40property%2Finherits%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40property%2Finherits%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40property%2Finherits%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")