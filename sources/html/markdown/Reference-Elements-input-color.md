*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#mdn-search)
    

`<input type="color">` HTML attribute value
===========================================

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`color`** provide a user interface element that lets a user specify a color, either by using a visual color picker interface or by entering the color into a text field in a [CSS color value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 format.

The element's presentation may vary substantially from one browser and/or platform to another—it might be a basic textual input that automatically validates to ensure that the color information is entered in the proper format, or a platform-standard color picker, or some kind of custom color picker window.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#try_it)

--------------------------------------------------------------------------------------------------

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#value)

------------------------------------------------------------------------------------------------

A [CSS color value](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
.

**Note:** Historically, only basic hexadecimal colors (without alpha channel) were allowed. Now, any CSS color format, including named colors, functional notations, and hexadecimal colors with an alpha channel, can be used. The default value is `#000000` (black) if a `value` is omitted or is invalid.

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#additional_attributes)

--------------------------------------------------------------------------------------------------------------------------------

In addition to the [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 and the [input attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#attributes)
 common to all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, the `color` input also supports the following attributes:

[`alpha`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#alpha)

A [boolean](https://developer.mozilla.org/en-US/docs/Glossary/Boolean/HTML)
 attribute, if present, indicates the color's alpha component can be manipulated by the end user and does not have to be fully opaque.

[`colorspace`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#colorspace)

Defines the [color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
 for the color and hints at the desired user interface for the color picker widget. Possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are:

*   `"limited-srgb"`: The color is in the [sRGB](https://developer.mozilla.org/en-US/docs/Glossary/RGB)
     color space. This includes [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
    , [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
    , [`hwb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
    , and [`<hex-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
     values. The color value is limited to 8-bits per `r`, `g`, and `b` component. This is the default.
*   `"display-p3"`: The [Display P3 color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#display-p3)
    , e.g., `color(display-p3 1.84 -0.19 0.72 / 0.6)`

[Using color inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#using_color_inputs)

--------------------------------------------------------------------------------------------------------------------------

Inputs of type `color` are simple, due to the limited number of attributes they support.

### [Providing a default color](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#providing_a_default_color)

You can update the example above to set a default value, so that the color picker is pre-filled with the default color and the color picker (if any) will also default to that color.

If you don't specify a value or if the value is invalid or otherwise not supported by the browser, the value defaults to `#000000`, which is opaque black.

### [Tracking color changes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#tracking_color_changes)

As is the case with other [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 types, there are two events that can be used to detect changes to the color value: [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input")
 and [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")
. `input` is fired on the `<input>` element every time the color changes. The `change` event is fired when the user dismisses the color picker. In both cases, you can determine the new value of the element by looking at its [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
.

Here's an example that watches changes over time to the color value:

### [Selecting the value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#selecting_the_value)

When a browser doesn't support a color picker interface, its implementation of color inputs will be a text box that validates the contents automatically to ensure that the value is in the correct format. In this case you can use the [`select()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/select "select()")
 method to select the text currently in the edit field.

If the browser instead uses a color picker, `select()` does nothing. You should be aware of this behavior so your code can respond appropriately in either case.

[Validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#validation)

----------------------------------------------------------------------------------------------------------

A color input's value is considered to be invalid if the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 is unable to convert the user's input into seven-character lower-case hexadecimal notation. If and when this is the case, the [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 pseudo-class is applied to the element.

[Example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#example)

----------------------------------------------------------------------------------------------------

Let's create an example which does a little more with the color input by tracking the [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")
 and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input")
 events to take the new color and apply it to every [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 element in the document.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#html)

The HTML is fairly straightforward — a couple of paragraphs of descriptive material with an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 of type `color` with the ID `color-picker`, which we'll use to change the color of the paragraphs' text.

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#javascript)

#### Initialization

The following code initializes the color input:

This gets a reference to the color `<input>` element in a variable called `colorPicker`, then sets the color input's value to the value in `defaultColor`. Then the color input's [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input")
 event is set up to call our `updateFirst()` function, and the [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")
 event is set to call `updateAll()`. These are both seen below.

Finally, we call [`select()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/select "select()")
 to select the text content of the color input if the control is implemented as a text field (this has no effect if a color picker interface is provided instead).

#### Reacting to color changes

We provide two functions that deal with color changes. The `updateFirst()` function is called in response to the `input` event. It changes the color of the first paragraph element in the document to match the new value of the color input. Since `input` events are fired every time an adjustment is made to the value (for example, if the brightness of the color is increased), these will happen repeatedly as the color picker is used.

When the color picker is dismissed, indicating that the value will not change again (unless the user re-opens the color picker), a `change` event is sent to the element. We handle that event using the `updateAll()` function, using [`Event.target.value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 to obtain the final selected color:

This sets the color of every [`<p>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/p)
 block so that its [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 attribute matches the current value of the color input, which is referred to using [`event.target`](https://developer.mozilla.org/en-US/docs/Web/API/Event/target "event.target")
.

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#result)

The final result looks like this:

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#technical_summary)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#value)<br>** | Any CSS [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)<br> value in any notation. |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br> and [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input") |
| **Supported common attributes** | [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)<br> and [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list) |
| **IDL attributes** | [`alpha`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/alpha)<br>, [`colorSpace`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/colorSpace)<br>, [`list`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/list)<br>, and [`value`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/value) |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | [no corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# color-state-(type=color)](https://html.spec.whatwg.org/multipage/input.html#color-state-(type=color)) |
| [HTML  <br>\# attr-input-alpha](https://html.spec.whatwg.org/multipage/input.html#attr-input-alpha) |
| [HTML  <br>\# attr-input-colorspace](https://html.spec.whatwg.org/multipage/input.html#attr-input-colorspace) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

### [html.elements.input.type\_color](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#html.elements.input.type_color)

### [html.elements.input.alpha](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#html.elements.input.alpha)

### [html.elements.input.colorspace](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#html.elements.input.colorspace)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color#see_also)

------------------------------------------------------------------------------------------------------

*   [`HTMLInputElement.alpha`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/alpha)
    
*   [`HTMLInputElement.colorspace`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/colorSpace)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jun 9, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/color/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fcolor&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fcolor%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fcolor%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fcolor%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F3944506d4afeeed774687cf3fd950878c6229bbc%0A*+Document+last+modified%3A+2026-06-09T11%3A58%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")