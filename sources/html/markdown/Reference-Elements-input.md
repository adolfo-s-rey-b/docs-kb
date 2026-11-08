*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#mdn-search)
    

`<input>` HTML input element
============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<input>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is used to create interactive controls for web-based forms in order to accept data from the user; a wide variety of types of input data and control widgets are available, depending on the device and [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
. The `<input>` element is one of the most powerful and complex in all of HTML due to the sheer number of combinations of input types and attributes.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#try_it)

--------------------------------------------------------------------------------------------

    <label for="name">Name (4 to 8 characters):</label>
    
    <input
      type="text"
      id="name"
      name="name"
      required
      minlength="4"
      maxlength="8"
      size="10" />
    

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
    

[<input> types](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#input_types)

--------------------------------------------------------------------------------------------------------

How an `<input>` works varies considerably depending on the value of its [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 attribute, hence the different types are covered in their own separate reference pages. If this attribute is not specified, the default type adopted is `text`.

The available types are as follows:

  
| Type | Description | Basic Examples |
| --- | --- | --- |
| [button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/button) | A push button with no default behavior displaying the value of the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)<br> attribute, empty by default. | <input type="button" name="button" value="Button" /> |
| [checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox) | A checkbox allowing single values to be selected/deselected. | <input type="checkbox" name="checkbox"/> |
| [color](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color) | A control for specifying a color; opening a color picker when active in supporting browsers. | <input type="color" name="color"/> |
| [date](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date) | A control for entering a date (year, month, and day, with no time). Opens a date picker or numeric wheels for year, month, day when active in supporting browsers. | <input type="date" name="date"/> |
| [datetime-local](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local) | A control for entering a date and time, with no time zone. Opens a date picker or numeric wheels for date- and time-components when active in supporting browsers. | <input type="datetime-local" name="datetime-local"/> |
| [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email) | A field for editing an email address. Looks like a `text` input, but has validation parameters and relevant keyboard in supporting browsers and devices with dynamic keyboards. | <input type="email" name="email"/> |
| [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file) | A control that lets the user select a file. Use the [`accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#accept)<br> attribute to define the types of files that the control can select. | <input type="file" accept="image/*, text/*" name="file"/> |
| [hidden](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/hidden) | A control that is not displayed but whose value is submitted to the server. There is an example in the next column, but it's hidden! | <input id="userId" name="userId" type="hidden" value="abc123" /> |
| [image](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image) | A graphical `submit` button. Displays an image defined by the `src` attribute. The [`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#alt)<br> attribute displays if the image [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#src)<br> is missing. | <input type="image" name="image" src="" alt="image input"/> |
| [month](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month) | A control for entering a month and year, with no time zone. | <input type="month" name="month"/> |
| [number](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/number) | A control for entering a number. Displays a spinner and adds default validation. Displays a numeric keypad in some devices with dynamic keypads. | <input type="number" name="number"/> |
| [password](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/password) | A single-line text field whose value is obscured. Will alert user if site is not secure. | <input type="password" name="password"/> |
| [radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio) | A radio button, allowing a single value to be selected out of multiple choices with the same [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#name)<br> value. | <input type="radio" name="radio"/> |
| [range](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/range) | A control for entering a number whose exact value is not important. Displays as a range widget defaulting to the middle value. Used in conjunction [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)<br> and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)<br> to define the range of acceptable values. | <input type="range" name="range" min="0" max="25"/> |
| [reset](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/reset) | A button that resets the contents of the form to default values. Not recommended. | <input type="reset" name="reset"/> |
| [search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/search) | A single-line text field for entering search strings. Line-breaks are automatically removed from the input value. May include a delete icon in supporting browsers that can be used to clear the field. Displays a search icon instead of enter key on some devices with dynamic keypads. | <input type="search" name="search"/> |
| [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit) | A button that submits the form. | <input type="submit" name="submit"/> |
| [tel](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/tel) | A control for entering a telephone number. Displays a telephone keypad in some devices with dynamic keypads. | <input type="tel" name="tel"/> |
| [text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text) | The default value. A single-line text field. Line-breaks are automatically removed from the input value. | <input type="text" name="text"/> |
| [time](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time) | A control for entering a time value with no time zone. | <input type="time" name="time"/> |
| [url](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url) | A field for entering a URL. Looks like a `text` input, but has validation parameters and relevant keyboard in supporting browsers and devices with dynamic keyboards. | <input type="url" name="url"/> |
| [week](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week) | A control for entering a date consisting of a week-year number and a week number with no time zone. | <input type="week" name="week"/> |
| Obsolete values |     |     |
| `datetime` | A control for entering a date and time (hour, minute, second, and fraction of a second) based on UTC time zone. | <input type="datetime" name="datetime"/> |

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#attributes)

----------------------------------------------------------------------------------------------------

The `<input>` element is so powerful because of its attributes; the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 attribute, described with examples above, being the most important. Since every `<input>` element, regardless of type, is based on the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 interface, they technically share the exact same set of attributes. However, in reality, most attributes have an effect on only a specific subset of input types. In addition, the way some attributes impact an input depends on the input type, impacting different input types in different ways.

This section provides a table listing all the attributes with a brief description. This table is followed by a list describing each attribute in greater detail, along with which input types they are associated with. Those that are common to most or all input types are defined in greater detail below. Attributes that are unique to particular input types—or attributes which are common to all input types but have special behaviors when used on a given input type—are instead documented on those types' pages.

Attributes for the `<input>` element include the [global HTML attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 and additionally:

| Attribute | Type(s) | Description |
| --- | --- | --- |
| [`accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#accept) | `file` | Hint for expected file type in file upload controls |
| [`alpha`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#alpha) | `color` | Opacity of the color |
| [`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#alt) | `image` | alt attribute for the image type. Required for accessibility |
| [`autocapitalize`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocapitalize) | all except `url`, `email`, and `password` | Controls automatic capitalization in inputted text. |
| [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete) | all except `checkbox`, `radio`, and buttons | Hint for form autofill feature |
| [`capture`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#capture) | `file` | Media capture input method in file upload controls |
| [`checked`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#checked) | `checkbox`, `radio` | Whether the command or control is checked |
| [`colorspace`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#colorspace) | `color` | The [color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)<br> that should be used for selecting the color value |
| [`dirname`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#dirname) | `hidden`, `text`, `search`, `url`, `tel`, `email` | Name of form field to use for sending the element's directionality in form submission |
| [`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#disabled) | all | Whether the form control is disabled |
| [`form`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#form) | all | Associates the control with a form element |
| [`formaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formaction) | `image`, `submit` | URL to use for form submission |
| [`formenctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formenctype) | `image`, `submit` | Form data set encoding type to use for form submission |
| [`formmethod`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formmethod) | `image`, `submit` | HTTP method to use for form submission |
| [`formnovalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formnovalidate) | `image`, `submit` | Bypass form control validation for form submission |
| [`formtarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formtarget) | `image`, `submit` | Browsing context for form submission |
| [`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#height) | `image` | Same as height attribute for [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)<br>; vertical dimension |
| [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list) | all except `hidden`, `password`, `checkbox`, `radio`, and buttons | Value of the id attribute of the [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)<br> of autocomplete options |
| [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max) | `date`, `month`, `week`, `time`, `datetime-local`, `number`, `range` | Maximum value |
| [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength) | `text`, `search`, `url`, `tel`, `email`, `password` | Maximum length (number of characters) of `value` |
| [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min) | `date`, `month`, `week`, `time`, `datetime-local`, `number`, `range` | Minimum value |
| [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength) | `text`, `search`, `url`, `tel`, `email`, `password` | Minimum length (number of characters) of `value` |
| [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#multiple) | `email`, `file` | Boolean. Whether to allow multiple values |
| [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#name) | all | Name of the form control. Submitted with the form as part of a name/value pair |
| [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern) | `text`, `search`, `url`, `tel`, `email`, `password` | Pattern the `value` must match to be valid |
| [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder) | `text`, `search`, `url`, `tel`, `email`, `password`, `number` | Text that appears in the form control when it has no value set |
| [`popovertarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#popovertarget) | `button` | Designates an `<input type="button">` as a control for a popover element |
| [`popovertargetaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#popovertargetaction) | `button` | Specifies the action that a popover control should perform |
| [`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#readonly) | all except `hidden`, `range`, `color`, `checkbox`, `radio`, and buttons | Boolean. The value is not editable |
| [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required) | all except `hidden`, `range`, `color`, and buttons | Boolean. A value is required or must be checked for the form to be submittable |
| [`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size) | `text`, `search`, `url`, `tel`, `email`, `password` | Size of the control |
| [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#src) | `image` | Same as `src` attribute for [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)<br>; address of image resource |
| [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step) | `date`, `month`, `week`, `time`, `datetime-local`, `number`, `range` | Incremental values that are valid |
| [`switch`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#switch) | `checkbox` | Whether the checkbox input should be rendered as a switch |
| [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type) | all | Type of form control |
| [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value) | all except `image` | The value of the control. When specified in the HTML, corresponds to the initial value |
| [`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#width) | `image` | Same as `width` attribute for [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img) |

A few additional non-standard attributes are listed following the descriptions of the standard attributes.

### [Individual attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#individual_attributes)

[`accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept)

Valid for the `file` input type only, the `accept` attribute defines which file types are selectable in a `file` upload control. See the [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
 input type.

[`alpha`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#alpha)

Valid for the `color` input type only, the `alpha` attribute provides the end user with the ability to set the opacity of the color being selected.

[`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#alt)

Valid for the `image` button only, the `alt` attribute provides alternative text for the image, displaying the value of the attribute if the image [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#src)
 is missing or otherwise fails to load. See the [image](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 input type.

[`autocapitalize`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocapitalize)

Controls whether inputted text is automatically capitalized and, if so, in what manner. See the [`autocapitalize`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/autocapitalize)
 global attribute page for more information.

[`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete)

(**Not** a Boolean attribute!) The [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete)
 attribute takes as its value a space-separated string that describes what, if any, type of autocomplete functionality the input should provide. A typical implementation of autocomplete recalls previous values entered in the same input field, but more complex forms of autocomplete can exist. For instance, a browser could integrate with a device's contacts list to autocomplete `email` addresses in an email input field. See [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete#value)
 for permitted values.

The `autocomplete` attribute is valid on `hidden`, `text`, `search`, `url`, `tel`, `email`, `date`, `month`, `week`, `time`, `datetime-local`, `number`, `range`, `color`, and `password`. This attribute has no effect on input types that do not return numeric or text data, being valid for all input types except `checkbox`, `radio`, `file`, or any of the button types.

See the [`autocomplete` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete)
 for additional information, including information on password security and how `autocomplete` is slightly different for `hidden` than for other input types.

[`autofocus`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autofocus)

A Boolean attribute which, if present, indicates that the input should automatically have focus when the page has finished loading (or when the [`<dialog>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dialog)
 containing the element has been displayed).

**Note:** An element with the `autofocus` attribute may gain focus before the [`DOMContentLoaded`](https://developer.mozilla.org/en-US/docs/Web/API/Document/DOMContentLoaded_event "DOMContentLoaded")
 event is fired.

No more than one element in the document may have the `autofocus` attribute. If put on more than one element, the first one with the attribute receives focus.

The `autofocus` attribute cannot be used on inputs of type `hidden`, since hidden inputs cannot be focused.

**Warning:** Automatically focusing a form control can confuse visually-impaired people using screen-reading technology and people with cognitive impairments. When `autofocus` is assigned, screen-readers "teleport" their user to the form control without warning them beforehand.

Use careful consideration for accessibility when applying the `autofocus` attribute. Automatically focusing on a control can cause the page to scroll on load. The focus can also cause dynamic keyboards to display on some touch devices. While a screen reader will announce the label of the form control receiving focus, the screen reader will not announce anything before the label, and the sighted user on a small device will equally miss the context created by the preceding content.

[`capture`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture)

Introduced in the HTML Media Capture specification and valid for the `file` input type only, the `capture` attribute defines which media—microphone, video, or camera—should be used to capture a new file for upload with `file` upload control in supporting scenarios. See the [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
 input type.

[`checked`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#checked)

Valid for both `radio` and `checkbox` types, `checked` is a Boolean attribute. If present on a `radio` type, it indicates that the radio button is the currently selected one in the group of same-named radio buttons. If present on a `checkbox` type, it indicates that the checkbox is checked by default (when the page loads). It does _not_ indicate whether this checkbox is currently checked: if the checkbox's state is changed, this content attribute does not reflect the change. (Only the [`HTMLInputElement`'s `checked` IDL attribute](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 is updated.)

**Note:** Unlike other input controls, a checkboxes and radio buttons value are only included in the submitted data if they are currently `checked`. If they are, the name and the value(s) of the checked controls are submitted.

For example, if a checkbox whose `name` is `fruit` has a `value` of `cherry`, and the checkbox is checked, the form data submitted will include `fruit=cherry`. If the checkbox isn't active, it isn't listed in the form data at all. The default `value` for checkboxes and radio buttons is `on`.

[`colorspace`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#colorspace)

Valid for the `color` input type only, the `colorspace` attribute specifies the [color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space)
 that is used by the `type="color"` input. Possible [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values are:

*   `"limited-srgb"`: The color is in the [sRGB](https://developer.mozilla.org/en-US/docs/Glossary/RGB)
     color space. This includes [`rgb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/rgb)
    , [`hsl()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hsl)
    , [`hwb()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value/hwb)
    , and [`<hex-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/hex-color)
     values. The color value is limited to 8-bits per `r`, `g`, and `b` component. This is the default.
*   `"display-p3"`: The [Display P3 color space](https://developer.mozilla.org/en-US/docs/Glossary/Color_space#display-p3)
    , e.g., `color(display-p3 1.84 -0.19 0.72 / 0.6)`

[`dirname`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname)

Valid for `hidden`, `text`, `search`, `url`, `tel`, and `email` input types, the `dirname` attribute enables the submission of the directionality of the element. When included, the form control will submit with two name/value pairs: the first being the [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#name)
 and [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
, and the second being the value of the `dirname` attribute as the name, with a value of `ltr` or `rtl` as set by the browser.

html

    <form action="page.html" method="post">
      <label>
        Fruit:
        <input type="text" name="fruit" dirname="fruit-dir" value="cherry" />
      </label>
      <input type="submit" />
    </form>
    <!-- page.html?fruit=cherry&fruit-dir=ltr -->
    

When the form above is submitted, the input cause both the `name` / `value` pair of `fruit=cherry` and the `dirname` / direction pair of `fruit-dir=ltr` to be sent. For more information, see the [`dirname` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/dirname)
.

[`disabled`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/disabled)

A Boolean attribute which, if present, indicates that the user should not be able to interact with the input. Disabled inputs are typically rendered with a dimmer color or using some other form of indication that the field is not available for use.

Specifically, disabled inputs do not receive the [`click`](https://developer.mozilla.org/en-US/docs/Web/API/Element/click_event "click")
 event, and disabled inputs are not submitted with the form.

**Note:** Although not required by the specification, Firefox will by default [persist the dynamic disabled state](https://stackoverflow.com/questions/5985839/bug-with-firefox-disabled-attribute-of-input-not-resetting-when-refreshing "External link (opens in new tab)")
 of an `<input>` across page loads. Use the [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#autocomplete)
 attribute to control this feature.

[`form`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/form)

A string specifying the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element with which the input is associated (that is, its **form owner**). This string's value, if present, must match the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#id)
 of a `<form>` element in the same document. If this attribute isn't specified, the `<input>` element is associated with the nearest containing form, if any.

The `form` attribute lets you place an input anywhere in the document but have it included with a form elsewhere in the document.

**Note:** An input can only be associated with one form.

[`formaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formaction)

Valid for the `image` and `submit` input types only. See the [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 input type for more information.

[`formenctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formenctype)

Valid for the `image` and `submit` input types only. See the [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 input type for more information.

[`formmethod`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formmethod)

Valid for the `image` and `submit` input types only. See the [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 input type for more information.

[`formnovalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formnovalidate)

Valid for the `image` and `submit` input types only. See the [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 input type for more information.

[`formtarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formtarget)

Valid for the `image` and `submit` input types only. See the [submit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 input type for more information.

[`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#height)

Valid for the `image` input button only, the `height` is the height of the image file to display to represent the graphical submit button. See the [image](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 input type.

[`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#id)

[Global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 valid for all elements, including all the input types, it defines a unique identifier (ID) which must be unique in the whole document. Its purpose is to identify the element when linking. The value is used as the value of the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
's [`for`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/for)
 attribute to link the label with the form control. See [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
.

[`inputmode`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#inputmode)

Global value valid for all elements, it provides a hint to browsers as to the type of virtual keyboard configuration to use when editing this element or its contents. Values include `none`, `text`, `tel`, `url`, `email`, `numeric`, `decimal`, and `search`.

[`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)

The value given to the `list` attribute should be the [`id`](https://developer.mozilla.org/en-US/docs/Web/API/Element/id "id")
 of a [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element located in the same document. The `<datalist>` provides a list of predefined values to suggest to the user for this input. Any values in the list that are not compatible with the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 are not included in the suggested options. The values provided are suggestions, not requirements: users can select from this predefined list or provide a different value.

It is valid on `text`, `search`, `url`, `tel`, `email`, `date`, `month`, `week`, `time`, `datetime-local`, `number`, `range`, and `color`.

Per the specifications, the `list` attribute is not supported by the `hidden`, `password`, `checkbox`, `radio`, `file`, or any of the button types.

Depending on the browser, the user may see a custom color palette suggested, tic marks along a range, or even an input that opens like a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)
 but allows for non-listed values. Check out the [browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist#browser_compatibility)
 for the other input types.

See the [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
 element.

[`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)

Valid for `date`, `month`, `week`, `time`, `datetime-local`, `number`, and `range`, it defines the greatest value in the range of permitted values. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 entered into the element exceeds this, the element fails [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If the value of the `max` attribute isn't a number, then the element has no maximum value.

There is a special case: if the data type is periodic (such as for dates or times), the value of `max` may be lower than the value of `min`, which indicates that the range may wrap around; for example, this allows you to specify a time range from 10 PM to 4 AM.

[`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/maxlength)

Valid for `text`, `search`, `url`, `tel`, `email`, and `password`, it defines the maximum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the field. This must be an integer value of 0 or higher. If no `maxlength` is specified, or an invalid value is specified, the field has no maximum length. This value must also be greater than or equal to the value of `minlength`.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text entered into the field is greater than `maxlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long. By default, browsers prevent users from entering more characters than allowed by the `maxlength` attribute. Constraint validation is only applied when the value is changed by the user. See [Client-side validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#client-side_validation)
 for more information.

[`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)

Valid for `date`, `month`, `week`, `time`, `datetime-local`, `number`, and `range`, it defines the most negative value in the range of permitted values. If the [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 entered into the element is less than this, the element fails [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. If the value of the `min` attribute isn't a number, then the element has no minimum value.

This value must be less than or equal to the value of the `max` attribute. If the `min` attribute is present but is not specified or is invalid, no `min` value is applied. If the `min` attribute is valid and a non-empty value is less than the minimum allowed by the `min` attribute, constraint validation will prevent form submission. See [Client-side validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#client-side_validation)
 for more information.

There is a special case: if the data type is periodic (such as for dates or times), the value of `max` may be lower than the value of `min`, which indicates that the range may wrap around; for example, this allows you to specify a time range from 10 PM to 4 AM.

[`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/minlength)

Valid for `text`, `search`, `url`, `tel`, `email`, and `password`, it defines the minimum string length (measured in [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
) that the user can enter into the entry field. This must be a non-negative integer value smaller than or equal to the value specified by `maxlength`. If no `minlength` is specified, or an invalid value is specified, the input has no minimum length.

The input will fail [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
 if the length of the text entered into the field is fewer than `minlength` [UTF-16 code units](https://developer.mozilla.org/en-US/docs/Glossary/UTF-16)
 long, preventing form submission. Constraint validation is only applied when the value is changed by the user. See [Client-side validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#client-side_validation)
 for more information.

[`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)

The Boolean `multiple` attribute, if set, means the user can enter comma separated email addresses in the email widget or can choose more than one file with the `file` input. See the [email](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/email)
 and [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
 input type.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#name)

A string specifying a name for the input control. This name is submitted along with the control's value when the form data is submitted.

Consider the `name` a required attribute (even though it's not). If an input has no `name` specified, or `name` is empty, the input's value is not submitted with the form! (Disabled controls, unchecked radio buttons, unchecked checkboxes, and reset buttons are also not sent.)

There are two special cases:

1.  `_charset_` : If used as the name of an `<input>` element of type [hidden](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/hidden)
    , the input's `value` is automatically set by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
     to the character encoding being used to submit the form.
2.  `isindex`: For historical reasons, the name [`isindex`](https://html.spec.whatwg.org/multipage/form-control-infrastructure.html#attr-fe-name "External link (opens in new tab)")
     is not allowed.

The [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#name)
 attribute creates a unique behavior for radio buttons.

Only one radio button in a same-named group of radio buttons can be checked at a time. Selecting any radio button in that group automatically deselects any currently-selected radio button in the same group. The value of that one checked radio button is sent along with the name if the form is submitted,

When tabbing into a series of same-named group of radio buttons, if one is checked, that one will receive focus. If they aren't grouped together in source order, if one of the group is checked, tabbing into the group starts when the first one in the group is encountered, skipping all those that aren't checked. In other words, if one is checked, tabbing skips the unchecked radio buttons in the group. If none are checked, the radio button group receives focus when the first button in the same name group is reached.

Once one of the radio buttons in a group has focus, using the arrow keys will navigate through all the radio buttons of the same name, even if the radio buttons are not grouped together in the source order.

When an input element is given a `name`, that name becomes a property of the owning form element's [`HTMLFormElement.elements`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLFormElement/elements)
 property. If you have an input whose `name` is set to `guest` and another whose `name` is `hat-size`, the following code can be used:

js

    let form = document.querySelector("form");
    
    let guestName = form.elements.guest;
    let hatSize = form.elements["hat-size"];
    

When this code has run, `guestName` will be the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 for the `guest` field, and `hatSize` the object for the `hat-size` field.

**Warning:** Avoid giving form elements a `name` that corresponds to a built-in property of the form, since you would then override the predefined property or method with this reference to the corresponding input.

[`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/pattern)

Valid for `text`, `search`, `url`, `tel`, `email`, and `password`, the `pattern` attribute is used to compile a regular expression that the input's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 must match in order for the value to pass [constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
. It must be a valid JavaScript regular expression, as used by the [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 type, and as documented in our [guide on regular expressions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
. No forward slashes should be specified around the pattern text. When compiling the regular expression:

1.  the pattern will be implicitly wrapped with `^(?:` and `)$`, such that the match is required against the _entire_ input value, i.e., `^(?:<pattern>)$`.
2.  the `'v'` flag is specified so that the pattern is treated as a sequence of Unicode code points, instead of as [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
    .

If the `pattern` attribute is present but is not specified or is invalid, no regular expression is applied and this attribute is ignored completely. If the pattern attribute is valid and a non-empty value does not match the pattern, constraint validation will prevent form submission. If the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)
 is present, the compiled regular expression is matched against each comma separated value.

**Note:** If using the `pattern` attribute, inform the user about the expected format by including explanatory text nearby. You can also include a [`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#title)
 attribute to explain what the requirements are to match the pattern; most browsers will display this title as a tooltip. The visible explanation is required for accessibility. The tooltip is an enhancement.

See [Client-side validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#client-side_validation)
 for more information.

[`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/placeholder)

Valid for `text`, `search`, `url`, `tel`, `email`, `password`, and `number`, the `placeholder` attribute provides a brief hint to the user as to what kind of information is expected in the field. It should be a word or short phrase that provides a hint as to the expected type of data, rather than an explanation or prompt. The text _must not_ include carriage returns or line feeds. So for example if a field is expected to capture a user's first name, and its label is "First Name", a suitable placeholder might be "e.g., Mustafa".

**Note:** The `placeholder` attribute is not as semantically useful as other ways to explain your form, and can cause unexpected technical issues with your content. See [Labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels)
 for more information.

[`popovertarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#popovertarget)

Turns an `<input type="button">` element into a popover control button; takes the ID of the popover element to control as its value. See the [Popover API](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API "Popover API")
 landing page for more details. Establishing a relationship between a popover and its invoker button using the `popovertarget` attribute has two additional useful effects:

*   The browser creates an implicit [`aria-details`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-details)
     and [`aria-expanded`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-expanded)
     relationship between popover and invoker, and places the popover in a logical position in the keyboard focus navigation order when shown. This makes the popover more accessible to keyboard and assistive technology (AT) users (see also [Popover accessibility features](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#popover_accessibility_features)
    ).
*   The browser creates an implicit anchor reference between the two, making it very convenient to position popovers relative to their controls using [CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning)
    . See [Popover anchor positioning](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using#popover_anchor_positioning)
     for more details.

[`popovertargetaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#popovertargetaction)

Specifies the action to be performed on a popover element being controlled by a control `<input type="button">`. Possible values are:

[`"hide"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#hide)

The button will hide a shown popover. If you try to hide an already hidden popover, no action will be taken.

[`"show"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#show)

The button will show a hidden popover. If you try to show an already showing popover, no action will be taken.

[`"toggle"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#toggle)

The button will toggle a popover between showing and hidden. If the popover is hidden, it will be shown; if the popover is showing, it will be hidden. If `popovertargetaction` is omitted, `"toggle"` is the default action that will be performed by the control button.

[`readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly)

A Boolean attribute which, if present, indicates that the user should not be able to edit the value of the input. The `readonly` attribute is supported by the `text`, `search`, `url`, `tel`, `email`, `date`, `month`, `week`, `time`, `datetime-local`, `number`, and `password` input types.

See the [HTML attribute: `readonly`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/readonly)
 for more information.

[`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)

`required` is a Boolean attribute which, if present, indicates that the user must specify a value for the input before the owning form can be submitted. The `required` attribute is supported by `text`, `search`, `url`, `tel`, `email`, `date`, `month`, `week`, `time`, `datetime-local`, `number`, `password`, `checkbox`, `radio`, and `file` inputs.

See [Client-side validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#client-side_validation)
 and the [HTML attribute: `required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/required)
 for more information.

[`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/size)

Valid for `email`, `password`, `tel`, `url`, and `text`, the `size` attribute specifies how much of the input is shown. Basically creates same result as setting CSS [`width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/width)
 property with a few specialties. The actual unit of the value depends on the input type. For `password` and `text`, it is a number of characters (or `em` units) with a default value of `20`, and for others, it is pixels (or `px` units). CSS `width` takes precedence over the `size` attribute.

[`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#src)

Valid for the `image` input button only, the `src` is string specifying the URL of the image file to display to represent the graphical submit button. See the [image](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 input type.

[`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step)

Valid for `date`, `month`, `week`, `time`, `datetime-local`, `number`, and `range`, the [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/step)
 attribute is a number that specifies the granularity that the value must adhere to. Only values which are a whole number of steps from the step base are valid. The step base is [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)
 if specified, [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 otherwise, or `0` if neither is provided (except for `week`, which has a default step base of −259,200,000, representing the start of week `1970-W01`).

If not explicitly included:

*   `step` defaults to 1 for `number` and `range`.
*   Each date/time input type has a default `step` value appropriate for the type; see the individual input pages: [`date`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/date#step)
    , [`datetime-local`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/datetime-local#step)
    , [`month`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/month#step)
    , [`time`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/time#step)
    , and [`week`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/week#step)
    .

The value must be a positive number—integer or float—or the special value `any`, which means no stepping is implied, and any value is allowed (barring other constraints, such as [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/min)
 and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/max)
).

For example, if you have `<input type="number" min="10" step="2">`, then any even integer, `10` or greater, is valid. If omitted, `<input type="number">`, any integer is valid, but floats (like `4.2`) are not valid, because `step` defaults to `1`. For `4.2` to be valid, `step` would have had to be set to `any`, 0.1, 0.2, or the `min` value would have had to be a number ending in `.2`, such as `<input type="number" min="-5.2">`.

**Note:** When the data entered by the user doesn't adhere to the stepping configuration, the value is considered invalid in constraint validation and will match the `:invalid` pseudoclass.

See [Client-side validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#client-side_validation)
 for more information.

[`switch`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox#switch)

Valid for `checkbox` input only, `switch` is a Boolean attribute that indicates whether the checkbox input should be rendered as a switch.

**Note:** This attribute is still experimental and has limited browser support. The attribute is ignored on unsupported browsers.

[`tabindex`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#tabindex)

Global attribute valid for all elements, including all the input types, an integer attribute indicating if the element can take input focus (is focusable), if it should participate to sequential keyboard navigation. As all input types except for input of type hidden are focusable, this attribute should not be used on form controls, because doing so would require the management of the focus order for all elements within the document with the risk of harming usability and accessibility if done incorrectly.

[`title`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#title)

Global attribute valid for all elements, including all input types, containing a text representing advisory information related to the element it belongs to. Such information can typically, but not necessarily, be presented to the user as a tooltip. The title should NOT be used as the primary explanation of the purpose of the form control. Instead, use the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element with a `for` attribute set to the form control's [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#id)
 attribute. See [Labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels)
 below.

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)

A string specifying the type of control to render. For example, to create a checkbox, a value of `checkbox` is used. If omitted (or an unknown value is specified), the input type `text` is used, creating a plaintext input field.

Permitted values are listed in [Input types](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#input_types)
 above.

[`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)

The input control's value. When specified in the HTML, this is the initial value, and from then on it can be altered or retrieved at any time using JavaScript to access the respective [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 object's `value` property. The `value` attribute is always optional, though should be considered mandatory for `checkbox`, `radio`, and `hidden`.

[`webkitdirectory`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#webkitdirectory)

The Boolean `webkitdirectory` attribute, if present, indicates that only directories should be available to be selected by the user in the file picker interface. See [`HTMLInputElement.webkitdirectory`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/webkitdirectory)
 for additional details and examples.

**Note:** `webkitdirectory` is defined in the [File and Directory Entries API](https://developer.mozilla.org/en-US/docs/Web/API/File_and_Directory_Entries_API)
. It's named `webkitdirectory` because of its origins as a Chrome-specific API. It is now available in all browsers.

[`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#width)

Valid for the `image` input button only, the `width` is the width of the image file to display to represent the graphical submit button. See the [image](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image)
 input type.

### [Non-standard attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#non-standard_attributes)

The following non-standard attributes are also available on some browsers. As a general rule, you should avoid using them unless it can't be helped.

| Attribute | Description |
| --- | --- |
| [`incremental`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#incremental) | Whether or not to send repeated [`search`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/search_event "search")<br> events to allow updating live search results while the user is still editing the value of the field. **WebKit and Blink only (Safari, Chrome, Opera, etc.).** |
| `mozactionhint` | A string indicating the type of action that will be taken when the user presses the Enter or Return key while editing the field; this is used to determine an appropriate label for that key on a virtual keyboard. **Since this attribute is deprecated, use [`enterkeyhint`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/enterkeyhint)<br> instead.** |
| [`orient`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#orient) | Sets the orientation of the range slider. **Firefox only**. |
| [`results`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#results) | The maximum number of items that should be displayed in the drop-down list of previous search queries. **Safari only.** |

[`incremental`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#incremental)

The Boolean attribute `incremental` is a WebKit and Blink extension (so supported by Safari, Opera, Chrome, etc.) which, if present, tells the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 to process the input as a live search. As the user edits the value of the field, the user agent sends [`search`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/search_event "search")
 events to the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 object representing the search box. This allows your code to update the search results in real time as the user edits the search.

If `incremental` is not specified, the [`search`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/search_event "search")
 event is only sent when the user explicitly initiates a search (such as by pressing the Enter or Return key while editing the field).

The `search` event is rate-limited so that it is not sent more frequently than an implementation-defined interval.

[`orient`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#orient)

Similar to the -moz-orient non-standard CSS property impacting the [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)
 and [`<meter>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meter)
 elements, the `orient` attribute defines the orientation of the range slider. Values include `horizontal`, meaning the range is rendered horizontally, and `vertical`, where the range is rendered vertically. See [Creating vertical form controls](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Writing_modes/Vertical_controls)
 for a modern approach to creating vertical form controls.

[`results`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#results)

The `results` attribute—supported only by Safari—is a numeric value that lets you override the maximum number of entries to be displayed in the `<input>` element's natively-provided drop-down menu of previous search queries.

The value must be a non-negative decimal number. If not provided, or an invalid value is given, the browser's default maximum number of entries is used.

[Methods](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#methods)

----------------------------------------------------------------------------------------------

The following methods are provided by the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
 interface which represents `<input>` elements in the DOM. Also available are those methods specified by the parent interfaces, [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement)
, [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element)
, [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node)
, and [`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)
.

[`checkValidity()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/checkValidity "checkValidity()")

Returns `true` if the element's value passes validity checks; otherwise, returns `false` and fires an [`invalid`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/invalid_event "invalid")
 event at the element.

[`reportValidity()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/reportValidity "reportValidity()")

Returns `true` if the element's value passes validity checks; otherwise, returns `false`, fires an [`invalid`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/invalid_event "invalid")
 event at the element, and (if the event isn't canceled) reports the problem to the user.

[`select()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/select "select()")

Selects the entire content of the `<input>` element, if the element's content is selectable. For elements with no selectable text content (such as a visual color picker or calendar date input), this method does nothing.

[`setCustomValidity()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/setCustomValidity "setCustomValidity()")

Sets a custom message to display if the input element's value isn't valid.

[`setRangeText()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/setRangeText "setRangeText()")

Sets the contents of the specified range of characters in the input element to a given string. A `selectMode` parameter is available to allow controlling how the existing content is affected.

[`setSelectionRange()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/setSelectionRange "setSelectionRange()")

Selects the specified range of characters within a textual input element. Does nothing for inputs which aren't presented as text input fields.

[`showPicker()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/showPicker "showPicker()")

Displays the browser picker for the input element that would normally be displayed when the element is selected, but triggered from a button press or other user interaction.

[`stepDown()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/stepDown "stepDown()")

Decrements the value of a numeric input by one, by default, or by the specified number of units.

[`stepUp()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/stepUp "stepUp()")

Increments the value of a numeric input by one or by the specified number of units.

[CSS](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#css)

--------------------------------------------------------------------------------------

Inputs, being replaced elements, have a few features not applicable to non form elements. There are CSS selectors that can specifically target form controls based on their UI features, also known as UI pseudo-classes. The input element can also be targeted by type with attribute selectors. There are some properties that are especially useful as well.

### [UI pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#ui_pseudo-classes)

|     |     |
| --- | --- |Pseudo-classes relevant to the `<input>` element:
| Pseudo-class | Description |
| --- | --- |
| [`:enabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:enabled) | Any currently enabled element that can be activated (selected, clicked on, typed into, etc.) or accept focus and also has a disabled state, in which it can't be activated or accept focus. |
| [`:disabled`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:disabled) | Any currently disabled element that has an enabled state, meaning it otherwise could be activated (selected, clicked on, typed into, etc.) or accept focus were it not disabled. |
| [`:read-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-only) | Element not editable by the user |
| [`:read-write`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:read-write) | Element that is editable by the user. |
| [`:placeholder-shown`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown) | Element that is currently displaying [`placeholder` text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)<br>, including `<input>` and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)<br> elements with the [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)<br> attribute present that has, as yet, no value. |
| [`:default`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:default) | Form elements that are the default in a group of related elements. Matches [checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)<br> and [radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)<br> input types that were checked on page load or render. |
| [`:checked`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:checked) | Matches [checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)<br> and [radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)<br> input types that are currently checked (and the [`<option>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/option)<br> in a [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)<br> that is currently selected). |
| [`:indeterminate`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:indeterminate) | [checkbox](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/checkbox)<br> elements whose indeterminate property is set to true by JavaScript, [radio](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/radio)<br> elements, when all radio buttons with the same name value in the form are unchecked, and [`<progress>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/progress)<br> elements in an indeterminate state |
| [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid) | Form controls that can have constraint validation applied and are currently valid. |
| [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid) | Form controls that have constraint validation applied and are currently not valid. Matches a form control whose value doesn't match the constraints set on it by its attributes, such as [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)<br>, [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern)<br>, [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step)<br> and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)<br>. |
| [`:in-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:in-range) | A non-empty input whose current value is within the range limits specified by the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)<br> and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)<br> attributes and the [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step)<br>. |
| [`:out-of-range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:out-of-range) | A non-empty input whose current value is NOT within the range limits specified by the [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)<br> and [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)<br> attributes or does not adhere to the [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step)<br> constraint. |
| [`:required`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:required) | `<input>`, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)<br>, or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)<br> element that has the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)<br> attribute set on it. Only matches elements that can be required. The attribute included on a non-requirable element will not make for a match. |
| [`:optional`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:optional) | `<input>`, [`<select>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/select)<br>, or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)<br> element that does NOT have the [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required)<br> attribute set on it. Does not match elements that can't be required. |
| [`:blank`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:blank) | `<input>` and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)<br> elements that currently have no value. |
| [`:user-invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:user-invalid) | Similar to `:invalid`, but is activated on blur. Matches invalid input but only after the user interaction, such as by focusing on the control, leaving the control, or attempting to submit the form containing the invalid control. |
| [`:open`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:open) | `<input>` elements that display a picker for the user to choose a value from (for example [`<input type="color">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/color)<br>) — but only when the element is in the open state, that is, when the picker is displayed. |

#### Pseudo-classes example

We can style a checkbox label based on whether the checkbox is checked or not. In this example, we are styling the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 and [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
 of the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 that comes immediately after a checked input. We haven't applied any styles if the `input` is not checked.

    <input id="checkboxInput" type="checkbox" />
    <label for="checkboxInput">Toggle the checkbox on and off</label>
    

css

    input:checked + label {
      color: red;
      font-weight: bold;
    }
    

### [Attribute selectors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#attribute_selectors)

It is possible to target different types of form controls based on their [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 using [attribute selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Attribute_selectors)
. CSS attribute selectors match elements based on either just the presence of an attribute or the value of a given attribute.

css

    /* matches a password input */
    input[type="password"] {
    }
    
    /* matches a form control whose valid values are limited to a range of values */
    input[min][max] {
    }
    
    /* matches a form control with a pattern attribute */
    input[pattern] {
    }
    

### [::placeholder](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)

By default, the appearance of placeholder text is a translucent or light gray. The [`::placeholder`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder)
 pseudo-element is the input's [`placeholder` text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
. It can be styled with a limited subset of CSS properties.

css

    ::placeholder {
      color: blue;
    }
    

Only the subset of CSS properties that apply to the [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
 pseudo-element can be used in a rule using `::placeholder` in its selector.

### [caret-color](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#caret-color)

A property specific to text entry-related elements is the CSS [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
 property, which lets you set the color used to draw the text input caret:

#### HTML

html

    <label for="textInput">Note the red caret:</label>
    <input id="textInput" class="custom" size="32" />
    

#### CSS

css

    input.custom {
      caret-color: red;
      font:
        16px "Helvetica",
        "Arial",
        sans-serif;
    }
    

#### Result

### [field-sizing](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#field-sizing)

The [`field-sizing`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/field-sizing)
 property enables you to control the sizing behavior of form inputs (i.e., they are given a default preferred size by default.) This property enables you to override the default behavior, allowing form controls to adjust in size to fit their contents.

This property is typically used to create form fields that shrinkwrap their content and grow as more text is entered. This works with input types that accept direct text input (for example, [`text`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/text)
 and [`url`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/url)
), input type [`file`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
, and [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 elements.

### [object-position and object-fit](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#object-position_and_object-fit)

In certain cases (typically involving non-textual inputs and specialized interfaces), the `<input>` element is a [replaced element](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
. When it is, the position and size of the element's size and positioning within its frame can be adjusted using the CSS [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
 and [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
 properties.

### [Styling](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#styling)

For more information about adding color to elements in HTML, see:

*   [Applying color to HTML elements using CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Colors/Applying_color)
    .

Also see:

*   [Styling HTML forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Styling_web_forms)
    
*   [Advanced styling for HTML forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Advanced_form_styling)
     and

[Additional features](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#additional_features)

----------------------------------------------------------------------------------------------------------------------

### [Labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels)

Labels are needed to associate assistive text with an `<input>`. The [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element provides explanatory information about a form field that is _always_ appropriate (aside from any layout concerns you have). It's never a bad idea to use a `<label>` to explain what should be entered into an `<input>` or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
.

#### Associated labels

The semantic pairing of `<input>` and `<label>` elements is useful for assistive technologies such as screen readers. By pairing them using the `<label>`'s [`for`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#for)
 attribute, you bond the label to the input in a way that lets screen readers describe inputs to users more precisely.

It does not suffice to have plain text adjacent to the `<input>` element. Rather, usability and accessibility requires the inclusion of either implicit or explicit [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
:

html

    <!-- inaccessible -->
    <p>Enter your name: <input id="name" type="text" size="30" /></p>
    
    <!-- implicit label -->
    <p>
      <label>Enter your name: <input id="name" type="text" size="30" /></label>
    </p>
    
    <!-- explicit label -->
    <p>
      <label for="name">Enter your name: </label>
      <input id="name" type="text" size="30" />
    </p>
    

The first example is inaccessible: no relationship exists between the prompt and the `<input>` element.

In addition to an accessible name, the label provides a larger 'hit' area for mouse and touch screen users to click on or touch. By pairing a `<label>` with an `<input>`, clicking on either one will focus the `<input>`. If you use plain text to "label" your input, this won't happen. Having the prompt part of the activation area for the input is helpful for people with motor control conditions.

As web developers, it's important that we never assume that people will know all the things that we know. The diversity of people using the web—and by extension your website—practically guarantees that some of your site's visitors will have some variation in thought processes and/or circumstances that leads them to interpret your forms very differently from you without clear and properly-presented labels.

#### Placeholders are not accessible

The [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
 attribute lets you specify text that appears within the `<input>` element's content area itself when it is empty. The placeholder should never be required to understand your forms. It is not a label, and should not be used as a substitute, because it isn't. The placeholder is used to provide a hint as to what an inputted value should look like, not an explanation or prompt.

Not only is the placeholder not accessible to screen readers, but once the user enters any text into the form control, or if the form control already has a value, the placeholder disappears. Browsers with automatic page translation features may skip over attributes when translating, meaning the `placeholder` may not get translated.

**Note:** Don't use the [`placeholder`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
 attribute if you can avoid it. If you need to label an `<input>` element, use the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element.

### [Client-side validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#client-side_validation)

**Warning:** Client-side validation is useful, but it does _not_ guarantee that the server will receive valid data. If the data must be in a specific format, _always_ verify it also on the server-side, and return a [`400` HTTP response](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/400)
 if the format is invalid.

In addition to using CSS to style inputs based on the [`:valid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:valid)
 or [`:invalid`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:invalid)
 UI states based on the current state of each input, as noted in the [UI pseudo-classes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#ui_pseudo-classes)
 section above, the browser provides for client-side validation on (attempted) form submission. On form submission, if there is a form control that fails constraint validation, supporting browsers will display an error message on the first invalid form control; displaying a default message based on the error type, or a message set by you.

Some input types and other attributes place limits on what values are valid for a given input. For example, `<input type="number" min="2" max="10" step="2">` means only the number 2, 4, 6, 8, or 10 are valid. Several errors could occur, including a `rangeUnderflow` error if the value is less than 2, `rangeOverflow` if greater than 10, `stepMismatch` if the value is a number between 2 and 10, but not an even integer (does not match the requirements of the `step` attribute), or `typeMismatch` if the value is not a number.

For the input types whose domain of possible values is periodic (that is, at the highest possible value, the values wrap back around to the beginning rather than ending), it's possible for the values of the [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max)
 and [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min)
 properties to be reversed, which indicates that the range of permitted values starts at `min`, wraps around to the lowest possible value, then continues on until `max` is reached. This is particularly useful for dates and times, such as when you want to allow the range to be from 8 PM to 8 AM:

html

    <input type="time" min="20:00" max="08:00" name="overnight" />
    

Specific attributes and their values can lead to a specific error [`ValidityState`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState)
:

|     |     |     |
| --- | --- | --- |Validity object errors depend on the `<input>` attributes and their values:
| Attribute | Relevant property | Description |
| --- | --- | --- |
| [`max`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#max) | [`validityState.rangeOverflow`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeOverflow) | Occurs when the value is greater than the maximum value as defined by the `max` attribute |
| [`maxlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#maxlength) | [`validityState.tooLong`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/tooLong) | Occurs when the number of characters is greater than the number allowed by the `maxlength` property |
| [`min`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#min) | [`validityState.rangeUnderflow`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeUnderflow) | Occurs when the value is less than the minimum value as defined by the `min` attribute |
| [`minlength`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#minlength) | [`validityState.tooShort`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/tooShort) | Occurs when the number of characters is less than the number required by the `minlength` property |
| [`pattern`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#pattern) | [`validityState.patternMismatch`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/patternMismatch) | Occurs when a pattern attribute is included with a valid regular expression and the `value` does not match it. |
| [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required) | [`validityState.valueMissing`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/valueMissing) | Occurs when the `required` attribute is present but the value is `null` or radio or checkbox is not checked. |
| [`step`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#step) | [`validityState.stepMismatch`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/stepMismatch) | The value doesn't match the step increment. Increment default is `1`, so only integers are valid on `type="number"` is step is not included. `step="any"` will never throw this error. |
| [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type) | [`validityState.typeMismatch`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/typeMismatch) | Occurs when the value is not of the correct type, for example an email does not contain an `@` or a url doesn't contain a protocol. |

If a form control doesn't have the `required` attribute, no value, or an empty string, is not invalid. Even if the above attributes are present, with the exception of `required`, an empty string will not lead to an error.

We can set limits on what values we accept, and supporting browsers will natively validate these form values and alert the user if there is a mistake when the form is submitted.

In addition to the errors described in the table above, the `validityState` interface contains the `badInput`, `valid`, and `customError` boolean readonly properties. The validity object includes:

*   [`validityState.valueMissing`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/valueMissing)
    
*   [`validityState.typeMismatch`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/typeMismatch)
    
*   [`validityState.patternMismatch`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/patternMismatch)
    
*   [`validityState.tooLong`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/tooLong)
    
*   [`validityState.tooShort`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/tooShort)
    
*   [`validityState.rangeUnderflow`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeUnderflow)
    
*   [`validityState.rangeOverflow`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/rangeOverflow)
    
*   [`validityState.stepMismatch`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/stepMismatch)
    
*   [`validityState.badInput`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState/badInput)
    
*   [`validityState.valid`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState "validityState.valid")
    
*   [`validityState.customError`](https://developer.mozilla.org/en-US/docs/Web/API/ValidityState "validityState.customError")
    

For each of these Boolean properties, a value of `true` indicates that the specified reason validation may have failed is true, with the exception of the `valid` property, which is `true` if the element's value obeys all constraints.

If there is an error, supporting browsers will both alert the user and prevent the form from being submitted. A word of caution: if a custom error is set to a truthy value (anything other than the empty string or `null`), the form will be prevented from being submitted. If there is no custom error message, and none of the other properties return true, `valid` will be true, and the form can be submitted.

js

    function validate(input) {
      let validityState = input.validity;
      if (validityState.valueMissing) {
        input.setCustomValidity("A value is required");
      } else if (validityState.rangeUnderflow) {
        input.setCustomValidity("Your value is too low");
      } else if (validityState.rangeOverflow) {
        input.setCustomValidity("Your value is too high");
      } else {
        input.setCustomValidity("");
      }
    }
    

The last line, setting the custom validity message to the empty string is vital. If the user makes an error, and the validity is set, it will fail to submit, even if all the values are valid, until the message is `null`.

#### Custom validation error example

If you want to present a custom error message when a field fails to validate, you need to use the [Constraint Validation API](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Form_validation#validating_forms_using_javascript)
 available on `<input>` (and related) elements. Take the following form:

html

    <form>
      <label for="name">Enter username (upper and lowercase letters): </label>
      <input type="text" name="name" id="name" required pattern="[A-Za-z]+" />
      <button>Submit</button>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

The basic HTML form validation features will cause this to produce a default error message if you try to submit the form with either no valid filled in, or a value that does not match the `pattern`.

If you wanted to instead display custom error messages, you could use JavaScript like the following:

js

    const nameInput = document.querySelector("input");
    
    nameInput.addEventListener("input", () => {
      nameInput.setCustomValidity("");
      nameInput.checkValidity();
    });
    
    nameInput.addEventListener("invalid", () => {
      if (nameInput.value === "") {
        nameInput.setCustomValidity("Enter your username!");
      } else {
        nameInput.setCustomValidity(
          "Usernames can only contain upper and lowercase letters. Try again!",
        );
      }
    });
    

The example renders like so:

In brief:

*   We check the valid state of the input element every time its value is changed by running the `checkValidity()` method via the `input` event handler.
*   If the value is invalid, an `invalid` event is raised, and the `invalid` event handler function is run. Inside this function we work out whether the value is invalid because it is empty, or because it doesn't match the pattern, using an `if ()` block, and set a custom validity error message.
*   As a result, if the input value is invalid when the submit button is pressed, one of the custom error messages will be shown.
*   If it is valid, it will submit as you'd expect. For this to happen, the custom validity has to be canceled, by invoking `setCustomValidity()` with an empty string value. We therefore do this every time the `input` event is raised. If you don't do this, and a custom validity was previously set, the input will register as invalid, even if it currently contains a valid value on submission.

**Note:** Always validate input constraints both client side and server side. Constraint validation doesn't remove the need for validation on the _server side_. Invalid values can still be sent by older browsers or by bad actors.

**Note:** Firefox supported a proprietary error attribute — `x-moz-errormessage` — for many versions, which allowed you set custom error messages in a similar way. This has been removed as of version 66 (see [Firefox bug 1513890](https://bugzil.la/1513890 "External link (opens in new tab)")
).

### [Localization](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#localization)

The allowed inputs for certain `<input>` types depend on the locale. In some locales, 1,000.00 is a valid number, while in other locales the valid way to enter this number is 1.000,00.

Firefox uses the following heuristics to determine the locale to validate the user's input (at least for `type="number"`):

*   Try the language specified by a `lang`/`xml:lang` attribute on the element or any of its parents.
*   Try the language specified by any `Content-Language` HTTP header. Or,
*   If none specified, use the browser's locale.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#accessibility)

----------------------------------------------------------------------------------------------------------

### [Labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels_2)

When including inputs, it is an accessibility requirement to add labels alongside. This is needed so those who use assistive technologies can tell what the input is for. Also, clicking or touching a label gives focus to the label's associated form control. This improves the accessibility and usability for sighted users, increases the area a user can click or touch to activate the form control. This is especially useful (and even needed) for radio buttons and checkboxes, which are tiny. For more information about labels in general see [Labels](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#labels)
.

The following is an example of how to associate the `<label>` with an `<input>` element in the above style. You need to give the `<input>` an `id` attribute. The `<label>` then needs a `for` attribute whose value is the same as the input's `id`.

html

    <label for="peas">Do you like peas?</label>
    <input type="checkbox" name="peas" id="peas" />
    

### [Size](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#size)

Interactive elements such as form input should provide an area large enough that it is easy to activate them. This helps a variety of people, including people with motor control issues and people using non-precise forms of input such as a stylus or fingers. A minimum interactive size of 44×44 [CSS pixels](https://w3c.github.io/wcag/guidelines/22/#dfn-css-pixels "External link (opens in new tab)")
 is recommended.

*   [Understanding Success Criterion 2.5.5: Target Size | W3C Understanding WCAG 2.1](https://www.w3.org/WAI/WCAG21/Understanding/target-size.html "External link (opens in new tab)")
    
*   [Target Size and 2.5.5 | Adrian Roselli](https://adrianroselli.com/2019/06/target-size-and-2-5-5.html "External link (opens in new tab)")
    
*   [Quick test: Large touch targets - The A11Y Project](https://www.a11yproject.com/posts/large-touch-targets/ "External link (opens in new tab)")
    

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#technical_summary)

------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, listed, submittable, resettable, form-associated element, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. If the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)<br> is not `hidden`, then labelable element, palpable content. |
| Permitted content | None; it is a [void element](https://developer.mozilla.org/en-US/docs/Glossary/Void_element)<br>. |
| Tag omission | Must have a start tag and must not have an end tag. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | *   `type=button`: `[button](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role) `<br>*   `type=checkbox`: `[checkbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/checkbox_role) `<br>*   `type=email`<br>    *   with no `list` attribute: `[textbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role) `<br>    *   with `list` attribute: [`combobox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role)<br>        <br>*   `type=image`: `[button](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role) `<br>*   `type=number`: [`spinbutton`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/spinbutton_role)<br>    <br>*   `type=radio`: [`radio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radio_role)<br>    <br>*   `type=range`: [`slider`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/slider_role)<br>    <br>*   `type=reset`: `[button](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role) `<br>*   `type=search`<br>    *   with no `list` attribute: [`searchbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/searchbox_role)<br>        <br>    *   with `list` attribute: [`combobox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role)<br>        <br>*   `type=submit`: `[button](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role) `<br>*   `type=tel`<br>    *   with no `list` attribute: `[textbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role) `<br>    *   with `list` attribute: [`combobox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role)<br>        <br>*   `type=text`<br>    *   with no `list` attribute: `[textbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role) `<br>    *   with `list` attribute: [`combobox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role)<br>        <br>*   `type=url`<br>    *   with no `list` attribute: `[textbox](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/textbox_role) `<br>    *   with `list` attribute: [`combobox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role)<br>        <br>*   `type=color\|date\|datetime-local\|file\|hidden\|month\|password\|time\|week`: [no corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | *   `type=button`: [`checkbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/checkbox_role)<br>    , [`combobox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role)<br>    , [`link`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/link_role)<br>    , [`menuitem`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitem_role)<br>    , [`menuitemcheckbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemcheckbox_role)<br>    , [`menuitemradio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemradio_role)<br>    , [`option`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/option_role)<br>    , [`radio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radio_role)<br>    , [`switch`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/switch_role)<br>    , [`tab`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/tab_role)<br>    <br>*   `type=checkbox`: [`button`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role)<br>     when used with `aria-pressed`, [`menuitemcheckbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemcheckbox_role)<br>    , [`option`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/option_role)<br>    , [`switch`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/switch_role)<br>    <br>*   `type=image`: [`link`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/link_role)<br>    , [`menuitem`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitem_role)<br>    , [`menuitemcheckbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemcheckbox_role)<br>    , [`menuitemradio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemradio_role)<br>    , [`radio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/radio_role)<br>    , [`switch`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/switch_role)<br>    <br>*   `type=radio`: [`menuitemradio`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/menuitemradio_role)<br>    <br>*   `type=text` with no `list` attribute: [`combobox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/combobox_role)<br>    , [`searchbox`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/searchbox_role)<br>    , [`spinbutton`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/spinbutton_role)<br>    <br>*   `type=color\|date\|datetime-local\|email\|file\|hidden\|` `month\|number\|password\|range\|reset\|search\|submit\|tel\|url\|week` or `text` with `list` attribute: no `role` permitted |
| DOM interface | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#specifications)

------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-input-element](https://html.spec.whatwg.org/multipage/input.html#the-input-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#see_also)

------------------------------------------------------------------------------------------------

*   CSS [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
     property
*   [Your first HTML form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Your_first_form)
    
*   [How to structure an HTML form](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/How_to_structure_a_web_form)
    
*   [The native form widgets](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Basic_native_form_controls)
    
*   [Sending form data](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Sending_and_retrieving_form_data)
    
*   [Form constraint validation](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Constraint_validation)
    
*   [Styling HTML forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Styling_web_forms)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F5c76c9c822b4083750ff7fcabcd07422ad3a591b%0A*+Document+last+modified%3A+2026-11-05T12%3A45%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")