*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#mdn-search)
    

`-moz-image-rect()` CSS function
================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`-moz-image-rect`** value for [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 lets you use a portion of a larger image as a background.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#syntax)

---------------------------------------------------------------------------------------------------

css

    -moz-image-rect(url("my-url"), top, right, bottom, left);
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#values)

[`<url>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)

The URI of the image from which to take the sub-image.

[`top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#top)

The top edge, specified as an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, of the sub-image within the specified image.

[`right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#right)

The right edge, specified as an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, of the sub-image within the specified image.

[`bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#bottom)

The bottom edge, specified as an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, of the sub-image within the specified image.

[`left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#left)

The left edge, specified as an [`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 or [`<percentage>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/percentage)
, of the sub-image within the specified image.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#description)

-------------------------------------------------------------------------------------------------------------

This property allows you to, for example, use different parts of one larger image as backgrounds in different parts of your content.

The syntax for the rectangle is similar to the [`rect()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape#syntax)
 function generating a [`<shape>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/shape)
 CSS type. All four values are relative to the upper left corner of the image.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#examples)

-------------------------------------------------------------------------------------------------------

This example loads an image and uses it in four segments to draw the Firefox logo in four [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 blocks. Clicking on their container causes the four segments to rotate around by swapping the [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 property values among the four [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 blocks.

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#css)

The CSS defines one container style, then the styles for the four boxes that comprise the complete image.

The container looks like this:

css

    #container {
      width: 267px;
      height: 272px;
      top: 100px;
      left: 100px;
      position: absolute;
      font-size: 16px;
      text-shadow: white 0px 0px 6px;
      text-align: center;
    }
    

Then the four boxes defining the segments of the image are defined. Let's look at them one at a time.

css

    #box1 {
      background-image: -moz-image-rect(url("firefox.png"), 0%, 50%, 50%, 0%);
      width: 133px;
      height: 136px;
      left: 0px;
      top: 0px;
      position: absolute;
    }
    

This is the top-left corner of the image. It defines a rectangle containing the top-left quarter of the image in the file `firefox.jpg`.

css

    #box2 {
      background-image: -moz-image-rect(url("firefox.png"), 0%, 100%, 50%, 50%);
      width: 133px;
      height: 136px;
      left: 133px;
      top: 0px;
      position: absolute;
    }
    

This defines the top-right corner of the image.

The other corners follow a similar pattern:

css

    #box3 {
      background-image: -moz-image-rect(url("firefox.png"), 50%, 50%, 100%, 0%);
      width: 133px;
      height: 136px;
      left: 0px;
      top: 136px;
      position: absolute;
    }
    #box4 {
      background-image: -moz-image-rect(url("firefox.png"), 50%, 100%, 100%, 50%);
      width: 133px;
      height: 136px;
      left: 133px;
      top: 136px;
      position: absolute;
    }
    

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#html)

We include a container with four boxes:

html

    <div id="container">
      <div id="box1">Top left</div>
      <div id="box2">Top right</div>
      <div id="box3">Bottom left</div>
      <div id="box4">Bottom right</div>
    </div>
    

This places the four segments of our image in a two-by-two box grid. These four segments are all contained within a larger [`<div>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/div)
 block whose primary purpose is to receive click events and dispatch them to our JavaScript code.

### [JavaScript](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#javascript)

This code handles the click event when the container receives a mouse click.

js

    function rotate() {
      let prevStyle = window
        .getComputedStyle(document.getElementById("box4"), null)
        .getPropertyValue("background-image");
    
      // Now that we've saved the last one, start rotating
      for (let i = 1; i <= 4; i++) {
        const curId = `box${i}`;
    
        // Shift the background images
        const curStyle = window
          .getComputedStyle(document.getElementById(curId), null)
          .getPropertyValue("background-image");
        document.getElementById(curId).style.backgroundImage = prevStyle;
        prevStyle = curStyle;
      }
    }
    
    document.getElementById("container").addEventListener("click", rotate);
    

This uses [`window.getComputedStyle()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle)
 to fetch the style of each element, shifting it to the following element. Notice that before it begins doing so it saves a copy of the last box's style since it will be overwritten by the third element's style. By copying the values of the [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 property from one element to the next with each mouse click, we achieve the desired effect.

### [What it looks like](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#what_it_looks_like)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#specifications)

-------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect#see_also)

-------------------------------------------------------------------------------------------------------

*   [Mozilla CSS extensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Mozilla_extensions)
    
*   [CSS Backgrounds and Borders module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/-moz-image-rect/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/values/-moz-image-rect/index.md?plain=1 "Folder: en-us/web/css/reference/values/-moz-image-rect (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2F-moz-image-rect&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fvalues%2F-moz-image-rect%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FValues%2F-moz-image-rect%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fvalues%2F-moz-image-rect%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")