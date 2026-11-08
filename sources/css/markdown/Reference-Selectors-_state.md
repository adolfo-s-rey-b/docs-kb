*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#mdn-search)
    

`:state()` CSS pseudo-class
===========================

Baseline 2024

Newly available

Since May 2024, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:state()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches [custom elements](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements)
 that have the specified custom state.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#syntax)

---------------------------------------------------------------------------------------------

css

    :state(<custom identifier>) {
      /* ... */
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#parameters)

The `:state()` pseudo-class takes as its argument a custom identifier that represents the state of the custom element to match.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#description)

-------------------------------------------------------------------------------------------------------

Elements can transition between states due to user interaction and other factors. For instance, an element can be in the "hover" state when a user hovers over the element, or a link can be in the "visited" state after a user clicks on it. Elements provided by browsers can be styled based on these states using CSS pseudo-classes such as [`:hover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:hover)
 and [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
. Similarly, [autonomous custom elements](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements#types_of_custom_element)
 (custom elements that are not derived from built-in elements) can expose their states, allowing pages that use the elements to style them using the CSS `:state()` pseudo-class.

The states of a custom element are represented by string values. These values are added to or removed from a [`CustomStateSet`](https://developer.mozilla.org/en-US/docs/Web/API/CustomStateSet)
 object associated with the element. The CSS `:state()` pseudo-class matches an element when the identifier, passed as an argument, is present in the `CustomStateSet` of the element.

The `:state()` pseudo-class can also be used to match custom states within the implementation of a custom element. This is achieved by using `:state()` within the [`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
 pseudo-class function, which matches a state only within the shadow DOM of the current custom element.

Additionally, the [`::part()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
 pseudo-element followed by the `:state()` pseudo-class allows matching on the [shadow parts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts)
 of a custom element that are in a particular state. (**Shadow parts** are parts of a custom element's shadow tree that are explicitly exposed to a containing page for styling purposes.)

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#examples)

-------------------------------------------------------------------------------------------------

### [Matching a custom state](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#matching_a_custom_state)

This CSS shows how to change the border of the autonomous custom element `<labeled-checkbox>` to `red` when it is in the "checked" state.

css

    labeled-checkbox {
      border: dashed red;
    }
    labeled-checkbox:state(checked) {
      border: solid;
    }
    

For a live example of this code in action, see the [Matching the custom state of a custom checkbox element](https://developer.mozilla.org/en-US/docs/Web/API/CustomStateSet#matching_the_custom_state_of_a_custom_checkbox_element)
 example on the `CustomStateSet` page.

### [Matching a custom state in a custom element's shadow DOM](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#matching_a_custom_state_in_a_custom_elements_shadow_dom)

This example shows how the `:state()` pseudo-class can be used within the [`:host()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:host_function)
 pseudo-class function to match custom states within the implementation of a custom element.

The following CSS injects a gray `[x]` before the element when it is in the "checked" state.

css

    :host(:state(checked))::before {
      content: "[x]";
    }
    

For a live example of this code in action, see the [Matching the custom state of a custom checkbox element](https://developer.mozilla.org/en-US/docs/Web/API/CustomStateSet#matching_the_custom_state_of_a_custom_checkbox_element)
 example on the `CustomStateSet` page.

### [Matching a custom state in a shadow part](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#matching_a_custom_state_in_a_shadow_part)

This example shows how the `:state()` pseudo-class can be used to target the [shadow parts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Shadow_parts)
 of a custom element.

Shadow parts are defined and named using the [`part`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/part)
 attribute. For example, consider a custom element named `<question-box>` that uses a `<labeled-checkbox>` custom element as a shadow part named `checkbox`:

js

    shadowRoot.innerHTML = `<labeled-checkbox part='checkbox'>Yes</labeled-checkbox>`;
    

The CSS below shows how the [`::part()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::part)
 pseudo-element can be used to match against the `'checkbox'` shadow part. It then shows how the `::part()` pseudo-element followed by the `:state()` pseudo-class can be used to match against the same part when it is in the `checked` state.

css

    question-box::part(checkbox) {
      color: red;
    }
    
    question-box::part(checkbox):state(checked) {
      color: green;
      outline: dashed 1px green;
    }
    

For a live example of this code in action, see the [Matching a custom state in a shadow part of a custom element](https://developer.mozilla.org/en-US/docs/Web/API/CustomStateSet#matching_a_custom_state_in_a_shadow_part_of_a_custom_element)
 example on the `CustomStateSet` page.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-custom](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-custom) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state#see_also)

-------------------------------------------------------------------------------------------------

*   [`CustomStateSet`](https://developer.mozilla.org/en-US/docs/Web/API/CustomStateSet)
    
*   [Pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
    
*   [Learn: Pseudo-classes and pseudo-elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Pseudo_classes_and_elements)
    
*   [Custom states and custom state pseudo-class CSS selectors](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements#custom_states_and_custom_state_pseudo-class_css_selectors)
     in [Using custom elements](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_custom_elements)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:state/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_state/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_state (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Astate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_state%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Astate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_state%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F28f5f3b9b463fa842fa686ccc73c9e1d9b06282b%0A*+Document+last+modified%3A+2026-08-27T09%3A06%3A52.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")