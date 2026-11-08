*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_negative_exponent#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_negative_exponent#mdn-search)
    

RangeError: BigInt negative exponent
====================================

The JavaScript exception "BigInt negative exponent" occurs when a [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
 is raised to the power of a negative BigInt value.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_negative_exponent#message)

---------------------------------------------------------------------------------------------------------------------

RangeError: Exponent must be positive (V8-based)
RangeError: BigInt negative exponent (Firefox)
RangeError: Negative exponent is not allowed (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_negative_exponent#error_type)

---------------------------------------------------------------------------------------------------------------------------

[`RangeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RangeError)
.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_negative_exponent#what_went_wrong)

--------------------------------------------------------------------------------------------------------------------------------------

The exponent of an [exponentiation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
 operation must be positive. Since negative exponents would take the reciprocal of the base, the result will be between -1 and 1 in almost all cases, which gets rounded to `0n`. To catch mistakes, negative exponents are not allowed. Check if the exponent is non-negative before doing exponentiation.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_negative_exponent#examples)

-----------------------------------------------------------------------------------------------------------------------

### [Using a negative BigInt as exponent](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_negative_exponent#using_a_negative_bigint_as_exponent)

Instead, check if the exponent is negative first, and either issue an error with a better message, or fall back to a different value, like `0n` or `undefined`.

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_negative_exponent#see_also)

-----------------------------------------------------------------------------------------------------------------------

*   [`BigInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/BigInt)
    
*   [Exponentiation (`**`)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Exponentiation)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 31, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/BigInt_negative_exponent/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/bigint_negative_exponent/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/bigint_negative_exponent (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBigInt_negative_exponent&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbigint_negative_exponent%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FBigInt_negative_exponent%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fbigint_negative_exponent%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F61f27416f7cfa79bd102042eeb3e44fe629d9c95%0A*+Document+last+modified%3A+2026-08-31T19%3A24%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")