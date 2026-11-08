*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#mdn-search)
    

Using container size and style queries
======================================

[Container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
 enable you to apply styles to elements nested within a specific container based on the features of that container. The query returns true or false depending on whether the query condition is true for the container.

Container queries are similar to [media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
. The [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 at-rule enables applying styles to elements based on viewport size or other device characteristics. Similarly, the [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
 at-rule enables applying styles to elements based on a containing element's size or other features, rather than the viewport's. Container queries have the same syntax rules and logical operators as media queries.

There are five types of container queries:

[**Container size queries**](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_size_queries_2)

Size queries enable applying styles to elements based on the current [size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#descriptors)
 of a containing element, including the orientation and [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
. The containing elements need to be explicitly declared as _size query containers_.

**[Container style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#container_style_queries)
**

Style queries enable applying styles to elements based on a containing element's style features, where any non-empty element can be a style query container. A style feature can be a CSS property, CSS [custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
, or a valid CSS [declaration](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#css_declarations)
. This allows you to apply styles to any container element's descendants based on its style features — such as whether it has a `display: inline` flex declaration set, or the value of a custom property.

**[Name-only container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#name-only_container_queries)
**

Name-only container queries enable selectively applying styles to an element based on whether it has a specific [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
 set.

**[Container scroll-state queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Container_scroll-state_queries)
**

Scroll-state queries allow you to selectively apply CSS rules to a container's descendants based on scroll-state conditions, such as whether the queried element is partially scrolled or whether the container is snapped to a scroll snap container. The containing elements need to be explicitly declared as _scroll-state query containers_.

**[Anchored container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Anchored_container_queries)
**

Anchored container queries enable querying whether the container is [anchor-positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 and has a [position-try fallback option](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)
 applied to it.

In this guide, we learn the basics of container queries by looking at:

1.  [container size queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_size_queries_2)
    ,
2.  [naming containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#naming_containers)
     to limit their scope, and
3.  using the `style()` functional notation within the [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
     at rule's `<container-condition>` to create [style queries with custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#style_queries_for_custom_properties)
    .

[Container size queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_size_queries)

------------------------------------------------------------------------------------------------------------------------------------------------------

Container size queries are filtered by a size condition. The associated styles are applied to contained elements if the container element has been declared to be a container and the container condition is true for that element. An element's size container is the nearest ancestor with containment.

Elements are declared as _size query containers_ by setting their [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
 property (or the [`container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container)
 shorthand) to `size` or `inline-size`.

Declaring size query containers adds [containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using)
 to them. This is a performance necessity — querying the size of every element in the DOM, all the time, would be bad for performance and user experience. Additionally, if a descendant style changed the size of the container element, an infinite loop could occur.

In a container size query, the `<container-condition>` includes one or more `<size-query>`s. Each size query includes a size feature name, a comparison operator, and a value. The size features that can be queried are limited to `width`, `height`, `inline-size`, `block-size`, `aspect-ratio`, and `orientation`. The boolean syntax and logic combining one or more `<size-query>`s is the same as for [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 size feature queries.

The `<container-condition>` in this example contains a single `<size-query>` — `(10em <= width <= 20em)`. In this case, all [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 elements are potential matches for any unnamed container query. The styles declared within our container query apply to the descendants of all forms between `10em` and `30em` wide, inclusive.

[Naming containers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#naming_containers)

--------------------------------------------------------------------------------------------------------------------------------------------

A `<container-condition>` can include an optional case-sensitive [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
. A container name makes the container condition more specific — it is evaluated only against elements that have that name set in the `container-name` property.

The [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
 property specifies a list of query `<container-name>` values that can be used in `@container` rules to target specific query containers; these are case-sensitive [`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
 values. Without a `<container-name>`, the query matches only the nearest container ancestor, and without a `<container-query>`, the query will match elements with the specified `container-name` set on them (see [Name-only container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#name-only_container_queries)
).

Styles inside the named `@container` at rules will be applied only to matching elements inside containers with those names set, which satisfy the container queries.

In the above example, the styles within the container query block will apply to the descendants of all [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements with a width that is greater than their height. Note that other elements with `container-name: card` applied to them that match the size query will also have these styles applied to their elements' descendants.

In the above example, the element has two container names, `wide` and `narrow`. The descendants of any elements with `class="sizeContainer"` will get the styles from the `wide` or `narrow` query applied.

The default value `container-type: normal` prevents the container from being a size container, but it can still be a [style container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_style_queries)
, and it can still be targeted by a [name-only container query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#name-only_container_queries)
. The default value `container-name: none` states the container has no name, but it does not prevent the element from matching unnamed queries.

[Container style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_style_queries)

--------------------------------------------------------------------------------------------------------------------------------------------------------

A _container style query_ is a `@container` query that evaluates computed styles of the container element as defined in one or more `style()` functional notations. The boolean syntax and logic used to combine style features into a style query are the same as in [CSS feature queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
. The only difference is the function name — `style()` within a `<style-feature>` as opposed to `supports()` within a `<support-condition>`:

The parameter of each `style()` function is a single **`<style-feature>`**. Per the CSS containment specification, a `<style-feature>` can be a valid CSS [declaration](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#css_declarations)
, a CSS property, or a [`<custom-property-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#values)
. The only style feature currently supported is custom properties, with or without a value. See the [browser compatibility table for `@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#browser_compatibility)
.

If the `<style-feature>` includes a value, the style query evaluates to true if the computed value of the custom property (or, in the future, the CSS declaration) passed as the `style()` argument is true for the container being queried. Otherwise, it resolves to false. A style feature without a value evaluates to true if the computed value is different from the [initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#registered_properties)
 for the given property.

In the future, we'll be able to write style queries like so:

The `style()` functional notation is used to differentiate style queries from size queries. While not yet supported, we will eventually be able to query regular CSS declarations such as `max-width: 600px`. Querying `@container (max-width: 600px)` is a size query; containment with [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
, or the [`container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container)
 shorthand, is needed. That query will return true if the container is 600px or less. That is different from querying `@container style(max-width: 600px)`, which is a style query; when supported, this query will return true if the container has a [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 value of `600px`.

Until style queries for regular CSS declarations and properties are supported, we are limited to including only custom properties as the `style()` parameter, with or without a value:

A few things to note that have already been mentioned but are important to remember:

*   All elements can be style query containers; setting a `container-type` is not required. When descendant styles don't impact the computed styles of an ancestor, containment is not needed.
*   A `<container-condition>` can include both style and size features. If including size features in your query, make sure your container elements have a `container-type` of `size` or `inline-size` set.
*   If you don't want an element to be considered as a container, ever, give it a `container-name` that will not be used. Setting `container-name: none` removes any query names associated with a container; it does not prevent the element from being a style container.
*   At the time of this writing (February 2024), container style queries only work with CSS custom property values in the `style()` query.

Now, let's dive in and take a look at the different `<style-feature>` types.

### [Style queries for custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#style_queries_for_custom_properties)

Style queries for custom properties allow you to query the [custom properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascading_variables/Using_custom_properties)
, also called "CSS variables", of a parent element. They are included within a `<style-query>` just as you would include any regular CSS property within a feature query: either with or without a value.

#### Standalone custom property queries

The `<style-query>` parameter of the `style()` functional notation can include just a CSS variable name; a custom property with no value. When no value is included, the query will return false if the value is the same as the value of the `initial-value` descriptor within the `@property` at-rule, if there is one. The style query will return true and match all elements that have a custom property value that differs from the `initial-value` or for all elements that have a custom property of any value if the custom property was declared without being registered.

##### Unregistered custom properties

When CSS variables are introduced via a CSS custom property value assignment, valueless custom property queries always return true.

In this example, the container query matches the element on which the `--theme-color` property was declared and all of its descendants. As the CSS variable `--theme-color` was declared on the [`:root`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:root)
, the style query `style(--theme-color)` will be true for every element within that [DOM](https://developer.mozilla.org/en-US/docs/Glossary/DOM)
 node.

##### Registered properties

The behavior of registered custom properties is different. When explicitly defined with the [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 CSS at-rule or via JavaScript with [`CSS.registerProperty()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/registerProperty_static "CSS.registerProperty()")
, the style query `style(--theme-color)` only returns true for elements if the element's computed value for `--theme-color` is different from the [`initial-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/initial-value)
 set in the original definition of that custom property.

In this example, the `:root` element does NOT match the style query because the value of the custom property is the same as the `initial-value` value. The custom property value for the element (and all the elements inheriting the value) is still `rebeccapurple`. Only elements that differ from the initial value, in this case, the [`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main)
 and its descendants that inherit that changed value, are a match.

#### Custom property with a value

If a style query includes a value for the custom property, the element's computed value for that property must be an exact match, with equivalent values only being a match if the custom property was defined with a [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 at rule (or a [`CSS.registerProperty()`](https://developer.mozilla.org/en-US/docs/Web/API/CSS/registerProperty_static "CSS.registerProperty()")
 method call) containing a `syntax` descriptor.

This container style query matches any element that has `blue` as the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
 of the `--accent-color` custom property.

In this case, other color values equivalent to sRGB `blue` (such as the hexadecimal code `#0000ff`) will match only if the `--accent-color` property was defined as a color with `@property` or `CSS.registerProperty()`, for example:

In this case, if the value of `--accent-color` were set to `blue`, `#00f`, `#0000ff`, `rgb(0 0 255 / 1)`, or `rgb(0% 0% 100%)` it would return true for `@container style(--accent-color: blue)`.

##### Example

In this example, we have a [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
 with four radio buttons. The fourth option includes a text [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 for entering a custom color.

JavaScript updates the value of the CSS `--theme` variable on the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 element, which is an ancestor of the [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
 and [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
 elements, whenever a radio button is selected. When the text `<input>` is updated, the [`value`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/value "value")
 of the `other` radio button is updated only if the `other` radio button is checked, which in turn updates the value of `--theme`.

We use the `@property` at-rule to define a CSS variable `--theme` to be a [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 value and set the `initial-value` to `red`, ensuring equivalent colors are a match regardless of what syntax is used (for example, `red` is equal to `rgb(255 0 0)`, `#ff0000`, and `#f00`).

The first style feature query is a custom property with no value. This query type returns true when the computed value for the custom property value is different from the `initial-value` for that property. In this case, it will be true when the value of `--theme` is any value other than any syntax equivalent value of `red` (such as `#ff0000`). When true, the [`<output>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/output)
 will have a 5px dotted outline. The outline color is the current value of `--theme`. The default text [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 is gray.

The second and third style queries include values for the custom property. These will match if the container's `--theme` value is an equivalent color to the value listed, even if that value is the same as the `initial-value`. The first query matches elements whose `--theme` value is equivalent to `red`, `blue`, or `green`. When it is, the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 will be the color current value of `--theme` (in the case of `blue` and `green`, overriding the gray set in the first style query).

The second style query states that when `--theme` is equivalent to `red`, the `<output>`'s contents will also be bold. We did this to better demonstrate that the container query is a match.

Try entering different color values into the text box. You may notice that values that are sRGB equivalents of `red` will make the `<output>` red — as it matches `style(--theme: red)` — while removing the outline, because `style(--theme)` returns false if the element's value for `--theme` is the same as the initial value for `--theme` defined by the `@property` at-rule. Any non-red sRGB valid color value, including `currentColor` or `hsl(180 100% 50%)`, etc., makes the first style query return true; they are values that are different from the `initial-value`.

Because we set `syntax: "<color>";`, the CSS variable can only be assigned valid `<color>` values. Valid values for the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property that aren't value `<color>` values, such as `unset` or `inherit`, are [invalid](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Error_handling)
 for this custom property, and will be ignored.

If you enter `unset` or `gibberish`, the JavaScript updates the `style` on the [`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body)
 to `--theme: unset` or `--theme: gibberish`. Neither of these are colors. Both are invalid and ignored. This means the initial value is inherited and unchanged, with `style(--theme)` returning false and `style(--theme: red)` returning true.

**Note:** When declaring custom properties, consider using `@property` with the [`syntax`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property/syntax)
 descriptor so the browser can properly compare computed values.

### [Plain versus range syntax in style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#plain_versus_range_syntax_in_style_queries)

When a `<style-feature>` includes a value, you can express the comparison in two different ways. They look similar but behave very differently, and choosing the right one matters.

The **plain syntax** uses a colon, the same syntax used in a CSS declaration:

This form is true if the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
 of the property matches the value on the right. For an [unregistered](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#unregistered_custom_properties)
 custom property, the computed value is the property's value as written: the browser doesn't evaluate `calc()` or other expressions inside it. The match is essentially a comparison of the two values' tokens. To match equivalent values (such as `blue` and `#0000ff`), [register the custom property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#registered_properties)
 with `@property` and a `syntax` descriptor.

The **range syntax** uses a comparison operator (`=`, `<`, `<=`, `>`, or `>=`):

To evaluate this form, the browser:

1.  Resolves each side (custom property names are looked up as if used with [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
    ).
2.  Parses each side as one of [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    , [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    , [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    , [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
    , [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
    , [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
    , or [`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
    . If either side can't be parsed as one of those types, the query is false.
3.  If both sides have the same type, computes each side (evaluating any `calc()` expressions) and performs the numeric comparison. Otherwise, the query is false.

Consider the following example, where `--n` is set to a `calc()` expression:

The range syntax also supports a three-value form for testing whether a value falls within an interval. Both comparators must point the same way:

The range syntax is also more flexible in how each side is written. Either side can be a custom property name, a [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
 reference, a literal value, or a `calc()` expression, and the operands can appear in any order. The following are all valid:

The plain syntax is more restrictive: the left-hand side must be the custom property name (without `var()`), and the value goes on the right. The following are all **invalid**:

Because the range syntax requires both sides to parse as one of the listed numeric types, it can't be used to compare keyword-like values. For example, given `--s: new`, the query `style(--s = new)` is false (because `new` isn't a number, length, etc.), while `style(--s: new)` is true.

In short:

*   Use **`style(--variable: value)`** for keyword-like or string-like matching, such as `style(--stock: low)` or `style(--theme: dark)`.
*   Use **`style(--variable = value)`** (or `<`, `<=`, `>`, `>=`) for numeric comparisons, such as `style(--columns >= 3)` or `style(--gap = 1rem)`.

### [Nested queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#nested_queries)

Container queries can be nested within other container queries. The styles defined inside multiple nested container queries are applied when all of the wrapping container queries are true.

In this case, the `<output>` will have a 5px dotted border if it's nested in a container where `--theme: purple` is set, and that container is nested within a container whose `--theme` value is `red`.

### [Style query CSS declarations and properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#style_query_css_declarations_and_properties)

Not yet supported in any browser, the `style()` functional notation can include regular CSS declarations including CSS properties and property value pairs.

When supported, this basic example will make the background color of any [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
 and [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
 elements yellow when the parent is already `bold`.

The matching is done against the computed value of the parent container; if the parent's computed [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 is `bold` (not `bolder` or `900`), there is a match. Just as with custom property container style queries, we did not have to define any elements as style containers as all elements are style containers by default. As long as an element doesn't have a `container-name` set, if it has `font-weight: bold` set or inherited, it will match.

Style features that query a shorthand property will be true if the computed values match for each of its longhand properties, and false otherwise. For example, ``@container style([`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border) : 2px solid red)`` will resolve to true if all 12 longhand properties ([`border-bottom-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-bottom-style)
, etc.) that make up that shorthand are set to the same equivalent values.

The global CSS values `revert` and `revert-layer` are invalid as values in a `<style-feature>` and cause the container style query to be false.

Do not apply the styles you are querying in the style query to the element you are styling with that query as this may cause an infinite loop.

It is expected that style queries will also accept properties in a boolean context. The style query will return false if the value of the property is the initial value for that property (if it has not been changed), and true otherwise.

The above example will return true for any element that has a value for `font-weight` that differs from its initial value. User-agent stylesheets set `font-weight: bold` for [heading](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/Heading_Elements)
 and [`<th>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/th)
 elements, for example. Some browsers set [`<strong>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/strong)
 and [`<b>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/b)
 to `bold`, others to `bolder`. [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
 also sometimes has a `font-weight` other than `normal` set by the user agent. As long as the element's `font-weight` is not the default value for that user-agent, the style query will return true.

These features are not yet supported in any browser.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#see_also)

--------------------------------------------------------------------------------------------------------------------------

*   [Media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
    
*   CSS [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
     at-rule
*   CSS [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
     property
*   CSS [`container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container)
     shorthand property
*   CSS [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
     property
*   [Using container scroll-state queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Container_scroll-state_queries)
    
*   [Understanding `aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_sizing/Aspect_ratios)
    
*   [Getting Started with Style Queries](https://developer.chrome.com/docs/css-ui/style-queries "External link (opens in new tab)")
     (2022)
*   [Style queries](https://una.im/style-queries/ "External link (opens in new tab)")
     via una.im (2022)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/containment/container_size_and_style_queries/index.md?plain=1 "Folder: en-us/web/css/guides/containment/container_size_and_style_queries (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FContainment%2FContainer_size_and_style_queries&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fcontainment%2Fcontainer_size_and_style_queries%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FContainment%2FContainer_size_and_style_queries%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fcontainment%2Fcontainer_size_and_style_queries%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")