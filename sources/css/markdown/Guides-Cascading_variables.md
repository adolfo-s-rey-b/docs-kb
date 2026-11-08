*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables#mdn-search)
    

CSS custom properties for cascading variables
=============================================

The **CSS custom properties for cascading variables** module adds support for cascading variables in CSS properties and lets you create custom properties to define these variables along with the mechanisms to use custom properties as the values for other CSS properties.

When working with CSS, you often end up reusing common project-specific values such as widths that work well with your layout, or a set of colors for your color scheme. One way of managing repetition in stylesheets is to define a value once and use it many times in other places. Custom properties let you create and define custom variables that can be reused, simplifying complex or repetitive rules and making them easier to read and maintain. For example, `--dark-grey-text` and `--dark-background` are easier to understand than hexadecimal colors such as `#323831`, and the context of how you use them is more obvious, too.

[Custom properties in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables#custom_properties_in_action)

---------------------------------------------------------------------------------------------------------------------------------------

To see how custom properties can be used, move the input slider left to right.

In these color swatches, the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 is set using the [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
 [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 function as `hsl(var(--hue) 50% 50%)`. Each color swatch increments the [`<hue>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hue)
 value by 10 degrees like `calc(var(--hue) + 10)`, `calc(var(--hue) + 20)` etc. As the slider's value changes from 0 up to 360, the value of the `--hue` [custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 is updated using [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
, and the background color of each box inside the grid is updated, also.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables#reference)

---------------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables#properties)

*   [`--*`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
    

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables#functions)

*   [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables#guides)

---------------------------------------------------------------------------------------------

[Using CSS custom properties (variables)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)

Explains how to use custom properties in CSS and JavaScript, with hints on handling undefined and invalid values, fallbacks, and inheritance.

[Invalid custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Error_handling#invalid_custom_properties)

Explains how browsers handle property values when a custom property's value is an invalid data type for that property.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables#related_concepts)

-----------------------------------------------------------------------------------------------------------------

*   [CSS Properties and Values API](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API)
     module
    *   [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
         at-rule
    *   [`CSS.registerProperty()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/registerProperty_static)
         method

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Custom Properties for Cascading Variables Module Level 1](https://drafts.csswg.org/css-variables/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables#see_also)

-------------------------------------------------------------------------------------------------

*   [CSS cascading and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
     module
*   [CSS `env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
     function
*   [CSS `calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
     function
*   [`getPropertyValue()`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration/getPropertyValue)
     method

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/cascading_variables/index.md?plain=1 "Folder: en-us/web/css/guides/cascading_variables (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCascading_variables&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcascading_variables%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCascading_variables%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcascading_variables%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")