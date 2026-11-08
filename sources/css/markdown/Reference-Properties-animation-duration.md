*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#mdn-search)
    

`animation-duration` CSS property
=================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation-duration`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the length of time that an animation takes to complete one cycle.

It is often convenient to use the shorthand property [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 to set all animation properties at once.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#try_it)

----------------------------------------------------------------------------------------------------------

    animation-duration: 750ms;
    

    animation-duration: 3s;
    

    animation-duration: 0s;
    

    <section class="flex-column" id="default-example">
      <div class="animating" id="example-element"></div>
      <button id="play-pause">Play</button>
    </section>
    

    #example-element {
      animation-direction: alternate;
      animation-iteration-count: infinite;
      animation-name: slide;
      animation-play-state: paused;
      animation-timing-function: ease-in;
      background-color: #1766aa;
      border-radius: 50%;
      border: 5px solid #333333;
      color: white;
      height: 150px;
      margin: auto;
      margin-left: 0;
      width: 150px;
    }
    
    #example-element.running {
      animation-play-state: running;
    }
    
    #play-pause {
      font-size: 2rem;
    }
    
    @keyframes slide {
      from {
        background-color: orange;
        color: black;
        margin-left: 0;
      }
      to {
        background-color: orange;
        color: black;
        margin-left: 80%;
      }
    }
    

    const el = document.getElementById("example-element");
    const button = document.getElementById("play-pause");
    
    button.addEventListener("click", () => {
      if (el.classList.contains("running")) {
        el.classList.remove("running");
        button.textContent = "Play";
      } else {
        el.classList.add("running");
        button.textContent = "Pause";
      }
    });
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* Single animation */
    animation-duration: auto; /* Default */
    animation-duration: 6s;
    animation-duration: 120ms;
    
    /* Multiple animations */
    animation-duration: 1.64s, 15.22s;
    animation-duration: 10s, 35s, 230ms;
    
    /* Global values */
    animation-duration: inherit;
    animation-duration: initial;
    animation-duration: revert;
    animation-duration: revert-layer;
    animation-duration: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#values)

This property is specified as a comma-separated list of the following values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#auto)

For time-based animations, `auto` is equivalent to a value of `0s` (see below). For [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
, `auto` fills the entire timeline with the animation.

[`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)

The time that an animation takes to complete one cycle. This may be specified in either seconds (`s`) or milliseconds (`ms`). The value must be positive or zero and the unit is required.

If no value is provided, the default value of `0s` is used, in which case the animation still executes (the [`animationStart`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationstart_event)
 and [`animationEnd`](https://developer.mozilla.org/en-US/docs/Web/API/Element/animationend_event)
 events are fired). Whether or not the animation will be visible when the duration is `0s` will depend on the value of [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
, as explained below:

*   If `animation-fill-mode` is set to `backwards` or `both`, the first frame of the animation as defined by `animation-direction` will be displayed during [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
     countdown.
*   If `animation-fill-mode` is set to `forwards` or `both`, the last frame of the animation will be displayed, as defined by `animation-direction`, after the `animation-delay` expires.
*   If `animation-fill-mode` is set to `none`, the animation will have no visible effect.

**Note:** Negative values are invalid, causing the declaration to be ignored. Some early, prefixed, implementations may consider them as identical to `0s`.

**Note:** When you specify multiple comma-separated values on an `animation-*` property, they are applied to the animations in the order in which the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
s appear. For situations where the number of animations and `animation-*` property values do not match, see [Setting multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
.

**Note:** When creating [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
, specifying an `animation-duration` value in seconds or milliseconds doesn't really make sense. In tests, it seemed to have no effect on scroll progress timeline animations, while on view progress timeline animations it seemed to push the animation to happen nearer the end of the timeline. However, Firefox requires an `animation-duration` to be set for it to successfully apply the animation. You are therefore advised to set `animation-duration` to `1ms` so that animations will work in Firefox, but the effect is not altered too much by it.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0s` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

animation-duration =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<time \[0s,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#examples)

--------------------------------------------------------------------------------------------------------------

### [Setting animation duration](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#setting_animation_duration)

This animation has an animation-duration of 0.7 seconds.

#### HTML

html

    <div class="box"></div>
    

#### CSS

css

    .box {
      background-color: rebeccapurple;
      border-radius: 10px;
      width: 100px;
      height: 100px;
    }
    
    .box:hover {
      animation-name: rotate;
      animation-duration: 0.7s;
    }
    
    @keyframes rotate {
      0% {
        transform: rotate(0);
      }
      100% {
        transform: rotate(360deg);
      }
    }
    

#### Result

Hover over the rectangle to start the animation.

See [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
 for more examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Animations Level 2  <br>\# animation-duration](https://drafts.csswg.org/css-animations-2/#animation-duration) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   JavaScript [`AnimationEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent)
     API
*   Other related animation properties: [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    , [`animation-composition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition)
    , [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
    , [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
    , [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
    , [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
    , [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    , [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
    , [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    , [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-duration/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-duration (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-duration&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-duration%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-duration%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-duration%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F22c0b3059ff71d769af670478cc41605581108d1%0A*+Document+last+modified%3A+2026-09-10T13%3A27%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")