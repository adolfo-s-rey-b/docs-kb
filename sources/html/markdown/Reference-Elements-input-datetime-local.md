*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#mdn-search)
    

`<input type="datetime-local">` HTML attribute value
====================================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since October 2021.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`datetime-local`** create input controls that let the user easily enter both a date and a time, including the year, month, and day as well as the time in hours and minutes.

The control's UI varies in general from browser to browser. The control is intended to represent _a local date and time_, not necessarily _the user's local date and time_. In other words, the input allows any valid combination of year, month, day, hour, and minute—even if such a combination is invalid in the user's local time zone (such as the one hour within a daylight saving time spring-forward transition gap).

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#try_it)

-----------------------------------------------------------------------------------------------------------

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#value)

---------------------------------------------------------------------------------------------------------

A string representing the value of the date entered into the input. The format of the date and time value used by this input type is described in [Local date and time strings](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats#local_date_and_time_strings)
.

You can set a default value for the input by including a date and time inside the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute, like so:

One thing to note is that the displayed date and time formats differ from the actual `value`; the displayed date and time are formatted according to the user's locale as reported by their operating system, whereas the date/time `value` is always formatted `YYYY-MM-DDTHH:mm`. When the above value is submitted to the server, for example, it will look like `party-date=2024-06-01T08:30`.

**Note:** Also bear in mind that if such data is submitted via HTTP [`GET`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET)
, the colon character will need to be escaped for inclusion in the URL parameters, e.g., `party-date=2024-06-01T08%3A30`. See [`encodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
 for one way to do this.

You can also get and set the date value in JavaScript using the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 `value` property, for example:

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#additional_attributes)

-----------------------------------------------------------------------------------------------------------------------------------------

In addition to the attributes common to all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, `datetime-local` inputs offer the following attributes.

### [max](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#max)

The latest date and time to accept. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 entered into the element is later than this timestamp, the element fails [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If the value of the `max` attribute isn't a valid string that follows the format `YYYY-MM-DDTHH:mm`, then the element has no maximum value.

This value must specify a date string later than or equal to the one specified by the `min` attribute.

### [min](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#min)

The earliest date and time to accept; timestamps earlier than this will cause the element to fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If the value of the `min` attribute isn't a valid string that follows the format `YYYY-MM-DDTHH:mm`, then the element has no minimum value.

This value must specify a date string earlier than or equal to the one specified by the `max` attribute.

### [step](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#step)

The `step` attribute is a number that specifies the granularity that the value must adhere to, or the special value `any`, which is described below. Only values which are a whole number of steps from the step base are valid. The step base is [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#min)
 if specified, [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 otherwise, or `0` (the Unix epoch, `1970-01-01T00:00`) if neither is provided.

For `datetime-local` inputs, the value of `step` is given in seconds and is treated as a number of milliseconds equal to 1000 times the `step` value (the underlying numeric value is in milliseconds). The default value is 60, indicating 1 minute.

A string value of `any` means that no stepping is implied, and any value is allowed (barring other constraints, such as [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#max)
). In reality, it has the same effect as `60` for `datetime-local` inputs because the picker UI in this case only allows selecting whole minutes.

**Note:** When the data entered by the user doesn't adhere to the stepping configuration, the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 may round to the nearest valid value, preferring numbers in the positive direction when there are two equally close options.

[Using datetime-local inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#using_datetime-local_inputs)

-----------------------------------------------------------------------------------------------------------------------------------------------------

Date/time inputs are convenient for the developer; they provide an easy UI for choosing dates and times, and they normalize the data format sent to the server, regardless of the user's locale. However, it is important to consider your users. Don't require your users to enter data that is not needed for your app to function.

### [Controlling input size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#controlling_input_size)

`<input type="datetime-local">` doesn't support form control sizing attributes such as [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)
. You'll have to resort to [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 for customizing the sizes of these elements.

### [Setting timezones](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#setting_timezones)

One thing the `datetime-local` input type doesn't provide is a way to set the time zone and/or locale of the date/time control. This was available in the `datetime` input type, but this type is now obsolete, having been removed from the spec. The main reasons why this was removed are a lack of implementation in browsers and concerns over the user interface/experience. It is easier to just have a control (or controls) for setting the date/time and then deal with the locale in a separate control.

For example, if you are creating a system where the user is likely to already be logged in, with their locale already set, you could provide the timezone in a [`hidden`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/hidden)
 input type. For example:

On the other hand, if you were required to allow the user to enter a time zone along with a date/time input, you could have a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 element to enable the user to set the right time zone by choosing a particular location from among a set of locations:

In either case, the date/time and time zone values would be submitted to the server as separate data points, and then you'd need to store them appropriately in the database on the server-side.

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#validation)

-------------------------------------------------------------------------------------------------------------------

By default, `<input type="datetime-local">` does not apply any validation to entered values. The UI implementations generally don't let you enter anything that isn't a date/time — which is helpful — but a user might still fill in no value and submit, or enter an invalid date and/or time (e.g., the 32nd of April).

You can use [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)
 to restrict the available dates (see [Setting maximum and minimum dates](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#setting_maximum_and_minimum_dates_and_times)
), and you can use the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)
 attribute to make filling in the date/time mandatory. As a result, browsers will display an error if you try to submit a date that is outside the set bounds or an empty date field.

Let's look at an example; here we've set minimum and maximum date/time values, and also made the field required:

If you try to submit the form with an incomplete date (or with a date outside the set bounds), the browser displays an error. Try playing with the example now:

Here's the CSS used in the above example. Here we make use of the [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 CSS properties to style the input based on whether the current value is valid. We put the icons on a [`<span>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/span)
 next to the input.

**Warning:** HTML form validation is _not_ a substitute for scripts that ensure that the entered data is in the proper format. It's far too easy for someone to make adjustments to the HTML that allow them to bypass the validation, or to remove it entirely. It's also possible for someone to bypass your HTML entirely and submit the data directly to your server. If your server-side code fails to validate the data it receives, problems can arise when improperly-formatted data is submitted (or data that is too large, is of the wrong type, and so forth).

**Note:** With a `datetime-local` input, the date value is always normalized to the format `YYYY-MM-DDTHH:mm`.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#examples)

---------------------------------------------------------------------------------------------------------------

### [Basic uses of datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#basic_uses_of_datetime-local)

The most basic use of `<input type="datetime-local">` involves a basic `<input>` and [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element combination, as seen below:

### [Setting maximum and minimum dates and times](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#setting_maximum_and_minimum_dates_and_times)

You can use the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)
 attributes to restrict the dates/times that can be chosen by the user. In the following example, we are setting a minimum datetime of `2025-06-01T08:30` and a maximum datetime of `2025-06-30T16:30`:

Only days in June 2025 can be selected. Depending on what browser you are using, times outside the specified values might not be selectable. In other browsers, invalid dates and times are selectable but will match [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 and [`:out-of-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range)
 and will fail [validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#validation)
.

In some browsers (Safari), the date picker will appear to allow any date, but the value will be clamped to the valid range when a date is selected.

The valid range included all times between the `min` and `max` values; the time of day is only constrained on the first and last dates in the range.

**Note:** You should be able to use the [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step)
 attribute to vary the number of days jumped each time the date is incremented (e.g., maybe you only want to make Saturdays selectable). However, this does not seem to work effectively in any implementation at the time of writing.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#technical_summary)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#value)<br>** | A string representing a date and time (in the local time zone), or empty. |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported common attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br>, [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#readonly)<br>, [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step) |
| **IDL attributes** | [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)<br>, [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)<br>, `valueAsDate`, `valueAsNumber` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | [no corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# local-date-and-time-state-(type=datetime-local)](https://html.spec.whatwg.org/multipage/input.html#local-date-and-time-state-(type=datetime-local)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#see_also)

---------------------------------------------------------------------------------------------------------------

*   The generic [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     element and the interface used to manipulate it, [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
    
*   [`<input type="date">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date)
     and [`<input type="time">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time)
    
*   [Date and time formats used in HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Date_and_time_formats)
    
*   [Date and Time picker tutorial](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/HTML5_input_types#date_and_time_pickers)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/datetime-local/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/datetime-local (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fdatetime-local&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fdatetime-local%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fdatetime-local%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fdatetime-local%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")