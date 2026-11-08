*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_token#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_token#mdn-search)
    

SyntaxError: Unexpected token
=============================

The JavaScript exceptions "unexpected token" occur when the parser does not see a token it recognizes at the given position, so it cannot make sense of the structure of the program. This might be a simple typo.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_token#message)

-------------------------------------------------------------------------------------------------------------

SyntaxError: Unexpected token ';' (V8-based)
SyntaxError: Unexpected identifier 'x' (V8-based)
SyntaxError: Unexpected number (V8-based)
SyntaxError: Unexpected string (V8-based)
SyntaxError: Unexpected regular expression (V8-based)
SyntaxError: Unexpected template string (V8-based)

SyntaxError: unexpected token: identifier (Firefox)
SyntaxError: expected expression, got "x" (Firefox)
SyntaxError: expected property name, got "x" (Firefox)
SyntaxError: expected target, got "x" (Firefox)
SyntaxError: expected meta, got "x" (Firefox)
SyntaxError: expected rest argument name, got "x" (Firefox)
SyntaxError: expected closing parenthesis, got "x" (Firefox)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_token#error_type)

-------------------------------------------------------------------------------------------------------------------

[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_token#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------

A specific language construct was expected, but something else was provided. This might be a simple typo.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_token#examples)

---------------------------------------------------------------------------------------------------------------

### [Expression expected](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_token#expression_expected)

For example, when chaining expressions, trailing commas are not allowed.

js

    for (let i = 0; i < 5,; ++i) {
      console.log(i);
    }
    // Uncaught SyntaxError: expected expression, got ';'
    

Correct would be omitting the comma or adding another expression:

js

    for (let i = 0; i < 5; ++i) {
      console.log(i);
    }
    

### [Not enough parentheses](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_token#not_enough_parentheses)

Sometimes, you leave out parentheses around `if` statements:

js

    function round(n, upperBound, lowerBound) {
    if (n > upperBound) || (n < lowerBound) { // Missing parentheses here!
        throw new Error(`Number ${n} is more than ${upperBound} or less than ${lowerBound}`);
      } else if (n < (upperBound + lowerBound) / 2) {
        return lowerBound;
      } else {
        return upperBound;
      }
    } // SyntaxError: expected expression, got '||'
    

The parentheses may look correct at first, but note how the `||` is outside the parentheses. Correct would be putting parentheses around the `||`:

js

    function round(n, upperBound, lowerBound) {
      if ((n > upperBound) || (n < lowerBound)) {
        throw new Error(
          `Number ${n} is more than ${upperBound} or less than ${lowerBound}`,
        );
      } else if (n < (upperBound + lowerBound) / 2) {
        return lowerBound;
      } else {
        return upperBound;
      }
    }
    

### [A structure error further up confused the meaning](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_token#a_structure_error_further_up_confused_the_meaning)

Sometimes, the error is caused by some structure issues not directly next to the error location, so you need to look around for potential errors. For example, you intended to declare a method of an object, but you declared it as a property instead:

js

    const MyComponent = {
      mounted: {
        document.getElementById("app").classList.add("loaded");
      }
    }
    

The `.` after `document` is unexpected, because JavaScript is parsing the `{}` as an object literal instead of a function body, so it expects a `:`. The problem is solved by declaring `mounted` as a function.

js

    const MyComponent = {
      mounted() {
        document.getElementById("app").classList.add("loaded");
      }
    }
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_token#see_also)

---------------------------------------------------------------------------------------------------------------

*   [`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Unexpected_token/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/unexpected_token/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/unexpected_token (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUnexpected_token&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Funexpected_token%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FUnexpected_token%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Funexpected_token%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1474534461893381d54c502e655f334b5568e597%0A*+Document+last+modified%3A+2026-08-21T19%3A37%3A29.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")