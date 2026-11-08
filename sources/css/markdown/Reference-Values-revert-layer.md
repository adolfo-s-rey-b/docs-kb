*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer#mdn-search)
    

`revert-layer` CSS keyword
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`revert-layer`** [CSS-wide keyword](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/Data_types#css-wide_keywords)
 rolls back the value of a property in a [cascade layer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@layer)
 to the value of the property in a CSS rule matching the element in a previous cascade layer. The value of a property with this keyword is recalculated as if no rules were specified on the target element in the current cascade layer.

If there is no other cascade layer to revert to for the matching CSS rule, the property value rolls back to the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
 derived from the current layer. Furthermore, if there is no matching CSS rule in the current layer, the property value for the element rolls back to the style defined in a previous [style origin](https://developer.mozilla.org/en-US/docs/Glossary/Style_origin)
.

This keyword can be applied to any CSS property, including the CSS shorthand property [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
.

[Revert-layer vs. revert](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer#revert-layer_vs._revert)

----------------------------------------------------------------------------------------------------------------------------------

The `revert-layer` keyword lets you rollback styles to those specified in previous cascade layers within the [author origin](https://developer.mozilla.org/en-US/docs/Glossary/Style_origin)
. The [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
 keyword, in comparison, lets you roll back styles applied in the author origin to those specified in the user origin or user-agent origin.

The `revert-layer` keyword is ideally meant to be applied to properties within a cascade layer. However, if applied to properties outside a cascade layer, it rolls back property values to any values set by presentational hints (such as `width` and `height` attributes or the `<s>` element in HTML), defaulting to the values established by the user agent's stylesheet or user styles. Unlike the `revert` keyword, which considers presentational hints as part of the author origin and reverts them as well, the `revert-layer` keyword ignores presentational hints outside the cascade layer, so it does not revert them.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer#examples)

----------------------------------------------------------------------------------------------------

### [Default cascade layer behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer#default_cascade_layer_behavior)

In the example below, two cascade layers are defined in the CSS, `base` and `special`. By default, rules in the `special` layer will override competing rules in the `base` layer because `special` is listed after `base` in the `@layer` declaration statement.

#### HTML

html

    <p>This example contains a list.</p>
    
    <ul>
      <li class="item feature">Item one</li>
      <li class="item">Item two</li>
      <li class="item">Item three</li>
    </ul>
    

#### CSS

css

    @layer base, special;
    
    @layer special {
      .item {
        color: red;
      }
    }
    
    @layer base {
      .item {
        color: blue;
      }
      .feature {
        color: green;
      }
    }
    

#### Result

All the `<li>` elements match the `item` rule in the `special` layer and are red. This is the default cascade layer behavior, where rules in the `special` layer take precedence over rules in the `base` layer.

### [Revert to style in previous cascade layer](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer#revert_to_style_in_previous_cascade_layer)

Let's examine how the `revert-layer` keyword changes the default cascade layer behavior. For this example, the `special` layer contains an additional `feature` rule targeting the first `<li>` element. The `color` property in this rule is set to `revert-layer`.

#### HTML

html

    <p>This example contains a list.</p>
    
    <ul>
      <li class="item feature">Item one</li>
      <li class="item">Item two</li>
      <li class="item">Item three</li>
    </ul>
    

#### CSS

css

    @layer base, special;
    
    @layer special {
      .item {
        color: red;
      }
      .feature {
        color: revert-layer;
      }
    }
    
    @layer base {
      .item {
        color: blue;
      }
      .feature {
        color: green;
      }
    }
    

#### Result

With `color` set to `revert-layer`, the `color` property value rolls back to the value in the matching `feature` rule in the previous layer `base`, and so 'Item one' is now green.

### [Revert to style in previous origin](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer#revert_to_style_in_previous_origin)

This example shows the `revert-layer` keyword behavior when there is no cascade layer to revert to _and_ there is no matching CSS rule in the current layer to inherit the property value.

#### HTML

html

    <p>This example contains a list.</p>
    
    <ul>
      <li class="item feature">Item one</li>
      <li class="item">Item two</li>
      <li class="item">Item three</li>
    </ul>
    

#### CSS

css

    @layer base {
      .item {
        color: revert-layer;
      }
    }
    

#### Result

The style for all `<li>` elements rolls back to the defaults in the user-agent origin.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Cascading and Inheritance Level 5  <br>\# revert-layer](https://drafts.csswg.org/css-cascade-5/#revert-layer) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer#see_also)

----------------------------------------------------------------------------------------------------

*   [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
    
*   [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
    
*   [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
    
*   [`revert-rule`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-rule)
    
*   [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
    
*   [`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/all)
    
*   [CSS cascading and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/revert-layer/index.md?plain=1 "Folder: en-us/web/css/reference/values/revert-layer (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frevert-layer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frevert-layer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2Frevert-layer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2Frevert-layer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F0aa8517faf9d7d15c745ac94db7014d3a2d2085f%0A*+Document+last+modified%3A+2026-04-20T12%3A06%3A36.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")