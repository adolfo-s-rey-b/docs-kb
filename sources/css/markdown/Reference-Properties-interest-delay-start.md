*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#mdn-search)
    

`interest-delay-start` CSS property
===================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/464)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#browser_compatibility)
 carefully before using this in production.

The **`interest-delay-start`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the delay between the user showing interest in an [interest invoker](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
 element and the [`interest`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/interest_event "interest")
 event firing.

The `interest-delay-start` and [`interest-delay-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)
 properties can both be set using the [`interest-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay)
 shorthand.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#syntax)

------------------------------------------------------------------------------------------------------------

css

    /* Keyword or custom delay */
    interest-delay-start: normal;
    interest-delay-start: 2s;
    interest-delay-start: 250ms;
    
    /* Global values */
    interest-delay-start: inherit;
    interest-delay-start: initial;
    interest-delay-start: revert;
    interest-delay-start: revert-layer;
    interest-delay-start: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#values)

This property is specified as one `<time>` value or the keyword `normal`:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#normal)

Sets the delay to the browser's default delay. This is the initial value.

[`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)

Sets the delay to a specific duration. The value must be positive, otherwise the property becomes invalid.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#formal_definition)

----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | `normal` or a computed time |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#formal_syntax)

--------------------------------------------------------------------------------------------------------------------------

interest-delay-start =   
  normal  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<time>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#examples)

----------------------------------------------------------------------------------------------------------------

### [Creating a basic `interest-delay-start` effect](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#creating_a_basic_interest-delay-start_effect)

In this example, we demonstrate how `interest-delay-start` affects interest invoker behavior.

#### HTML

The markup includes a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
, and an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 of type `checkbox`. We specify the `<button>` as an interest invoker by giving it the `interestfor` attribute, whose value matches the `id` of the `<p>` element. This makes the paragraph the target element. The paragraph is turned into a popover by giving it the [`popover`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover)
 attribute, which hides it initially.

html

    <button interestfor="mypopover">Button</button>
    <p id="mypopover" popover>Hover tooltip</p>
    <form>
      <input type="checkbox" id="apply-delay" />
      <label for="apply-delay">
        Apply an <code>interest-delay-start</code> of <code>2s</code>
      </label>
    </form>
    

#### CSS

In the CSS, we specify a rule with a `.delay` selector that applies an `interest-delay-start` value of `2s` to any interest invoker the `delay` class is set on. We will set this on the `<button>` when the checkbox is checked using JavaScript.

css

    .delay {
      interest-delay-start: 2s;
    }
    

#### JavaScript

In our script, we get references to the `<button>` and the checkbox, then create an event listener that toggles the `delay` class on the `<button>` whenever the checkbox value changes (when it is checked or unchecked).

js

    const btn = document.querySelector("button");
    const checkbox = document.querySelector("input");
    checkbox.addEventListener("change", () => {
      btn.classList.toggle("delay");
    });
    

#### Result

This renders as follows:

Try showing interest in the button (for example, by hovering or focusing it) and then losing interest to observe the popover showing and hiding. By default, the popover shows and hides after a very short delay.

Now check the checkbox and try the same actions again. This time, the popover should appear after a delay of `2s` when interest is shown. The delay after interest is lost should be unaffected.

### [Removing `interest-delay-start` after interest has been shown](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#removing_interest-delay-start_after_interest_has_been_shown)

In this example, we show how to remove the `interest-delay-start` from multiple interest invoker elements after interest has been shown on one of them.

This is a useful technique. Having a popover appear as soon as interest is shown on any invoker would create a distracting and annoying user experience, which is why browsers add a small delay by default (see the [`interest-delay` description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#description)
 for more details). However, once users have shown interest in an invoker, it is convenient to allow them to move between other invokers quickly without delay.

#### HTML

The markup includes three `<button>` elements wrapped in a paragraph with a `container` class, and another paragraph that has been turned into a popover using the `popover` attribute. All three buttons are set up as interest invokers and reference the popover as their target using the `interestfor` attribute.

html

    <p class="container">
      <button interestfor="mypopover">Button 1</button>
      <button interestfor="mypopover">Button 2</button>
      <button interestfor="mypopover">Button 3</button>
    </p>
    <p id="mypopover" popover>Hover tooltip</p>
    

#### CSS

In the CSS, we apply an `interest-delay-start` value of `1s` to the buttons, then position the popover below whatever button is having interest shown on it by giving it a [`position-area`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/position-area)
 value of `bottom` (see [Popover anchoring positioning](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#popover_anchor_positioning)
 for more information).

css

    button {
      interest-delay-start: 1s;
    }
    
    #mypopover {
      position-area: bottom;
    }
    

Finally, we combine the [`:interest-source`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source)
 pseudo-class with the [`:has()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has)
 pseudo-class to apply `interest-delay-start: 0s` to all buttons inside the paragraph, but only when the paragraph contains a button on which interest has been shown (that is, matched by `button:interest-source`).

css

    .container:has(button:interest-source) button {
      interest-delay-start: 0s;
    }
    

#### Result

This renders as follows:

Try showing interest in any button and notice how, when you then immediately show interest in another button, the popover appears without delay. If you stop showing interest in the buttons and then start again, the initial delay will return.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#specifications)

----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# propdef-interest-delay-start](https://drafts.csswg.org/css-ui-4/#propdef-interest-delay-start) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start#see_also)

----------------------------------------------------------------------------------------------------------------

*   [`interest-delay-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)
    , [`interest-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay)
    
*   [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
    
*   [Using interest invokers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
    
*   [CSS basic user interface](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/interest-delay-start/index.md?plain=1 "Folder: en-us/web/css/reference/properties/interest-delay-start (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finterest-delay-start&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finterest-delay-start%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finterest-delay-start%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finterest-delay-start%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")