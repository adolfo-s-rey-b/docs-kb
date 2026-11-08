*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#mdn-search)
    

`animation-play-state` CSS property
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`animation-play-state`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets whether an animation is running or paused.

Resuming a paused animation will start the animation from where it left off at the time it was paused, rather than starting over from the beginning of the animation sequence.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#try_it)

------------------------------------------------------------------------------------------------------------

    animation-play-state: paused;
    

    animation-play-state: running;
    

    <section class="flex-column" id="default-example">
      <div class="animating" id="example-element"></div>
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
    }
    
    .animating {
      animation-name: slide;
      animation-duration: 3s;
      animation-timing-function: ease-in;
      animation-iteration-count: infinite;
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#syntax)

------------------------------------------------------------------------------------------------------------

css

    /* Single animation */
    animation-play-state: running;
    animation-play-state: paused;
    
    /* Multiple animations */
    animation-play-state: paused, running, running;
    
    /* Global values */
    animation-play-state: inherit;
    animation-play-state: initial;
    animation-play-state: revert;
    animation-play-state: revert-layer;
    animation-play-state: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#values)

This property is specified as a comma-separated list of the following keyword values:

[`running`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#running)

The **animation** is currently **playing**.

[`paused`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#paused)

The **animation** is currently **paused**.

**Note:** When you specify multiple comma-separated values on an `animation-*` property, they are applied to the animations in the order in which the [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
s appear. For situations where the number of animations and `animation-*` property values do not match, see [Setting multiple animation property values](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using#setting_multiple_animation_property_values)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `running` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

animation-play-state =   
  <single-animation-play-state>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<single-animation-play-state> =   
  running  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  paused     

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#examples)

----------------------------------------------------------------------------------------------------------------

### [Pausing an animation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#pausing_an_animation)

This animation is paused, but runs when you hover over it.

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
      animation-name: rotate;
      animation-duration: 0.7s;
      animation-iteration-count: infinite;
      animation-play-state: paused;
    }
    
    .box:hover {
      animation-play-state: running;
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

Hover over the rectangle to play the animation.

See [CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
 for examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Animations Level 1  <br>\# animation-play-state](https://drafts.csswg.org/css-animations/#animation-play-state) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state#see_also)

----------------------------------------------------------------------------------------------------------------

*   [Using CSS animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Using)
    
*   JavaScript [`AnimationEvent`](https://developer.mozilla.org/en-US/docs/Web/API/AnimationEvent)
     API
*   Other related animation properties: [`animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation)
    , [`animation-composition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-composition)
    , [`animation-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-delay)
    , [`animation-direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-direction)
    , [`animation-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-duration)
    , [`animation-fill-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-fill-mode)
    , [`animation-iteration-count`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-iteration-count)
    , [`animation-name`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-name)
    , [`animation-timeline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timeline)
    , [`animation-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-timing-function)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/animation-play-state/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/animation-play-state/index.md?plain=1 "Folder: en-us/web/css/reference/properties/animation-play-state (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-play-state&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-play-state%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fanimation-play-state%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fanimation-play-state%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")