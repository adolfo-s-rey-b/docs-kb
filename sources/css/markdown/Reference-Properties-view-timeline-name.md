*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#mdn-search)
    

`view-timeline-name` CSS property
=================================

Baseline 2026

Newly available

Since October 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`view-timeline-name`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the names of one or more [named view progress timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#named_view_progress_timeline)
 associated with the element.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    view-timeline-name: none;
    
    /* Custom identifier */
    view-timeline-name: --custom_name_for_timeline;
    
    /* Multiple identifiers */
    view-timeline-name: --first_timeline_name, --another_timeline_name;
    
    /* Global values */
    view-timeline-name: inherit;
    view-timeline-name: initial;
    view-timeline-name: revert;
    view-timeline-name: revert-layer;
    view-timeline-name: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#none)

Indicates that the timeline has no name. This is the default value.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#dashed-ident)

Specifies a comma-separated list of [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
 custom name identifiers. All `<dashed-ident>` values must start with `--`, which helps avoid name clashes with standard CSS keywords.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#description)

--------------------------------------------------------------------------------------------------------------------

The `view-timeline-name` property is used to set the name of a [view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#view_progress_timelines)
. A view progress timeline is progressed through based on the change in visibility of an element, called the _subject_, inside a scrollable element, called the _scroller_. The `view-timeline-name` property is set on the subject. You can also set `view-timeline-name` by using the [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
 shorthand property.

If the subject's named scroller element does not overflow its container in the [axis dimension](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
 or if the overflow is hidden or clipped, no scroll progress timeline will be created.

Once created, the `<dashed-ident>` name values specified can be referenced in [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
 declarations to indicate the element that will be animated as the timeline progresses.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | `none` or an ordered list of identifiers |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

view-timeline-name =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#examples)

--------------------------------------------------------------------------------------------------------------

### [Creating a named view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#creating_a_named_view_progress_timeline)

A view progress timeline named `--subject-reveal` is defined using the `view-timeline-name` property on a subject element with a `class` of `animation`. This is then set as the timeline for the same element using `animation-timeline: --subject-reveal;`. The result is that the subject element animates as it moves upwards through the document as it is scrolled.

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
    

The `<div>` with the class of `subject` is also given a class of `animation` — this is where `view-timeline-name` is set to define a named view progress timeline. It is also given an `animation-timeline` name with the same value to declare that this will be the element animated as the view progress timeline is progressed.

Last, an animation is specified on the element that animates its opacity and scale, causing it to fade in and size up as it moves up the scroller.

css

    .animation {
      view-timeline-name: --subject-reveal;
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
      @supports not (view-timeline-name: none) {
        body::before {
          content: "Your browser doesn't support the `view-timeline-name` property.";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

#### Result

Scroll to see the subject element being animated.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Scroll-driven Animations  <br>\# view-timeline-name](https://drafts.csswg.org/scroll-animations/#view-timeline-name) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    
*   [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
    
*   [Scroll-driven animation timelines](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
    
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/view-timeline-name/index.md?plain=1 "Folder: en-us/web/css/reference/properties/view-timeline-name (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-timeline-name&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-timeline-name%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fview-timeline-name%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fview-timeline-name%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fa8b7faffbd3fdeae5c0be97793d963d8a31cd1cf%0A*+Document+last+modified%3A+2026-04-22T11%3A39%3A37.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")