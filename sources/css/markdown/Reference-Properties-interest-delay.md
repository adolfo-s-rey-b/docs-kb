*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#mdn-search)
    

`interest-delay` CSS property
=============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/464)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#browser_compatibility)
 carefully before using this in production.

The **`interest-delay`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the delay between the user showing interest in an [interest invoker](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
 element and the [`interest`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/interest_event "interest")
 event firing, and the delay between the user losing interest and the [`loseinterest`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/loseinterest_event "loseinterest")
 event firing.

[Constituent properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#constituent_properties)

--------------------------------------------------------------------------------------------------------------------------------------

This property is a shorthand for the following properties:

*   [`interest-delay-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)
    
*   [`interest-delay-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#syntax)

------------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#values)

The `interest-delay` property accepts one or two values. The first value sets the delay before interest is shown (`interest-delay-start`); the second value, if provided, sets the delay before interest is lost (`interest-delay-end`). Each value can be either the keyword `normal` or a [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
 value:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#normal)

Sets the delay to the browser's default delay. This is the initial value.

[`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)

Sets the delay to a specific duration. The value must be positive, otherwise the property becomes invalid.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#description)

----------------------------------------------------------------------------------------------------------------

A control element such as an [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
 or [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 can be set as an [interest invoker](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
 by giving it the [`interestfor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a#interestfor)
 attribute. Its value should be the `id` of a target element. When this relationship is established, the target element is affected when the user "shows interest" in the invoker (for example, by hovering or focusing it). A common use case is to display a popover on hover or focus. When the user "loses interest", the effect stops.

When the user shows or loses interest, the associated effect doesn't start or stop immediately — the browser adds a short delay (which may vary by browser). This prevents [preview popovers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers#using_interest_invokers_for_creating_preview_popovers)
, for example, from appearing immediately when the user hovers a link, which could be annoying and distracting on a link-heavy page.

The `interest-delay` property allows you to customize these delays. You can use `interest-delay` to specify the delay before the interest effect starts (specified by the [`interest-delay-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)
 property) and the delay before the interest effect ends (specified by the [`interest-delay-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)
 property) in a single declaration.

The `interest-delay` property can take one or two values. These values can be the keyword `normal`, which sets the default browser delay, or a [`<time>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
 value, which sets a custom delay. If a single value is specified, it applies to both [`interest-delay-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)
 and [`interest-delay-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)
. If two values are specified, the first value sets [`interest-delay-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)
, and the second value sets [`interest-delay-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#formal_definition)

----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | as each of the properties of the shorthand:  <br><br>*   [`interest-delay-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)<br>    : `normal`<br>*   [`interest-delay-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)<br>    : `normal` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as each of the properties of the shorthand:  <br><br>*   [`interest-delay-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)<br>    : `normal` or a computed time<br>*   [`interest-delay-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)<br>    : `normal` or a computed time |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | as each of the properties of the shorthand:  <br><br>*   [`interest-delay-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)<br>    : by computed value type<br>*   [`interest-delay-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)<br>    : by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#formal_syntax)

--------------------------------------------------------------------------------------------------------------------

interest-delay =   
  [<'interest-delay-start'>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)
[{1,2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<interest-delay-start>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)
 =   
  normal  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<time>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/time)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#examples)

----------------------------------------------------------------------------------------------------------

### [Creating a basic `interest-delay` effect](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#creating_a_basic_interest-delay_effect)

In this example, we demonstrate how `interest-delay` affects interest invoker behavior.

#### HTML

The markup includes a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, a [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
, and an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 of type `checkbox`. We specify the `<button>` as an interest invoker by giving it the `interestfor` attribute whose value matches the `id` of the `<p>` element. This makes the paragraph the target element. The paragraph is turned into a popover by giving it the [`popover`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover)
 attribute, which hides it initially.

#### CSS

In the CSS, we define a `.delay` rule that applies an `interest-delay` value of `1s 2s` to any interest invoker the `delay` class is set on. We will set this class on the `<button>` when the checkbox is checked using JavaScript.

#### JavaScript

In our script, we get references to the `<button>` and the checkbox, then create an event listener that toggles the `delay` class on the `<button>` whenever the checkbox value changes (when it is checked or unchecked).

#### Result

This renders as follows:

Try showing interest in the button (for example, by hovering or focusing it) and then losing interest to observe the popover showing and hiding. By default, the popover shows and hides after a very short delay.

Now check the checkbox and try the same actions again. This time, the popover should appear after a delay of `1s` when interest is shown, and hide after a delay of `2s` when interest is lost.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# propdef-interest-delay](https://drafts.csswg.org/css-ui-4/#propdef-interest-delay) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay#see_also)

----------------------------------------------------------------------------------------------------------

*   [`interest-delay-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)
    , [`interest-delay-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)
    
*   [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API)
    
*   [Using interest invokers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)
    
*   [CSS basic user interface](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/interest-delay/index.md?plain=1 "Folder: en-us/web/css/reference/properties/interest-delay (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finterest-delay&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finterest-delay%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Finterest-delay%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Finterest-delay%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5381238460a48ff323a93e652d15cb62598f0262%0A*+Document+last+modified%3A+2026-08-27T15%3A14%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")