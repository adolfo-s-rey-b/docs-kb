*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#mdn-search)
    

`animation-delay` CSS property
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation-delay`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the amount of time to wait from applying the animation to an element before beginning to perform the animation. The animation can start later, immediately from its beginning, or immediately and partway through the animation.

It is often convenient to use the shorthand property [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 to set all animation properties at once.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#try_it)

-------------------------------------------------------------------------------------------------------

    animation-delay: 250ms;
    

    animation-delay: 2s;
    

    animation-delay: -2s;
    

    <section class="flex-column" id="default-example">
      <div>Animation <span id="play-status"></span></div>
      <div id="example-element">Select a delay to start!</div>
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
      animation-name: slide;
      animation-duration: 3s;
      animation-timing-function: ease-in;
      animation-iteration-count: 2;
      animation-direction: alternate;
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Single animation */
    animation-delay: 3s;
    animation-delay: 0s;
    animation-delay: -1500ms;
    
    /* Multiple animations */
    animation-delay: 2.1s, 480ms;
    
    /* Global values */
    animation-delay: inherit;
    animation-delay: initial;
    animation-delay: revert;
    animation-delay: revert-layer;
    animation-delay: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#values)

This property is specified as a comma-separated list of `<time>` values:

[`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)

The time offset, from the moment at which the animation is applied to the element, at which the animation should begin. This may be specified in either seconds (`s`) or milliseconds (`ms`). The unit is required.

A positive value indicates that the animation should begin after the specified amount of time has elapsed. A value of `0s`, which is the default, indicates that the animation should begin as soon as it's applied.

A negative value causes the animation to begin immediately, but partway through its cycle. For example, if you specify `-1s` as the animation delay time, the animation will begin immediately but will start 1 second into the animation sequence. If you specify a negative value for the animation delay, but the starting value is implicit, the starting value is taken from the moment the animation is applied to the element.

**Note:** When you specify multiple comma-separated values on an `animation-*` property, they are applied to the animations in the order in which the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
s appear. For situations where the number of animations and `animation-*` property values do not match, see [Setting multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
.

**Note:** `animation-delay` has no effect on [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0s` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

animation-delay =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <'animation-delay-start'> <'animation-delay-end'>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<animation-delay-start> =   
  [<time>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<animation-delay-end> =   
  [<time \[0s,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#examples)

-----------------------------------------------------------------------------------------------------------

### [Setting an animation delay](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#setting_an_animation_delay)

This animation has a delay of 2 seconds.

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
      animation-delay: 2s;
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

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Animations Level 1  <br>\# animation-delay](https://drafts.csswg.org/css-animations/#animation-delay) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay#see_also)

-----------------------------------------------------------------------------------------------------------

*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   JavaScript [`AnimationEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent)
     API
*   Other related animation properties: [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    , [`animation-composition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition)
    , [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
    , [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
    , [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
    , [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
    , [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    , [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
    , [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    , [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-delay/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-delay (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-delay&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-delay%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-delay%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-delay%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")