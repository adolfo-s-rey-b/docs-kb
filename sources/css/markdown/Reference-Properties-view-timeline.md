*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#mdn-search)
    

`view-timeline` CSS property
============================

Baseline 2026

Newly available

Since October 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`view-timeline`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property defines a [named view progress timeline's](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#named_view_progress_timeline)
 name, direction, and inset values.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#constituent_properties)

-------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
    
*   [`view-timeline-inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
    
*   [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* One component */
    view-timeline: none;
    view-timeline: --custom_name_for_timeline;
    
    /* Two components */
    view-timeline: --custom_name_for_timeline block;
    view-timeline: --custom_name_for_timeline y;
    view-timeline: none inline;
    view-timeline: none x;
    
    /* Three components */
    view-timeline: --custom_name_for_timeline block auto;
    view-timeline: --custom_name_for_timeline block 20% 200px;
    
    /* Global values */
    view-timeline: inherit;
    view-timeline: initial;
    view-timeline: revert;
    view-timeline: revert-layer;
    view-timeline: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#values)

[`<view-timeline-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#view-timeline-name)

See [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
. The default value is `none`.

[`<view-timeline-inset>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#view-timeline-inset)

See [`view-timeline-inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
. The default value is `auto`.

[`<view-timeline-axis>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#view-timeline-axis)

See [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
. The default value is `block`.

### [Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#description)

The `view-timeline` shorthand property defines a _named view progress timeline_, which progresses based on changes to the visibility of an element (the _subject_) within a scrollable element (_scroller_). The `view-timeline` property is set on the subject. If the scroller element does not overflow its container in the axis dimension or if the overflow is hidden or clipped, no scroll progress timeline will be created.

The subject's visibility inside the scroller is tracked — by default, the timeline is at `0%` when the subject is first visible at one edge of the scroller and `100%` when it reaches the opposite edge.

The `view-timeline` can contain three constituent values: a name for the named view progress timeline, a scroll axis value, and up to two timeline inset values. If only one value is declared, the value is the `view-timeline-name`. The name is then referenced in an [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 declaration to indicate the element that will be animated as the timeline progresses. This can be the subject element, but it doesn't have to be — you can animate a different element as the subject moves through the scrolling area.

The `view-timeline` shorthand property can be applied to a container element to set a combination of the `<view-timeline-name>`, `<view-timeline-inset>`, and `<view-timeline-axis>` values. At least one value must be specified. If all values are specified, the order must be `<view-timeline-name>` followed by `<view-timeline-axis>` and/or `<view-timeline-inset>`.

The names specified in the `<view-timeline-name>` component must be a list of comma-separated [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 values (which means they must start with `--`) or the keyword `none`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)<br>    : `none`<br>*   [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)<br>    : `block` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)<br>    : `none` or an ordered list of identifiers<br>*   [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)<br>    : Not animatable<br>*   [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)<br>    : Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

view-timeline =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<'view-timeline-name'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<'view-timeline-axis'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)\
 [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [<'view-timeline-inset'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<view-timeline-name>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<view-timeline-axis>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 block [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 inline [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 x [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 y [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<view-timeline-inset>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
 =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <length-percentage> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<length-percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length-percentage)
 =   
  [<length>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#examples)

---------------------------------------------------------------------------------------------------------

### [Creating a named view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#creating_a_named_view_progress_timeline)

A view progress timeline named `--subject-reveal` is defined using the `view-timeline` property on a subject element with a `class` of `animation`. This is then set as the timeline for the same element using `animation-timeline: --subject-reveal`. The result is that the subject element animates as it moves upwards through the document as it is scrolled.

#### HTML

The HTML for the example is shown below.

html

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
    
      <div class="subject animation"></div>
    
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

The `subject` element and its containing `content` element are styled minimally, and the text content is given some basic font settings:

css

    .subject {
      width: 300px;
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
    

The `<div>` with the class of `subject` is also given a class of `animation` — this is where `view-timeline` is set to define a named view progress timeline. It is also given an `animation-timeline` name with the same value to declare that this will be the element animated as the view progress timeline progresses.

Lastly, an animation is specified on the element that animates its opacity and scale, causing it to fade in and grow as it moves up the scroller.

css

    .animation {
      view-timeline: --subject-reveal block;
      animation-timeline: --subject-reveal;
    
      animation-name: appear;
      animation-fill-mode: both;
      animation-duration: 1ms; /* Firefox requires this to apply the animation */
    }
    
    @keyframes appear {
      from {
        opacity: 0;
        transform: scaleX(0);
      }
    
      to {
        opacity: 1;
        transform: scaleX(1);
      }
    }
    

    @layer no-support {
      @supports not (view-timeline: none) {
        body::before {
          content: "Your browser doesn't support the `view-timeline` property.";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

#### Result

Scroll to see the subject element being animated.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# view-timeline-shorthand](https://drafts.csswg.org/scroll-animations/#view-timeline-shorthand) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline#see_also)

---------------------------------------------------------------------------------------------------------

*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
    , [`view-timeline-inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
    , [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
    
*   [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
    
*   [Guide: CSS scroll driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#named_view_progress_timeline)
    
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/view-timeline/index.md?plain=1 "Folder: en-us/web/css/reference/properties/view-timeline (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-timeline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-timeline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-timeline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-timeline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")