*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open#mdn-search)
    

`:open` CSS pseudo-class
========================

Baseline 2026

Newly available

Since May 2026, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:open`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents an element that has open and closed states, only when it is currently in the open state.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open#syntax)

--------------------------------------------------------------------------------------------

css

    :open {
      /* ... */
    }
    

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open#description)

------------------------------------------------------------------------------------------------------

The `:open` pseudo-class selects any element currently in the open state, which includes the following elements:

*   [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
     and [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
     elements that are in an open state, that is, they have the `open` attribute set. This selection can also be done using an attribute selector: `details[open]`.
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     elements that display a picker interface for the user to choose a value from (for example [`<input type="color">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color)
    ), when the picker is displayed.
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
     elements that display a drop-down picker for the user to choose a value from, when the picker is displayed. Note that when implementing [customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
    , the picker itself can be selected using the [`::picker(select)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker)
     pseudo-element.

Note that the open and closed states are semantic states, and don't necessary correlate with the visibility of the element in question. For example, a `<details>` element that is expanded to show its content is open, and will be selected by the `details:open` selector, even if it is hidden with a [`visibility`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
 value of `hidden`.

[Popover](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API "Popover")
 elements (that is, elements with the [`popover`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/popover)
 attribute set on them) have distinct semantic states representing popovers that are showing or hidden, which can coexist alongside open and closed states. To target a popover element in a showing state, use the [`:popover-open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)
 pseudo-class instead.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open#examples)

------------------------------------------------------------------------------------------------

### [Basic `:open` usage](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open#basic_open_usage)

This example demonstrates some of the HTML elements that have an open state.

#### CSS

css

    details:open > summary {
      background-color: pink;
    }
    
    :is(select, input):open {
      background-color: pink;
    }
    

    @supports not selector(:open) {
      body::before {
        content: "Your browser doesn't support the :open selector.";
        background-color: wheat;
        display: block;
        text-align: center;
        padding: 1rem 0;
      }
    }
    

#### HTML

html

    <details>
      <summary>Details</summary>
      Lorem ipsum dolor sit amet, consectetur adipiscing elit. In pulvinar dapibus
      lacus, sit amet finibus lectus mollis eu. Nullam quis orci dictum, porta lacus
      et, cursus nunc. Aenean pulvinar imperdiet neque fermentum facilisis. Nulla
      facilisi. Curabitur vitae sapien ut nunc pulvinar semper vitae vitae nisi.
    </details>
    <hr />
    
    <label for="pet-select">Choose a pet:</label>
    <select id="pet-select">
      <option value="dog">Dog</option>
      <option value="cat">Cat</option>
      <option value="hamster">Hamster</option>
    </select>
    <hr />
    
    <label for="start">Start date:</label>
    <input type="date" id="start" />
    

#### Result

### [Custom `<select>` styling with `:open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open#custom_select_styling_with_open)

In this example, we give a basic [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element some custom styling. The `:open` pseudo-class is used to apply a styling enhancement to its open state — when the dropdown menu is displayed.

#### HTML

There is nothing special about our fruit selector.

html

    <label>
      Choose your favorite fruit:
      <select name="fruit">
        <option>apple</option>
        <option>banana</option>
        <option>boysenberry</option>
        <option>cranberry</option>
        <option>fig</option>
        <option>grapefruit</option>
        <option>lemon</option>
        <option>orange</option>
        <option>papaya</option>
        <option>pomegranate</option>
        <option>tomato</option>
      </select>
    </label>
    

**Note:** We are not using a multi-line `<select>` (that is, one with the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)
 attribute set) — those tend to render as a scrolling list box rather than a dropdown menu, so don't have an open state.

#### CSS

In the CSS, we set an [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
 value of `none` on our `<select>` element to remove the default OS styling from the select box, and provide some basic styles of or own. Most notably, we set an [SVG](https://developer.mozilla.org/en-US/docs/Glossary/SVG)
 background image of a down arrow on the right-hand side — users tend to recognize `<select>` elements by the down arrow, so it is a good idea to include it.

We then set some [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
 on the surrounding [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element, and a transparent border to keep the layout consistent when we later add a colored border to it.

css

    select {
      appearance: none;
      width: 100%;
      display: block;
      font-family: inherit;
      font-size: 100%;
      padding: 5px;
      border: 1px solid black;
      background: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpolygon points='5,5 15,5 10,15'/%3E%3C/svg%3E")
        no-repeat right 3px center / 1em 1em;
    }
    
    label {
      font-family: sans-serif;
      max-width: 20em;
      display: block;
      padding: 20px;
      border: 2px solid transparent;
    }
    

When the `<select>` is opened, we use the `:open` pseudo-class to set a different background color and change the background image to an up arrow. We also set a different background color and border on the enclosing `<label>` element using a combination of the `:open` and [`:has()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:has)
 pseudo-classes to create a parent selector. We are literally saying "select the `<label>`, but only when its descendant `<select>` is open."

css

    select:open {
      background-color: #f8f2dc;
      background-image: url("data:image/svg+xml,%3Csvg width='20' height='20' viewBox='0 0 20 20' xmlns='http://www.w3.org/2000/svg'%3E%3Cpolygon points='5,15 10,5 15,15'/%3E%3C/svg%3E");
    }
    
    label:has(select:open) {
      background-color: #81adc8;
      border-color: #cd4631;
    }
    

#### Result

The result is as follows. Try opening the `<select>` dropdown to see the effect on the styling:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-open](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-open) |
| [Selectors Level 4  <br>\# selectordef-open](https://drafts.csswg.org/selectors/#selectordef-open) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open#see_also)

------------------------------------------------------------------------------------------------

*   [`<details>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/details)
    , [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
    , [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    , and [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     elements
*   [`:popover-open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:popover-open)
     pseudo-class
*   [`:modal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:modal)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 31, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_open/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_open (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aopen&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_open%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Aopen%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_open%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F26fb7eaa7b398a35c2463fa15ab6ccfa46a9e06d%0A*+Document+last+modified%3A+2026-08-31T07%3A32%3A10.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")