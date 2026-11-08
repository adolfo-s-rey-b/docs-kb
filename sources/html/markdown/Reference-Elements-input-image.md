*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#mdn-search)
    

`<input type="image">` HTML attribute value
===========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of type **`image`** are used to create graphical submit buttons, i.e., submit buttons that take the form of an image rather than text.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#try_it)

--------------------------------------------------------------------------------------------------

    <p>Sign in to your account:</p>
    
    <div>
      <label for="userId">User ID</label>
      <input type="text" id="userId" name="userId" />
    </div>
    
    <input
      type="image"
      id="image"
      alt="Login"
      src="/shared-assets/images/examples/login-button.png" />
    

    label {
      font-size: 0.8rem;
    }
    
    label,
    input[type="image"] {
      margin-top: 1rem;
    }
    
    input[type="image"] {
      width: 80px;
    }
    

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#value)

------------------------------------------------------------------------------------------------

`<input type="image">` elements do not accept `value` attributes. The path to the image to be displayed is specified in the `src` attribute.

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#additional_attributes)

--------------------------------------------------------------------------------------------------------------------------------

In addition to the attributes shared by all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, `image` button inputs support the following attributes.

### [alt](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#alt)

The `alt` attribute provides an alternate string to use as the button's label if the image cannot be shown (due to error, a [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 that cannot or is configured not to show images, or if the user is using a screen reading device). If provided, it must be a non-empty string appropriate as a label for the button.

For example, if you have a graphical button that shows an image with an icon and/or image text "Login Now", you should also set the `alt` attribute to something like `Login Now`.

**Note:** While the `alt` attribute is technically optional, you should always include one to maximize the usability of your content.

Functionally, the `alt` attribute of the `<input type="image">` element works just like the [`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#alt)
 attribute on [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 elements.

### [formaction](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#formaction)

A string indicating the URL to which to submit the data. This takes precedence over the [`action`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#action)
 attribute on the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element that owns the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
.

This attribute is also available on [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements.

### [formenctype](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#formenctype)

A string that identifies the encoding method to use when submitting the form data to the server. There are three permitted values:

[`application/x-www-form-urlencoded`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#applicationx-www-form-urlencoded)

This, the default value, sends the form data as a string after [percent-encoding](https://developer.mozilla.org/en-US/docs/Glossary/Percent-encoding)
 the text using an algorithm such as [`encodeURI()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
.

[`multipart/form-data`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#multipartform-data)

Uses the [`FormData`](https://developer.mozilla.org/en-US/docs/Web/API/FormData)
 API to manage the data, allowing for files to be submitted to the server. You _must_ use this encoding type if your form includes any [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements of [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 `file` ([`<input type="file">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
).

[`text/plain`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#textplain)

Plain text; mostly useful only for debugging, so you can easily see the data that's to be submitted.

If specified, the value of the `formenctype` attribute overrides the owning form's [`enctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#enctype)
 attribute.

This attribute is also available on [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements.

### [formmethod](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#formmethod)

A string indicating the HTTP method to use when submitting the form's data; this value overrides any [`method`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#method)
 attribute given on the owning form. Permitted values are:

[`get`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#get)

A URL is constructed by starting with the URL given by the `formaction` or [`action`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#action)
 attribute, appending a question mark ("?") character, then appending the form's data, encoded as described by `formenctype` or the form's [`enctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#enctype)
 attribute. This URL is then sent to the server using an HTTP [`get`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/GET)
 request. This method works well for forms that contain only [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 characters and have no side effects. This is the default value.

[`post`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#post)

The form's data is included in the body of the request that is sent to the URL given by the `formaction` or [`action`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#action)
 attribute using an HTTP [`post`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods/POST)
 request. This method supports complex data and file attachments.

[`dialog`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#dialog)

This method is used to indicate that the button closes the dialog with which the input is associated, and does not transmit the form data at all.

This attribute is also available on [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements.

### [formnovalidate](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#formnovalidate)

A Boolean attribute which, if present, specifies that the form should not be validated before submission to the server. This overrides the value of the [`novalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#novalidate)
 attribute on the element's owning form.

This attribute is also available on [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements.

### [formtarget](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#formtarget)

A string which specifies a name or keyword that indicates where to display the response received after submitting the form. The string must be the name of a **browsing context** (that is, a tab, window, or [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
. A value specified here overrides any target given by the [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#target)
 attribute on the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 that owns this input.

In addition to the actual names of tabs, windows, or inline frames, there are a few special keywords that can be used:

[`_self`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#_self)

Loads the response into the same browsing context as the one that contains the form. This will replace the current document with the received data. This is the default value used if none is specified.

[`_blank`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#_blank)

Loads the response into a new, unnamed, browsing context. This is typically a new tab in the same window as the current document, but may differ depending on the configuration of the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
.

[`_parent`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#_parent)

Loads the response into the parent browsing context of the current one. If there is no parent context, this behaves the same as `_self`.

[`_top`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#_top)

Loads the response into the top-level browsing context; this is the browsing context that is the topmost ancestor of the current context. If the current context is the topmost context, this behaves the same as `_self`.

This attribute is also available on [`<input type="submit">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 and [`<button>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/button)
 elements.

### [height](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#height)

A number specifying the height, in CSS pixels, at which to draw the image specified by the `src` attribute.

### [src](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#src)

A string specifying the URL of the image file to display to represent the graphical submit button. When the user interacts with the image, the input is handled like any other button input.

### [width](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#width)

A number indicating the width at which to draw the image, in CSS pixels.

[Obsolete attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#obsolete_attributes)

----------------------------------------------------------------------------------------------------------------------------

The following attribute was defined by HTML 4 for `image` inputs, but was not implemented by all browsers and has since been deprecated.

### [usemap](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#usemap)

If `usemap` is specified, it must be the name of an image map element, [`<map>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map)
, that defines an image map to use with the image. This usage is obsolete; you should switch to using the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element when you want to use image maps.

[Using image inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#using_image_inputs)

--------------------------------------------------------------------------------------------------------------------------

The `<input type="image">` element is a [replaced element](https://developer.mozilla.org/en-US/docs/Glossary/Replaced_elements)
 (an element whose content isn't generated or directly managed by the CSS layer), behaving in much the same way as a regular [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element, but with the capabilities of a [submit button](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
.

### [Essential image input features](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#essential_image_input_features)

Let's look at a basic example that includes all the essential features you'd need to use (These work exactly the same as they do on the `<img>` element.):

html

    <input
      id="image"
      type="image"
      width="100"
      height="30"
      alt="Login"
      src="https://mdn.github.io/shared-assets/images/examples/login-button.png" />
    

*   The [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#src)
     attribute is used to specify the path to the image you want to display in the button.
*   The [`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#alt)
     attribute provides alt text for the image, so screen reader users can get a better idea of what the button is used for. It will also display if the image can't be shown for any reason (for example if the path is misspelled). If possible, use text which matches the label you'd use if you were using a standard submit button.
*   The [`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#width)
     and [`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#height)
     attributes are used to specify the width and height the image should be shown at, in pixels. The button is the same size as the image; if you need the button's hit area to be bigger than the image, you will need to use CSS (e.g., [`padding`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/padding)
    ). Also, if you specify only one dimension, the other is automatically adjusted so that the image maintains its original [aspect ratio](https://developer.mozilla.org/en-US/docs/Glossary/Aspect_ratio)
    .

### [Overriding default form behaviors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#overriding_default_form_behaviors)

`<input type="image">` elements — like regular [submit buttons](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/submit)
 — can accept a number of attributes that override the default form behavior:

[`formaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#formaction_2)

The URI of a program that processes the information submitted by the input element; overrides the [`action`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#action)
 attribute of the element's form owner.

[`formenctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#formenctype_2)

Specifies the type of content that is used to submit the form to the server. Possible values are:

*   `application/x-www-form-urlencoded`: The default value if the attribute is not specified.
*   `text/plain`.

If this attribute is specified, it overrides the [`enctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#enctype)
 attribute of the element's form owner.

[`formmethod`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#formmethod_2)

Specifies the HTTP method that the browser uses to submit the form. Possible values are:

*   `post`: The data from the form is included in the body of the form and is sent to the server.
*   `get`: The data from the form is appended to the **`form`** attribute URI, with a '?' as a separator, and the resulting URI is sent to the server. Use this method when the form has no side effects and contains only ASCII characters.

If specified, this attribute overrides the [`method`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#method)
 attribute of the element's form owner.

[`formnovalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#formnovalidate_2)

A Boolean attribute specifying that the form is not to be validated when it is submitted. If this attribute is specified, it overrides the [`novalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#novalidate)
 attribute of the element's form owner.

[`formtarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#formtarget_2)

A name or keyword indicating where to display the response that is received after submitting the form. This is a name of, or keyword for, a _browsing context_ (for example, tab, window, or inline frame). If this attribute is specified, it overrides the [`target`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form#target)
 attribute of the element's form owner. The following keywords have special meanings:

*   `_self`: Load the response into the same browsing context as the current one. This value is the default if the attribute is not specified.
*   `_blank`: Load the response into a new unnamed browsing context.
*   `_parent`: Load the response into the parent browsing context of the current one. If there is no parent, this option behaves the same way as `_self`.
*   `_top`: Load the response into the top-level browsing context (that is, the browsing context that is an ancestor of the current one, and has no parent). If there is no parent, this option behaves the same as `_self`.

### [Using the x and y data points](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#using_the_x_and_y_data_points)

When you submit a form using a button created with `<input type="image">`, two extra data points are submitted to the server automatically by the browser — `x` and `y`. You can see this in action in our [X Y coordinates example](https://mdn.github.io/learning-area/html/forms/image-type-xy-coords/ "External link (opens in new tab)")
.

When you click on the image to submit the form, you'll see the data appended to the URL as parameters, such as `?x=52&y=55`. If the image input has a [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#name)
 attribute, then the specified name is prefixed to each coordinate entry's name with a dot separator. For example, if the `name` were `position`, then the returned coordinates would be formatted in the URL as `?position.x=52&position.y=55`.

These are the X and Y coordinates of the image that the mouse clicked on to submit the form, where (0,0) is the top-left of the image and the default in case submission happens without a click on the image. These can be used when the position the image was clicked on is significant, for example you might have a map that when clicked, sends the coordinates that were clicked to the server. The server-side code then works out what location was clicked on, and returns information about places nearby.

In our above example, we could write server-side code that works out what color was clicked on by the coordinates submitted, and keeps a tally of the favorite colors people voted for.

### [Adjusting the image's position and scaling algorithm](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#adjusting_the_images_position_and_scaling_algorithm)

You can use the [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
 property to adjust the positioning of the image within the `<input>` element's frame, and the [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
 property to control how the image's size is adjusted to fit within the frame. This allows you to specify a frame for the image using the `width` and `height` attributes to set aside space in the layout, then adjust where within that space the image is located and how (or if) it is scaled to occupy that space.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#examples)

------------------------------------------------------------------------------------------------------

### [A login form](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#a_login_form)

The following example shows the same button as before, but included in the context of a typical login form.

#### HTML

html

    <form>
      <p>Login to your account</p>
      <div>
        <label for="userId">User ID</label>
        <input type="text" id="userId" name="userId" />
      </div>
      <div>
        <label for="pwd">Password</label>
        <input type="password" id="pwd" name="pwd" />
      </div>
      <div>
        <input
          id="image"
          type="image"
          src="https://mdn.github.io/shared-assets/images/examples/login-button.png"
          alt="Login"
          width="100" />
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

#### CSS

And now some CSS to make the basic elements sit more neatly:

css

    div {
      margin-bottom: 10px;
    }
    
    label {
      display: inline-block;
      width: 70px;
      text-align: right;
      padding-right: 10px;
    }
    

#### Result

### [Adjusting the image position and scaling](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#adjusting_the_image_position_and_scaling)

In this example, we adapt the previous example to set aside more space for the image and then adjust the actual image's size and positioning using [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
 and [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
.

#### HTML

html

    <form>
      <p>Login to your account</p>
      <div>
        <label for="userId">User ID</label>
        <input type="text" id="userId" name="userId" />
      </div>
      <div>
        <label for="pwd">Password</label>
        <input type="password" id="pwd" name="pwd" />
      </div>
      <div>
        <input
          id="image"
          type="image"
          src="https://mdn.github.io/shared-assets/images/examples/login-button.png"
          alt="Login"
          width="100" />
      </div>
    </form>
    

    document.querySelector("form").addEventListener("submit", (event) => {
      event.preventDefault();
    });
    

#### CSS

css

    div {
      margin-bottom: 10px;
    }
    
    label {
      display: inline-block;
      width: 70px;
      text-align: right;
      padding-right: 10px;
    }
    
    #image {
      object-position: right top;
      object-fit: contain;
      background-color: #dddddd;
    }
    

#### Result

Here, `object-position` is configured to draw the image in the top-right corner of the element, while `object-fit` is set to `contain`, which indicates that the image should be drawn at the largest size that will fit within the element's box without altering its aspect ratio. Note the visible gray background of the element still visible in the area not covered by the image.

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#technical_summary)

------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#value)<br>** | None — the `value` attribute should not be specified. |
| **Events** | None. |
| **Supported common attributes** | [`alt`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#alt)<br>, [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#src)<br>, [`width`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#width)<br>, [`height`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#height)<br>, [`formaction`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formaction)<br>, [`formenctype`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formenctype)<br>, [`formmethod`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formmethod)<br>, [`formnovalidate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formmethod)<br>, [`formtarget`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#formtarget) |
| **IDL attributes** | None. |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | [`button`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# image-button-state-(type=image)](https://html.spec.whatwg.org/multipage/input.html#image-button-state-(type=image)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image#see_also)

------------------------------------------------------------------------------------------------------

*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
     and the [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement)
     interface which implements it.
*   The HTML [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
     element
*   Positioning and sizing the image within the `<input>` element's frame: [`object-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-position)
     and [`object-fit`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/object-fit)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/image/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/image/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/image (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fimage&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fimage%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Fimage%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Fimage%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")