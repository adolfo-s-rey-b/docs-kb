*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#mdn-search)
    

`<input type="month">` HTML attribute value
===========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/925)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`month`** create input fields that let the user enter a month and year allowing a month and year to be easily entered. The value is a string whose value is in the format `YYYY-MM`, where `YYYY` is the four-digit year and `MM` is the month number.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#try_it)

--------------------------------------------------------------------------------------------------

    <label for="start">Start month:</label>
    
    <input type="month" id="start" name="start" min="2018-03" value="2018-05" />
    

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
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#value)

------------------------------------------------------------------------------------------------

A string representing the value of the month and year entered into the input, in the form YYYY-MM (four or more digit year, then a hyphen (`-`), followed by the two-digit month). The format of the month string used by this input type is described in [Month strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#month_strings)
.

### [Setting a default value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#setting_a_default_value)

You can set a default value for the input control by including a month and year inside the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute, like so:

html

    <label for="bday-month">What month were you born in?</label>
    <input id="bday-month" type="month" name="bday-month" value="2001-06" />
    

One thing to note is that the displayed date format differs from the actual `value`; most [user agents](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 display the month and year in a locale-appropriate form, based on the set locale of the user's operating system, whereas the date `value` is always formatted `yyyy-MM`.

When the above value is submitted to the server, for example, it will look like `bday-month=1978-06`.

### [Setting the value using JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#setting_the_value_using_javascript)

You can also get and set the date value in JavaScript using the [`HTMLInputElement.value`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/value)
 property, for example:

html

    <label for="bday-month">What month were you born in?</label>
    <input id="bday-month" type="month" name="bday-month" />
    

js

    const monthControl = document.querySelector('input[type="month"]');
    monthControl.value = "2001-06";
    

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#additional_attributes)

--------------------------------------------------------------------------------------------------------------------------------

In addition to the attributes common to [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, month inputs offer the following attributes.

### [list](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#list)

The values of the list attribute is the [`id`](https://developer.mozilla.org/en-US/docs/Web/API/Element/id "id")
 of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element located in the same document. The [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 provides a list of predefined values to suggest to the user for this input. Any values in the list that are not compatible with the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 are not included in the suggested options. The values provided are suggestions, not requirements: users can select from this predefined list or provide a different value.

### [max](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#max)

The latest year and month, in the string format discussed in the [Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#value)
 section above, to accept. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 entered into the element exceeds this, the element fails [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If the value of the `max` attribute isn't a valid string in `yyyy-MM` format, then the element has no maximum value.

This value must specify a year-month pairing later than or equal to the one specified by the `min` attribute.

### [min](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#min)

The earliest year and month to accept, in the same `yyyy-MM` format described above. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 of the element is less than this, the element fails [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If a value is specified for `min` that isn't a valid year and month string, the input has no minimum value.

This value must be a year-month pairing which is earlier than or equal to the one specified by the `max` attribute.

### [readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#readonly)

A Boolean attribute which, if present, means this field cannot be edited by the user. Its `value` can, however, still be changed from JavaScript code that directly sets the value of the [`HTMLInputElement.value`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/value)
 property.

**Note:** Because a read-only field cannot have a value, `required` does not have any effect on inputs with the `readonly` attribute also specified.

### [step](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#step)

The `step` attribute is a number that specifies the granularity that the value must adhere to, or the special value `any`, which is described below. Only values which are a whole number of steps from the step base are valid. The step base is [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#min)
 if specified, [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 otherwise, or `0` (the Unix epoch, `1970-01`) if neither is provided.

For `month` inputs, the value of `step` is given in months. The default value of `step` is 1, indicating 1 month.

A string value of `any` means that no stepping is implied, and any value is allowed (barring other constraints, such as [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#max)
). In reality, it has the same effect as `1` for `month` inputs because the picker UI only allows selecting whole months.

**Note:** When the data entered by the user doesn't adhere to the stepping configuration, the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 may round to the nearest valid value, preferring numbers in the positive direction when there are two equally close options.

[Using month inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#using_month_inputs)

--------------------------------------------------------------------------------------------------------------------------

Date-related inputs (including `month`) sound convenient at first glance; they promise an easy UI for choosing dates, and they normalize the data format sent to the server, regardless of the user's locale. However, there are issues with `<input type="month">` because at this time, many major browsers don't yet support it.

We'll look at basic and more complex uses of `<input type="month">`, then offer advice on mitigating the browser support issue in the section [Handling browser support](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#handling_browser_support)
.

### [Basic uses of month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#basic_uses_of_month)

The most basic use of `<input type="month">` involves a basic [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 and [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element combination, as seen below:

html

    <label for="bday-month">What month were you born in?</label>
    <input id="bday-month" type="month" name="bday-month" />
    

### [Setting maximum and minimum dates](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#setting_maximum_and_minimum_dates)

You can use the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)
 attributes to restrict the range of dates that the user can choose. In the following example we specify a minimum month of `1900-01` and a maximum month of `2013-12`:

html

    <label for="bday-month">What month were you born in?</label>
    <input
      id="bday-month"
      type="month"
      name="bday-month"
      min="1900-01"
      max="2013-12" />
    

The result here is that:

*   Only months between in January 1900 and December 2013 can be selected; months outside that range can't be scrolled to in the control.
*   Depending on what browser you are using, you might find that months outside the specified range might not be selectable in the month picker (e.g., Edge), or invalid (see [Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#validation)
    ) but still available (e.g., Chrome).

### [Controlling input size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#controlling_input_size)

`<input type="month">` doesn't support form sizing attributes such as [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
. You'll have to resort to [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 for sizing needs.

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#validation)

----------------------------------------------------------------------------------------------------------

By default, `<input type="month">` does not apply any validation to entered values. The UI implementations generally don't let you enter anything that isn't a date — which is helpful — but you can still submit the form with the `month` input empty, or enter an invalid date (e.g., the 32nd of April).

To help avoid this, you can use [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)
 to restrict the available dates (see [Setting maximum and minimum dates](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#setting_maximum_and_minimum_dates)
), and in addition use the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute to make filling in the date mandatory. As a result, supporting browsers will display an error if you try to submit a date that is outside the set bounds, or an empty date field.

Let's look at an example; here we've set minimum and maximum dates, and also made the field required:

html

    <form>
      <div>
        <label for="month">
          What month would you like to visit (June to Sept.)?
        </label>
        <input
          id="month"
          type="month"
          name="month"
          min="2022-06"
          max="2022-09"
          required />
        <span class="validity"></span>
      </div>
      <div>
        <input type="submit" value="Submit form" />
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

If you try to submit the form without both the month and year specified (or with a date outside the set bounds), the browser displays an error. Try playing with the example now:

Here's the CSS used in the above example. Here we make use of the [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 CSS properties to style the input based on whether the current value is valid. We had to put the icons on a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 next to the input, not on the input itself, because in Chrome the generated content is placed inside the form control, and can't be styled or shown effectively.

css

    div {
      margin-bottom: 10px;
      position: relative;
    }
    
    input[type="number"] {
      width: 100px;
    }
    
    input + span {
      padding-right: 30px;
    }
    
    input:invalid + span::after {
      position: absolute;
      content: "✖";
      padding-left: 5px;
    }
    
    input:valid + span::after {
      position: absolute;
      content: "✓";
      padding-left: 5px;
    }
    

**Warning:** HTML form validation is _not_ a substitute for scripts that ensure that the entered data is in the proper format. It's far too easy for someone to make adjustments to the HTML that allow them to bypass the validation, or to remove it entirely. It's also possible for someone to bypass your HTML entirely and submit the data directly to your server. If your server-side code fails to validate the data it receives, disaster could strike when improperly-formatted data is submitted (or data which is too large, of the wrong type, and so forth).

[Handling browser support](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#handling_browser_support)

--------------------------------------------------------------------------------------------------------------------------------------

The control's UI varies in general from browser to browser; at the moment support is patchy, with only Chromium browsers on desktop and mobile browsers having usable implementations. The control is usually presented as either a calendar-like grid or two wheel pickers.

In browsers that don't support `month` inputs, the control degrades gracefully to [`<input type="text">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
, although there may be automatic validation of the entered text to ensure it's formatted as expected. But this creates problems both in terms of consistency of user interface (the presented control will be different), and data handling.

The second problem is the more serious of the two. As mentioned earlier, with a `month` input the actual value is always normalized to the format `yyyy-mm`. On the other hand, in its default configuration, a `text` input has no idea what format the date should be in, and this is an issue because of the number of different ways in which people write dates. For example:

*   `mmyyyy` (072022)
*   `mm/yyyy` (07/2022)
*   `mm-yyyy` (07-2022)
*   `yyyy-mm` (2022-07)
*   `Month yyyy` (July 2022)
*   and so forth…

One way around this is to put a [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)
 attribute on your `month` input. Even though the `month` input doesn't use it, if the browser falls back to treating it like a `text` input, the pattern will be used. For example, try viewing the following demo in a browser that doesn't support `month` inputs:

html

    <form>
      <div>
        <label for="month">
          What month would you like to visit (June to Sept.)?
        </label>
        <input
          id="month"
          type="month"
          name="month"
          min="2022-06"
          max="2022-09"
          required
          pattern="[0-9]{4}-[0-9]{2}" />
        <span class="validity"></span>
      </div>
      <div>
        <input type="submit" value="Submit form" />
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

If you try submitting it, you'll see that the browser now displays an error message (and highlights the input as invalid) if your entry doesn't match the pattern `nnnn-nn`, where `n` is a number from 0 to 9. Of course, this doesn't stop people from entering invalid dates (such as `0000-42`), or incorrectly formatted dates that follow the pattern.

There's also the problem that the user won't necessarily know which of the many date formats is expected. We have work left to do.

    div {
      margin-bottom: 10px;
      position: relative;
    }
    
    input[type="number"] {
      width: 100px;
    }
    
    input + span {
      padding-right: 30px;
    }
    
    input:invalid + span::after {
      position: absolute;
      content: "✖";
      padding-left: 5px;
    }
    
    input:valid + span::after {
      position: absolute;
      content: "✓";
      padding-left: 5px;
    }
    

The best way to deal with dates in forms in a cross-browser way (until all major browsers have supported them for a while) is to get the user to enter the month and year in separate controls ([`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 elements being popular; see below for an implementation), or use JavaScript libraries such as the [jQuery date picker](https://jqueryui.com/datepicker/ "External link (opens in new tab)")
 plugin.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#examples)

------------------------------------------------------------------------------------------------------

In this example, we create two sets of UI elements, each designed to let the user select a month and year. The first is a native `month` input, and the other is a pair of [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 elements that allow choosing a month and year independently, for compatibility with browsers that don't yet support `<input type="month">`.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#html)

The HTML that requests the month and year looks like this:

html

    <div class="nativeDatePicker">
      <label for="month-visit">What month would you like to visit us?</label>
      <input type="month" id="month-visit" name="month-visit" />
      <span class="validity"></span>
    </div>
    <p class="fallbackLabel">What month would you like to visit us?</p>
    <div class="fallbackDatePicker">
      <div>
        <span>
          <label for="month">Month:</label>
          <select id="month" name="month">
            <option selected>January</option>
            <option>February</option>
            <option>March</option>
            <option>April</option>
            <option>May</option>
            <option>June</option>
            <option>July</option>
            <option>August</option>
            <option>September</option>
            <option>October</option>
            <option>November</option>
            <option>December</option>
          </select>
        </span>
        <span>
          <label for="year">Year:</label>
          <select id="year" name="year"></select>
        </span>
      </div>
    </div>
    

The [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 with the ID `nativeDatePicker` uses the `month` input type to request the month and year, while the `<div>` with the ID `fallbackDatePicker` instead uses a pair of `<select>` elements. The first requests the month, and the second the year.

The `<select>` for choosing the month is hardcoded with the names of the months, as they don't change (leaving localization out of things). The list of available year values is dynamically generated depending on the current year (see the code comments below for detailed explanations of how these functions work).

    div {
      margin-bottom: 10px;
      position: relative;
    }
    
    input[type="number"] {
      width: 100px;
    }
    
    input + span {
      padding-right: 30px;
    }
    
    input:invalid + span::after {
      position: absolute;
      content: "✖";
      padding-left: 5px;
    }
    
    input:valid + span::after {
      position: absolute;
      content: "✓";
      padding-left: 5px;
    }
    

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#javascript)

The JavaScript code that handles selecting which approach to use and to set up the list of years to include in the non-native year `<select>` follows.

The part of the example that may be of most interest is the feature detection code. In order to detect whether the browser supports `<input type="month">`, we create a new [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element, try setting its `type` to `month`, then immediately check what its type is set to. Browsers that don't support type `month` will return `text`, since that's What month falls back to when not supported. If `<input type="month">` is not supported, we hide the native picker and show the fallback picker UI instead.

js

    // Get UI elements
    const nativePicker = document.querySelector(".nativeDatePicker");
    const fallbackPicker = document.querySelector(".fallbackDatePicker");
    const fallbackLabel = document.querySelector(".fallbackLabel");
    
    const yearSelect = document.querySelector("#year");
    const monthSelect = document.querySelector("#month");
    
    // Hide fallback initially
    fallbackPicker.style.display = "none";
    fallbackLabel.style.display = "none";
    
    // Test whether a new date input falls back to a text input or not
    const test = document.createElement("input");
    
    try {
      test.type = "month";
    } catch (e) {
      console.log(e.description);
    }
    
    // If it does, run the code inside the if () {} block
    if (test.type === "text") {
      // Hide the native picker and show the fallback
      nativePicker.style.display = "none";
      fallbackPicker.style.display = "block";
      fallbackLabel.style.display = "block";
    
      // Populate the years dynamically
      // (the months are always the same, therefore hardcoded)
      populateYears();
    }
    
    function populateYears() {
      // Get the current year as a number
      const date = new Date();
      const year = date.getFullYear();
    
      // Make this year, and the 100 years before it available in the year <select>
      for (let i = 0; i <= 100; i++) {
        const option = document.createElement("option");
        option.textContent = year - i;
        yearSelect.appendChild(option);
      }
    }
    

**Note:** Remember that some years have 53 weeks in them (see [Weeks per year](https://en.wikipedia.org/wiki/ISO_week_date#Weeks_per_year "External link (opens in new tab)")
)! You'll need to take this into consideration when developing production apps.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#technical_summary)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#value)<br>** | A string representing a month and year, or empty. |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported common attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br>, [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#readonly)<br>, [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step) |
| **IDL attributes** | [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)<br>, `valueAsDate`, `valueAsNumber` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | [no corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# month-state-(type=month)](https://html.spec.whatwg.org/multipage/input.html#month-state-(type=month)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#see_also)

------------------------------------------------------------------------------------------------------

*   The generic [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     element and the interface used to manipulate it, [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
    
*   [Date and time formats used in HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats)
    
*   [Date and Time picker tutorial](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/HTML5_input_types#date_and_time_pickers)
    
*   [`<input type="datetime-local">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
    , [`<input type="date">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date)
    , [`<input type="time">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time)
    , and [`<input type="week">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/month/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/month (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fmonth&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fmonth%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fmonth%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fmonth%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")