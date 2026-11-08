*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Hash_outside_class#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Hash_outside_class#mdn-search)
    

SyntaxError: Unexpected '#' used outside of class body
======================================================

The JavaScript exception "Unexpected '#' used outside of class body" occurs when a hash ("#") is encountered in an unexpected context, most notably [outside of a class declaration](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
. Hashes are valid at the beginning of a file as a [hashbang comment](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)
, or inside of a class as part of a private field. You may encounter this error if you forget the quotation marks when trying to access a DOM identifier as well.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Hash_outside_class#message)

---------------------------------------------------------------------------------------------------------------

SyntaxError: Unexpected '#' used outside of class body.

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Hash_outside_class#error_type)

---------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Hash_outside_class#what_went_wrong)

--------------------------------------------------------------------------------------------------------------------------------

We encountered a `#` somewhere unexpected. This may be due to code moving around and no longer being part of a class, a hashbang comment found on a line other than the first line of a file, or accidentally forgetting the quotation marks around a DOM identifier.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Hash_outside_class#examples)

-----------------------------------------------------------------------------------------------------------------

### [Missing quotation marks](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Hash_outside_class#missing_quotation_marks)

For each case, there might be something slightly wrong. For example

This can be fixed via

### [Outside of a class](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Hash_outside_class#outside_of_a_class)

This can be fixed by moving the private field back into the class

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Hash_outside_class#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Hash_outside_class/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/hash_outside_class/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/hash_outside_class (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FHash_outside_class&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fhash_outside_class%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FHash_outside_class%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fhash_outside_class%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")