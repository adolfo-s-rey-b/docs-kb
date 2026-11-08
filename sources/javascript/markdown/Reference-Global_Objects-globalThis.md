*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#mdn-search)
    

globalThis
==========

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`globalThis`** global property contains the [global `this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this#global_context)
 value, which is usually akin to the [global object](https://developer.mozilla.org/en-US/docs/Glossary/Global_object)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#try_it)

-------------------------------------------------------------------------------------------------------------

[Value](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#value)

-----------------------------------------------------------------------------------------------------------

The global `this` object.

|     |     |
| --- | --- |
| Writable | yes |
| Enumerable | no  |
| Configurable | yes |

**Note:** The `globalThis` property is configurable and writable so that code authors can hide it when executing untrusted code and prevent exposing the global object.

[Description](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#description)

-----------------------------------------------------------------------------------------------------------------------

Historically, accessing the global object has required different syntax in different JavaScript environments. On the web you can use [`window`](https://developer.mozilla.org/en-US/docs/Web/API/Window/window "window")
, [`self`](https://developer.mozilla.org/en-US/docs/Web/API/Window/self "self")
, or [`frames`](https://developer.mozilla.org/en-US/docs/Web/API/Window/frames "frames")
 - but in [Web Workers](https://developer.mozilla.org/en-US/docs/Web/API/Worker)
 only `self` will work. In Node.js none of these work, and you must instead use `global`. The `this` keyword could be used inside functions running in non–strict mode, but `this` will be `undefined` in modules and inside functions running in strict mode. You can also use `Function('return this')()`, but environments that disable [`eval()`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/eval)
, like [CSP](https://developer.mozilla.org/en-US/docs/Glossary/CSP)
 in browsers, prevent use of [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function)
 in this way.

The `globalThis` property provides a standard way of accessing the global `this` value (and hence the global object itself) across environments. Unlike similar properties such as `window` and `self`, it's guaranteed to work in window and non-window contexts. In this way, you can access the global object in a consistent manner without having to know which environment the code is being run in. To help you remember the name, just remember that in global scope the `this` value is `globalThis`.

**Note:** `globalThis` is generally the same concept as the global object (i.e., adding properties to `globalThis` makes them global variables) — this is the case for browsers and Node — but hosts are allowed to provide a different value for `globalThis` that's unrelated to the global object.

### [HTML and the WindowProxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#html_and_the_windowproxy)

In many engines `globalThis` will be a reference to the actual global object, but in web browsers, due to iframe and cross-window security considerations, it references a [`Proxy`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy)
 around the actual global object (which you can't directly access). This distinction is rarely relevant in common usage, but important to be aware of.

### [Naming](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#naming)

Several other popular name choices such as `self` and `global` were removed from consideration because of their potential to break compatibility with existing code. See the [language proposal's "naming" document](https://github.com/tc39/proposal-global/blob/master/NAMING.md "External link (opens in new tab)")
 for more details.

`globalThis` is, quite literally, the global `this` value. It's the same value as the `this` value in a non-strict function called without an object. It's also the value of `this` in the global scope of a script.

[Examples](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#examples)

-----------------------------------------------------------------------------------------------------------------

### [Search for the global across environments](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#search_for_the_global_across_environments)

Usually, the global object does not need to be explicitly specified — its properties are automatically accessible as global variables.

However, one case where one needs to explicitly access the global object is when _writing_ to it, usually for the purpose of [polyfills](https://developer.mozilla.org/en-US/docs/Glossary/Polyfill)
.

Prior to `globalThis`, the only reliable cross-platform way to get the global object for an environment was `Function('return this')()`. However, this causes [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
 violations in some settings, so authors would use a piecewise definition like this (slightly adapted from the [original core-js source](https://github.com/zloirock/core-js/blob/master/packages/core-js/internals/global-this.js "External link (opens in new tab)")
):

After obtaining the global object, we can define new globals on it. For example, adding an implementation for [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
:

With `globalThis` available, the additional search for the global across environments is not necessary anymore:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [ECMAScript® 2027 Language Specification  <br>\# sec-globalthis](https://tc39.es/ecma262/multipage/global-object.html#sec-globalthis) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Polyfill of `globalThis` in `core-js`](https://core-js.io/docs/features/ecmascript/global-this "External link (opens in new tab)")
    
*   [es-shims polyfill of `globalThis`](https://www.npmjs.com/package/globalthis "External link (opens in new tab)")
    
*   [`this`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/this)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/globalThis/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/global_objects/globalthis/index.md?plain=1 "Folder: en-us/web/javascript/reference/global_objects/globalthis (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FglobalThis&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fglobalthis%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FGlobal_Objects%2FglobalThis%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fglobal_objects%2Fglobalthis%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9de14917b151f7db567a65d44c2685cea754b12a%0A*+Document+last+modified%3A+2026-10-26T04%3A56%3A01.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")