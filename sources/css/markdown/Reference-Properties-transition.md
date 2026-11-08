*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#mdn-search)
    

`transition` CSS property
=========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`transition`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [shorthand](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Shorthand_properties)
 property for [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
, [`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)
, [`transition-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)
, [`transition-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay)
, and [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
.

Transitions enable you to define the transition between two states of an element. Different states may be defined using [pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 like [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
 or [`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)
 or dynamically set using JavaScript.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#try_it)

--------------------------------------------------------------------------------------------------

    transition: margin-right 2s;
    

    transition: margin-right 2s 0.5s;
    

    transition: margin-right 2s ease-in-out;
    

    transition: margin-right 2s ease-in-out 0.5s;
    

    transition:
      margin-right 2s,
      color 1s;
    

    transition: all 1s ease-out;
    

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
    

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#constituent_properties)

----------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following CSS properties:

*   [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)
    
*   [`transition-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay)
    
*   [`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)
    
*   [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)
    
*   [`transition-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#syntax)

--------------------------------------------------------------------------------------------------

css

    /* Apply to 1 property */
    /* property name | duration */
    transition: margin-right 4s;
    
    /* property name | duration | delay */
    transition: margin-right 4s 1s;
    
    /* property name | duration | easing function */
    transition: margin-right 4s ease-in-out;
    
    /* property name | duration | easing function | delay */
    transition: margin-right 4s ease-in-out 1s;
    
    /* property name | duration | behavior */
    transition: display 4s allow-discrete;
    
    /* Apply to 2 properties */
    transition:
      margin-right 4s,
      color 1s;
    
    /* Apply to all changed properties */
    transition: all 0.5s ease-out allow-discrete;
    transition: 200ms linear 50ms;
    
    /* Global values */
    transition: inherit;
    transition: initial;
    transition: revert;
    transition: revert-layer;
    transition: unset;
    

The `transition` property value is specified as one of the following:

*   The special value `none`, which specifies that no transitions will occur on this element. This is the default value.
*   One or more single-property transitions, separated by commas.

Each single-property transition describes the transition that should be applied to a single property or all properties. It includes:

*   zero or one value representing the property or properties to which the transition should apply. This can be set as:
    *   A [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
         representing a single property.
    *   The special value `all`, which specifies that the transition will be applied to all properties that change as the element changes state.
    *   No value, in which case a value of `all` will be inferred and the specified transition will still apply to all changing properties.
*   zero or one [`<easing-function>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
     value representing the easing function to use
*   zero, one, or two [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
     values. The first value that can be parsed as a time is assigned to the [`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)
    , and the second value that can be parsed as a time is assigned to [`transition-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay)
    .
*   zero or one value declaring whether to start transitions for properties whose animation behavior is [discrete](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties#discrete)
    . The value, if present, is either the keyword `allow-discrete` or the keyword `normal`.

If you specify `all` as the transition property for one single-property transition, but then specify subsequent single-property transitions with [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 values, those subsequent transitions will override the first one. For example:

css

    transition:
      all 200ms,
      opacity 400ms;
    

In this case, all the properties that change as the element changes state will transition with a duration of 200ms except for [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
, which will take 400ms to transition.

See [how things are handled](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using#when_property_value_lists_are_of_different_lengths)
 when lists of property values aren't the same length. In short, extra transition descriptions beyond the number of properties actually being animated are ignored.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`transition-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay)<br>    : `0s`<br>*   [`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)<br>    : `0s`<br>*   [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)<br>    : `all`<br>*   [`transition-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)<br>    : `ease`<br>*   [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)<br>    : `normal` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`transition-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay)<br>    : as specified<br>*   [`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)<br>    : as specified<br>*   [`transition-property`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property)<br>    : as specified<br>*   [`transition-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)<br>    : as specified<br>*   [`transition-behavior`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-behavior)<br>    : as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#formal_syntax)

----------------------------------------------------------------------------------------------------------------

transition =   
  <single-transition>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<single-transition> =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 none [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <single-transition-property> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
  [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<time>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
                                   [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <easing-function>                        [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  [<time>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
                                   [||](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#double_bar "Double bar: one or several of the entities must be present, in any order")
  
  <transition-behavior-value>                
  
<single-transition-property> =   
  all             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    
  
[<easing-function>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/easing-function)
 =   
  <linear-easing-function>        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <cubic-bezier-easing-function>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <step-easing-function>            
  
<transition-behavior-value> =   
  normal          [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  allow-discrete    
  
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

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#examples)

------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#basic_example)

In this example, when the user hovers over the element, there is a half-second (`500ms`) delay before a two-second `background-color` transition occurs.

#### HTML

html

    <a class="target">Hover over me</a>
    

#### CSS

We include two [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
 values. In the `transition` shorthand, the first `<time>` value is the `transition-duration`. The second time value is the `transition-delay`. Both default to `0s` if omitted.

css

    .target {
      font-size: 2rem;
      background-color: palegoldenrod;
      transition: background-color 2s 500ms;
    }
    
    .target:hover {
      background-color: darkorange;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transitions Module Level 1  <br>\# transition-shorthand-property](https://drafts.csswg.org/css-transitions/#transition-shorthand-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#see_also)

------------------------------------------------------------------------------------------------------

*   [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
     module
*   [Using CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)
    
*   [`TransitionEvent`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/transition/index.md?plain=1 "Folder: en-us/web/css/reference/properties/transition (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")