*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#mdn-search)
    

Author fast-loading HTML pages
==============================

An optimized web page not only provides for a more responsive site for your visitors but also reduces the load on your web servers and internet connection. This can be crucial for high volume sites or sites which have a spike in traffic due to unusual circumstances such as breaking news stories. This article describes how to improve page load times based on common knowledge and experimentation.

Optimizing page load performance is not just for content which will be viewed by narrowband dial-up or mobile device visitors. It is just as important for broadband content and can lead to dramatic improvements even for your visitors with the fastest connections.

[Tips](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#tips)

-----------------------------------------------------------------------------------------------------

### [Reduce page weight](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#reduce_page_weight)

Page weight is by far the most important factor in page-load performance.

Reducing page weight through the elimination of unnecessary whitespace and comments, commonly known as minimization, and by moving inline script and CSS into external files, can improve download performance with minimal need for other changes in the page structure.

Tools such as [HTML Tidy](https://www.html-tidy.org/ "External link (opens in new tab)")
 can automatically strip leading whitespace and extra blank lines from valid HTML source. Other tools can "compress" JavaScript by reformatting the source or by obfuscating the source and replacing long identifiers with shorter versions.

### [Minimize the number of files](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#minimize_the_number_of_files)

Reducing the number of files referenced in a web page lowers the number of [HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP)
 connections required to download a page, thereby reducing the time for these requests to be sent, and for their responses to be received.

Depending on a browser's cache settings, it may send a request with the [`If-Modified-Since`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-Modified-Since)
 header for each referenced file, asking whether the file has been modified since the last time it was downloaded. Too much time spent querying the last modified time of the referenced files can delay the initial display of the web page, since the browser must check the modification time for each of these files, before rendering the page.

If you use background images a lot in your CSS, you can reduce the number of HTTP lookups needed by combining the images into one, known as an image sprite. Then you just apply the same image each time you need it for a background and adjust the x/y coordinates appropriately. This technique works best with elements that will have limited dimensions, and will not work for every use of a background image. However, the fewer HTTP requests and single image caching can help reduce page-load time.

### [Use a Content Delivery Network (CDN)](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#use_a_content_delivery_network_cdn)

For the purposes of this article, a CDN is a means to reduce the physical distance between your server and your visitor. As the distance between your server origin and visitor increases, the load times will increase. Suppose your website server is located in the United States and it has a visitor from India; the page load time will be much higher for the Indian visitor compared to a visitor from the US.

A CDN is a geographically distributed network of servers that work together to shorten the distance between the user and your website. CDNs store cached versions of your website and serve them to visitors via the network node closest to the user, thereby reducing [latency](https://developer.mozilla.org/en-US/docs/Web/Performance/Guides/Understanding_latency)
.

Further reading:

*   [Understanding CDNs](https://www.imperva.com/learn/performance/what-is-cdn-how-it-works/ "External link (opens in new tab)")
    

### [Reduce domain lookups](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#reduce_domain_lookups)

Since each separate domain costs time in a DNS lookup, the page load time will grow along with the number of separate domains appearing in CSS link(s) and JavaScript and image src(es).

This may not always be practical; however, you should always take care to use only the minimum necessary number of different domains in your pages.

### [Cache reused content](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#cache_reused_content)

Make sure that any content that can be cached, is cached, and with appropriate expiration times.

In particular, pay attention to the `Last-Modified` header. It allows for efficient page caching; by means of this header, information is conveyed to the user agent about the file it wants to load, such as when it was last modified. Most web servers automatically append the `Last-Modified` header to static pages (e.g., `.html`, `.css`), based on the last-modified date stored in the file system. With dynamic pages (e.g., `.php`, `.aspx`), this, of course, can't be done, and the header is not sent.

So, in particular, for pages which are generated dynamically, a little research on this subject is beneficial. It can be somewhat involved, but it will save a lot in page requests on pages which would normally not be cacheable.

More information:

1.  [HTTP Conditional Get for RSS Hackers](https://fishbowl.pastiche.org/2002/10/21/http_conditional_get_for_rss_hackers "External link (opens in new tab)")
    
2.  [HTTP 304: Not Modified](https://annevankesteren.nl/2005/05/http-304 "External link (opens in new tab)")
    
3.  [HTTP ETag on Wikipedia](https://en.wikipedia.org/wiki/HTTP_ETag "External link (opens in new tab)")
    
4.  [Caching in HTTP](https://www.w3.org/Protocols/rfc2616/rfc2616-sec13.html "External link (opens in new tab)")
    

### [Optimally order the components of the page](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#optimally_order_the_components_of_the_page)

Download page content first, along with any CSS or JavaScript that may be required for its initial display, so that the user gets the quickest apparent response during the page loading. This content is typically text, and can, therefore, benefit from text compression in transit, thus providing an even quicker response to the user.

Any dynamic features that require the page to complete loading before being used, should be initially disabled, and then only enabled after the page has loaded. This will cause the JavaScript to be loaded after the page contents, which will improve the overall appearance of the page load.

### [Reduce the number of inline scripts](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#reduce_the_number_of_inline_scripts)

Inline scripts can be expensive for page loading since the parser must assume that an inline script could modify the page structure while parsing is in progress. Reducing the use of inline scripts in general, and reducing the use of `document.write()` to output content in particular, can improve overall page loading. Use [DOM APIs to manipulate page content](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Scripting/DOM_scripting)
, rather than `document.write()`.

### [Use modern CSS and valid markup](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#use_modern_css_and_valid_markup)

Use of modern CSS reduces the amount of markup, can reduce the need for (spacer) images, in terms of layout, and can very often replace images of stylized text — that "cost" much more than the equivalent text-and-CSS.

Using valid markup has other advantages. First, browsers will have no need to perform error-correction when parsing the HTML (this is aside from the philosophical issue of whether to allow format variation in user input and then programmatically "correct" or normalize it; or whether, instead, to enforce a strict, no-tolerance input format).

Moreover, valid markup allows for the free use of other tools that can _pre-process_ your web pages. For example, [HTML Tidy](https://www.html-tidy.org/ "External link (opens in new tab)")
 can remove whitespace and optional ending tags; however, it will refuse to run on a page with serious markup errors.

### [Chunk your content](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#chunk_your_content)

Tables for layouts are a legacy method that should not be used anymore. Layouts utilizing [floats](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Floats)
, [positioning](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Positioning)
, [flexbox](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Flexbox)
, or [grids](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Grids)
 should be used instead.

Tables are still considered valid markup but should be used for displaying tabular data. To help the browser render your page quicker, you should use CSS methods such as [flexible box layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout)
 and [grid layout](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout)
 instead of nesting tables.

### [Minify and compress SVG assets](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#minify_and_compress_svg_assets)

SVG produced by most drawing applications often contains unnecessary metadata which can be removed. Configure your servers, apply gzip compression for SVG assets.

### [Minify and compress your images](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#minify_and_compress_your_images)

Large images cause your page to take more time to load. Consider compressing your images before adding them to your page, using compression features built into image-manipulation tools such as Photoshop, or using a specialized tool such as [Compress JPEG](https://compressjpeg.com/ "External link (opens in new tab)")
 or [Tiny PNG](https://tinypng.com/ "External link (opens in new tab)")
.

### [Specify sizes for images and tables](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#specify_sizes_for_images_and_tables)

If the browser can immediately determine the height and/or width of your images and tables, it will be able to display a web page without having to reflow the content. This not only speeds the display of the page but prevents annoying changes in a page's layout when the page completes loading. For this reason, `height` and `width` should be specified for images, whenever possible.

Tables should use the CSS selector: property combination:

and should specify widths of columns using the [`<col>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/col)
 and the [`<colgroup>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/colgroup)
 elements.

### [Use lazy loading for images](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#use_lazy_loading_for_images)

By default, images are loaded **eagerly**; that is, the image is fetched and rendered as soon as it's processed in the HTML. All eagerly loaded images are rendered before the window's [`load`](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event)
 event is sent. Switching to lazy loading of images tells the browser to hold off on loading images until they're about to be needed to draw the [visual viewport](https://developer.mozilla.org/en-US/docs/Glossary/Visual_Viewport)
.

To mark an image for lazy loading, specify its [`loading`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/img#loading)
 attribute with a value of `lazy`. With this set, the image will only be loaded when it's needed.

Note that lazily-loaded images may not be available when the `load` event is fired. You can determine if a given image is loaded by checking to see if the value of its Boolean [`complete`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLImageElement/complete "complete")
 property is `true`.

### [Choose your user-agent requirements wisely](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#choose_your_user-agent_requirements_wisely)

To achieve the greatest improvements in page design, make sure that reasonable user-agent requirements are specified for projects. Do not require your content to appear pixel-perfect in all browsers, especially not in down-version browsers.

Ideally, your basic minimum requirements should be based on the consideration of modern browsers that support the relevant standards. This can include recent versions of Firefox, Google Chrome, Opera, and Safari.

Note, however, that many of the tips listed in this article are common-sense techniques which apply to any user agent, and can be applied to any web page, regardless of browser-support requirements.

### [Use async and defer, if possible](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#use_async_and_defer_if_possible)

Make the JavaScript scripts such that they are compatible with both the [async](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script#attributes)
 and the [defer](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script#attributes)
 attributes, and use [async](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script#attributes)
 whenever possible, especially if you have multiple script elements.

With that, the page can stop rendering while JavaScript is still loading. Otherwise, the browser will not render anything that is after the script elements that do not have these attributes.

Note: Even though these attributes do help a lot the first time a page is loaded, you should use them but not assume they will work in all browsers. If you already follow all JavaScript best practices, there is no need to change your code.

[Example page structure](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#example_page_structure)

-----------------------------------------------------------------------------------------------------------------------------------------

*   ``[`<html>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/html) ``
    *   ``[`<head>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/head) ``
        
        *   ``[`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link) ``
            
            CSS files required for page appearance. Minimize the number of files for performance while keeping unrelated CSS in separate files for maintenance.
            
        *   ``[`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script) ``
            
            JavaScript files for functions **required** during the loading of the page, but not any interaction related JavaScript that can only run after page loads.
            
            Minimize the number of files for performance while keeping unrelated JavaScript in separate files for maintenance.
            
    *   ``[`<body>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/body) ``
        
        User visible page content in small chunks (``[`<header>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/header) ``/ ``[`<main>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/main) /`` ``[`<table>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/table) ``) that can be displayed without waiting for the full page to download.
        
        *   ``[`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script) ``
            
            Any scripts which will be used to perform interactivity. Interaction scripts typically can only run after the page has completely loaded and all necessary objects have been initialized. There is no need to load these scripts before the page content. That only slows down the initial appearance of the page load.
            
            Minimize the number of files for performance while keeping unrelated JavaScript in separate files for maintenance.
            

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages#see_also)

-------------------------------------------------------------------------------------------------------------

*   Book: ["Speed Up Your Site" by Andy King](https://www.websiteoptimization.com/ "External link (opens in new tab)")
    
*   [Learn performance](https://web.dev/learn/performance "External link (opens in new tab)")
     via web.dev (2023)
*   Tools for analyzing and optimizing performance: [Google PageSpeed Tools](https://developers.google.com/speed "External link (opens in new tab)")
     and [PageSpeed Insights](https://pagespeed.web.dev/ "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/How_to/Author_fast-loading_HTML_pages/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/how_to/author_fast-loading_html_pages/index.md?plain=1 "Folder: en-us/web/html/how_to/author_fast-loading_html_pages (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FHow_to%2FAuthor_fast-loading_HTML_pages&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Fhow_to%2Fauthor_fast-loading_html_pages%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FHow_to%2FAuthor_fast-loading_HTML_pages%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Fhow_to%2Fauthor_fast-loading_html_pages%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")