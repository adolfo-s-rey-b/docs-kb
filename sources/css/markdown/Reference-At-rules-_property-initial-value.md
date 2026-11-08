*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#mdn-search)
    

`initial-value` CSS at-rule descriptor
======================================

Baseline 2024

Newly available

Since July 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`initial-value`** descriptor of the [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 specifies the initial value for the registered [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
. It is a required descriptor unless the [`syntax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)
 descriptor value is the universal syntax (`*`). If required but missing or invalid, the entire `@property` rule is invalid and ignored.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Set initial color value */
    initial-value: rebeccapurple;
    
    /* Set initial length value */
    initial-value: 16px;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#values)

A value that matches the type specified in the [`syntax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)
 descriptor. For example, if `syntax` is `<color>`, then the `initial-value` must be a valid [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 value.

If the value of the `syntax` descriptor is not the universal syntax definition, the `initial-value` descriptor has to be a [computationally independent](https://drafts.css-houdini.org/css-properties-values-api-1/#computationally-independent "External link (opens in new tab)")
 value. This means the value can be converted into a computed value without depending on other values, except for "global" definitions independent of CSS. For example, `10px` is computationally independent—it doesn't change when converted to a computed value. `2in` is also valid, because `1in` is always equivalent to `96px`. However, `3em` is not valid, because the value of an `em` is dependent on the parent's [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `n/a (required)` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

initial-value =   
  <declaration-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#examples)

-----------------------------------------------------------------------------------------------------------------

### [Setting an initial value for a custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#setting_an_initial_value_for_a_custom_property)

This example shows how to define a custom property `--my-color` with an initial color value of `#c0ffee`. This initial value will be used when the property is not inherited (`inherits: false`) and no other value is set on the element.

css

    @property --my-color {
      syntax: "<color>";
      inherits: false;
      initial-value: #c0ffee;
    }
    

Using [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
 [`CSS.registerProperty()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/registerProperty_static "CSS.registerProperty()")
:

js

    window.CSS.registerProperty({
      name: "--my-color",
      syntax: "<color>",
      inherits: false,
      initialValue: "#c0ffee",
    });
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Properties and Values API Level 1  <br>\# initial-value-descriptor](https://drafts.css-houdini.org/css-properties-values-api/#initial-value-descriptor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value#see_also)

-----------------------------------------------------------------------------------------------------------------

*   Other [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
     descriptors: [`inherits`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits)
     and [`syntax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)
    
*   [Registering CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Registering_properties)
    
*   [CSS Properties and Values API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Properties_and_Values_API)
    
*   [CSS Painting API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Painting_API)
    
*   [CSS Typed Object Model](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Typed_OM_API)
    
*   [Houdini APIs](https://developer.mozilla.org/en-US/docs/Web/API/Houdini_APIs)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@property/initial-value/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@property/initial-value (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40property%2Finitial-value&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40property%2Finitial-value%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40property%2Finitial-value%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40property%2Finitial-value%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")