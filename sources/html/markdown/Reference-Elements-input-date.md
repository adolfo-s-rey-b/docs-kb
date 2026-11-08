*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#mdn-search)
    

`<input type="date">` HTML attribute value
==========================================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2021.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of **`type="date"`** create input fields that let the user enter a date. The appearance of the date picker input UI varies based on the browser and operating system. The value is normalized to the format `yyyy-mm-dd`.

The resulting value includes the year, month, and day, but _not_ the time. The [time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time)
 and [datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
 input types support time and date+time input.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#try_it)

-------------------------------------------------------------------------------------------------

    <label for="start">Start date:</label>
    
    <input
      type="date"
      id="start"
      name="trip-start"
      value="2018-07-22"
      min="2018-01-01"
      max="2018-12-31" />
    

    label {
      display: block;
      font:
        1rem "Fira Sans",
        sans-serif;
    }
    
    input,
    label {
      margin: 0.4rem 0;
    }
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#value)

-----------------------------------------------------------------------------------------------

A string representing the date entered in the input. The date is formatted according to [Date strings format](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#date_strings)
.

You can set a default value for the input with a date inside the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute, like so:

html

    <input type="date" value="2017-06-01" />
    

**Note:** The displayed date format will differ from the actual `value` — the displayed date is formatted _based on the locale of the user's browser_, but the parsed `value` is always formatted `yyyy-mm-dd`.

You can get and set the date value in JavaScript with the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 `value` and `valueAsNumber` properties. For example:

js

    const dateControl = document.querySelector('input[type="date"]');
    dateControl.value = "2017-06-01";
    console.log(dateControl.value); // prints "2017-06-01"
    console.log(dateControl.valueAsNumber); // prints 1496275200000, a JavaScript timestamp (ms)
    

This code finds the first [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element whose `type` is `date`, and sets its value to `2017-06-01` (June 1st, 2017). It then reads that value back in string and number formats.

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#additional_attributes)

-------------------------------------------------------------------------------------------------------------------------------

In addition to [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 and the [input attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#attributes)
 common to all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, the `date` input supports the following attributes:

### [max](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#max)

The latest date to accept. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 entered into the element occurs afterward, the element fails [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If the value of the `max` attribute isn't a possible date string in the format `yyyy-mm-dd`, then the element has no maximum date value.

If both the `max` and `min` attributes are set, this value must be a date string **later than or equal to** the one in the `min` attribute.

### [min](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#min)

The earliest date to accept. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 entered into the element occurs beforehand, the element fails [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If the value of the `min` attribute isn't a possible date string in the format `yyyy-mm-dd`, then the element has no minimum date value.

If both the `max` and `min` attributes are set, this value must be a date string **earlier than or equal to** the one in the `max` attribute.

### [step](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#step)

The `step` attribute is a number that specifies the granularity that the value must adhere to, or the special value `any`, which is described below. Only values which are a whole number of steps from the step base are valid. The step base is [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#min)
 if specified, [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 otherwise, or `0` (the Unix epoch, `1970-01-01`) if neither is provided.

For `date` inputs, the value of `step` is given in days and is treated as a number of milliseconds equal to 86,400,000 times the `step` value (the underlying numeric value is in milliseconds). The default value is 1, indicating 1 day.

A string value of `any` means that no stepping is implied, and any value is allowed (barring other constraints, such as [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#max)
). In reality, it has the same effect as `1` for `date` inputs because the picker UI only allows selecting whole days.

**Note:** When the data entered by the user doesn't adhere to the stepping configuration, the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 may round to the nearest valid value, preferring numbers in the positive direction when there are two equally close options.

[Using date inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#using_date_inputs)

-----------------------------------------------------------------------------------------------------------------------

Date inputs provide an easy interface for choosing dates, and they normalize the data format sent to the server regardless of the user's locale.

In this section, we'll look at basic and then more complex uses of `<input type="date">`.

### [Basic uses of date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#basic_uses_of_date)

The most basic use of `<input type="date">` involves one `<input>` combined with its [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
, as seen below:

html

    <label>
      Enter your birthday:
      <input type="date" name="bday" />
    </label>
    

If this input is included in a form submitted to `https://example.com` using the `GET` method, the entered date is sent under the key `bday` — resulting in a URL like `https://example.com/?bday=1955-06-08`.

### [Setting maximum and minimum dates](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#setting_maximum_and_minimum_dates)

You can use the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)
 attributes to restrict the dates that can be chosen by the user. In the following example, we set a minimum date of `2017-04-01` and a maximum date of `2017-04-30`:

html

    <label>
      Choose your preferred party date:
      <input type="date" name="party" min="2017-04-01" max="2017-04-30" />
    </label>
    

The result is that only days in April 2017 can be selected — the month and year parts of the textbox will be uneditable, and dates outside April 2017 can't be selected in the picker widget.

You can use the [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step)
 attribute to vary the number of days jumped each time the date is incremented (e.g., to only make Saturdays selectable).

### [Controlling input size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#controlling_input_size)

`<input type="date">` doesn't support form sizing attributes such as [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
. Prefer [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 for sizing it.

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#validation)

---------------------------------------------------------------------------------------------------------

By default, `<input type="date">` doesn't validate the entered value beyond its format. The interfaces generally don't let you enter anything that isn't a date — which is helpful.

If you use [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)
 to restrict the available dates (see [Setting maximum and minimum dates](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#setting_maximum_and_minimum_dates)
), the form control disables invalid dates, and will display an error if you try to submit a date that is out of bounds.

You can also use the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute to make filling in the date mandatory — an error will be displayed if you try to submit an empty date field.

Let's look at an example of minimum and maximum dates, and also make a field required:

html

    <form>
      <label>
        Choose your preferred party date (required, April 1st to 20th):
        <input
          type="date"
          name="party"
          min="2017-04-01"
          max="2017-04-20"
          required />
        <span class="validity"></span>
      </label>
    
      <p>
        <button>Submit</button>
      </p>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

If you try to submit the form with an incomplete date (or with a date outside the set bounds), the browser displays an error. Try playing with the example now:

Here's the CSS used in the above example. We make use of the [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 [pseudo-elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 to add an icon next to the input, based on whether the current value is valid. We had to put the icon on a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 next to the input, not on the input itself, because in Chrome at least the input's generated content is placed inside the form control, and can't be styled or shown effectively.

css

    label {
      display: flex;
      align-items: center;
    }
    
    span::after {
      padding-left: 5px;
    }
    
    input:invalid + span::after {
      content: "✖";
    }
    
    input:valid + span::after {
      content: "✓";
    }
    

**Warning:** Client-side form validation _is not a substitute_ for validating on the server. It's easy for someone to modify the HTML, or bypass your HTML entirely and submit the data directly to your server. If your server fails to validate the received data, disaster could strike with data that is badly-formatted, too large, of the wrong type, etc.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#examples)

-----------------------------------------------------------------------------------------------------

In this example, we create a date picker using the native `<input type="date">` picker.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#html)

The HTML looks like so:

html

    <div class="nativeDatePicker">
      <label for="bday">Enter your birthday:</label>
      <input type="date" id="bday" name="bday" />
      <span class="validity"></span>
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#css)

The CSS looks like so:

css

    input:invalid + span::after {
      content: " ✖";
    }
    
    input:valid + span::after {
      content: " ✓";
    }
    

### [Results](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#results)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#technical_summary)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#value)<br>** | A string representing a date in YYYY-MM-DD format, or empty |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported common attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br>, [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#readonly)<br>, [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step) |
| **IDL attributes** | [`value`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/value)<br>, [`valueAsDate`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/valueAsDate)<br>, [`valueAsNumber`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/valueAsNumber) |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | [no corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# date-state-(type=date)](https://html.spec.whatwg.org/multipage/input.html#date-state-(type=date)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#see_also)

-----------------------------------------------------------------------------------------------------

*   The generic [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     element and the interface used to manipulate it, [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
    
*   [Date and Time picker tutorial](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/HTML5_input_types#date_and_time_pickers)
    
*   [Date and time formats used in HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/date/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/date (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fdate&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fdate%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fdate%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fdate%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")