*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API#mdn-search)
    

CSS properties and values API
=============================

The **CSS properties and values API** module defines a method for registering new CSS properties, defining the property's data type, inheritance behavior, and, optionally, an initial value. This API expands on [CSS custom properties for cascading variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables)
 module, which allows authors to define custom properties in CSS using [two dash syntax (`--`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
. The CSS properties and values API is part of the [CSS Houdini](https://developer.mozilla.org/en-US/docs/Web/API/Houdini_APIs)
 umbrella of APIs.

Custom properties let you reuse values across a project to simplify complex or repetitive stylesheets. Basic custom properties are defined in the [CSS custom properties for cascading variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables)
 module. The CSS properties and values API expands on that module, enabling adding metadata to custom properties using CSS with the [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 at-rule or, alternatively, using JavaScript's [`CSS.registerProperty`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/registerProperty_static "CSS.registerProperty")
 method.

Whether registered with CSS or JavaScript, setting metadata on custom properties provides for an expected data type that the browser can use depending on the context, defines an initial value, and lets you control inheritance.

CSS properties and values API custom property registration is more robust than the more basic CSS cascading variable custom property declaration, especially when it comes to transitioning and animating values as browsers can interpolate between custom values of this type, whereas properties that use [two dash syntax (`--`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 behave more like a string substitution.

[Properties and values API in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API#properties_and_values_api_in_action)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

To see how custom properties and values can be used via API, hover over the box below.

The box has a [background](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
 consisting of a [linear gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
 from `--stop-color` (the custom property) to [`lavenderblush`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color)
. The value of `--stop-color` is set to `cornflowerblue` at first, but when you hover over the box, `--stop-color` [transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
 to `aquamarine` over two seconds (`linear-gradient(to right, aquamarine, lavenderblush)`).

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API#reference)

---------------------------------------------------------------------------------------------------------

### [At-rules and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API#at-rules_and_descriptors)

*   [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
    *   [syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#descriptors)
         descriptor
        *   [`+` and `#`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#descriptors)
             multipliers
        *   [`|`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#descriptors)
             combinator
    *   [inherits](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#descriptors)
         descriptor
    *   [initial-value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property#descriptors)
         descriptor

### [Interfaces and APIs](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API#interfaces_and_apis)

*   [`CSSPropertyRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSPropertyRule)
    
*   [`CSS.registerProperty()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/registerProperty_static "CSS.registerProperty()")
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API#guides)

---------------------------------------------------------------------------------------------------

[Registering CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Registering_properties)

Covers how to register CSS custom properties with the `@property` at-rule and explains the benefits of doing so.

[Using the CSS properties and values API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Properties_and_Values_API/guide)

Explains how to register custom properties in CSS and JavaScript, with hints on handling undefined and invalid values, fallbacks, and inheritance.

[CSS Houdini](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/Houdini)

Reference guide to Houdini resources including the CSS modules, API guides, and external resources.

[Houdini APIs](https://developer.mozilla.org/en-US/docs/Web/API/Houdini_APIs)

Explains what CSS Houdini is and its advantages, along with a list of available APIs and their statuses.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API#related_concepts)

-----------------------------------------------------------------------------------------------------------------------

*   [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
    
*   [CSSRule](https://developer.mozilla.org/en-US/docs/Web/API/CSSRule)
    
*   [CSSStyleValue](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleValue)
    
*   [CSS scoping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping)
    
*   [Using shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
    
*   [CSS Typed Object Model API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Typed_OM_API)
    
*   [CSS Painting API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Painting_API)
    
*   [Worklet](https://developer.mozilla.org/en-US/docs/Web/API/Worklet)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Properties and Values API Level 1](https://drafts.css-houdini.org/css-properties-values-api-1/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API#see_also)

-------------------------------------------------------------------------------------------------------

*   [CSS cascading and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
    
*   [CSS scoping](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scoping)
     module
*   [Using shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM)
    
*   [CSS Painting API](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Painting_API)
     module
*   [Worklet](https://developer.mozilla.org/en-US/docs/Web/API/Worklet)
     interface
*   [CSS `env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
    
*   [CSS Typed Object Model](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Typed_OM_API)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Feb 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Properties_and_values_API/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/properties_and_values_api/index.md?plain=1 "Folder: en-us/web/css/guides/properties_and_values_api (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FProperties_and_values_API&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fproperties_and_values_api%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FProperties_and_values_API%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fproperties_and_values_api%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F98bbdcd90e5487539cebe19b12fe3d731fb5a03e%0A*+Document+last+modified%3A+2026-02-02T17%3A31%3A33.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")