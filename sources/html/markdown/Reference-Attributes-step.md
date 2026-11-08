*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step#mdn-search)
    

`step` HTML attribute
=====================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`step`** attribute is a number that specifies the granularity that the value must adhere to or the keyword `any`. It is valid for the numeric input types, including the [date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date)
, [month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month)
, [week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week)
, [time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time)
, [datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
, [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number)
 and [range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 types.

The `step` sets the _stepping interval_ when clicking up and down spinner buttons, moving a slider left and right on a range, and validating the different date types. If not explicitly included, `step` defaults to 1 for `number` and `range`, and 1 unit type (minute, week, month, day) for the date/time input types. The value must be a positive number - integer or float — or the special value `any`, which means no stepping is implied and any value is allowed (barring other constraints, such as [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)
).

Only values which are a whole number of steps from the step base are valid. The step base is [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)
 if specified, [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 otherwise, or `0` if neither is provided (except for `week`, which has a default step base of −259,200,000, representing the start of week `1970-W01`).

[Syntax](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step#syntax)

---------------------------------------------------------------------------------------------

|     |     |     |
| --- | --- | --- |Default values for step
| Input type | Value | Example |
| --- | --- | --- |
| [date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date) | 1 (day) | `<input type="date" min="2019-12-25" step="1">` |
| [month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month) | 1 (month) | `<input type="month" min="2019-12" step="12">` |
| [week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week) | 1 (week) | `<input type="week" min="2019-W23" step="2">` |
| [time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time) | 60 (seconds) | `<input type="time" min="09:00" step="900">` |
| [datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local) | 60 (seconds) | `<input type="datetime-local" min="2019-12-25T19:30" step="900">` |
| [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number) | 1   | `<input type="number" min="0" step="0.1" max="10">` |
| [range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range) | 1   | `<input type="range" min="0" step="2" max="10">` |

If `any` is not explicitly set, valid values for the `number`, date/time input types, and `range` input types are equal to the basis for stepping - the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)
 value and increments of the step value, up to the [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)
 value, if specified. The following example results in any even integer, 10 or greater, being valid:

html

    <input type="number" min="10" step="2" />
    

If `step` is omitted, any integer is valid but floats like 4.2 are not valid as `step` defaults to 1. For 4.2 to be valid:

*   either `step` would have to be set to `any`, 0.1, or 0.2,
*   or the `min` value would have to be a number ending in .2, such as 0.2, 1.2, or -5.2.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step#examples)

-------------------------------------------------------------------------------------------------

### [`min` impact on step](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step#min_impact_on_step)

The value of `min` defines valid values, even if the `step` attribute is not included. This is because `step` defaults to `1` for the `number` input type.

In this example, we add a big red border around invalid inputs:

css

    input:invalid {
      border: solid red 3px;
    }
    

We then define an input with a minimum value of 1.2 and a step value of 2:

html

    <input id="myNumber" name="myNumber" type="number" step="2" min="1.2" />
    

Valid values include 1.2, 3.2, 5.2, 7.2, 9.2, 11.2, and so on. Only floats with an odd-numbered integer part and a decimal part of .2 are valid. The number spinner, if present, generates valid float values of 1.2 and greater, in increments of 2.

**Note:** When the data entered by the user doesn't adhere to the stepping configuration, the value is considered invalid in constraint validation and will match the [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 and [`:out-of-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range)
 pseudoclasses.

See [Client-side validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 and [`stepMismatch`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/stepMismatch "stepMismatch")
 for more information.

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step#accessibility_concerns)

-----------------------------------------------------------------------------------------------------------------------------

Provide instructions to help users understand how to complete the form and use individual form controls. Indicate any required and optional input, data formats, and other relevant information. When using the `min` attribute, ensure this minimum requirement is understood by the user. Providing instructions within the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 may be sufficient. If providing instructions outside of labels, which allows more flexible positioning and design, consider using [`aria-labelledby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby)
 or [`aria-describedby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step#specifications)

-------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-input-step](https://html.spec.whatwg.org/multipage/input.html#attr-input-step) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step#see_also)

-------------------------------------------------------------------------------------------------

*   [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)
    
*   [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)
    
*   [Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
    
*   [Form validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
    
*   [`validityState.stepMismatch`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/stepMismatch)
    
*   [`:out-of-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date)
    , [month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month)
    , [week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week)
    , [time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time)
    , [datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
    , [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number)
     and [range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
     types, and the [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/step/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/step (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fstep&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fstep%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fstep%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fstep%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb50ed7ac1c2ca21b4b5cfb594474a17da3f2e6c2%0A*+Document+last+modified%3A+2026-04-20T12%3A09%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")