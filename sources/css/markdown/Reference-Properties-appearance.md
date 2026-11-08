*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#mdn-search)
    

`appearance` CSS property
=========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2022.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`appearance`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the rendered appearance of replaced UI widget elements such as form controls. Most commonly, such elements are given native, platform-specific styling based on the operating system's theme, or a primitive appearance with styles that can be overridden using CSS.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#try_it)

--------------------------------------------------------------------------------------------------

    appearance: auto;
    

    appearance: none;
    

    appearance: textfield;
    

    <section id="default-example">
      <div class="background" id="example-element">
        <input type="search" value="search" aria-label="unlabeled search" />
        <input type="checkbox" aria-label="unlabeled checkbox" />
        <input type="radio" aria-label="unlabeled radio button" />
        <button>Button</button>
      </div>
    </section>
    

    input,
    button {
      appearance: inherit;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#syntax)

--------------------------------------------------------------------------------------------------

css

    /* CSS Basic User Interface Module Level 4 values */
    appearance: none;
    appearance: auto;
    appearance: menulist-button;
    appearance: textfield;
    appearance: base-select;
    
    /* Global values */
    appearance: inherit;
    appearance: initial;
    appearance: revert;
    appearance: revert-layer;
    appearance: unset;
    
    /* <compat-auto> values have the same effect as 'auto' */
    appearance: button;
    appearance: checkbox;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#values)

The `appearance` property can be applied to all elements and pseudo-elements, but the effect of the specified value, if any, depends on the element to which it is applied.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#none)

Gives the widget a _primitive_ appearance, making it stylable via CSS, while maintaining the widget's native functionality. This value does not affect non-widgets.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#auto)

Sets interactive widgets to render with their _OS-native_ appearance. Behaves as `none` on elements with no OS-native styling.

[`base-select`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#base-select)

Relevant only to the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element and [`::picker(select)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker)
 pseudo-element, allowing them to be fully styled.

[`<compat-special>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#compat-special)

Has an effect similar to `auto` on certain elements.

[`textfield`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#textfield)

Causes the appearance of certain `<input>` types to [match the appearance of the `text` type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#try_it)
.

[`menulist-button`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#menulist-button)

When set on the `<select>` element, the drop-down picker's style [matches that of its default state](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#setting_the_appearance_of_a_select)
.

[`<compat-auto>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#compat-auto)

Included for backwards compatibility; possible values include `button`, `checkbox`, `listbox`, `menulist`, `meter`, `progress-bar`, `push-button`, `radio`, `searchfield`, `slider-horizontal`, `square-button`, and `textarea`. The values all behave as `auto`: use `auto` instead.

**Note:** The specification also defines a `base` value. This is not yet supported by any browser.

#### Non-standard values

Some non-standard values are also supported in some browsers:

[`slider-vertical`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#slider-vertical)

Makes the slider vertical when applied to `<input type="range">` elements. To [create a vertical slider](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls)
 you should instead set the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 to `vertical-lr` and the [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 to `rtl`.

[`-apple-pay-button`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#-apple-pay-button)

Displays the Apple Pay logo when set on a [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
, [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, or [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element of type `button` or `reset`.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#description)

------------------------------------------------------------------------------------------------------------

The `appearance` property enables displaying elements in their OS-native style based on the operating system's theme, as well as the removal of any platform-native styling with the `none` value. Setting `appearance: none`, or otherwise changing the appearance of UI widgets, does not change the element's functionality.

While most elements in a document can be fully styled by CSS, UI controls (_widgets_) are typically rendered by the browser using the operating system's native UI styles. This _native_ appearance differs between operating systems and browsers. In this default state, widgets have limited, if any, features that can be styled with CSS. Which elements have this native UI appearance is defined in HTML.

The `appearance` property provides some control over the appearance of HTML widgets that, by default, look like native operating system controls. Most notably, the `none` value suppresses some of a widget's native appearance. This results in a _primitive_ look that can be styled via CSS while still maintaining functionality and supporting native user interactions.

Some widgets disappear completely when set to `appearance: none`. The hidden controls are still interactive, however. For example, clicking on a [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 associated with an `appearance: none` checkbox will toggle the checkbox's checked state.

Because `none` can cause a widget to be hidden, the `base` value is being added to provide widgets with a base appearance. When supported, the `base` value will ensure widgets maintain their native appearance while enabling CSS to be used to change a widget's styles that are not changeable by default. Unlike `none`, which can make radio buttons and checkboxes disappear, `base` gives the widget a primitive appearance with default native styles that are usable and interoperable, as well as enabling a good degree of customization via CSS. While this `base` value is not yet supported, the many `<compat-auto>` values provide similar functionality but are type-specific and not global.

### [Customizable select elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#customizable_select_elements)

The `base-select` value, which is relevant only to the [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element and [`::picker(select)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker)
 pseudo-element, enables [styling `<select>` elements and the select picker](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#setting_the_appearance_of_a_select)
 (which contains the `<option>` elements). The picker is rendered in the top layer, similar to a popover. When `base-select` is set, the picker can be positioned relative to the select (or other elements) using [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
 features. In addition, the `base-select` value causes the `<select>` not to render outside the browser pane or to trigger built-in mobile operating system components. It is also no longer sized based on the width of the widest `<option>`.

See [Customizable select elements](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Customizable_select)
 for more information.

### [Prefixed non-standard values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#prefixed_non-standard_values)

Before standardization, the prefixed **`-moz-appearance`** and **`-webkit-appearance`** properties allowed elements to be shown as widgets such as buttons or checkboxes. The following non-standard values may be encountered in legacy style sheets, most commonly as values of shadow DOM component [prefixed pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_extensions#pseudo-elements)
.

Non-standard values

*   `attachment`
*   `borderless-attachment`
*   `button-bevel`
*   `caps-lock-indicator`
*   `caret`
*   `checkbox-container`
*   `checkbox-label`
*   `checkmenuitem`
*   `color-well`
*   `continuous-capacity-level-indicator`
*   `default-button`
*   `discrete-capacity-level-indicator`
*   `inner-spin-button`
*   `image-controls-button`
*   `list-button`
*   `listitem`
*   `media-enter-fullscreen-button`
*   `media-exit-fullscreen-button`
*   `media-fullscreen-volume-slider`
*   `media-fullscreen-volume-slider-thumb`
*   `media-mute-button`
*   `media-play-button`
*   `media-overlay-play-button`
*   `media-return-to-realtime-button`
*   `media-rewind-button`
*   `media-seek-back-button`
*   `media-seek-forward-button`
*   `media-toggle-closed-captions-button`
*   `media-slider`
*   `media-sliderthumb`
*   `media-volume-slider-container`
*   `media-volume-slider-mute-button`
*   `media-volume-slider`
*   `media-volume-sliderthumb`
*   `media-controls-background`
*   `media-controls-dark-bar-background`
*   `media-controls-fullscreen-background`
*   `media-controls-light-bar-background`
*   `media-current-time-display`
*   `media-time-remaining-display`
*   `menulist-text`
*   `menulist-textfield`
*   `meterbar`
*   `number-input`
*   `progress-bar-value`
*   `progressbar`
*   `progressbar-vertical`
*   `range`
*   `range-thumb`
*   `rating-level-indicator`
*   `relevancy-level-indicator`
*   `scale-horizontal`
*   `scalethumbend`
*   `scalethumb-horizontal`
*   `scalethumbstart`
*   `scalethumbtick`
*   `scalethumb-vertical`
*   `scale-vertical`
*   `scrollbarthumb-horizontal`
*   `scrollbarthumb-vertical`
*   `scrollbartrack-horizontal`
*   `scrollbartrack-vertical`
*   `searchfield-decoration`
*   `searchfield-results-decoration`
*   `searchfield-results-button`
*   `searchfield-cancel-button`
*   `snapshotted-plugin-overlay`
*   `sheet`
*   `sliderthumb-horizontal`
*   `sliderthumb-vertical`
*   `textfield-multiline`

Authors are encouraged to use only standard keywords.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#formal_definition)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `none` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | no  |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#formal_syntax)

----------------------------------------------------------------------------------------------------------------

appearance =   
  none              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  base              [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  base-select       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <compat-auto>     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <compat-special>    
  
<compat-auto> =   
  searchfield   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  textarea      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  checkbox      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  radio         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  menulist      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  listbox       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  meter         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  progress-bar  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  button          
  
<compat-special> =   
  textfield        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  menulist-button    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#examples)

------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#basic_example)

This example demonstrates basic usage of the `appearance` property, altering the appearance of an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element in some browsers.

#### HTML

We include two `number` form controls along with their labels.

html

    <p>
      <label>Enter a number: <input type="number" min="0" max="10" /></label>
    </p>
    <p>
      <label
        >Enter a number: <input type="number" min="0" max="10" class="text"
      /></label>
    </p>
    

#### CSS

We set the element with the class of `text` to look like a text field.

css

    .text {
      appearance: textfield;
    }
    

#### Results

Depending on the browser, the spinner may be visually removed when the control is set to look like a text field. The `appearance` property has no effect on the functionality: for example, while there may no longer be a spinner to click on, the up and down cursor keys will still increment and decrement the value.

### [Appearance set to `none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#appearance_set_to_none)

The following example shows how to remove the default styling from a checkbox, a radio button, and a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element, and apply custom styling.

#### HTML

We include pairs of checkboxes, radio buttons, and `<select>` elements, along with their associated labels:

html

    <label><input type="checkbox" /> Default unchecked </label>
    <label><input type="checkbox" checked /> Default checked </label>
    
    <hr />
    
    <label><input type="radio" name="radio" /> Default unchecked </label>
    <label><input type="radio" name="radio" checked /> Default checked </label>
    
    <hr />
    
    <label
      >Unstyled select
      <select>
        <option>Option 1</option>
        <option>Option 2</option>
      </select>
    </label>
    
    <label
      >Styled select
      <select class="none">
        <option>Option 1</option>
        <option>Option 2</option>
      </select>
    </label>
    

#### CSS

    label {
      display: block;
      margin: 0.5em 0;
    }
    

We apply styles to both [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type `checkbox`; these styles create a red square if the element is stylable. We set `appearance: none` on the [`:checked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked)
 UI state for all inputs (`checkbox` and `radio`), as well as to elements with the `.none` class. This removes all the style of the radio button and checkbox, other than the margins, and allows any set styles to be applied. There are no alternative styles provided for the radio buttons or `<select>` elements for when `none` is set.

css

    [type="checkbox"] {
      width: 1em;
      height: 1em;
      display: inline-block;
      background: red;
    }
    input:checked,
    .none {
      appearance: none;
    }
    

#### Result

Setting `appearance: none` enables UI elements to be styled, but it also runs the risk of hiding the widget. The unchecked checkbox, with its `appearance` defaulting to `auto`, looks like a checkbox. Setting `appearance: none` in the `:checked` state enables it to be styled.

Like the unchecked checkbox, the unchecked radio button looks like the native UI widget, because it is. When in the checked state, with `appearance: none` applied, the radio button disappears; its functionality is retained, and only its margins affect page rendering.

### [Setting the appearance of a select](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#setting_the_appearance_of_a_select)

We can use the `appearance` property to opt-in to custom select functionality, enabling styling the `<select>` element and its picker, which represents the part of the form control that pops out of the page.

#### HTML

We include three `<select>` elements, with the same multiple [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 children. As with every `<select>`, we also include associated [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 elements. The third option has more text to demonstrate the effect of `base-select` on the width of the `<select>`:

html

    <label for="ice-cream1"
      >Default flavor:
      <select id="ice-cream1">
        <option>Asparagus</option>
        <option>Dulce de leche</option>
        <option>Pistachio, rum raisin, and coffee</option>
      </select>
    </label>
    <label for="ice-cream2"
      >Base select flavor:
      <select id="ice-cream2" class="baseSelect">
        <option>Asparagus</option>
        <option>Dulce de leche</option>
        <option>Pistachio, rum raisin, and coffee</option>
      </select>
    </label>
    <label for="ice-cream3"
      >Menulist button flavor:
      <select id="ice-cream3" class="menulistButton">
        <option>Asparagus</option>
        <option>Dulce de leche</option>
        <option>Pistachio, rum raisin, and coffee</option>
      </select>
    </label>
    

#### CSS

We select the pickers of all the `<select>` elements using the [`::picker()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::picker)
 pseudo-element with the `select` parameter. We set the `appearance` value of all the pickers and one `<select>` element to `base-select`. We set the last `<select>` to `menulist-button`. The first `<select>` defaults to the `auto` state:

css

    .baseSelect,
    ::picker(select) {
      appearance: base-select;
    }
    .menulistButton {
      appearance: menulist-button;
    }
    

css

    label {
      display: block;
    }
    

We set values for the `<select>` and pickers' [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 and [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 properties to demonstrate the effects of the `appearance` values:

css

    select {
      border: 1px solid red;
      background-color: orange;
    }
    
    ::picker(select) {
      background-color: yellow;
      border: none;
    }
    

#### Results

While the [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 and [`border`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border)
 styles are defined on all the `<select>` elements and their pickers, the `::picker(select)` styles only affect the picker where both the select and the picker have the `appearance` property set to `base-select`. The first and third selects look the same because `menulist-button` is a compatibility keyword.

Notice that, by default, the inline-size of the `<select>` is generally the inline-size of the `<option>` with the most text, and that the drop-down picker appears over the top of the rendered page when opened, making it not constrained by the surrounding page and therefore fully visible. These statements are no longer true when `base-select` is set.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# appearance-switching](https://drafts.csswg.org/css-ui/#appearance-switching) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance#see_also)

------------------------------------------------------------------------------------------------------

*   [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/prefers-color-scheme)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/appearance/index.md?plain=1 "Folder: en-us/web/css/reference/properties/appearance (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fappearance&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fappearance%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fappearance%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fappearance%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd78544a841b0e266a6efc169c044573f5e0b4e7d%0A*+Document+last+modified%3A+2026-10-07T05%3A41%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")