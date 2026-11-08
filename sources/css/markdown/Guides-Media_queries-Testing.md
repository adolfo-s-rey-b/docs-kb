*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing#mdn-search)
    

Testing media queries programmatically
======================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The [DOM](https://developer.mozilla.org/en-US/docs/Glossary/DOM)
 provides features that can test the results of a [media query](https://developer.mozilla.org/en-US/docs/Glossary/Media_query)
 programmatically, via the [`MediaQueryList`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList)
 interface and its methods and properties. Once you've created a `MediaQueryList` object, you can check the result of the [query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
 or receive notifications when the result changes.

[Creating a media query list](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing#creating_a_media_query_list)

-----------------------------------------------------------------------------------------------------------------------------------------

Before you can evaluate the results of a media query, you need to create the [`MediaQueryList`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList)
 object representing the query. To do this, use the [`window.matchMedia`](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia)
 method.

For example, to set up a query list that determines if the device is in landscape or portrait [orientation](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/orientation)
:

[Checking the result of a query](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing#checking_the_result_of_a_query)

-----------------------------------------------------------------------------------------------------------------------------------------------

Once you've created your media query list, you can check the result of the query by looking at the value of its [`matches`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList/matches)
 property:

[Receiving query notifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing#receiving_query_notifications)

---------------------------------------------------------------------------------------------------------------------------------------------

If you need to be aware of changes to the evaluated result of the query on an ongoing basis, it's more efficient to register a [listener](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener)
 than to poll the query's result. To do this, call the [`addEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/addEventListener "addEventListener()")
 method on the [`MediaQueryList`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList)
 object, with a callback function to invoke when the media query status changes (e.g., the media query test goes from `true` to `false`):

This code creates the orientation-testing media query list and adds an event listener to it. After defining the listener, we also call the listener directly. This makes our listener perform adjustments based on the current device orientation; otherwise, our code might assume the device is in portrait mode at startup, even if it's actually in landscape mode.

The `handleOrientationChange()` function would look at the result of the query and handle whatever we need to do on an orientation change:

Above, we define the parameter as `evt` — an event object of type [`MediaQueryListEvent`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryListEvent)
 that also includes the [`media`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryListEvent/media "media")
 and [`matches`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryListEvent/matches "matches")
 properties, so you can query these features of the `MediaQueryList` by directly accessing it, or accessing the event object.

[Ending query notifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing#ending_query_notifications)

---------------------------------------------------------------------------------------------------------------------------------------

To stop receiving notifications about changes to the value of your media query, call [`removeEventListener()`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget/removeEventListener "removeEventListener()")
 on the `MediaQueryList`, passing it the name of the previously-defined callback function:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSSOM View Module  <br>\# mediaquerylist](https://drafts.csswg.org/cssom-view/#mediaquerylist) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing#see_also)

---------------------------------------------------------------------------------------------------

*   [Media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [CSS media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries)
     module
*   [CSS object model](https://developer.mozilla.org/en-US/docs/Web/API/CSS_Object_Model)
     module
*   [`window.matchMedia()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia)
    
*   [`MediaQueryList`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryList)
    
*   [`MediaQueryListEvent`](https://developer.mozilla.org/en-US/docs/Web/API/MediaQueryListEvent)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Testing/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/media_queries/testing/index.md?plain=1 "Folder: en-us/web/css/guides/media_queries/testing (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMedia_queries%2FTesting&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fmedia_queries%2Ftesting%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FMedia_queries%2FTesting%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fmedia_queries%2Ftesting%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")