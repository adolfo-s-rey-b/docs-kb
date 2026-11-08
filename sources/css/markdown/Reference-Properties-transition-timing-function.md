*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#mdn-search)
    

`transition-timing-function` CSS property
=========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`transition-timing-function`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets how intermediate values are calculated for CSS properties being affected by a [transition effect](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#try_it)

------------------------------------------------------------------------------------------------------------------

    transition-timing-function: linear;
    

    transition-timing-function: ease-in;
    

    transition-timing-function: steps(6, end);
    

    transition-timing-function: cubic-bezier(0.29, 1.01, 1, -0.68);
    

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
    

This, in essence, lets you establish an acceleration curve so that the speed of the transition can vary over its duration.

This acceleration curve is defined using one [`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 for each property to be transitioned.

You may specify multiple easing functions; each one will be applied to the corresponding property as specified by the [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
 property, which acts as a `transition-property` list. If there are fewer easing functions specified than in the `transition-property` list, the user agent must calculate which value is used by repeating the list of values until there is one for each transition property. If there are more easing functions, the list is truncated to the right size. In both cases, the CSS declaration stays valid.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#syntax)

------------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    transition-timing-function: ease;
    transition-timing-function: ease-in;
    transition-timing-function: ease-out;
    transition-timing-function: ease-in-out;
    transition-timing-function: linear;
    transition-timing-function: step-start;
    transition-timing-function: step-end;
    
    /* Function values */
    transition-timing-function: steps(4, jump-end);
    transition-timing-function: cubic-bezier(0.1, 0.7, 1, 0.1);
    
    /* Steps Function keywords */
    transition-timing-function: steps(4, jump-start);
    transition-timing-function: steps(10, jump-end);
    transition-timing-function: steps(20, jump-none);
    transition-timing-function: steps(5, jump-both);
    transition-timing-function: steps(6, start);
    transition-timing-function: steps(8, end);
    
    /* Multiple easing functions */
    transition-timing-function: ease, step-start, cubic-bezier(0.1, 0.7, 1, 0.1);
    
    /* Global values */
    transition-timing-function: inherit;
    transition-timing-function: initial;
    transition-timing-function: revert;
    transition-timing-function: revert-layer;
    transition-timing-function: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#values)

[`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#easing-function)

Each [`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 represents the easing function to link to the corresponding property to transition, as defined in [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
.

The non-step keyword values (ease, linear, ease-in-out, etc.) each represent cubic Bézier curve with fixed four point values, with the cubic-bezier() function value allowing for a non-predefined value. The step easing functions divide the input time into a specified number of intervals that are equal in length. It is defined by a number of steps and a step position.

[`ease`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#ease)

Equal to `cubic-bezier(0.25, 0.1, 0.25, 1.0)`, the default value, increases in velocity towards the middle of the transition, slowing back down at the end.

[`linear`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#linear)

Equal to `cubic-bezier(0.0, 0.0, 1.0, 1.0)`, transitions at an even speed.

[`ease-in`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#ease-in)

Equal to `cubic-bezier(0.42, 0, 1.0, 1.0)`, starts off slowly, with the transition speed increasing until complete.

[`ease-out`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#ease-out)

Equal to `cubic-bezier(0, 0, 0.58, 1.0)`, starts transitioning quickly, slowing down as the transition continues.

[`ease-in-out`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#ease-in-out)

Equal to `cubic-bezier(0.42, 0, 0.58, 1.0)`, starts transitioning slowly, speeds up, and then slows down again.

[`cubic-bezier(p1, p2, p3, p4)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#cubic-bezierp1_p2_p3_p4)

An author-defined cubic-Bezier curve, where the p1 and p3 values must be in the range of 0 to 1.

[`steps(n, <jump-term>)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#stepsn_jump-term)

Displays the transition along _n stops along the transition, displaying each stop for_ equal lengths of time. For example, if _n_ is 5, there are 5 steps. Whether the transition holds temporarily at 0%, 20%, 40%, 60% and 80%, on the 20%, 40%, 60%, 80% and 100%, or makes 5 stops between the 0% and 100% along the transition, or makes 5 stops including the 0% and 100% marks (on the 0%, 25%, 50%, 75%, and 100%) depends on which of the following jump terms is used:

[`jump-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#jump-start)

Denotes a left-continuous function, so that the first jump happens when the transition begins;

[`jump-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#jump-end)

Denotes a right-continuous function, so that the last jump happens when the animation ends;

[`jump-none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#jump-none)

There is no jump on either end. Instead, holding at both the 0% mark and the 100% mark, each for 1/n of the duration

[`jump-both`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#jump-both)

Includes pauses at both the 0% and 100% marks, effectively adding a step during the transition time.

[`start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#start)

Same as `jump-start`.

[`end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#end)

Same as `jump-end`.

[`step-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#step-start)

Equal to `steps(1, jump-start)`

[`step-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#step-end)

Equal to `steps(1, jump-end)`

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#accessibility)

--------------------------------------------------------------------------------------------------------------------------------

Some animations can be helpful such as to guide users to understand what actions are expected, to show relationships within the user interface, and to inform users as to what actions have occurred. Animations can help reduce cognitive load, prevent change blindness, and establish better recall in spatial relationships. However, some animations can be problematic for people with cognitive concerns such as Attention Deficit Hyperactivity Disorder (ADHD) and certain kinds of motion can be a trigger for Vestibular disorders, epilepsy, and migraine and Scotopic sensitivity.

Consider providing a mechanism for pausing or disabling animation, as well as using the [Reduced Motion Media Query](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-reduced-motion)
 (or equivalent [User Agent client hint](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Client_hints#user_agent_client_hints)
 [`Sec-CH-Prefers-Reduced-Motion`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Sec-CH-Prefers-Reduced-Motion)
) to create a complementary experience for users who have expressed a preference for less animation.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `ease` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------------

transition-timing-function =   
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#examples)

----------------------------------------------------------------------------------------------------------------------

### [Cubic-Bezier examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#cubic-bezier_examples)

    <div class="parent">
      <div class="ease">ease</div>
      <div class="ease-in">ease-in</div>
      <div class="ease-out">ease-out</div>
      <div class="ease-in-out">ease-in-out</div>
      <div class="linear">linear</div>
      <div class="cb">cubic-bezier(0.2,-2,0.8,2)</div>
    </div>
    

    .parent {
    }
    .parent > div[class] {
      width: 12em;
      min-width: 12em;
      margin-bottom: 4px;
      background-color: black;
      border: 1px solid red;
      color: white;
      transition-property: all;
      transition-duration: 7s;
    }
    .parent > div.box1 {
      width: 90vw;
      min-width: 24em;
      background-color: magenta;
      color: yellow;
      border: 1px solid orange;
      transition-property: all;
      transition-duration: 2s;
    }
    

    function updateTransition() {
      const els = document.querySelectorAll(".parent > div[class]");
      for (const el of els) {
        el.classList.toggle("box1");
      }
    }
    
    const intervalID = setInterval(updateTransition, 10000);
    

css

    .ease {
      transition-timing-function: ease;
    }
    .ease-in {
      transition-timing-function: ease-in;
    }
    .ease-out {
      transition-timing-function: ease-out;
    }
    .ease-in-out {
      transition-timing-function: ease-in-out;
    }
    .linear {
      transition-timing-function: linear;
    }
    .cb {
      transition-timing-function: cubic-bezier(0.2, -2, 0.8, 2);
    }
    

### [Step examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#step_examples)

    <div class="parent">
      <div class="jump-start">jump-start</div>
      <div class="jump-end">jump-end</div>
      <div class="jump-both">jump-both</div>
      <div class="jump-none">jump-none</div>
      <div class="step-start">step-start</div>
      <div class="step-end">step-end</div>
    </div>
    

    .parent {
    }
    .parent > div[class] {
      width: 12em;
      min-width: 12em;
      margin-bottom: 4px;
      background-color: black;
      border: 1px solid red;
      color: white;
      transition-property: all;
      transition-duration: 7s;
    }
    .parent > div.box1 {
      width: 90vw;
      min-width: 24em;
      background-color: magenta;
      color: yellow;
      border: 1px solid orange;
      transition-property: all;
      transition-duration: 2s;
    }
    

    function updateTransition() {
      const els = document.querySelectorAll(".parent > div[class]");
      for (const el of els) {
        el.classList.toggle("box1");
      }
    }
    
    const intervalID = setInterval(updateTransition, 10000);
    

css

    .jump-start {
      transition-timing-function: steps(5, jump-start);
    }
    .jump-end {
      transition-timing-function: steps(5, jump-end);
    }
    .jump-none {
      transition-timing-function: steps(5, jump-none);
    }
    .jump-both {
      transition-timing-function: steps(5, jump-both);
    }
    .step-start {
      transition-timing-function: step-start;
    }
    .step-end {
      transition-timing-function: step-end;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transitions Module Level 1  <br>\# transition-timing-function-property](https://drafts.csswg.org/css-transitions/#transition-timing-function-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [Using CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)
    
*   [`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
    
*   [CSS easing functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Easing_functions)
     module
*   [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
    
*   [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
    
*   [`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)
    
*   [`transition-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay)
    
*   [`TransitionEvent`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 11, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/transition-timing-function/index.md?plain=1 "Folder: en-us/web/css/reference/properties/transition-timing-function (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition-timing-function&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition-timing-function%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition-timing-function%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition-timing-function%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3064cbe8212ea919874fb21120a89657afccba25%0A*+Document+last+modified%3A+2026-09-11T17%3A16%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")