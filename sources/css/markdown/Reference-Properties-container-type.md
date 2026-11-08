*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#mdn-search)
    

`container-type` CSS property
=============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since February 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **container-type** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the type of container context used in a container query.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#syntax)

------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#values)

This property is specified as one or two keyword values from the following list. In the two-value case, one must be `scroll-state` and the other must be `inline-size` or `size`:

[`anchored`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#anchored)

Establishes a query container for anchored container queries on the container. In this case, the size of the element is not computed in isolation; no [containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using)
 is applied.

[`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#inline-size)

Establishes a query container for dimensional queries on the [inline axis](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts#block_and_inline_dimensions)
 of the container. Applies [style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#style)
 and [inline-size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#inline-size)
 containment to the element. The inline size of the element can be [computed in isolation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using#size_containment)
, ignoring the child elements (see [Using CSS containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Using)
).

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#normal)

Default value. The element is not a query container for any container size, scroll-state, or anchored queries, but can be used as a query container for [container style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#container_style_queries)
 and [name-only container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#name-only_container_queries)
.

[`scroll-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#scroll-state)

Establishes a query container for scroll-state queries on the container. In this case, the size of the element is not computed in isolation; no containment is applied.

[`size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#size)

Establishes a query container for container size queries in both the [inline and block](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Logical_properties_and_values/Basic_concepts#block_and_inline_dimensions)
 dimensions. Applies [style](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#style)
 and [size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain#size)
 containment to the element. Size containment is applied to the element in both the inline and block directions. The size of the element can be computed in isolation, ignoring the child elements.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | a [color](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#interpolation "Values of the <color> CSS data type are interpolated on each of their red, green, blue components, each handled as a real, floating-point number. Note that interpolation of colors happens in the alpha-premultiplied sRGBA color space to prevent unexpected grey colors to appear.") |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

container-type =   
  normal                                      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 size [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inline-size [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 scroll-state [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#description)

----------------------------------------------------------------------------------------------------------------

Container queries allow you to selectively apply styles inside a container based on conditional queries performed on the container. The [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
 at-rule is used to specify the tests performed on a container, and the rules that will apply to the container's contents if the query returns `true`.

Certain types of container query can only be performed on elements with specific `container-type` property values set, which establish specific container contexts on those containers:

*   [Size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#container_size_queries)
    : Enable selectively applying CSS rules to a container's children based on a general size or inline size condition such as a maximum or minimum dimension, aspect ratio, or orientation.
*   [Scroll-state](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#container_scroll-state_queries)
    : Enable selectively applying CSS rules to a container's children based on a scroll-state condition such as whether the container is a scroll container that is partially scrolled or whether the container is a [snap target](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snap_target)
     that is going to be snapped to its scroll snap container.
*   [Anchored](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#anchored_container_queries)
    : Enable selectively applying CSS rules to a container's children based on whether the container is [anchor-positioned](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
     and has a [position-try fallback option](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Try_options_hiding)
     applied to it.

If a `container-type` is not set on a container, the element is not a query container for container size, scroll-state, or anchored queries, but can still be used as a query container for [container style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#container_style_queries)
 and [name-only container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#name-only_container_queries)
.

### [Container size queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#container_size_queries)

[Container size queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#container_size_queries)
 allow you to selectively apply CSS rules to a container's descendants based on a size condition such as a maximum or minimum dimension, aspect ratio, or orientation.

Size containers additionally have size containment applied to them — this turns off the ability of an element to get size information from its contents, which is important for container queries to avoid infinite loops. If this were not the case, a CSS rule inside a container query could change the content size, which in turn could make the query evaluate to false and change the parent element's size, which in turn could change the content size and flip the query back to true, and so on. This sequence would then repeat itself in an endless loop.

The container size has to be set by context, such as block-level elements that stretch to the full width of their parent, or explicitly defined. If a contextual or explicit size is not available, elements with size containment will collapse.

**Note:** Size containers' descendants can be sized using [container query length units](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#container_query_length_units)
.

### [Container scroll-state queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#container_scroll-state_queries)

[Container scroll-state queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Container_scroll-state_queries)
 allow you to selectively apply CSS rules to a container's children based on a scroll-state condition such as:

*   Whether the container's contents are partially scrolled.
*   Whether the container is a snap target that is going to be snapped to a scroll snap container.
*   Whether the container is positioned via [`position: sticky`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
     and stuck to a boundary of a [scrolling container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
    .

In the first case, the queried container is the scroll container itself. In the other two cases the queried container is an element that is affected by the scroll position of an ancestor scroll container.

### [Anchored container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#anchored_container_queries)

[Anchored container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Anchored_container_queries)
 allow you to selectively apply CSS rules to the descendants of an anchor-positioned container when it has a position-try fallback active on it, as specified via the [`position-try-fallbacks`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
 property.

For example, you might have an anchor-positioned tooltip element that is positioned above its anchor by default via a [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 value of `top`, but has a `position-try-fallbacks` value of `flip-block` specified. This will cause the tooltip to flip in the block direction to the bottom of its anchor when it starts to overflow the top of the viewport. If we set `container-type: anchored` on it, we can detect when the position-try fallback is applied via a `@container` at-rule and apply CSS as a result.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#examples)

----------------------------------------------------------------------------------------------------------

### [Establishing inline size containment](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#establishing_inline_size_containment)

Given the following HTML example which is a card component with an image, a title, and some text:

To create an inline size container context, add the `container-type` property to an element with a value of `inline-size`:

Writing a container query via the [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
 at-rule will apply styles to the elements of the container when it is wider than `400px`:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Conditional Rules Module Level 5  <br>\# container-type](https://drafts.csswg.org/css-conditional-5/#container-type) |
| [CSS Anchor Positioning Module Level 2  <br>\# container-type-anchored](https://drafts.csswg.org/css-anchor-position-2/#container-type-anchored) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type#see_also)

----------------------------------------------------------------------------------------------------------

*   [CSS container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
    
*   [Using container size and style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries)
    
*   [Using container scroll-state queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Container_scroll-state_queries)
    
*   [Using anchored container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Anchored_container_queries)
    
*   [`@container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container)
     at-rule
*   CSS [`container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container)
     shorthand property
*   CSS [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
     property
*   CSS [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
     property

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 6, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/container-type/index.md?plain=1 "Folder: en-us/web/css/reference/properties/container-type (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontainer-type&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontainer-type%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcontainer-type%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcontainer-type%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F892eb917bee599a9d6cae7d33ed783129dbb39b3%0A*+Document+last+modified%3A+2026-10-06T01%3A16%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")