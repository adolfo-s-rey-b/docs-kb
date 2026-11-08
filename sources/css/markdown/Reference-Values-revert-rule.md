*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule#mdn-search)
    

`revert-rule` CSS keyword
=========================

Baseline 2026

Newly available

Since September 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`revert-rule`** [CSS-wide keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#css-wide_keywords)
 rolls back the cascaded value of a property to the value it would have had if the current [style rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#css_rulesets)
 had not been present. The cascade then determines the value from the remaining declarations — this could be another rule in the same [cascade layer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
, a rule in a different layer, a different [style origin](https://developer.mozilla.org/en-US/docs/Glossary/Style_origin)
, or a [default value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#defaulting)
 (`inherited` or `initial`).

When used inside a [CSS animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
 (the animation origin), the `revert-rule` keyword behaves like [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
.

This keyword can be applied to any CSS property, including the CSS shorthand property [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
.

[Revert-rule vs. revert-layer vs. revert](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule#revert-rule_vs._revert-layer_vs._revert)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------

The `revert-rule`, [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
, and [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
 keywords each roll back the cascade, but at different levels of granularity:

*   [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
     removes all declarations from the current [style origin](https://developer.mozilla.org/en-US/docs/Glossary/Style_origin)
    , rolling back to the previous origin (for example, from author styles to user-agent styles).
*   [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
     removes all declarations from the current [cascade layer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
    , rolling back to the previous layer within the same origin.
*   `revert-rule` removes only the declarations from the current style rule. Other rules in the same cascade layer still apply.

This makes `revert-rule` useful for conditionally ignoring specific declarations within a rule while still respecting declarations from other rules in the same layer.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule#examples)

---------------------------------------------------------------------------------------------------

### [Rolling back to the previous rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule#rolling_back_to_the_previous_rule)

In this example, two rules target the same element. The second rule uses `revert-rule` on the `color` property, which causes the cascade to determine the value as if the `p.special` rule were not present, falling back to the value established by the first rule.

#### HTML

html

    <p class="special">This paragraph has special styling.</p>
    

#### CSS

    body {
      font-family: system-ui;
    }
    
    @supports not (color: revert-rule) {
      body::before {
        content: "Your browser doesn't support the revert-rule keyword yet.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1em;
      }
    }
    

css

    p {
      color: blue;
      font-weight: bold;
    }
    
    p.special {
      color: revert-rule;
      border: 1px solid currentColor;
    }
    

#### Result

The paragraph text is blue from the `p` rule because `color: revert-rule` causes the `color` declaration in `p.special` to be ignored. The `font-weight` and `border` declarations are unaffected.

### [Reverting from a style attribute](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule#reverting_from_a_style_attribute)

When `revert-rule` is used in a [style attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/style)
, it causes the cascade to act as if the style attribute were not present. This works because the style attribute is treated as its own style rule.

#### HTML

html

    <p style="color: revert-rule">This text uses the stylesheet color.</p>
    

#### CSS

    body {
      font-family: system-ui;
    }
    
    @supports not (color: revert-rule) {
      body::before {
        content: "Your browser doesn't support the revert-rule keyword yet.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1em;
      }
    }
    

css

    p {
      color: green;
    }
    

#### Result

The paragraph text is green because `revert-rule` causes the cascade to ignore the style attribute's declaration, and the `p` rule takes effect.

### [Chaining multiple `revert-rule` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule#chaining_multiple_revert-rule_values)

If multiple rules use `revert-rule` for the same property, the cascade ignores each of them in turn, continuing back through earlier rules until it finds a concrete value.

#### HTML

html

    <p class="a b">This text is styled by a chain of revert-rule values.</p>
    

#### CSS

    body {
      font-family: system-ui;
    }
    
    @supports not (color: revert-rule) {
      body::before {
        content: "Your browser doesn't support the revert-rule keyword yet.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1em;
      }
    }
    

css

    p {
      color: red;
    }
    p.a {
      color: revert-rule;
    }
    p.b {
      color: revert-rule;
    }
    

#### Result

Both the `p.b` and `p.a` rules are ignored by `revert-rule`. The cascade falls through to the `p` rule, so the text is red.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Cascading and Inheritance Level 5  <br>\# revert-rule-keyword](https://drafts.csswg.org/css-cascade-5/#revert-rule-keyword) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule#see_also)

---------------------------------------------------------------------------------------------------

*   [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
    
*   [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
    
*   [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
    
*   [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
    
*   [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
    
*   [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
    
*   [CSS cascading and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 29, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/revert-rule/index.md?plain=1 "Folder: en-us/web/css/reference/values/revert-rule (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frevert-rule&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frevert-rule%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frevert-rule%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frevert-rule%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fda614d19956cb816e3289721e079ded286c34a43%0A*+Document+last+modified%3A+2026-09-29T00%3A32%3A40.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")