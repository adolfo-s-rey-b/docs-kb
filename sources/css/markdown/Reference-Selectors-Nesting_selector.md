*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#mdn-search)
    

& nesting selector
==================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The CSS **`&` nesting selector** explicitly states the relationship between parent and child rules when using [CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting)
. It makes the nested child rule selectors _relative to the parent element_. Without the `&` nesting selector, the child rule selector selects child elements. The child rule selectors have the same [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Nesting_and_specificity)
 weight as if they were within [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
.

**Note:** _Child rule_ does not mean _child element selector_. A child rule can target parent element or child elements depending on use of the `&` nesting selector.

If not used in nested style rule, the `&` nesting selector represents the [scoping root](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Nested directly — adds whitespace (descendant) */
    parentRule {
      & childRule { }
    }
    
    /* Attached to parent — no whitespace (e.g., pseudo-class, compound selector) */
    parentRule {
      &:pseudo-class { }
    }
    
    /* Reversed context — & placed after another selector */
    parentRule {
      otherRule & { }
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#description)

-----------------------------------------------------------------------------------------------------------------

### [`&` nesting selector and whitespace](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#nesting_selector_and_whitespace)

Consider the following code where nesting is done _without_ the `&` nesting selector.

css

    .parent-rule {
      /* parent rule properties */
      .child-rule {
        /* child rule properties */
      }
    }
    

When the browser parses the nested selectors, it automatically adds whitespace between the selectors to create a new CSS selector rule. The following code shows the equivalent non-nested rules:

css

    .parent-rule {
      /* parent rule style properties */
    }
    
    .parent-rule .child-rule {
      /* style properties for .child-rule descendants for .parent-rule ancestors */
    }
    

When the nested rule needs to be attached (with no whitespace) to the parent rule, such as when using a [`pseudo-class`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 or creating [compound selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Selector_structure#compound_selector)
, the `&` nesting selector must be immediately prepended to achieve the desired effect.

Consider an example where we want to style an element, providing styles to be applied at all times, and also nesting some styles to be applied only on hover. If the `&` nesting selector is not included, whitespace is added and we end up with a ruleset that applies the nested styles to any _hovered descendant of the parent rule selector_. This is, however, not what we want.

css

    .parent-rule {
      /* parent rule properties */
      :hover {
        /* child rule properties */
      }
    }
    
    /* the browser parses the above nested rules as shown below */
    .parent-rule {
      /* parent rule properties */
    }
    
    .parent-rule *:hover {
      /* child rule properties */
    }
    

With the `&` nesting selector added with no whitespace, the elements matched by the parent rule will be styled when hovered.

css

    .parent-rule {
      /* parent rule properties */
      &:hover {
        /* child rule properties */
      }
    }
    
    /* the browser parses the above nested rules as shown below */
    .parent-rule {
      /* parent rule properties */
    }
    
    .parent-rule:hover {
      /* child rule properties */
    }
    

### [Appending the `&` nesting selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#appending_the_nesting_selector)

The `&` nesting selector can also be appended to reverse the context of the rules.

css

    .card {
      /* .card styles */
      .featured & {
        /* .featured .card styles */
      }
    }
    
    /* the browser parses above nested rules as */
    
    .card {
      /* .card styles */
    }
    
    .featured .card {
      /* .featured .card styles */
    }
    

The `&` nesting selector can be placed multiple times:

css

    .card {
      /* .card styles */
      .featured & & & {
        /* .featured .card .card .card styles */
      }
    }
    
    /* the browser parses above nested rules as */
    
    .card {
      /* .card styles */
    }
    
    .featured .card .card .card {
      /* .featured .card .card .card styles */
    }
    

### [Cannot represent pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#cannot_represent_pseudo-elements)

The `&` selector is equivalent to the [`:is()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:is)
 selector, and has the same limitation that it cannot represent pseudo-elements.

For example, with the following style rule, no generated content will be styled red, even when nested in `<div class="important">`, because `.important :is(.foo::before)` cannot match anything.

css

    .foo::before {
      content: "Hello";
    
      .important & {
        color: red;
      }
    }
    

This limitation also applies to [nested at-rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/At-rules)
, whose properties are implicitly wrapped in an `&` selector. For example, with the following rule, no generated content will be styled red, even on a small screen, because the `color: red` property is implicitly wrapped in an `&` selector, which in this case is `:is(.foo::before)`.

css

    .foo::before {
      content: "Hello";
    
      @media (width < 600px) {
        color: red;
      }
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#examples)

-----------------------------------------------------------------------------------------------------------

Both of the following examples produce the same output. The first one uses normal CSS styles and the second one uses the `&` nesting selector.

### [Using normal CSS styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#using_normal_css_styles)

This example uses normal CSS styling.

#### HTML

html

    <p class="example">
      This paragraph <a href="#">contains a link</a>, try hovering or focusing it.
    </p>
    

#### CSS

css

    .example {
      font-family: system-ui;
      font-size: 1.2rem;
    }
    
    .example > a {
      color: tomato;
    }
    
    .example > a:hover,
    .example > a:focus {
      color: ivory;
      background-color: tomato;
    }
    

#### Result

### [Using `&` in nested CSS styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#using_in_nested_css_styles)

This example uses nested CSS styling.

#### HTML

html

    <p class="example">
      This paragraph <a href="#">contains a link</a>, try hovering or focusing it.
    </p>
    

#### CSS

css

    .example {
      font-family: system-ui;
      font-size: 1.2rem;
      & > a {
        color: tomato;
        &:hover,
        &:focus {
          color: ivory;
          background-color: tomato;
        }
      }
    }
    

#### Result

### [Using `&` outside nested rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#using_outside_nested_rule)

If not used in a nested style rule, `&` represents the [scoping root](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:scope)
. In this case, all styles apply to the [document](https://developer.mozilla.org/en-US/docs/Web/API/Document)
.

html

    <p>Hover over the output box to change document's background color.</p>
    

css

    & {
      color: blue;
      font-weight: bold;
    }
    
    &:hover {
      background-color: wheat;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Nesting Module Level 1  <br>\# nest-selector](https://drafts.csswg.org/css-nesting/#nest-selector) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Using CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting/Using)
    
*   [CSS nesting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Nesting)
     module
*   [CSS selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Nesting_selector/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/nesting_selector/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/nesting_selector (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FNesting_selector&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fnesting_selector%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FNesting_selector%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fnesting_selector%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5249290f5d1191482d679f74ee0efdcc108ead9c%0A*+Document+last+modified%3A+2026-09-10T07%3A41%3A57.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")