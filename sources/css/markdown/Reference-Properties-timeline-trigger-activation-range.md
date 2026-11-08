*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#mdn-search)
    

timeline-trigger-activation-range CSS property
==============================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/961)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#browser_compatibility)
 carefully before using this in production.

The **`timeline-trigger-activation-range`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand property](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 specifies the start and end of a [scroll-triggered animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
 trigger's activation range.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#constituent_properties)

---------------------------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
    
*   [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#syntax)

-------------------------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#values)

This property is specified as a comma-separated list of animation ranges. Each animation range is specified as a [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
 value and, optionally, a [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
 value.

[`<'timeline-trigger-activation-range-start'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#timeline-trigger-activation-range-start)

The keyword `normal`, a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
, a [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
, or a `<timeline-range-name>` followed by a `<length-percentage>`, representing the [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
. If a `<timeline-range-name>` is set without a `<length-percentage>`, the `<length-percentage>` defaults to `0%`.

[`<'timeline-trigger-activation-range-end'>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#timeline-trigger-activation-range-end)

The keyword `normal`, a `<length-percentage>`, a `<timeline-range-name>`, or a `<timeline-range-name>` followed by a `<length-percentage>`, representing the [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
. If a `<timeline-range-name>` is set without a `<length-percentage>`, the `<length-percentage>` defaults to `100%`.

Percentages are relative to the length of the named timeline range if one is specified, or the timeline represented by `normal` if not.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#description)

-----------------------------------------------------------------------------------------------------------------------------------

The `timeline-trigger-activation-range` property can be used to explicitly specify the start or start and end of a trigger's activation range. The property sets both the [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
 and [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
 properties in one declaration, with each specified as a timeline range, offset, or both. Start and end offsets are both measured from the start of their ranges. If only the `timeline-trigger-activation-range-start` value is specified, the `timeline-trigger-activation-range-end` value defaults to `normal`, which is either `contain 100%` or `scroll 100%`, depending on the [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
 value.

A trigger's activation range is the range along the associated scrollport within which a [CSS scroll-triggered animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animation_triggers/Using_scroll-triggered_animations)
 trigger will activate. Activation occurs when the tracked element enters the _activation range_, and deactivation occurs when it leaves the _active range_.

The default value is `normal`, which sets the activation range to the default named range. The default named range depends on the [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
: it is equivalent to `cover` for a [view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#view_progress_timelines)
 and `scroll` for a [scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#scroll_progress_timelines)
. The default offset values are `0%` for activation start and `100%` for activation end. Therefore, `normal` resolves to either `cover 0% cover 100%` or `scroll 0% scroll 100%`.

Other `timeline-trigger-activation-range` values can be used to set:

[Start and end offsets from the `normal` range](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#start_and_end_offsets_from_the_normal_range)

A `<length>` or `<percentage>` value specifies an offset from the beginning of the `normal` timeline, which again defaults to [`cover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#cover)
 for a `view()` progress timeline source, and [`scroll`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name#scroll)
 for a `scroll()` progress timeline source. Negative values outset the start and end, resulting in a longer activation range. Positive values inset the start and end of the activation range, shortening it.

[Specific named ranges](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#specific_named_ranges)

If a `<timeline-range-name>` values is set without including an offset, the offset defaults to `0%` for start and `100%` for end values. The named timeline ranges include `cover`, `contain`, `entry`, `exit`, `entry-crossing`, `exit-crossing`, and `scroll`. See [Understanding timeline range names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
.

[Offsets from specific named ranges](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#offsets_from_specific_named_ranges)

When both a `<timeline-range-name>` and `<length>` or `<percentage>` value are specified for the start or end, the value is specified as a length or percentage offset from the start of the named range. Percentage values are relative to the full length of the named range specified. See [Setting insets using percentages](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_insets#setting_insets_using_percentages)
.

In each component of a `timeline-trigger-activation-range` value, the `<timeline-range-name>` value must come before the `<length>` or `<percentage>` offset. In the following example, you might think `timeline-trigger-activation-range-start` is set to `contain` and `timeline-trigger-activation-range-end` is set to `50%`, but that is not the case. Instead, `timeline-trigger-activation-range-start` is set to `contain 50%` while `timeline-trigger-activation-range-end` defaults to `normal`:

To set `timeline-trigger-activation-range-start` to `contain` and `timeline-trigger-activation-range-end` to `50%`, explicitly set `0%`, which is the default start offset:

By default, the active range is the same as the activation range. To make the active range longer than the activation range, use the [`timeline-trigger-active-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-start)
 and [`timeline-trigger-active-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range-end)
 properties, or the [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
 shorthand. Making the active range longer than the activation range is useful when you want to trigger an animation in a small activation range but keep the trigger active over a larger range.

The `timeline-trigger-activation-range` property, along with the [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
, [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
, and [`timeline-trigger-active-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-active-range)
 properties, can also be set using the [`timeline-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger)
 shorthand.

### [Explicit and default values for `timeline-trigger-activation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#explicit_and_default_values_for_timeline-trigger-activation-range)

In terms of explicit and default values, `timeline-trigger-activation-range` works in exactly the same way as the [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
 property. See the following for more information:

*   [Explicitly defining both range start and range end with two values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#explicitly_defining_both_range_start_and_range_end_with_two_values)
    
*   [Defining range start and defaulting range end](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#defining_range_start_and_defaulting_range_end)
    

### [Specifying multiple ranges](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#specifying_multiple_ranges)

When multiple values are specified in a comma-separated `timeline-trigger-activation-range` declaration, each value applies to a timeline trigger in the order in which the names appear in the [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
 property. When the number of triggers and `timeline-trigger-activation-range` property values do not match, they are applied in the same way as [multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
:

*   If the number of `timeline-trigger-activation-range` values exceeds the number of `timeline-trigger-name` values, the excess range values are discarded.
*   If the number of trigger names is greater than the number of ranges, the `timeline-trigger-activation-range` values are cycled until every `timeline-trigger-name` value has a `timeline-trigger-activation-range` value set.
*   If multiple `timeline-trigger-name` values are set, but only one `timeline-trigger-activation-range` value is set, the `timeline-trigger-activation-range` will apply to all the `timeline-trigger-name`s.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)<br>    : `normal`<br>*   [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)<br>    : `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | as each of the properties of the shorthand:  <br><br>*   [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)<br>    : Relative to the specified named timeline range if specified, otherwise relative to the entire timeline<br>*   [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)<br>    : Relative to the specified named timeline range if specified, otherwise relative to the entire timeline |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`timeline-trigger-activation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)<br>    : A list where each item may be 'normal', a length percentage, or a timeline range name and a length percentage<br>*   [`timeline-trigger-activation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)<br>    : A list where each item may be 'normal', a length percentage, or a timeline range name and a length percentage |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------------------

timeline-trigger-activation-range =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<'timeline-trigger-activation-range-start'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)\
 [<'timeline-trigger-activation-range-end'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<timeline-trigger-activation-range-start>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-start)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 normal [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<timeline-range-name>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)\
 <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<timeline-trigger-activation-range-end>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range-end)
 =   
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#examples)

-----------------------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#basic_usage)

In this example, we inset a scroll-triggered animation trigger's activation range by setting a custom `timeline-trigger-activation-range` value.

#### HTML

Our markup contains two [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements—one to animate and one to create a trigger on—and some text content to make the page scroll. We have hidden the text content for brevity.

#### CSS

The `.animated` element's [`position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position)
 is set to `fixed`, positioning it near the top-left of the scrollport so we can see when its animation starts and stops.

Next, we define the [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 for a `rotate` animation:

Using the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand, the `rotate` animation is applied to the `.animated` element. Without an associated trigger, the element would start animating when the page loads. The `animation-trigger` property makes it a triggered animation. The value references a `timeline-trigger-name` of `--t` and specifies two `<animation-action>` values — `play` and `pause` — which specify that the animation plays on activation and pauses on deactivation.

The `.trigger` element creates the `.animated` element's trigger via the following properties:

*   A [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
     with value `--t`, which is equal to the identifier referenced in the `.animated` element's `animation-trigger` property value, associating the two together.
*   A [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
     with value [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    , which sets the timeline trigger as a view progress timeline, and the element providing the timeline trigger as the nearest scrolling ancestor element.
*   A `timeline-trigger-activation-range` of `entry 50% exit 50%`. The `entry` range spans from when the trigger element first starts entering the scrollport to when it has completely entered the scrollport, while the `exit` range spans from when the trigger element first starts leaving the scrollport to when it has completely left the scrollport. This value sets the trigger's activation range to start at `50%` through the `entry` range and end `50%` through the `exit` range.

#### Result

Try scrolling the content up and down. The animation starts playing when `50%` of the tracked `.trigger` element has entered the scrollport in either direction and pauses when `50%` of the trigger element has exited the scrollport at either edge.

### [Comparing multiple range values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#comparing_multiple_range_values)

This example is identical to the previous example, except that it allows selecting different activation ranges to compare their effects.

The markup is the same as the previous example except we've added a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element that can be used to change the `timeline-trigger-activation-range` value. When a new value is selected, it is applied to the trigger element using JavaScript. We have hidden the HTML and JavaScript for brevity.

    <form>
      <label for="range-select">Select activation range</label>
      <select id="range-select">
        <optgroup label="Start value">
          <option>40%</option>
          <option>200px</option>
          <option>contain</option>
          <option selected>cover</option>
          <option>entry</option>
          <option>exit 50%</option>
          <option>contain 150px</option>
        </optgroup>
        <optgroup label="Start and end value">
          <option>20% 80%</option>
          <option>entry exit</option>
          <option>normal 20%</option>
          <option>20% normal</option>
          <option>contain contain 40%</option>
          <option>200px exit 300px</option>
          <option>entry 10% 90%</option>
          <option>entry 0% exit 50%</option>
          <option>contain 100px contain 90%</option>
        </optgroup>
      </select>
    </form>
    

    const selectElem = document.querySelector("select");
    const triggerElem = document.querySelector(".trigger");
    
    selectElem.addEventListener("change", () => {
      triggerElem.style.timelineTriggerActivationRange = selectElem.value;
    });
    

#### CSS

The CSS is the same as for the previous example, except we've omitted the `timeline-trigger-activation-range` value. This means that until a range value is selected, the range will default to `normal`, which is `cover 0% cover 100%` in this case.

    form {
      width: 250px;
      padding: 5px;
      border: 2px solid black;
      background: white;
      position: fixed;
      top: 0;
      right: 0;
    }
    
    label,
    select {
      font-size: 1rem;
    }
    
    select {
      padding: 5px;
      margin-top: 5px;
      width: 100%;
    }
    

css

    .animated {
      animation: rotate 3s infinite linear;
      animation-trigger: --t play pause;
    }
    
    .trigger {
      timeline-trigger-name: --t;
      timeline-trigger-source: view();
    }
    

#### Result

Select different range values then scroll the tracked element up and down the scrollport to see where the animated element starts and stops rotating.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#specifications)

-----------------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Animation Triggers  <br>\# propdef-timeline-trigger-activation-range](https://drafts.csswg.org/animation-triggers-1/#propdef-timeline-trigger-activation-range) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range#see_also)

-----------------------------------------------------------------------------------------------------------------------------

*   [`animation-trigger`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-trigger)
    
*   [`timeline-trigger-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-name)
    , [`timeline-trigger-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-source)
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

This page was last modified on Oct 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-trigger-activation-range/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/timeline-trigger-activation-range/index.md?plain=1 "Folder: en-us/web/css/reference/properties/timeline-trigger-activation-range (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-trigger-activation-range&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-trigger-activation-range%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftimeline-trigger-activation-range%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftimeline-trigger-activation-range%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1a2a5b56a689b441ebf3be91b90f15746c5a5a01%0A*+Document+last+modified%3A+2026-10-12T05%3A04%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")