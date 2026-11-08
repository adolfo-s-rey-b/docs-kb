*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#mdn-search)
    

CSS property value processing
=============================

For every element in a document tree, the browser assigns a value to every CSS property that applies to that element. The rendered value of each CSS property for a given element or box is the result of a calculation based on stylesheet definitions, inheritance, the [cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
, dependencies, unit conversion, and the display environment. This guide provides an overview of the processing steps applied to define how each CSS value is ultimately rendered by exploring key concepts like specified, computed, used, and actual values.

[Property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#property_values)

-----------------------------------------------------------------------------------------------------------------------------

Every style applied to an element or pseudo-element is based on a single CSS property declaration. Each CSS property has only one value. The value that is applied is determined by the [cascaded values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascaded_value)
 of all the declarations of that property that apply to that element or pseudo-element, with the single value applied coming from the property declaration that ranks highest in the [cascade sorting order](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#cascading_order)
 based on the [cascade algorithm](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
.

When there are multiple [declared values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#declared_value)
, with multiple declarations, providing the same or different property values for the same element, each property value must still come from a single property name-value pair as only a single value is applied from each property, even if the value is a comma-separated list of values.

To determine which [declared value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#declared_value)
 is applied, the user agent gathers and processes all the styles from different sources, such as inline styles, and internal and external stylesheets.

The [cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
 determines which value should be applied when multiple conflicting styles target the same element. The [cascade algorithm](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#cascading_order)
 defines how user agents combine property values originating from different sources, scopes, and/or [layers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#cascade_layers)
. When a selector matches an element, the property's [declared value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#declared_value)
 from the [origin](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#origin_types)
 with the highest precedence gets applied, even if a selector from a lower precedence [origin](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#origin_types)
 or [layers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#cascade_layers)
 has greater [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
.

Certain properties inherit values from their parent elements unless explicitly overridden. [Inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
 may occur when no style information exists for a specific property on an element. If the property is inherited, the value is set to the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
 of the parent element. If the property is not inherited, its value is set to the [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
 for that element.

After applying the [cascading](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascading)
 rules and defaulting values step by step, the browser ensures the visual presentation matches the processed CSS.

[Processing overview](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#processing_overview)

-------------------------------------------------------------------------------------------------------------------------------------

Before diving into the individual value stages, it's important to understand the three main phases that occur in value processing; [filtering](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#filtering)
, [cascading](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascading)
, and [defaulting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#defaulting)
.

### [Filtering](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#filtering)

**Filtering** is the process of identifying all declarations that apply to each element. A declaration applies to an element only if:

*   The declaration belongs to a style sheet that currently applies to this document
*   Any [conditional rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules)
     (like [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
     or [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
    ) that contain the declaration are currently true.
*   The declaration belongs to a style rule whose selector matches the element
*   The declaration is syntactically valid: the property name is recognized by the browser and the value matches the expected syntax for that property

Only valid declarations become declared values. Declarations with invalid property names or invalid values get filtered out according to [CSS error handling rules](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Error_handling)
.

In this example, only the [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 and [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 declarations are processed. The [CSS parser filters out errors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Error_handling#css_parser_errors)
, ignoring or "filtering" out the declaration with the invalid property name:

css

    p {
      font-size: 1.25em;
      colr: blue;
      font-weight: bold;
    }
    

When filtering is complete, every element has zero or more [declared values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#declared_value)
 for every CSS property. These declared values are the starting point for the [cascading](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascading)
 processing stage.

### [Cascading](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascading)

[Cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
 resolves conflicts when multiple declarations apply to the same property on the same element. Cascade sorts declarations using [the cascade sorting order](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction#cascading_order)
 algorithm.

For example, both [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 declarations match `<p class="large">CSS is fun!</p>`, but the second declaration gets applied because it has higher [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
. Both declarations have author origin, but the second selector has specificity of `0-1-1` while the first has `0-0-1`:

css

    p {
      font-size: 1em;
    }
    
    p.large {
      font-size: 1.5em;
    }
    

After cascading, the browser determines the [**cascaded value**](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascaded_value)
 for each property on each element. This is the value used in the next processing stage; [defaulting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#defaulting)
.

### [Defaulting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#defaulting)

**Defaulting** ensures every property on every element has a value. This involves applying default property values when no CSS declarations explicitly set that property value. This involves:

*   Setting **inherited values** for [inherited properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#inherited_properties)
    
*   Setting **initial values** for [non-inherited properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#non-inherited_properties)
    

As a result of defaulting, every property is guaranteed to have a [specified value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
.

Note that explicit defaulting keywords ([`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
, [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
, [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
, [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
, [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
) are also resolved to their corresponding values to determine the [specified value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
.

[Processing stages](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#processing_stages)

---------------------------------------------------------------------------------------------------------------------------------

All elements that are part of the document's flattened element tree have [declared](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#declared_value)
, [cascaded](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascaded_value)
, [specified](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
, [computed](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
, [used](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
, and [actual](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
 values. For a specific property, these values may or may not be the same. For example, if your large code base includes the CSS `p { font-size: 1.25em; }` and your HTML includes `<p class="large">CSS is fun!</p>`, what size will the paragraph be? The [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 value moves through a few stages to go from the `em` specified value to the rendered `px` value.

The value processing stages are [Declared value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#declared_value)
, [Cascaded value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascaded_value)
, [Specified value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
, [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
, [Used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
, and [Actual value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
. These values are used to determine the final [rendered value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#rendered_values)
.

### [Declared value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#declared_value)

A **declared value** is any syntactically valid value from a declaration that applies to an element. An element can have zero or more declared values for each property. These values come from style sheets (author, user, or user-agent) and are identified during the [filtering](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#filtering)
 stage.

Continuing our example, in which our stylesheet includes an occurrence of `p { font-size: 1.25em; }` and the document linking to that stylesheet includes `<p class="large">CSS is fun!</p>`, there may be other `font-size` declarations that could potentially apply to the same paragraph. The user-agent stylesheet might set `font-size: 1em` for all paragraphs, while another author declaration sets `font-size: 2em` for elements with class "large":

css

    /* User agent styles */
    p {
      font-size: 1em;
    }
    
    /* author styles */
    p {
      font-size: 1.25em;
    }
    
    .large {
      font-size: 2em;
    }
    

There may be many other `font-size` declarations in our stylesheets, but only declarations whose selectors match the element become declared values. In this example, as our `<p>` element has `class="large"`, all three declarations are declared values for this element.

### [Cascaded value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascaded_value)

The **cascaded value** is the declared value that wins the [cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascading)
. There is at most one cascaded value per property per element.

From our declared values, author styles win over user agent styles. Within the same origin, higher specificity styles win over lower specificity styles. In this case, the cascaded value would be `font-size: 2em`, from the author origin with specificity `0-1-1`:

css

    font-size: 2em;
    

If there are no declared values for a property, there is no cascaded value, which means the [specified value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
 for that property is determined by the [defaulting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#defaulting)
 process.

### [Specified value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)

The **specified value** is the result of the [defaulting](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#defaulting)
 process. It is guaranteed to exist for every property on every element. The specified value is determined as follows:

1.  If there is a [cascaded value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascaded_value)
    , the cascaded value is the specified value.
2.  If there is _no_ cascaded value and the property is [inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
    , the specified value is the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
     of the parent element.
3.  If there is _no_ cascaded value and the property is _not_ inherited, the specified value is the property's [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
    .

In our example, since we have a [cascaded value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#cascaded_value)
 of `2em`, this becomes the specified value:

css

    font-size: 2em;
    

For properties without cascaded values, the defaulting process determines the value. For example, if `color` is not specified, the `color` is inherited from the parent's computed value since it's an inherited property. If `margin` is not specified, the `initial` value of `0` is used as `margin` is not an [inherited property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#inherited_properties)
:

css

    color: inherit;
    margin: 0;
    

#### Initial value

A property's **initial value** is the default value as listed in its definition table in the specification. The initial value is used during defaulting when:

*   For [inherited properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#inherited_properties)
    , the initial value is used on the _root element only_, which has no parent element, when no cascaded value exists.
*   For [non-inherited properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance#non-inherited_properties)
    , the initial value is used on _all elements_ when no cascaded value exists.

You can explicitly set the initial value by using the [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
 keyword.

**Note:** The initial value can be found in the formal syntax section of each CSS property reference page. For example, the [initial value of `font-size` is `medium`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size#formal_definition)
. The initial value should not be confused with the value specified by the browser's style sheet.

### [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)

The **computed value** of a property is the value transferred from parent to child during inheritance. It is the result after resolving things like relative units and custom properties into absolute values, but before considering layout-specific information.

The computed value is calculated from the [specified value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
 by:

1.  Handling the special values [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
    , [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
    , [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
    , [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
    , and [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
    .
2.  Doing the computation needed to reach the value described in the "Computed value" line in the property's definition table.

The computation needed to reach a property's computed value typically involves converting relative values (such as those in `em` units or percentages) to absolute values. For example, if an element has specified values `font-size: 16px` and `padding-top: 2em`, then the computed value of `padding-top` is `32px` (double the font size).

However, for some properties (those where percentages are relative to something that may require layout to determine, such as `width`, `margin-right`, `text-indent`, and `top`), percentage-specified values turn into percentage-computed values. Additionally, unitless numbers specified on the `line-height` property become the computed value, as specified. The relative values that remain in the computed value become absolute when the [used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
 is determined.

### [Used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)

The **used value** is the property's value after all calculations have been performed on the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
 and it has been refined with layout-specific details (e.g., percentages resolved to actual pixel values).

Every CSS property has a used value. The used values of dimensions (e.g., [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 or [`line-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/line-height)
) are in pixels. The used values of shorthand properties (e.g., [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
) are consistent with those of their component properties (e.g., [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 or [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
) and with [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 and [`float`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/float)
.

The used value for the [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 or [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
 of an element is a pixel value even if the specified value of the property was set with percentages or keyword values.

If we have three container elements with their width set as `auto`, `50%`, and `inherit`:

    <div id="no-width">
      <p>No explicit width.</p>
      <p class="show-used-width">..</p>
    
      <div id="width-50">
        <p>Explicit width: 50%.</p>
        <p class="show-used-width">..</p>
    
        <div id="width-inherit">
          <p>Explicit width: inherit.</p>
          <p class="show-used-width">..</p>
        </div>
      </div>
    </div>
    

css

    #no-width {
      width: auto;
    }
    
    #width-50 {
      width: 50%;
    }
    
    #width-inherit {
      width: inherit;
    }
    
    /* Make results easier to see */
    div {
      border: 1px solid red;
      padding: 8px;
    }
    

    function updateUsedWidth(id) {
      const div = document.getElementById(id);
      const par = div.querySelector(".show-used-width");
      const wid = window.getComputedStyle(div)["width"];
      par.textContent = `Used width: ${wid}.`;
    }
    
    function updateAllUsedWidths() {
      updateUsedWidth("no-width");
      updateUsedWidth("width-50");
      updateUsedWidth("width-inherit");
    }
    
    updateAllUsedWidths();
    window.addEventListener("resize", updateAllUsedWidths);
    

While the three specified values, `auto`, `50%`, and `inherit`, are keyword and [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 values, retrieving the `width` using `window.getComputedStyle(el)["width"];` returns an [absolute length](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length#absolute_length_units)
 `px` value:

Change the window size or rotate your mobile device to change the size and the used values.

[Rendered values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#rendered_values)

-----------------------------------------------------------------------------------------------------------------------------

The rendered value is called the [actual value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)
, while the value retrieved via script is called the [resolved value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#resolved_value)
.

### [Actual value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#actual_value)

The **actual value** of a property is the [used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
 of that property after any necessary approximations have been applied. It is the final rendered value as implemented by the browser, including adjustments for rendering quirks or limitations. For example, a [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 that can only render borders with a whole-number pixel width may round the thickness of the border to the nearest integer.

The calculation includes these steps:

1.  First, the [specified value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#specified_value)
     is determined based on the result of [cascading](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
    , [inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance)
    , or using the [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value)
    .
2.  Next, the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
     is calculated according to the specification (for example, a `span` with `position: absolute` will have its computed `display` changed to `block`).
3.  Then, layout is calculated, resulting in the [used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
    .
4.  Finally, the used value is transformed according to the limitations of the local environment, resulting in the actual value.

### [Resolved value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#resolved_value)

The **resolved value** of a property is the value after applying active stylesheets and resolving any basic computation those values may contain. The [`getComputedStyle()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle "getComputedStyle()")
 method returns a live [`CSSStyleDeclaration`](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration)
 object containing the resolved values of all CSS properties applied to a specified element. Each resolved value is either the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
 or the [used value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#used_value)
, depending on the property.

Historically, `getComputedStyle()` returned the computed value of an element or pseudo-element. As CSS evolved, so did the concept of "computed value", but the values returned by `getComputedStyle()` had to remain the same for backward compatibility with deployed scripts. These values are the "resolved values".

For most properties, the resolved value is the computed value, but for a few legacy properties (including [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 and [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
), it is the used value. The [CSSOM specification](https://drafts.csswg.org/cssom/#resolved_values "External link (opens in new tab)")
 provides per-property details.

CSS 2.0 defined _computed value_ as the last step in a property's calculation. CSS 2.1 introduced the distinct definition of "used value". An element could then explicitly inherit the width/height of its parent, whose computed value is a percentage. For CSS properties that don't depend on layout (e.g., `display`, `font-size`, or `line-height`), the computed values and used values are the same. The following list contains the CSS 2.1 properties that _do_ depend on layout, and therefore have a different computed value and used value (taken from [CSS 2.1 Changes: Specified, computed, and actual values](https://www.w3.org/TR/CSS2/changes.html#q21.36 "External link (opens in new tab)")
):

*   [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
    
*   [`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/bottom)
    , [`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/left)
    , [`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/right)
    , [`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/top)
    
*   [`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/height)
    , [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
    
*   [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
    , [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
    , [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
    , [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
    
*   [`min-height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-height)
    , [`min-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/min-width)
    
*   [`padding-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-bottom)
    , [`padding-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-left)
    , [`padding-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-right)
    , [`padding-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding-top)
    
*   [`text-indent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-indent)
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#see_also)

---------------------------------------------------------------------------------------------------------------

*   CSS values for controlling inheritance: [`inherit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/inherit)
    , [`initial`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/initial)
    , [`revert`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert)
    , [`revert-layer`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/revert-layer)
    , and [`unset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/unset)
    
*   [CSS cascading and inheritance](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade)
     module
*   [CSS syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jan 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/cascade/property_value_processing/index.md?plain=1 "Folder: en-us/web/css/guides/cascade/property_value_processing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCascade%2FProperty_value_processing&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcascade%2Fproperty_value_processing%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FCascade%2FProperty_value_processing%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcascade%2Fproperty_value_processing%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6ad108adad746bd7ed79b5b32d8d3e05e5ec685a%0A*+Document+last+modified%3A+2026-01-06T00%3A03%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")