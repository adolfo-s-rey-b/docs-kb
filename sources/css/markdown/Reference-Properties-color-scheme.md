*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#mdn-search)
    

`color-scheme` CSS property
===========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`color-scheme`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property allows an element to indicate which color schemes it can comfortably be rendered in. User agents change the following aspects of the UI chrome to match the used color scheme:

*   The color of the canvas surface.
*   The default colors of scrollbars and other interaction UI.
*   The default colors of form controls.
*   The default colors of other browser-provided UI, such as "spellcheck" underlines.

Component authors must use the [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
 media feature to support the color schemes on the rest of the elements.

Common choices for operating system color schemes are "light" and "dark", or "day mode" and "night mode". When a user selects one of these color schemes, the operating system makes adjustments to the user interface. This includes [form controls](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
, [scrollbars](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scrollbars_styling)
, and the used values of [CSS system colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#try_it)

----------------------------------------------------------------------------------------------------

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#syntax)

----------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#values)

This property is specified as one of the following keyword values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#normal)

Indicates that the element can be rendered using the page's [color scheme](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme)
 settings. If the page does not have a color scheme set, the element is rendered using the page's default color settings.

[`light`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#light)

Indicates that the element can be rendered using the operating system _light_ color scheme.

[`dark`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#dark)

Indicates that the element can be rendered using the operating system _dark_ color scheme.

[`only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#only)

Forbids the user agent from overriding the color scheme for the element.

Can be used to turn off color overrides caused by Chrome's [Auto Dark Theme](https://developer.chrome.com/blog/auto-dark-theme/#per-element-opt-out "External link (opens in new tab)")
, by applying `color-scheme: only light;` on a specific element or `:root`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#formal_definition)

--------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#formal_syntax)

------------------------------------------------------------------------------------------------------------------

color-scheme =   
  normal                                       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 light [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 dark [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")
 only[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#examples)

--------------------------------------------------------------------------------------------------------

### [Declaring color scheme preferences](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#declaring_color_scheme_preferences)

To opt the entire page into the user's color scheme preferences, declare `color-scheme` on the [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
 element.

To opt in specific elements to the user's color scheme preferences, declare `color-scheme` on those elements.

Along with the above CSS, also include the [`<meta name="color-scheme">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/color-scheme)
 HTML [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 tag in the [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
, before any CSS style information, to inform user agents about the preferred color scheme, helping prevent unwanted screen flashes during the page load.

### [Styling based on color schemes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#styling_based_on_color_schemes)

To style elements based on color scheme preferences, use the [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
 media query. The example below opts in the entire page to using both light and dark operating system color schemes via the `color-scheme` property, and then uses `prefers-color-scheme` to specify the desired foreground and background colors for individual elements in those color schemes.

Alternatively, use the [`light-dark()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark)
 [`<color>` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Functions#color_functions)
 to set the foreground and background colors for the different color schemes using a more compact code structure:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Color Adjustment Module Level 1  <br>\# color-scheme-prop](https://drafts.csswg.org/css-color-adjust/#color-scheme-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme#see_also)

--------------------------------------------------------------------------------------------------------

*   [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
     media query to detect user preferences for color schemes.
*   [`light-dark()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/light-dark)
     color function to set colors for both light and dark color schemes.
*   Other color-related properties: [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    , [`accent-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/accent-color)
    , [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    , [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
    , [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    , [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    , [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    , [`text-shadow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-shadow)
    , [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
    , and [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
    
*   [`print-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/print-color-adjust)
    
*   [Using relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color-scheme/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/color-scheme/index.md?plain=1 "Folder: en-us/web/css/reference/properties/color-scheme (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolor-scheme&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolor-scheme%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcolor-scheme%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcolor-scheme%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")