*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#mdn-search)
    

`<input type="range">` HTML attribute value
===========================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`range`** let the user specify a numeric value which must be no less than a given value, and no more than another given value. The precise value, however, is not considered important. This is typically represented using a slider or dial control rather than a text entry box like the [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number)
 input type.

Because this kind of widget is imprecise, it should only be used if the control's exact value isn't important.

If the user's browser doesn't support type `range`, it will fall back and treat it as a `[text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text) ` input.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#try_it)

--------------------------------------------------------------------------------------------------

    <p>Audio settings:</p>
    
    <div>
      <input type="range" id="volume" name="volume" min="0" max="11" />
      <label for="volume">Volume</label>
    </div>
    
    <div>
      <input
        type="range"
        id="cowbell"
        name="cowbell"
        min="0"
        max="100"
        value="90"
        step="10" />
      <label for="cowbell">Cowbell</label>
    </div>
    

    p,
    label {
      font:
        1rem "Fira Sans",
        sans-serif;
    }
    
    input {
      margin: 0.4rem;
    }
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#value)

------------------------------------------------------------------------------------------------

The value of an `<input type="range">` element is set using the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute which accepts a string representing the selected number. The value is never an empty string (`""`). The default value is halfway between the specified minimum and maximum—unless the maximum is actually less than the minimum, in which case the default is set to the value of the `min` attribute. The algorithm for determining the default value is:

js

    defaultValue =
      rangeElem.max < rangeElem.min
        ? rangeElem.min
        : rangeElem.min + (rangeElem.max - rangeElem.min) / 2;
    

If an attempt is made to set the value lower than the minimum, it is set to the minimum. Similarly, an attempt to set the value higher than the maximum results in it being set to the maximum.

### [Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#validation)

There is no pattern validation available; however, the following forms of automatic validation are performed:

*   If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
     is set to something which can't be converted into a valid floating-point number, validation fails because the input is suffering from a bad input.
*   The value won't be less than [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)
    . The default is 0.
*   The value won't be greater than [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)
    . The default is 100.
*   The value will be a multiple of [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step)
    . The default is 1.

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#additional_attributes)

--------------------------------------------------------------------------------------------------------------------------------

In addition to the attributes shared by all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, range inputs offer the following attributes.

**Note:** The following input attributes do not apply to the input range: `accept`, `alt`, `checked`, `dirname`, `formaction`, `formenctype`, `formmethod`, `formnovalidate`, `formtarget`, `height`, `maxlength`, `minlength`, `multiple`, `pattern`, `placeholder`, `readonly`, `required`, `size`, and `src`. Any of these attributes, if included, will be ignored.

### [list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#list)

The value of the `list` attribute is the [`id`](https://developer.mozilla.org/en-US/docs/Web/API/Element/id "id")
 of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element located in the same document. The [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 provides a list of predefined values to suggest to the user for this input. Any values in the list that are not compatible with the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 are not included in the suggested options. The values provided are suggestions, not requirements: users can select from this predefined list or provide a different value.

See the [adding tick marks](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#adding_tick_marks)
 below for an example of how the options on a range are denoted in supported browsers.

### [max](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#max)

The greatest value in the range of permitted values. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 entered into the element exceeds this, the element fails [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If the value of the [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)
 attribute isn't a number, then the element has no maximum value.

This value must be greater than or equal to the value of the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)
 attribute. See the HTML [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)
 attribute.

### [min](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#min)

The lowest value in the range of permitted values. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 of the element is less than this, the element fails [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If a value is specified for `min` that isn't a valid number, the input has no minimum value.

This value must be less than or equal to the value of the [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)
 attribute. See the HTML [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)
 attribute.

**Note:** If the `min` and `max` values are equal or the `max` value is lower than the `min` value the user will not be able to interact with the range.

### [step](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#step)

The `step` attribute is a number that specifies the granularity that the value must adhere to, or the special value `any`, which is described below. Only values which are a whole number of steps from the step base are valid. The step base is [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#min)
 if specified, [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 otherwise, or `0` if neither is provided.

The default stepping value for `step` inputs is `1`, allowing only integers to be entered—_unless_ the stepping base is not an integer.

A string value of `any` means that no stepping is implied, and any value is allowed (barring other constraints, such as [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#max)
). See the [Setting step to the `any` value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#setting_step_to_any)
 example for how this works in supported browsers.

**Note:** When the value entered by a user doesn't adhere to the stepping configuration, the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 may round off the value to the nearest valid value, preferring to round numbers up when there are two equally close options.

[Non-standard attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#non-standard_attributes)

------------------------------------------------------------------------------------------------------------------------------------

### [orient](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#orient)

Similar to the -moz-orient non-standard CSS property impacting the [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
 and [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
 elements, the `orient` attribute defines the orientation of the range slider. Values include `horizontal`, meaning the range is rendered horizontally, and `vertical`, where the range is rendered vertically.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#examples)

------------------------------------------------------------------------------------------------------

While the `number` type lets users enter a number with optional constraints forcing their value to be between a minimum and a maximum value, it does require that they enter a specific value. The `range` input type lets you ask the user for a value in cases where the user may not even care—or know—what the specific numeric value selected is.

A few examples of situations in which range inputs are commonly used:

*   Audio controls such as volume and balance, or filter controls.
*   Color configuration controls such as color channels, transparency, brightness, etc.
*   Game configuration controls such as difficulty, visibility distance, world size, and so forth.
*   Password length for a password manager's generated passwords.

As a rule, if the user is more likely to be interested in the percentage of the distance between minimum and maximum values than the actual number itself, a range input is a great candidate. For example, in the case of a home stereo volume control, users typically think "set volume at halfway to maximum" instead of "set volume to 0.5".

### [Specifying the minimum and maximum](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#specifying_the_minimum_and_maximum)

By default, the minimum is 0 and the maximum is 100. If that's not what you want, you can easily specify different bounds by changing the values of the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)
 and/or [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)
 attributes. These can be any floating-point value.

For example, to ask the user for a value between -10 and 10, you can use:

html

    <input type="range" min="-10" max="10" />
    

### [Setting the value's granularity](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#setting_the_values_granularity)

By default, the granularity is 1, meaning the value is always an integer. To control the granularity, you can change the [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step)
 attribute. For example, if you need a value to be halfway between 5 and 10, you should set the value of `step` to 0.5:

#### Setting the step attribute

html

    <input type="range" min="5" max="10" step="0.5" />
    

#### Setting step to `any`

If you want to accept any value regardless of how many decimal places it extends to, you can specify a value of `any` for the [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step)
 attribute:

##### HTML

html

    <input id="pi_input" type="range" min="0" max="3.14" step="any" />
    <p>Value: <output id="value"></output></p>
    

##### JavaScript

js

    const value = document.querySelector("#value");
    const input = document.querySelector("#pi_input");
    value.textContent = input.value;
    input.addEventListener("input", (event) => {
      value.textContent = event.target.value;
    });
    

This example lets the user select any value between 0 and π without any restriction on the fractional part of the value selected. JavaScript is used to show how the value changes as the user interacts with the range.

### [Adding tick marks](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#adding_tick_marks)

To add tick marks to a range control, include the `list` attribute, giving it the `id` of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element which defines a series of tick marks on the control. Each point is represented using an [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)
 element with its [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option#value)
 set to the range's value at which a mark should be drawn.

#### HTML

html

    <label for="temp">Choose a comfortable temperature:</label><br />
    <input type="range" id="temp" name="temp" list="markers" />
    
    <datalist id="markers">
      <option value="0"></option>
      <option value="25"></option>
      <option value="50"></option>
      <option value="75"></option>
      <option value="100"></option>
    </datalist>
    

#### Result

### [Using the same datalist for multiple range controls](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#using_the_same_datalist_for_multiple_range_controls)

To help you from repeating code you can reuse that same [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 for multiple `<input type="range">` elements, and other [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 types.

**Note:** If you also want to [show the labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#adding_labels)
 as in the example below then you would need a `datalist` for each range input.

#### HTML

html

    <p>
      <label for="temp1">Temperature for room 1:</label>
      <input type="range" id="temp1" name="temp1" list="values" />
    </p>
    <p>
      <label for="temp2">Temperature for room 2:</label>
      <input type="range" id="temp2" name="temp2" list="values" />
    </p>
    
    <p>
      <label for="temp3">Temperature for room 3:</label>
      <input type="range" id="temp3" name="temp3" list="values" />
    </p>
    
    <datalist id="values">
      <option value="0" label="0"></option>
      <option value="25" label="25"></option>
      <option value="50" label="50"></option>
      <option value="75" label="75"></option>
      <option value="100" label="100"></option>
    </datalist>
    

#### Result

### [Adding labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#adding_labels)

You can label tick marks by giving the `<option>` elements `label` attributes. However, the label content will not be displayed by default. You can use CSS to show the labels and to position them correctly. Here's one way you could do this.

#### HTML

html

    <label for="tempB">Choose a comfortable temperature:</label><br />
    <input type="range" id="tempB" name="temp" list="values" />
    
    <datalist id="values">
      <option value="0" label="very cold!"></option>
      <option value="25" label="cool"></option>
      <option value="50" label="medium"></option>
      <option value="75" label="getting warm!"></option>
      <option value="100" label="hot!"></option>
    </datalist>
    

#### CSS

css

    datalist {
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      writing-mode: vertical-lr;
      width: 200px;
    }
    
    option {
      padding: 0;
    }
    
    input[type="range"] {
      width: 200px;
      margin: 0;
    }
    

#### Result

### [Creating vertical range controls](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#creating_vertical_range_controls)

By default, browsers render range inputs as sliders with the knob sliding left and right.

To create a vertical range wherein the thumb slides up and down, set the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 property with a value of either `vertical-rl` or `vertical-lr`:

    <input type="range" min="0" max="10" value="8" />
    

css

    input[type="range"] {
      writing-mode: vertical-lr;
    }
    

This causes the range slider to render vertically:

You can also set the CSS [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
 property to the non-standard `slider-vertical` value if you want to support older versions of Chrome and Safari, and include the non-standard `orient="vertical"` attribute to support older versions of Firefox.

See [Creating vertical form controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls)
 for examples.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#technical_summary)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#value)<br>** | A string containing the string representation of the selected numeric value; use [`valueAsNumber`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/valueAsNumber "valueAsNumber")<br> to get the value as a number. |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported common attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br>, [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)<br>, [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)<br>, [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step) |
| **IDL attributes** | [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)<br>, `valueAsNumber` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | `[slider](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/slider_role) ` |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# range-state-(type=range)](https://html.spec.whatwg.org/multipage/input.html#range-state-(type=range)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range#see_also)

------------------------------------------------------------------------------------------------------

*   [HTML Forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     and the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
     interface it's based upon
*   [`<input type="number">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number)
    
*   [`validityState.rangeOverflow`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeOverflow)
     and [`validityState.rangeUnderflow`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeUnderflow)
    
*   [Controlling multiple parameters with ConstantSourceNode](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Controlling_multiple_parameters_with_ConstantSourceNode)
    
*   [Creating vertical form controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls)
    
*   [Styling the range element](https://css-tricks.com/sliding-nightmare-understanding-range-input/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 10, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/range/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/range (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Frange&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Frange%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Frange%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Frange%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F100cf25d92d3953f3c70ecaa2af637d5e42179d8%0A*+Document+last+modified%3A+2026-09-10T17%3A31%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")