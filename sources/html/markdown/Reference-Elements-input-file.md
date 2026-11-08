*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#mdn-search)
    

`<input type="file">` HTML attribute value
==========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

[`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements with **`type="file"`** let the user choose one or more files from their device storage. Once chosen, the files can be uploaded to a server using [form submission](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
, or manipulated using JavaScript code and [the File API](https://developer.mozilla.org/en-US/docs/Web/API/File_API/Using_files_from_web_applications)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#try_it)

-------------------------------------------------------------------------------------------------

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#value)

-----------------------------------------------------------------------------------------------

A file input's [`value`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#value)
 attribute contains a string that represents the path to the selected file(s). If no file is selected yet, the value is an empty string (`""`). When the user selected multiple files, the `value` represents the first file in the list of files they selected. The other files can be identified using the [input's `HTMLInputElement.files` property](https://developer.mozilla.org/en-US/docs/Web/API/File_API/Using_files_from_web_applications#getting_information_about_selected_files)
.

**Note:** The value is [always the file's name prefixed with `C:\fakepath\`](https://html.spec.whatwg.org/multipage/input.html#fakepath-srsly "External link (opens in new tab)")
, which isn't the real path of the file. This is to prevent malicious software from guessing the user's file structure.

[Additional attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#additional_attributes)

-------------------------------------------------------------------------------------------------------------------------------

In addition to the common attributes shared by all [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements, inputs of type `file` also support the following attributes.

### [accept](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#accept)

The [`accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept)
 attribute value is a string that defines the file types the file input should accept. This string is a comma-separated list of **[unique file type specifiers](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#unique_file_type_specifiers)
**. Because a given file type may be identified in more than one manner, it's useful to provide a thorough set of type specifiers when you need files of a given format.

For instance, there are a number of ways Microsoft Word files can be identified, so a site that accepts Word files might use an `<input>` like this:

### [capture](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#capture)

The [`capture`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture)
 attribute value is a string that specifies which camera to use for capture of image or video data, if the [`accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept)
 attribute indicates that the input should be of one of those types. A value of `user` indicates that the user-facing camera and/or microphone should be used. A value of `environment` specifies that the outward-facing camera and/or microphone should be used. If this attribute is missing, the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 is free to decide on its own what to do. If the requested facing mode isn't available, the user agent may fall back to its preferred default mode.

**Note:** `capture` was previously a Boolean attribute which, if present, requested that the device's media capture device(s) such as camera or microphone be used instead of requesting a file input.

### [multiple](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#multiple)

When the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/multiple)
 Boolean attribute is specified, the file input allows the user to select more than one file.

### [webkitdirectory](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#webkitdirectory)

The Boolean `webkitdirectory` attribute, if present, indicates that only directories should be available to be selected by the user in the file picker interface. See [`HTMLInputElement.webkitdirectory`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/webkitdirectory)
 for additional details and examples.

**Note:** `webkitdirectory` is defined in the [File and Directory Entries API](https://developer.mozilla.org/en-US/docs/Web/API/File_and_Directory_Entries_API)
. It's named `webkitdirectory` because of its origins as a Chrome-specific API. It is now available in all browsers.

[Unique file type specifiers](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#unique_file_type_specifiers)

-------------------------------------------------------------------------------------------------------------------------------------------

A **unique file type specifier** is a string that describes a type of file that may be selected by the user in an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element of type `file`. Each unique file type specifier may take one of the following forms:

*   A valid case-insensitive filename extension, starting with a period (".") character. For example: `.jpg`, `.pdf`, or `.doc`.
*   A valid MIME type string, with no extensions.
*   The string `audio/*` meaning "any audio file".
*   The string `video/*` meaning "any video file".
*   The string `image/*` meaning "any image file".

The `accept` attribute takes a string containing one or more of these unique file type specifiers as its value, separated by commas. For example, a file picker that needs content that can be presented as an image, including both standard image formats and PDF files, might look like this:

[Using file inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#using_file_inputs)

-----------------------------------------------------------------------------------------------------------------------

### [A basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#a_basic_example)

This produces the following output:

Regardless of the user's device or operating system, the file input provides a button that opens up a file picker dialog that allows the user to choose a file.

Including the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#multiple)
 attribute, as shown above, specifies that multiple files can be chosen at once. The user can choose multiple files from the file picker in any way that their chosen platform allows (e.g., by holding down Shift or Control and then clicking). If you only want the user to choose a single file per `<input>`, omit the `multiple` attribute.

### [Getting information on selected files](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#getting_information_on_selected_files)

The selected files are returned by the element's `HTMLInputElement.files` property, which is a [`FileList`](https://developer.mozilla.org/en-US/docs/Web/API/FileList)
 object containing a list of [`File`](https://developer.mozilla.org/en-US/docs/Web/API/File)
 objects. The `FileList` behaves like an array, so you can check its `length` property to get the number of selected files.

Each `File` object contains the following information:

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#name)

The file's name.

[`lastModified`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#lastmodified)

A number specifying the date and time at which the file was last modified, in milliseconds since the UNIX epoch (January 1, 1970, at midnight).

[`lastModifiedDate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#lastmodifieddate)

A [`Date`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date)
 object representing the date and time at which the file was last modified. _This is deprecated and should not be used. Use `lastModified` instead._

[`size`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#size)

The size of the file in bytes.

[`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#type)

The file's [MIME type](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types)
.

[`webkitRelativePath`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#webkitrelativepath)

A string specifying the file's path relative to the base directory selected in a directory picker (that is, a `file` picker in which the [`webkitdirectory`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#webkitdirectory)
 attribute is set). _This is non-standard and should be used with caution._

### [Limiting accepted file types](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#limiting_accepted_file_types)

Often you won't want the user to be able to pick any arbitrary type of file; instead, you often want them to select files of a specific type or types. For example, if your file input lets users upload a profile picture, you probably want them to select web-compatible image formats, such as [JPEG](https://developer.mozilla.org/en-US/docs/Glossary/JPEG)
 or [PNG](https://developer.mozilla.org/en-US/docs/Glossary/PNG)
.

Acceptable file types can be specified with the [`accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#accept)
 attribute, which takes a comma-separated list of allowed file extensions or MIME types. Some examples:

*   `accept="image/png"` or `accept=".png"` — Accepts PNG files.
*   `accept="image/png, image/jpeg"` or `accept=".png, .jpg, .jpeg"` — Accept PNG or JPEG files.
*   `accept="image/*"` — Accept any file with an `image/*` MIME type. (Many mobile devices also let the user take a picture with the camera when this is used.)
*   `accept=".doc,.docx,.xml,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document"` — accept anything that smells like an MS Word document.

Let's look at a more complete example:

This produces a similar-looking output to the previous example:

It may look similar, but if you try selecting a file with this input, you'll see that the file picker only lets you select the file types specified in the `accept` value (the exact interface differs across browsers and operating systems).

The `accept` attribute doesn't validate the types of the selected files; it provides hints for browsers to guide users towards selecting the correct file types. It is still possible (in most cases) for users to toggle an option in the file chooser that makes it possible to override this and select any file they wish, and then choose incorrect file types.

Because of this, you should make sure that the `accept` attribute is backed up by appropriate server-side validation.

### [Detecting cancellations](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#detecting_cancellations)

The `cancel` event is fired when the user does not change their selection, reselecting the previously selected files. The `cancel` event is also fired when the file picker dialog gets closed, or canceled, via the "cancel" button or the escape key.

For example, the following code will log to the console if the user closes the popup without selecting a file:

### [Notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#notes)

1.  You cannot set the value of a file picker from a script — doing something like the following has no effect:
    
2.  When a file is chosen using an `<input type="file">`, the real path to the source file is not shown in the input's `value` attribute for obvious security reasons. Instead, the filename is shown, with `C:\fakepath\` prepended to it. There are some historical reasons for this quirk, but it is supported across all modern browsers, and in fact is [defined in the spec](https://html.spec.whatwg.org/multipage/forms.html#fakepath-srsly "External link (opens in new tab)")
    .
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#examples)

-----------------------------------------------------------------------------------------------------

### [Complete file example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#complete_file_example)

In this example, we'll present a slightly more advanced file chooser that takes advantage of the file information available in the `HTMLInputElement.files` property, as well as showing off a few clever tricks.

#### HTML

The HTML looks like so:

This is similar to what we've seen earlier, so we won't spend time describing it. Also, we've hidden the CSS applied to the example, as it isn't relevant to understanding the file input or the JavaScript that powers it.

#### JavaScript

In the first lines of script, we get references to the form input itself, and the [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 element with the class of `.preview`. Next, we hide the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element — we do this because file inputs tend to be ugly, difficult to style, and inconsistent in their design across browsers. You can activate the `input` element by clicking its [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
, so it is better to visually hide the `input` and style the label like a button, so the user will know to interact with it if they want to upload files.

**Note:** [`opacity`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/opacity)
 is used to hide the file input instead of [`visibility: hidden`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/visibility)
 or [`display: none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
, because assistive technology interprets the latter two styles to mean the file input isn't interactive.

Next, we add an [event listener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
 to the input to listen for changes to its selected value (in this case, when files are selected). The event listener invokes our custom `updateImageDisplay()` function.

Whenever the `updateImageDisplay()` function is invoked, we:

*   Use a [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
     loop to empty the previous contents of the preview `<div>`.
    
*   Grab the [`FileList`](https://developer.mozilla.org/en-US/docs/Web/API/FileList)
     object that contains the information on all the selected files, and store it in a variable called `curFiles`.
    
*   Check to see if no files were selected, by checking if `curFiles.length` is equal to 0. If so, print a message into the preview `<div>` stating that no files have been selected.
    
*   If files _have_ been selected, we loop through each one, printing information about it into the preview `<div>`. Things to note here:
    
*   We use the custom `validFileType()` function to check whether the file is of the correct type (e.g., the image types specified in the `accept` attribute).
    
*   If it is, we:
    
    *   Print out its name and file size into a list item inside the previous `<div>` (obtained from `file.name` and `file.size`). The custom `returnFileSize()` function returns a nicely-formatted version of the size in bytes/KB/MB (by default the browser reports the size in absolute bytes).
    *   Generate a thumbnail preview of the image by calling [`URL.createObjectURL(file)`](https://developer.mozilla.org/en-US/docs/Web/API/URL/createObjectURL_static "URL.createObjectURL(file)")
        . Then, insert the image into the list item too by creating a new [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
         and setting its [`src`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#src)
         to the thumbnail.
*   If the file type is invalid, we display a message inside a list item telling the user that they need to select a different file type.
    

The custom `validFileType()` function takes a [`File`](https://developer.mozilla.org/en-US/docs/Web/API/File)
 object as a parameter, then uses [`Array.prototype.includes()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/includes)
 to check if any value in the `fileTypes` matches the file's `type` property. If a match is found, the function returns `true`. If no match is found, it returns `false`.

The `returnFileSize()` function takes a number (of bytes, taken from the current file's `size` property), and turns it into a nicely formatted size in bytes/KB/MB.

**Note:** The "KB" and "MB" units here use the [SI prefix](https://en.wikipedia.org/wiki/Binary_prefix "External link (opens in new tab)")
 convention of 1KB = 1000B, similar to macOS. Different systems represent file sizes differently—for example, Ubuntu uses IEC prefixes where 1KiB = 1024B, while RAM specifications often use SI prefixes to represent powers of two (1KB = 1024B). For this reason, we used `1e3` (`1000`) and `1e6` (`100000`) instead of `1024` and `1048576`. In your application, you should communicate the unit system clearly to your users if the exact size is important.

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#technical_summary)

-----------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| **[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#value)<br>** | A string representing the path to the selected file. |
| **Events** | [`change`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/change_event "change")<br>, [`input`](https://developer.mozilla.org/en-US/docs/Web/API/Element/input_event "input")<br> and [`cancel`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/cancel_event "cancel") |
| **Supported common attributes** | [`required`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#required) |
| **Additional Attributes** | [`accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#accept)<br>, [`capture`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#capture)<br>, [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#multiple) |
| **IDL attributes** | `files` and `value` |
| **DOM interface** | [`HTMLInputElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement) |
| **Implicit ARIA Role** | [no corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#specifications)

-----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# file-upload-state-(type=file)](https://html.spec.whatwg.org/multipage/input.html#file-upload-state-(type=file)) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file#see_also)

-----------------------------------------------------------------------------------------------------

*   [Using files from web applications](https://developer.mozilla.org/en-US/docs/Web/API/File_API/Using_files_from_web_applications)
     — contains a number of other useful examples related to `<input type="file">` and the [File API](https://developer.mozilla.org/en-US/docs/Web/API/File)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/input/file/index.md?plain=1 "Folder: en-us/web/html/reference/elements/input/file (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Ffile&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Ffile%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Finput%2Ffile%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Finput%2Ffile%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")