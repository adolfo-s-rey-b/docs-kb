*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#mdn-search)
    

`animation-timeline` CSS property
=================================

Baseline 2026

Newly available

Since October 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation-timeline`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the timeline used to control the progress of a CSS animation.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#syntax)

----------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#values)

The `animation-timeline` property is specified as one or more comma-separated values, each of which can be one of the following:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#none)

The animation is not associated with a timeline, and no animation occurs.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#auto)

The animation's timeline is the document's default [`DocumentTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentTimeline)
. This is the default value.

[`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)

Defines the root element, nearest scroller, or self as an anonymous scroll progress timeline, and optionally the scroll direction of the scroller.

[`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)

Defines the nearest ancestor scroll container as an anonymous view progress timeline, optionally overriding the default `baseline` axis direction and the `auto` start and ending insets.

[`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#dashed-ident)

The name of a scroll-driven or view-progress timeline, as defined by the scroll container's [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
 or [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
 property (or the [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
 or [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
 shorthand property).

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#description)

--------------------------------------------------------------------------------------------------------------------

The default timeline for a CSS keyframe animation is the time-based [`DocumentTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentTimeline)
. The `animation-timeline` property can be used to set a named or anonymous scroll progress or view progress timeline. Alternatively, it can be used to explicitly set the default time-based document timeline to control the progress of an element's animation or to have no timeline at all, in which case the element does not animate.

The following types of timelines can be set via `animation-timeline`:

[`DocumentTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentTimeline)

The default document timeline, which is progressed through by the passing of time since the document was first loaded in the browser. This is the timeline traditionally associated with CSS animations and is selected with a value of `auto`, or by not specifying an `animation-timeline` value at all, as this is the default value.

[Scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#scroll_progress_timelines)

The animation is progressed through by scrolling a scrollable element, or _scroller_, horizontally or vertically. The element that provides the scroll progress timeline can be specified in two ways:

[Named scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#named_scroll_progress_timelines)

The scroller is explicitly named by setting the [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
 property (or the [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
 shorthand property) to a [`<dashed-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
; that `<dashed-ident>` name is then set as the value of the `animation-timeline` property.

[Anonymous scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_scroll_progress_timelines)

The `animation-timeline` property of the element to animate is set to the [`scroll()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
 function. The function's two optional parameters define the scroller providing the scroll progress timeline and the scroll axis to be used.

[View progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#view_progress_timelines)

A keyframe animation is progressed through based on the change in visibility of an element inside a scroller; this element is known as the _subject_. By default, the timeline is at `0%` when the element first becomes visible at one edge of the scroller, and is at `100%` when its end edge exits the scroller's opposite edge. A view progress timeline can be specified in two ways:

[Named view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#named_view_progress_timeline)

The subject is explicitly named by setting the [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
 property (or the [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
 shorthand property) to a `<dashed-ident>`. When you set the `animation-timeline` property of the element to animate to that `<dashed-ident>`, the subject's visibility controls the progression of the element's animation. Note that the element to animate does not have to be the same as the subject.

[Anonymous view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines#anonymous_view_progress_timeline_the_view_function)

The `animation-timeline` property of the element to animate is set to a [`view()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
 function, causing it to be animated based on its visibility within the scrollport of its nearest parent scroller.

[No timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#no_timeline)

All animation timelines can be removed by selecting a value of `none`. When `animation-timeline: none` is set, no animation will occur as there is no timeline to follow.

The `animation-timeline` property is included in the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand as a reset-only value. This means that including `animation` resets a previously-declared `animation-timeline` value to `auto`. As this component of the shorthand is reset-only, a specific value cannot be set via `animation`. When creating [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations/Timelines)
, you need to declare `animation-timeline` after declaring any `animation` shorthand for it to take effect.

If you specify multiple comma-separated values, each `animation-timeline` value is applied to a single animation in the order in which the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
 values appear. If the number of values in the `animation-timeline` declaration is greater than the number of `animation-name` values, the excess timeline values are ignored. If there are fewer `animation-timeline` values than `animation-name` values, the `animation-timeline` values are repeated, in order, until every `animation-name` has an associated timeline.

If two or more timelines share the same `<dashed-ident>` name and the same specificity, the one last declared within the cascade will be used. If no timeline is found that matches a name included within the `animation-timeline`, the `animation-name` associated with that value is not associated with a timeline.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | a list, each item either a case-sensitive CSS identifier or the keywords `none`, `auto` |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

animation-timeline =   
  <single-animation-timeline>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<single-animation-timeline> =   
  auto            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none            [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<dashed-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/dashed-ident)
  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <scroll()>      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <view()>          
  
[<scroll()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/scroll)
 =   
  scroll( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <scroller> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 <axis> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<view()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/view)
 =   
  view( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <axis> [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")\
 [<'view-timeline-inset'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
<scroller> =   
  root     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  nearest  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  self       
  
[<axis>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/axis)
 =   
  block   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  inline  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  x       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  y         
  
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
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#examples)

--------------------------------------------------------------------------------------------------------------

### [Basic usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#basic_usage)

This example demonstrates basic usage of the `animation-timeline` property, along with the `none`, `auto`, and default (`auto`) values.

#### HTML

We have an [`<article>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/article)
 with three [`<section>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/section)
 children. Each `<section>` has a unique `id` and a [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 child.

#### CSS

We use [flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 to set the three sections side-by-side. We use [generated content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Generated_content)
 to display the `id`. We style all elements the same, applying the `rotate` [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 animation that rotates the element by 1 full turn. Using the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand, we declare infinite, 2-second, linearly progressing iterations of the `rotate` animation, alternating the direction of each animation.

The only difference is the `animation-timeline` declaration (or lack thereof in the case of `default`) for each `<div>`.

Because the `animation-timeline` property is included in the [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 shorthand as a reset-only value, the `animation-timeline` must come after the `animation` shorthand, or be applied with greater specificity than the `animation` shorthand, to be applied.

#### Results

Note that declaring a value of `auto` has the same effect as allowing the `animation-timeline` to default to that value, and that `none` removes all timelines from the element, so no animation in the `none` case.

### [Setting a named scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#setting_a_named_scroll_progress_timeline)

In this example, the animation timeline is set to a horizontal scroll progress timeline.

#### HTML

Our container includes three stretcher elements which will be wide enough to ensure our container is a scroll container. The middle one contains a shape that we will animate.

html

    <div id="container">
      <div class="stretcher"></div>
      <div class="stretcher">
        <div id="shape"></div>
      </div>
      <div class="stretcher"></div>
    </div>
    

#### CSS

We define the container as a flex container, setting a [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 on the container that is half the width of it's combined flex children. Adding an [`overflow-x`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-x)
 value of `scroll` sets it to have a horizontal scrollbar.

Our scroll progress timeline, defined using the [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
 and [`scroll-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-axis)
 properties, is named `--square-timeline`. This timeline is applied to our `#shape` element using `animation-timeline: --square-timeline`.

css

    #container {
      display: flex;
      width: 300px;
      border: 1px solid;
    
      overflow-x: scroll;
      scroll-timeline-axis: inline;
      scroll-timeline-name: --square-timeline;
    }
    
    .stretcher {
      flex: 0 0 200px;
    }
    

The CSS below defines a square that rotates in alternate directions according to the timeline provided by the `animation-timeline` property, which is set to the `--square-timeline` timeline named above. The animation is set two occur twice, in alternating directions, as it passes through the viewport. We added [notched corners](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/corner-shape)
 to make the animation effect more apparent.

css

    #shape {
      background-color: deeppink;
      width: 100px;
      height: 100px;
      border-radius: 25px;
      corner-shape: notch;
    
      animation: rotateAnimation 1ms linear 2 alternate;
      animation-timeline: --square-timeline;
    }
    
    @keyframes rotateAnimation {
      from {
        transform: rotate(0deg);
      }
      to {
        transform: rotate(360deg);
      }
    }
    

    @layer no-support {
      @supports not (animation-timeline: --square-timeline) {
        body::before {
          content: "Your browser doesn't support named animation timelines.";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

#### Result

Scroll to see the element being animated.

### [Setting an anonymous scroll progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#setting_an_anonymous_scroll_progress_timeline)

This example expands on the previous one, applying an anonymous scroll progress timeline using the `scroll()` function.

#### CSS

We include all the CSS from the previous example, only setting the `animation-timeline` property to override the previous example's value. The timeline is provided by the `scroll(inline nearest)` value, which selects the scrollbar in the inline direction of the nearest ancestor element that has scrollbars. This is the vertical scrollbar of the `#container` element, as the `.stretcher` elements don't have overflowing content and therefore aren't scroll containers.

css

    #shape {
      animation-timeline: scroll(inline nearest);
    }
    

    @layer no-support {
      @supports not (animation-timeline: scroll()) {
        body::before {
          content: "Your browser doesn't support the scroll() function.";
          background-color: wheat;
          display: block;
          text-align: center;
          padding: 1rem 0;
        }
      }
    }
    

#### Result

Scroll to see the square element being animated.

### [Setting a named view progress timeline](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#setting_a_named_view_progress_timeline)

In this example, we demonstrate how to create and apply a named view progress timeline. Two elements will be animated, with different elements serving as the scroller.

#### HTML

    <main class="scroller">
      <div class="container">
        <h1>Directions</h1>
        <h2>Lincoln Memorial to Martin Luther King, Jr. Memorial</h2>
        <ol>
          <li>Head south on Lincoln Memorial Circle</li>
          <li>Turn right toward Independence Ave</li>
          <li>Turn left onto Independence Ave</li>
          <li>Turn right onto West Basin Dr</li>
          <li>Look up when you reach 64 Independence Ave!</li>
        </ol>
        <section>
    

Our HTML includes a lot of text in a container within a scroller, which we've hidden for brevity. In the middle of the wall of text, we include two `<div>` elements that we will animate based on the visibility of the element itself in the first case and based on the visibility of its parent in the second case:

html

    <div class="animated-element self">SELF</div>
    <div class="animated-element parent">PARENT</div>
    

    </section>
    <h2>Martin Luther King, Jr. Memorial to Lincoln Memorial</h2>
    <ol>
      <li>Head north toward Independence Ave SW</li
      ><li>Turn left onto Independence Ave</li
      ><li>Turn right toward the Korean War Veterans Memorial</li
      ><li>Take a photo of the memorial as you walk past it.</li
      ><li>Head north on Lincoln Memorial Circle</li
      ><li>Look up. You can't miss it!</li>
    </ol>
      </div>
    </main>
    

#### CSS

We create a keyframe animation that changes the opacity and scale of the element, and apply it to both animated elements:

css

    @keyframes animation-effect {
      0% {
        opacity: 0;
        scale: 0;
      }
      100% {
        opacity: 1;
        scale: 1;
      }
    }
    
    .animated-element {
      animation: animation-effect 1ms linear;
    }
    

The `self` element is explicitly named as the scroller for itself by setting the `view-timeline-name` property to a `<dashed-ident>` and also setting that `<dashed-ident>` name as the value of the `animation-timeline` property. In the `parent` case, we set the `container` as the scroller for the animated element:

css

    .self {
      view-timeline-name: --self-scroller-element;
      animation-timeline: --self-scroller-element;
    }
    .container {
      view-timeline-name: --parent-scroller-element;
    }
    .parent {
      animation-timeline: --parent-scroller-element;
    }
    

Additional CSS declarations were hidden for brevity.

    @layer setup {
      section {
        display: flex;
        gap: 10px;
      }
      main {
        width: 400px;
        padding: 1em;
        height: 300px;
        overflow: scroll;
        border: 1px solid;
        background-color: beige;
        font-family: sans-serif;
      }
    
      li {
        margin-bottom: 0.75lh;
      }
    
      .animated-element {
        height: 200px;
        width: calc(100% - 2em);
        margin: auto;
        background-color: forestgreen;
        background-image:
          repeating-linear-gradient(37deg, transparent 0 52px, beige 52px 57px),
          repeating-linear-gradient(94deg, transparent 0 52px, beige 52px 57px);
        border: 1px solid;
        font-size: 3em;
        place-content: center;
      }
    }
    

#### Result

Scroll the container to see both elements animate.

Note how the visibility of the `self` element controls its own animation. In this case, the element is at the `0%` keyframe when the top edge enters the viewport, or visible part of the scrollport, and only reaches the `100%` keyframe when the bottom edge exits the viewport.

The `parent` element only becomes visible when that parent is visible, meaning that when it comes into view, it is already about `25%` of the way through the animation. It is only about `75%` through its animation when it exits the top of the viewport.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Animations Level 2  <br>\# animation-timeline](https://drafts.csswg.org/css-animations-2/#animation-timeline) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    , [`animation-composition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition)
    , [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
    , [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
    , [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
    , [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
    , [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
    , [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    , [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
    , [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
    
*   [`scroll-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-name)
    , [`scroll-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline-axis)
    , [`scroll-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scroll-timeline)
    
*   [`view-timeline-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-name)
    , [`view-timeline-axis`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-axis)
    , [`view-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline)
    , [`view-timeline-inset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/view-timeline-inset)
    
*   [`AnimationTimeline`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationTimeline)
    
*   [Guide: Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations)
     module
*   [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-timeline/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-timeline (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-timeline&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-timeline%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-timeline%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-timeline%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")