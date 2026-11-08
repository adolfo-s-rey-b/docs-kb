*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Malformed_URI#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Malformed_URI#mdn-search)
    

URIError: malformed URI sequence
================================

The JavaScript exception "malformed URI sequence" occurs when URI encoding or decoding wasn't successful.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Malformed_URI#message)

----------------------------------------------------------------------------------------------------------

URIError: URI malformed (V8-based)
URIError: malformed URI sequence (Firefox)
URIError: String contained an illegal UTF-16 sequence. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Malformed_URI#error_type)

----------------------------------------------------------------------------------------------------------------

[`URIError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Malformed_URI#what_went_wrong)

---------------------------------------------------------------------------------------------------------------------------

URI encoding or decoding wasn't successful. An argument given to either the [`decodeURI`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)
, [`encodeURI`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
, [`encodeURIComponent`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)
, or [`decodeURIComponent`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent)
 function was not valid, so that the function was unable encode or decode properly.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Malformed_URI#examples)

------------------------------------------------------------------------------------------------------------

### [Encoding](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Malformed_URI#encoding)

Encoding replaces each instance of certain characters by one, two, three, or four escape sequences representing the UTF-8 encoding of the character. An [`URIError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)
 will be thrown if there is an attempt to encode a surrogate which is not part of a high-low pair, for example:

A high-low pair is OK. For example:

### [Decoding](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Malformed_URI#decoding)

Decoding replaces each escape sequence in the encoded URI component with the character that it represents. If there isn't such a character, an error will be thrown:

With proper input, this should usually look like something like this:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Malformed_URI#see_also)

------------------------------------------------------------------------------------------------------------

*   [`URIError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/URIError)
    
*   [`decodeURI`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)
    
*   [`encodeURI`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURI)
    
*   [`encodeURIComponent`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent)
    
*   [`decodeURIComponent`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURIComponent)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Malformed_URI/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/malformed_uri/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/malformed_uri (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FMalformed_URI&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fmalformed_uri%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FMalformed_URI%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fmalformed_uri%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")