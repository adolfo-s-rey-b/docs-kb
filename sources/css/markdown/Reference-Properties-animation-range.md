*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#mdn-search)
    

`animation-range` CSS property
==============================

Baseline 2026

Newly available

Since October 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation-range`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property is used to set the start and end of an animation's attachment range along its timeline, i.e., where along the timeline an animation will start and end.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#constituent_properties)

---------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
    
*   [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Range start value only*/
    /* Single value syntax */
    animation-range: normal;
    animation-range: 20%;
    animation-range: 100px;
    animation-range: cover;
    animation-range: contain;
    /* Two value syntax */
    animation-range: cover 20%;
    animation-range: contain 100px;
    
    /* Range start and end values */
    /* Two value syntax */
    animation-range: normal 25%;
    animation-range: 25% normal;
    animation-range: 25% 50%;
    animation-range: entry exit;
    /* Three value syntax */
    animation-range: cover cover 200px;
    animation-range: 10% exit 90%;
    animation-range: entry 10% 90%;
    /* Four value syntax */
    animation-range: cover 0% cover 200px;
    animation-range: entry 10% exit 100%;
    
    /* Global values */
    animation-range: inherit;
    animation-range: initial;
    animation-range: revert;
    animation-range: revert-layer;
    animation-range: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#values)

The `animation-range` shorthand property is specified as one or more single animation ranges, separated by commas. Each animation range is specified as one to four space separated values composed of `<timeline-range-name>` values, `<length-percentage>` values, and/or the keyword `normal`.

[`<animation-range-start>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#animation-range-start)

The keyword `normal`, a `<length-percentage>`, a [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
, or a `<timeline-range-name> <length-percentage>` pair, representing the [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
. If a `<timeline-range-name>` is set without a `<length-percentage>`, the `<length-percentage>` defaults to `0%`.

[`<animation-range-end>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#animation-range-end)

The keyword `normal`, a `<length-percentage>`, a `<timeline-range-name>`, or a `<timeline-range-name> <length-percentage>` pair, representing the [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
. If a `<timeline-range-name>` is set without a `<length-percentage>`, the `<length-percentage>` defaults to `100%`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#description)

-----------------------------------------------------------------------------------------------------------------

The `animation-range` shorthand property sets the `animation-range-start` and `animation-range-end` values, defining where along the animation timeline the animation will start and end. By default, the styles defined in a keyframe animation are only applied to an element while that element is being animated. When a keyframe animation is applied to an element depends on the animation timeline of that animation. By default, animations are only applied between the timeline's range start and range end. To apply the animation outside of this range, set the [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
 to `backwards`, `forwards`, or `both`. These three `animation-fill-mode` values apply the first keyframe styles until range start, the last keyframe styles after the animation ends, or both before and after, respectively.

The [scroll port](https://developer.mozilla.org/en-US/docs/Glossary/Scroll_container)
 area known as the view progress visibility range is the area inside which the subject element of a [named view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#view_progress_timelines)
 animation is deemed to be visible. By default, this is the full range of the scrollport, but it can be adjusted using the [`view-timeline-inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
 property.

If two values are specified as components of the `<animation-range>` property, they will be interpreted in the order `<animation-range-start>` then `<animation-range-end>`. The value of each component is either the keyword `normal`, a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
, or a [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
 optionally followed by a `<length-percentage>`. These values are space-separated. Normal is equal to `0%` for start and `100%` for end. Setting `normal` with a `<length-percentage>` for either the start or end range is invalid.

### [Defining range start and defaulting range end](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#defining_range_start_and_defaulting_range_end)

When you define only the `<animation-range-start>`, either by setting a single [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
, a single [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
, or the keyword `normal`, or by specifying a single `<timeline-range-name>` followed by a single `<length-percentage>`, the computed value of the `<animation-range-end>` follows specific rules:

If the value is a single `<length-percentage>` or the keyword `normal`, this value defines the `<animation-range-start>` and the `<animation-range-end>` is implicitly set to `normal`. For example:

*   `animation-range: 20%;` is the equivalent to `animation-range-start: 20%; animation-range-end: normal;`
*   `animation-range: normal;` is the equivalent to `animation-range-start: normal; animation-range-end: normal;`

If the value is a single [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
 (without a `<length-percentage>` following it), that timeline range name is applied to both the `<animation-range-start>` and `<animation-range-end>` components, and the ranges of `0%` and `100%`, respectively, are implied. For example:

*   `animation-range: contain;` is equivalent to `animation-range-start: contain 0%; animation-range-end: contain 100%;`
*   `animation-range: cover;` is equivalent to `animation-range-start: cover 0%; animation-range-end: cover 100%;`

If the value is a single `<timeline-range-name>` with a single `<length-percentage>` following it, in that order, the pair defines the `<animation-range-start>`, and the defined `<timeline-range-name>` is applied to the `<animation-range-end>` at `100%`. For example:

*   `animation-range: cover 20%;` is equivalent to `animation-range-start: cover 20%; animation-range-end: cover 100%;`
*   `animation-range: contain 100px;` is equivalent to `animation-range-start: contain 100px; animation-range-end: contain 100%;`

### [Explicitly defining both range start and range end with two values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#explicitly_defining_both_range_start_and_range_end_with_two_values)

If two or more values are included in your `animation-range` declaration and the values are anything other than a single `<timeline-range-name>` followed by a `<length-percentage>`, both `<animation-range-start>` and `<animation-range-end>` are explicitly set.

If you include two values and the first value is the keyword `normal` or a `<length-percentage>`, that value defines the `<animation-range-start>`, and the second value defines the `<animation-range-end>`. For example:

*   `animation-range: normal 25%;` is equivalent to `animation-range-start: normal; animation-range-end: 25%;`
*   `animation-range: 25% 50%;` is equivalent to `animation-range-start: 25%; animation-range-end: 50%;`
*   `animation-range: 25% contain;` is equivalent to `animation-range-start: 25%; animation-range-end: contain 100%;`
*   `animation-range: 25% normal;` is equivalent to `animation-range-start: 25%; animation-range-end: normal;`

### [Multiple animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#multiple_animations)

When specifying ranges for multiple animations, the `animation-range` shorthand property is specified as one or more single animation ranges, separated by commas. Each animation-range is applied to the animations in the order in which the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
s appear. For situations where the number of animations and the `animation-range` property values do not match, if there are more `animation-range` values than animations, the extra ranges are ignored. If there are more animations than ranges, the list of `animation-range` values are repeated until there is a corresponding range for each animation. For example, if we set `animation-range: 25% 75%, normal;`, the animation range of all the odd numbered animations `25% 75%` and all the even animations will be `0% 100%`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)<br>    : `normal`<br>*   [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)<br>    : `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | Relative to the specified named timeline range if specified, otherwise relative to the entire timeline |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)<br>    : A list where each item may be 'normal', a length percentage, or a timeline range name and a length percentage<br>*   [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)<br>    : A list where each item may be 'normal', a length percentage, or a timeline range name and a length percentage |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)<br>    : Not animatable<br>*   [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)<br>    : Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

animation-range =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<'animation-range-start'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)\
 [<'animation-range-end'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<animation-range-start>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 normal [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<timeline-range-name>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)\
 <length-percentage>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<animation-range-end>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#examples)

-----------------------------------------------------------------------------------------------------------

### [Basic usage of the `animation-range` property](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#basic_usage_of_the_animation-range_property)

In this example, we reduce the duration of the view progress scroll animation by using the `animation-range` property to offset the start and end of the animation, and demonstrate the effect of the [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
 property on shortened animation timelines.

#### HTML

In the middle of a wall of text, we include an element that we will animate. We include a lot of text to ensure that our content overflows its container, but this is hidden for the sake of brevity. We also include a checkbox to toggle the [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
 property on and off, to demonstrate its effect on shortened animation timelines. This is also hidden.

    <div class="content">
      <h1>Content</h1>
    
      <p>
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Risus quis varius quam
        quisque id. Et ligula ullamcorper malesuada proin libero nunc consequat
        interdum varius. Elit ullamcorper dignissim cras tincidunt lobortis feugiat
        vivamus at augue.
      </p>
    
      <p>
        Dolor sed viverra ipsum nunc aliquet. Sed sed risus pretium quam vulputate
        dignissim. Tortor aliquam nulla facilisi cras. A erat nam at lectus urna
        duis convallis convallis. Nibh ipsum consequat nisl vel pretium lectus.
        Sagittis aliquam malesuada bibendum arcu vitae elementum. Malesuada bibendum
        arcu vitae elementum curabitur vitae nunc sed velit.
      </p>
    

html

    <div class="animatedElement"></div>
    

      <p>
        Adipiscing enim eu turpis egestas pretium aenean pharetra magna ac. Arcu
        cursus vitae congue mauris rhoncus aenean vel. Sit amet cursus sit amet
        dictum. Augue neque gravida in fermentum et. Gravida rutrum quisque non
        tellus orci ac auctor augue mauris. Risus quis varius quam quisque id diam
        vel quam elementum. Nibh praesent tristique magna sit amet purus gravida
        quis. Duis ultricies lacus sed turpis tincidunt id aliquet. In egestas erat
        imperdiet sed euismod nisi. Eget egestas purus viverra accumsan in nisl nisi
        scelerisque. Netus et malesuada fames ac.
      </p>
      <label>
        <input type="checkbox" /> Add <code>animation-fill-mode: both;</code>
      </label>
    </div>
    

#### CSS

We define an animation that animates an element's opacity, scale, and background color, causing it to fade in, scale up, and change color as the animation progresses. We apply this animation to the `animatedElement` with the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand.

A view progress timeline is created by setting the [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
 function as the value of the [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 property on our `animatedElement`. The result is that the element animates as it moves upwards through the document as it is scrolled. We declare `animation-timeline` property after the shorthand, as the shorthand resets this property.

Lastly, an `animation-range` declaration is set to make the animation begin later than expected and finish earlier.

css

    .animatedElement {
      background-color: deeppink;
      animation: appear 1ms linear;
      animation-timeline: view();
      animation-range: entry 10% exit -25%;
    }
    
    @keyframes appear {
      from {
        background-color: rebeccapurple;
        opacity: 0;
        transform: scaleX(0);
      }
    
      to {
        background-color: darkturquoise;
        opacity: 0.75;
        transform: scaleX(0.75);
      }
    }
    

We also include conditional styling: when the checkbox is checked, the `animation-fill-mode` property gets applied to the animated element:

css

    :has(:checked) .animatedElement {
      animation-fill-mode: both;
    }
    

The other styles are hidden for the sake of brevity.

    .animatedElement {
      width: 300px;
      height: 200px;
      margin: 0 auto;
      background-color: deeppink;
    }
    
    :has(:checked) .animatedElement {
      animation-fill-mode: both;
    }
    
    .content {
      width: 75%;
      max-width: 800px;
      margin: 0 auto;
    }
    
    p,
    h1 {
      font-family: "Helvetica", "Arial", sans-serif;
    }
    
    h1 {
      font-size: 3rem;
    }
    
    p {
      font-size: 1.5rem;
      line-height: 1.5;
    }
    @supports not (animation-range: normal) {
      body::before {
        content: "Your browser does not support the 'animation-range' property.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Result

Scroll to see the element being animated.

Note how the `from`, or `0%`, keyframe property values are not applied to the animated element until the top block border edge is `10%` past the container's bottom edge; it is full size, fully opaque, and magenta. At that point, the animation is applied and it is styled with the values defined by the `0%` [keyframe selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Keyframe_selectors)
. When the `animation-range-end` is reached, 25% from the top of the scrollport, it jumps back to its original styling.

Generally, you will want to set `animation-fill-mode: both` when creating [scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
. The jump to the default state occurs because we did not set the [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
 property on the element, which can be used to apply an animation's styles to an element before and after the animation's execution. We initially omitted the property in this example to better enable visualizing the effects of `animation-range`.

Check the checkbox to apply the `animation-fill-mode` property to the animated element in then re-scroll: the animation styles should now be continuously applied.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# animation-range](https://drafts.csswg.org/scroll-animations/#animation-range) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
    
*   [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
    
*   [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
    
*   [`timeline-scope`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/timeline-scope)
    
*   [`view-timeline-inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
    
*   [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
    
*   [Understanding timeline range names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
    
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
*   [View timeline range visualizer](https://scroll-driven-animations.style/tools/view-timeline/ranges/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-range/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-range (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-range&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-range%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-range%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-range%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")