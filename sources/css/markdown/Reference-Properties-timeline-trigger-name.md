*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#mdn-search)
    

timeline-trigger-name CSS property
==================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/961)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#browser_compatibility)
 carefully before using this in production.

The **`timeline-trigger-name`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies a [scroll-triggered animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
 trigger's identifier(s).

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Keyword */
    timeline-trigger-name: none;
    
    /* Single dashed ident */
    timeline-trigger-name: --my-trigger;
    timeline-trigger-name: --my-other-trigger;
    
    /* Multiple dashed idents */
    timeline-trigger-name: --my-trigger, --my-other-name;
    
    /* Global values */
    timeline-trigger-name: inherit;
    timeline-trigger-name: initial;
    timeline-trigger-name: revert;
    timeline-trigger-name: revert-layer;
    timeline-trigger-name: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#values)

Specified as one or more [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 values separated by commas, or the keyword `none`.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#none)

Specifies that the element does not define any scroll-triggered animation triggers.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)

Specifies the name of the timeline trigger.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#description)

-----------------------------------------------------------------------------------------------------------------------

The `timeline-trigger-name` property specifies one or more identifying names for a [CSS scroll-triggered animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
 trigger. This identifier is used within the [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
 property value.

For example:

css

    .trigger {
      timeline-trigger-name: --my-trigger;
      timeline-trigger-source: view();
    }
    

An element with these declarations set will create a trigger with the name `--my-trigger`. The `timeline-trigger-source` declaration is needed to create a timeline to control triggering animations; in this case, the value of `view()` creates an [anonymous view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_view_progress_timeline_the_view_function)
.

The resulting [`ViewTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/ViewTimeline)
 tracks the position of the `.trigger` element across the block-axis of the nearest ancestor scroller. The trigger is activated and deactivated when the tracked element is scrolled to specific positions inside the scrollport.

Any animated element with its [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
 property set to `--my-trigger` will have its animation controlled by the `--my-trigger` trigger:

css

    .animated {
      animation: rotate 3s infinite linear both;
      animation-trigger: --my-trigger play-once;
    }
    

Each `animation-trigger` value includes two or three components: the `<dashed-ident>` identifying the trigger, and one or two [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
 keywords specifying what should happen when the trigger is activated and, optionally, when it's deactivated. In this case, the animation will play once when activated.

The animated element can create its own trigger: to achieve this, set its `timeline-trigger-name` and `animation-trigger` properties to include the same `<dashed-ident>` value:

css

    .animatedAndTrigger {
      animation: rotate 3s infinite linear both;
      animation-trigger: --my-trigger play-once;
    
      timeline-trigger-name: --my-trigger;
      timeline-trigger-source: view();
    }
    

The `timeline-trigger-name` property, along with the [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
, [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
, and [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
 properties, can also be set using the [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
 shorthand property.

### [Multiple trigger names](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#multiple_trigger_names)

You can specify multiple, comma-separated `<dashed-ident>` values in the same trigger's `timeline-trigger-name` value, meaning that it can be referenced by multiple identifiers. This can be useful in a situation where you have multiple components dropped into a page that you want to trigger animations on, but which use predefined `animation-trigger` values that you can't edit.

You could use multiple `timeline-trigger-name` values to create a trigger for all the animations:

css

    .trigger {
      timeline-trigger-name: --animation-trigger-1, --animation-trigger-2;
      timeline-trigger-source: view();
    }
    

If you specify the same `<dashed-ident>` multiple times in the same `timeline-trigger-name` list, only the last instance will define a trigger. The preceding ones will have no effect.

If multiple elements define triggers with the same trigger name, the trigger defined by the last element in the source order is used, unless scoped. See [`trigger-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope)
 for more details.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

timeline-trigger-name =   
  none             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#examples)

-----------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#basic_usage)

This example shows how to create a basic scroll-triggered animation. We use the `timeline-trigger-name` property to name a trigger and reference that name within an animated element's `animation-trigger` property.

#### HTML

Our markup contains two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, one to animate and one on which to create a trigger, plus some basic text content to cause the page to scroll. We have hidden the text content for brevity.

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

The animated `<div>` element's [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 is set to `fixed`, positioning it near the top-left of the scrollport to enable us to see when its animation starts and stops.

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
 for the `rotate` animation we will use later:

css

    @keyframes rotate {
      from {
        rotate: 0deg;
      }
    
      to {
        rotate: 360deg;
      }
    }
    

Using the `animation` shorthand, we apply the `rotate` animation to the `.animated` element. Without an associated trigger, the element would start animating when the page loads. The `animation-trigger` property makes it a triggered animation. The value references a `timeline-trigger-name` of `--t` and specifies two `<animation-action>` values — `play` and `pause` — which specify that the animation will play on activation, and pause on deactivation.

css

    .animated {
      animation: rotate 3s infinite linear;
      animation-trigger: --t play pause;
    }
    

The `.trigger` element creates the `.animated` element's trigger via the following properties:

*   A `timeline-trigger-name` with value `--t`, which is equal to the identifier referenced in the animated element's `animation-trigger` property value, associating the two together.
*   A [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
     with value [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    , which sets the timeline trigger as a view progress timeline, and the element providing the timeline trigger as the nearest scrolling ancestor element.

css

    .trigger {
      timeline-trigger-name: --t;
      timeline-trigger-source: view();
    }
    

#### Result

Try scrolling the content up. When any part of the tracked `.trigger` element appears in the scrollport, the animation plays; when it has completely left the scrollport at either edge, the animation pauses.

### [Making the animated element the trigger](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#making_the_animated_element_the_trigger)

This example demonstrates how an animated element can create its own trigger.

#### HTML

This time, our markup contains a single [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element.

html

    <div>I create my own trigger</div>
    

The text content that causes the page to scroll has been hidden for brevity.

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

We define an `invert-colors` keyframe animation that inverts the foreground and background colors:

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
    

We set an `animation-trigger` value that references a `timeline-trigger-name` of `--t`. We also specify two `<animation-action>` values — `play-forwards` and `play-backwards` — which set the animation to play forwards on activation and in reverse on deactivation.

We then specify the following properties on the same `<div>`:

*   A `timeline-trigger-name` with value `--t`. This specifies that the `<div>` creates the trigger for its own animation.
*   A `timeline-trigger-source` with value [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    . This sets the timeline trigger as a view progress timeline, and the element providing the timeline trigger as the nearest scrolling ancestor element.
*   A [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
     with value [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#contain)
    . This means the trigger will activate when the tracked element is fully inside the scrollport. Because [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
     defaults to `auto`, the active range is the same as the activation range; therefore, the trigger will deactivate when it stops being fully inside the scrollport. This is in contrast to the default activation and active range, [`cover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#cover)
    , which would cause the trigger to activate when any part of the element enters the scrollport and deactivate only when it has fully left the scrollport. This would make the reverse animation occur when the element is out of view.

css

    div {
      animation: invert-colors 0.6s ease-in both;
    
      animation-trigger: --t play-forwards play-backwards;
    
      timeline-trigger-name: --t;
      timeline-trigger-source: view();
      timeline-trigger-activation-range: contain;
    }
    

    @supports not (timeline-trigger-name: --t) {
      body::before {
        content: "Your browser does not support the timeline-trigger-name property.";
        background-color: wheat;
        text-align: center;
        padding: 1rem 0;
    
        z-index: 1;
        position: fixed;
        inset: 40% 0 auto;
      }
    }
    

#### Result

Try scrolling the content up. The tracked element's animation plays after it has fully entered the scrollport, and pauses when it starts to leave the scrollport.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Animation Triggers  <br>\# propdef-timeline-trigger-name](https://drafts.csswg.org/animation-triggers-1/#propdef-timeline-trigger-name) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
    
*   [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
    , [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
    , and [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
    
*   [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
     shorthand property
*   [`trigger-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/trigger-scope)
    
*   [`<animation-action>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/animation-action)
     type
*   [Using CSS scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
    
*   [CSS animation triggers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/timeline-trigger-name/index.md?plain=1 "Folder: en-us/web/css/reference/properties/timeline-trigger-name (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-trigger-name&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-trigger-name%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-trigger-name%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-trigger-name%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")