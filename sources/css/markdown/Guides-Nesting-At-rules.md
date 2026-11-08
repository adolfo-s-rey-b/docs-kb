*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules#mdn-search)
    

CSS nesting at-rules
====================

Any [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 whose body contains style rules can be nested inside another style rule using CSS nesting. Style rules nested inside at-rules take their nesting selector definition from the nearest ancestor style rule. Properties can be directly included inside a nested at-rule, acting as if they were nested in a `& {...}` block.

[at-rules that can be nested](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules#at-rules_that_can_be_nested)

------------------------------------------------------------------------------------------------------------------------------------

*   [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    
*   [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
    
*   [`@layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
    
*   [`@scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@scope)
    
*   [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
    
*   [`@starting-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@starting-style)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules#examples)

----------------------------------------------------------------------------------------------

### [Nesting `@media` at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules#nesting_media_at-rule)

In this example we see three blocks of CSS. The first one shows how to write typical at-rule nesting, the second is an expanded way of writing the nesting as the browser parses it, and the third one shows the non-nested equivalent.

#### Nested CSS

css

    .foo {
      display: grid;
      @media (orientation: landscape) {
        grid-auto-flow: column;
      }
    }
    

#### Expanded nested CSS

css

    .foo {
      display: grid;
      @media (orientation: landscape) {
        & {
          grid-auto-flow: column;
        }
      }
    }
    

#### Non-nested equivalent

css

    .foo {
      display: grid;
    }
    
    @media (orientation: landscape) {
      .foo {
        grid-auto-flow: column;
      }
    }
    

### [Multiple nested `@media` at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules#multiple_nested_media_at-rules)

At-rules can be nested within other at-rules. Below you can see an example of this, and how it would be written without nesting.

#### Nested at-rules

css

    .foo {
      display: grid;
      @media (orientation: landscape) {
        grid-auto-flow: column;
        @media (width >= 1024px) {
          max-inline-size: 1024px;
        }
      }
    }
    

#### Non-nested equivalent

css

    .foo {
      display: grid;
    }
    @media (orientation: landscape) {
      .foo {
        grid-auto-flow: column;
      }
    }
    @media (orientation: landscape) and (width >= 1024px) {
      .foo {
        max-inline-size: 1024px;
      }
    }
    

### [Nesting Cascade Layers (`@layer`)](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules#nesting_cascade_layers_layer)

[Cascade Layers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
 can be nested to [create child-layers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#nesting_layers)
. These are joined with a `.` (dot).

#### Defining the parent & child layers

We start by defining the named cascade layers, prior to using them, without any style assignments.

css

    @layer base {
      @layer support;
    }
    

#### Assigning rules to layers with nesting

Here the `.foo` selector assigns its rules to the **base** `@layer`. The nested **support** `@layer` creates the `base.support` sub-layer, and the `&` nesting selector is used to create the rules for the `.foo .bar` selector.

css

    .foo {
      @layer base {
        block-size: 100%;
        @layer support {
          & .bar {
            min-block-size: 100%;
          }
        }
      }
    }
    

#### Equivalent without nesting

css

    @layer base {
      .foo {
        block-size: 100%;
      }
    }
    @layer base.support {
      .foo .bar {
        min-block-size: 100%;
      }
    }
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules#see_also)

----------------------------------------------------------------------------------------------

*   [CSS Nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting)
     module
*   [`&` nesting selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector)
    
*   [Using CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Using)
    
*   [Nesting and specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Nesting_and_specificity)
    
*   [Nesting container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#nested_queries)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 18, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/nesting/at-rules/index.md?plain=1 "Folder: en-us/web/css/guides/nesting/at-rules (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FNesting%2FAt-rules&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fnesting%2Fat-rules%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FNesting%2FAt-rules%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fnesting%2Fat-rules%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F81f8fcd666952c1782653a3675347c392cc997ca%0A*+Document+last+modified%3A+2025-11-18T10%3A30%3A16.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")