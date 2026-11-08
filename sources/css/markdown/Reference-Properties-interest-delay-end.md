*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#mdn-search)
    

`interest-delay-end` CSS property
=================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/464)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#browser_compatibility)
 carefully before using this in production.

The **`interest-delay-end`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the delay between the user losing interest in an [interest invoker](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
 element and the [`loseinterest`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/loseinterest_event "loseinterest")
 event firing.

The `interest-delay-end` and [`interest-delay-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)
 properties can both be set using the [`interest-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay)
 shorthand.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* Keyword or custom delay */
    interest-delay-end: normal;
    interest-delay-end: 2s;
    interest-delay-end: 250ms;
    
    /* Global values */
    interest-delay-end: inherit;
    interest-delay-end: initial;
    interest-delay-end: revert;
    interest-delay-end: revert-layer;
    interest-delay-end: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#values)

This property is specified as one `<time>` value or the keyword `normal`:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#normal)

Sets the delay to the browser's default delay. This is the initial value.

[`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)

Sets the delay to a specific duration. The value must be positive, otherwise the property becomes invalid.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | `normal` or a computed time |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

interest-delay-end =   
  normal  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<time>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#examples)

--------------------------------------------------------------------------------------------------------------

### [Creating a basic `interest-delay-end` effect](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#creating_a_basic_interest-delay-end_effect)

In this example, we demonstrate how `interest-delay-end` affects interest invoker behavior.

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
        Apply an <code>interest-delay-end</code> of <code>2s</code>
      </label>
    </form>
    

#### CSS

In the CSS, we specify a rule with a `.delay` selector that applies an `interest-delay-end` value of `2s` to any interest invoker the `delay` class is set on. We will set this on the `<button>` when the checkbox is checked using JavaScript.

css

    .delay {
      interest-delay-end: 2s;
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

Now check the checkbox and try the same actions again. This time, the delay between showing interest and the popover appearing is unaffected, but the delay between losing interest and the popover disappearing should be increased to `2s`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# propdef-interest-delay-end](https://drafts.csswg.org/css-ui-4/#propdef-interest-delay-end) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`interest-delay-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)
    , [`interest-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay)
    
*   [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
    
*   [Using interest invokers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
    
*   [CSS basic user interface](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/interest-delay-end/index.md?plain=1 "Folder: en-us/web/css/reference/properties/interest-delay-end (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finterest-delay-end&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finterest-delay-end%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finterest-delay-end%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finterest-delay-end%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")