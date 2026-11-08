*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#mdn-search)
    

`@custom-media` CSS at-rule
===========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/445)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#browser_compatibility)
 carefully before using this in production.

The **`@custom-media`** CSS [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules)
 defines aliases for long or complex [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
. Instead of repeating the same hardcoded `<media-query-list>` in multiple [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 at-rules, it can be defined once in a `@custom-media` at-rule and referenced throughout the stylesheet whenever needed.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#syntax)

---------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#values)

[`<extension-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#extension-name)

A [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
; the name identifying the custom media query.

[Represented value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#represented_value)

The value aliased by the custom media query. Possible values are:

[`<media-query-list>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#media-query-list)

A comma-separated [list of `<media-query>` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#description)
.

[`true`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#true)

The `@custom-media` value always evaluates to `true`.

[`false`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#false)

The `@custom-media` value always evaluates to `false`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#description)

-------------------------------------------------------------------------------------------------------------

When building responsive interfaces, the same media condition often needs to be repeated across multiple [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 at-rules, sometimes across different files and teams. Duplicating media queries increases the risk of mistakes, makes refactoring harder, and creates unnecessary maintenance overhead. Any time a media query changes, every instance must be found and updated manually — a process that can be both error-prone and difficult to track in large codebases.

The `@custom-media` at-rule solves this problem by letting you define **named aliases** for media queries. Instead of repeating the full media query everywhere, you declare the media condition once as a custom media query and reference its alias throughout your stylesheets. With this in place, updating the underlying media query requires a single change in one location.

Custom media queries can be composed from others by referencing their alias names inside the media query features. This enables building more expressive, layered conditions. However, a custom media query cannot refer to itself, nor can it form part of a circular chain of references. Any circular dependency — direct or indirect — invalidates all custom media queries involved in that loop.

If multiple `@custom-media` rules define the same `<dashed-ident>` name, the rule that is in scope at the time a `@media` rule is evaluated is used. Earlier references are not retroactively updated when a later `@custom-media` rule is declared.

### [Evaluating media queries with logical operators](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#evaluating_media_queries_with_logical_operators)

Custom media queries accept the full range of CSS logical operators — `not`, `and`, and `or` (comma-separated or using the `or` keyword).

Because a `@custom-media` value is just a normal `<media-query-list>`, you can combine, invert, or group conditions exactly as you would in a regular `@media` rule.

#### Using the `not` operator

The `not` operator negates an entire media condition. This is useful when you want a rule to apply only when a specific condition is `false`.

#### Using the `and` operator

The `and` operator lets you combine multiple conditions that must all be `true`.

This alias only matches when the viewport is within the specified width range.

#### Using the `or` operator

The logical `or` operator (or its comma alias, when combining media types) creates a media query that matches if any of the listed conditions are `true`.

The `--screen-or-print` alias uses a comma to match either the `screen` or `print` media type. The `--narrow-or-tall` alias uses the `or` keyword to combine two media features, matching when the viewport is narrower than 600px, taller than 800px, or both.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

@custom-media =   
  @custom-media <extension-name> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <media-query-list> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 true [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 false [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 ;    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#examples)

-------------------------------------------------------------------------------------------------------

### [Updating multiple media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#updating_multiple_media_queries)

In this example, the `@custom-media` at-rule is used on a responsive website that uses a particular breakpoint in several places:

If the breakpoint needs to be changed, it can be updated in one place to adjust all dependent media queries across the whole site.

### [Grouping multiple responsive breakpoints](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#grouping_multiple_responsive_breakpoints)

Here, the `@custom-media` at-rule is used to set multiple breakpoints in a single place, improving maintainability and simplifying responsive design management across multiple stylesheets:

Grouping all the breakpoints in a single location makes it easier to maintain the responsive design. When a breakpoint needs adjustment, it only requires a single update to the associated `@custom-media` definition, ensuring consistency across all stylesheets.

### [Using `true` and `false` keywords](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#using_true_and_false_keywords)

The following example shows how the `true` and `false` keywords can be used with `@custom-media` to create media queries that always or never match, respectively.

This can be useful for feature flags or conditional logic within stylesheets.

### [Overriding existing `@custom-media` rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#overriding_existing_custom-media_rules)

In this example, one `@custom-media` rule is overridden by another `@custom-media` rule using the same `<dashed-ident>` name.

When multiple `@custom-media` rules use the same name, the rule that is in scope at the time a `@media` rule is evaluated is used. Earlier references are not retroactively updated when a later `@custom-media` rule is declared.

For example, in the code above, the `--mobile-breakpoint` reference inside the `@media` rule is evaluated as `(width < 320px)`, so the `.container` rule is only applied when the viewport is less than 320px wide, even though `--mobile-breakpoint` is redefined as `(width < 480px)` later in the stylesheet.

**Note:** The overriding behavior of `@custom-media` is still under discussion in the CSS specification and may change in the future. See the [Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#browser_compatibility)
 section for current support status.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Media Queries Level 5  <br>\# at-ruledef-custom-media](https://drafts.csswg.org/mediaqueries-5/#at-ruledef-custom-media) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media#see_also)

-------------------------------------------------------------------------------------------------------

*   CSS [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
     at-rule
*   CSS [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
     at-rule
*   [Responsive design](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design)
    
*   [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 19, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@custom-media/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@custom-media/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@custom-media (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40custom-media&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40custom-media%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40custom-media%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40custom-media%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6b0dc010f6c32a23b54aef95094cee9ec0e1b7b5%0A*+Document+last+modified%3A+2026-08-19T12%3A00%3A16.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")