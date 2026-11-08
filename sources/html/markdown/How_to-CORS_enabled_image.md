*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image#mdn-search)
    

Use cross-origin images in a canvas
===================================

HTML provides a [`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#crossorigin)
 attribute for images that, in combination with an appropriate [CORS](https://developer.mozilla.org/en-US/docs/Glossary/CORS)
 header, allows images defined by the [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 element that are loaded from foreign origins to be used in a [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 as if they had been loaded from the current origin.

See [CORS settings attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)
 for details on how the `crossorigin` attribute is used.

[Security and tainted canvases](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image#security_and_tainted_canvases)

-------------------------------------------------------------------------------------------------------------------------------------------

Because the pixels in a canvas's bitmap can come from a variety of sources, including images or videos retrieved from other hosts, it's inevitable that security problems may arise.

As soon as you draw into a canvas any data that was loaded from another origin without CORS approval, the canvas becomes **tainted**. A tainted canvas is one which is no longer considered secure, and any attempts to retrieve image data back from the canvas will cause an exception to be thrown.

If the source of the foreign content is an HTML [`<img>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img)
 or SVG [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
 element, attempting to retrieve the contents of the canvas isn't allowed.

If the foreign content comes from an image obtained from either as [`HTMLCanvasElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement)
 or [`ImageBitMap`](https://developer.mozilla.org/en-US/docs/Web/API/ImageBitmap)
, and the image source doesn't meet the same origin rules, attempts to read the canvas's contents are blocked.

Calling any of the following on a tainted canvas will result in an error:

*   Calling [`getImageData()`](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/getImageData "getImageData()")
     on the canvas's context
*   Calling [`toBlob()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toBlob "toBlob()")
    , [`toDataURL()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL "toDataURL()")
     or [`captureStream()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/captureStream "captureStream()")
     on the [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
     element itself

Attempting any of these when the canvas is tainted will cause a `SecurityError` to be thrown. This protects users from having private data exposed by using images to pull information from remote websites without permission.

[Storing an image from a foreign origin](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image#storing_an_image_from_a_foreign_origin)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

In this example, we wish to permit images from a foreign origin to be retrieved and saved to local storage. Implementing this requires configuring the server as well as writing code for the website itself.

### [Web server configuration](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image#web_server_configuration)

The first thing we need is a server that's configured to host images with the [`Access-Control-Allow-Origin`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin)
 header configured to permit cross-origin access to image files.

Let's assume we're serving our site using [Apache](https://httpd.apache.org/ "External link (opens in new tab)")
. Consider the HTML5 Boilerplate [Apache server configuration file for CORS images](https://github.com/h5bp/server-configs-apache/blob/main/h5bp/cross-origin/images.conf "External link (opens in new tab)")
, shown below:

In short, this configures the server to allow graphic files (those with the extensions ".bmp", ".cur", ".gif", ".ico", ".jpg", ".jpeg", ".png", ".svg", ".svgz", and ".webp") to be accessed cross-origin from anywhere on the internet.

### [Implementing the save feature](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image#implementing_the_save_feature)

Now that the server has been configured to allow retrieval of the images cross-origin, we can write the code that allows the user to save them to [local storage](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)
, just as if they were being served from the same domain the code is running on.

The key is to use the [`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#crossorigin)
 attribute by setting [`crossOrigin`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/crossOrigin "crossOrigin")
 on the [`HTMLImageElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement)
 into which the image will be loaded. This tells the browser to request cross-origin access when downloading the image data.

#### Starting the download

The code that starts the download (say, when the user clicks a "Download" button), looks like this:

We're using a hard-coded URL (`imageURL`) and associated descriptive text (`imageDescription`) here, but that could easily come from anywhere. To begin downloading the image, we create a new [`HTMLImageElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement)
 object by using the [`Image()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/Image "Image()")
 constructor. The image is then configured to allow cross-origin downloading by setting its `crossOrigin` attribute to `"anonymous"` (that is, allow non-authenticated downloading of the image cross-origin). An event listener is added for the [`load`](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event "load")
 event being fired on the image element, which means the image data has been received. Alternative text is added to the image; while `<canvas>` does not support the `alt` attribute, the value can be used to set an `aria-label` or the canvas's inner content.

Finally, the image's [`src`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/src "src")
 attribute is set to the URL of the image to download; this triggers the download to begin.

#### Receiving and saving the image

The code that handles the newly-downloaded image is found in the `imageReceived()` method:

`imageReceived()` is called to handle the `"load"` event on the `HTMLImageElement` that receives the downloaded image. This event is triggered once the downloaded data is all available. It begins by creating a new [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
 element that we'll use to convert the image into a data URL, and by getting access to the canvas's 2D drawing context ([`CanvasRenderingContext2D`](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D)
) in the variable `context`.

The canvas's size is adjusted to match the received image, the inner text is set to the image description, then the image is drawn into the canvas using [`drawImage()`](https://developer.mozilla.org/en-US/docs/Web/API/CanvasRenderingContext2D/drawImage "drawImage()")
. The canvas is then inserted into the document so the image is visible.

Now it's time to actually save the image locally. To do this, we use the Web Storage API's local storage mechanism, which is accessed through the [`localStorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage "localStorage")
 global. The canvas method [`toDataURL()`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLCanvasElement/toDataURL "toDataURL()")
 is used to convert the image into a data:// URL representing a PNG image, which is then saved into local storage using [`setItem()`](https://developer.mozilla.org/en-US/docs/Web/API/Storage/setItem "setItem()")
.

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image#see_also)

-------------------------------------------------------------------------------------------------

*   [Using Cross-domain images in WebGL and Chrome 13](https://blog.chromium.org/2011/07/using-cross-domain-images-in-webgl-and.html "External link (opens in new tab)")
    
*   [HTML Specification - the `crossorigin` attribute](https://html.spec.whatwg.org/multipage/embedded-content.html#attr-img-crossorigin "External link (opens in new tab)")
    
*   [Web Storage API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Storage_API)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 18, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/CORS_enabled_image/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/how_to/cors_enabled_image/index.md?plain=1 "Folder: en-us/web/html/how_to/cors_enabled_image (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FHow_to%2FCORS_enabled_image&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fhow_to%2Fcors_enabled_image%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FHow_to%2FCORS_enabled_image%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fhow_to%2Fcors_enabled_image%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6036cd414b2214f85901158bdf3e3a96123d4553%0A*+Document+last+modified%3A+2025-09-18T15%3A38%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")