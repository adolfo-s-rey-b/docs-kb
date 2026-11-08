*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#mdn-search)
    

`animation-iteration-count` CSS property
========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation-iteration-count`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the number of times an animation sequence should be played before stopping.

It is often convenient to use the shorthand property [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 to set all animation properties at once.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#try_it)

-----------------------------------------------------------------------------------------------------------------

    animation-iteration-count: 0;
    

    animation-iteration-count: 2;
    

    animation-iteration-count: 1.5;
    

    <section class="flex-column" id="default-example">
      <div>Animation <span id="play-status"></span></div>
      <div id="example-element">Select a count to start!</div>
    </section>
    

    #example-element {
      align-items: center;
      background-color: #1766aa;
      border-radius: 50%;
      border: 5px solid #333333;
      color: white;
      display: flex;
      flex-direction: column;
      height: 150px;
      justify-content: center;
      margin: auto;
      margin-left: 0;
      width: 150px;
    }
    
    #play-status {
      font-weight: bold;
    }
    
    .animating {
      animation-name: slide;
      animation-duration: 3s;
      animation-timing-function: ease-in;
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#syntax)

-----------------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    animation-iteration-count: infinite;
    
    /* <number> values */
    animation-iteration-count: 3;
    animation-iteration-count: 2.4;
    
    /* Multiple values */
    animation-iteration-count: 2, 0, infinite;
    
    /* Global values */
    animation-iteration-count: inherit;
    animation-iteration-count: initial;
    animation-iteration-count: revert;
    animation-iteration-count: revert-layer;
    animation-iteration-count: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#values)

This property is specified as one or more comma-separated values:

[`infinite`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#infinite)

The animation will repeat forever.

[`<number>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)

The number of times the animation will repeat; this is `1` by default. You may specify non-integer values to play part of an animation cycle: for example, `0.5` will play half of the animation cycle. Negative values are invalid.

**Note:** When you specify multiple comma-separated values on an `animation-*` property, they are applied to the animations in the order in which the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
s appear. For situations where the number of animations and `animation-*` property values do not match, see [Setting multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
.

**Note:** When creating [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
, specifying an `animation-iteration-count` causes the animation to repeat that number of times over the course of the timeline's progression. If an `animation-iteration-count` is not provided, the animation will only occur once. `infinite` is a valid value for scroll-driven animations, but it results in an animation that doesn't work.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `1` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------------

animation-iteration-count =   
  <single-animation-iteration-count>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<single-animation-iteration-count> =   
  infinite        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<number \[0,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#examples)

---------------------------------------------------------------------------------------------------------------------

### [Setting iteration count](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#setting_iteration_count)

This animation will run 10 times.

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
      animation-iteration-count: 10;
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
 for examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Animations Level 1  <br>\# animation-iteration-count](https://drafts.csswg.org/css-animations/#animation-iteration-count) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   JavaScript [`AnimationEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent)
     API
*   Other related animation properties: [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    , [`animation-composition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition)
    , [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
    , [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
    , [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
    , [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
    , [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    , [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
    , [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    , [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-iteration-count/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-iteration-count (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-iteration-count&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-iteration-count%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-iteration-count%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-iteration-count%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")