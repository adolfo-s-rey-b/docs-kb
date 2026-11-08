*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Property_access_denied#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Property_access_denied#mdn-search)
    

Error: Permission denied to access property "x"
===============================================

The JavaScript exception "Permission denied to access property" occurs when there was an attempt to access an object for which you have no permission.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Property_access_denied#message)

-------------------------------------------------------------------------------------------------------------------

DOMException: Blocked a frame with origin "x" from accessing a cross-origin frame. (Chromium-based)
DOMException: Permission denied to access property "x" on cross-origin object (Firefox)
SecurityError: Blocked a frame with origin "x" from accessing a cross-origin frame. Protocols, domains, and ports must match. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Property_access_denied#error_type)

-------------------------------------------------------------------------------------------------------------------------

[`DOMException`](https://developer.mozilla.org/en-US/docs/Web/API/DOMException)
.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Property_access_denied#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------------

There was attempt to access an object for which you have no permission. This is likely an [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
 element loaded from a different domain for which you violated the [same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy)
.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Property_access_denied#examples)

---------------------------------------------------------------------------------------------------------------------

### [No permission to access document](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Property_access_denied#no_permission_to_access_document)

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Property_access_denied#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [`<iframe>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/iframe)
    
*   [Same-origin policy](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Same-origin_policy)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 30, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Property_access_denied/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/property_access_denied/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/property_access_denied (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FProperty_access_denied&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fproperty_access_denied%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FProperty_access_denied%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fproperty_access_denied%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca26363fcc6fc861103d40ac0205e5c5b79eb2fa%0A*+Document+last+modified%3A+2025-11-30T02%3A30%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")