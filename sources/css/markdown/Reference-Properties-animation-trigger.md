*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#mdn-search)
    

animation-trigger CSS property
==============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/961)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#browser_compatibility)
 carefully before using this in production.

The **`animation-trigger`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies whether [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
 declared on an element are triggered animations (or not) and, if so, what their triggers are and how they should behave when the trigger becomes active or inactive. This is used to create [scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#syntax)

---------------------------------------------------------------------------------------------------------

css

    /* Keywords */
    animation-trigger: none;
    
    /* One trigger */
    animation-trigger: --my-trigger play;
    animation-trigger: --my-other-trigger play-once;
    animation-trigger: --my-trigger play-forwards play-backwards;
    animation-trigger: --my-other-trigger play reset;
    
    /* Multiple values */
    animation-trigger:
      none,
      -forwards play-backwards,
      --my-other-trigger play reset;
    
    /* Global values */
    animation-trigger: inherit;
    animation-trigger: initial;
    animation-trigger: revert;
    animation-trigger: revert-layer;
    animation-trigger: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#values)

Specified as a comma-separated list of values. Each value is either the keyword `none` or a [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 followed by one or two [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
 values.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#none)

The associated animation is not a triggered animation.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

A custom identifier defining the name of the trigger that will trigger the animation.

[`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)

An `<animation-action>`: The keywords `none`, `play`, `play-forwards`, `play-backwards`, `play-once`, `pause`, `replay`, or `reset`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#description)

-------------------------------------------------------------------------------------------------------------------

The `animation-trigger` property specifies which trigger will control an animated element's animations. A value other than `none` turns the animation into a [scroll-triggered animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
.

### [Defining a trigger](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#defining_a_trigger)

The trigger is identified via a `<dashed-ident>` value, which is defined in the tracked element's [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
 property.

For example:

css

    .animated {
      animation: rotate 3s infinite linear both;
      animation-trigger: --my-trigger play;
    }
    

In this case, the animation will play when an element with a `timeline-trigger-name` of `--my-trigger` enters the activation range defined on the trigger.

Here we create a trigger by setting the `timeline-trigger-name` using the [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
 shorthand property. The `.trigger` can be any element, including the `.animated` element.

css

    .trigger {
      timeline-trigger: --my-trigger view();
    }
    

If an element has an animation _and_ an `animation-trigger` set on it, but no scrolling element exists with the same `<dashed-ident>` set as its `timeline-trigger-name` value, the animation will not have a trigger and therefore will never play.

### [Defining the triggered animation actions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#defining_the_triggered_animation_actions)

The `animation-trigger` value must include one or two [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
 keywords after the `<dashed-ident>` to specify the animation behavior when the trigger is activated and deactivated. If two `<animation-action>`s are specified, the first is the activation action and the second is the deactivation action. If only one `<animation-action>` is set, this is the activation action, and nothing happens on deactivation.

For example:

css

    .animated {
      animation: rotate 3s infinite linear both;
      animation-trigger: --my-trigger play-forwards play-backwards;
    }
    

When the trigger is activated, the animation will `play-forwards`. When the trigger is deactivated, the animation will `play-backwards`.

There are eight `<animation-action>` values, each providing different animation behaviors.

Setting `play-forwards play-backwards` is a common pattern, often used to "animate in" an element when its trigger becomes active, for example by scrolling it into view, and then "animate out" the element again when the trigger becomes inactive, for example by scrolling it out of view.

The `play-once` action is generally used on its own or as part of `play-once pause`; setting `play-once` as the activation action causes the animation to play only once when it scrolls into view. Adding `pause` on deactivation pauses the animation when the trigger scrolls out of its active range; if the trigger is re-activated, the animation will restart from where it was paused.

See the [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
 data type for examples and more about each keyword value.

### [Triggering one animation via multiple triggers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#triggering_one_animation_via_multiple_triggers)

If you want to define triggers on multiple elements that all trigger the same animation on an element, you need to specify the animation multiple times on that animated element, giving each `animation` instance a different trigger.

For example:

css

    .animated {
      animation:
        spinOnce 2s 1 ease-out,
        spinOnce 2s 1 ease-out;
      animation-trigger:
        --t1 play-forwards play-backwards,
        --t2 play-forwards play-backwards;
    }
    
    .trigger1 {
      timeline-trigger: --t1 view();
    }
    
    .trigger2 {
      timeline-trigger: --t2 view();
    }
    

See [Multiple triggers for the same animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#multiple_triggers_for_the_same_animation)
 for a working example.

### [Reset by the `animation` shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#reset_by_the_animation_shorthand)

The `animation-trigger` property is a reset-only sub-property of the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand property. This means trigger names and animation actions can not be included in the `animation` shorthand, but setting the `animation` shorthand resets `animation-trigger` to its initial value of `none`. For this reason, you should always set `animation-trigger` after a corresponding `animation` property in a declaration list or declare the `animation-trigger` in a declaration block with selectors with stronger [`specificity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
.

### [Multiple `animation-trigger` values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#multiple_animation-trigger_values)

Setting multiple `animation-trigger` values works in the same way as setting [multiple values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
 for the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand property and the other animation longhand properties:

*   If multiple `animation-name` values are set, but only a single `animation-trigger` value is set, the `animation-trigger` will apply to all the animations.
*   If two or more comma-separated `animation-trigger` values are set, they will cycle between the animations until all of them have an `animation-trigger` value set. See an example of [declaring multiple scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations#multiple_scroll-triggered_animations)
    .

Given the following CSS:

css

    .animated {
      animation:
        fade-in linear 1s forwards,
        rotate infinite 5s both,
        shrink ease-in 3s forwards,
        color-change steps(5) 5s forwards;
    
      animation-trigger:
        --t1 play pause,
        --t2 forwards backwards;
    }
    .trigger1 {
      timeline-trigger: --t1 view();
    }
    .trigger2 {
      timeline-trigger: --t2 view();
    }
    

With `animation-trigger: --t1 play pause, --t2 forwards backwards` set on the animated element, `--t1` triggers the `fade-in` and `shrink` animations while `--t2` triggers the `rotate` and `color-change` animations.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------

animation-trigger =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)\
 [<animation-action>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)\
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#examples)

-------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#basic_usage)

This example demonstrates how to create a scroll-triggered animation that plays when activated and pauses when deactivated.

#### HTML

The markup contains two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, one to animate and one to create a trigger, plus some basic text content to make the page scrollable. The text is hidden for brevity.

html

    <div class="animated">I am animated</div>
    
    ...
    
    <div class="trigger">I create the trigger</div>
    
    ...
    

    <div class="animated">I am animated</div>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <div class="trigger">I create the trigger</div>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    

#### CSS

The `.animated` element's [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 is set to `fixed`, positioning it near the top-left of the scrollport to allow us to see the animation play and pause.

    body {
      width: 80%;
      margin: 0 auto;
      font-family: "Helvetica", "Arial";
      font-size: 1.3rem;
    }
    
    div {
      height: 100px;
      border: 5px solid black;
    }
    
    .animated {
      width: 100px;
      background: orange;
    }
    
    .trigger {
      background: wheat;
    }
    

css

    .animated {
      position: fixed;
      top: 25px;
      left: 25px;
    }
    

Next, we define the [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 for the `rotate` animation:

css

    @keyframes rotate {
      from {
        rotate: 0deg;
      }
    
      to {
        rotate: 360deg;
      }
    }
    

Using the `animation` shorthand, the `rotate` animation is applied to the `.animated` element. Without an associated trigger, the animation would start when the page loads. The `animation-trigger` property makes it a triggered animation. The value references a `timeline-trigger-name` of `--t` and specifies two `<animation-action>` values — `play` and `pause` — which specify that the animation will play on activation and pause on deactivation.

css

    .animated {
      animation: rotate 3s infinite linear both;
      animation-trigger: --t play pause;
    }
    

We set a `timeline-trigger-name` of `--t` on the `.trigger` element. As this value is the identifier referenced in the `.animated` declaration block's `animation-trigger` property value, this associates the two together, creating the animated element's trigger. We also include a [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
 value of [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
, which sets the timeline trigger as a [view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#view_progress_timelines)
 and both the active and activation ranges as the full `cover` timeline. We could have declared both together as `timeline-trigger: view() --t`.

css

    .trigger {
      timeline-trigger-name: --t;
      timeline-trigger-source: view();
    }
    

#### Result

Try scrolling the content up and down. When any part of the `.trigger` element appears in the scrollport, the animation plays; when it has completely left the scrollport at either edge, the animation pauses.

### [Making the animated element create the trigger](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#making_the_animated_element_create_the_trigger)

In this example, we demonstrate how an animated element can also create its own trigger.

#### HTML

This time, the markup contains only a single [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element, plus basic text content to cause the page to scroll. We have hidden the content markup for brevity.

html

    <div>I create my own trigger</div>
    

    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <div>I create my own trigger</div>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    

#### CSS

We create an `@keyframes` block that inverts the background and foreground colors:

    body {
      width: 80%;
      margin: 0 auto;
      font-family: "Helvetica", "Arial";
      font-size: 1.3rem;
    }
    
    div {
      height: 100px;
      background: orange;
      border: 5px solid black;
    }
    

css

    @keyframes invert-colors {
      from {
        background: orange;
        color: black;
      }
    
      to {
        background: black;
        color: orange;
      }
    }
    

We set the `animation` on the [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element, inverting the colors smoothly over 600ms. We also set an `animation-trigger` value that references a `timeline-trigger-name` of `--t` and include two `<animation-action>` values — `play-forwards` and `play-backwards` — which specify that the animation will play forwards on activation and play in reverse on deactivation.

We also specify a `timeline-trigger` value of `--t view() contain` on the `<div>`, so it creates the trigger for its own animation. The `timeline-trigger` shorthand includes three longhand property values:

*   A [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
     value: A `<dashed-ident>` identifier referenced in the `animation-trigger` property.
*   A [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
     value: The [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
     value sets the timeline trigger to a view progress timeline tracking the element inside its nearest scrolling ancestor element.
*   A [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
     value: The [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
     value of [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#contain)
     sets the trigger to activate when the `<div>` is fully inside the scrollport. Because we didn't set a value for the [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
     component, the active range is the same as the activation range, so it deactivates when it starts to exit the scrollport.

css

    div {
      animation: invert-colors 0.6s ease-in both;
      animation-trigger: --t play-forwards play-backwards;
      timeline-trigger: --t view() contain;
    }
    

#### Result

Try scrolling the content up. When the `<div>` is fully in the scrollport, its animation plays. When any part leaves the scrollport at either edge, the animation plays backward.

### [Multiple triggers for the same animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#multiple_triggers_for_the_same_animation)

This example shows how to assign multiple triggers to control the same animation. This example is similar to the [basic usage example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#basic_usage)
, but with multiple triggers triggering the same keyframe animation.

#### HTML

We include three `<div>` elements as triggers. The text content is hidden for brevity.

html

    <div class="animated">I am animated</div>
    
    ...
    
    <div class="trigger1">I create a trigger</div>
    
    ...
    
    <div class="trigger2">I create another trigger</div>
    
    ...
    
    <div class="trigger3">I create yet another trigger</div>
    
    ...
    

    <div class="animated">I am animated</div>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <div class="trigger1">I create a trigger</div>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <div class="trigger2">I create another trigger</div>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    
    <div class="trigger3">I create yet another trigger</div>
    
    <p>
      Fusce dictum ex quis ipsum consectetur placerat. Cras sed lectus ex. Quisque
      purus dolor, vulputate ac mi eget, commodo varius odio. Suspendisse faucibus
      ipsum vel libero finibus, in placerat nibh congue. Sed iaculis, metus et
      euismod posuere, mi diam vestibulum felis, ac vulputate eros ipsum id justo.
      Etiam a tincidunt purus. Maecenas semper sed enim at blandit. Aenean ut
      sagittis lorem, eget gravida purus. Phasellus eleifend, lectus nec pulvinar
      facilisis, dui dolor feugiat odio, iaculis tempor felis est non tortor. In
      suscipit lorem efficitur molestie tempus. Integer sit amet neque et risus
      iaculis sodales sed eget diam. Quisque sodales nunc sapien, vitae lacinia ex
      luctus quis. Maecenas scelerisque scelerisque elit eu consequat. Etiam ac
      tristique tellus, sed tincidunt velit.
    </p>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#css_3)

    body {
      width: 80%;
      margin: 0 auto;
      font-family: "Helvetica", "Arial";
      font-size: 1.3rem;
    }
    
    div {
      height: 100px;
      border: 5px solid black;
    }
    
    .animated {
      width: 100px;
      background: orange;
    }
    
    .trigger1,
    .trigger2,
    .trigger3 {
      background: palegoldenrod;
    }
    

The `animation` shorthand property value is a comma-separated list of animations, applying the same `animation-name` — `rotate` — three times. The `animation-trigger` value is a comma-separated list with three animation triggers, one for each animation instance.

css

    .animated {
      animation:
        rotate 3s infinite linear both,
        rotate 3s infinite linear forwards,
        rotate 3s infinite linear forwards;
      animation-trigger:
        --t1 play-forwards play-backwards,
        --t2 play-forwards play-backwards,
        --t3 play-forwards play-backwards;
    }
    

We define a timeline trigger with a different name on each trigger `<div>` element. These names correspond to the names referenced in the `.animated` element's `animation-trigger` property.

css

    .trigger1 {
      timeline-trigger: --t1 view();
    }
    
    .trigger2 {
      timeline-trigger: --t2 view();
    }
    
    .trigger3 {
      timeline-trigger: --t3 view();
    }
    

    @supports not (animation-trigger: --t play-forwards play-backwards) {
      body::before {
        content: "Your browser does not support the animation-trigger property.";
        background-color: wheat;
        text-align: center;
        padding: 1rem 0;
    
        z-index: 1;
        position: fixed;
        inset: 40% 0 auto;
      }
    }
    

#### Result

Try scrolling the content up and down, and note how the animation activates and then deactivates when each trigger element scrolls into and out of view.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Animation Triggers  <br>\# propdef-animation-trigger](https://drafts.csswg.org/animation-triggers-1/#propdef-animation-trigger) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
     type
*   [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
    , [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
    , [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
    , and [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
    
*   [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
     shorthand
*   [`trigger-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope)
    
*   [Using CSS scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
    
*   [CSS animation triggers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-trigger/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-trigger (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-trigger&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-trigger%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-trigger%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-trigger%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")