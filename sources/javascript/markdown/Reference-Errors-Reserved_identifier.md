*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Reserved_identifier#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Reserved_identifier#mdn-search)
    

SyntaxError: "x" is a reserved identifier
=========================================

The JavaScript exception "_variable_ is a reserved identifier" occurs when [reserved keywords](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#keywords)
 are used as identifiers.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Reserved_identifier#message)

----------------------------------------------------------------------------------------------------------------

SyntaxError: Unexpected reserved word (V8-based)
SyntaxError: implements is a reserved identifier (Firefox)
SyntaxError: Cannot use the reserved word 'implements' as a variable name. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Reserved_identifier#error_type)

----------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Reserved_identifier#what_went_wrong)

---------------------------------------------------------------------------------------------------------------------------------

[Reserved keywords](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#keywords)
 will throw in if they are used as identifiers. These are reserved in strict mode and sloppy mode:

*   `enum`

The following are only reserved when they are found in strict mode code:

*   `implements`
*   `interface`
*   [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
    
*   `package`
*   `private`
*   `protected`
*   `public`
*   `static`

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Reserved_identifier#examples)

------------------------------------------------------------------------------------------------------------------

### [Strict and non-strict reserved keywords](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Reserved_identifier#strict_and_non-strict_reserved_keywords)

The `enum` identifier is generally reserved.

js

    const enum = { RED: 0, GREEN: 1, BLUE: 2 };
    // SyntaxError: enum is a reserved identifier
    

In strict mode code, more identifiers are reserved.

js

    "use strict";
    const package = ["potatoes", "rice", "fries"];
    // SyntaxError: package is a reserved identifier
    

You'll need to rename these variables.

js

    const colorEnum = { RED: 0, GREEN: 1, BLUE: 2 };
    const list = ["potatoes", "rice", "fries"];
    

### [Update older browsers](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Reserved_identifier#update_older_browsers)

If you are using an older browser that does not yet implement [`let`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let)
 or [`class`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/class)
, for example, you should update to a more recent browser version that does support these new language features.

js

    "use strict";
    class DocArchiver {}
    
    // SyntaxError: class is a reserved identifier
    // (throws in older browsers only, e.g. Firefox 44 and older)
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Reserved_identifier#see_also)

------------------------------------------------------------------------------------------------------------------

*   [Lexical grammar](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Reserved_identifier/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/reserved_identifier/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/reserved_identifier (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FReserved_identifier&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Freserved_identifier%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FReserved_identifier%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Freserved_identifier%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")