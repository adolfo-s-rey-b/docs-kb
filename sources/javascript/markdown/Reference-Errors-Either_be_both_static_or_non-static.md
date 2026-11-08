*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Either_be_both_static_or_non-static#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Either_be_both_static_or_non-static#mdn-search)
    

SyntaxError: getter and setter for private name #x should either be both static or non-static
=============================================================================================

The JavaScript exception "mismatched placement" occurs when a private [getter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 and [setter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 are mismatched in whether or not they are [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Either_be_both_static_or_non-static#message)

--------------------------------------------------------------------------------------------------------------------------------

SyntaxError: Identifier '#x' has already been declared (V8-based)
SyntaxError: getter and setter for private name #x should either be both static or non-static (Firefox)
SyntaxError: Cannot declare a private non-static getter if there is a static private setter with used name. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Either_be_both_static_or_non-static#error_type)

--------------------------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Either_be_both_static_or_non-static#what_went_wrong)

-------------------------------------------------------------------------------------------------------------------------------------------------

Private [getters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
 and [setters](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
 for the same name must either be both [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
, or both non-static. This limitation does not exist for public methods.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Either_be_both_static_or_non-static#examples)

----------------------------------------------------------------------------------------------------------------------------------

### [Mismatched placement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Either_be_both_static_or_non-static#mismatched_placement)

Since `foo` is [private](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
, the methods must be either both [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
:

or non-static:

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Either_be_both_static_or_non-static#see_also)

----------------------------------------------------------------------------------------------------------------------------------

*   [`get`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/get)
    
*   [`set`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/set)
    
*   [`static`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/static)
    
*   [Private elements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes/Private_elements)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Either_be_both_static_or_non-static/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/either_be_both_static_or_non-static/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/either_be_both_static_or_non-static (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FEither_be_both_static_or_non-static&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Feither_be_both_static_or_non-static%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FEither_be_both_static_or_non-static%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Feither_be_both_static_or_non-static%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")