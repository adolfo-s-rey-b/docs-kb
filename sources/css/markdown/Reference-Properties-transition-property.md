*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#mdn-search)
    

`transition-property` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`transition-property`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the CSS properties to which a [transition effect](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)
 should be applied.

If you specify a shorthand property (e.g., [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
), all of its longhand sub-properties that can be animated will be.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#try_it)

-----------------------------------------------------------------------------------------------------------

    transition-property: margin-right;
    

    transition-property: margin-right, color;
    

    transition-property: all;
    

    transition-property: none;
    

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
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#syntax)

-----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    transition-property: none;
    transition-property: all;
    
    /* <custom-ident> values */
    transition-property: test_05;
    transition-property: -specific;
    transition-property: sliding-vertically;
    
    /* Multiple values */
    transition-property: test1, animation4;
    transition-property: all, height, color;
    transition-property:
      all,
      -moz-specific,
      sliding;
    
    /* Global values */
    transition-property: inherit;
    transition-property: initial;
    transition-property: revert;
    transition-property: revert-layer;
    transition-property: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#values)

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#none)

No properties will transition.

[`all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#all)

All properties that can transition will.

[`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)

A string identifying the property to which a transition effect should be applied when its value changes.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `all` |
| Applies to | all elements, [`::before`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::before)<br> and [`::after`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::after)<br> [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements) |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | Not animatable |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

transition-property =   
  none                           [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <single-transition-property>[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<single-transition-property> =   
  all             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#examples)

---------------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#basic_example)

When the button is hovered or focused, it undergoes a one-second color transition; the `transition-property` is [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
.

#### HTML

html

    <button class="target">Focus me!</button>
    

#### CSS

    html {
      height: 100vh;
    }
    
    button {
      font-size: 1.4rem;
      padding: 10px 20px;
      border: 1px solid #cccccc;
      border-radius: 10px;
      outline: none;
    }
    

css

    .target {
      transition-property: background-color;
      transition-duration: 1s;
      background-color: #cccccc;
    }
    
    .target:hover,
    .target:focus {
      background-color: #eeeeee;
    }
    

See our [Using CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)
 guide for more `transition-property` examples.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Transitions Module Level 1  <br>\# transition-property-property](https://drafts.csswg.org/css-transitions/#transition-property-property) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Using CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)
    
*   [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
    
*   [`transition-duration`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-duration)
    
*   [`transition-timing-function`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-timing-function)
    
*   [`transition-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-delay)
    
*   [`TransitionEvent`](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition-property/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/transition-property/index.md?plain=1 "Folder: en-us/web/css/reference/properties/transition-property (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition-property&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition-property%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ftransition-property%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ftransition-property%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3fb9ea0187429234b47cb0385a9515a69757fe63%0A*+Document+last+modified%3A+2026-09-10T12%3A13%3A15.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")