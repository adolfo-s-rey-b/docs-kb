*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#mdn-search)
    

`transition-duration` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`transition-duration`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the length of time a transition animation should take to complete. By default, the value is `0s`, meaning that no animation will occur.

You may specify multiple durations; each duration will be applied to the corresponding property as specified by the [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
 property, which acts as a master list. If the number of specified durations is less than in the master list, the user agent repeats the list of durations. If the number of specified durations is more than in the master list, the list is truncated to the right size. In both the cases, the CSS declaration stays valid.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#try_it)

-----------------------------------------------------------------------------------------------------------

    transition-duration: 500ms;
    transition-property: margin-right;
    

    transition-duration: 2s;
    transition-property: background-color;
    

    transition-duration: 2s;
    transition-property: margin-right, color;
    

    transition-duration: 3s, 1s;
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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* <time> values */
    transition-duration: 6s;
    transition-duration: 120ms;
    transition-duration: 1s, 15s;
    transition-duration: 10s, 30s, 230ms;
    
    /* Global values */
    transition-duration: inherit;
    transition-duration: initial;
    transition-duration: revert;
    transition-duration: revert-layer;
    transition-duration: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#values)

[`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#time)

Is a [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
 denoting the amount of time the transition from the old value of a property to the new value should take. A time of `0s` indicates that no transition will happen, that is the switch between the two states will be instantaneous. A negative value for the time renders the declaration invalid.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `0s` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

transition-duration =   
  [<time \[0s,∞\]>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#examples)

---------------------------------------------------------------------------------------------------------------

### [Example showing different durations](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#example_showing_different_durations)

#### HTML

html

    <div class="box duration-1">0.5 seconds</div>
    
    <div class="box duration-2">2 seconds</div>
    
    <div class="box duration-3">4 seconds</div>
    
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
    }
    
    .transformed-state {
      transform: rotate(270deg);
      background-color: blue;
      color: yellow;
      font-size: 12px;
      transition-property: background-color, font-size, transform, color;
      transition-timing-function: ease-in-out;
    }
    
    .duration-1 {
      transition-duration: 0.5s;
    }
    
    .duration-2 {
      transition-duration: 2s;
    }
    
    .duration-3 {
      transition-duration: 4s;
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

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transitions Module Level 1  <br>\# transition-duration-property](https://drafts.csswg.org/css-transitions/#transition-duration-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Using CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)
    
*   [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
    
*   [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
    
*   [`transition-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)
    
*   [`transition-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay)
    
*   [`TransitionEvent`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/transition-duration/index.md?plain=1 "Folder: en-us/web/css/reference/properties/transition-duration (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition-duration&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition-duration%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition-duration%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition-duration%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")