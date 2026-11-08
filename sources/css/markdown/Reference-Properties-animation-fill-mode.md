*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#mdn-search)
    

`animation-fill-mode` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation-fill-mode`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how a CSS animation applies styles to its target before and after its execution.

It is often convenient to use the shorthand property [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 to set all animation properties at once.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#try_it)

-----------------------------------------------------------------------------------------------------------

    animation-fill-mode: none;
    animation-delay: 1s;
    

    animation-fill-mode: forwards;
    animation-delay: 1s;
    

    animation-fill-mode: backwards;
    animation-delay: 1s;
    

    animation-fill-mode: both;
    animation-delay: 1s;
    

    <section class="flex-column" id="default-example">
      <div>Animation <span id="play-status"></span></div>
      <div id="example-element">Select a mode to start!</div>
    </section>
    

    #example-element {
      background-color: #1766aa;
      color: white;
      margin: auto;
      margin-left: 0;
      border: 5px solid #333333;
      width: 150px;
      height: 150px;
      border-radius: 50%;
    
      display: flex;
      justify-content: center;
      align-items: center;
      flex-direction: column;
    }
    
    #play-status {
      font-weight: bold;
    }
    
    .animating {
      animation: slide 1s ease-in 1;
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
    const status = document.getElementById("play-status");
    
    function update() {
      status.textContent = "delaying";
      el.className = "";
      window.requestAnimationFrame(() => {
        window.requestAnimationFrame(() => {
          el.className = "animating";
        });
      });
    }
    
    el.addEventListener("animationstart", () => {
      status.textContent = "playing";
    });
    
    el.addEventListener("animationend", () => {
      status.textContent = "finished";
    });
    
    const observer = new MutationObserver(() => {
      update();
    });
    
    observer.observe(el, {
      attributes: true,
      attributeFilter: ["style"],
    });
    
    update();
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Single animation */
    animation-fill-mode: none;
    animation-fill-mode: forwards;
    animation-fill-mode: backwards;
    animation-fill-mode: both;
    
    /* Multiple animations */
    animation-fill-mode: none, backwards;
    animation-fill-mode: both, forwards, none;
    
    /* Global values */
    animation-fill-mode: inherit;
    animation-fill-mode: initial;
    animation-fill-mode: revert;
    animation-fill-mode: revert-layer;
    animation-fill-mode: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#values)

This property is specified as a comma-separated list of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#none)

The animation will not apply any styles to the target when it's not executing. The element will instead be displayed using any other CSS rules applied to it. This is the default value.

[`forwards`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#forwards)

The target will retain the computed values set by the last [keyframe](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 encountered during execution. The last keyframe depends on the value of [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
 and [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
:

| `animation-direction` | `animation-iteration-count` | last keyframe encountered |
| --- | --- | --- |
| `normal` | even or odd | `100%` or `to` |
| `reverse` | even or odd | `0%` or `from` |
| `alternate` | even | `0%` or `from` |
| `alternate` | odd | `100%` or `to` |
| `alternate-reverse` | even | `100%` or `to` |
| `alternate-reverse` | odd | `0%` or `from` |

Animated properties behave as if included in a set [`will-change`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/will-change)
 property value. If a new stacking context was created during the animation, the target element retains the stacking context after the animation has finished.

[`backwards`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#backwards)

The animation will apply the values defined in the first relevant [keyframe](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 as soon as it is applied to the target, and retain this during the [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
 period. The first relevant keyframe depends on the value of [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
:

| `animation-direction` | first relevant keyframe |
| --- | --- |
| `normal` or `alternate` | `0%` or `from` |
| `reverse` or `alternate-reverse` | `100%` or `to` |

[`both`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#both)

The animation will follow the rules for both forwards and backwards, thus extending the animation properties in both directions.

**Note:** When you specify multiple comma-separated values on an `animation-*` property, they are applied to the animations in the order in which the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
s appear. For situations where the number of animations and `animation-*` property values do not match, see [Setting multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
.

**Note:** `animation-fill-mode` has the same effect when creating [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
 as it does for regular time-based animations.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

animation-fill-mode =   
  <single-animation-fill-mode>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<single-animation-fill-mode> =   
  none       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  forwards   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  backwards  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  both         

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#examples)

---------------------------------------------------------------------------------------------------------------

### [Setting fill mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#setting_fill_mode)

You can see the effect of `animation-fill-mode` in the following example. It demonstrates how you can make the animation remain in its final state rather than reverting to the original state (which is the default).

#### HTML

html

    <p>Move your mouse over the gray box!</p>
    <div class="demo">
      <div class="grows-and-stays">This grows and stays big.</div>
      <div class="grows">This just grows.</div>
    </div>
    

#### CSS

css

    .demo {
      border-top: 100px solid #cccccc;
      height: 300px;
    }
    
    @keyframes grow {
      0% {
        font-size: 0;
      }
      100% {
        font-size: 40px;
      }
    }
    
    .demo:hover .grows {
      animation-name: grow;
      animation-duration: 3s;
    }
    
    .demo:hover .grows-and-stays {
      animation-name: grow;
      animation-duration: 3s;
      animation-fill-mode: forwards;
    }
    

#### Result

See [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
 for more examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Animations Level 1  <br>\# animation-fill-mode](https://drafts.csswg.org/css-animations/#animation-fill-mode) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   JavaScript [`AnimationEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent)
     API
*   Other related animation properties: [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    , [`animation-composition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition)
    , [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
    , [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
    , [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
    , [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
    , [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    , [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
    , [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    , [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-fill-mode/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-fill-mode (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-fill-mode&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-fill-mode%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-fill-mode%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-fill-mode%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")