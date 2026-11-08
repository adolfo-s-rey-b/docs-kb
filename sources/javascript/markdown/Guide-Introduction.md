*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#mdn-search)
    

Introduction
============

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types)
    

This chapter introduces JavaScript and discusses some of its fundamental concepts.

[What you should already know](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#what_you_should_already_know)

----------------------------------------------------------------------------------------------------------------------------------------

This guide assumes you have the following basic background:

*   A general understanding of the Internet and the World Wide Web ([WWW](https://developer.mozilla.org/en-US/docs/Glossary/World_Wide_Web)
    ).
*   Good working knowledge of HyperText Markup Language ([HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML)
    ).
*   Some programming experience. If you are new to programming, try one of the tutorials linked on the main page about [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    .

[Where to find JavaScript information](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#where_to_find_javascript_information)

--------------------------------------------------------------------------------------------------------------------------------------------------------

The JavaScript documentation on MDN includes the following:

*   [Dynamic scripting with JavaScript](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting)
     provides structured JavaScript guides for beginners and introduces basic concepts of programming and the Internet.
*   [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
     (this guide) provides an overview about the JavaScript language and its objects.
*   [JavaScript Reference](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference)
     provides detailed reference material for JavaScript.

[What is JavaScript?](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#what_is_javascript)

---------------------------------------------------------------------------------------------------------------------

JavaScript is a cross-platform, object-oriented scripting language used to make webpages interactive (e.g., having complex animations, clickable buttons, popup menus, etc.). There are also more advanced server side versions of JavaScript such as Node.js, which allow you to add more functionality to a website than downloading files (such as realtime collaboration between multiple computers). Inside a host environment (for example, a web browser), JavaScript can be connected to the objects of its environment to provide programmatic control over them.

JavaScript contains a standard library of objects, such as `Array`, `Map`, and `Math`, and a core set of language elements such as operators, control structures, and statements. Core JavaScript can be extended for a variety of purposes by supplementing it with additional objects; for example:

*   _Client-side JavaScript_ extends the core language by supplying objects to control a browser and its _Document Object Model_ (DOM). For example, client-side extensions allow an application to place elements on an HTML form and respond to user events such as mouse clicks, form input, and page navigation.
*   _Server-side JavaScript_ extends the core language by supplying objects relevant to running JavaScript on a server. For example, server-side extensions allow an application to communicate with a database, provide continuity of information from one invocation to another of the application, or perform file manipulations on a server.

This means that in the browser, JavaScript can change the way the webpage (DOM) looks. And, likewise, Node.js JavaScript on the server can respond to custom requests sent by code executed in the browser.

[JavaScript and Java](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#javascript_and_java)

----------------------------------------------------------------------------------------------------------------------

JavaScript and Java are similar in some ways but fundamentally different in some others. The JavaScript language resembles Java but does not have Java's static typing and strong type checking. JavaScript follows most Java expression syntax, naming conventions and basic control-flow constructs which was the reason why it was renamed from LiveScript to JavaScript.

In contrast to Java's compile-time system of classes built by declarations, JavaScript supports a runtime system based on a small number of data types representing numeric, Boolean, and string values. JavaScript has a prototype-based object model instead of the more common class-based object model. The prototype-based model provides dynamic inheritance; that is, what is inherited can vary for individual objects. JavaScript also supports functions without any special declarative requirements. Functions can be properties of objects, executing as loosely typed methods.

JavaScript is a very free-form language compared to Java. You do not have to declare all variables, classes, and methods. You do not have to be concerned with whether methods are public, private, or protected, and you do not have to implement interfaces. Variables, parameters, and function return types are not explicitly typed.

Java is a class-based programming language designed for fast execution and type safety. Type safety means, for instance, that you can't cast a Java integer into an object reference or access private memory by corrupting the Java bytecode. Java's class-based model means that programs consist exclusively of classes and their methods. Java's class inheritance and strong typing generally require tightly coupled object hierarchies. These requirements make Java programming more complex than JavaScript programming.

In contrast, JavaScript descends in spirit from a line of smaller, dynamically typed languages such as HyperTalk and dBase. These scripting languages offer programming tools to a much wider audience because of their easier syntax, specialized built-in functionality, and minimal requirements for object creation.

| JavaScript | Java |
| --- | --- |
| Object-oriented. No distinction between types of objects. Inheritance is through the prototype mechanism, and properties and methods can be added to any object dynamically. | Class-based. Objects are divided into classes and instances with all inheritance through the class hierarchy. Classes and instances cannot have properties or methods added dynamically. |
| Variable data types are not declared (dynamic typing, loosely typed). | Variable data types must be declared (static typing, strongly typed). |
| Cannot automatically write to hard disk. | Can automatically write to hard disk. |

[JavaScript and the ECMAScript specification](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#javascript_and_the_ecmascript_specification)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

JavaScript is standardized at [Ecma International](https://ecma-international.org/ "External link (opens in new tab)")
 — the European association for standardizing information and communication systems (ECMA was formerly an acronym for the European Computer Manufacturers Association) to deliver a standardized, international programming language based on JavaScript. This standardized version of JavaScript, called ECMAScript, behaves the same way in all applications that support the standard. Companies can use the open standard language to develop their implementation of JavaScript. The ECMAScript standard is documented in the ECMA-262 specification.

The ECMA-262 standard is also approved by the [ISO](https://www.iso.org/home.html "External link (opens in new tab)")
 (International Organization for Standardization) as ISO-16262. You can also find the specification on [the Ecma International website](https://ecma-international.org/publications-and-standards/standards/ecma-262/ "External link (opens in new tab)")
. The ECMAScript specification does not describe the Document Object Model (DOM), which is standardized by the [World Wide Web Consortium (W3C)](https://www.w3.org/ "External link (opens in new tab)")
 and/or [WHATWG (Web Hypertext Application Technology Working Group)](https://whatwg.org/ "External link (opens in new tab)")
. The DOM defines the way in which HTML document objects are exposed to your script. To get a better idea about the different technologies that are used when programming with JavaScript, consult the article [JavaScript technologies overview](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/JavaScript_technologies_overview)
.

### [JavaScript documentation versus the ECMAScript specification](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#javascript_documentation_versus_the_ecmascript_specification)

The ECMAScript specification is a set of requirements for implementing ECMAScript. It is useful if you want to implement standards-compliant language features in your ECMAScript implementation or engine (such as SpiderMonkey in Firefox, or V8 in Chrome).

The ECMAScript document is _not_ intended to help script programmers. Use the JavaScript documentation for information when writing scripts.

The ECMAScript specification uses terminology and syntax that may be unfamiliar to a JavaScript programmer. Although the description of the language may differ in ECMAScript, the language itself remains the same. JavaScript supports all functionality outlined in the ECMAScript specification.

The JavaScript documentation describes aspects of the language that are appropriate for a JavaScript programmer.

[Getting started with JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#getting_started_with_javascript)

----------------------------------------------------------------------------------------------------------------------------------------------

To get started with JavaScript, all you need is a modern web browser. Recent versions of [Firefox](https://www.firefox.com/en-US/ "External link (opens in new tab)")
, [Chrome](https://www.google.com/chrome/index.html "External link (opens in new tab)")
, [Microsoft Edge](https://explore.microsoft.com/en-us/edge "External link (opens in new tab)")
, and [Safari](https://www.apple.com/safari/ "External link (opens in new tab)")
 all support the features discussed in this guide.

A very useful tool for exploring JavaScript is the JavaScript Console (sometimes called the Web Console, or just the console): this is a tool which enables you to enter JavaScript and run it in the current page.

The screenshots here show the [Firefox Web Console](https://firefox-source-docs.mozilla.org/devtools-user/web_console/ "External link (opens in new tab)")
, but all modern browsers ship with a console that works in a similar way.

### [Opening the console](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#opening_the_console)

The exact instructions for opening the console vary from one browser to another:

*   [Opening the console in Firefox](https://firefox-source-docs.mozilla.org/devtools-user/web_console/#opening-the-web-console "External link (opens in new tab)")
    
*   [Opening the console in Chrome](https://developer.chrome.com/docs/devtools/open "External link (opens in new tab)")
    
*   [Opening the console in Microsoft Edge](https://learn.microsoft.com/en-us/microsoft-edge/devtools/console/ "External link (opens in new tab)")
    

### [Entering and running JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#entering_and_running_javascript)

The console appears at the bottom of the browser window. Along the bottom of the console is an input line that you can use to enter JavaScript, and the output appears in the panel above:

![A browser window with the web console open at the bottom, containing two lines of input and output. Text can be entered below that.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction/2019-04-04_00-15-29.png)

The console works the exact same way as `eval`: the last expression entered is returned. For the sake of simplicity, it can be imagined that every time something is entered into the console, it is actually surrounded by `console.log` around `eval`, like so:

### [Multi-line input in the console](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#multi-line_input_in_the_console)

By default, if you press Enter (or Return, depending on your keyboard) after entering a line of code, then the string you typed is executed. To enter multi-line input:

*   If the string you typed was incomplete (for example, you typed `function foo() {`) then the console will treat Enter as a line break, and let you type another line.
*   If you hold down Shift while pressing Enter, then the console will treat this as a line break, and let you type another line.
*   In Firefox only, you can activate [multi-line input mode](https://firefox-source-docs.mozilla.org/devtools-user/web_console/the_command_line_interpreter/index.html#multi-line-mode "External link (opens in new tab)")
    , in which you can enter multiple lines in a mini-editor, then run the whole thing when you are ready.

To get started with writing JavaScript, open the console, copy the following code, and paste it in at the prompt:

Press Enter to watch it unfold in your browser!

[What's next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction#whats_next)

-----------------------------------------------------------------------------------------------------

In the following pages, this guide introduces you to the JavaScript syntax and language features, so that you will be able to write more complex applications.

But for now, remember to always include the `(function(){"use strict";` before your code, and add `})();` to the end of your code. The [strict mode](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)
 and [IIFE](https://developer.mozilla.org/en-US/docs/Glossary/IIFE)
 articles explain what those do, but for now they can be thought of as doing the following:

1.  Prevent semantics in JavaScript that trip up beginners.
2.  Prevent code snippets executed in the console from interacting with one another (e.g., having something created in one console execution being used for a different console execution).

*   [Previous](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
    
*   [Next](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Grammar_and_types)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 8, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Introduction/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/javascript/guide/introduction/index.md?plain=1 "Folder: en-us/web/javascript/guide/introduction (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FIntroduction&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fjavascript%2Fguide%2Fintroduction%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FJavaScript%2FGuide%2FIntroduction%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fjavascript%2Fguide%2Fintroduction%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fafcdfa050626bb7eb05ee693df8997020db9ff2e%0A*+Document+last+modified%3A+2026-07-08T23%3A28%3A09.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")