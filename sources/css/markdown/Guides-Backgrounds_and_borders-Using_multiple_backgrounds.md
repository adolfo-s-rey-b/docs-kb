*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds#mdn-search)
    

Using multiple backgrounds
==========================

You can apply **multiple backgrounds** to elements. These are layered atop one another with the first background you provide on top and the last background listed in the back. Only the last background can include a background color.

Multiple backgrounds are specified as a comma-separated list, such as `background: background1, background2, ...;`. This syntax is accepted by both the shorthand [`background`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background)
 property and the individual properties thereof except for [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
: [`background-attachment`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-attachment)
, [`background-clip`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-clip)
, [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
, [`background-origin`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-origin)
, [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
, [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
, [`background-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-size)
.

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds#example)

------------------------------------------------------------------------------------------------------------------------------

In this example, three backgrounds are stacked: the Firefox logo, an image of bubbles, and a [linear gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/gradient/linear-gradient)
:

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds#html)

html

    <div class="multi-bg-example"></div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds#css)

css

    .multi-bg-example {
      width: 100%;
      height: 400px;
      background-image:
        url("firefox.png"), url("bubbles.png"),
        linear-gradient(to right, rgb(30 75 115 / 100%), transparent);
      background-repeat: no-repeat, no-repeat, no-repeat;
      background-position:
        bottom right,
        left,
        right;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds#result)

As you can see here, the Firefox logo (listed first within [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
) is on top, directly above the bubbles graphic, followed by the gradient (listed last) sitting underneath all previous 'images'. Each subsequent sub-property ([`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
 and [`background-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-position)
) applies to the corresponding backgrounds. So the first listed value for [`background-repeat`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-repeat)
 applies to the first (frontmost) background, and so forth.

[Value repetition for multiple backgrounds](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds#value_repetition_for_multiple_backgrounds)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

When using multiple backgrounds, if a background-related property is given fewer comma-separated values than the number of background layers, the user agent repeats the list of values until there are enough values for all layers.

For example:

css

    .element {
      background-image: url("a.png"), url("b.png"), url("c.png");
      background-position: left top;
    }
    

This is equivalent to:

css

    .element {
      background-position:
        left top,
        left top,
        left top;
    }
    

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds#see_also)

--------------------------------------------------------------------------------------------------------------------------------

*   [CSS backgrounds and borders](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders)
     module
*   [Using CSS gradients](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Images/Using_gradients)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on May 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Backgrounds_and_borders/Using_multiple_backgrounds/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/backgrounds_and_borders/using_multiple_backgrounds/index.md?plain=1 "Folder: en-us/web/css/guides/backgrounds_and_borders/using_multiple_backgrounds (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBackgrounds_and_borders%2FUsing_multiple_backgrounds&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbackgrounds_and_borders%2Fusing_multiple_backgrounds%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBackgrounds_and_borders%2FUsing_multiple_backgrounds%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbackgrounds_and_borders%2Fusing_multiple_backgrounds%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc53bfa01f3bf436d486f4032c16f592855a2af2c%0A*+Document+last+modified%3A+2026-05-04T02%3A41%3A10.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")