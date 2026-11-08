*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture#mdn-search)
    

`capture` HTML attribute
========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/27)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`capture`** attribute specifies that, optionally, a new file should be captured, and which device should be used to capture that new media of a type defined by the [`accept`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept)
 attribute.

Values include `user` and `environment`. The capture attribute is supported on the [file](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input/file)
 input type.

The `capture` attribute takes as its value a string that specifies which camera to use for capture of image or video data, if the [accept](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/accept)
 attribute indicates that the input should be of one of those types.

| Value | Description |
| --- | --- |
| `user` | The user-facing camera and/or microphone should be used. |
| `environment` | The outward-facing camera and/or microphone should be used |

**Note:** Capture was previously a Boolean attribute which, if present, requested that the device's media capture device(s) such as camera or microphone be used instead of requesting a file input.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture#try_it)

------------------------------------------------------------------------------------------------

    <label for="selfie">Take a picture of your face:</label>
    
    <input type="file" id="selfie" name="selfie" accept="image/*" capture="user" />
    
    <label for="picture">Take a picture using back facing camera:</label>
    
    <input
      type="file"
      id="picture"
      name="picture"
      accept="image/*"
      capture="environment" />
    

    label {
      display: block;
      margin-top: 1rem;
    }
    
    input {
      margin-bottom: 1rem;
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture#examples)

----------------------------------------------------------------------------------------------------

When set on a file input type, operating systems with microphones and cameras will display a user interface allowing the selection from an existing file or the creating of a new one.

html

    <p>
      <label for="soundFile">What does your voice sound like?:</label>
      <input type="file" id="soundFile" capture="user" accept="audio/*" />
    </p>
    <p>
      <label for="videoFile">Upload a video:</label>
      <input type="file" id="videoFile" capture="environment" accept="video/*" />
    </p>
    <p>
      <label for="imageFile">Upload a photo of yourself:</label>
      <input type="file" id="imageFile" capture="user" accept="image/*" />
    </p>
    

Note these work better on mobile devices; if your device is a desktop computer, you'll likely get a typical file picker.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML Media Capture  <br>\# dfn-capture](https://w3c.github.io/html-media-capture/#dfn-capture) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture#see_also)

----------------------------------------------------------------------------------------------------

*   [Using files from web applications](https://developer.mozilla.org/en-US/docs/Web/API/File_API/Using_files_from_web_applications)
    
*   [File API](https://developer.mozilla.org/en-US/docs/Web/API/File)
    
*   [`HTMLInputElement.files`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLInputElement/files)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/capture/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/capture/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/capture (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fcapture&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fcapture%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fcapture%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fcapture%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb50ed7ac1c2ca21b4b5cfb594474a17da3f2e6c2%0A*+Document+last+modified%3A+2026-04-20T12%3A09%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")