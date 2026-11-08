*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#mdn-search)
    

timeline-trigger-activation-range-start CSS property
====================================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/961)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#browser_compatibility)
 carefully before using this in production.

The **`timeline-trigger-activation-range-start`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the start of a [scroll-triggered animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
 trigger's activation range.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#syntax)

-------------------------------------------------------------------------------------------------------------------------------

css

    /* Keyword */
    timeline-trigger-activation-range-start: normal;
    
    /* <length-percentage> */
    timeline-trigger-activation-range-start: 20%;
    timeline-trigger-activation-range-start: 350px;
    
    /* Named timeline range */
    timeline-trigger-activation-range-start: cover;
    timeline-trigger-activation-range-start: exit;
    
    /* Named timeline with <length-percentage> */
    timeline-trigger-activation-range-start: entry 40%;
    timeline-trigger-activation-range-start: contain -20px;
    
    /* Multiple range start values */
    timeline-trigger-activation-range-start:
      contain,
      entry -10%;
    
    /* Global values */
    timeline-trigger-activation-range-start: inherit;
    timeline-trigger-activation-range-start: initial;
    timeline-trigger-activation-range-start: revert;
    timeline-trigger-activation-range-start: revert-layer;
    timeline-trigger-activation-range-start: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#values)

This property is specified as a comma-separated list of the following values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#normal)

The default value. Equivalent to `cover 0%` for a [view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#view_progress_timelines)
 [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
, and `scroll 0%` for a [scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#scroll_progress_timelines)
.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies an offset as a `<length>` or `<percentage>`, measured from the beginning of the `normal` timeline. Percentages are relative to the length of the `normal` timeline range.

[`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)

Specifies the start (`0%`) of the `cover`, `contain`, `entry`, `exit`, `entry-crossing`, `exit-crossing`, or `scroll` timeline range.

[`<timeline-range-name>` `<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#timeline-range-name_2)

Specifies a length or percentage offset measured from the beginning of the specified [named timeline range](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
. Percentages are relative to the length of the named timeline.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#description)

-----------------------------------------------------------------------------------------------------------------------------------------

The `timeline-trigger-activation-range-start` property can be used to explicitly specify the start of a trigger's [activation range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#description)
. The value is specified as a timeline range, offset, or both.

A trigger's activation range is the range along the associated scrollport within which a [CSS scroll-triggered animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
 trigger will activate. Activation occurs when the tracked element enters the _activation range_, and deactivation occurs when it leaves the _active range_.

The `normal` value sets the start of the activation range to the start of the default named range. This is equivalent to `cover 0%` for a [view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#view_progress_timelines)
 and `scroll 0%` for a [scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#scroll_progress_timelines)
.

Other `timeline-trigger-activation-range-start` property can be used to set:

[An offset from the `normal` range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#an_offset_from_the_normal_range)

A `<length>` or `<percentage>` value specifies an offset from the beginning of the `normal` timeline, which again defaults to `cover 0%` for a view progress timeline source, and `scroll 0%` for a scroll progress timeline source. Negative values outset the start, resulting in a longer activation range. Positive values inset the start, making the activation range shorter.

[The start of a specific named range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#the_start_of_a_specific_named_range)

A `<timeline-range-name>` value specifies a `0%` offset along the named timeline range, which is either `cover`, `contain`, `entry`, `exit`, `entry-crossing`, `exit-crossing`, or `scroll`. See [Understanding timeline range names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
.

[An offset from a specific named range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#an_offset_from_a_specific_named_range)

When both a `<timeline-range-name>` and `<length>` or `<percentage>` value are specified, the start is the beginning of the named range offset by the distance specified. Percentage values are relative to the length of the range specified. See [Setting insets using percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_insets#setting_insets_using_percentages)
.

The `timeline-trigger-activation-range-start` property, along with the [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
 property, can also be set using the [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
 shorthand, which in turn can be set using the [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
 shorthand.

### [Specifying multiple range start values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#specifying_multiple_range_start_values)

When multiple values are specified in a comma-separated `timeline-trigger-activation-range-start` declaration, each value applies to a timeline trigger in the order in which the names appear in the [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
 property. When the number of triggers and `timeline-trigger-activation-range-start` property values do not match, they are applied in the same way as [multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
:

*   If the number of `timeline-trigger-activation-range-start` values exceeds the number of `timeline-trigger-name` values, the excess range values are discarded.
*   If the number of trigger names is greater than the number of ranges, the `timeline-trigger-activation-range-start` values are cycled until every `timeline-trigger-name` value has a `timeline-trigger-activation-range-start` value set.
*   If multiple `timeline-trigger-name` values are set, but only one `timeline-trigger-activation-range-start` value is set, that `timeline-trigger-activation-range-start` value will apply to all the `timeline-trigger-name`s.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | Relative to the specified named timeline range if specified, otherwise relative to the entire timeline |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | A list where each item may be 'normal', a length percentage, or a timeline range name and a length percentage |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------------------------

timeline-trigger-activation-range-start =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#examples)

-----------------------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#basic_usage)

In this example, we inset the start of a scroll-triggered animation trigger's activation range by setting a custom `timeline-trigger-activation-range-start` value.

#### HTML

Our markup contains two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements — one to animate and one to create a trigger on — plus some basic text content to cause the page to scroll. We have hidden the text content for brevity.

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
 shorthand, the `rotate` animation is applied to the `.animated` element. Without an associated trigger, the element would start animating when the page loads. The `animation-trigger` property makes it a triggered animation. The value references a `timeline-trigger-name` of `--t` and specifies two `<animation-action>` values — `play` and `pause` — which specify that the animation will play on activation and pause on deactivation.

css

    .animated {
      animation: rotate 3s infinite linear;
      animation-trigger: --t play pause;
    }
    

The `.trigger` element creates the `.animated` element's trigger via the following properties:

*   A [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
     with value `--t`, which is equal to the identifier referenced in the `.animated` element's `animation-trigger` property value, associating the two together.
*   A [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
     with value [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    , which sets the timeline trigger as a view progress timeline, and the element providing the timeline trigger as the nearest scrolling ancestor element.
*   A `timeline-trigger-activation-range-start` of `entry 50%`. The `entry` range spans from when the trigger element first starts entering the scrollport to when it has completely entered the scrollport. This value sets the trigger's activation range's start to `50%` through the `entry` range, which occurs when `50%` of the tracked `.trigger` element has entered the scrollport via the scrollport's end edge.

css

    .trigger {
      timeline-trigger-name: --t;
      timeline-trigger-source: view();
      timeline-trigger-activation-range-start: entry 50%;
    }
    

When not explicitly set, the [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
 value defaults to `normal`, which in this case is `cover 100%`. The [`timeline-trigger-active-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-end)
 value defaults to `auto` — the same as `timeline-trigger-activation-range-end`. This means that deactivation occurs at the end of the `cover` range, when the tracked element exits the scrollport's start edge.

    @supports not (timeline-trigger-activation-range-start: entry 50%) {
      body::before {
        content: "Your browser does not support the timeline-trigger-activation-range-start property.";
        background-color: wheat;
        text-align: center;
        padding: 1rem 0;
    
        z-index: 1;
        position: fixed;
        inset: 40% 0 auto;
      }
    }
    

#### Result

Try scrolling the content up. The animation starts playing when `50%` of the tracked `.trigger` element has entered the scrollport end edge and pauses when it has completely exited the scrollport at the opposite edge. When you scroll down, the effect reverses — the animation restarts playing when the trigger element starts to enter the top of the scrollport, and pauses again when `50%` of the trigger element has exited the bottom.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#specifications)

-----------------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Animation Triggers  <br>\# propdef-timeline-trigger-activation-range-start](https://drafts.csswg.org/animation-triggers-1/#propdef-timeline-trigger-activation-range-start) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start#see_also)

-----------------------------------------------------------------------------------------------------------------------------------

*   [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
    
*   [`timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range)
     shorthand property
*   [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
    , [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
    , and [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
    
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

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/timeline-trigger-activation-range-start/index.md?plain=1 "Folder: en-us/web/css/reference/properties/timeline-trigger-activation-range-start (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-trigger-activation-range-start&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-trigger-activation-range-start%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-trigger-activation-range-start%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-trigger-activation-range-start%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")