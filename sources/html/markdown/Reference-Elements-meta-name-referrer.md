*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#mdn-search)
    

`<meta name="referrer">` HTML attribute value
=============================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`referrer`** value for the [`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name)
 attribute of the [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 element controls the HTTP [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer)
 header of requests sent from the document. If specified, you define the referrer using a [`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)
 attribute in the `<meta>` element as a keyword value.

For example, the following `<meta>` element sends the [origin](https://developer.mozilla.org/en-US/docs/Glossary/Origin)
 of the document as the referrer:

**Warning:** Dynamically inserting `<meta name="referrer">` (with [`document.write()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/write "document.write()")
 or [`appendChild()`](https://developer.mozilla.org/en-US/docs/Web/API/Node/appendChild "appendChild()")
) makes the referrer behavior unpredictable. When several conflicting policies are defined, the `no-referrer` policy is applied.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#usage_notes)

-------------------------------------------------------------------------------------------------------------------

A `<meta name="referrer">` element has the following additional attributes:

[`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#content)

Sets the document referrer. You must define this attribute. Accepts one of the following values:

[`no-referrer`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#no-referrer)

Does not send an HTTP `Referer` header.

[`origin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#origin)

Sends the origin of the document.

[`no-referrer-when-downgrade`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#no-referrer-when-downgrade)

Sends the full URL when the destination is at least as secure as the current page (HTTP(S)→HTTPS), but sends no referrer when it's less secure (HTTPS→HTTP). This is the default behavior.

[`origin-when-cross-origin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#origin-when-cross-origin)

Sends the full URL (stripped of parameters) for same-origin requests, but only sends the origin for other cases.

[`same-origin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#same-origin)

Sends the full URL (stripped of parameters) for same-origin requests. Cross-origin requests will contain no referrer header.

[`strict-origin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#strict-origin)

Sends the origin when the destination is at least as secure as the current page (HTTP(S)→HTTPS), but sends no referrer when it's less secure (HTTPS→HTTP).

[`strict-origin-when-cross-origin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#strict-origin-when-cross-origin)

Sends the full URL (stripped of parameters) for same-origin requests. Sends the origin when the destination is at least as secure as the current page (HTTP(S)→HTTPS). Otherwise, sends no referrer.

[`unsafe-URL`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#unsafe-url)

Sends the full URL (stripped of parameters) for same-origin or cross-origin requests.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#examples)

-------------------------------------------------------------------------------------------------------------

### [Removing a referrer from requests](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#removing_a_referrer_from_requests)

The following `<meta>` element specifies that the document shouldn't send a `Referer` header with HTTP requests from the document:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# meta-referrer](https://html.spec.whatwg.org/multipage/semantics.html#meta-referrer) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer#see_also)

-------------------------------------------------------------------------------------------------------------

*   HTTP [`Referer`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer)
     header

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 22, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/meta/name/referrer/index.md?plain=1 "Folder: en-us/web/html/reference/elements/meta/name/referrer (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Freferrer&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Freferrer%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fname%2Freferrer%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fname%2Freferrer%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf5017c389132af39b50106cf1763fa7106e87b4%0A*+Document+last+modified%3A+2026-04-22T15%3A05%3A30.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")