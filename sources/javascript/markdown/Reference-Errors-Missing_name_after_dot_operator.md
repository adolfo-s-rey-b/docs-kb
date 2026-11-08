*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_name_after_dot_operator#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_name_after_dot_operator#mdn-search)
    

SyntaxError: missing name after . operator
==========================================

The JavaScript exception "missing name after . operator" occurs when there is a problem with how the dot operator (`.`) is used for [property access](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)
.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_name_after_dot_operator#message)

----------------------------------------------------------------------------------------------------------------------------

SyntaxError: missing name after . operator (Firefox)
SyntaxError: Unexpected token '\['. Expected a property name after '.'. (Safari)\
\
[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_name_after_dot_operator#error_type)\
\
----------------------------------------------------------------------------------------------------------------------------------\
\
[`SyntaxError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/SyntaxError)\
\
[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_name_after_dot_operator#what_went_wrong)\
\
---------------------------------------------------------------------------------------------------------------------------------------------\
\
The dot operator (`.`) is used for [property access](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)\
. You will have to specify the name of the property that you want to access. For computed property access, you might need to change your property access from using a dot to using square brackets. These will allow you to compute an expression. Maybe you intended to do concatenation instead? A plus operator (`+`) is needed in that case. Please see the examples below.\
\
[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_name_after_dot_operator#examples)\
\
------------------------------------------------------------------------------------------------------------------------------\
\
### [Property access](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_name_after_dot_operator#property_access)\
\
[Property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)\
 in JavaScript use either the dot (.) or square brackets (`[]`), but not both. Square brackets allow computed property access.\
\
js\
\
    const obj = { foo: { bar: "baz", bar2: "baz2" } };\
    const i = 2;\
    \
    obj.[foo].[bar]\
    // SyntaxError: missing name after . operator\
    \
    obj.foo."bar"+i;\
    // SyntaxError: missing name after . operator\
    \
\
To fix this code, you need to access the object like this:\
\
js\
\
    obj.foo.bar; // "baz"\
    // or alternatively\
    obj["foo"]["bar"]; // "baz"\
    \
    // computed properties require square brackets\
    obj.foo["bar" + i]; // "baz2"\
    // or as template literal\
    obj.foo[`bar${i}`]; // "baz2"\
    \
\
### [Property access vs. concatenation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_name_after_dot_operator#property_access_vs._concatenation)\
\
If you are coming from another programming language (like [PHP](https://developer.mozilla.org/en-US/docs/Glossary/PHP)\
), it is also easy to mix up the dot operator (`.`) and the concatenation operator (`+`).\
\
js\
\
    console.log("Hello" . "world");\
    \
    // SyntaxError: missing name after . operator\
    \
\
Instead you need to use a plus sign for concatenation:\
\
js\
\
    console.log("Hello" + "World");\
    \
\
[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_name_after_dot_operator#see_also)\
\
------------------------------------------------------------------------------------------------------------------------------\
\
*   [Property accessors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Property_accessors)\
    \
\
Help improve MDN\
----------------\
\
[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)\
\
This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Missing_name_after_dot_operator/contributors.txt)\
.\
\
[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/missing_name_after_dot_operator/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/missing_name_after_dot_operator (Opens in a new tab)")\
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FMissing_name_after_dot_operator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fmissing_name_after_dot_operator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FMissing_name_after_dot_operator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Fmissing_name_after_dot_operator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")