*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#mdn-search)
    

`<input type="week">` HTML attribute value
==========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/926)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`week`** create input fields allowing easy entry of a year plus the [ISO 8601 week number](https://en.wikipedia.org/wiki/ISO_8601#Week_dates "External link (opens in new tab)")
 during that year (i.e., week 1 to [52 or 53](https://en.wikipedia.org/wiki/ISO_8601#Week_dates "External link (opens in new tab)")
).

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#try_it)

-------------------------------------------------------------------------------------------------

    <label for="camp-week">Choose a week in May or June:</label>
    
    <input
      type="week"
      name="week"
      id="camp-week"
      min="2018-W18"
      max="2018-W26"
      required />
    

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
    

The control's user interface varies from browser to browser; cross-browser support is currently a bit limited, with only Chrome/Opera and Microsoft Edge supporting it at this time. In non-supporting browsers, the control degrades gracefully to function identically to [`<input type="text">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
.

![An input reading 'week 01, 2017'. The background of the 2017 is the same blue as the focus ring. There are 3 icons in the input: x or clear, a spinner with small up and down arrows, and a larger down arrow. A calendar is a pop-up below the input set to January 2017. The first column of the calendar is the week: 52, 1, 2, 3, 4, 5. the full month calendar is to the right of that. The row with Week 1 and January 2 to 8 is highlighted. On the same line as the month, there are buttons to move right and left for the next and previous months.](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week/week-control-chrome.png)

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#value)

-----------------------------------------------------------------------------------------------

A string representing the value of the week/year entered into the input. The format of the date and time value used by this input type is described in [Week strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#week_strings)
.

You can set a default value for the input by including a value inside the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute, like so:

html

    <label for="week">What week would you like to start?</label>
    <input id="week" type="week" name="week" value="2017-W01" />
    

One thing to note is that the displayed format may differ from the actual `value`, which is always formatted `yyyy-Www`. When the above value is submitted to the server, for example, browsers may display it as `Week 01, 2017`, but the submitted value will always look like `week=2017-W01`.

You can also get and set the value in JavaScript using the input element's [`value`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/value "value")
 property, for example:

js

    const weekControl = document.querySelector('input[type="week"]');
    weekControl.value = "2017-W45";
    

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#additional_attributes)

-------------------------------------------------------------------------------------------------------------------------------

In addition to the attributes common to [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, week inputs offer the following attributes.

### [max](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#max)

The latest (time-wise) year and week number, in the string format discussed in the [Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#value)
 section above, to accept. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 entered into the element exceeds this, the element fails [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If the value of the `max` attribute isn't a valid week string, then the element has no maximum value.

This value must be greater than or equal to the year and week specified by the `min` attribute.

### [min](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#min)

The earliest year and week to accept. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 of the element is less than this, the element fails [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If a value is specified for `min` that isn't a valid week string, the input has no minimum value.

This value must be less than or equal to the value of the `max` attribute.

### [readonly](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#readonly)

A Boolean attribute which, if present, means this field cannot be edited by the user. Its `value` can, however, still be changed by JavaScript code directly setting the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 `value` property.

**Note:** Because a read-only field cannot have a value, `required` does not have any effect on inputs with the `readonly` attribute also specified.

### [step](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#step)

The `step` attribute is a number that specifies the granularity that the value must adhere to, or the special value `any`, which is described below. Only values which are a whole number of steps from the step base are valid. The step base is [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#min)
 if specified, [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 otherwise, or −259,200,000 (the start of week `1970-W01`) if neither is provided.

For `week` inputs, the value of `step` is given in weeks and is treated as a number of milliseconds equal to 604,800,000 times the `step` value (the underlying numeric value is in milliseconds). The default value is 1, indicating 1 week.

A string value of `any` means that no stepping is implied, and any value is allowed (barring other constraints, such as [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#max)
). In reality, it has the same effect as `1` for `week` inputs because the picker UI only allows selecting whole weeks.

**Note:** When the data entered by the user doesn't adhere to the stepping configuration, the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 may round to the nearest valid value, preferring numbers in the positive direction when there are two equally close options.

[Using week inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#using_week_inputs)

-----------------------------------------------------------------------------------------------------------------------

Week inputs sound convenient at first glance, since they provide an easy UI for choosing weeks, and they normalize the data format sent to the server, regardless of the user's browser or locale. However, there are issues with `<input type="week">` because browser support is not guaranteed across all browsers.

We'll look at basic and more complex uses of `<input type="week">`, then offer advice on mitigating the browser support issue later on (see [Handling browser support](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#handling_browser_support)
).

### [Basic uses of week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#basic_uses_of_week)

The most basic use of `<input type="week">` involves a basic `<input>` and [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element combination, as seen below:

html

    <label for="week">What week would you like to start?</label>
    <input id="week" type="week" name="week" />
    

### [Controlling input size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#controlling_input_size)

`<input type="week">` doesn't support form sizing attributes such as [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
. You'll have to resort to [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 for sizing needs.

### [Using the step attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#using_the_step_attribute)

You should be able to use the [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step)
 attribute to vary the number of weeks jumped whenever they are incremented or decremented, however it doesn't seem to have any effect on supporting browsers.

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#validation)

---------------------------------------------------------------------------------------------------------

By default, `<input type="week">` does not apply any validation to entered values. The UI implementations generally don't let you specify anything that isn't a valid week/year, which is helpful, but it's still possible to submit with the field empty, and you might want to restrict the range of choosable weeks.

### [Setting maximum and minimum weeks](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#setting_maximum_and_minimum_weeks)

You can use the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)
 attributes to restrict the valid weeks that can be chosen by the user. In the following example we are setting a minimum value of `Week 01, 2017` and a maximum value of `Week 52, 2017`:

html

    <label for="week">What week would you like to start?</label>
    <input id="week" type="week" name="week" min="2017-W01" max="2017-W52" />
    <span class="validity"></span>
    

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
    

The result here is that only weeks between W01 and W52 in 2017 will be seen as valid and be selectable in supporting browsers.

### [Making week values required](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#making_week_values_required)

In addition you can use the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute to make filling in the week mandatory. As a result, supporting browsers will display an error if you try to submit an empty week field.

Let's look at an example; here we've set minimum and maximum weeks, and also made the field required:

html

    <form>
      <div>
        <label for="week">What week would you like to start?</label>
        <input
          id="week"
          type="week"
          name="week"
          min="2017-W01"
          max="2017-W52"
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
    

If you try to submit the form with no value, the browser displays an error. Try playing with the example now:

Here is a screenshot for those of you who aren't using a supporting browser:

![The week form control has two dashes where the week number should be. A popup with a yellow warning symbol and a 'Please fill out this field' is emanating from the two dashes, which are highlighted in blue, the same blue as the input's focus ring.](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week/week-validation-chrome.png)

**Warning:** HTML form validation is _not_ a substitute for scripts that ensure that the entered data is in the proper format. It's far too easy for someone to make adjustments to the HTML that allow them to bypass the validation, or to remove it entirely. It's also possible for someone to bypass your HTML entirely and submit the data directly to your server. If your server-side code fails to validate the data it receives, disaster could strike when improperly-formatted data is submitted (or data which is too large, of the wrong type, and so forth).

[Handling browser support](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#handling_browser_support)

-------------------------------------------------------------------------------------------------------------------------------------

As mentioned above, the major problem with using week inputs right now is browser support: Safari and Firefox don't support it on desktop, and old versions of IE don't support it.

Mobile platforms such as Android and iOS make perfect use of such input types, providing specialist UI controls that make it really easy to select values in a touchscreen environment. For example, the `week` picker on Chrome for Android looks like this:

![A modal popup. The header reads 'set week'. There are two columns: the left has 36 in the middle at full opacity, with 35 above it and 37 below being semi-opaque. On the right side, 2017 is fully opaque. There are no other options. Three text links or buttons on the bottom include 'clear' on the 'left' and 'cancel' and 'set' on the right.](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week/week-chrome-android.png)

Non-supporting browsers gracefully degrade to a text input, but this creates problems both in terms of consistency of user interface (the presented control will be different), and data handling.

The second problem is the more serious. As mentioned earlier, with a `week` input the actual value is always normalized to the format `yyyy-Www`. When the browser falls back to a generic text input, there's nothing to guide the user toward correctly formatting the input (and it's certainly not intuitive). There are multiple ways in which people could write week values; for example:

*   `Week 1 2017`
*   `Jan 2-8 2017`
*   `2017-W01`
*   etc.

The best way to deal with week/years in forms in a cross-browser way at the moment is to get the user to enter the week number and year in separate controls ([`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 elements being popular; see below for an example), or use JavaScript libraries such as [jQuery date picker](https://jqueryui.com/datepicker/ "External link (opens in new tab)")
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#examples)

-----------------------------------------------------------------------------------------------------

In this example we create two sets of UI elements for choosing weeks: a native picker created using `<input type="week">`, and a set of two [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 elements for choosing weeks/years in older browsers that don't support the `week` input type.

The HTML looks like so:

html

    <div class="nativeWeekPicker">
      <label for="week">What week would you like to start?</label>
      <input
        id="week"
        type="week"
        name="week"
        min="2017-W01"
        max="2018-W52"
        required />
      <span class="validity"></span>
    </div>
    <p class="fallbackLabel">What week would you like to start?</p>
    <div class="fallbackWeekPicker">
      <div>
        <span>
          <label for="week">Week:</label>
          <select id="fallbackWeek" name="week"></select>
        </span>
        <span>
          <label for="year">Year:</label>
          <select id="year" name="year">
            <option value="2017" selected>2017</option>
            <option value="2018">2018</option>
          </select>
        </span>
      </div>
    </div>
    

The week values are dynamically generated by the JavaScript code below.

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
    

The other part of the code that may be of interest is the feature detection code. To detect whether the browser supports `<input type="week">`, we create a new [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element, try setting its `type` to `week`, then immediately check what its `type` is set to. Non-supporting browsers will return `text`, because the `week` type falls back to type `text`. If `<input type="week">` is not supported, we hide the native picker and show the fallback picker UI ([`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
s) instead.

js

    // Get UI elements
    const nativePicker = document.querySelector(".nativeWeekPicker");
    const fallbackPicker = document.querySelector(".fallbackWeekPicker");
    const fallbackLabel = document.querySelector(".fallbackLabel");
    
    const yearSelect = document.querySelector("#year");
    const weekSelect = document.querySelector("#fallbackWeek");
    
    // Hide fallback initially
    fallbackPicker.style.display = "none";
    fallbackLabel.style.display = "none";
    
    // Test whether a new date input falls back to a text input or not
    const test = document.createElement("input");
    
    try {
      test.type = "week";
    } catch (e) {
      console.log(e.description);
    }
    
    // If it does, run the code inside the if () {} block
    if (test.type === "text") {
      // Hide the native picker and show the fallback
      nativePicker.style.display = "none";
      fallbackPicker.style.display = "block";
      fallbackLabel.style.display = "block";
    
      // populate the weeks dynamically
      populateWeeks();
    }
    
    function populateWeeks() {
      // Populate the week select with 52 weeks
      for (let i = 1; i <= 52; i++) {
        const option = document.createElement("option");
        option.textContent = i < 10 ? `0${i}` : i;
        weekSelect.appendChild(option);
      }
    }
    

**Note:** Remember that some years have 53 weeks in them (see [Weeks per year](https://en.wikipedia.org/wiki/ISO_week_date#Weeks_per_year "External link (opens in new tab)")
)! You'll need to take this into consideration when developing production apps.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#technical_summary)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#value)<br>** | A string representing a week and year, or empty |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported common attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br>, [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#readonly)<br>, [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step) |
| **IDL attributes** | [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)<br>, `valueAsDate`, `valueAsNumber` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | [no corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# week-state-(type=week)](https://html.spec.whatwg.org/multipage/input.html#week-state-(type=week)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#see_also)

-----------------------------------------------------------------------------------------------------

*   The generic [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     element and the interface used to manipulate it, [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
    
*   [Date and time formats used in HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats)
    
*   [`<input type="datetime-local">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
    , [`<input type="date">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date)
    , [`<input type="time">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time)
    , and [`<input type="month">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/week/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/week (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fweek&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fweek%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fweek%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fweek%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")