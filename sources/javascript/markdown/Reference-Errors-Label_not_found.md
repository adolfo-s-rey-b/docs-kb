*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Label_not_found#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Label_not_found#mdn-search)
    

SyntaxError: label not found
============================

The JavaScript exception "label not found" occurs when a [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
 or [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
 statement references a label that does not exist on any statement that contains the `break` or `continue` statement.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Label_not_found#message)

------------------------------------------------------------------------------------------------------------

SyntaxError: Undefined label 'label' (V8-based)
SyntaxError: label not found (Firefox)
SyntaxError: Cannot use the undeclared label 'label'. (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Label_not_found#error_type)

------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
.

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Label_not_found#what_went_wrong)

-----------------------------------------------------------------------------------------------------------------------------

In JavaScript, [labels](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
 are very limited: you can only use them with [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
 and [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
 statements, and you can only jump to them from a statement contained within the labeled statement. You cannot jump to this label from anywhere in the program.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Label_not_found#examples)

--------------------------------------------------------------------------------------------------------------

### [Unsyntactic jump](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Label_not_found#unsyntactic_jump)

You cannot use labels as if they are `goto`.

js

    start: console.log("Hello, world!");
    console.log("Do it again");
    break start;
    

Instead, you can only use labels to enhance the normal semantics of `break` and `continue` statements.

js

    start: {
      console.log("Hello, world!");
      if (Math.random() > 0.5) {
        break start;
      }
      console.log("Maybe I'm logged");
    }
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Label_not_found#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Labeled statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Label_not_found/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/label_not_found/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/label_not_found (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FLabel_not_found&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Flabel_not_found%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FLabel_not_found%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Flabel_not_found%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")