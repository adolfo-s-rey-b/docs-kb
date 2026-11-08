*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/compression-dictionary#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/compression-dictionary#mdn-search)
    

`rel="compression-dictionary"` HTML attribute value
===================================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/258)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/compression-dictionary#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/compression-dictionary#browser_compatibility)
 carefully before using this in production.

The **`compression-dictionary`** keyword for the [`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#rel)
 attribute of the [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 element is a link that browsers can use to download a [compression dictionary](https://developer.mozilla.org/en-US/docs/Glossary/Compression_dictionary_transport)
 that can be used to compress future downloads for resources on this site so the download sizes of those resources are smaller than standard compression.

**Note:** if the website has a [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy)
 header, the `connect-src` directive (or `default-src`, if `connect-src` is not set) must permit the location of the dictionary resource to avoid the request being blocked.

See the [Compression Dictionary Transport guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Compression_dictionary_transport)
 for more information.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/compression-dictionary#specifications)

-----------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Compression Dictionary Transport  <br>\# the-compression-dictionary-link-relation-type](https://httpwg.org/specs/rfc9842.html#the-compression-dictionary-link-relation-type) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/compression-dictionary#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/compression-dictionary#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [Compression Dictionary Transport guide](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Compression_dictionary_transport)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/compression-dictionary/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/rel/compression-dictionary/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/rel/compression-dictionary (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Fcompression-dictionary&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Fcompression-dictionary%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Fcompression-dictionary%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Fcompression-dictionary%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf5017c389132af39b50106cf1763fa7106e87b4%0A*+Document+last+modified%3A+2026-04-22T15%3A05%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")