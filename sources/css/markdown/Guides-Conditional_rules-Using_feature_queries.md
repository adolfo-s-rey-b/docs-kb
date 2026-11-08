*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#mdn-search)
    

Using feature queries
=====================

**Feature queries** are conditional group rules that test whether the user agent supports or doesn't support one or more CSS features, such as CSS properties and property values. Feature queries give web developers a way to test to see if a browser has support for a certain feature, and then provide CSS that will only run based on the result of that test. In this guide, you will learn how to implement progressive enhancement using feature queries.

Feature queries are created using the CSS at-rule [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 (or the `supports()` function within [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
 at-rules).

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#syntax)

-----------------------------------------------------------------------------------------------------------------

CSS feature queries are part of the [CSS conditional rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules)
 module, which also defines the media query [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 at-rule. Feature queries behave similarly to [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
. The difference is that with a media query, you are testing something about the environment in which the web page is running, whereas with feature queries you are testing browser support for CSS features.

A feature query consists of the `@supports` at-rule followed by the support condition or a `supports()` function and declaration parameter within an `@import` at-rule declaration:

/\* \`@supports\` at-rule \*/
@supports <support-condition> {
  /\* CSS rules to apply \*/
}

/\* \`supports()\` function \*/
@import url\_to\_import supports(<declaration>);

For example, we can apply a set of styles or import an entire stylesheet if the user-agent supports `red` as a valid value for the CSS [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property:

css

    /* `@supports` at-rule */
    @supports (color: red) {
      /* CSS rules to apply */
    }
    
    /* `supports()` function */
    @import "/css/styles.css" supports(color: red);
    

As another example, if you want to check if a browser supports the `row-gap` property you would write the following feature query. It doesn't matter which value you use in a lot of cases: if all you want is to check that the browser supports this property, then any valid value will do.

html

    <div class="box">
      If your browser supports the row-gap property, the border will be dashed and
      text will be red.
    </div>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    .box {
      border: 4px solid blue;
      color: blue;
      padding: 1em;
    }
    @supports (row-gap: 10px) {
      .box {
        border: 4px dashed darkgreen;
        color: red;
      }
    }
    

The value part of the property-value pair matters more if you are testing for new values of a particular property. All browsers support `color: red`: this dates back to CSS1. However, there are often additional values added to properties in CSS, like [relative colors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Using_relative_colors)
, which may not be supported. Feature queries enable testing property and value pairs, meaning we can detect support for values.

Expanding on the `color` property example above, here we check if the browser supports the `color: AccentColor` declaration:

css

    /* `@supports` at-rule */
    @supports (color: AccentColor) {
      /* CSS rules to apply */
    }
    
    /* `supports()` function */
    @import "/css/styles.css" supports(color: AccentColor);
    

In these examples, we've used feature queries to check if the user-agent supports a specific value of a CSS property, listing the single declaration within parenthesis. You can test for multiple property values or the lack of support.

[Testing for lack of support](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#testing_for_lack_of_support)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to asking the browser if it supports a feature, you can test for the opposite by adding in the `not` keyword:

css

    /* `@supports` at-rule with `not` */
    @supports not (property: value) {
      /* CSS rules to apply */
    }
    

The CSS inside the following example feature query will run if the browser does not support `row-gap`.

html

    <div class="box">
      If your browser does not support row-gap, the content will be darkgreen with a
      dashed border.
    </div>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    .box {
      border: 4px solid blue;
      color: blue;
      padding: 1em;
    }
    @supports not (row-gap: 10px) {
      .box {
        border: 4px dashed darkgreen;
        color: darkgreen;
      }
    }
    

[Testing for more than one feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#testing_for_more_than_one_feature)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

You may need to test support for more than one property in your feature query. To do so, you can include a list of features to test for, separated by `and` keywords:

css

    /* multiple feature `@supports` at-rule */
    @supports (property1: value) and (property2: value) {
      /* CSS rules to apply */
    }
    

For example, if the CSS you want to run requires that the browser supports CSS Shapes and CSS grid, you could create a rule that tests browser support for both of these features. The following rule will only return true if `shape-outside: circle()` and `display: grid` are both supported by the browser.

html

    <div class="box">
      If your browser supports <code>display: grid</code> and
      <code>shape-outside: circle()</code>, the content will be darkgreen with a
      dashed border.
    </div>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    .box {
      border: 4px solid blue;
      color: blue;
      padding: 1em;
    }
    @supports (display: grid) and (shape-outside: circle()) {
      .box {
        border: 4px dashed darkgreen;
        color: darkgreen;
      }
    }
    

[Testing for at least one of multiple features](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#testing_for_at_least_one_of_multiple_features)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can also use `or` to apply CSS only if one or more declarations are supported:

css

    /* any feature `@supports` at-rule */
    @supports (property1: value) or (property2: value) {
      /* CSS rules to apply */
    }
    

This can be particularly useful if a feature is vendor prefixed, as you can test for the standard property plus any vendor prefixes.

html

    <div class="box">
      The text and border will be green if your browser supports font smoothing.
    </div>
    

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    .box {
      border: 4px solid blue;
      color: blue;
      padding: 1em;
    }
    @supports (font-smooth: always) or (-webkit-font-smoothing: antialiased) {
      .box {
        border: 4px dashed darkgreen;
        color: darkgreen;
      }
    }
    

[Additional feature query options](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#additional_feature_query_options)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------

Feature queries are not limited to property-value pairs. You can include [`font-tech()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#font-tech)
, [`font-format()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#font-format)
, and [`selector()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports#function_syntax)
 functions in your feature queries to selectively apply CSS based on whether the user-agent supports a specified font technology, font format, or selector syntax, respectively.

For example, the `selector()` function can be used to import a stylesheet for browsers that support a vendor-prefixed pseudo-element:

css

    /* A `selector()` query within a `supports()` function */
    @import "/css/webkitShadowStyles.css"
      supports(selector(::-webkit-inner-spin-button));
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#examples)

---------------------------------------------------------------------------------------------------------------------

### [Browser support test](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#browser_support_test)

In this example, we check if the browser supports the `AccentColor` [`<system-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/system-color)
 and use `display: none` to change the default "not supported" message to a "supported" message if the color type is supported.

#### HTML

html

    <p class="accentcolor">
      Your browser does <span>not</span> support <code>AccentColor</code> as a color
      value.
    </p>
    

#### CSS

css

    body {
      font: 1.2em / 1.5 sans-serif;
    }
    p {
      padding: 1em;
    }
    @supports (color: AccentColor) {
      p {
        color: green;
        border: 2px solid;
      }
      span {
        display: none;
      }
    }
    @supports not (color: AccentColor) {
      p {
        color: red;
      }
    }
    

#### Result

[Limitations of feature queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#limitations_of_feature_queries)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The `@supports` rule tests to see if browsers can parse one or more property/value pairs, and therefore if they claim to support the associated feature(s). If the property/value pairs are understood by a browser it returns a positive response. Feature queries check that declarations are considered valid by a browser, but can't be used to check if it supports a feature properly without bugs or spec violations. Feature queries cannot test for _partial implementations_.

[Summary](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#summary)

-------------------------------------------------------------------------------------------------------------------

Feature queries are a useful tool for progressively enhancing a site. They enable you to provide a good solution for all browsers, and an enhanced solution for browsers that support newer properties and values.

You don't need to use feature queries to start using new CSS features; CSS error handling means the browser simply ignores CSS it does not yet recognize. However, feature queries are a useful alternative to fallback declarations, and enable writing code once that can eventually be supported everywhere.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [CSS conditional rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules)
     module
*   [Using CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [Supporting older browsers: feature queries](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Supporting_Older_Browsers#feature_queries)
    
*   [Browser feature detection: CSS `@supports`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Testing/Feature_detection#supports)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/conditional_rules/using_feature_queries/index.md?plain=1 "Folder: en-us/web/css/guides/conditional_rules/using_feature_queries (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FConditional_rules%2FUsing_feature_queries&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fconditional_rules%2Fusing_feature_queries%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FConditional_rules%2FUsing_feature_queries%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fconditional_rules%2Fusing_feature_queries%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")