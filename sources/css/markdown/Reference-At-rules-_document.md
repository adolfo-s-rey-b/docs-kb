*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#mdn-search)
    

`@document` CSS at-rule
=======================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`@document`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 restricts the style rules contained within it based on the URL of the document. It is designed primarily for user-defined style sheets (see [userchrome.org](https://www.userchrome.org/ "External link (opens in new tab)")
 for more information), though it can be used on author-defined style sheets, too.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#syntax)

-----------------------------------------------------------------------------------------------

css

    @document url("https://www.example.com/")
    {
      h1 {
        color: green;
      }
    }
    

An `@document` rule can specify one or more matching functions. If any of the functions apply to a given URL, the rule will take effect on that URL. The functions available are:

[`url()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#url)

Matches an exact URL.

[`url-prefix()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#url-prefix)

Matches if the document URL starts with the value provided.

[`domain()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#domain)

Matches if the document URL is on the domain provided (or a subdomain of it).

[`media-document()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#media-document)

Matches the media according to the string in parameter, one of `video`, `image`, `plugin` or `all`.

[`regexp()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#regexp)

Matches if the document URL is matched by the [regular expression](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions)
 provided. The expression must match the entire URL.

The values provided to the `url()`, `url-prefix()`, `domain()`, and `media-document()` functions can be optionally enclosed by single or double quotes. The values provided to the `regexp()` function _must_ be enclosed in quotes.

Escaped values provided to the `regexp()` function must additionally be escaped from the CSS. For example, a `.` (period) matches any character in regular expressions. To match a literal period, you would first need to escape it using regular expression rules (to `\.`), then escape that string using CSS rules (to `\\.`).

`@document` is currently only supported in Firefox; if you wanted to replicate using such functionality in your own non-Firefox browser, you could try using [this polyfill](https://github.com/An-Error94/Handy-Scripts/tree/master/%40document-polyfill "External link (opens in new tab)")
 by @An-Error94, which uses a combination of a user script, [data-\* attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*)
, and [attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
.

**Note:** There is a -moz-prefixed version of this property — `@-moz-document`. This has been limited to use only in user and UA sheets in Firefox 59 in Nightly and Beta — an experiment designed to mitigate potential CSS injection attacks (See [Firefox bug 1035091](https://bugzil.la/1035091 "External link (opens in new tab)")
).

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#formal_syntax)

-------------------------------------------------------------------------------------------------------------

@document \[ <url>                    |\
            url-prefix(<string>)     |\
            domain(<string>)         |\
            media-document(<string>) |\
            regexp(<string>)\
          \]# {
  <group-rule-body>
}

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#examples)

---------------------------------------------------------------------------------------------------

### [Specifying document for CSS rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#specifying_document_for_css_rule)

css

    @document url("http://www.w3.org/"),
              url-prefix("http://www.w3.org/Style/"),
              domain("mozilla.org"),
              media-document("video"),
              regexp("https:.*") {
      /* CSS rules here apply to:
         - The page "http://www.w3.org/"
         - Any page whose URL begins with "http://www.w3.org/Style/"
         - Any page whose URL's host is "mozilla.org"
           or ends with ".mozilla.org"
         - Any standalone video
         - Any page whose URL starts with "https:" */
    
      /* Make the above-mentioned pages really ugly */
      body {
        color: purple;
        background: yellow;
      }
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#specifications)

---------------------------------------------------------------------------------------------------------------

[Initially](https://www.w3.org/TR/2012/WD-css3-conditional-20120911/#at-document "External link (opens in new tab)")
 in Level 3, `@document` was [postponed](https://www.w3.org/TR/2012/WD-css3-conditional-20121213/#changes "External link (opens in new tab)")
 to Level 4, but then subsequently removed.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document#see_also)

---------------------------------------------------------------------------------------------------

*   [Per-site user style sheet rules](https://lists.w3.org/Archives/Public/www-style/2004Aug/0135 "External link (opens in new tab)")
     on the www-style mailing list.

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@document/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@document/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@document (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40document&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40document%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40document%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40document%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")