*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Implementing_image_sprites#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Implementing_image_sprites#mdn-search)
    

Implementing image sprites in CSS
=================================

**Image sprites** are used in numerous web apps where multiple images are used. Rather than include each image as a separate image file, it is much more memory- and bandwidth-friendly to send them as a single image; using background position as a way to distinguish between individual images in the same image file, so the number of HTTP requests is reduced.

**Note:** When using HTTP/2, it may in fact be more bandwidth-friendly to use multiple small requests.

[Implementation](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Implementing_image_sprites#implementation)

---------------------------------------------------------------------------------------------------------------------------

Suppose an image is given to every item with class `tool-btn`:

A background position can be added either as two x, y values after the [`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)
 in the background, or as [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
. For example:

This would slide the starting point of the background image for the element with the ID `btn1` 20 pixels to the left and the element with the ID `btn2` 40 pixels to the left (assuming they have the class `tool-btn` assigned and are affected by the image rule above).

Similarly, you can also make hover states by targeting `#btn:hover`.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Implementing_image_sprites#see_also)

---------------------------------------------------------------------------------------------------------------

*   [Full working demo at CSS Tricks](https://css-tricks.com/snippets/css/perfect-css-sprite-sliding-doors-button/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Implementing_image_sprites/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/images/implementing_image_sprites/index.md?plain=1 "Folder: en-us/web/css/guides/images/implementing_image_sprites (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FImages%2FImplementing_image_sprites&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fimages%2Fimplementing_image_sprites%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FImages%2FImplementing_image_sprites%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fimages%2Fimplementing_image_sprites%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")