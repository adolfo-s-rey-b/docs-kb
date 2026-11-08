*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#mdn-search)
    

`syntax` CSS at-rule descriptor
===============================

Baseline 2024

Newly available

Since July 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`syntax`** descriptor of the [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 defines the allowed value types for the registered [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
. It controls how the property's specified value is processed to derive the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
. It is a required descriptor; if missing or invalid, the entire `@property` rule is invalid and ignored.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#syntax)

------------------------------------------------------------------------------------------------------

css

    /* A data type name */
    syntax: "<color>";
    
    /* A '|' combinator for multiple data types */
    syntax: "<length> | <percentage>";
    
    /* Space-separated list of values */
    syntax: "<color>+";
    
    /* Comma-separated list of values */
    syntax: "<length>#";
    
    /* Keywords */
    syntax: "small | medium | large";
    
    /* Combination of data type and keyword */
    syntax: "<length> | auto";
    
    /* Universal syntax value */
    syntax: "*";
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#values)

A string (known as the syntax string) that defines the allowed values. It can be one of the following:

*   One or more syntax component names, which can be:
    *   Data type names (written with angle brackets, such as `<color>` or `<length>`)
    *   Keywords (written without angle brackets, such as `auto` or `none`)
*   The universal syntax `*`, which accepts any valid CSS value. It cannot be multiplied or combined with other syntax components.

The syntax component names can be used alone or multiplied and combined in different ways:

*   The `+` (space-separated) and `#` (comma-separated) multipliers indicate that a list of values is expected. For example, `<color>#` means a comma-separated list of `<color>` values is the expected syntax.
    
*   The vertical line (`|`) combinator can create "or" conditions for the expected syntax. For example, `<length> | auto` accepts `<length>` or `auto`, and `<color># | <integer>#` expects a comma-separated list of `<color>` values or a comma-separated list of `<integer>` values.
    

The following syntax component names are supported:

[`"<angle>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#angle)

Accepts any valid [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
 value.

[`"<color>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#color)

Accepts any valid [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value.

[`"<custom-ident>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#custom-ident)

Accepts any valid [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 value.

[`"<image>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#image)

Accepts any valid [`<image>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/image)
 value.

[`"<integer>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#integer)

Accepts any valid [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 value.

[`"<length>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#length)

Accepts any valid [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value.

[`"<length-percentage>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#length-percentage)

Accepts any valid [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value and any valid [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
 expression combining `<length>` and `<percentage>` values.

[`"<number>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#number)

Accepts any valid [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
 value.

[`"<percentage>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#percentage)

Accepts any valid [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 value.

[`"<resolution>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#resolution)

Accepts any valid [`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
 value.

[`"<string>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#string)

Accepts any valid [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 value.

[`"<time>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#time)

Accepts any valid [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
 value.

[`"<transform-function>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#transform-function)

Accepts any valid [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 value.

[`"<transform-list>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#transform-list)

Accepts a list of valid [`<transform-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/transform-function)
 values. It is equivalent to `"<transform-function>+"`.

[`"<url>"`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#url)

Accepts any valid [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `n/a (required)` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

syntax =   
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#examples)

----------------------------------------------------------------------------------------------------------

### [Registering a custom property with type checking](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#registering_a_custom_property_with_type_checking)

This example shows how to define a custom property `--my-color` that allows only `<color>` values:

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
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Properties and Values API Level 1  <br>\# the-syntax-descriptor](https://drafts.css-houdini.org/css-properties-values-api/#the-syntax-descriptor) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax#see_also)

----------------------------------------------------------------------------------------------------------

*   Other [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
     descriptors: [`inherits`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits)
     and [`initial-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value)
    
*   [Registering CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Registering_properties)
    
*   [CSS Properties and Values API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Properties_and_Values_API)
    
*   [CSS Painting API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Painting_API)
    
*   [CSS Typed Object Model](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Typed_OM_API)
    
*   [Houdini APIs](https://developer.mozilla.org/en-US/docs/Web/API/Houdini_APIs)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@property/syntax/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@property/syntax (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40property%2Fsyntax&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40property%2Fsyntax%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40property%2Fsyntax%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40property%2Fsyntax%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")