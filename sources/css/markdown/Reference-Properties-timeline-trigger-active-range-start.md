*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#mdn-search)
    

timeline-trigger-active-range-start CSS property
================================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/961)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#browser_compatibility)
 carefully before using this in production.

The **`timeline-trigger-active-range-start`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the start of a [scroll-triggered animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
 trigger's active range.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#syntax)

---------------------------------------------------------------------------------------------------------------------------

css

    /* Keywords */
    timeline-trigger-active-range-start: auto;
    timeline-trigger-active-range-start: normal;
    
    /* <length-percentage> */
    timeline-trigger-active-range-start: 10%;
    timeline-trigger-active-range-start: 50px;
    
    /* Named timeline range */
    timeline-trigger-active-range-start: contain;
    timeline-trigger-active-range-start: exit;
    
    /* Named timeline with <length-percentage> */
    timeline-trigger-active-range-start: entry -5%;
    timeline-trigger-active-range-start: contain 100px;
    
    /* Multiple range start values */
    timeline-trigger-active-range-start:
      contain -10px,
      entry 5%;
    
    /* Global values */
    timeline-trigger-active-range-start: inherit;
    timeline-trigger-active-range-start: initial;
    timeline-trigger-active-range-start: revert;
    timeline-trigger-active-range-start: revert-layer;
    timeline-trigger-active-range-start: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#values)

This property is specified as a comma-separated list of the following values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#auto)

Specifies the value of the [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
 property. This is the default value.

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#normal)

Specifies the start, or `0%`, of the `normal` range. Equivalent to `cover 0%` for a [view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#view_progress_timelines)
 [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
, and `scroll 0%` for a [scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#scroll_progress_timelines)
.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies a length or percentage value measured from the beginning of the `normal` timeline. Percentages are relative to the length of the [`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#normal)
 timeline range.

[`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)

Specifies the start, or `0%`, of the `cover`, `contain`, `entry`, `exit`, `entry-crossing`, `exit-crossing`, or `scroll` timeline range.

[`<timeline-range-name>` `<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#timeline-range-name_2)

Specifies a length or percentage value measured from the beginning of the specified [named timeline range](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
. Percentages are relative to the length of the named range.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#description)

-------------------------------------------------------------------------------------------------------------------------------------

The `timeline-trigger-active-range-start` property can be used to explicitly set the start of a trigger's [active range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range#description)
 to a value equal to or preceding the [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
, which specifies the start of the trigger's activation range.

The _active range_ is the range in which a trigger remains activated once activation has occurred. Activation occurs when the tracked element enters the _activation range_, and deactivation occurs when it leaves the _active range_. By default, the active range starts where the activation range starts. This property creates a buffer zone and is used to prevent premature resetting when a user scrolls back and forth across the activation's starting point. Only when a tracked element moves out of the _active range_ does the trigger become inactive.

The default value of `timeline-trigger-active-range-start` is `auto`, which sets the value to the same named range and offset as the [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
. When specified as a timeline range, offset, or both, this property sets the start of the active range to a point that is independent of the `timeline-trigger-activation-range-start` value. If the range start position doesn't extend the activation range, it has no effect.

The value of `normal` sets the start of the active range to the start of the default named range, resolving to either [`cover 0%`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#cover)
 for a view progress timeline (the [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
 is set to a [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
 function) or [`scroll 0%`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#scroll)
 for a scroll progress timeline (the `timeline-trigger-source` is set to a [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
 function).

Other values of the `timeline-trigger-active-range-start` property can be used to set:

[An offset from the `normal` range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#an_offset_from_the_normal_range)

A `<length>` or `<percentage>` value specifies an offset from the beginning of the `normal` timeline of [`cover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#cover)
 or [`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#scroll)
. Negative values outset the start, resulting in a longer active range. Positive values inset the start of the active range, making it shorter.

[The start of a specific named range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#the_start_of_a_specific_named_range)

A `<timeline-range-name>` value specifies a `0%` offset along the named timeline range, which is either `cover`, `contain`, `entry`, `exit`, `entry-crossing`, `exit-crossing`, or `scroll`. See [Understanding timeline range names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
.

[An offset from a specific named range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#an_offset_from_a_specific_named_range)

When both a `<timeline-range-name>` and `<length>` or `<percentage>` value are specified, the start is offset by the distance specified from the start of the named range. Percentage values are relative to the range specified. See [Setting insets using percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_insets#setting_insets_using_percentages)
.

The `timeline-trigger-active-range-start` property, along with the [`timeline-trigger-active-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-end)
 property, can also be set using the [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
 shorthand, which in turn can be set using the [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
 shorthand.

### [Specifying multiple range start values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#specifying_multiple_range_start_values)

When you specify multiple comma-separated values in a single `timeline-trigger-active-range-start` declaration, they apply to the timeline triggers in the order in which they appear in the [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
 property. When the number of triggers and `timeline-trigger-active-range-start` property values do not match, they are applied in the same way as [multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
.

For example, if multiple `timeline-trigger-name` values are set, but only a single `timeline-trigger-active-range-start` value is set, the `timeline-trigger-active-range-start` will apply to all the `timeline-trigger-name`s. If two or more `timeline-trigger-active-range-start` values are set, they will cycle between the `timeline-trigger-name`s until every timeline trigger has a `timeline-trigger-active-range-start` value set.

Consider these declarations:

css

    timeline-trigger-name: --my-trigger, --my-other-trigger, --another-trigger;
    timeline-trigger-active-range-start:
      contain,
      entry 5%;
    

In this case, `--my-trigger` will use the `contain` range start and `--my-other-trigger` will use the `entry 5%` range start. As there are three names but only two range starts, the range starts are cycled, so the third trigger name, `--another-trigger`, will use the `contain` range start.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#formal_definition)

-------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | Relative to the specified named timeline range if specified, otherwise relative to the entire timeline |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | A list where each item may be 'normal', a length percentage, or a timeline range name and a length percentage |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#formal_syntax)

-----------------------------------------------------------------------------------------------------------------------------------------

timeline-trigger-active-range-start =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 normal [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<timeline-range-name>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)\
 <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#examples)

-------------------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#basic_usage)

This example demonstrates the effect of extending a trigger's active range. It compares two identical triggered animations, with the start of one animation trigger's active range outset using the `timeline-trigger-active-range-start` property.

#### HTML

The markup contains four [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements — two to animate and two to create a trigger on — plus some basic text content to cause the page to scroll. The text content is hidden for brevity.

html

    <div class="animated">I am animated</div>
    <div class="animated longer">I am animated longer</div>
    
    ...
    <section>
      <div class="trigger">I create the trigger</div>
      <div class="trigger longer">I create a longer trigger</div>
    </section>
    ...
    

    <div class="animated">I am animated</div>
    <div class="animated longer">I am animated longer</div>
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
    
    <section>
      <div class="trigger">I create the trigger</div>
      <div class="trigger longer">I create a longer trigger</div>
    </section>
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

The `.animated` elements' [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 is set to `fixed`, positioning them near the top-left of the scrollport to enable us to see when their animations start and stop.

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
    .animated.longer {
      left: 150px;
    }
    section {
      display: flex;
      gap: 20px;
    }
    

Next, we define the [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 for a `rotate` animation:

css

    @keyframes rotate {
      from {
        rotate: 0deg;
      }
    
      to {
        rotate: 360deg;
      }
    }
    

Using the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand, the `rotate` animation is applied to the `.animated` elements. Without an associated trigger, the elements would start animating when the page loads. The `animation-trigger` property makes it a triggered animation. The values reference a `timeline-trigger-name` of `--t` and `--longer-t`, respectively, and define the same two `<animation-action>` values — `play` and `pause` — which specify that the animations will play on activation and pause on deactivation.

css

    .animated {
      animation: rotate 3s infinite linear;
      animation-trigger: --t play pause;
    }
    .animated.longer {
      animation-trigger: --longer-t play pause;
    }
    

The `.trigger` element creates the `.animated` element's trigger via the following properties:

*   A [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
     with value `--t`, which is equal to the identifier referenced in the `.animated` element's `animation-trigger` property value, associating the two together.
*   A [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
     with value [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    , which sets the timeline trigger as a view progress timeline, and the element providing the timeline trigger as the nearest scrolling ancestor element.
*   A [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
     of `contain 50% contain 100%`. The `contain` range spans from when the trigger element has completely entered the scrollport to when it starts to leave. This value sets the trigger's activation range to start at `50%` through the `contain` range (when the tracked element's bottom edge is halfway through the scrollport), and end at `100%`, when the element's top edge first exits the scrollport.

The `.trigger.longer` element creates the `.animated.longer` element's trigger via the following properties:

*   A [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
     with value `--longer-t` (overriding the `--t`), which is equal to the identifier referenced in the `.animated.longer` element's `animation-trigger` property value, associating the two together.
    
*   A `timeline-trigger-active-range-start` of `contain 0%`, which occurs when the trigger's bottom edge is at the bottom edge of the scrollport.
    

css

    .trigger {
      timeline-trigger-name: --t;
      timeline-trigger-source: view();
      timeline-trigger-activation-range: contain 50% contain 100%;
    }
    .trigger.longer {
      timeline-trigger-name: --longer-t;
      timeline-trigger-active-range-start: contain 0%;
    }
    

    @supports not (timeline-trigger-active-range-start: contain 0%) {
      body::before {
        content: "Your browser does not support the timeline-trigger-active-range-start property.";
        background-color: wheat;
        text-align: center;
        padding: 1rem 0;
    
        z-index: 1;
        position: fixed;
        inset: 40% 0 auto;
      }
    }
    

#### Result

Try scrolling the content up. Both animations start playing when the tracked `.trigger` elements get to the middle of the scrollport and stop playing when they start to leave the top edge of the scrollport.

If you then scroll downward, both animations start playing when they are fully in the scrollport, with the top edge of the tracked elements meeting the top edge of the scrollport. The first animation pauses when the tracked element exits the activation range, when it passes the center of the scrollport. The second animation doesn't pause until its trigger element starts to leave the scrollport at its bottom edge. This is because the active range on the second animation extends how long the trigger remains active.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#specifications)

-------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Animation Triggers  <br>\# propdef-timeline-trigger-active-range-start](https://drafts.csswg.org/animation-triggers-1/#propdef-timeline-trigger-active-range-start) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start#see_also)

-------------------------------------------------------------------------------------------------------------------------------

*   [`timeline-trigger-active-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-end)
    
*   [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
     shorthand property
*   [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
    
*   [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
    , [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
    , and [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
    
*   [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
     shorthand property
*   [Using CSS scroll-triggered animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
    
*   [CSS animation triggers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/timeline-trigger-active-range-start/index.md?plain=1 "Folder: en-us/web/css/reference/properties/timeline-trigger-active-range-start (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-trigger-active-range-start&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-trigger-active-range-start%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-trigger-active-range-start%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-trigger-active-range-start%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")