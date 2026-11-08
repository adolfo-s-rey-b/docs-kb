*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#mdn-search)
    

`<progress>` HTML progress indicator element
============================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<progress>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#try_it)

-----------------------------------------------------------------------------------------------

    <label for="file">File progress:</label>
    
    <progress id="file" max="100" value="70">70%</progress>
    

    label {
      padding-right: 10px;
      font-size: 1rem;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#attributes)

-------------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)

This attribute describes how much work the task indicated by the `progress` element requires. The `max` attribute, if present, must have a value greater than `0` and be a valid floating point number. The default value is `1`.

[`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#value)

This attribute specifies how much of the task that has been completed. It must be a valid floating point number between `0` and `max`, or between `0` and `1` if `max` is omitted. If there is no `value` attribute, the progress bar is indeterminate; this indicates that an activity is ongoing with no indication of how long it is expected to take.

**Note:** Unlike the [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
 element, the minimum value is always 0, and the `min` attribute is not allowed for the `<progress>` element.

**Note:** The [`:indeterminate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate)
 pseudo-class can be used to match against indeterminate progress bars. To change the progress bar to indeterminate after giving it a value you must remove the value attribute with [`element.removeAttribute('value')`](https://developer.mozilla.org/en-US/docs/Web/API/Element/removeAttribute "element.removeAttribute('value')")
.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#accessibility)

-------------------------------------------------------------------------------------------------------------

### [Labeling](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#labeling)

In most cases you should provide an accessible label when using `<progress>`. While you can use the standard ARIA labeling attributes [`aria-labelledby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-labelledby)
 or [`aria-label`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-label)
 as you would for any element with `role="progressbar"`, when using `<progress>` you can alternatively use the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element.

**Note:** Text placed between the element's tags is not an accessible label, it is only recommended as a fallback for old browsers that do not support this element.

#### Examples

html

    <label>
      Uploading Document: <progress value="70" max="100">70 %</progress>
    </label>
    
    <!-- OR -->
    <br />
    
    <label for="progress-bar">Uploading Document</label>
    <progress id="progress-bar" value="70" max="100">70 %</progress>
    

#### Result

### [Describing a particular region](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#describing_a_particular_region)

If the `<progress>` element is describing the loading progress of a section of a page, use [`aria-describedby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby)
 to point to the status, and set [`aria-busy="true"`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-busy)
 on the section that is being updated, removing the `aria-busy` attribute when it has finished loading.

#### Examples

html

    <div aria-busy="true" aria-describedby="progress-bar">
      <!-- content is for this region is loading -->
    </div>
    
    <!-- ... -->
    
    <progress id="progress-bar" aria-label="Content loading…"></progress>
    

##### Result

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#examples_3)

-----------------------------------------------------------------------------------------------------

html

    <progress value="70" max="100">70 %</progress>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#result_3)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#technical_summary)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, labelable content, [palpable content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#palpable_content)<br>. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, but there must be no `<progress>` element among its descendants. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [`progressbar`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/progressbar_role) |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLProgressElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLProgressElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-progress-element](https://html.spec.whatwg.org/multipage/form-elements.html#the-progress-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress#see_also)

---------------------------------------------------------------------------------------------------

*   [Creating vertical form controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls)
    
*   [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
    
*   [`:indeterminate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate)
    
*   [`-moz-orient`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-orient)
    
*   [`::-moz-progress-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-moz-progress-bar)
    
*   [`::-webkit-progress-bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-bar)
    
*   [`::-webkit-progress-value`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-value)
    
*   [`::-webkit-progress-inner-element`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-progress-inner-element)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/progress/index.md?plain=1 "Folder: en-us/web/html/reference/elements/progress (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fprogress&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fprogress%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fprogress%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fprogress%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F11a5944cd0a3bf015b2ee9c7ee4c55025dd878ca%0A*+Document+last+modified%3A+2026-08-28T11%3A00%3A42.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")