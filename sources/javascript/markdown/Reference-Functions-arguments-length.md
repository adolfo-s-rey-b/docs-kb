*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length#mdn-search)
    

arguments.length
================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`arguments.length`** data property contains the number of arguments passed to the function.

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length#value)

------------------------------------------------------------------------------------------------------------

A non-negative integer.

|     |     |
| --- | --- |
| Writable | yes |
| Enumerable | no  |
| Configurable | yes |

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length#description)

------------------------------------------------------------------------------------------------------------------------

The `arguments.length` property provides the number of arguments actually passed to a function. This can be more or less than the number of defined parameters (see [`Function.prototype.length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length)
). For example, for the function below:

js

    function func1(a, b, c) {
      console.log(arguments.length);
    }
    

`func1.length` returns `3`, because `func1` declares three formal parameters. However, `func1(1, 2, 3, 4, 5)` logs `5`, because `func1` was called with five arguments. Similarly, `func1(1)` logs `1`, because `func1` was called with one argument.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length#examples)

------------------------------------------------------------------------------------------------------------------

### [Using arguments.length](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length#using_arguments.length)

In this example, we define a function that can add two or more numbers together.

js

    function adder(base /*, num1, …, numN */) {
      base = Number(base);
      for (let i = 1; i < arguments.length; i++) {
        base += Number(arguments[i]);
      }
      return base;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length#specifications)

------------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-arguments-exotic-objects](https://tc39.es/ecma262/multipage/ordinary-and-exotic-objects-behaviours.html#sec-arguments-exotic-objects) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length#see_also)

------------------------------------------------------------------------------------------------------------------

*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions)
     guide
*   [Functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions)
    
*   [`arguments`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments)
    
*   [`Function`: `length`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/length)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 2, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/arguments/length/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/functions/arguments/length/index.md?plain=1 "Folder: en-us/web/javascript/reference/functions/arguments/length (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Farguments%2Flength&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Farguments%2Flength%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FFunctions%2Farguments%2Flength%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ffunctions%2Farguments%2Flength%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F389605121ed8ea78cc1878f31bbca6759cc7417d%0A*+Document+last+modified%3A+2026-11-02T18%3A33%3A54.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")