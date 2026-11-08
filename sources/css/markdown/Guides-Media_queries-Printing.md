*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing#mdn-search)
    

Printing
========

There may be times in which your website or application would like to improve the user's experience when printing content. There are several possible scenarios:

*   You wish to adjust layout to take advantage of the size and shape of the paper.
*   You wish to use different styles to enhance the appearance of your content on paper.
*   You wish to use higher resolution images for a better result.
*   You want to adjust the user experience of printing, such as presenting a specially-formatted version of your content before printing begins.

There may be other cases in which you want to manage the printing process, but these are some of the most common scenarios. This article provides tips and techniques for helping your web content print better.

[Using a print style sheet](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing#using_a_print_style_sheet)

--------------------------------------------------------------------------------------------------------------------------------------

Add the following to your [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
 tag.

[Using media queries and @page to control printed content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing#using_media_queries_and_page_to_control_printed_content)

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can use the CSS [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
 at-rule to set different styles for your webpage when it is printed on paper or as a PDF versus when it is displayed on the screen. The `print` [media type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_types)
 sets the styles for printed media; these styles will only be used for printed content.

Add this at the end of your stylesheet. Note that [specificity](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Specificity)
 and precedence rules still apply:

You can also use the [`@page`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@page)
 at-rule to modify different aspects of printed pages including the page's dimensions, orientation, and margins. The `@page` at-rule can be used to target all pages in a print-out or just a specific subset of pages

[Detecting print requests](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing#detecting_print_requests)

------------------------------------------------------------------------------------------------------------------------------------

Browsers send [`beforeprint`](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeprint_event "beforeprint")
 and [`afterprint`](https://developer.mozilla.org/en-US/docs/Web/API/Window/afterprint_event "afterprint")
 events to determine when printing may have occurred. You can use this to adjust the user interface presented during printing (for example displaying or hiding user interface elements during the print process).

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing#examples)

----------------------------------------------------------------------------------------------------

Here are some common examples.

### [Automatically close the window when finished](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing#automatically_close_the_window_when_finished)

The following example will close the window after the user has printed its contents:

### [Print an external page without opening it](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing#print_an_external_page_without_opening_it)

If you want to be able to print an external page without opening it, you can utilize a hidden [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 (see: [HTMLIFrameElement](https://developer.mozilla.org/en-US/docs/Web/API/HTMLIFrameElement)
), automatically removing it after the user prints its contents. The following is a possible example which will print a file named `externalPage.html`:

#### HTML

#### JavaScript

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing#see_also)

----------------------------------------------------------------------------------------------------

*   [`window.print`](https://developer.mozilla.org/en-US/docs/Web/API/Window/print)
    
*   [`beforeprint`](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeprint_event "beforeprint")
     event
*   [`afterprint`](https://developer.mozilla.org/en-US/docs/Web/API/Window/afterprint_event "afterprint")
     event
*   [Media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
    
*   [CSS paged media](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Paged_media)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Printing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/media_queries/printing/index.md?plain=1 "Folder: en-us/web/css/guides/media_queries/printing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMedia_queries%2FPrinting&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmedia_queries%2Fprinting%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMedia_queries%2FPrinting%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmedia_queries%2Fprinting%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")