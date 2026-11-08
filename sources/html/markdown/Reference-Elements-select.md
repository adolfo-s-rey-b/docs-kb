*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#mdn-search)
    

`<select>` HTML select element
==============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<select>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents a control that provides a menu of options.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#try_it)

---------------------------------------------------------------------------------------------

    <label for="pet-select">Choose a pet:</label>
    
    <select name="pets" id="pet-select">
      <option value="">--Please choose an option--</option>
      <option value="dog">Dog</option>
      <option value="cat">Cat</option>
      <option value="hamster">Hamster</option>
      <option value="parrot">Parrot</option>
      <option value="spider">Spider</option>
      <option value="goldfish">Goldfish</option>
    </select>
    

    label {
      font-family: sans-serif;
      font-size: 1rem;
      padding-right: 10px;
    }
    
    select {
      font-size: 0.9rem;
      padding: 2px 5px;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#attributes)

-----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete)

A string providing a hint for a [user agent's](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 autocomplete feature. See [The HTML autocomplete attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete)
 for a complete list of values and details on how to use autocomplete.

[`autofocus`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#autofocus)

This Boolean attribute lets you specify that a form control should have input focus when the page loads. Only one form element in a document can have the `autofocus` attribute.

[`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)

This Boolean attribute indicates that the user cannot interact with the control. If this attribute is not specified, the control inherits its setting from the containing element, for example [`<fieldset>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/fieldset)
; if there is no containing element with the `disabled` attribute set, then the control is enabled.

[`form`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form)

The [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element to associate the `<select>` with (its _form owner_). The value of this attribute must be the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 of a `<form>` in the same document. (If this attribute is not set, the `<select>` is associated with its ancestor `<form>` element, if any.)

This attribute lets you associate `<select>` elements to `<form>`s anywhere in the document, not just inside a `<form>`. It can also override an ancestor `<form>` element.

[`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)

This Boolean attribute indicates that zero or more options can be selected in the list. If it is not specified, then only one option can be selected at a time. Multiple selected options are submitted using the [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)
 array convention, i.e., `name=value1&name=value2`. If `multiple` is specified, `size` defaults to `4` instead of `1`.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#name)

This attribute is used to specify the name of the control.

[`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)

This Boolean attribute indicates that the user must select at least one option before the form can be submitted. The `<select>` has no selected options if it has no options, `multiple` is specified and the user deselects all options, the select's value is programmatically set to `""`, or only the _placeholder label option_ is selected. Any option other than the placeholder label option is considered valid, even if its value is also empty.

The placeholder label option is the text shown in the box before the user makes a choice, like the "--Please choose an option--" in the [Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#try_it)
 demo above. Semantically, it is considered equivalent to the [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder)
 attribute and is not considered an actual option. It is defined as the first option in the options list which is a direct child of the `<select>` (not inside an `<optgroup>`) and has an empty string as its value. It is only relevant when the `size` is `1` and `multiple` is not specified; in all other cases, such an `<option>` is just a regular option due to the way the `<select>` is rendered.

[`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/size)

Specifies the number of options to display in the closed state as a positive integer. If the attribute is not specified, the default value is `1`, unless the `multiple` attribute is specified, in which case the default value is `4`. If the value is greater than `1` or the `multiple` attribute is present, browsers render a scrolling list box that has the specified number of rows visible; otherwise the options render as a drop-down list. For backwards compatibility, the [`size`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/size "size")
 property always returns `0` as the default value.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#usage_notes)

-------------------------------------------------------------------------------------------------------

Typically, like other form controls, a `<select>` element is associated with a [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 for accessibility purposes, as well as a `name` attribute to represent the name of the associated data point submitted to the server. Each menu option is defined by an [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 element nested inside the `<select>`.

Each `<option>` element should have a [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#value)
 attribute containing the data value to submit to the server when that option is selected. If no `value` attribute is included, the value defaults to the text contained inside the element. You can include a [`selected`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#selected)
 attribute on an `<option>` element to make it selected by default when the page first loads. If no `selected` attribute is specified, the first `<option>` element will be selected by default.

A `<select>` element is represented in JavaScript by an [`HTMLSelectElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement)
 object, and this object has a [`value`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement/value "value")
 property which contains the value of the selected `<option>`.

You can further nest [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 elements inside [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
 elements to create separate groups of options inside the dropdown. You can also include [`<hr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr)
 elements to create separators that add visual breaks between options.

For further examples, see [The native form widgets: Drop-down content](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Other_form_controls#drop-down_controls)
.

### [Options inside wrapper elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#options_inside_wrapper_elements)

The `<select>` element builds its list of options from all `<option>` descendants, not just its direct children. This means that options can be wrapped in other elements, such as [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 elements, and they will still appear as selectable options in the dropdown and be included in form submission. Wrapper elements are useful for styling in [customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
 but have no effect on the select's behavior: they don't create groups, labels, or separators. To group options under a heading, use an [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
; an [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 counts as part of an `<optgroup>` if the group is an ancestor, so wrapper elements may also be used inside a group without breaking the association.

**Note:** Browsers with modern parsing behavior preserve all elements written inside a `<select>` in the DOM — including wrapper elements, [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, and [`<selectedcontent>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent)
. Older browsers instead remove non-permitted elements while parsing, keeping only the `<option>`, `<optgroup>`, and `<hr>` structure. As a result, styling, markup, or scripting that depends on the removed elements will not work on older browsers.

### [Selecting multiple options](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#selecting_multiple_options)

A `<select>` element with the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)
 attribute lets the user choose zero or more options. How the control is rendered depends on the [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#size)
 attribute:

*   If the `multiple` attribute is set, browsers show a scrolling list box, unless the `size` is set to `1`. When `size` is omitted, the list box is four options tall, even if there are fewer options.
*   If `size` is `1`, supporting browsers display a drop-down that lets the user select more than one option when the control is active. If exactly one option is selected, the selected option is displayed, otherwise, the control displays the count of its selected options as a single-line list box. Browsers that don't support these features display a multiple option menu list within a control that is the height of a single-line box.

When using the `multiple` attribute, always inform users that more than one option can be selected.

The following example uses `<select multiple size="1">` to create a drop-down that allows multiple selections:

html

    <label for="flavors">Choose one or more ice cream flavors:</label>
    <select id="flavors" name="flavors" multiple size="1">
      <option value="chocolate">Chocolate</option>
      <option value="strawberry">Strawberry</option>
      <option value="vanilla">Vanilla</option>
    </select>
    

#### Selecting options in a list box

On a desktop computer, there are a number of ways to select multiple options in a `<select>` element with a `multiple` attribute and a `size` attribute greater than `1`.

Mouse users can hold the Ctrl (Command on macOS) or Shift key (depending on what makes sense for your operating system) and then click multiple options to select/deselect them.

**Note:** The keyboard mechanisms described below are not standardized and depend on the browser and operating system.

For example, Firefox on macOS additionally supports using Ctrl, while Safari on macOS does not support using Space for non-contiguous selection.

Keyboard users can select multiple contiguous items by:

*   Focusing on the `<select>` element (e.g., using Tab).
*   Selecting an item at the top or bottom of the range they want to select using the Up and Down cursor keys to go up and down the options.
*   Holding down the Shift key and then using the Up and Down cursor keys to increase or decrease the range of items selected.

Keyboard users can select multiple non-contiguous items by:

*   Focusing on the `<select>` element (e.g., using Tab).
*   Holding down the Ctrl key (Command on macOS) then using the Up and Down cursor keys to change the "focused" select option, i.e., the one that will be selected if you choose to do so. The "focused" select option is highlighted with a dotted outline, in the same way as a keyboard-focused link.
*   Pressing Space to select/deselect "focused" select options.

[Styling with CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#styling_with_css)

-----------------------------------------------------------------------------------------------------------------

The `<select>` element has historically been difficult to style effectively with CSS. The following guides contain information about features that enable fully customizable select elements:

*   [Customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
    
*   [Customizable select listboxes](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select_listboxes)
    

### [Legacy select styling](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#legacy_select_styling)

In browsers that don't support the modern customization features (or legacy codebases where they can't be used), you are limited to manipulating the [box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model)
, the [displayed font](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Fonts)
, etc. You can also use the [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
 property to remove the default system `appearance`.

It is however, hard to get a consistent result across browsers with traditional `<select>` elements. If you want to get full control, you should consider using a library with good facilities for styling form widgets, or try rolling your own dropdown menu using non-semantic elements, JavaScript, and [WAI-ARIA](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/WAI-ARIA_basics)
 to provide semantics.

You can use the [`:open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open)
 pseudo-class to style `<select>` elements in the open state, that is, when the drop-down options list is displayed. This doesn't apply to multi-line `<select>` elements (those with the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)
 attribute set) — they tend to render as a scrolling list box rather than a drop-down, so don't have an open state.

For more information on legacy `<select>` styling, see:

*   [Styling HTML forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Styling_web_forms)
    
*   [Advanced styling for HTML forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Advanced_form_styling)
    
*   The [`field-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing)
     property, which controls how `<select>` elements are sized in relation to their contained options.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#accessibility)

-----------------------------------------------------------------------------------------------------------

The `<hr>` within a `<select>` should be considered purely decorative, as they are currently not exposed within the accessibility tree and therefore not exposed to assistive technologies.

Setting `size="1"` on a multiple select (i.e., `<select multiple size="1">`) renders a drop-down that lets users select multiple options. Some browsers don't expand the option list when the control is active, displaying multiple options in a menu list the height of a single-line box. This harms usability. When including a multiple-select, inform users they can select more than one option, even when multiple options are displayed.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#examples)

-------------------------------------------------------------------------------------------------

### [Basic select](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#basic_select)

The following example creates a three-value dropdown menu. The second option includes the `selected` attribute, making that option selected by default.

html

    <select name="choice">
      <option value="first">First Value</option>
      <option value="second" selected>Second Value</option>
      <option value="third">Third Value</option>
    </select>
    

#### Result

### [Select with grouping options](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#select_with_grouping_options)

The following example creates a dropdown menu with grouping using [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
 and [`<hr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr)
 to make it easier for the user to understand the content in the dropdown.

html

    <label for="hr-select">Your favorite food</label> <br />
    
    <select name="foods" id="hr-select">
      <option value="">Choose a food</option>
      <hr />
      <optgroup label="Fruit">
        <option value="apple">Apples</option>
        <option value="banana">Bananas</option>
        <option value="cherry">Cherries</option>
        <option value="damson">Damsons</option>
      </optgroup>
      <hr />
      <optgroup label="Vegetables">
        <option value="artichoke">Artichokes</option>
        <option value="broccoli">Broccoli</option>
        <option value="cabbage">Cabbages</option>
      </optgroup>
      <hr />
      <optgroup label="Meat">
        <option value="beef">Beef</option>
        <option value="chicken">Chicken</option>
        <option value="pork">Pork</option>
      </optgroup>
      <hr />
      <optgroup label="Fish">
        <option value="cod">Cod</option>
        <option value="haddock">Haddock</option>
        <option value="salmon">Salmon</option>
        <option value="turbot">Turbot</option>
      </optgroup>
    </select>
    

#### Result

### [Advanced select with multiple features](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#advanced_select_with_multiple_features)

The following example is more complex, showing off more features you can use on a `<select>` element:

*   The `multiple` attribute enables selecting more than one option.
*   The `size` attribute is set to `4`, which means 4 lines are displayed at a time. Users can scroll to view all the options.
*   Two [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
     elements are included, creating two visual groupings, generally with the group name being bolded and nested options being indented.
*   The `disabled` attribute is included on the "Hamster" option, making that option not selectable.

html

    <label>
      Please choose one or more pets:
      <select name="pets" multiple size="4">
        <optgroup label="4-legged pets">
          <option value="dog">Dog</option>
          <option value="cat">Cat</option>
          <option value="hamster" disabled>Hamster</option>
        </optgroup>
        <optgroup label="Flying pets">
          <option value="parrot">Parrot</option>
          <option value="macaw">Macaw</option>
          <option value="albatross">Albatross</option>
        </optgroup>
      </select>
    </label>
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#technical_summary)

-------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, [interactive content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#interactive_content)<br>, [listed](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#listed)<br>, [labelable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#labelable)<br>, [resettable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#resettable)<br>, and [submittable](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#submittable)<br> [form-associated](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#form-associated_content)<br> element |
| Permitted content | *   [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)<br>    , [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)<br>    , or [`<hr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/hr)<br>     elements, optionally preceded by a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)<br>     element with a nested [`<selectedcontent>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/selectedcontent)<br>     element if a dropdown box.<br>*   [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)<br>    , [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)<br>    , [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)<br>    , and [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript)<br>     elements. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [`combobox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role)<br> with **no** `multiple` attribute and **no** `size` attribute greater than 1, otherwise [`listbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/listbox_role)<br>. |
| Permitted ARIA roles | [`menu`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menu_role)<br> with **no** `multiple` attribute and **no** `size` attribute greater than 1, otherwise [`combobox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role)<br> is permitted but not recommended. |
| DOM interface | [`HTMLSelectElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLSelectElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-select-element](https://html.spec.whatwg.org/multipage/form-elements.html#the-select-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select#see_also)

-------------------------------------------------------------------------------------------------

*   The [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
     element
*   The [`<optgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/optgroup)
     element
*   [Customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
    
*   Events fired by `<select>`: [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")
    , [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/select/index.md?plain=1 "Folder: en-us/web/html/reference/elements/select (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fselect&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fselect%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fselect%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fselect%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffd0b11ad5b5014a9333578adcc4bc98fb9024da3%0A*+Document+last+modified%3A+2026-10-08T21%3A47%3A27.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")