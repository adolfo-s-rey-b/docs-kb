*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#mdn-search)
    

`@layer` CSS at-rule
====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@layer`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 is used to declare a cascade layer and can also be used to define the order of precedence in case of multiple cascade layers.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#try_it)

--------------------------------------------------------------------------------------------

    @layer module, state;
    
    @layer state {
      .alert {
        background-color: brown;
      }
      p {
        border: medium solid limegreen;
      }
    }
    
    @layer module {
      .alert {
        border: medium solid violet;
        background-color: yellow;
        color: white;
      }
    }
    

    <p class="alert">Beware of the zombies</p>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#syntax)

--------------------------------------------------------------------------------------------

css

    /* statement at-rules */
    @layer layer-name;
    @layer layer-name, layer-name, layer-name;
    
    /* block at-rules */
    @layer {rules}
    @layer layer-name {rules}
    

where:

[_layer-name_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#layer-name)

Is the name of the cascade layer.

[_rules_](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#rules)

Is the set of CSS rules in the cascade layer.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#description)

------------------------------------------------------------------------------------------------------

Rules within a cascade layer cascade together, giving more control over the cascade to web developers. Styles that are not defined in a layer always override styles declared in named and anonymous layers.

The following diagram shows layer priorities where layers are declared in 1, 2, ..., N order.

![Diagram showing cascade layer priorities](https://mdn.github.io/shared-assets/images/diagrams/css/at-rules/layer-cascade.svg)

As noted in the above diagram, _important declarations_, declarations with the `!important` flag, have priority over _normal declarations_, or regular declarations without the `!important` flag. The order of precedence among important rules is the inverse of normal rules. Transitions have the greatest precedence. Next in order of highest to lowest priority are the important [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 declarations, important user declarations, and important author declarations; in that order. Users can specify styles using browser preferences, operating system preferences, or browser extensions. Their important declarations take precedence over _author_, or _web developer_ written, important declarations.

Within author styles, all important declarations within CSS layers take precedence over any important declarations declared outside of a layer, while all normal declarations within CSS layers have a lower priority than declarations declared outside of a layer. The declaration order matters. The first declared layer gets the lowest priority and the last declared layer gets the highest priority. However, the priority is reversed when the [`!important`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/important)
 flag is used.

The `@layer` at-rule is used to create a cascade layer in one of three ways.

The first way is to use a `@layer` block at-rule to create a named cascade layer with the CSS rules for that layer inside, like so:

css

    @layer utilities {
      .padding-sm {
        padding: 0.5rem;
      }
    
      .padding-lg {
        padding: 0.8rem;
      }
    }
    

The second way is to use a `@layer` statement at-rule to create one or more comma-separated named cascade layers without assigning any styles. This can be a single layer, as shown below:

css

    @layer utilities;
    

Multiple layers can be defined at once, as shown below:

css

    @layer theme, layout, utilities;
    

This is useful because the initial order in which layers are declared indicates which layer has precedence. As with declarations, the last layer to be listed will win if declarations are found in multiple layers. Therefore, with the preceding example, if a competing rule was found in `theme` and `utilities`, the one in `utilities` would win and be applied.

A rule in `utilities` would be applied _even if it has lower specificity_ than the rule in `theme`. This is because once the layer order has been established, specificity and order of appearance are ignored. This enables using simpler CSS selectors because you do not have to ensure that a selector will have high enough specificity to override competing rules; all you need to ensure is that it appears in a later layer.

**Note:** Having declared your layer names, thus setting their order, you can add CSS rules to the layer by re-declaring the name. The styles are then appended to the layer and the layer order will not be changed.

The third way is to create an unnamed layer using a `@layer` block at-rule without including a layer name. For example:

css

    @layer {
      p {
        margin-block: 1rem;
      }
    }
    

This creates an _anonymous cascade layer_. This layer functions in the same way as named layers; however, rules cannot be assigned to it later. The order of precedence for anonymous layers is the order in which layers are declared, named or not, and lower than the styles declared outside of a layer.

Another way to create a cascade layer is by using [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
. In this case, the rules would be in the imported stylesheet. Remember that the `@import` at-rule must precede all other types of rules, except `@charset` and `@layer` statements (not `@layer` blocks).

css

    @import "theme.css" layer(utilities);
    

### [Nesting layers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#nesting_layers)

Layers may be nested. For example:

css

    @layer framework {
      @layer layout {
      }
    }
    

To append rules to the `layout` layer inside `framework`, join the two names with a `.`.

css

    @layer framework.layout {
      p {
        margin-block: 1rem;
      }
    }
    

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#formal_syntax)

----------------------------------------------------------------------------------------------------------

@layer =   
  @layer <layer-name>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 { [<rule-list>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list)
 }  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  @layer <layer-name>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 ;                  
  
<layer-name> =   
  [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 '.' [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#examples)

------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#basic_example)

In the following example, two CSS rules are created. One for the [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element outside of any layer and one inside a layer named `type` for `.box p`.

Without layers, the selector `.box p` would have the highest specificity, and therefore, the text `Hello, world!` will display in green. As the `type` layer comes before the anonymous layer created to hold non-layer content, the text will be purple.

Also notice the order. Even though we declare the non-layered style first, it's still applied _after_ the layer styles.

#### HTML

html

    <div class="box">
      <p>Hello, world!</p>
    </div>
    

#### CSS

css

    p {
      color: rebeccapurple;
    }
    
    @layer type {
      .box p {
        font-weight: bold;
        font-size: 1.3em;
        color: green;
      }
    }
    

#### Result

### [Assigning rules to existing layers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#assigning_rules_to_existing_layers)

In the following example, two layers are created with no rules applied, then CSS rules are applied to the two layers. The `base` layer defines a `color`, `border`, `font-size`, and `padding`. The `special` layer defines a different color. As `special` comes last when the layers were defined, the color it provides is used and the text is displayed using `rebeccapurple`. All of the other rules from `base` still apply.

#### HTML

html

    <div class="item">
      I am displayed in <code>color: rebeccapurple</code> because the
      <code>special</code> layer comes after the <code>base</code> layer. My green
      border, font-size, and padding come from the <code>base</code> layer.
    </div>
    

#### CSS

css

    @layer base, special;
    
    @layer special {
      .item {
        color: rebeccapurple;
      }
    }
    
    @layer base {
      .item {
        color: green;
        border: 5px solid green;
        font-size: 1.3em;
        padding: 0.5em;
      }
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Cascading and Inheritance Level 5  <br>\# layering](https://drafts.csswg.org/css-cascade-5/#layering) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer#see_also)

------------------------------------------------------------------------------------------------

*   [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
    
*   [`CSSLayerBlockRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSLayerBlockRule)
    
*   [`CSSLayerStatementRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSLayerStatementRule)
    
*   [`!important`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/important)
    
*   [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
    
*   [Introducing the CSS cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
    
*   [Learn: Handling conflicts](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_conflicts)
    
*   [Learn: Cascade layers](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Cascade_layers)
    
*   [The future of CSS: Cascade layers](https://www.bram.us/2021/09/15/the-future-of-css-cascade-layers-css-at-layer/ "External link (opens in new tab)")
     on bram.us (2021)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@layer/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@layer (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40layer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40layer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40layer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40layer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe328268bb418551ab451881845881b5837c9da83%0A*+Document+last+modified%3A+2026-04-20T16%3A14%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")