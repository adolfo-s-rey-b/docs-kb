*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions#mdn-search)
    

CSS at-rule functions
=====================

**[CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 functions** are at-rule statements that represent complex rules or can invoke special data processing or calculations.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions#syntax)

-------------------------------------------------------------------------------------------------------

@identifier function(\[argument\]? \[, argument\]!) {
}

The syntax begins with the at symbol `@` and an at-rule identifier, such as `import`. This is followed by the **name of the at-rule function**, such as `url`, followed by a pair of opening and closing parentheses. One or more arguments are specified inside the parentheses.

Some at-rule functions can take multiple arguments, which are formatted similar to CSS property values. White space is allowed, but it is optional inside the parentheses. Multiple arguments can be separated using a comma or a space.

[@import functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions#import_functions)

----------------------------------------------------------------------------------------------------------------------------

The [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
 at-rule is used to import styles from other stylesheets.

[`@import url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)

Imports a stylesheet file from the specified URL.

[`@import supports()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)

Imports a stylesheet file based on browser support.

[`@import layer()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import/layer_function)

Imports a stylesheet file into the specified cascade layer.

[@supports functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions#supports_functions)

--------------------------------------------------------------------------------------------------------------------------------

The [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 at-rule checks for a browser's support for the specified CSS feature and then applies the CSS styling.

[`@supports selector()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)

Applies CSS rules after checking browser's support for the specified selector syntax.

[`@supports font-tech()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)

Applies CSS rules after checking browser's support for the specified font technology.

[`@supports font-format()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)

Applies CSS rules after checking browser's support for the specified font format.

[@namespace functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions#namespace_functions)

----------------------------------------------------------------------------------------------------------------------------------

The [`@namespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace)
 at-rule is used to specify XML namespaces to be used in a CSS stylesheet.

[`@namespace url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace)

Defines XML namespace from the specified URL.

[@container functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions#container_functions)

----------------------------------------------------------------------------------------------------------------------------------

The [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
 at-rule is used to specify styles for a containment context.

[`@container style()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)

Defines the containment context style.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions#see_also)

-----------------------------------------------------------------------------------------------------------

*   [CSS at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules)
    
*   [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/at-rule_functions/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/at-rule_functions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2FAt-rule_functions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2Fat-rule_functions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2FAt-rule_functions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2Fat-rule_functions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")