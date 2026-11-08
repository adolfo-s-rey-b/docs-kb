*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Form_must_be_one_of#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Form_must_be_one_of#mdn-search)
    

RangeError: form must be one of 'NFC', 'NFD', 'NFKC', or 'NFKD'
===============================================================

The JavaScript exception "form must be one of 'NFC', 'NFD', 'NFKC', or 'NFKD'" occurs when an unrecognized string is passed to the [`String.prototype.normalize()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize)
 method.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Form_must_be_one_of#message)

----------------------------------------------------------------------------------------------------------------

RangeError: The normalization form should be one of NFC, NFD, NFKC, NFKD. (V8-based)
RangeError: form must be one of 'NFC', 'NFD', 'NFKC', or 'NFKD' (Firefox)
RangeError: argument does not match any normalization form (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Form_must_be_one_of#error_type)

----------------------------------------------------------------------------------------------------------------------

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Form_must_be_one_of#what_went_wrong)

---------------------------------------------------------------------------------------------------------------------------------

The [`String.prototype.normalize()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize)
 method only accepts the following four values as its `form` argument: `"NFC"`, `"NFD"`, `"NFKC"`, or `"NFKD"`. If you pass any other value, an error will be thrown. Read the reference of `normalize()` to learn about different normalization forms.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Form_must_be_one_of#examples)

------------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Form_must_be_one_of#invalid_cases)

js

    "foo".normalize("nfc"); // RangeError
    "foo".normalize(" NFC "); // RangeError
    

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Form_must_be_one_of#valid_cases)

js

    "foo".normalize("NFC"); // 'foo'
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Form_must_be_one_of#see_also)

------------------------------------------------------------------------------------------------------------------

*   [`String.prototype.normalize()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/normalize)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Form_must_be_one_of/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/form_must_be_one_of/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/form_must_be_one_of (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FForm_must_be_one_of&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fform_must_be_one_of%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FForm_must_be_one_of%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fform_must_be_one_of%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")