*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#mdn-search)
    

`@property` CSS at-rule
=======================

Baseline 2024

Newly available

Since July 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@property`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 is used to explicitly define [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
, allowing for property type checking and constraining, setting default values, and defining whether a custom property can inherit values or not.

**Note:** The JavaScript [`registerProperty()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/registerProperty_static "registerProperty()")
 method is equivalent to the `@property` at-rule.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#syntax)

-----------------------------------------------------------------------------------------------

css

    @property --canBeAnything {
      syntax: "*";
      inherits: true;
    }
    
    @property --rotation {
      syntax: "<angle>";
      inherits: false;
      initial-value: 45deg;
    }
    
    @property --defaultSize {
      syntax: "<length> | <percentage>";
      inherits: true;
      initial-value: 200px;
    }
    

The custom property name is a [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 that starts with `--` and is followed by a valid, user-defined identifier. It is case-sensitive.

### [Descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#descriptors)

[`syntax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)

A string that describes the allowed value types for the registered custom property.

[`inherits`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits)

A boolean value that controls whether the custom property registration specified by `@property` inherits by default.

[`initial-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value)

A value that sets the starting value for the property.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#description)

---------------------------------------------------------------------------------------------------------

The `@property` at-rule is part of the [CSS Houdini](https://developer.mozilla.org/en-US/docs/Web/API/Houdini_APIs)
 set of APIs. It allows developers to explicitly define [CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
, allowing for property type checking and constraining, setting default values, and defining whether a custom property can inherit values or not.

The `@property` rule enables custom property registration directly inside stylesheets without requiring any JavaScript. Valid `@property` rules produce registered custom properties, producing the same effect as calling [`registerProperty()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/registerProperty_static "registerProperty()")
 with equivalent parameters.

The following conditions must be met for the `@property` rule to be valid:

*   The `@property` rule must include both the [`syntax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)
     and [`inherits`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/inherits)
     descriptors. If either is missing, the entire `@property` rule is invalid and ignored.
*   The `syntax` may be a data type name (such as `<color>`, `<length>`, or `<number>`, etc.), with multipliers (`+` to accept a space-separated list, or `#` to accept a comma-separated list) and combinators (`|` to accept one data type or another), a custom ident, or the universal syntax definition (`*`), meaning the syntax can be any valid token stream. The value is a [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    . As such, it must be in quotes.
*   The [`initial-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value)
     descriptor is optional if the value of the `syntax` descriptor is the universal syntax definition (`syntax: "*"`). If the `initial-value` descriptor is required but omitted, the entire `@property` rule is invalid and ignored.
*   If the value of the `syntax` descriptor is not the universal syntax definition, the [`initial-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value)
     descriptor has to be a [computationally independent](https://drafts.css-houdini.org/css-properties-values-api-1/#computationally-independent "External link (opens in new tab)")
     value. This means the value can be converted into a computed value without depending on other values, except for "global" definitions independent of CSS. For example, `10px` is computationally independent—it doesn't change when converted to a computed value. `2in` is also valid, because `1in` is always equivalent to `96px`. However, `3em` is not valid, because the value of an `em` is dependent on the parent's [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
    .
*   Unknown descriptors are invalid and ignored, but do not invalidate the `@property` rule.

If multiple valid `@property` rules are defined using the same name, the last one in stylesheet order "wins". If custom properties are registered with the same name using `@property` in CSS and `CSS.registerProperty()` in JavaScript, the JavaScript registration wins.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#formal_syntax)

-------------------------------------------------------------------------------------------------------------

@property =   
  @property <custom-property-name>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 { <declaration-list> }    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#examples)

---------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#basic_example)

In this example, we use the `@property` at-rule to declare two custom properties, and then use those properties in our style declarations.

#### HTML

html

    <p>Hello world!</p>
    

#### CSS

css

    @property --myColor {
      syntax: "<color>";
      inherits: true;
      initial-value: rebeccapurple;
    }
    
    @property --myWidth {
      syntax: "<length> | <percentage>";
      inherits: true;
      initial-value: 200px;
    }
    
    p {
      background-color: var(--myColor);
      width: var(--myWidth);
      color: white;
    }
    

#### Results

The paragraph should be `200px` wide, with a purple background and white text.

### [Animating a custom property value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#animating_a_custom_property_value)

In this example, we define a custom property called `--progress` using `@property`: this accepts [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values and has an initial value of `25%`. We use `--progress` to define the position value of the color stops in a [`linear-gradient()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
, specifying where a green color stops, and black starts. We then animate the value of `--progress` to `100%` over 2.5 seconds, giving the effect of animating a progress bar.

#### HTML

html

    <div class="bar"></div>
    

#### CSS

css

    @property --progress {
      syntax: "<percentage>";
      inherits: false;
      initial-value: 25%;
    }
    
    .bar {
      display: inline-block;
      --progress: 25%;
      width: 100%;
      height: 5px;
      background: linear-gradient(
        to right,
        #00d230 var(--progress),
        black var(--progress)
      );
      animation: progressAnimation 2.5s ease infinite;
    }
    
    @keyframes progressAnimation {
      to {
        --progress: 100%;
      }
    }
    

#### Results

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Properties and Values API Level 1  <br>\# at-property-rule](https://drafts.css-houdini.org/css-properties-values-api/#at-property-rule) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#see_also)

---------------------------------------------------------------------------------------------------

*   [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
    
*   [Custom properties (`--*`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
    
*   [Registering CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Registering_properties)
    
*   [CSS Properties and Values API](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API)
     module
*   [CSS Properties and Values](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Properties_and_Values_API)
     API documentation
*   [Using CSS custom properties (variables)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
     guide
*   [CSS custom properties for cascading variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 1, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@property/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@property (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40property&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40property%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40property%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40property%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F4560e287e8c75c40aa5ecf40a0c9e8ecd0217c56%0A*+Document+last+modified%3A+2026-05-01T01%3A02%3A03.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")