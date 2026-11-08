*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#mdn-search)
    

Creating vertical form controls
===============================

The guide explains how to use the CSS [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 and [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 properties to create and configure vertical form controls. This includes:

*   [`<input type="range">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
     sliders, [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
     bars, and [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
     elements.
*   [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
     elements.
*   [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
     elements and button input types such as [`<input type="button">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button)
    , [`<input type="reset">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset)
    , and [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
    .
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
     elements and text-based input types such as [`<input type="text">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
    , [`<input type="datetime-local">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local)
    , and [`<input type="url">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
    .

[General technique](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#general_technique)

-------------------------------------------------------------------------------------------------------------------------------

In modern browsers, the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 property can be set to a vertical value to vertically display form controls with text characters that are normally horizontal (for example in Latin languages), with text displayed at a 90-degree angle from the default. Normally vertical text characters, for example in Chinese or Japanese, are unaffected in this regard.

This is useful when creating vertical language forms.

Specifically:

*   `writing-mode: vertical-lr` will create vertical form controls with a left-to-right block flow direction, meaning that in controls with wrapping or multiple lines of text, subsequent lines will appear to the right of previous lines.
*   `writing-mode: vertical-rl` will create vertical form controls with a right-to-left block flow direction, meaning that in controls with wrapping or multiple lines of text, subsequent lines will appear to the left of previous lines.

You could use a [transform](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transform)
 to rotate the controls by 90 degrees, but that would place the controls in their own layer and cause unintended layout side effects such as other content being overlapped. Using `writing-mode` offers a more reliable solution.

**Note:** While the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 property is well supported, creating vertically-oriented form controls with `writing-mode` only gained full browser support in 2024.

**Note:** The experimental `sideways-lr` and `sideways-rl` values have a similar effect as `vertical-lr` and `vertical-rl` respectively, except that normally vertical text characters (for example in Chinese or Japanese) are rotated 90 degrees to display on their sides, while horizontal text characters (for example in Latin languages) are unaffected by these values.

In addition, the [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 property can be used to control the direction of the content inside the controls:

*   `direction: ltr` will cause the content to start at the top and flow towards the bottom.
*   `direction: rtl` will cause the content to start at the bottom and flow towards the top.

The `direction` property can be used to set the **inline base direction** — the primary direction in which content is ordered on a line, which defines on which sides the "start" and "end" of a line are. For text-based form controls the difference is obvious — the flow of text starts at the top or bottom. In non-text-based controls such as range sliders, `direction` sets the direction in which the control is drawn. For example, including `direction: ltr` on a vertical slider sets the lowest value at the top of the slider and the highest value at the bottom of the slider.

The sections below show how to create different types of vertical form control, along with examples of each. Consult the browser compatibility information on each of the linked reference pages to find out the exact support information for each type.

[Range sliders, meters, and progress bars](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#range_sliders_meters_and_progress_bars)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Let's have a look at creating vertical range sliders, meters, and progress bars.

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#basic_example)

A typical set of visual [`<input type="range">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 slider, [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
, and [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
 controls is created like this:

**Note:** Best practice is to include a [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element for each form control, to associate a meaningful text description with each field for accessibility purposes (see [Use meaningful text labels](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Accessibility/HTML#use_meaningful_text_labels)
 for more information). We haven't done that here, as this article focuses purely on aspects of the form controls' visual rendering, but you should make sure you do so in production code.

To display the controls vertically, we can use CSS like this:

[`writing-mode: vertical-lr`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 (and `vertical-rl`) causes the controls to be displayed vertically in modern browsers.

The result of this looks like so:

### [Drawing the control from bottom to top](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#drawing_the_control_from_bottom_to_top)

By default, the controls have a [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 value of `ltr`. This causes your sliders, meters, and progress bars to be drawn from top to bottom, as seen above.

You can change this by setting `direction: rtl` — this causes them to be drawn from bottom to top instead:

    <input type="range" min="0" max="11" value="9" step="1" />
    <meter id="fuel" min="0" max="100" low="33" high="66" optimum="80" value="20">
      at 50/100
    </meter>
    <progress id="file" max="100" value="70">70%</progress>
    

css

    input[type="range"],
    meter,
    progress {
      margin-block-end: 20px;
      writing-mode: vertical-lr;
      direction: rtl;
    }
    

The result of this looks like so:

### [Creating vertical range sliders in older browsers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#creating_vertical_range_sliders_in_older_browsers)

In older browsers that do not support the creation of vertical form controls with `writing-mode` and `direction`, there are limited alternatives available. The following only work on `<input type="range">`, causing the text to flow from bottom to top — they have no effect on `<meter>` and `<progress>` elements:

*   The non-standard [`appearance: slider-vertical`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
     property can be used in older versions of Safari and Chrome.
*   The non-standard `orient="vertical"` attribute can be added to the `<input type="range">` element itself in older versions of Firefox.

The HTML for this example includes an [`<input type="range">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range)
 slider only, with `orient="vertical"` added to make it display vertically in older Firefox versions:

html

    <input type="range" min="0" max="11" value="9" step="1" orient="vertical" />
    

To cause the controls to also display vertically in older versions of Chrome and Safari, we can use `appearance: slider-vertical`:

css

    input[type="range"] {
      margin-block-end: 20px;
      appearance: slider-vertical;
    }
    

The result looks like so:

[Select elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#select_elements)

---------------------------------------------------------------------------------------------------------------------------

This section shows how to handle vertical [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 elements.

### [Select basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#select_basic_example)

The below HTML creates two `<select>` elements, one where a single selection can be made and one with multiple selections:

html

    <select multiple>
      <option>First</option>
      <option>Second</option>
      <option>Third</option>
      <option>Fourth</option>
      <option>Fifth</option>
    </select>
    <select>
      <option>First</option>
      <option>Second</option>
      <option>Third</option>
      <option>Fourth</option>
      <option>Fifth</option>
    </select>
    

To display the controls vertically, we can use CSS like this:

css

    select {
      inline-size: 100px;
      margin-block-end: 20px;
      writing-mode: vertical-rl;
    }
    

The result of this looks like so:

### [Adjusting text direction and option order](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#adjusting_text_direction_and_option_order)

Again, it is possible to use a [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 property value of `rtl` to set the text direction to go from bottom to top, instead of the default direction of top to bottom.

It is also worth noting that in the above example, the inline direction for the select options goes from right to left because we used `writing-mode: vertical-rl`. If we use `writing-mode: vertical-lr` instead, the `<option>` text will appear from left to right.

We'll explore these two use cases using three listbox (`multiple`) `<select>` elements, to enable comparing the effects side-by-side.

html

    <div class="controls">
      <div>
        <h2>writing-mode: vertical-lr</h2>
        <select multiple>
          <option>First</option>
          <option>Second</option>
          <option>Third</option>
          <option>Fourth</option>
          <option>Fifth</option>
        </select>
      </div>
      <div class="direction">
        <h2>direction: rtl & writing-mode: vertical-lr</h2>
        <select multiple>
          <option>First</option>
          <option>Second</option>
          <option>Third</option>
          <option>Fourth</option>
          <option>Fifth</option>
        </select>
      </div>
      <div class="reverse-option-order">
        <h2>writing-mode: vertical-rl</h2>
        <select multiple>
          <option>First</option>
          <option>Second</option>
          <option>Third</option>
          <option>Fourth</option>
          <option>Fifth</option>
        </select>
      </div>
    </div>
    

In the CSS for this example, we set the following properties on the three listboxes:

1.  `writing-mode: vertical-rl`, displaying just like in the previous example — text flowing top-to-bottom, and options displaying right-to-left.
2.  `writing-mode: vertical-rl` and `direction: rtl`, with the options going from right-to-left but reversing the text flow from bottom-to-top.
3.  `writing-mode: vertical-lr`, with the text going from top-to-bottom while reversing the option order from left-to-right.

    .controls {
      box-sizing: border-box;
      display: flex;
      gap: 20px;
      font-family: sans-serif;
    }
    
    h2 {
      margin-top: 0;
      font-size: 1rem;
      text-align: center;
      flex: 1 0 100%;
    }
    
    .controls > div {
      margin-bottom: 20px;
      flex: 1;
      display: flex;
      align-items: flex-start;
      justify-content: space-around;
      flex-flow: row wrap;
    }
    

css

    select {
      inline-size: 100px;
      margin-block-end: 20px;
      writing-mode: vertical-rl;
    }
    
    .direction select {
      direction: rtl;
    }
    
    .reverse-option-order select {
      writing-mode: vertical-lr;
    }
    

The result looks like so:

[Buttons](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#buttons)

-----------------------------------------------------------------------------------------------------------

This section shows how to handle vertical [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements. Note that while we have only used a `<button>` element in the examples below, the behavior is the same for other elements that create buttons, such as [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 types of [`button`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button)
, [`reset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset)
, and [`submit`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
.

### [Basic button example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#basic_button_example)

The below HTML creates two `<button>` elements, one with a single line of text, and one with three:

html

    <button>Press me</button> <button>Press me<br />Please?<br />Thanks</button>
    

To display the buttons vertically, we can use CSS like this:

css

    button {
      inline-size: 100px;
      margin-block-end: 20px;
      writing-mode: vertical-rl;
    }
    

The result looks like so:

### [Adjusting button text line order](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#adjusting_button_text_line_order)

When you swap the `writing-mode` value of `vertical-rl` to `vertical-lr`, subsequent lines of text will appear to the right of previous lines, rather than the left.

This example uses two copies of the three-text-line button we saw in the previous example, so you can easily see the effects of changing the writing mode:

html

    <div>
      <h2>writing-mode: vertical-lr</h2>
      <button>Press me<br />Please?<br />Thanks</button>
    </div>
    <div class="reverse-line-order">
      <h2>writing-mode: vertical-rl</h2>
      <button>Press me<br />Please?<br />Thanks</button>
    </div>
    

In the CSS, we set `writing-mode: vertical-rl` on the first button to lay out the line order from right to left. On the second button, we set `writing-mode: vertical-lr` to reverse the line order — left to right:

    body {
      box-sizing: border-box;
      display: flex;
      gap: 20px;
      font-family: sans-serif;
    }
    
    h2 {
      margin-top: 0;
      font-size: 1rem;
      text-align: center;
      flex: 1 0 100%;
    }
    
    div {
      margin-bottom: 20px;
      flex: 1;
      display: flex;
      align-items: flex-start;
      justify-content: space-around;
      flex-flow: row wrap;
    }
    

css

    button {
      inline-size: 100px;
      margin-block-end: 20px;
      writing-mode: vertical-rl;
    }
    
    .reverse-line-order button {
      writing-mode: vertical-lr;
    }
    

The result looks like so:

[Text-based form controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#text-based_form_controls)

---------------------------------------------------------------------------------------------------------------------------------------------

Last but not least, we'll look at handling vertical [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
s and textual `<input>` types. Note that, while the only `<input>` type we are including is an `<input type="text">` element in the examples below, the behavior is the same for other textual [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 types: [`password`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button)
, [`number`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset)
, [`url`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
, etc.

### [Basic text input and textarea example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#basic_text_input_and_textarea_example)

The below HTML creates a `<textarea>` and an `<input type="text">`:

html

    <textarea>This is my textarea</textarea>
    <input type="text" value="Input text" />
    

To display the input and textarea vertically, we can use CSS like this:

css

    textarea,
    input[type="text"] {
      inline-size: 100px;
      margin-block-end: 20px;
      writing-mode: vertical-rl;
    }
    

The result looks like so:

### [Adjusting text direction and line layout order](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#adjusting_text_direction_and_line_layout_order)

You can use a [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
 property value of `rtl` to change the text direction from the default top-to-bottom to bottom-to-top. You can also set `writing-mode` to `vertical-lr` instead of `vertical-rl`, to cause multiple lines of text in `<textarea>`s to appear from left-to-right rather than the default right-to-left.

This example uses three copies of the same text controls we saw in the previous example, so you can easily see the effects of changing `direction` and `writing-mode` as discussed above:

html

    <div class="controls">
      <div>
        <h2>writing-mode: vertical-lr</h2>
        <textarea>This is my textarea</textarea>
        <input type="text" value="Input text" />
      </div>
      <div class="direction">
        <h2>direction: rtl & writing-mode: vertical-lr</h2>
        <textarea>This is my textarea</textarea>
        <input type="text" value="Input text" />
      </div>
      <div class="reverse-line-order">
        <h2>writing-mode: vertical-rl</h2>
        <textarea>This is my textarea</textarea>
        <input type="text" value="Input text" />
      </div>
    </div>
    

In the CSS, we set the following properties on the three sets of text controls:

1.  `writing-mode: vertical-rl` to make it display just like in the previous example — text flowing top-to-bottom, and lines flowing right-to-left.
2.  `writing-mode: vertical-rl` and `direction: rtl` to flow the lines from right-to-left but reverse the text flow from bottom-to-top.
3.  `writing-mode: vertical-lr` to flow the text top-to-bottom but reverse the flow of lines — left-to-right. Note that this has no effect on `<input type="text">` elements, as they are always single lines.

    .controls {
      box-sizing: border-box;
      display: flex;
      gap: 20px;
      font-family: sans-serif;
    }
    
    h2 {
      margin-top: 0;
      font-size: 1rem;
      text-align: center;
      flex: 1 0 100%;
    }
    
    .controls > div {
      margin-bottom: 20px;
      flex: 1;
      display: flex;
      align-items: flex-start;
      justify-content: space-around;
      flex-flow: row wrap;
    }
    

css

    textarea,
    input[type="text"] {
      inline-size: 100px;
      margin-block-end: 20px;
      writing-mode: vertical-rl;
    }
    
    .direction textarea,
    .direction input[type="text"] {
      writing-mode: vertical-rl;
      direction: rtl;
    }
    
    .reverse-line-order textarea,
    .reverse-line-order input[type="text"] {
      writing-mode: vertical-lr;
    }
    

The result looks like so:

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls#see_also)

-------------------------------------------------------------------------------------------------------------

*   The [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     element.
*   Other relevant elements: [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
    , [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
    , [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
    , and [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
    .
*   [Learn: Handling different text directions](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Handling_different_text_directions)
    
*   [Styling web forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Styling_web_forms)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/writing_modes/vertical_controls/index.md?plain=1 "Folder: en-us/web/css/guides/writing_modes/vertical_controls (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FWriting_modes%2FVertical_controls&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fwriting_modes%2Fvertical_controls%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FWriting_modes%2FVertical_controls%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fwriting_modes%2Fvertical_controls%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf3b0f3217d5d5a6957e9e17f863ece19d939d20%0A*+Document+last+modified%3A+2026-10-14T12%3A11%3A21.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")