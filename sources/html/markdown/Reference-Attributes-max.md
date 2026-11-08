*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max#mdn-search)
    

`max` HTML attribute
====================

The **`max`** attribute defines the maximum value that is acceptable and valid for the input containing the attribute. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 of the element is greater than this, the element fails [validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
. This value must be greater than or equal to the value of the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)
 attribute. If the `max` attribute is present but is not specified or is invalid, no `max` value is applied. If the `max` attribute is valid and a non-empty value is greater than the maximum allowed by the `max` attribute, constraint validation will prevent form submission.

The max attribute is valid for the numeric input types, including the [date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date)
, [month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month)
, [week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week)
, [time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time)
, [datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
, [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number)
 and [range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 types, and both the [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
 and [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
 elements. It is a number that specifies the most positive value a form control to be considered valid.

If the value exceeds the max value allowed, the [`validityState.rangeOverflow`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeOverflow)
 will be true, and the control will be matched by the [`:out-of-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range)
 and [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 pseudo-classes.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max#syntax)

--------------------------------------------------------------------------------------------

|     |     |     |
| --- | --- | --- |Syntax for `max` values by input `type`
| Input type | Syntax | Example |
| --- | --- | --- |
| [date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date) | `yyyy-mm-dd` | `<input type="date" max="2019-12-25" step="1">` |
| [month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month) | `yyyy-mm` | `<input type="month" max="2019-12" step="12">` |
| [week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week) | `yyyy-W##` | `<input type="week" max="2019-W23" step="">` |
| [time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time) | `HH:mm` | `<input type="time" max="17:00" step="900">` |
| [datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local) | `yyyy-mm-ddTHH:mm` | `<input type="datetime-local" max="2019-12-25T23:59">` |
| [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number) | [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number) | `<input type="number" min="0" step="5" max="100">` |
| [range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range) | [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number) | `<input type="range" min="60" step="5" max="100">` |

**Note:** When the data entered by the user doesn't adhere to the maximum value set, the value is considered invalid in constraint validation and will match the [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 and [`:out-of-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range)
 pseudo-classes.

See [Client-side validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 and [`rangeOverflow`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeOverflow "rangeOverflow")
 for more information.

For the [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
 element, the `max` attribute describes how much work the task indicated by the `progress` element requires. If present, must have a value greater than zero and be a valid floating point number. For the [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
 element, the `max` attribute defines the upper numeric bound of the measured range. This must be greater than the minimum value ([`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)
 attribute), if specified. In both cases, if omitted, the value defaults to 1.

|     |     |     |
| --- | --- | --- |Syntax for `max` values for other elements
| Input type | Syntax | Example |
| --- | --- | --- |
| [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress) | [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number) | `<progress id="file" max="100" value="70"> 70% </progress>` |
| [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter) | [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number) | `<meter id="fuel" min="0" max="100" low="33" high="66" optimum="80" value="40"> at 40/100</meter>` |

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max#accessibility_concerns)

----------------------------------------------------------------------------------------------------------------------------

Provide instructions to help users understand how to complete the form and use individual form controls. Indicate any required and optional input, data formats, and other relevant information. When using the `max` attribute, ensure this maximum requirement is understood by the user. Providing instructions within the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 may be sufficient. If providing instructions outside of labels, which allows more flexible positioning and design, consider using [`aria-labelledby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby)
 or [`aria-describedby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-input-max](https://html.spec.whatwg.org/multipage/input.html#attr-input-max) |
| [HTML  <br>\# attr-meter-max](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-max) |
| [HTML  <br>\# attr-progress-max](https://html.spec.whatwg.org/multipage/form-elements.html#attr-progress-max) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

### [html.elements.input.max](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max#html.elements.input.max)

### [html.elements.meter.max](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max#html.elements.meter.max)

### [html.elements.progress.max](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max#html.elements.progress.max)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max#see_also)

------------------------------------------------------------------------------------------------

*   [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step)
    
*   [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)
    
*   [Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
    
*   [Form validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
    
*   [`validityState.rangeOverflow`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeOverflow)
    
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

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/max/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/max (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fmax&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fmax%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fmax%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fmax%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb50ed7ac1c2ca21b4b5cfb594474a17da3f2e6c2%0A*+Document+last+modified%3A+2026-04-20T12%3A09%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")