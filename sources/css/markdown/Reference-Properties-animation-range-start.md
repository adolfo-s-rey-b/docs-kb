*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#mdn-search)
    

`animation-range-start` CSS property
====================================

Baseline 2026

Newly available

Since October 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation-range-start`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the point on the timeline where an animation should start.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Keyword or length percentage value */
    animation-range-start: normal;
    animation-range-start: 20%;
    animation-range-start: 100px;
    
    /* Named timeline range value */
    animation-range-start: cover;
    animation-range-start: contain;
    animation-range-start: cover 20%;
    animation-range-start: contain 100px;
    
    /* Multiple values */
    animation-range-start:
      cover 20%,
      contain 100px;
    
    /* Global values */
    animation-range-start: inherit;
    animation-range-start: initial;
    animation-range-start: revert;
    animation-range-start: revert-layer;
    animation-range-start: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#values)

This property is specified as a comma-separated list of values. Each value can be one of the following:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#normal)

Represents the start of the timeline. This is the default value.

[`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)

Specifies a length or percentage value measured from the beginning of the timeline.

[`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)

Specifies a named timeline range within the overall timeline. The range starts at `0%`.

[`<timeline-range-name> <length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#timeline-range-name_length-percentage)

Specifies a length or percentage value measured from the beginning of the specified named timeline range.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#description)

-----------------------------------------------------------------------------------------------------------------------

Allowed values for the `animation-range-start` property are `normal`, a [`<length-percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
, a `<timeline-range-name>`, or a `<timeline-range-name>` followed by a `<length-percentage>`. If the [`<timeline-range-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/timeline-range-name)
 value does not include a `<length-percentage>`, the percentage defaults to `0%`.

See [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
 for a detailed description of the available values.

When specifying multiple comma-separated values, they apply to the animations in the order in which the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
 values appear. See [Setting multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
.

The `animation-range-start` is included in the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand as a reset-only value. This means that using the `animation` shorthand resets any previously declared `animation-range-start` value of equal or lower specificity to `normal`; the shorthand cannot be used to set a new `animation-range-start` value. When creating [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
, you should declare `animation-range-start` _after_ declaring any `animation` shorthand to avoid resetting the value to `normal`.

The `animation-range-start`, along with the [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
 property, can also be set using the [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
 shorthand.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| Percentages | Relative to the specified named timeline range if specified, otherwise relative to the entire timeline |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | A list where each item may be 'normal', a length percentage, or a timeline range name and a length percentage |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

animation-range-start =   
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#examples)

-----------------------------------------------------------------------------------------------------------------

### [Creating a scroll progress timeline with range start](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#creating_a_scroll_progress_timeline_with_range_start)

In this example, the `animation-range-start` is applied to an element animated via a scroll progress timeline. This makes the animation start well before the element enters the scrollport.

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
      dictum. Augue neque gravida in fermentum et. Gravida rutrum quisque non
      tellus orci ac auctor augue mauris. Risus quis varius quam quisque id diam
      vel quam elementum. Nibh praesent tristique magna sit amet purus gravida
      quis. Duis ultricies lacus sed turpis tincidunt id aliquet. In egestas erat
      imperdiet sed euismod nisi. Eget egestas purus viverra accumsan in nisl nisi
      scelerisque. Netus et malesuada fames ac.
    </p>
    </div>
    

#### CSS

A scroll progress timeline is defined using setting a [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
 function as the value of the [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 property. This is declared **after** the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand to avoid resetting the longhand property value.

We've also set `animation-range-start` to make the animation start earlier than expected.

css

    .animatedElement {
      background-color: deeppink;
    
      animation: appear 1ms linear;
    
      animation-timeline: scroll();
      animation-range-start: -25%;
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
    

Other styles applied in this example have been hidden here for brevity.

    .animatedElement {
      height: 200px;
      margin: 0 auto;
      background-color: deeppink;
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
    
    @supports not (animation-range-start: normal) {
      body::before {
        content: "Your browser does not support the 'animation-range-start' property.";
        color: black;
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### Result

Scroll to see the element animate. Notice how the element is already scaled and semi-opaque as it enters the viewport. This is because the element started animating well before it entered the viewport.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# animation-range-start](https://drafts.csswg.org/scroll-animations/#animation-range-start) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [`animation-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range)
    
*   [`animation-range-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-end)
    
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

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-range-start/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-range-start/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-range-start (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-range-start&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-range-start%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-range-start%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-range-start%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F22c0b3059ff71d769af670478cc41605581108d1%0A*+Document+last+modified%3A+2026-09-10T13%3A27%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")