*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Using_:target#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Using_:target#mdn-search)
    

Using the :target pseudo-class in selectors
===========================================

When a URL points at a specific piece of a document using a [URL fragment identifier](https://developer.mozilla.org/en-US/docs/Web/URI/Reference/Fragment#fragment)
, it can be difficult for the user to notice. This guide discusses using CSS to draw attention to the target of a URL to improve user experience.

[Picking a Target](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Using_:target#picking_a_target)

---------------------------------------------------------------------------------------------------------------------

The [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 [`:target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target)
 is used to style the target element of the document identified using the URL fragment identifier. For example, the URL `https://developer.mozilla.org/en-US/docs/Web/CSS#reference` contains the fragment identifier `#reference`. In HTML, identifiers are found as the values of either `id` or `name` attributes, since the two share the same namespace. Thus, the example URL would point to the element that has the id `reference` in that document.

To style any `h2` element that is the target of a URL, while not affecting any other kind of element to get a target style, use the `:target` pseudo-class with the [type selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors)
:

It's also possible to create styles that are specific to a particular fragment of the document. This is done using the same identifying value that is found in the URI. Thus, to add a background color to the `#reference` fragment, we would write:

[Targeting all elements](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Using_:target#targeting_all_elements)

---------------------------------------------------------------------------------------------------------------------------------

If the intent is to create a "blanket" style that will apply to all targeted elements, then the universal selector comes in handy:

[Example](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Using_:target#example)

---------------------------------------------------------------------------------------------------

In the following example, there are five links that point to elements in the same document. Selecting the "First" link, for example, will cause `<h1 id="one">` to become the target element. Note that the document may jump to a new scroll position, since target elements are placed on the top of the browser window if possible.

[Conclusion](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Using_:target#conclusion)

---------------------------------------------------------------------------------------------------------

In cases where a fragment identifier points to a portion of the document, readers may become confused about which part of the document they're supposed to be reading. By styling the target of a URI, reader confusion can be reduced or eliminated.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Using_:target#see_also)

-----------------------------------------------------------------------------------------------------

*   [`:target`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:target)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Using_:target/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/selectors/using__colon_target/index.md?plain=1 "Folder: en-us/web/css/guides/selectors/using__colon_target (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSelectors%2FUsing_%3Atarget&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fselectors%2Fusing__colon_target%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSelectors%2FUsing_%3Atarget%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fselectors%2Fusing__colon_target%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F298079b550c76f20de6611c4ecdde4c30dc68b2b%0A*+Document+last+modified%3A+2026-09-22T10%3A09%3A51.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")