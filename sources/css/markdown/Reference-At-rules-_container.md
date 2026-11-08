*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#mdn-search)
    

`@container` CSS at-rule
========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since February 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`@container`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 is a conditional group rule that applies styles to a [containment context](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#naming_containment_contexts)
. Style declarations are filtered by a condition and applied to the elements within the container if the condition is true. The condition is evaluated when the queried container size, [`<style-feature>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#container_style_queries)
, or scroll-state changes.

The condition must specify a [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
, a `<container-query>`, or both.

The [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
 property specifies a list of query container names, which are used to filter which containers are targeted by the `@container` rules. If only a `container-name` value is included (a [name-only container query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries#name-only_container_queries)
), the contained rules are applied to any containers with one or more of those `container-name` values set on them.

The container features in the `<container-query>` are evaluated against the selected containers. If no `<container-name>` is specified, the `<container-query>` features are evaluated against the nearest ancestor query container that has the matching [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#syntax)

------------------------------------------------------------------------------------------------

css

    /* With a <size-query> */
    @container (width > 400px) {
      h2 {
        font-size: 1.5em;
      }
    }
    
    /* With an optional <container-name> */
    @container tall (height > 30rem) {
      p {
        line-height: 1.6;
      }
    }
    
    /* With a <container-name> only (query is optional) */
    @container sidebar {
      h2 {
        background: blue;
      }
    }
    
    /* With a <scroll-state> */
    @container scroll-state(scrollable: top) {
      .back-to-top-link {
        visibility: visible;
      }
    }
    
    /* With an anchored query */
    @container anchored(fallback: bottom) {
      .infobox::before {
        content: "▲";
        bottom: 100%;
        top: auto;
      }
    }
    
    /* With a <container-name> and a <scroll-state> */
    @container sticky-heading scroll-state(stuck: top) {
      h2 {
        background: purple;
        color: white;
      }
    }
    
    /* Multiple queries in a single condition */
    @container (width > 400px) and style(--responsive: true) {
      h2 {
        font-size: 1.5em;
      }
    }
    
    /* Condition list */
    @container card (width > 400px), style(--responsive: true), scroll-state(stuck: top) {
      h2 {
        font-size: 1.5em;
      }
    }
    
    /* Boolean style() queries */
    @container style(--theme: one) or style(--theme: two) {
      /* matched container styles */
    }
    @container style((--theme: one) or (--theme: two)) {
      /* matched container styles */
    }
    @container style(--theme: one) and style(--theme: two) {
      /* matched container styles */
    }
    @container style((--theme: one) and (--theme: two)) {
      /* matched container styles */
    }
    @container not style(--theme: one) {
      /* matched container styles */
    }
    
    /* range style() queries */
    @container style(--number > 4) {
      /* matched container styles */
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#parameters)

[`<container-condition>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#container-condition)

One or both of `<container-name>` and `<container-query>`. Styles defined in the `<stylesheet>` are applied if the condition is `true`.

[`<container-name>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#container-name)

The name of the container to query; it is specified as an [`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
. If the query evaluates to `true`, the declared styles are applied to the container's descendant elements.

[`<container-query>` Optional](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#container-query)

A set of features that are evaluated against the query container when the size, [`<style-feature>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#container_style_queries)
, scroll-state, or applied position-try fallback of the container changes.

### [Logical keywords in container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#logical_keywords_in_container_queries)

Logical keywords can be used to define the container condition:

*   `and` combines two or more conditions.
*   `or` combines two or more conditions.
*   `not` negates the condition. Only one `not` condition is allowed per container query and it cannot be used with the `and` or `or` keywords.

css

    @container (width > 400px) and (height > 400px) {
      /* <stylesheet> */
    }
    
    @container (width > 400px) or (height > 400px) {
      /* <stylesheet> */
    }
    
    @container not (width < 400px) {
      /* <stylesheet> */
    }
    

### [Named containment contexts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#named_containment_contexts)

A containment context can be named using the [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
 property.

css

    .post {
      container-name: sidebar;
      container-type: inline-size;
    }
    

The shorthand syntax for this is to use [`container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container)
 in the form `container: <name> / <type>`, for example:

css

    .post {
      container: sidebar / inline-size;
    }
    

In container queries, the [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
 property is used to filter the set of containers to those with a matching query container name:

css

    @container sidebar (width > 400px) {
      /* <stylesheet> */
    }
    

Details about usage and naming restrictions are described in the [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
 page.

### [Descriptors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#descriptors)

The `<container-condition>` queries include [size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#size_container_descriptors)
, [scroll-state](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#scroll-state_container_descriptors)
, and [anchored](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#anchored_container_descriptors)
 container descriptors.

#### Size container descriptors

The `<container-condition>` can include one or more boolean size queries, each within a set of parentheses. A size query includes a size descriptor, a value, and — depending on the descriptor — a comparison operator. The queries always measure the [content box](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/box-edge#content-box)
 as the comparison. The syntax for including multiple conditions is the same as for [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 size feature queries.

css

    @container (min-width: 400px) {
      /* … */
    }
    @container (orientation: landscape) and (width > 400px) {
      /* … */
    }
    @container (15em <= block-size <= 30em) {
      /* … */
    }
    

[`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#aspect-ratio)

The [`aspect-ratio`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/aspect-ratio)
 of the container calculated as the width to the height of the container expressed as a [`<ratio>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ratio)
 value.

[`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#block-size)

The [`block-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/block-size)
 of the container expressed as a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value.

[`height`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#height)

The height of the container expressed as a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value.

[`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#inline-size)

The [`inline-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/inline-size)
 of the container expressed as a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value.

[`orientation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#orientation)

The [orientation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation)
 of the container, either `landscape` or `portrait`.

[`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#width)

The width of the container expressed as a [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 value.

#### Scroll-state container descriptors

Scroll-state container descriptors are specified inside the `<container-condition>` as an argument for the `scroll-state()` function, for example:

css

    @container scroll-state(scrollable: top) {
      /* … */
    }
    @container scroll-state(scrolled: block-end) {
      /* … */
    }
    @container scroll-state(stuck: inline-end) {
      /* … */
    }
    @container scroll-state(snapped: both) {
      /* … */
    }
    

Supported keywords for scroll-state container descriptors include [physical](https://developer.mozilla.org/en-US/docs/Glossary/Physical_properties)
 and [flow relative](https://developer.mozilla.org/en-US/docs/Glossary/Flow_relative_values)
 values.

[`scrollable`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#scrollable)

Queries whether the container can be scrolled in the given direction via user-initiated scrolling, such as by dragging the scrollbar or using a trackpad gesture. In other words, is there overflowing content in the given direction that can be scrolled to? Valid `scrollable` values include the following keywords:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#none)

The container is not a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 or otherwise cannot be scrolled in any direction.

[`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#top)

The container can be scrolled towards its top edge.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#right)

The container can be scrolled towards its right-hand edge.

[`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#bottom)

The container can be scrolled towards its bottom edge.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#left)

The container can be scrolled towards its left-hand edge.

[`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#x)

The container can be scrolled horizontally towards either or both of its left-hand or right-hand edges.

[`y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#y)

The container can be scrolled vertically towards either or both of its top or bottom edges.

[`block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#block-start)

The container can be scrolled towards its block-start edge.

[`block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#block-end)

The container can be scrolled towards its block-end edge.

[`inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#inline-start)

The container can be scrolled towards its inline-start edge.

[`inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#inline-end)

The container can be scrolled towards its inline-end edge.

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#block)

The container can be scrolled in its block direction towards either or both of its block-start or block-end edges.

[`inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#inline)

The container can be scrolled in its inline direction towards either or both of its inline-start and inline-end edges.

If the test passes, the rules inside the `@container` block are applied to descendants of the scroll container.

To evaluate whether a container is scrollable, without being concerned about the direction, use the `none` value with the `not` operator:

css

    @container not scroll-state(scrollable: none) {
      /* … */
    }
    

[`scrolled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#scrolled)

Queries whether the container was most recently scrolled in a specified direction. Valid `scrolled` values include the following keywords:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#none_2)

The container is not a [scroll container](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 or otherwise has not previously been scrolled in any direction.

[`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#top_2)

The container was most recently scrolled towards its top edge.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#right_2)

The container was most recently scrolled towards its right-hand edge.

[`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#bottom_2)

The container was most recently scrolled towards its bottom edge.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#left_2)

The container was most recently scrolled towards its left-hand edge.

[`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#x_2)

The container was most recently scrolled towards either its left-hand or right-hand edges.

[`y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#y_2)

The container was most recently scrolled towards either its top or bottom edges.

[`block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#block-start_2)

The container was most recently scrolled towards its block-start edge.

[`block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#block-end_2)

The container was most recently scrolled towards its block-end edge.

[`inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#inline-start_2)

The container was most recently scrolled towards its inline-start edge.

[`inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#inline-end_2)

The container was most recently scrolled towards its inline-end edge.

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#block_2)

The container was most recently scrolled towards either its block-start or block-end edges.

[`inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#inline_2)

The container was most recently scrolled towards either its inline-start or inline-end edges.

If the test returns true, the rules nested in the `@container` block are applied to the descendants of the scroll container.

To evaluate whether a container has recently been scrolled, without being concerned about the direction, use the `none` value with the `not` operator:

css

    @container not scroll-state(scrolled: none) {
      /* … */
    }
    

[`snapped`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#snapped)

Queries whether the container is going to be snapped to a [scroll snap](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll_snap)
 container ancestor along the given axis. Valid `snapped` values include the following keywords:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#none_3)

The container is not a scroll [snap target](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_snap#snap_target)
 for its ancestor scroll container. When implementing a `snapped: none` query, containers that _are_ snap targets for the scroll container will _not_ have the `@container` styles applied, whereas non-snap targets _will_ have the styles applied.

[`x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#x_3)

The container is a horizontal scroll snap target for its ancestor scroll container, that is, it is snapping horizontally to its ancestor.

[`y`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#y_3)

The container is a vertical scroll snap target for its ancestor scroll container, that is, it is snapping vertically to its ancestor.

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#block_3)

The container is a block-axis scroll snap target for its ancestor scroll container, that is, it is snapping to its ancestor in the block direction.

[`inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#inline_3)

The container is an inline-axis scroll snap target for its ancestor scroll container, that is, it is snapping to its ancestor in the inline direction.

[`both`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#both)

The container is both a horizontal and vertical scroll snap target for its ancestor scroll container and is snapping to its ancestor in both directions. The container won't match if it is only snapping to its ancestor along the horizontal _or_ vertical axis. It needs to be both.

To evaluate a container with a non-`none` `snapped` scroll-state query, it must be a container with a scroll container ancestor having a [`scroll-snap-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-snap-type)
 value other than `none`. A `snapped: none` query will match even when there is no scroll container ancestor.

Evaluations occur when [`scrollsnapchanging`](https://developer.mozilla.org/en-US/docs/Web/API/Element/scrollsnapchanging_event)
 events fire on the scroll snap container. If the test passes, the rules inside the `@container` block are applied to descendants of the container.

To evaluate whether a container is a snap target, without being concerned about the direction, use the `none` value with the `not` operator:

css

    @container not scroll-state(snapped: none) {
      /* … */
    }
    

[`stuck`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#stuck)

Queries whether a container with a [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 value of [`sticky`](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning#sticky_positioning)
 is stuck to an edge of its scrolling container ancestor. Valid `stuck` values include the following keywords:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#none_4)

The container is not stuck to any edges of its container. Note that `none` queries will match even if the container does not have `position: sticky` set on it.

[`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#top_3)

The container is stuck to the top edge of its container.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#right_3)

The container is stuck to the right-hand edge of its container.

[`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#bottom_3)

The container is stuck to the bottom edge of its container.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#left_3)

The container is stuck to the left-hand edge of its container.

[`block-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#block-start_3)

The container is stuck to the block-start edge of its container.

[`block-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#block-end_3)

The container is stuck to the block-end edge of its container.

[`inline-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#inline-start_3)

The container is stuck to the inline-start edge of its container.

[`inline-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#inline-end_3)

The container is stuck to the inline-end edge of its container.

To evaluate a container with a non-`none` `stuck` scroll-state query, it must have `position: sticky` set on it, and be inside a scroll container. If the test passes, the rules inside the `@container` block are applied to descendants of the `position: sticky` container.

It is possible for two values from adjacent axes to match at the same time:

css

    @container scroll-state((stuck: top) and (stuck: left)) {
      /* … */
    }
    

However, two values from opposite edges will never match at the same time:

css

    @container scroll-state((stuck: left) and (stuck: right)) {
      /* … */
    }
    

To evaluate whether a container is stuck, without being concerned about the direction, use the `none` value with the `not` operator:

css

    @container not scroll-state(stuck: none) {
      /* … */
    }
    

#### Anchored container descriptors

Anchored container descriptors are specified inside the `<container-condition>` as an argument for the `anchored()` function, for example:

css

    @container anchored(fallback: top) {
      /* … */
    }
    @container anchored(fallback: flip-block flip-inline) {
      /* … */
    }
    @container anchored(fallback: --custom-fallback) {
      /* … */
    }
    

[`fallback`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#fallback)

Queries whether a specific position-try fallback is currently active on an anchor-positioned container, as specified via the [`position-try-fallbacks`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-try-fallbacks)
 property. Valid `fallback` values include any component value that is valid for inclusion in a `position-try-fallbacks` property value.

If the `fallback` value named in the test is currently active on the anchor-positioned container, the test passes, and the rules inside the `@container` block are applied to descendants of the anchor-positioned container.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#formal_syntax)

--------------------------------------------------------------------------------------------------------------

@container =   
  @container <container-condition>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 { [<rule-list>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/rule-list)
 }    
  
<container-condition> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <container-name>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 <container-query>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
!    
  
<container-name> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
  
<container-query> =   
  not <query-in-parens>                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <query-in-parens> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 and <query-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 or <query-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
    
  
<query-in-parens> =   
  ( <container-query> )                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ( <size-feature> )                    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  style( <style-query> )                [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  scroll-state( <scroll-state-query> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <general-enclosed>                      
  
<style-query> =   
  not <style-in-parens>                               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-in-parens> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 and <style-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 or <style-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-feature>                                       
  
<scroll-state-query> =   
  not <scroll-state-in-parens>                        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <scroll-state-in-parens> [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 and <scroll-state-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 or <scroll-state-in-parens> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[\*](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#asterisk "Asterisk: the entity may occur zero, one or several times")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <scroll-state-feature>                                
  
<general-enclosed> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <function-token> <any-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 ( <any-value>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 ) [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
                   
  
<style-in-parens> =   
  ( <style-query> )    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ( <style-feature> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <general-enclosed>     
  
<style-feature> =   
  <style-feature-plain>    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-feature-boolean>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-range>              
  
<scroll-state-in-parens> =   
  ( <scroll-state-query> )    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ( <scroll-state-feature> )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <general-enclosed>            
  
<style-feature-plain> =   
  <style-feature-name> : <style-feature-value>    
  
<style-feature-boolean> =   
  <style-feature-name>    
  
<style-range> =   
  <style-range-value> <mf-comparison> <style-range-value>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-range-value> <mf-lt> <style-range-value> <mf-lt> <style-range-value>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-range-value> <mf-gt> <style-range-value> <mf-gt> <style-range-value>    
  
<style-range-value> =   
  <custom-property-name>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <style-feature-value>     
  
<mf-comparison> =   
  <mf-lt>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <mf-gt>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <mf-eq>    
  
<mf-lt> =   
  '<' '='[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<mf-gt> =   
  '>' '='[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
    
  
<mf-eq> =   
  '='    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#examples)

----------------------------------------------------------------------------------------------------

### [Setting styles based on a container's size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#setting_styles_based_on_a_containers_size)

Consider the following example of a card component with a title and some text:

html

    <div class="post">
      <div class="card">
        <h2>Card title</h2>
        <p>Card content</p>
      </div>
    </div>
    

A container context can be created using the `container-type` property, in this case using the `inline-size` value on the `.post` class. You can then use the `@container` at-rule to apply styles to the element with the `.card` class in a container that's narrower than `650px`.

    const post = document.querySelector(".post");
    const span = document.createElement("span");
    span.textContent = `.post width: ${post.clientWidth}px`;
    post.parentNode.insertBefore(span, post.nextSibling);
    // update on resize
    window.addEventListener("resize", () => {
      span.textContent = `.post width: ${post.clientWidth}px`;
    });
    

    span {
      display: block;
      text-align: center;
    }
    .card {
      margin: 10px;
      border: 2px dotted;
      font-size: 1.5em;
    }
    .post {
      border: 2px solid;
    }
    

css

    /* A container context based on inline size */
    .post {
      container-type: inline-size;
    }
    
    /* Apply styles if the container is narrower than 650px */
    @container (width < 650px) {
      .card {
        width: 50%;
        background-color: lightgray;
        font-size: 1em;
      }
    }
    

### [Creating named container contexts](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#creating_named_container_contexts)

Given the following HTML example which is a card component with a title and some text:

html

    <div class="post">
      <div class="card">
        <h2>Card title</h2>
        <p>Card content</p>
      </div>
    </div>
    

First, create a container context using the `container-type` and `container-name` properties. The shorthand syntax for this declaration is described in the [`container`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container)
 page.

css

    .post {
      container-type: inline-size;
      container-name: summary;
    }
    

Next, target that container by adding the name to the container query:

css

    @container summary (width >= 400px) {
      .card {
        font-size: 1.5em;
      }
    }
    

### [Nested container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#nested_container_queries)

It's not possible to target multiple containers in a single container query. It is possible to nest container queries which has the same effect.

The following query evaluates to true and applies the declared style if the container named `summary` is wider than `400px` and has an ancestor container wider than `800px`:

css

    @container summary (width > 400px) {
      @container (width > 800px) {
        /* <stylesheet> */
      }
    }
    

### [Container style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#container_style_queries)

Container queries can also evaluate the computed style of the container element. A _container style query_ is a `@container` query that uses one or more `style()` functional notations. The boolean syntax and logic combining style features into a style query is the same as for [CSS feature queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
.

css

    @container style(<style-feature>),
        not style(<style-feature>),
        style(<style-feature>) and style(<style-feature>),
        style(<style-feature>) or style(<style-feature>) {
      /* <stylesheet> */
    }
    

The parameter of each `style()` is a single `<style-feature>`. A **`<style-feature>`** can be a valid CSS [declaration](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/Introduction#css_declarations)
 (the **plain** form), a CSS property or [`<custom-property-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var#values)
 on its own (the **boolean** form), or a [range comparison](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#range_syntax)
 (the **range** form).

css

    @container style(--themeBackground),
        not style(background-color: red),
        style(color: green) and style(background-color: transparent),
        style(--themeColor: blue) or style(--themeColor: purple) {
      /* <stylesheet> */
    }
    

A style feature without a value evaluates to true if the computed value is different from the initial value for the given property.

If the `<style-feature>` passed as the `style()` function's argument is a declaration, the style query evaluates to true if the declaration's value is the same as the computed value of that property for the container being queried. Otherwise, it resolves to false.

The following container query checks if the [computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value)
 of the container element's `--accent-color` is `blue`:

css

    @container style(--accent-color: blue) {
      /* <stylesheet> */
    }
    

**Note:** If a custom property has a value of `blue`, the equivalent hexadecimal code `#0000ff` will not match unless the property has been defined as a color with [`@property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@property)
 so the browser can properly compare computed values.

Style features that query a shorthand property are true if the computed values match for each of its longhand properties, and false otherwise. For example, `@container style(border: 2px solid red)` will resolve to true if all 12 longhand properties (`border-bottom-style`, etc.) that make up that shorthand are true.

Note that [`!important`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/important)
 is allowed in style queries but is ignored.

css

    /* !important is valid but has no effect */
    @container style(--themeColor: purple !important) {
      /* <stylesheet> */
    }
    

The global `revert` and `revert-layer` are invalid as values in a `<style-feature>` and cause the container style query to be false.

#### Range syntax

In addition to the plain `<style-feature-name>: <value>` form described above, a `<style-feature>` can be written as a **range** comparison using `=`, `<`, `<=`, `>`, or `>=`. Range syntax enables **numeric** comparisons that the plain form can't, such as `style(--columns >= 3)` or `style(--gap = 1rem)`. It compares the resolved values of both sides numerically.

To evaluate a range, the browser:

1.  Resolves each side (custom property names are looked up as if used with [`var()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/var)
    ).
2.  Parses each side as a [`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    , [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    , [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
    , [`<angle>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/angle)
    , [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
    , [`<frequency>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/frequency)
    , or [`<resolution>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/resolution)
    . If either side can't be parsed as one of those types, or the two sides don't have the same type, the query is false.
3.  Computes each side (evaluating any `calc()` expressions) and performs the numeric comparison.

This means range syntax can't be used to compare keyword-like values: `style(--theme = dark)` is always false because `dark` isn't a numeric type. Use the plain syntax for those, for example `style(--theme: dark)`.

Either side of a range can be a custom property name, a `var()` reference, a literal value, or a `calc()` expression, in either order:

css

    @container style(3 = --n) {
      /* … */
    }
    @container style(var(--n) = 3) {
      /* … */
    }
    @container style(calc(6/2) = var(--n)) {
      /* … */
    }
    

A range can also take a three-value form, with both comparators pointing the same way, to test whether a value falls within an interval:

css

    @container style(0 < --n < 10) {
      /* true when --n is greater than 0 and less than 10 */
    }
    @container style(100px > --width > 50px) {
      /* true when --width is less than 100px and greater than 50px */
    }
    

In other words, `style(0 < --n < 10)` is equivalent to `style(0 < --n) and style(--n < 10)`. The middle value is tested against both bounds, rather than being chained left-to-right.

**Note:** Plain and range syntax behave differently even when they look similar. Given `--n: calc(6/2)`, the query `style(--n: 3)` is **false** because the plain form compares the property's computed value (`calc(6/2)`) directly against `3`. The equivalent range query `style(--n = 3)` is **true** because the range form computes both sides numerically before comparing. See [Plain versus range syntax in style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries#plain_versus_range_syntax_in_style_queries)
 in the container style queries guide for more details.

### [Scroll-state queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#scroll-state_queries)

See [Using container scroll-state queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Container_scroll-state_queries)
 for scroll-state query examples.

### [Anchored queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#anchored_queries)

See [Using anchored container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Anchored_container_queries)
 for anchored query examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Conditional Rules Module Level 5  <br>\# container-type](https://drafts.csswg.org/css-conditional-5/#container-type) |
| [CSS Anchor Positioning Module Level 2  <br>\# container-rule-anchored](https://drafts.csswg.org/css-anchor-position-2/#container-rule-anchored) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container#see_also)

----------------------------------------------------------------------------------------------------

*   [Using container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_queries)
    
*   [Using container size and style queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment/Container_size_and_style_queries)
    
*   [Using container scroll-state queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Container_scroll-state_queries)
    
*   [Using anchored container queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Anchored_container_queries)
    
*   [`container-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-name)
    
*   [`container-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/container-type)
    
*   [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/contain)
    
*   [`content-visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content-visibility)
    
*   [`CSSContainerRule`](https://developer.mozilla.org/en-US/docs/Web/API/CSSContainerRule)
     API
*   [CSS containment module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Containment)
    
*   [CSS at-rule functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@container/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@container/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@container (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40container&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40container%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40container%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40container%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fdc6f92b8877c1c53c187ad6cb6ba677db3ab179a%0A*+Document+last+modified%3A+2026-09-21T08%3A56%3A39.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")