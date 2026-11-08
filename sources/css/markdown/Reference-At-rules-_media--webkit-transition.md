*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition#mdn-search)
    

`-webkit-transition` CSS media feature
======================================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**Note:** All browsers support the [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition#browser_compatibility)
 property without vendor prefixes. Only WebKit (Safari), and not Chromium, based browsers support the `-webkit-transition` media feature. No browsers support `transition` without the prefix as a media query (though some browsers do support - [`-webkit-transform-3d`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d)
). Use the [`@supports (transition)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 feature query instead.

The **`-webkit-transition`** Boolean non-standard [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [media feature](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media#media_features)
 is a [WebKit extension](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_extensions)
 whose value is `true` if the browsing context supports [CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions)
.

Apple has [a description in Safari CSS Reference](https://developer.apple.com/library/archive/documentation/AppleApplications/Reference/SafariCSSRef/Articles/OtherStandardCSS3Features.html#//apple_ref/doc/uid/TP40007601-SW3 "External link (opens in new tab)")
; this is now called `transition` there.

**Note:** You should not use this media feature; it was never specified, has never been widely implemented, and has been [removed from most browsers](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition#browser_compatibility)
. Use a [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 feature query instead.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition#syntax)

---------------------------------------------------------------------------------------------------------------

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition#examples)

-------------------------------------------------------------------------------------------------------------------

### [Use @supports instead](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition#use_supports_instead)

Do not use the `-webkit-transition` media feature. Instead, test for transition support using the CSS [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
, like this:

### [Obsolete example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition#obsolete_example)

Before this became obsolete, you could use `-webkit-transition` in your CSS like this:

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition#specifications)

-------------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition#see_also)

-------------------------------------------------------------------------------------------------------------------

*   [`-webkit-transform-3d`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-3d)
    
*   [`-webkit-transform-2d`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transform-2d)
    
*   [`-webkit-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-animation)
    
*   [`transition`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/transition)
     and [using CSS transitions](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Transitions/Using)
    
*   [`@media`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media)
     and [Using media queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using)
    
*   [`@supports`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@supports)
     and [using feature queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Using_feature_queries)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/-webkit-transition/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@media/-webkit-transition/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@media/-webkit-transition (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2F-webkit-transition&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2F-webkit-transition%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40media%2F-webkit-transition%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40media%2F-webkit-transition%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")