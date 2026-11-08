*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#mdn-search)
    

`<dashed-ident>` CSS type
=========================

The **`<dashed-ident>`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [data type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types)
 is a case-sensitive [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 starting with two dashes that denotes an arbitrary string used as an [identifier](https://developer.mozilla.org/en-US/docs/Glossary/Identifier)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#syntax)

------------------------------------------------------------------------------------------------

The syntax of `<dashed-ident>` is similar to CSS identifiers (such as property names), except that it is case-sensitive. It is a user-defined identifier preceded by two dashes (`--`).

The double dash at the beginning makes them easily identifiable when reading through a CSS code block, and helps to avoid name clashes with standard CSS keywords.

Just like [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
s, `<dashed-ident>`s are defined by the user. However, some `<custom-ident>`s are defined by the CSS language itself; `<dashed-ident>`s will never be defined in CSS.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#examples)

----------------------------------------------------------------------------------------------------

### [Using with CSS custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#using_with_css_custom_properties)

When a `<dashed-ident>` is used as a [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
, the property is declared first, and then the `<dashed-ident>` is used within a [CSS `var()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
.

### [Using with @color-profile](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#using_with_color-profile)

When a `<dashed-ident>` is used with the [`@color-profile`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@color-profile)
 at-rule, the at-rule is declared first, and then the `<dashed-ident>` is used within a [CSS `color()` function](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/color)
.

### [Using with @font-palette-values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#using_with_font-palette-values)

When a `<dashed-ident>` is used with the [`@font-palette-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-palette-values)
 at-rule, the at-rule is declared first, and then the `<dashed-ident>` is used as the value for the [`font-palette`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-palette)
 property.

### [Using with env() and param()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#using_with_env_and_param)

When a `<dashed-dent>` is used in an external resource in an [`env()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/env)
 CSS function, it can be updated using the [`param()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/param)
 CSS function.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Values and Units Module Level 4  <br>\# dashed-idents](https://drafts.csswg.org/css-values/#dashed-idents) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

_As this type is not a real type but a convenience type used to simplify the definition of other CSS syntax, there is no browser compatibility information as such._

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident#see_also)

----------------------------------------------------------------------------------------------------

*   [`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
    
*   [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/dashed-ident/index.md?plain=1 "Folder: en-us/web/css/reference/values/dashed-ident (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdashed-ident&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdashed-ident%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Fdashed-ident%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Fdashed-ident%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F35cd8b781219157e42b289364754cff862c2dd1a%0A*+Document+last+modified%3A+2026-07-24T20%3A50%3A17.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")