*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#mdn-search)
    

`animation-timing-function` CSS property
========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation-timing-function`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how an animation progresses through the duration of each cycle.

It is often convenient to use the shorthand property [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
 to set all animation properties at once.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#try_it)

-----------------------------------------------------------------------------------------------------------------

    animation-timing-function: linear;
    

    animation-timing-function: ease-in-out;
    

    animation-timing-function: steps(5, end);
    

    animation-timing-function: cubic-bezier(0.1, -0.6, 0.2, 0);
    

    <section class="flex-column" id="default-example">
      <div class="animating" id="example-element"></div>
      <button id="play-pause">Play</button>
    </section>
    

    #example-element {
      animation-duration: 3s;
      animation-iteration-count: infinite;
      animation-name: slide;
      animation-play-state: paused;
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#syntax)

-----------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    animation-timing-function: ease;
    animation-timing-function: ease-in;
    animation-timing-function: ease-out;
    animation-timing-function: ease-in-out;
    animation-timing-function: linear;
    animation-timing-function: step-start;
    animation-timing-function: step-end;
    
    /* cubic-bezier() function values */
    animation-timing-function: cubic-bezier(0.42, 0, 1, 1); /* ease-in */
    animation-timing-function: cubic-bezier(0, 0, 0.58, 1); /* ease-out */
    animation-timing-function: cubic-bezier(0.42, 0, 0.58, 1); /* ease-in-out */
    
    /* linear() function values */
    animation-timing-function: linear(0, 0.25, 1);
    animation-timing-function: linear(0 0%, 0.25 50%, 1 100%);
    animation-timing-function: linear(0, 0.25 50% 75%, 1);
    animation-timing-function: linear(0, 0.25 50%, 0.25 75%, 1);
    
    /* steps() function values */
    animation-timing-function: steps(4, jump-start);
    animation-timing-function: steps(10, jump-end);
    animation-timing-function: steps(20, jump-none);
    animation-timing-function: steps(5, jump-both);
    animation-timing-function: steps(6, start);
    animation-timing-function: steps(8, end);
    
    /* Multiple animations */
    animation-timing-function: ease, step-start, cubic-bezier(0.1, 0.7, 1, 0.1);
    
    /* Global values */
    animation-timing-function: inherit;
    animation-timing-function: initial;
    animation-timing-function: revert;
    animation-timing-function: revert-layer;
    animation-timing-function: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#values)

[`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)

The easing function that corresponds to a given animation, as determined by [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
.

The non-step keyword values (`ease`, `linear`, `ease-in-out`, etc.) each represent cubic Bézier curves with fixed four-point values, while the `cubic-bezier()` function value allows non-predefined values to be specified. The `steps()` easing function divides the input time into a specified number of equal-length intervals. Its parameters include a number of steps and a step position.

[`linear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#linear)

Equal to `cubic-bezier(0.0, 0.0, 1.0, 1.0)`, animates at an even speed.

[`ease`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#ease)

Equal to `cubic-bezier(0.25, 0.1, 0.25, 1.0)`, the default value, increases in velocity towards the middle of the animation, slowing back down at the end.

[`ease-in`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#ease-in)

Equal to `cubic-bezier(0.42, 0, 1.0, 1.0)`, starts off slowly, with the speed of the transition of the animating property increasing until complete.

[`ease-out`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#ease-out)

Equal to `cubic-bezier(0, 0, 0.58, 1.0)`, starts quickly, slowing down the animation continues.

[`ease-in-out`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#ease-in-out)

Equal to `cubic-bezier(0.42, 0, 0.58, 1.0)`, with the animating properties slowly transitioning, speeding up, and then slowing down again.

[`cubic-bezier(<number [0,1]> , <number> , <number [0,1]> , <number>)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#cubic-beziernumber_01_number_number_01_number)

An author defined cubic-bezier curve, where the first and third values must be in the range of 0 to 1.

[`linear(<number> <percentage>{1,2}, …)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#linearnumber_percentage12_%E2%80%A6)

The function interpolates linearly between the provided easing stop points. A stop point is a pair of an output progress and an input percentage. The input percentage is optional and is inferred if not specified. If an input percentage is not provided then the first and last stop points are set to `0%` and `100%` respectively, and the stop points in the middle receive percentage values derived by linearly interpolating between the closest previous and next points that have a percentage value.

[`steps(<integer>, <step-position>)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#stepsinteger_step-position)

Displays an animation iteration along _n_ stops along the transition, displaying each stop for equal lengths of time. For example, if _n_ is 5, there are 5 steps. Whether the animation holds temporarily at 0%, 20%, 40%, 60% and 80%, on the 20%, 40%, 60%, 80% and 100%, or makes 5 stops between the 0% and 100% along the animation, or makes 5 stops including the 0% and 100% marks (on the 0%, 25%, 50%, 75%, and 100%) depends on which of the following step position is used:

[`jump-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#jump-start)

Denotes a left-continuous function, so that the first jump happens when the animation begins.

[`jump-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#jump-end)

Denotes a right-continuous function, so that the last jump happens when the animation ends. This is the default.

[`jump-none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#jump-none)

There is no jump on either end, effectively removing a step during the interpolation iteration. Instead, it holds at both the 0% mark and the 100% mark, each for 1/n of the duration.

[`jump-both`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#jump-both)

Includes pauses at both the 0% and 100% marks, effectively adding a step during the animation iteration.

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#start)

Same as `jump-start`.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#end)

Same as `jump-end`.

[`step-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#step-start)

Equal to `steps(1, jump-start)`

[`step-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#step-end)

Equal to `steps(1, jump-end)`

**Note:** When you specify multiple comma-separated values on an `animation-*` property, they are applied to the animations in the order in which the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
s appear. For situations where the number of animations and `animation-*` property values do not match, see [Setting multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
.

**Note:** `animation-timing-function` has the same effect when creating [CSS scroll-driven animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations)
 as it does for regular time-based animations.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#description)

---------------------------------------------------------------------------------------------------------------------------

Easing functions may be specified on individual keyframes in a [`@keyframes`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@keyframes)
 rule. If no **`animation-timing-function`** is specified on a keyframe, the corresponding value of **`animation-timing-function`** from the element to which the animation is applied is used for that keyframe.

Within a keyframe, `animation-timing-function` is an at-rule-specific descriptor, not the property of the same name. The timing is not being animated. Rather, a keyframe's easing function is applied on a property-by-property basis from the keyframe on which it is specified until the next keyframe specifying that property, or until the end of the animation if there is no subsequent keyframe specifying that property. As a result, an **`animation-timing-function`** specified on the **`100%`** or **`to`** keyframe will never be used.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `ease` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------------

animation-timing-function =   
  <easing-function>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
[<easing-function>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 =   
  <linear-easing-function>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cubic-bezier-easing-function>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <step-easing-function>            
  
<linear-easing-function> =   
  linear      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <linear()>    
  
<cubic-bezier-easing-function> =   
  ease              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ease-in           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ease-out          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ease-in-out       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cubic-bezier()>    
  
<step-easing-function> =   
  step-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  step-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <steps()>     
  
[<linear()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/linear)
 =   
  linear( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [&&](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_ampersand "Double ampersand: all of the entities must be present, in any order")\
 [<percentage>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)\
[{0,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
 )    
  
[<cubic-bezier()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/cubic-bezier)
 =   
  cubic-bezier( [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<number \[0,1\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 , [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
 )    
  
[<steps()>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function/steps)
 =   
  steps( <integer> , <step-position>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 )    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    
  
<step-position> =   
  jump-start  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jump-end    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jump-none   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  jump-both   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  start       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  end           

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#examples)

---------------------------------------------------------------------------------------------------------------------

All the examples in this section animate the `width` and `background-color` properties of several `<div>` elements with different `animation-timing-function` values. The width is being animated from `0` to `100%`, and the background color is being animated from lime to magenta.

### [Linear function examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#linear_function_examples)

The example demonstrates the effects of various `linear()` easing function values.

    <div class="parent">
      <div class="linear">'linear' value</div>
      <div class="linear-fn1">linear(0, 0.5 50%, 1)</div>
      <div class="linear-fn2">linear(0, 0.25 75%, 1)</div>
      <div class="linear-fn3">linear(0, 0.75 25%, 1)</div>
      <div class="linear-fn4">linear(0, 0.5 25% 75%, 1)</div>
      <div class="linear-fn5">linear(0, 0.25 45%, 0.75 55%, 0.5 70%, 1)</div>
      <div class="linear-fn6">linear(0, 1.2 50%, 0.75 80%, 1)</div>
      <div class="linear-fn7">linear(0, 0.5 75%, 1 120%)</div>
    </div>
    <div class="x-axis"><span>25%</span><span>50%</span><span>75%</span></div>
    <button>Play animation</button>
    

    const btn = document.querySelector("button");
    const divs = document.querySelectorAll(".parent > div[class]");
    
    btn.addEventListener("click", () => {
      btn.setAttribute("disabled", "true");
      for (const div of divs) {
        div.classList.remove("animate");
        void div.offsetWidth;
        div.classList.add("animate");
      }
      setTimeout(() => {
        btn.removeAttribute("disabled");
      }, 11000);
    });
    

    .x-axis {
      display: flex;
      justify-content: space-evenly;
      width: 80vw;
      margin-left: 4px;
    }
    
    .parent {
      background: linear-gradient(
        to right,
        white 24.8%,
        grey 24.8%,
        grey 25.2%,
        white 25.2%,
        white 49.8%,
        grey 49.8%,
        grey 50.2%,
        white 50.2%,
        white 74.8%,
        grey 74.8%,
        grey 75.2%,
        white 75.2%
      );
      width: 80vw;
      font-family: monospace;
      font-weight: bold;
      border: 2px solid grey;
    }
    
    .animate {
      animation-name: changeme;
    }
    
    .parent > div[class] {
      animation-fill-mode: forwards;
      animation-duration: 10s;
    
      width: 0;
      margin-bottom: 4px;
      padding: 5px 0;
      box-sizing: border-box;
      text-wrap: nowrap;
      background-color: lime;
    }
    
    @keyframes changeme {
      0% {
        width: 0em;
      }
      100% {
        width: 100%;
        background-color: orange;
      }
    }
    
    .linear {
      animation-timing-function: linear;
    }
    .linear-fn1 {
      animation-timing-function: linear(0, 0.5 50%, 1);
    }
    .linear-fn2 {
      animation-timing-function: linear(0, 0.25 75%, 1);
    }
    .linear-fn3 {
      animation-timing-function: linear(0, 0.75 25%, 1);
    }
    .linear-fn4 {
      animation-timing-function: linear(0, 0.5 25% 75%, 1);
    }
    .linear-fn5 {
      animation-timing-function: linear(0, 0.25 45%, 0.75 55%, 0.5 70%, 1);
    }
    .linear-fn6 {
      animation-timing-function: linear(0, 1.2 50%, 0.75 80%, 1);
    }
    .linear-fn7 {
      animation-timing-function: linear(0, 0.5 75%, 1 120%);
    }
    

The following image shows graphs of all the `linear()` function values used in this example. Input progress (time) is plotted on the x-axis and output progress is plotted on the y-axis. As per the syntax, the input progress ranges from 0 to 100%, and the output ranges from 0 to 1.

![An image showing 'linear' function graphs](https://mdn.github.io/shared-assets/images/diagrams/css/animation-easing/linear-function-graphs.png)

Note that the output can go forward or backward.

### [Cubic-Bézier examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#cubic-b%C3%A9zier_examples)

The example demonstrates the effects of various bézier curve easing functions.

    <div class="parent">
      <div class="linear">linear</div>
      <div class="ease">ease</div>
      <div class="ease-in">ease-in</div>
      <div class="ease-out">ease-out</div>
      <div class="ease-in-out">ease-in-out</div>
      <div class="cb">cubic-bezier(.5, -0.5, 1, 1.5)</div>
    </div>
    <div class="x-axis"><span>50%</span></div>
    <button>Play animation</button>
    

    const btn = document.querySelector("button");
    const divs = document.querySelectorAll(".parent > div[class]");
    
    btn.addEventListener("click", () => {
      btn.setAttribute("disabled", "true");
      for (const div of divs) {
        div.classList.remove("animate");
        void div.offsetWidth;
        div.classList.add("animate");
      }
      setTimeout(() => {
        btn.removeAttribute("disabled");
      }, 11000);
    });
    

    .x-axis {
      display: flex;
      justify-content: space-evenly;
      width: 80vw;
      margin-left: 4px;
    }
    
    .parent {
      background: linear-gradient(
        to right,
        white 49.8%,
        grey 49.8%,
        grey 50.2%,
        white 50.2%
      );
      width: 80vw;
      font-family: monospace;
      font-weight: bold;
      border: 2px solid grey;
    }
    
    .animate {
      animation-name: changeme;
    }
    
    .parent > div[class] {
      animation-fill-mode: forwards;
      animation-duration: 10s;
    
      width: 0;
      margin-bottom: 4px;
      padding: 5px 0;
      box-sizing: border-box;
      text-wrap: nowrap;
      background-color: lime;
    }
    
    @keyframes changeme {
      0% {
        width: 0em;
      }
      100% {
        width: 100%;
        background-color: orange;
      }
    }
    
    .linear {
      animation-timing-function: linear;
    }
    .ease {
      animation-timing-function: ease;
    }
    .ease-in {
      animation-timing-function: ease-in;
    }
    .ease-out {
      animation-timing-function: ease-out;
    }
    .ease-in-out {
      animation-timing-function: ease-in-out;
    }
    .cb {
      animation-timing-function: cubic-bezier(0.5, -0.5, 1, 1.5);
    }
    

The following image shows graphs of all the cubic bézier function values used in this example. The input progress (time) ranges from 0 to 1 and the output progress ranges from 0 to 1.

![An image showing 'cubic-bezier' function graphs](https://mdn.github.io/shared-assets/images/diagrams/css/animation-easing/cubic-bezier-function-graphs.png)

### [Step examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#step_examples)

This example demonstrates the effects of several step easing function values.

    <div class="parent">
      <div class="linear">linear</div>
      <div class="start">steps(4, start)</div>
      <div class="jump-start">steps(4, jump-start)</div>
      <div class="end">steps(4, end)</div>
      <div class="jump-end">steps(4, jump-end)</div>
      <div class="jump-both">steps(4, jump-both)</div>
      <div class="jump-none">steps(4, jump-none)</div>
      <div class="step-start">step-start</div>
      <div class="step-end">step-end</div>
    </div>
    <div class="x-axis"><span>25%</span><span>50%</span><span>75%</span></div>
    <button>Play animation</button>
    

    const btn = document.querySelector("button");
    const divs = document.querySelectorAll(".parent > div[class]");
    
    btn.addEventListener("click", () => {
      btn.setAttribute("disabled", "true");
      for (const div of divs) {
        div.classList.remove("animate");
        void div.offsetWidth;
        div.classList.add("animate");
      }
      setTimeout(() => {
        btn.removeAttribute("disabled");
      }, 11000);
    });
    

    .x-axis {
      display: flex;
      justify-content: space-evenly;
      width: 80vw;
      margin-left: 4px;
    }
    
    .parent {
      background: linear-gradient(
        to right,
        white 24.8%,
        grey 24.8%,
        grey 25.2%,
        white 25.2%,
        white 49.8%,
        grey 49.8%,
        grey 50.2%,
        white 50.2%,
        white 74.8%,
        grey 74.8%,
        grey 75.2%,
        white 75.2%
      );
      width: 80vw;
      font-family: monospace;
      font-weight: bold;
      border: 2px solid grey;
    }
    
    .animate {
      animation-name: changeme;
    }
    
    .parent > div[class] {
      animation-fill-mode: forwards;
      animation-duration: 10s;
    
      width: 0;
      margin-bottom: 4px;
      padding: 5px 0;
      box-sizing: border-box;
      text-wrap: nowrap;
      background-color: lime;
    }
    
    @keyframes changeme {
      0% {
        width: 0em;
      }
      100% {
        width: 100%;
        background-color: orange;
      }
    }
    

    .linear {
      animation-timing-function: linear;
    }
    
    .start {
      animation-timing-function: steps(4, start);
    }
    .jump-start {
      animation-timing-function: steps(4, jump-start);
    }
    .end {
      animation-timing-function: steps(4, end);
    }
    .jump-end {
      animation-timing-function: steps(4, jump-end);
    }
    .jump-both {
      animation-timing-function: steps(4, jump-both);
    }
    .jump-none {
      animation-timing-function: steps(4, jump-none);
    }
    .step-start {
      animation-timing-function: step-start;
    }
    .step-end {
      animation-timing-function: step-end;
    }
    

The following image shows graphs of all the `step()` function values used in this example. The input progress (time) and output progress range from 0 to 1.

![image showing 'steps' function graphs](https://mdn.github.io/shared-assets/images/diagrams/css/animation-easing/step-function-graphs.png)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#specifications)

---------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Animations Level 1  <br>\# animation-timing-function](https://drafts.csswg.org/css-animations/#animation-timing-function) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   [`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
    
*   [CSS easing functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Easing_functions)
     module
*   JavaScript [`AnimationEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent)
     API
*   [Cubic bézier generation tool](https://cubic-bezier.com/ "External link (opens in new tab)")
    
*   Other related animation properties: [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    , [`animation-composition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition)
    , [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
    , [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
    , [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
    , [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
    , [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
    , [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    , [`animation-play-state`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state)
    , [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-timing-function/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-timing-function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-timing-function&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-timing-function%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-timing-function%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-timing-function%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")