*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Media_objects#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Media_objects#mdn-search)
    

Media objects
=============

The _Media Object_ is a pattern we see all over the web. It refers to a two-column box with an image on one side and descriptive text on the other, e.g., a social media post.

![Example of a media object with profile image on the left side and lorem ipsum text to the right filling up 80% of the space](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Media_objects/media-object.png)

[Requirements](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Media_objects#requirements)

-------------------------------------------------------------------------------------------------------------------

Media Object pattern needs some or all of the following characteristics:

*   Stacked on Mobile, two columns on Desktop.
*   The image can be on the left or right.
*   The image might be small or large.
*   Media Objects can be nested.
*   The Media Object should clear the contents no matter which side is tallest.

[The recipe](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Media_objects#the_recipe)

---------------------------------------------------------------------------------------------------------------

Click "Play" in the code blocks below to edit the example in the MDN Playground:

[Choices made](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Media_objects#choices_made)

-------------------------------------------------------------------------------------------------------------------

I have chosen to use [grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 for the media object as it allows me to control the layout in two dimensions when I need to. This means that when we have a footer, with short content above, the footer can be pushed down to the bottom of the media object.

Another reason to use grid layout is in order that I can use [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
 for the track sizing of the image. By using `fit-content` with a maximum size of 200 pixels, when we have a small image such as the icon, the track only gets as large as the size of that image — the `max-content` size. If the image is larger, the track stops growing at 200 pixels and as the image has a [`max-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/max-width)
 of 100% applied, it scales down so that it continues to fit inside the column.

By using [`grid-template-areas`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/grid-template-areas)
 to achieve the layout, I can see the pattern in the CSS. I define my grid once the viewport is 500 pixels wide, so on smaller devices the media object stacks.

An option for the pattern is to flip it to switch the image to the other side — this is done by adding the `media-flip` class, which defines a flipped grid template causing the layout to be mirrored.

When we nest one media object inside another we need to place it into the second track in the regular layout, and the first track when flipped.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Media_objects#see_also)

-----------------------------------------------------------------------------------------------------------

*   [`fit-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/fit-content)
     property
*   [Using grid template areas](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Grid_template_areas)
    
*   [CSS grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Media_objects/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/how_to/layout_cookbook/media_objects/index.md?plain=1 "Folder: en-us/web/css/how_to/layout_cookbook/media_objects (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FMedia_objects&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fmedia_objects%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FMedia_objects%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fmedia_objects%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")