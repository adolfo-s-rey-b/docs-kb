*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#mdn-search)
    

`<body>` HTML document body element
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<body>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents the content of an HTML document. There can be only one `<body>` element in a document.

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#attributes)

---------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
, event attributes, and deprecated attributes:

### [Event attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#event_attributes)

**Note:** Each of the below event attribute names is linked to its equivalent [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
 interface event. You can listen to these events using [`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
 instead of adding the `oneventname` attribute to the `<body>` element.

[`onafterprint`](https://developer.mozilla.org/en-US/docs/Web/API/Window/afterprint_event)

Function to call after the user has printed the document.

[`onbeforeprint`](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeprint_event)

Function to call when the user requests printing of the document.

[`onbeforeunload`](https://developer.mozilla.org/en-US/docs/Web/API/Window/beforeunload_event)

Function to call when the document is about to be unloaded.

[`onblur`](https://developer.mozilla.org/en-US/docs/Web/API/Window/blur_event)

Function to call when the document loses focus.

[`onerror`](https://developer.mozilla.org/en-US/docs/Web/API/Window/error_event)

Function to call when the document fails to load properly.

[`onfocus`](https://developer.mozilla.org/en-US/docs/Web/API/Window/focus_event)

Function to call when the document receives focus.

[`onhashchange`](https://developer.mozilla.org/en-US/docs/Web/API/Window/hashchange_event)

Function to call when the fragment identifier part (starting with the hash (`'#'`) character) of the document's current address has changed.

[`onlanguagechange`](https://developer.mozilla.org/en-US/docs/Web/API/Window/languagechange_event)

Function to call when the preferred languages changed.

[`onload`](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event)

Function to call when the document has finished loading.

[`onmessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/message_event)

Function to call when the document has received a message.

[`onmessageerror`](https://developer.mozilla.org/en-US/docs/Web/API/Window/messageerror_event)

Function to call when the document has received a message that cannot be deserialized.

[`onoffline`](https://developer.mozilla.org/en-US/docs/Web/API/Window/offline_event)

Function to call when network communication has failed.

[`ononline`](https://developer.mozilla.org/en-US/docs/Web/API/Window/online_event)

Function to call when network communication has been restored.

[`onpageswap`](https://developer.mozilla.org/en-US/docs/Web/API/Window/pageswap_event)

Function to call when you navigate across documents, when the previous document is about to unload.

[`onpagehide`](https://developer.mozilla.org/en-US/docs/Web/API/Window/pagehide_event)

Function to call when the browser hides the current page in the process of presenting a different page from the session's history.

[`onpagereveal`](https://developer.mozilla.org/en-US/docs/Web/API/Window/pagereveal_event)

Function to call when a document is first rendered, either when loading a fresh document from the network or activating a document.

[`onpageshow`](https://developer.mozilla.org/en-US/docs/Web/API/Window/pageshow_event)

Function to call when the browser displays the window's document due to navigation.

[`onpopstate`](https://developer.mozilla.org/en-US/docs/Web/API/Window/popstate_event)

Function to call when the user has navigated session history.

[`onresize`](https://developer.mozilla.org/en-US/docs/Web/API/Window/resize_event)

Function to call when the document has been resized.

[`onrejectionhandled`](https://developer.mozilla.org/en-US/docs/Web/API/Window/rejectionhandled_event)

Function to call when a JavaScript [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 is handled late.

[`onstorage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/storage_event)

Function to call when the storage area has changed.

[`onunhandledrejection`](https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event)

Function to call when a JavaScript [`Promise`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise)
 that has no rejection handler is rejected.

[`onunload`](https://developer.mozilla.org/en-US/docs/Web/API/Window/unload_event)

Function to call when the document is going away.

### [Deprecated attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#deprecated_attributes)

**Warning:** Do not use these deprecated attributes; opt for the CSS alternatives listed with each deprecated attribute instead.

[`alink`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#alink)

Color of text for hyperlinks when selected. Use the CSS [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property in conjunction with the [`:active`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:active)
 and [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
 pseudo-classes instead.

[`background`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#background)

URI of an image to use as a background. Use the CSS [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
 property instead.

[`bgcolor`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#bgcolor)

Background color for the document. Use the CSS [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
 property instead.

[`bottommargin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#bottommargin)

Ignored.

[`leftmargin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#leftmargin)

The margin of the left and right of the body. Use the CSS [`margin-left`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-left)
 and [`margin-right`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-right)
 properties (or the logical [`margin-inline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-inline)
 property) instead.

[`link`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#link)

Color of text for unvisited hypertext links. Use the CSS [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property in conjunction with the [`:link`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:link)
 pseudo-class instead.

[`rightmargin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#rightmargin)

Ignored.

[`text`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#text)

Foreground color of text. Use the CSS [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property instead.

[`topmargin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#topmargin)

The margin of the top and bottom of the body. Use the CSS [`margin-top`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-top)
 and [`margin-bottom`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-bottom)
 properties (or the logical [`margin-block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin-block)
 property) instead.

[`vlink`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#vlink)

Color of text for visited hypertext links. Use the CSS [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property in conjunction with the [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
 pseudo-class instead.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#examples)

-----------------------------------------------------------------------------------------------

html

    <html lang="en">
      <head>
        <title>Document title</title>
      </head>
      <body>
        <p>
          The <code>&lt;body&gt;</code> HTML element represents the content of an
          HTML document. There can be only one <code>&lt;body&gt;</code> element in
          a document.
        </p>
      </body>
    </html>
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#result)

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#technical_summary)

-----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | None. |
| Permitted content | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>. |
| Tag omission | The start tag may be omitted if the element is empty, or if the first thing inside it is not ASCII whitespace or a comment, except if the first thing inside it is a [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)<br>, [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript)<br>, [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)<br>, [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)<br>, [`<style>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/style)<br>, or [`<template>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/template)<br> element. The end tag may be omitted if the `<body>` element is not immediately followed by a comment. |
| Permitted parents | It must be the second element of an [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)<br> element. |
| Implicit ARIA role | `[generic](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/generic_role) ` |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLBodyElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLBodyElement)<br><br>*   The `<body>` element exposes the [`HTMLBodyElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLBodyElement)<br>     interface.<br>*   You can access the `<body>` element through the [`document.body`](https://developer.mozilla.org/en-US/docs/Web/API/Document/body)<br>     property. |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-body-element](https://html.spec.whatwg.org/multipage/sections.html#the-body-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body#see_also)

-----------------------------------------------------------------------------------------------

*   [`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html)
    
*   [`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head)
    
*   [Event handling overview](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Events#registering_event_handlers)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 7, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/body/index.md?plain=1 "Folder: en-us/web/html/reference/elements/body (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbody&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbody%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fbody%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fbody%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff44f946c49273a558b97e342e22a100780d224c8%0A*+Document+last+modified%3A+2026-10-07T07%3A17%3A34.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")