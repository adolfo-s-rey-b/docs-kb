*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#mdn-search)
    

`transition-delay` CSS property
===============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`transition-delay`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the duration to wait before starting a property's [transition effect](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)
 when its value changes.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#try_it)

--------------------------------------------------------------------------------------------------------

    transition-delay: 250ms;
    transition-property: margin-right;
    

    transition-delay: 1s;
    transition-property: background-color;
    

    transition-delay: 1s;
    transition-property: margin-right, color;
    

    transition-delay: 1s, 250ms;
    transition-property: margin-right, color;
    

    <section id="default-example">
      <div id="example-element">Hover to see<br />the transition.</div>
    </section>
    

    #example-element {
      background-color: #e4f0f5;
      color: black;
      padding: 1rem;
      border-radius: 0.5rem;
      font: 1em monospace;
      width: 100%;
      transition: margin-right 2s;
    }
    
    #default-example:hover > #example-element {
      background-color: #990099;
      color: white;
      margin-right: 40%;
    }
    

The delay may be zero, positive, or negative:

*   A value of `0s` (or `0ms`) will begin the transition effect immediately.
*   A positive value will delay the start of the transition effect for the given length of time.
*   A negative value will begin the transition effect immediately, and partway through the effect. In other words, the effect will be animated as if it had already been running for the given length of time.

You may specify multiple delays, which is useful when transitioning multiple properties. Each delay will be applied to the corresponding property as specified by the [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
 property, which acts as a master list. If there are fewer delays specified than in the master list, the list of delay values will be repeated until there are enough. If there are more delays, the list of delay values will be truncated to match the number of properties. In both cases, the CSS declaration remains valid.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#syntax)

--------------------------------------------------------------------------------------------------------

css

    /* <time> values */
    transition-delay: 3s;
    transition-delay: 2s, 4ms;
    
    /* Global values */
    transition-delay: inherit;
    transition-delay: initial;
    transition-delay: revert;
    transition-delay: revert-layer;
    transition-delay: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#values)

[`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)

Denotes the amount of time to wait between a property's value changing and the start of the transition effect.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#formal_definition)

------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0s` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#formal_syntax)

----------------------------------------------------------------------------------------------------------------------

transition-delay =   
  [<time>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#examples)

------------------------------------------------------------------------------------------------------------

### [Example showing different delays](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#example_showing_different_delays)

#### HTML

html

    <div class="box delay-1">0.5 seconds</div>
    
    <div class="box delay-2">2 seconds</div>
    
    <div class="box delay-3">4 seconds</div>
    
    <button id="change">Change</button>
    

#### CSS

css

    .box {
      margin: 20px;
      padding: 10px;
      display: inline-block;
      width: 100px;
      height: 100px;
      background-color: red;
      font-size: 18px;
      transition-property: background-color, font-size, transform, color;
      transition-timing-function: ease-in-out;
      transition-duration: 3s;
    }
    
    .transformed-state {
      transform: rotate(270deg);
      background-color: blue;
      color: yellow;
      font-size: 12px;
      transition-property: background-color, font-size, transform, color;
      transition-timing-function: ease-in-out;
      transition-duration: 3s;
    }
    
    .delay-1 {
      transition-delay: 0.5s;
    }
    
    .delay-2 {
      transition-delay: 2s;
    }
    
    .delay-3 {
      transition-delay: 4s;
    }
    

#### JavaScript

js

    function change() {
      const elements = document.querySelectorAll("div.box");
      for (const element of elements) {
        element.classList.toggle("transformed-state");
      }
    }
    
    const changeButton = document.querySelector("#change");
    changeButton.addEventListener("click", change);
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#specifications)

------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transitions Module Level 1  <br>\# transition-delay-property](https://drafts.csswg.org/css-transitions/#transition-delay-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay#see_also)

------------------------------------------------------------------------------------------------------------

*   [Using CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)
    
*   [`TransitionEvent`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent)
     API

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/transition-delay/index.md?plain=1 "Folder: en-us/web/css/reference/properties/transition-delay (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition-delay&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition-delay%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition-delay%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition-delay%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")