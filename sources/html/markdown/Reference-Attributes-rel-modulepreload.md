*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload#mdn-search)
    

`rel="modulepreload"` HTML attribute value
==========================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`modulepreload`** keyword, for the [`rel`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel)
 attribute of the [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 element, provides a declarative way to preemptively fetch a [module script](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules)
, parse and compile it, and store it in the document's module map for later execution.

Preloading allows modules and their dependencies to be downloaded early, and can also significantly reduce the overall download and processing time. This is because it allows pages to fetch modules in parallel, instead of sequentially as each module is processed and its dependencies are discovered. Note however that you can't just preload everything! What you choose to preload must be balanced against other operations that might then be starved, adversely affecting user experience.

Links with `rel="modulepreload"` are similar to those with [`rel="preload"`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/preload)
. The main difference is that `preload` just downloads the file and stores it in the cache, while `modulepreload` gets the module, parses and compiles it, and puts the results into the module map so that it is ready to execute.

When using `modulepreload` the fetch request mode is always [`cors`](https://developer.mozilla.org/en-US/docs/Web/API/Request/mode#cors)
, and the [`crossorigin`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin)
 property is used to determine the request [credential mode](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials)
. If `crossorigin` is set to [`anonymous`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#anonymous)
 or [`""`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#sect)
 (default), then the credentials mode is [`same-origin`](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials#same-origin)
, and user credentials such as cookies and authentication are only sent for requests with the `same-origin`. If `crossorigin` is set to [`use-credentials`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/crossorigin#use-credentials)
 then the credentials mode is [`include`](https://developer.mozilla.org/en-US/docs/Web/API/Request/credentials#include)
, and user credentials for both single- and cross-origin requests.

The [`as`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link#as)
 attribute is optional for links with `rel="modulepreload"`, and defaults to `"script"`. It can be set to `"script"`, `"style"`, `"json"`, `"text"`, or any script-like destination, such as `"audioworklet"`, `"paintworklet"`, `"serviceworker"`, `"sharedworker"`, or `"worker"`. The full set of allowed values is defined in the HTML spec's [module preload destination](https://html.spec.whatwg.org/multipage/links.html#module-preload-destination "External link (opens in new tab)")
 mapping. For the list of script-like destinations, refer to the [Fetch spec](https://fetch.spec.whatwg.org/#request-destination-script-like "External link (opens in new tab)")
. An [`Event`](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)
 named "error" is fired on the element if any other destination is used.

A browser _may_ additionally also choose to automatically fetch any dependencies of the module resource. Note however that this is a browser-specific optimization — the only approach to ensure that all browsers will try to preload a module's dependencies is to individually specify them! Further, the events named `load` or `error` fire immediately following success or failure of loading the _specified_ resources. If dependencies are automatically fetched, no additional events are fired in the main thread (although you might monitor additional requests in a service worker or on the server).

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload#examples)

--------------------------------------------------------------------------------------------------------------

Consider the [basic-modules](https://github.com/mdn/js-examples/tree/main/module-examples/basic-modules "External link (opens in new tab)")
 example ([live version](https://mdn.github.io/js-examples/module-examples/basic-modules/ "External link (opens in new tab)")
), introduced in the [JavaScript modules](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Modules#working_with_examples)
 guide.

This has a file structure as shown below, consisting of the top level module `main.js`, which statically imports two dependency modules `modules/canvas.js` and `modules/square.js` using the [`import` statement](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/import)
.

index.html
main.js
modules/
    canvas.js
    square.js

The HTML for the example below shows how `main.js` is fetched in a `<script>` element. Only after `main.js` has loaded does the browser discover and fetch the two dependency modules.

The HTML below updates the example to use `<link>` elements with `rel="modulepreload"` for the main file and each of the dependency modules. This is much faster because the three modules all start downloading asynchronously and in parallel before they are needed. By the time `main.js` has been parsed and its dependencies are known, they have already been fetched and downloaded.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# link-type-modulepreload](https://html.spec.whatwg.org/multipage/links.html#link-type-modulepreload) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload#see_also)

--------------------------------------------------------------------------------------------------------------

*   [Speculative loading](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Speculative_loading)
     for a comparison of `<link rel="modulepreload">` and other similar performance improvement features.
*   [Preloading modules](https://web.dev/articles/modulepreload "External link (opens in new tab)")
     on web.dev

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 5, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/rel/modulepreload/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/rel/modulepreload/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/rel/modulepreload (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Fmodulepreload&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Fmodulepreload%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Frel%2Fmodulepreload%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Frel%2Fmodulepreload%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F696a0436bb4dd20eb4d30ac3f1d4fc5140d1eee9%0A*+Document+last+modified%3A+2026-11-05T23%3A53%3A11.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")