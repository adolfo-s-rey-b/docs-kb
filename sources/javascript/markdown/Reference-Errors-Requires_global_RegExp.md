*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Requires_global_RegExp#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Requires_global_RegExp#mdn-search)
    

TypeError: matchAll/replaceAll must be called with a global RegExp
==================================================================

The JavaScript exception "TypeError: matchAll/replaceAll must be called with a global RegExp" occurs when the [`String.prototype.matchAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll)
 or [`String.prototype.replaceAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)
 method is used with a [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 object that does not have the [`global`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/global)
 flag set.

[Message](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Requires_global_RegExp#message)

-------------------------------------------------------------------------------------------------------------------

TypeError: String.prototype.matchAll called with a non-global RegExp argument (V8-based)
TypeError: String.prototype.replaceAll called with a non-global RegExp argument (V8-based)
TypeError: matchAll must be called with a global RegExp (Firefox)
TypeError: replaceAll must be called with a global RegExp (Firefox)
TypeError: String.prototype.matchAll argument must not be a non-global regular expression (Safari)
TypeError: String.prototype.replaceAll argument must not be a non-global regular expression (Safari)

[Error type](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Requires_global_RegExp#error_type)

-------------------------------------------------------------------------------------------------------------------------

[`TypeError`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError)

[What went wrong?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Requires_global_RegExp#what_went_wrong)

------------------------------------------------------------------------------------------------------------------------------------

The [`String.prototype.matchAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll)
 and [`String.prototype.replaceAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)
 methods require a [`RegExp`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp)
 object with the [`global`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/global)
 flag set. This flag indicates that the regular expression can match all locations of the input string, instead of stopping at the first match. Although the `g` flag is redundant when using these methods (because these methods always do a global replacement), they are still required to make the intention clear.

It's worth noting that the `g` flag validation is done in the `matchAll` and `replaceAll` methods. If you use the [`[Symbol.matchAll]()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/Symbol.matchAll)
 method of `RegExp` instead, you won't get this error, but there will only be a single match.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Requires_global_RegExp#examples)

---------------------------------------------------------------------------------------------------------------------

### [Invalid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Requires_global_RegExp#invalid_cases)

js

    "abc".matchAll(/./); // TypeError
    "abc".replaceAll(/./, "f"); // TypeError
    

### [Valid cases](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Requires_global_RegExp#valid_cases)

If you intend to do global matching/replacement: either add the `g` flag, or construct a new `RegExp` object with the `g` flag, if you want to keep the original regex unchanged.

js

    [..."abc".matchAll(/./g)]; // [[ "a" ], [ "b" ], [ "c" ]]
    "abc".replaceAll(/./g, "f"); // "fff"
    
    const existingPattern = /./;
    const newPattern = new RegExp(
      existingPattern.source,
      `${existingPattern.flags}g`,
    );
    "abc".replaceAll(newPattern, "f"); // "fff"
    

If you only intend to do a single matching/replacement: use [`String.prototype.match()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/match)
 or [`String.prototype.replace()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replace)
 instead. You can also use the `[Symbol.matchAll]()` method if you want an iterator like `matchAll` returns that only contains one match, but doing so will be very confusing.

js

    "abc".match(/./); // [ "a" ]
    "abc".replace(/./, "f"); // "fbc"
    
    [..././[Symbol.matchAll]("abc")]; // [[ "a" ]]
    

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Requires_global_RegExp#see_also)

---------------------------------------------------------------------------------------------------------------------

*   [`String.prototype.matchAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/matchAll)
    
*   [`String.prototype.replaceAll()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/String/replaceAll)
    
*   [`RegExp.prototype.global`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/RegExp/global)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Errors/Requires_global_RegExp/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/errors/requires_global_regexp/index.md?plain=1 "Folder: en-us/web/javascript/reference/errors/requires_global_regexp (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRequires_global_RegExp&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Frequires_global_regexp%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FErrors%2FRequires_global_RegExp%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Ferrors%2Frequires_global_regexp%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ffad67be4431d8e6c2a89ac880735233aa76c41d4%0A*+Document+last+modified%3A+2025-07-08T13%3A18%3A45.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")