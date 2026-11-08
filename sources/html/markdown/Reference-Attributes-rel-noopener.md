*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener#mdn-search)
    

`rel="noopener"` HTML attribute value
=====================================

The **`noopener`** keyword for the [`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel)
 attribute of the [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
, [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
, and [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 elements instructs the browser to navigate to the target resource without granting the new browsing context access to the document that opened it — by not setting the [`Window.opener`](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)
 property on the opened window (it returns `null`).

This is especially useful when opening untrusted links, in order to ensure they cannot tamper with the originating document via the [`Window.opener`](https://developer.mozilla.org/en-US/docs/Web/API/Window/opener)
 property (see [About rel=noopener](https://mathiasbynens.github.io/rel-noopener/ "External link (opens in new tab)")
 for more details), while still providing the `Referer` HTTP header (unless `noreferrer` is used as well).

Note that when `noopener` is used, nonempty target names other than `_top`, `_self`, and `_parent` are all treated like `_blank` in terms of deciding whether to open a new window/tab.

**Note:** Setting `target="_blank"` on `<a>`, `<area>` and `<form>` elements implicitly provides the same `rel` behavior as setting `rel="noopener"` which does not set `window.opener`.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# link-type-noopener](https://html.spec.whatwg.org/multipage/links.html#link-type-noopener) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

### [html.elements.a.rel.noopener](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener#html.elements.a.rel.noopener)

### [html.elements.area.rel.noopener](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener#html.elements.area.rel.noopener)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/noopener/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/rel/noopener/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/rel/noopener (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Fnoopener&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Fnoopener%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Fnoopener%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Fnoopener%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf5017c389132af39b50106cf1763fa7106e87b4%0A*+Document+last+modified%3A+2026-04-22T15%3A05%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")