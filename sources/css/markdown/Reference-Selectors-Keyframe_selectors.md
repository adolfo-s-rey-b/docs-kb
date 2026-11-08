*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#mdn-search)
    

Keyframe selectors
==================

CSS **keyframe selectors** identify specific points in an animation timeline where keyframe styles should be applied. These selectors are used exclusively within the [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 at-rule.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* Keywords */
    from {
    }
    to {
    }
    
    /* <percentage> values */
    0% {
    }
    50% {
    }
    100% {
    }
    
    /* With <timeline-range-name> */
    entry 20% {
    }
    exit 80% {
    }
    
    /* Selector lists */
    0%,
    50%,
    100% {
    }
    from,
    to {
    }
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#values)

[`from`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#from)

Represents the start of the animation sequence. It is equivalent to `0%`.

[`to`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#to)

Represents the end of the animation sequence. It is equivalent to `100%`.

[`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#percentage)

A [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
 between `0%` and `100%`, inclusive, representing the total progression through the animation sequence.

[`<timeline-range-name> <percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#timeline-range-name_percentage)

A [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
 preceding a `<percentage>` component represents a specific progress point within the named timeline range.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#description)

-------------------------------------------------------------------------------------------------------------------

A `<keyframe-selector>` can be the `to` or `from` keyword, a percentage between `0%` and `100%`, inclusive, or a comma-separated list of these keywords and/or percentages. When the percentage is preceded by a [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
, it defines a timeline range if the animation timeline is a view progress timeline; otherwise, the selector is ignored. When a comma-separated `<keyframe-selector>` list is used, the style block that follows applies to all the specified progression points.

### [Valid percentage values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#valid_percentage_values)

Percentage values must include the percent sign (`%`). Unitless values (such as `0` and `20`) and values outside the range `0%` to `100%` (such as `-10%` or `110%`) are invalid and will cause the keyframe block to be ignored.

### [Cascade, order, precedence, and importance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#cascade_order_precedence_and_importance)

Property values set by animation `@keyframes` are more important than all normal styles, meaning no matter the [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
, an animated value will override values that do not have an [`!important`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/important)
 flag set. Only important property values and values currently being transitioned take precedence over animated property values.

All keyframe selectors have the same specificity. The order of keyframe selectors within the selector list does not matter. The source order only matters if a duplicate keyframe selector declares a different value for an already declared property on the same selector.

The `!important` flag is not valid within an `@keyframes` definition.

### [Omitted start and end selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#omitted_start_and_end_selectors)

If no `0%` (or `from`) or `100%` (or `to`) keyframe is specified, the browser will use the element's computed styles for those states, allowing the animation to transition smoothly from or to the element's non-animated property values. In other words, if a property is specified in a middle-of-the-timeline keyframe without being set within a starting or ending keyframe selector block, the property will animate from its original value to that value.

For example, if an element has a `red` background color, and the following animation is applied:

css

    @keyframes changeToPurple {
      25%,
      75% {
        background-color: purple;
      }
    }
    

The background color will be `red` at the start of the animation, transitioning to `purple` a quarter of the way through the animation, remaining `purple` for half the animation, and transitioning back to `red`, the original background color, starting `75%` of the way through the [animation timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
. See the example that [omits the `to` and `from`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#omitting_to_and_from)
.

#### Omitted property declarations

When creating an `@keyframes` animation to animate multiple properties, you don't have to declare all the properties in all the keyframe selector blocks.

For example, in the [basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#basic_usage)
 example, the `opacity` is declared in all the keyframe selector blocks, but only start and end `transform` values are set. In that case, the element will be fully opaque `50%` of the way through the animation timeline, but the point at which the element is transformed `25vw` to the right depends on the [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
 — it will be `50%` in the case of `linear`, but not if `ease-in` is used (which it is in this case).

### [Cascade order](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#cascade_order)

If multiple keyframe blocks use the same `<keyframe-selector>`, they [cascade](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Introduction)
. This means that if the same property is defined in multiple blocks with the same selector, the last declaration in the rule takes precedence. If they define different properties, they are merged.

This animation repeats non-changing values in multiple selector blocks, which is not necessary:

css

    @keyframes uglyAnimation {
      0% {
        transform: translateX(0);
        opacity: 0;
        background-color: purple;
      }
      50% {
        transform: translateX(0);
        opacity: 1;
        background-color: purple;
      }
      75% {
        transform: translateX(0);
        opacity: 0;
        background-color: green;
      }
      100% {
        transform: translateX(50vw);
        opacity: 0;
        background-color: purple;
      }
    }
    

We can use the cascade to group values in one selector block, then override them as necessary. The following is equivalent to the previous animation, but with fewer lines of CSS:

css

    @keyframes uglyAnimation {
      0%,
      50%,
      75%,
      100% {
        transform: translateX(0);
        opacity: 0;
        background-color: purple;
      }
      50% {
        opacity: 1;
      }
      75% {
        background-color: green;
      }
      100% {
        transform: translateX(50vw);
      }
    }
    

Order is important! We can't ignore the cascade. If we reorder the above incorrectly, we lose the transitions. The following makes the element purple, fully opaque, and resets all the transforms during the entire time the animation is applied. The property values are applied and remain static because the last declaration overrides the declarations made in the previous keyframe selector blocks.

css

    @keyframes makeItPurpleOnly {
      0% {
        background-color: yellow;
      }
      50% {
        opacity: 0;
      }
      75% {
        background-color: green;
      }
      100% {
        transform: translateX(50vw);
      }
      0%,
      50%,
      75%,
      100% {
        transform: translateX(0);
        opacity: 1;
        background-color: purple;
      }
    }
    

### [With named timeline ranges](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#with_named_timeline_ranges)

Originally defined in the [CSS animation module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
, the [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
 module expanded the keyframe selector to enable view progress timeline range information to be included directly in the `@keyframes` animation definition. A [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
 can precede the `<percentage>` component of the selector to attach keyframes to specific progress points within the named timeline range. The `<timeline-range-name>` represents the selected predefined named timeline range, and the `<percentage>` after it represents the percentage progress between the start and end of that named timeline range.

css

    @keyframes in-and-out {
      entry 0% {
        opacity: 0;
        transform: translateX(100%);
      }
      entry 100% {
        opacity: 1;
        transform: translateX(0);
      }
      exit 0% {
        opacity: 1;
        transform: translateX(0);
      }
      exit 100% {
        opacity: 0;
        transform: translateX(-100%);
      }
    }
    

If the element's animation timeline does not have a corresponding named view timeline range, then any keyframes attached to points on that named timeline range are ignored. These attachment points may be outside the active interval of the animation. When this occurs, the automatic `from` (`0%`) and `to` (`100%`) keyframes are only generated for properties that don't have keyframes at or earlier than `0%` or at or after `100%`, respectively. See the [timeline range name guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
 for more information.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#examples)

-------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#basic_usage)

This example demonstrates using keywords and percentages by creating a keyframe animation that uses these keyframe selector types.

#### HTML

We include an element that we will animate.

html

    <div>I am animated</div>
    

#### CSS

We provide some basic styling to our box:

css

    div {
      background-color: rebeccapurple;
      color: white;
      width: min-content;
      padding: 10px;
      font: 2rem sans-serif;
    }
    

We create an [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 animation, applying styles to the `from` and `to` keywords and a middle percentage. We animate the [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 and the [`transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 properties.

css

    @keyframes slide-and-fade {
      from {
        transform: translateX(0);
        opacity: 0;
      }
      50% {
        opacity: 1;
      }
      to {
        transform: translateX(50vw);
        opacity: 0;
      }
    }
    

We apply our animation to the element using the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand property:

css

    div {
      animation: slide-and-fade 4s ease-in infinite;
    }
    

#### Results

### [Selector lists](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#selector_lists)

Using the same HTML and basic styling as in the previous example, this example demonstrates the use of comma-separated selectors to group keyframes, applying the same styles at multiple points in an animation.

    <div>I am animated</div>
    

#### CSS

We create a `pulse` animation that changes the size of our element.

css

    div {
      animation: pulse 4s linear infinite;
    }
    
    @keyframes pulse {
      0%,
      75% {
        transform: scale(1);
      }
      50% {
        transform: scale(1.2);
      }
      25%,
      100% {
        transform: scale(0.8);
      }
    }
    

    div {
      background-color: rebeccapurple;
      color: white;
      width: min-content;
      padding: 10px;
      font: 2rem sans-serif;
    }
    

#### Result

By using a selector list with multiple comma-separated keyframe selectors, the animation "pauses" from the `25%` keyframe until it reaches the `75%` keyframe.

### [Omitting `to` and `from`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#omitting_to_and_from)

This example demonstrates how, when the `to` or `from` keyframe selectors are not included in a `@keyframes` animation definition, the animated properties will animate to and from the original, non-animated property values.

#### HTML

We include a few elements. We will be animating all of them.

html

    <div>I am animated</div>
    <div>I am animated</div>
    <div>I am animated</div>
    

#### CSS

We provide basic styles to our elements, and give each one a different [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
 and [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
. We will animate these two properties.

css

    div {
      background-color: magenta;
      outline: 10px dashed black;
      color: white;
      width: min-content;
      padding: 10px;
      font: 2rem sans-serif;
      margin: 35px auto;
    
      animation: changes 5s linear infinite;
    }
    div:first-of-type {
      background-color: blue;
      outline-width: 0;
    }
    div:last-of-type {
      background-color: green;
      outline-width: 20px;
    }
    

We create an animation that sets an element's `background-color` and `outline-width` at `30%` and `40%` keyframes.

css

    @keyframes changes {
      30%, 40% {
        background-color: black;
        outline-width: 15px;
    }
    

#### Result

The `background-color` and `outline-width` properties are set in `30%` and `40%` keyframes. As a result, the elements' `background-color` values animate from `green`, `magenta`, and `blue` to `black` while their `outline-width` values animate from `0px`, `10px`, and `20px` to `15px`. They remain in that state for one-tenth of the animation — between `30%` and `40%` duration. After `40%` duration, these properties animate back to their initial values again.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#specifications)

-------------------------------------------------------------------------------------------------------------------------

This feature does not appear to be defined in any specification.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
    
*   [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    
*   [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
    
*   [Understanding timeline range names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
    
*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Mar 29, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/keyframe_selectors/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/keyframe_selectors (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FKeyframe_selectors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fkeyframe_selectors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FKeyframe_selectors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fkeyframe_selectors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff94b7a0b06a0e32df81ec8197720d306fe50a4a0%0A*+Document+last+modified%3A+2026-03-29T14%3A50%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")