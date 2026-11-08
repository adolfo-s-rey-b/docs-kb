*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/nonce#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/nonce#mdn-search)
    

`nonce` HTML global attribute
=============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since May 2022.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/nonce#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`nonce`** [global attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
 is a content attribute defining a cryptographic [nonce](https://developer.mozilla.org/en-US/docs/Glossary/Nonce)
 ("number used once") which can be used by [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
 to determine whether or not a given fetch will be allowed to proceed for a given element.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/nonce#description)

---------------------------------------------------------------------------------------------------------------

The `nonce` attribute is useful to allowlist specific elements, such as a particular inline script or style elements. It can help you to avoid using the [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
 `unsafe-inline` directive, which would allowlist _all_ inline scripts or styles.

**Note:** Only use `nonce` for cases where you have no way around using unsafe inline script or style contents. If you don't need `nonce`, don't use it. If your script is static, you could also use a CSP hash instead. (See usage notes on [unsafe inline script](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/script-src#unsafe_inline_script)
.) Always try to take full advantage of [CSP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
 protections and avoid nonces or unsafe inline scripts whenever possible.

### [Using nonce to allowlist a <script> element](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/nonce#using_nonce_to_allowlist_a_script_element)

There are a few steps involved to allowlist an inline script using the nonce mechanism:

#### Generating values

From your web server, generate a random base64-encoded string of at least 128 bits of data from a cryptographically secure random number generator. Nonces should be generated differently each time the page loads (nonce only once!). For example, in nodejs:

#### Allowlisting inline script

The nonce generated on your backend code should now be used for the inline script that you'd like to allowlist:

#### Sending a nonce with a CSP header

Finally, you'll need to send the nonce value in a [`Content-Security-Policy`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy)
 header (prepend `nonce-`):

### [Accessing nonces and nonce hiding](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/nonce#accessing_nonces_and_nonce_hiding)

For security reasons, the `nonce` content attribute is hidden (an empty string will be returned).

The [`nonce`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/nonce)
 property is the only way to access nonces:

Nonce hiding helps prevent attackers from exfiltrating nonce data via mechanisms that can grab data from content attributes like this:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/nonce#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-nonce](https://html.spec.whatwg.org/multipage/urls-and-fetching.html#attr-nonce) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/nonce#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/nonce#see_also)

---------------------------------------------------------------------------------------------------------

*   [`HTMLElement.nonce`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/nonce)
    
*   [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP)
    
*   CSP: [`script-src`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Security-Policy/script-src)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/nonce/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/global_attributes/nonce/index.md?plain=1 "Folder: en-us/web/html/reference/global_attributes/nonce (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fnonce&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fnonce%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FGlobal_attributes%2Fnonce%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fglobal_attributes%2Fnonce%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F9c70c6ff09189cad43d40e241fbd2fe67349c3c2%0A*+Document+last+modified%3A+2026-04-17T01%3A02%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")