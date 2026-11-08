*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#mdn-search)
    

do...while
==========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`do...while`** statement creates a loop that executes a specified statement as long as the test condition evaluates to true. The condition is evaluated after executing the statement, resulting in the specified statement executing at least once.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#try_it)

---------------------------------------------------------------------------------------------------------

    let result = "";
    let i = 0;
    
    do {
      i += 1;
      result += i;
    } while (i < 5);
    
    console.log(result);
    // Expected output: "12345"
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#syntax)

---------------------------------------------------------------------------------------------------------

js

    do
      statement
    while (condition);
    

[`statement`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#statement)

A statement that is executed at least once and re-executed as long as the condition evaluates to true. You can use a [block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/block)
 to execute multiple statements.

[`condition`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#condition)

An expression evaluated _after_ each pass through the loop. If this condition [evaluates to true](https://developer.mozilla.org/en-US/docs/Glossary/Truthy)
, `statement` is re-executed. When condition [evaluates to false](https://developer.mozilla.org/en-US/docs/Glossary/Falsy)
, execution continues with the statement after the `do...while` loop.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#description)

-------------------------------------------------------------------------------------------------------------------

Like other looping statements, you can use [control flow statements](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements#control_flow)
 inside `statement`:

*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
     stops `statement` execution and goes to the first statement after the loop.
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
     stops `statement` execution and re-evaluates `condition`.

The `do...while` statement syntax requires a semicolon at the end, but the [automatic semicolon insertion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#automatic_semicolon_insertion)
 process may insert one for you if the lack of a semicolon results in invalid syntax.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#examples)

-------------------------------------------------------------------------------------------------------------

### [Using do...while](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#using_do...while)

In the following example, the `do...while` loop iterates at least once and reiterates until `i` is no longer less than 5.

js

    let result = "";
    let i = 0;
    do {
      i += 1;
      result += `${i} `;
    } while (i > 0 && i < 5);
    // Despite i === 0 this will still loop as it starts off without the test
    
    console.log(result);
    

### [Using false as do...while condition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#using_false_as_do...while_condition)

Because the statement is always executed once, `do...while (false)` is the same as executing the statement itself. This is a common idiom in C-like languages, which allows you to use `break` to break out of branching logic early.

js

    do {
      if (!user.loggedIn) {
        console.log("You are not logged in");
        break;
      }
      const friends = user.getFriends();
      if (!friends.length) {
        console.log("No friends found");
        break;
      }
      for (const friend of friends) {
        handleFriend(friend);
      }
    } while (false);
    // The rest of code
    

In JavaScript, there are some alternatives, such as using a [labeled block statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/label)
 with `break`:

js

    handleFriends: {
      if (!user.loggedIn) {
        console.log("You are not logged in");
        break handleFriends;
      }
      const friends = user.getFriends();
      if (!friends.length) {
        console.log("No friends found");
        break handleFriends;
      }
      for (const friend of friends) {
        handleFriend(friend);
      }
    }
    

Or using a function:

js

    function handleFriends() {
      if (!user.loggedIn) {
        console.log("You are not logged in");
        return;
      }
      const friends = user.getFriends();
      if (!friends.length) {
        console.log("No friends found");
        return;
      }
      for (const friend of friends) {
        handleFriend(friend);
      }
    }
    

### [Using an assignment as a condition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#using_an_assignment_as_a_condition)

In some cases, it can make sense to use an assignment as a condition, such as this:

js

    do {
      // …
    } while ((match = regexp.exec(str)));
    

But when you do, there are readability tradeoffs. The [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
 documentation has a [Using an assignment as a condition](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while#using_an_assignment_as_a_condition)
 section with our recommendations.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#specifications)

-------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-do-while-statement](https://tc39.es/ecma262/multipage/ecmascript-language-statements-and-declarations.html#sec-do-while-statement) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while#see_also)

-------------------------------------------------------------------------------------------------------------

*   [`while`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/while)
    
*   [`for`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for)
    
*   [`break`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/break)
    
*   [`continue`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/continue)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/do...while/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/statements/do...while/index.md?plain=1 "Folder: en-us/web/javascript/reference/statements/do...while (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fdo...while&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fdo...while%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FStatements%2Fdo...while%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fstatements%2Fdo...while%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")