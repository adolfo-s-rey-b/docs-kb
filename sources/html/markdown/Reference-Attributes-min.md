*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min#mdn-search)
    

`min` HTML attribute
====================

The **`min`** attribute defines the minimum value that is acceptable and valid for the input containing the attribute. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 of the element is less than this, the element fails [validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
. This value must be less than or equal to the value of the `max` attribute.

Some input types have a default minimum. If the input has no default minimum and a value is specified for `min` that can't be converted to a valid number (or no minimum value is set), the input has no minimum value.

It is valid for the input types including: [date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date)
, [month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month)
, [week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week)
, [time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time)
, [datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
, [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number)
 and [range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 types, and the [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
 element.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min#syntax)

--------------------------------------------------------------------------------------------

|     |     |     |
| --- | --- | --- |Syntax for `min` values by input `type`
| Input type | Syntax | Example |
| --- | --- | --- |
| [date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date) | `yyyy-mm-dd` | `<input type="date" min="2019-12-25" step="1">` |
| [month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month) | `yyyy-mm` | `<input type="month" min="2019-12" step="12">` |
| [week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week) | `yyyy-W##` | `<input type="week" min="2019-W23" step="">` |
| [time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time) | `HH:mm` | `<input type="time" min="09:00" step="900">` |
| [datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local) | `yyyy-mm-ddTHH:mm` | `<input type="datetime-local" min="2019-12-25T19:30">` |
| [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number) | [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number) | `<input type="number" min="0" step="5" max="100">` |
| [range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range) | [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number) | `<input type="range" min="60" step="5" max="100">` |

**Note:** When the data entered by the user doesn't adhere to the min value set, the value is considered invalid in constraint validation and will match the [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 and [`:out-of-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range)
 pseudo-classes.

See [Client-side validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 and [`rangeUnderflow`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeUnderflow "rangeUnderflow")
 for more information.

For the [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
 element, the `min` attribute defines the lower numeric bound of the measured range. This must be less than the maximum value ([`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)
 attribute), if specified. In both cases, if omitted, the value defaults to 1.

|     |     |     |
| --- | --- | --- |Syntax for `min` values for other elements
| Input type | Syntax | Example |
| --- | --- | --- |
| [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter) | [<number>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/number) | `<meter id="fuel" min="0" max="100" low="33" high="66" optimum="80" value="40"> at 40/100</meter>` |

### [Impact on step](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min#impact_on_step)

The value of `min` and `step` define what are valid values, even if the `step` attribute is not included, as `step` defaults to `0`.

We add a big red border around invalid inputs:

Then define an input with a minimum value of 7.2, omitting the step attribute, wherein it defaults to 1.

Because `step` defaults to 1, valid values include `7.2`, `8.2`, `9.2`, and so on. The value 8 is not valid. As we included an invalid value, supporting browsers will show the value as invalid.

If not explicitly included, `step` defaults to 1 for `number` and `range`, and 1 unit type (second, week, month, day) for the date/time input types.

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min#accessibility_concerns)

----------------------------------------------------------------------------------------------------------------------------

Provide instructions to help users understand how to complete the form and use individual form controls. Indicate any required and optional input, data formats, and other relevant information. When using the `min` attribute, ensure this minimum requirement is understood by the user. Providing instructions within the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 may be sufficient. If providing instructions outside of labels, which allows more flexible positioning and design, consider using [`aria-labelledby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby)
 or [`aria-describedby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby)
.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-input-min](https://html.spec.whatwg.org/multipage/input.html#attr-input-min) |
| [HTML  <br>\# attr-meter-max](https://html.spec.whatwg.org/multipage/form-elements.html#attr-meter-max) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

### [html.elements.input.min](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min#html.elements.input.min)

### [html.elements.meter.min](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min#html.elements.meter.min)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min#see_also)

------------------------------------------------------------------------------------------------

*   [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step)
    
*   [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)
    
*   other meter attributes: [`low`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#low)
    , [`high`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#high)
    , [`optimum`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#optimum)
    
*   [Constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
    
*   [Form validation](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation)
    
*   [`validityState.rangeUnderflow`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeUnderflow)
    
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

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/min/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/min (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fmin&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fmin%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fmin%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fmin%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb50ed7ac1c2ca21b4b5cfb594474a17da3f2e6c2%0A*+Document+last+modified%3A+2026-04-20T12%3A09%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")