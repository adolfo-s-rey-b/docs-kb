*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins#mdn-search)
    

CSS custom functions and mixins
===============================

The **CSS custom functions and mixins** module allows developers to create reusable blocks of CSS code that can accept arguments, contain complex logic (defined using features such as CSS [`if()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if)
 functions and [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 at-rules), and return values based on that logic.

CSS custom functions are defined in [`@function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function)
 at-rules and called using [`<dashed-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function)
 syntax, which looks very similar to [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/--*)
 syntax except that it includes parentheses at the end containing arguments (for example, `--my-function(30px, 3)`). CSS custom functions can be called within any property value, and will return a value based on the arguments passed into the function and the logic inside it.

CSS mixins are defined in `@mixin` at-rules and applied using `@apply` at-rules nested inside rulesets. CSS mixins define a set of properties that can be reused inside multiple rulesets and customized with arguments and logic.

CSS custom functions and mixins can be assigned optional data types for their arguments and return values, to restrict the values passed into them and returned from them.

**Note:** Currently, only CSS custom functions have browser support. CSS mixins are not currently supported in any browser.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins#reference)

-----------------------------------------------------------------------------------------------------------

### [At-rules and descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins#at-rules_and_descriptors)

*   [`@function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function)
    *   [`result`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@function#result)
        

The CSS custom functions and mixins module also introduces the `@mixin`, `@apply`, `@contents`, and `@env` at-rules. Currently, no browsers support these features.

### [Data types and values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins#data_types_and_values)

*   [`<dashed-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-function)
    

### [Functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins#functions)

*   [`type()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/type)
    

### [Interfaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins#interfaces)

*   [`CSSFunctionRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSFunctionRule)
    
*   [`CSSFunctionDeclarations`](https://developer.mozilla.org/en-US/docs/Web/API/CSSFunctionDeclarations)
    
*   [`CSSFunctionDescriptors`](https://developer.mozilla.org/en-US/docs/Web/API/CSSFunctionDescriptors)
    

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins#guides)

-----------------------------------------------------------------------------------------------------

[Using CSS custom functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/Using_custom_functions)

This guide teaches you how to use CSS custom functions and presents some typical use cases.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins#related_concepts)

-------------------------------------------------------------------------------------------------------------------------

[CSS values and units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units)

*   [`abs()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/abs)
    
*   [`acos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/acos)
    
*   [`asin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/asin)
    
*   [`atan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan)
    
*   [`atan2()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/atan2)
    
*   [`calc()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/calc)
    
*   [`clamp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/clamp)
    
*   [`cos()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/cos)
    
*   [`exp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/exp)
    
*   [`log()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/log)
    
*   [`max()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/max)
    
*   [`min()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/min)
    
*   [`mod()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/mod)
    
*   [`pow()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/pow)
    
*   [`rem()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rem)
    
*   [`round()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/round)
    
*   [`sign()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sign)
    
*   [`sin()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sin)
    
*   [`sqrt()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/sqrt)
    
*   [`tan()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/tan)
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Functions and Mixins Module](https://drafts.csswg.org/css-mixins-1/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins#see_also)

---------------------------------------------------------------------------------------------------------

*   [`if()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/if)
    
*   [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Feb 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Custom_functions_and_mixins/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/custom_functions_and_mixins/index.md?plain=1 "Folder: en-us/web/css/guides/custom_functions_and_mixins (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCustom_functions_and_mixins&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcustom_functions_and_mixins%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCustom_functions_and_mixins%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcustom_functions_and_mixins%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F569b07ef525429e0929c70e7dd067cbc0ce707bd%0A*+Document+last+modified%3A+2026-02-06T10%3A57%3A46.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")