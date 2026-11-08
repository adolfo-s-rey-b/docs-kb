*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#mdn-search)
    

`animation-range-end` CSS property
==================================

Baseline 2026

Newly available

Since October 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation-range-end`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the point on the timeline where an animation should end.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword or length percentage value */
    animation-range-end: normal;
    animation-range-end: 80%;
    animation-range-end: 700px;
    
    /* Named timeline range value */
    animation-range-end: cover;
    animation-range-end: contain;
    animation-range-end: cover 80%;
    animation-range-end: contain 700px;
    
    /* Multiple values */
    animation-range-end:
      cover 80%,
      contain 700px;
    
    /* Global values */
    animation-range-end: inherit;
    animation-range-end: initial;
    animation-range-end: revert;
    animation-range-end: revert-layer;
    animation-range-end: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#values)

This property is specified as a comma-separated list of values. Each value can be one of the following:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#normal)

Represents the end of the timeline. This is the default value.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies a length or percentage value measured from the beginning of the timeline.

[`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)

Specifies a named timeline range within the overall timeline. The range ends at `100%`.

[`<timeline-range-name> <length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#timeline-range-name_length-percentage)

Specifies a length or percentage value measured from the beginning of the specified named timeline range.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#description)

---------------------------------------------------------------------------------------------------------------------

The `animation-range-end` property specifies the end of the animation's attachment range. Changing the end of the attachment range can potentially shift the end of the animation, that is, the point where keyframes mapped to `100%` progress land when the iteration count is `1`, and can also reduce the effective duration of the animation.

The property value can be `normal`, a `<length-percentage>`, or a [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
 with an optional `<length-percentage>`. If the `<timeline-range-name>` value does not include a `<length-percentage>`, the percentage defaults to `100%`.

When specifying multiple comma-separated values, they apply to the animations in the order in which the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
 values appear. See [Setting multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
.

The `animation-range-end` property is included in the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand as a reset-only value. This means that using the `animation` shorthand resets any previously declared `animation-range-end` value to `normal`; the shorthand cannot be used to set a new `animation-range-end` value. When creating [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
, you should declare `animation-range-end` _after_ declaring any `animation` shorthand to avoid resetting the value to `normal`.

The `animation-range-end` property, along with the [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
 property, can also be set by using the [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
 shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | Relative to the specified named timeline range if specified, otherwise relative to the entire timeline |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | A list where each item may be 'normal', a length percentage, or a timeline range name and a length percentage |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

animation-range-end =   
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#examples)

---------------------------------------------------------------------------------------------------------------

### [Creating a view progress timeline with a range end](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#creating_a_view_progress_timeline_with_a_range_end)

In this example, the `animation-range-end` is applied to an element animated via a view progress timeline. This makes the animation reach its last keyframe well before the element reaches the end of its containing viewport.

#### HTML

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
    

In the middle of a long block of text, we've included an element that we'll animate. We've added a lot of text to ensure that the content overflows its container; the extra text is hidden here for brevity.

html

    <div class="animatedElement"></div>
    

    <p>
      Adipiscing enim eu turpis egestas pretium aenean pharetra magna ac. Arcu
      cursus vitae congue mauris rhoncus aenean vel. Sit amet cursus sit amet
      dictum. Augue neque gravida in fermentum et. Gravida rutrum quisque non tellus
      orci ac auctor augue mauris. Risus quis varius quam quisque id diam vel quam
      elementum. Nibh praesent tristique magna sit amet purus gravida quis. Duis
      ultricies lacus sed turpis tincidunt id aliquet. In egestas erat imperdiet sed
      euismod nisi. Eget egestas purus viverra accumsan in nisl nisi scelerisque.
      Netus et malesuada fames ac.
    </p>
    <p>
    

We've also included a checkbox that will toggle the [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
 property, so you can see how this property affects animations with shortened timelines.

html

    <label>
      <input type="checkbox" /> Add <code>animation-fill-mode: forwards;</code>
    </label>
    

      </p>
    </div>
    

#### CSS

We've defined a view progress timeline by setting a [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
 function as the value of the [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 property. This is declared **after** the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand to avoid resetting the longhand property value.

We've also set `animation-range-end` to make the animation end earlier than expected.

css

    .animatedElement {
      background-color: deeppink;
      animation: appear 1ms linear;
      animation-timeline: view();
      animation-range-end: exit 25%;
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
    

When the checkbox is checked, the `animation-fill-mode` property gets applied to the animated element:

css

    :has(:checked) ~ .animatedElement {
      animation-fill-mode: forwards;
    }
    

The other styles applied in this example have been hidden for brevity.

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
    @supports not (animation-range-end: normal) {
      body::before {
        content: "Your browser does not support the 'animation-range-end' property.";
        color: black;
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Result

Scroll to see the element animate. Then toggle the checkbox at the end of the block of text and scroll again. Notice how the element finishes animating when it is 75% of the way through the viewport, and how it returns to its default state at that point when the `animation-fill-mode` property is not applied.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# animation-range-end](https://drafts.csswg.org/scroll-animations/#animation-range-end) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
    
*   [`animation-range-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start)
    
*   [`view-timeline-inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
    
*   [`Element.animate()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animate)
     `rangeStart` property
*   [Scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
    
*   [Understanding timeline range names](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timeline_range_names)
    
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
*   [View progress timeline: Ranges and animation progress visualizer](https://scroll-driven-animations.style/tools/view-timeline/ranges/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-range-end/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-range-end (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-range-end&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-range-end%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-range-end%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-range-end%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3144662126702b3473a0c9537c5ec8ff61457ff5%0A*+Document+last+modified%3A+2026-10-22T17%3A51%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")