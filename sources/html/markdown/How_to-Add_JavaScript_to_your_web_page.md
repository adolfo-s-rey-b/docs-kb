*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_JavaScript_to_your_web_page#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_JavaScript_to_your_web_page#mdn-search)
    

Add JavaScript to your web page
===============================

Take your webpages to the next level by harnessing JavaScript. Learn in this article how to trigger JavaScript right from your HTML documents.

|     |     |
| --- | --- |
| Prerequisites: | You need to be familiar with how to [create a basic HTML document](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website)<br>. |
| Objective: | Learn how to trigger JavaScript in your HTML file, and learn the most important best practices for keeping JavaScript accessible. |

[About JavaScript](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_JavaScript_to_your_web_page#about_javascript)

------------------------------------------------------------------------------------------------------------------------------

[JavaScript](https://developer.mozilla.org/en-US/docs/Glossary/JavaScript)
 is a programming language mostly used client-side to make webpages interactive. You _can_ create amazing webpages without JavaScript, but JavaScript opens up a whole new level of possibilities.

**Note:** In this article we're going over the HTML code you need to make JavaScript take effect. If you want to learn JavaScript itself, you can start with our [JavaScript basics](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Your_first_website/Adding_interactivity)
 article. If you already know something about JavaScript or if you have a background with other programming languages, we suggest you jump directly into our [JavaScript Guide](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
.

[How to trigger JavaScript from HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_JavaScript_to_your_web_page#how_to_trigger_javascript_from_html)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------

Within a browser, JavaScript doesn't do anything by itself. You run JavaScript from inside your HTML webpages. To call JavaScript code from within HTML, you need the [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 element. There are two ways to use `script`, depending on whether you're linking to an external script or embedding a script right in your webpage.

### [Linking an external script](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_JavaScript_to_your_web_page#linking_an_external_script)

Usually, you'll be writing scripts in their own .js files. If you want to execute a .js script from your webpage, just use [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 with an `src` attribute pointing to the script file, using its [URL](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_URL)
:

### [Writing JavaScript within HTML](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_JavaScript_to_your_web_page#writing_javascript_within_html)

You may also add JavaScript code between `<script>` tags rather than providing an `src` attribute.

That's convenient when you just need a small bit of JavaScript, but if you keep JavaScript in separate files you'll find it easier to

*   focus on your work
*   write self-sufficient HTML
*   write structured JavaScript applications

**Note:** For both inline scripts and external scripts without the [`defer`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script#defer)
 or [`async`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script#async)
 attributes, the script is executed immediately when the browser encounters the `<script>` element while parsing the HTML. This means that the script cannot access any HTML elements that appear later in the document. To access such elements, consider moving the script to the end of the document body (just before the closing `</body>` tag), or use the `defer` attribute on external scripts.

[Use scripting accessibly](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_JavaScript_to_your_web_page#use_scripting_accessibly)

----------------------------------------------------------------------------------------------------------------------------------------------

Accessibility is a major issue in any software development. JavaScript can make your website more accessible if you use it wisely, or it can become a disaster if you use scripting without care. To make JavaScript work in your favor, it's worth knowing about certain best practices for adding JavaScript:

*   **Make all content available as (structured) text.** Rely on HTML for your content as much as possible. For example, if you've implemented a nice JavaScript progress bar, make sure to supplement it with matching text percentages inside the HTML. Likewise, your drop-down menus should be structured as [unordered lists](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Lists#unordered_lists)
     of [links](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Creating_links)
    .
    
*   **Make all functionality accessible from the keyboard.**
    
    *   Let users Tab through all controls (e.g., links and form input) in a logical order.
    *   If you use pointer events (like mouse events or touch events), duplicate the functionality with keyboard events.
    *   Test your site using a keyboard only.
*   **Don't set nor even guess time limits.** It takes extra time to navigate with the keyboard or hear content read out. You can hardly ever predict just how long it will take for users or browsers to complete a process (especially asynchronous actions such as loading resources).
    
*   **Keep animations subtle and brief with no flashing.** Flashing is annoying and can [cause seizures](https://www.w3.org/TR/UNDERSTANDING-WCAG20/seizure-does-not-violate.html "External link (opens in new tab)")
    . Additionally, if an animation lasts more than a couple seconds, give the user a way to cancel it.
    
*   **Let users initiate interactions.** That means, don't update content, redirect, or refresh automatically. Don't use carousels or display popups without warning.
    
*   **Have a plan B for users without JavaScript.** People may have JavaScript turned off to improve speed and security, and users often face network issues that prevent loading scripts. Moreover, third-party scripts (ads, tracking scripts, browser extensions) might break your scripts.
    
    *   At a minimum, leave a short message with [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript)
         like this: `<noscript>To use this site, please enable JavaScript.</noscript>`
    *   Ideally, replicate the JavaScript functionality with HTML and server-side scripting when possible.
    *   If you're only looking for simple visual effects, CSS can often get the job done even more intuitively.
    *   _Since almost everybody **does** have JavaScript enabled, `<noscript>` is no excuse for writing inaccessible scripts._

[Learn more](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_JavaScript_to_your_web_page#learn_more)

------------------------------------------------------------------------------------------------------------------

*   [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
    
*   [`<noscript>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/noscript)
    
*   [Writing JavaScript with Accessibility in Mind](https://www.sitepoint.com/writing-javascript-with-accessibility-in-mind/ "External link (opens in new tab)")
     by Manuel Matuzovic (2017)
*   [Accessibility guidelines from W3C](https://w3c.github.io/wcag/guidelines/22/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 11, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Add_JavaScript_to_your_web_page/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/how_to/add_javascript_to_your_web_page/index.md?plain=1 "Folder: en-us/web/html/how_to/add_javascript_to_your_web_page (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FHow_to%2FAdd_JavaScript_to_your_web_page&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fhow_to%2Fadd_javascript_to_your_web_page%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FHow_to%2FAdd_JavaScript_to_your_web_page%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fhow_to%2Fadd_javascript_to_your_web_page%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F116577234db1d6275c74a8bb879fce54d944f4ed%0A*+Document+last+modified%3A+2025-09-11T16%3A42%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")