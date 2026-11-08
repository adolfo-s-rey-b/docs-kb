*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#mdn-search)
    

`<meta http-equiv>` HTML attribute
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`http-equiv`** attribute of the [`<meta>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta)
 element allows you to provide processing instructions for the browser as if the response that returned the document included certain HTTP headers. The metadata is _document-level metadata_ that applies to the whole page.

When a `<meta>` element has an `http-equiv` attribute, a [`content`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/content)
 attribute defines the corresponding `http-equiv` value. For example, the following `<meta>` tag tells the browser to refresh the page after 5 minutes:

[Value](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#value)

----------------------------------------------------------------------------------------------------

Only a subset of the HTTP headers are supported as `http-equiv` values. These include:

[`content-language`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#content-language)

Sets a default language for the document used by assistive technologies or styling by the browser. Similar to the [`Content-Language`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Language)
 HTTP header. Use the [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 attribute instead.

[`content-type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#content-type)

Declares the document's [media type (MIME type)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/MIME_types)
 and character encoding. The `content` attribute must be `"text/html; charset=utf-8"` if specified. This is equivalent to a `<meta>` element with the [`charset`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta#charset)
 attribute specified and carries the same restriction on placement within the document. Can only be used in documents served with a `text/html` media type — not in documents served with an XML (`application/xml` or `application/xhtml+xml`) type. See the [`Content-Type`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type)
 HTTP header.

[`content-security-policy`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#content-security-policy)

Allows page authors to define a content security policy (CSP) for the current page, typically to specify allowed origins and script endpoints to guard against cross-site scripting attacks. See the [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy)
 HTTP header.

[`default-style`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#default-style)

Sets the name of the default [CSS style sheet](https://developer.mozilla.org/en-US/docs/Web/CSS)
 set.

[`refresh`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#refresh)

Equivalent to the [`Refresh`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Refresh)
 HTTP header. This instruction specifies:

*   The number of seconds until the page should be reloaded if the `content` attribute is a non-negative integer.
*   The number of seconds until the page should redirect to another URL if the `content` attribute is a non-negative integer followed by `;url=` and a valid URL.

The timer starts when the page is _completely loaded_, which is after the [`load`](https://developer.mozilla.org/en-US/docs/Web/API/Window/load_event "load")
 and [`pageshow`](https://developer.mozilla.org/en-US/docs/Web/API/Window/pageshow_event "pageshow")
 events have both fired. See [Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#accessibility_concerns)
 for more information.

[`set-cookie`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#set-cookie)

Sets a cookie for the document. Browsers now ignore this pragma; use the [`Set-Cookie`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie)
 HTTP response header or [`document.cookie`](https://developer.mozilla.org/en-US/docs/Web/API/Document/cookie)
 instead.

[`x-ua-compatible`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#x-ua-compatible)

Used by legacy versions of the now-retired [Microsoft Internet Explorer](https://developer.mozilla.org/en-US/docs/Glossary/Microsoft_Internet_Explorer)
 so that it more closely followed specified behavior. If specified, the `content` attribute must have the value `"IE=edge"`. User agents now ignore this pragma. The name derives from the `X-UA-Compatible` HTTP header.

**Warning:** Some browsers process additional headers that are not listed above. Since unrecognized headers or invalid values are ignored, this can lead to inconsistent behavior across browser implementations. In particular, **Do not set other security headers** using `<meta http-equiv=`, as this can lead to a false sense of security!

[Accessibility concerns](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#accessibility_concerns)

--------------------------------------------------------------------------------------------------------------------------------------

Pages set with a `http-equiv="Refresh"` value run the risk of having the refresh interval being too short. People navigating with the aid of assistive technology such as a screen reader may be unable to read through and understand the page's content before being automatically redirected. Abrupt, unannounced page updates may also be disorienting for people experiencing low vision conditions.

*   [MDN Understanding WCAG, Guideline 2.2 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Operable#guideline_2.2_%E2%80%94_enough_time_provide_users_enough_time_to_read_and_use_content)
    
*   [MDN Understanding WCAG, Guideline 3.2 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Understandable#guideline_3.2_%E2%80%94_predictable_make_web_pages_appear_and_operate_in_predictable_ways)
    
*   [Understanding Success Criterion 2.2.1 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/time-limits-required-behaviors.html "External link (opens in new tab)")
    
*   [Understanding Success Criterion 2.2.4 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/time-limits-postponed.html "External link (opens in new tab)")
    
*   [Understanding Success Criterion 3.2.5 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/consistent-behavior-no-extreme-changes-context.html "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#examples)

----------------------------------------------------------------------------------------------------------

### [Disable unsafe inline code and only allow HTTPS resources](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#disable_unsafe_inline_code_and_only_allow_https_resources)

This HTML `<meta>` element sets the default CSP to only allow resource loading (images, fonts, scripts, etc.) over HTTPS. Because the `unsafe-inline` and `unsafe-eval` directives are not set, inline scripts will be blocked:

The same restrictions can be applied using the HTTP [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy)
 header:

### [Setting a page redirect](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#setting_a_page_redirect)

The following example uses `http-equiv="refresh"` to direct the browser to perform a redirect. The `content="3;url=https://www.mozilla.org"` attribute will redirect page to `https://www.mozilla.org` after 3 seconds:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-meta-http-equiv](https://html.spec.whatwg.org/multipage/semantics.html#attr-meta-http-equiv) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv#see_also)

----------------------------------------------------------------------------------------------------------

*   [`<meta name="referrer">`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/referrer)
    
*   [Metadata: the `<meta>` element](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Structuring_content/Webpage_metadata#metadata_the_meta_element)
    
*   [Preventing attacks using `<meta>`](https://almanac.httparchive.org/en/2022/security#preventing-attacks-using-meta "External link (opens in new tab)")
     httparchive.org (2022)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/http-equiv/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/meta/http-equiv/index.md?plain=1 "Folder: en-us/web/html/reference/elements/meta/http-equiv (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fhttp-equiv&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fhttp-equiv%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmeta%2Fhttp-equiv%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmeta%2Fhttp-equiv%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb50ed7ac1c2ca21b4b5cfb594474a17da3f2e6c2%0A*+Document+last+modified%3A+2026-04-20T12%3A09%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")