*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#mdn-search)
    

JavaScript technologies overview
================================

Whereas [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 defines a webpage's structure and content and [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 sets the formatting and appearance, [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
 adds interactivity to a webpage and creates rich web applications.

However, the umbrella term "JavaScript" as understood in a web browser context contains several very different elements. One of them is the core language (ECMAScript), another is the collection of the [Web APIs](https://developer.mozilla.org/en-US/docs/Web/API)
, including the DOM (Document Object Model).

[JavaScript, the core language (ECMAScript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#javascript_the_core_language_ecmascript)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The core language of JavaScript is standardized by the ECMA TC39 committee as a language named ECMAScript. "ECMAScript" is the term for the language standard, but "ECMAScript" and "JavaScript" can be used interchangeably.

This core language is also used in non-browser environments, for example in [Node.js](https://nodejs.org/ "External link (opens in new tab)")
.

### [What falls under the ECMAScript scope?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#what_falls_under_the_ecmascript_scope)

Among other things, ECMAScript defines:

*   Language syntax (parsing rules, keywords, control flow, object literal initialization, ...)
*   Error handling mechanisms ([`throw`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw)
    , [`try...catch`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch)
    , ability to create user-defined [`Error`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Error)
     types)
*   Types (boolean, number, string, function, object, ...)
*   A prototype-based inheritance mechanism
*   Built-in objects and functions, including [`JSON`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)
    , [`Math`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math)
    , [Array](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array)
     methods, [`parseInt`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/parseInt)
    , [`decodeURI`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/decodeURI)
    , etc.
*   [Strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
    
*   A [module system](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
    
*   Basic memory model

### [Standardization process](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#standardization_process)

ECMAScript editions are approved and published as a standard by the ECMA General Assembly on a yearly basis. All development is public on the [Ecma TC39 GitHub organization](https://github.com/tc39 "External link (opens in new tab)")
, which hosts proposals, the official specification text, and meeting notes.

Before the 6th edition of ECMAScript (known as ES6), specifications were published once every several years, and are commonly referred to by their major version numbers — ES3, ES5, etc. After ES6, the specification is named by the publishing year — ES2017, ES2018, etc. ES6 is synonymous with ES2015. _ESNext_ is a dynamic name that refers to whatever the next version is at the time of writing. ESNext features are more correctly called proposals, because, by definition, the specification has not been finalized yet.

The current committee-approved snapshot of ECMA-262 is available in PDF and HTML format on Ecma International's [ECMA-262 language specification page](https://ecma-international.org/publications-and-standards/standards/ecma-262/ "External link (opens in new tab)")
. ECMA-262 and ECMA-402 are continuously maintained and kept up to date by the specification editors; the TC39 website hosts the latest, up-to-date [ECMA-262](https://tc39.es/ecma262/ "External link (opens in new tab)")
 and [ECMA-402](https://tc39.es/ecma402/ "External link (opens in new tab)")
 versions.

New language features, including introduction of new syntaxes and APIs and revision of existing behaviors, are discussed in the form of proposals. Each proposal goes through a [staged process](https://tc39.es/process-document/ "External link (opens in new tab)")
, and is typically implemented by JavaScript engines at stage 3 or stage 4 and thus available for public consumption.

See [Wikipedia ECMAScript entry](https://en.wikipedia.org/wiki/ECMAScript "External link (opens in new tab)")
 for more information on ECMAScript history.

### [Internationalization API](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#internationalization_api)

The [ECMAScript Internationalization API Specification](https://402.ecma-international.org/1.0/ "External link (opens in new tab)")
 is an addition to the ECMAScript Language Specification, also standardized by Ecma TC39. The internationalization API provides collation (string comparison), number formatting, and date-and-time formatting for JavaScript applications, letting the applications choose the language and tailor the functionality to their needs. The initial standard was approved in December 2012; the status of implementations in browsers is tracked in the documentation of the [`Intl`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Intl)
 object. The Internationalization specification is nowadays also ratified on a yearly basis and browsers constantly improve their implementation.

### [Related resources](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#related_resources)

There are a variety of ways you can participate in or just track current work on the ECMAScript Language Specification and the ECMAScript Internationalization API Specification and related resources:

*   [ECMAScript Language Specification repo](https://github.com/tc39/ecma262 "External link (opens in new tab)")
    
*   [ECMAScript Internationalization API Specification repo](https://github.com/tc39/ecma402 "External link (opens in new tab)")
    
*   [ECMAScript proposals repo](https://github.com/tc39/proposals "External link (opens in new tab)")
    
*   [ECMAScript conformance test suite repo](https://github.com/tc39/test262 "External link (opens in new tab)")
    
*   [TC39 meeting notes](https://github.com/tc39/notes "External link (opens in new tab)")
    
*   [ECMAScript spec discussion; current mailing list](https://es.discourse.group/ "External link (opens in new tab)")
    
*   [ECMAScript spec discussion; historical mailing-list archives (until March 2021)](https://esdiscuss.org/ "External link (opens in new tab)")
    

[DOM APIs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#dom_apis)

------------------------------------------------------------------------------------------------------------------------

### [WebIDL](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#webidl)

The [WebIDL specification](https://webidl.spec.whatwg.org/ "External link (opens in new tab)")
 provides the glue between the DOM technologies and ECMAScript.

### [The Core of the DOM](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#the_core_of_the_dom)

The Document Object Model (DOM) is a cross-platform, **language-independent convention** for representing and interacting with objects in HTML, XHTML and XML documents. Objects in the **DOM tree** may be addressed and manipulated by using methods on the objects. Nowadays, the [DOM core](https://dom.spec.whatwg.org/ "External link (opens in new tab)")
 spec is maintained by [WHATWG](https://developer.mozilla.org/en-US/docs/Glossary/WHATWG)
 (superseding the [W3C](https://developer.mozilla.org/en-US/docs/Glossary/W3C)
 version). It defines language-agnostic interfaces that abstract HTML and XML documents as objects, and also defines mechanisms to manipulate this abstraction. This includes: [`Node`](https://developer.mozilla.org/en-US/docs/Web/API/Node)
, [`Element`](https://developer.mozilla.org/en-US/docs/Web/API/Element)
, [`DocumentFragment`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment)
, [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document)
, [`DOMImplementation`](https://developer.mozilla.org/en-US/docs/Web/API/DOMImplementation)
, [`Event`](https://developer.mozilla.org/en-US/docs/Web/API/Event)
, [`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget)
, and more.

From the ECMAScript point of view, objects defined in the DOM specification are called "host objects".

### [HTML DOM](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#html_dom)

[HTML](https://html.spec.whatwg.org/multipage/ "External link (opens in new tab)")
, the Web's markup language, is specified in terms of the DOM. Layered above the abstract concepts defined in DOM Core, HTML also defines the _meaning_ of elements. The HTML DOM includes APIs such as [`Document.body`](https://developer.mozilla.org/en-US/docs/Web/API/Document/body)
 and HTML element interfaces.

The HTML specification also defines restrictions on documents; for example, it requires all children of a [`<ul>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ul)
 element, which represents an unordered list, to be [`<li>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/li)
 elements, as those represent list items. In general, it also forbids using elements and attributes that aren't defined in a standard.

Looking for the [`Document`](https://developer.mozilla.org/en-US/docs/Web/API/Document)
 object, [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
 object, and the other DOM elements? Read the [DOM documentation](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model)
.

[Other notable APIs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#other_notable_apis)

--------------------------------------------------------------------------------------------------------------------------------------------

*   The [`setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout "setTimeout()")
     and [`setInterval()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setInterval "setInterval()")
     functions were first specified on the [`Window`](https://developer.mozilla.org/en-US/docs/Web/API/Window)
     interface in HTML Standard.
*   [XMLHttpRequest](https://xhr.spec.whatwg.org/ "External link (opens in new tab)")
     makes it possible to send asynchronous HTTP requests.
*   The [Fetch API](https://fetch.spec.whatwg.org/ "External link (opens in new tab)")
     provides a more ergonomic abstraction for network requests.
*   The [CSS Object Model](https://drafts.csswg.org/cssom/ "External link (opens in new tab)")
     abstracts CSS rules as objects.
*   [WebWorkers](https://html.spec.whatwg.org/multipage/workers.html "External link (opens in new tab)")
     allow parallel computation.
*   [WebSockets](https://html.spec.whatwg.org/multipage/#network "External link (opens in new tab)")
     allow low-level bidirectional communication.
*   [Canvas 2D Context](https://html.spec.whatwg.org/multipage//#2dcontext "External link (opens in new tab)")
     is a drawing API for [`<canvas>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/canvas)
    .
*   The [WebAssembly interface](https://webassembly.github.io/spec/js-api/ "External link (opens in new tab)")
     provides utilities for communication between JavaScript code and [WebAssembly](https://developer.mozilla.org/en-US/docs/WebAssembly)
     modules.

Non-browser environments (like Node.js) often do not have DOM APIs — because they don't interact with a document — but they still usually implement many web APIs, such as [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/fetch "fetch()")
 and [`setTimeout()`](https://developer.mozilla.org/en-US/docs/Web/API/Window/setTimeout "setTimeout()")
.

[JavaScript implementations](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#javascript_implementations)

------------------------------------------------------------------------------------------------------------------------------------------------------------

JavaScript engines used in current web browsers include:

*   Mozilla's [SpiderMonkey](https://spidermonkey.dev/ "External link (opens in new tab)")
    , used in Firefox, Servo, and Flow. Other non-browser usage includes MongoDB, CouchDB, and more. This was the first _ever_ JavaScript engine, created by Brendan Eich at Netscape.
*   Google's [V8](https://v8.dev/ "External link (opens in new tab)")
    , used in Chrome and Chromium-based browsers such as Opera, Edge, and Brave. Other non-browser usage includes [Node.js](https://nodejs.org/ "External link (opens in new tab)")
    , [Deno](https://deno.com/ "External link (opens in new tab)")
    , [Electron](https://www.electronjs.org/ "External link (opens in new tab)")
    , and more.
*   Apple's [JavaScriptCore](https://docs.webkit.org/Deep%20Dive/JSC/JavaScriptCore.html "External link (opens in new tab)")
     (also known as SquirrelFish/Nitro), used in Safari and other WebKit-based browsers. Other non-browser usage includes [Bun](https://bun.com/ "External link (opens in new tab)")
    .
*   [LibJS](https://serenityos.github.io/libjs-website/ "External link (opens in new tab)")
    , used in [Ladybird](https://ladybird.org/ "External link (opens in new tab)")
    .

Some JavaScript engines used in earlier browsers include:

*   [Carakan](https://en.wikipedia.org/wiki/Presto_(browser_engine)#ECMAScript_engines "External link (opens in new tab)")
    , used in Opera before it became a Chromium-based browser.
*   Microsoft's [Chakra](https://en.wikipedia.org/wiki/Chakra_(JScript_engine) "External link (opens in new tab)")
    , used in Internet Explorer (although the language it implements is formally called "JScript" to avoid trademark issues). Earlier versions of Edge used another JavaScript engine, confusingly also called [Chakra](https://en.wikipedia.org/wiki/Chakra_(JavaScript_engine) "External link (opens in new tab)")
    , before it became a Chromium-based browser.

Some JavaScript engines specifically tailored for non-browser purposes include:

*   [Engine262](https://engine262.js.org/ "External link (opens in new tab)")
    , written in JavaScript and intended essentially as a reference implementation of the language.
*   Meta's [Hermes](https://github.com/meta/hermes "External link (opens in new tab)")
    , optimized for [React Native](https://reactnative.dev/docs/hermes "External link (opens in new tab)")
    .
*   Mozilla's [Rhino](https://en.wikipedia.org/wiki/Rhino_(JavaScript_engine) "External link (opens in new tab)")
    , written in Java.
*   Oracle's [GraalJS](https://www.graalvm.org/ "External link (opens in new tab)")
    , written in Java and built on top of GraalVM.
*   [Moddable XS](https://www.moddable.com/ "External link (opens in new tab)")
    , intended for IoT/embedded systems.
*   [QuickJS](https://bellard.org/quickjs/ "External link (opens in new tab)")
    , intended to be small and lightweight.

JavaScript engines expose a public API which application developers can use to integrate JavaScript into their software. By far, the most common host environment for JavaScript is web browsers. Web browsers typically use the public API to create **host objects** responsible for reflecting the [DOM](https://dom.spec.whatwg.org/ "External link (opens in new tab)")
 into JavaScript.

Another common application for JavaScript is as a (Web) server-side scripting language. A JavaScript web server exposes host objects representing an HTTP request and response objects, which can then be manipulated by a JavaScript program to dynamically generate web pages. [Node.js](https://nodejs.org/ "External link (opens in new tab)")
 is a popular example of this.

[Shells](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#shells)

--------------------------------------------------------------------------------------------------------------------

A JavaScript shell allows you to quickly test snippets of JavaScript code without having to reload a web page. They are extremely useful for developing and debugging code.

### [Standalone JavaScript shells](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#standalone_javascript_shells)

The following JavaScript shells are stand-alone environments, like Perl or Python.

*   [Node.js](https://nodejs.org/ "External link (opens in new tab)")
     - A V8-based JavaScript runtime.
*   [Bun](https://bun.com/ "External link (opens in new tab)")
     - A JavaScriptCore-based JavaScript runtime.

### [Browser-based JavaScript shells](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#browser-based_javascript_shells)

The following JavaScript shells run code through the browser's JavaScript engine.

*   Firefox has a [built-in JavaScript console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/the_command_line_interpreter/index.html "External link (opens in new tab)")
    , which supports multi-line editing.
*   [Babel REPL](https://babeljs.io/repl "External link (opens in new tab)")
     - A browser-based [REPL](https://en.wikipedia.org/wiki/REPL "External link (opens in new tab)")
     for experimenting with future JavaScript.
*   [TypeScript playground](https://www.typescriptlang.org/play/ "External link (opens in new tab)")
     — A browser-based playground for experimenting with both new JavaScript features (via the tsc compiler) and TypeScript syntax.

[Tools & resources](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview#tools_resources)

----------------------------------------------------------------------------------------------------------------------------------------

Helpful tools for writing and debugging your JavaScript code.

[Firefox Developer Tools](https://firefox-source-docs.mozilla.org/devtools-user/index.html "External link (opens in new tab)")

[Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/index.html "External link (opens in new tab)")
, [JavaScript Profiler](https://firefox-source-docs.mozilla.org/devtools-user/performance/index.html "External link (opens in new tab)")
, [Debugger](https://firefox-source-docs.mozilla.org/devtools-user/debugger/index.html "External link (opens in new tab)")
, and more.

[Learn JavaScript](https://learnjavascript.online/ "External link (opens in new tab)")

An excellent resource for aspiring web developers — Learn JavaScript in an interactive environment, with short lessons and interactive tests, guided by automated assessment. The first 40 lessons are free, and the complete course is available for a small one-time payment.

[TogetherJS](https://togetherjs.com/ "External link (opens in new tab)")

Collaboration made easy. By adding TogetherJS to your site, your users can help each other out on a website in real-time!

[Stack Overflow](https://stackoverflow.com/questions/tagged/javascript "External link (opens in new tab)")

Stack Overflow questions tagged with "JavaScript".

[JSFiddle](https://jsfiddle.net/ "External link (opens in new tab)")

Edit JavaScript, CSS, and HTML and get live results. Use external resources and collaborate with your team online.

[Plunker](https://plnkr.co/ "External link (opens in new tab)")

Plunker is an online community for creating, collaborating on, and sharing your web development ideas. Edit your JavaScript, CSS, and HTML files and get live results and file structure.

[JS Bin](https://jsbin.com/ "External link (opens in new tab)")

JS Bin is an open-source collaborative web development debugging tool.

[CodePen](https://codepen.io/ "External link (opens in new tab)")

CodePen is another collaborative web development tool used as a live result playground.

[StackBlitz](https://stackblitz.com/ "External link (opens in new tab)")

StackBlitz is another online playground/debugging tool, which can host and deploy full-stack applications using React, Angular, etc.

[RunJS](https://runjs.app/ "External link (opens in new tab)")

RunJS is a desktop playground/scratchpad tool, which provides live results and access to both Node and Browser APIs.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/reference/javascript_technologies_overview/index.md?plain=1 "Folder: en-us/web/javascript/reference/javascript_technologies_overview (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FJavaScript_technologies_overview&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Freference%2Fjavascript_technologies_overview%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FReference%2FJavaScript_technologies_overview%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Freference%2Fjavascript_technologies_overview%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F2a563c927890794b513523649ccfbbe48d336465%0A*+Document+last+modified%3A+2026-11-05T23%3A07%3A41.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")