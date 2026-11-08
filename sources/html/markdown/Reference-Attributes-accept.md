*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#mdn-search)
    

`accept` HTML attribute
=======================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`accept`** attribute takes as its value a comma-separated list of one or more file types, or [unique file type specifiers](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#unique_file_type_specifiers)
, describing which file types to allow.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#try_it)

-----------------------------------------------------------------------------------------------

    <label for="movie">Choose a movie to upload:</label>
    
    <input type="file" id="movie" name="movie" accept="video/*" />
    
    <label for="poster">Choose a poster:</label>
    
    <input type="file" id="poster" name="poster" accept="image/png, image/jpeg" />
    

    label {
      display: block;
      margin-top: 1rem;
    }
    
    input {
      margin-bottom: 1rem;
    }
    

[Overview](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#overview)

---------------------------------------------------------------------------------------------------

The accept property is an attribute of the [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
 [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 type. It was supported on the [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 element, but was removed in favor of [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
.

Because a given file type may be identified in more than one manner, it's useful to provide a thorough set of type specifiers when you need files of specific type, or use the wild card to denote a type of any format is acceptable.

For instance, there are a number of ways Microsoft Word files can be identified, so a site that accepts Word files might use an `<input>` like this:

html

    <input
      type="file"
      id="docpicker"
      accept=".doc,.docx,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document" />
    

Whereas if you're accepting a media file, you may want to include any format of that media type:

html

    <input type="file" id="soundFile" accept="audio/*" />
    <input type="file" id="videoFile" accept="video/*" />
    <input type="file" id="imageFile" accept="image/*" />
    

The `accept` attribute doesn't validate the types of the selected files; it provides hints for browsers to guide users towards selecting the correct file types. It is still possible (in most cases) for users to toggle an option in the file chooser that makes it possible to override this and select any file they wish, and then choose incorrect file types.

Because of this, you should make sure that expected requirement is validated server-side.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#examples)

---------------------------------------------------------------------------------------------------

When set on a file input type, the native file picker that opens up should only enable selecting files of the correct file type. Most operating systems lighten the files that don't match the criteria and aren't selectable.

html

    <p>
      <label for="soundFile">Select an audio file:</label>
      <input type="file" id="soundFile" accept="audio/*" />
    </p>
    <p>
      <label for="videoFile">Select a video file:</label>
      <input type="file" id="videoFile" accept="video/*" />
    </p>
    <p>
      <label for="imageFile">Select some images:</label>
      <input type="file" id="imageFile" accept="image/*" multiple />
    </p>
    

Note the last example allows you to select multiple images. See the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#multiple)
 attribute for more information.

[Unique file type specifiers](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#unique_file_type_specifiers)

-----------------------------------------------------------------------------------------------------------------------------------------

A **unique file type specifier** is a string that describes a type of file that may be selected by the user in an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element of type `file`. Each unique file type specifier may take one of the following forms:

*   A valid case-insensitive filename extension, starting with a period (".") character. For example: `.jpg`, `.pdf`, or `.doc`.
*   A valid MIME type string, with no extensions.
*   The string `audio/*` meaning "any audio file".
*   The string `video/*` meaning "any video file".
*   The string `image/*` meaning "any image file".

The `accept` attribute takes as its value a string containing one or more of these unique file type specifiers, separated by commas. For example, a file picker that needs content that can be presented as an image, including both standard image formats and PDF files, might look like this:

html

    <input type="file" accept="image/*,.pdf" />
    

[Using file inputs](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#using_file_inputs)

---------------------------------------------------------------------------------------------------------------------

### [A basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#a_basic_example)

html

    <div>
      <label for="file">Choose file to upload</label>
      <input type="file" id="file" name="file" multiple />
    </div>
    

    div {
      margin-bottom: 10px;
    }
    

This produces the following output:

Regardless of the user's device or operating system, the file input provides a button that opens up a file picker dialog that allows the user to choose a file.

Including the [`multiple`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#multiple)
 attribute, as shown above, specifies that multiple files can be chosen at once. The user can choose multiple files from the file picker in any way that their chosen platform allows (e.g., by holding down Shift or Control, and then clicking). If you only want the user to choose a single file per `<input>`, omit the `multiple` attribute.

### [Limiting accepted file types](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#limiting_accepted_file_types)

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

html

    <div>
      <label for="profile_pic">Choose file to upload</label>
      <input
        type="file"
        id="profile_pic"
        name="profile_pic"
        accept=".jpg, .jpeg, .png" />
    </div>
    

    div {
      margin-bottom: 10px;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-input-accept](https://html.spec.whatwg.org/multipage/input.html#attr-input-accept) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept#see_also)

---------------------------------------------------------------------------------------------------

*   [Using files from web applications](https://developer.mozilla.org/en-US/docs/Web/API/File_API/Using_files_from_web_applications)
    
*   [File API](https://developer.mozilla.org/en-US/docs/Web/API/File)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 14, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/accept/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/accept (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Faccept&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Faccept%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Faccept%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Faccept%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F46afd57950146568819d0bf98175a2ffdbe079d7%0A*+Document+last+modified%3A+2026-10-14T12%3A01%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")