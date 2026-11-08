*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#mdn-search)
    

`integrity` HTML attribute
==========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since April 2018.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`integrity`** attribute provides a mechanism for a developer to assert that a linked script or stylesheet must have a particular content. The browser will check that the resource does in fact have that content, and refuse to load the resource if it does not.

This is a defense against a [supply-chain attack](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Supply_chain_attacks)
 in which an attacker gets access to the domain that serves the script or stylesheet, and changes the expected resource for a malicious one.

[Description](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#description)

------------------------------------------------------------------------------------------------------------

The attribute can be applied to [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 or [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 elements only.

The attribute consists of one or more components, each of which consists of:

*   An identifier for a [cryptographic hash function](https://developer.mozilla.org/en-US/docs/Glossary/Hash_function)
    . Three hash functions are supported. In increasing order of strength, these are: SHA-256, SHA-384, and SHA-512.
*   The result of hashing the resource contents using the specified hash function.

When the browser downloads a resource with the `integrity` attribute set, it will first select the set of hashes that were generated using the strongest hash function present. That is, if the attribute contains values generated with SHA-256 and SHA-384, it will only use the hashes generated using SHA-384.

The browser will then calculate the hash of the resource contents using the specified function, and compare the result with all the specified values: if the actual value matches any of the specified values, then the browser will load the resource, otherwise it will refuse to load the resource.

For more details, see our guide to [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity)
.

[Values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#values)

--------------------------------------------------------------------------------------------------

The value of this attribute consists of a whitespace-separated list of components, each of which has one of the following forms:

*   `sha256-HASH_VALUE`
*   `sha384-HASH_VALUE`
*   `sha512-HASH_VALUE`

In each case, the part preceding `-` identifies the [hash function](https://developer.mozilla.org/en-US/docs/Glossary/Hash_function)
 used, and `HASH_VALUE` is the [base64](https://developer.mozilla.org/en-US/docs/Glossary/Base64)
 encoding of the result of hashing the resource using the specified hash function.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#examples)

------------------------------------------------------------------------------------------------------

### [Including different hash functions](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#including_different_hash_functions)

The following [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 element includes an `integrity` attribute containing three values, one calculated using SHA-256, one calculated using SHA-384, and one calculated using SHA-512.

The browser will select the value that was calculated using the strongest algorithm that the browser supports. Since all modern browsers support SHA-512, this means that the browser will select the `sha512-` value. It will hash the file contents using SHA-512 and compare the result with the `sha512-` value, and load the file only if they match.

In this case providing multiple values enables a website to work with browsers that may not support all the hash functions.

Note that in this and subsequent examples, we've truncated the example hash values, for brevity.

### [Including different hash values](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#including_different_hash_values)

The following [`<script>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/script)
 element includes an `integrity` attribute containing two different values, both calculated using the SHA-512 algorithm. These different values reflect alternative contents for the linked file.

If the SHA-512 hash of the linked file matches either of the given values, then the browser will load it.

This enables the server at `cdn.example.com` to respond with one of two versions of the file.

### [Including `integrity` on `<link>` elements](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#including_integrity_on_link_elements)

The following [`<link>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/link)
 element loads a stylesheet and includes an `integrity` attribute containing six values, reflecting two possible contents for the linked file, each calculated using three different hash functions.

The browser will select the set of values that were calculated using the strongest hash function that it supports: in modern browsers, this will be the two `sha512-` values.

It will then calculate the hash of the downloaded file using SHA-512, and compare the result with both the `sha512-` values: if either of them match, then the browser will load the resource.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#specifications)

------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# attr-link-integrity](https://html.spec.whatwg.org/multipage/semantics.html#attr-link-integrity) |
| [HTML  <br>\# attr-script-integrity](https://html.spec.whatwg.org/multipage/scripting.html#attr-script-integrity) |
| [Subresource Integrity  <br>\# the-integrity-attribute](https://w3c.github.io/webappsec-subresource-integrity/#the-integrity-attribute) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#browser_compatibility)

--------------------------------------------------------------------------------------------------------------------------------

### [html.elements.link.integrity](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#html.elements.link.integrity)

### [html.elements.script.integrity](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#html.elements.script.integrity)

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity#see_also)

------------------------------------------------------------------------------------------------------

*   [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Defenses/Subresource_Integrity)
    
*   [Supply chain attacks](https://developer.mozilla.org/en-US/docs/Web/Security/Attacks/Supply_chain_attacks)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Attributes/integrity/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/attributes/integrity/index.md?plain=1 "Folder: en-us/web/html/reference/attributes/integrity (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fintegrity&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fintegrity%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FAttributes%2Fintegrity%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Fattributes%2Fintegrity%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb50ed7ac1c2ca21b4b5cfb594474a17da3f2e6c2%0A*+Document+last+modified%3A+2026-04-20T12%3A09%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")