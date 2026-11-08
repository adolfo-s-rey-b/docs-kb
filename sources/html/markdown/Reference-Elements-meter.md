*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#mdn-search)
    

`<meter>` HTML meter element
============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since March 2017.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<meter>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents either a scalar value within a known range or a fractional value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#try_it)

--------------------------------------------------------------------------------------------

    <label for="fuel">Fuel level:</label>
    
    <meter id="fuel" min="0" max="100" low="33" high="66" optimum="80" value="50">
      at 50/100
    </meter>
    

    label {
      padding-right: 10px;
      font-size: 1rem;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#attributes)

----------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#value)

The current numeric value. This must be between the minimum and maximum values (`min` attribute and `max` attribute) if they are specified. If unspecified or malformed, the value is `0`. If specified, but not within the range given by the `min` attribute and `max` attribute, the value is equal to the nearest end of the range.

**Note:** Unless the `value` attribute is between `0` and `1` (inclusive), the `min` and `max` attributes should define the range so that the `value` attribute's value is within it.

[`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)

The lower numeric bound of the measured range. This must be less than the maximum value (`max` attribute), if specified. If unspecified, the minimum value is `0`.

[`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)

The upper numeric bound of the measured range. This must be greater than the minimum value (`min` attribute), if specified. If unspecified, the maximum value is `1`.

[`low`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#low)

The upper numeric bound of the low end of the measured range. This must be greater than the minimum value (`min` attribute), and it also must be less than the high value and maximum value (`high` attribute and `max` attribute, respectively), if any are specified. If unspecified, or if less than the minimum value, the `low` value is equal to the minimum value.

[`high`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#high)

The lower numeric bound of the high end of the measured range. This must be less than the maximum value (`max` attribute), and it also must be greater than the low value and minimum value (`low` attribute and `min` attribute, respectively), if any are specified. If unspecified, or if greater than the maximum value, the `high` value is equal to the maximum value.

[`optimum`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#optimum)

This attribute indicates the optimal numeric value. It must be within the range (as defined by the `min` attribute and `max` attribute). When used with the `low` attribute and `high` attribute, it gives an indication where along the range is considered preferable. For example, if it is between the `min` attribute and the `low` attribute, then the lower range is considered preferred. The browser may color the meter's bar differently depending on whether the value is less than or equal to the optimum value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#examples)

------------------------------------------------------------------------------------------------

### [Basic Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#basic_example)

#### HTML

html

    <p>Battery level: <meter min="0" max="100" value="75">75%</meter></p>
    

#### Result

### [High and low range example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#high_and_low_range_example)

Note that in this example the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#min)
 attribute is omitted. This is allowed, as it will default to `0`.

#### HTML

html

    <p>
      Student's exam score:
      <meter low="50" high="80" max="100" value="84">84%</meter>
    </p>
    

#### Result

[Technical Summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, labelable content, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, but there must be no `<meter>` element among its descendants. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | `[meter](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/structural_roles#structural_roles_with_html_equivalents) ` |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLMeterElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMeterElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-meter-element](https://html.spec.whatwg.org/multipage/form-elements.html#the-meter-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter#see_also)

------------------------------------------------------------------------------------------------

*   [Creating vertical form controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls)
    
*   [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
    
*   [`::-webkit-meter-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-bar)
    , [`::-webkit-meter-inner-element`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-inner-element)
    , [`::-webkit-meter-even-less-good-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-even-less-good-value)
    , [`::-webkit-meter-optimum-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-optimum-value)
    , [`::-webkit-meter-suboptimum-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-meter-suboptimum-value)
    : non-standard pseudo-elements

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/meter/index.md?plain=1 "Folder: en-us/web/html/reference/elements/meter (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeter&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeter%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeter%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeter%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")