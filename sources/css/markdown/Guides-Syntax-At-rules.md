*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules#mdn-search)
    

At-rules
========

**At-rules** are [CSS statements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#css_statements)
 that instruct CSS how to behave. They begin with an at-sign, `@` (U+0040 COMMERCIAL AT), followed by an identifier. They include everything from the at-keyword up to the next semicolon, `;` (U+003B SEMICOLON), or the next [CSS block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#css_declaration_blocks)
, whichever comes first.

At-rules are used to group and structure style rules and other at-rules, declare style information not directly associated with selected content, and manage syntactic constructs such as imports and namespaces keyword mappings.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules#syntax)

-----------------------------------------------------------------------------------------

The at-rule is defined in the [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax)
 module, with different at-rules being defined in their respective modules. They generally take one of two forms depending on the specific rule and its purpose: statement at-rules and block at-rules, which can contain nested qualified rules, at-rules, or declarations.

### [Statement at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules#statement_at-rules)

css

    /* General structure */
    @identifier (RULE);
    
    /* Example: tells browser to use UTF-8 character set */
    @charset "utf-8";
    

Statement at-rules end in a semicolon. There are several statement at-rules, designated by their identifiers, each with a different syntax:

[`@charset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset)

An algorithm (has the syntactic form of an at-rule, but isn't a definition) that determines the fallback character set used by the style sheet ([CSS Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax)
).

[`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)

Tells the CSS engine to include an external style sheet ([CSS cascading and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
).

[`@layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)

Defines the order of precedence in case of multiple cascade layers ([CSS cascading and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
). Also used as a [block at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules#layer_2)
 to define a layer's styles.

[`@namespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace)

Defines a default namespace for a style sheet or a namespace prefix that a selector only matches if the namespace and other selector components match ([CSS namespaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Namespaces)
).

### [Block at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules#block_at-rules)

css

    @identifier (RULE) {
    }
    

Block at-rules end in a `{}`\-block that contain nested rules, other at-rules, or property or descriptor declarations.

[`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)

Define custom counter styles and extend predefined list styles ([CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
).

[`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)

A conditional group rule that applies its content if the container meets the [`<container-condition>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#container-condition)
s ([CSS containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment)
).

[`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)

Defines font resource locations, both local and external, along with the style characteristics for when those resources are used with a declared [`font-family`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family)
 ([CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
).

[`@font-feature-values`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-feature-values)
 (plus `@swash`, `@ornaments`, `@annotation`, `@stylistic`, `@styleset` and `@character-variant`)

Controls font display per font-family by defining font-specific alternates, or custom names, to feature indexes in [`font-variant-alternates`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
 in OpenType ([CSS fonts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
).

[`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 (and the `@-webkit-keyframes` alias)

Define a named animation by describing defining CSS styles for intermediate steps (or keyframes) in the animation sequence ([CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
).

[`@layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)

Creates a named cascade layer with the CSS rules for that layer inside ([CSS cascading and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
). Also used as a [statement at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules#layer)
 to define the order of precedence in case of multiple cascade layers

[`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)

A conditional group rule that applies its content if the device meets the criteria of the condition defined using a _media query_ ([CSS conditional rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules)
).

[`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)

Specifies aspects of a page to be printed, such as its dimensions, orientation, and margins ([CSS paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
).

[`@position-try`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@position-try)

Defines custom position options which can be used to define fallback positioning and alignment options for anchor-positioned elements ([CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
).

[`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)

Defines a [CSS custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
, allowing for property type checking and constraining, setting default values, and defining whether a custom property can inherit values or not ([CSS custom properties for cascading variables](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables)
).

[`@scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope)

Defines a scope in which to apply them to selected elements and the styles to apply to the elements in that scope ([CSS cascading and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
).

[`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)

Define the starting property values for an element to transition from when the element receives its first style update, such as when transitioning from `display: none` ([CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
).

[`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)

A conditional group rule applies its content if the browser supports the CSS features of the given condition ([CSS conditional rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules)
).

[`@view-transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@view-transition)

Opts the current document into a [view transition](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API)
, and the destination document as well in the case of cross-document navigation transitions.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules#specifications)

---------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Syntax Module Level 3](https://drafts.csswg.org/css-syntax/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules#see_also)

---------------------------------------------------------------------------------------------

*   [CSS at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules)
    
*   [CSS at-rule functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions)
    
*   [Nesting at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules)
    
*   [CSS statements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#css_statements)
    
*   [CSSRule](https://developer.mozilla.org/en-US/docs/Web/API/CSSRule)
     interface
*   [CSS conditional rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules)
     module
*   [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction)
     module
*   [Specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
    
*   [Inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/syntax/at-rules/index.md?plain=1 "Folder: en-us/web/css/guides/syntax/at-rules (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSyntax%2FAt-rules&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fsyntax%2Fat-rules%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSyntax%2FAt-rules%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fsyntax%2Fat-rules%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")