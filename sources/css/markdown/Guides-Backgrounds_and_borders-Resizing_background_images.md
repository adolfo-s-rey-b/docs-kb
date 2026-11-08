*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#mdn-search)
    

Resizing background images with background-size
===============================================

The **[`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property lets you resize the background image of an element, overriding the default behavior of tiling the image at its full size by specifying the width and/or height of the image. By doing so, you can scale the image upward or downward as desired.

[Tiling a large image](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#tiling_a_large_image)

--------------------------------------------------------------------------------------------------------------------------------------------------------

Let's consider a large image, a 2982x2808 Firefox logo image. We want (for some reason likely involving horrifyingly bad site design) to tile four copies of this image into a 300x300-pixel element. To do this, we can use a fixed `background-size` value of 150 pixels.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#html)

html

    <div class="tiledBackground"></div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#css)

css

    .tiledBackground {
      background-image: url("https://www.mozilla.org/media/img/logos/firefox/logo-quantum.9c5e96634f92.png");
      background-size: 150px;
      width: 300px;
      height: 300px;
      border: 2px solid;
      color: pink;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#result)

[Stretching an image](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#stretching_an_image)

------------------------------------------------------------------------------------------------------------------------------------------------------

You can also specify both the horizontal and vertical sizes of the image, like this:

css

    background-size: 300px 150px;
    

The result looks like this:

![Firefox logo stretched](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images/stretched_firefox_logo.png)

[Scaling an image up](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#scaling_an_image_up)

------------------------------------------------------------------------------------------------------------------------------------------------------

On the other end of the spectrum, you can scale an image up in the background. Here we scale a 32x32 pixel favicon to 300x300 pixels:

![MDN Logo scaled](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images/scaled_mdn_logo.png)

css

    .square2 {
      background-image: url("favicon.png");
      background-size: 300px;
      width: 300px;
      height: 300px;
      border: 2px solid;
      text-shadow: white 0px 0px 2px;
      font-size: 16px;
    }
    

As you can see, the CSS is actually essentially identical, save the name of the image file.

[Special values: `contain` and `cover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#special_values_contain_and_cover)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

In addition to [`<length>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/length)
 values, the [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
 CSS property offers two special size values, `contain` and `cover`. Let's take a look at these.

### [`contain`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#contain)

The `contain` value specifies that, regardless of the size of the containing box, the background image should be scaled so that each side is as large as possible while not exceeding the length of the corresponding side of the container. Try resizing the example below to see this in action.

#### HTML

html

    <div class="bgSizeContain">
      <p>Try resizing this element!</p>
    </div>
    

#### CSS

css

    .bgSizeContain {
      background-image: url("https://www.mozilla.org/media/img/logos/firefox/logo-quantum.9c5e96634f92.png");
      background-size: contain;
      width: 160px;
      height: 160px;
      border: 2px solid;
      resize: both;
      overflow: scroll;
    }
    

#### Result

### [`cover`](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#cover)

The `cover` value specifies that the background image should be sized so that it is as small as possible while ensuring that both dimensions are greater than or equal to the corresponding size of the container. Try resizing the example below to see this in action.

#### HTML

html

    <div class="bgSizeCover">
      <p>Try resizing this element!</p>
    </div>
    

#### CSS

css

    .bgSizeCover {
      background-image: url("https://www.mozilla.org/media/img/logos/firefox/logo-quantum.9c5e96634f92.png");
      background-size: cover;
      width: 160px;
      height: 160px;
      border: 2px solid;
      resize: both;
      overflow: scroll;
    }
    

#### Result

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images#see_also)

--------------------------------------------------------------------------------------------------------------------------------

*   [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
    
*   [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
    
*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module
*   [Scaling SVG backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Scaling_SVG_backgrounds)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 20, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Resizing_background_images/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/backgrounds_and_borders/resizing_background_images/index.md?plain=1 "Folder: en-us/web/css/guides/backgrounds_and_borders/resizing_background_images (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBackgrounds_and_borders%2FResizing_background_images&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbackgrounds_and_borders%2Fresizing_background_images%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBackgrounds_and_borders%2FResizing_background_images%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbackgrounds_and_borders%2Fresizing_background_images%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca5d9f9e63b460fc0c9e15ac57d9739e10e4ea0d%0A*+Document+last+modified%3A+2025-11-20T07%3A05%3A04.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")