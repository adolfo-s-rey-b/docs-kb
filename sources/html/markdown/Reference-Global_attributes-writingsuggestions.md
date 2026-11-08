*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/writingsuggestions#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/writingsuggestions#mdn-search)
    

`writingsuggestions` HTML global attribute
==========================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/238)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/writingsuggestions#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`writingsuggestions`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is an [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 attribute indicating if browser-provided writing suggestions should be enabled under the scope of the element or not.

Some browsers provide writing suggestions to users as they type in editable fields. Suggestions usually appear as grayed-out text positioned after the text cursor, completing the user's sentence. While this can be helpful to users, developers might want to turn writing suggestions off in some cases, such as when providing site-specific writing suggestions.

The `writingsuggestions` attribute can be set on editable fields such as [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 elements, or on other HTML elements to control the behavior of the browser's suggestions on sections of a page, or on the entire page.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/writingsuggestions#syntax)

------------------------------------------------------------------------------------------------------------------

In browsers that support them, writing suggestions are enabled by default. To disable them, set the `writingsuggestions` attribute's value to `false`. Setting the attribute's value to `true`, or omitting the value, enables writing suggestions.

To disable writing suggestions:

To enable writing suggestions:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/writingsuggestions#specifications)

----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# writing-suggestions](https://html.spec.whatwg.org/multipage/interaction.html#writing-suggestions) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/writingsuggestions#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/writingsuggestions#see_also)

----------------------------------------------------------------------------------------------------------------------

*   [`autocomplete`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/autocomplete)
     attribute
*   [`spellcheck`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/spellcheck)
     attribute
*   [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
     attribute
*   [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    
*   [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    
*   [`<datalist>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/datalist)
     and [`list`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#list)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 27, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/writingsuggestions/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/writingsuggestions/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/writingsuggestions (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fwritingsuggestions&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fwritingsuggestions%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fwritingsuggestions%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fwritingsuggestions%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fd19dec85109590176f946fcceef48c787d578b1e%0A*+Document+last+modified%3A+2026-08-27T15%3A03%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")