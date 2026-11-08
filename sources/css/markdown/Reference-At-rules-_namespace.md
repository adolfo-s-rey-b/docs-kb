*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#mdn-search)
    

`@namespace` CSS at-rule
========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**`@namespace`** is an [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Syntax/At-rules)
 that defines XML [namespaces](https://developer.mozilla.org/en-US/docs/Glossary/Namespace)
 to be used in a [CSS](https://developer.mozilla.org/en-US/docs/Glossary/CSS)
 [style sheet](https://developer.mozilla.org/en-US/docs/Web/API/StyleSheet)
.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#try_it)

------------------------------------------------------------------------------------------------

    @namespace svg url("http://www.w3.org/2000/svg");
    
    a {
      color: orangered;
      text-decoration: underline dashed;
      font-weight: bold;
    }
    
    svg|a {
      fill: blueviolet;
      text-decoration: underline solid;
      text-transform: uppercase;
    }
    

    <p>
      <a href="#">This is an ordinary HTML link</a>
    </p>
    
    <svg width="250px" viewBox="0 0 250 20" xmlns="http://www.w3.org/2000/svg">
      <a href="#">
        <text x="0" y="15">This is a link created in SVG</text>
      </a>
    </svg>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#syntax)

------------------------------------------------------------------------------------------------

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#description)

----------------------------------------------------------------------------------------------------------

The defined namespaces can be used to restrict the [universal](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)
, [type](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors)
, and [attribute](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
 [selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors)
 to only select elements within that namespace. The `@namespace` rule is generally only useful when dealing with documents containing multiple namespaces—such as HTML with inline SVG or MathML, or XML that mixes multiple vocabularies.

Any `@namespace` rules must follow all [`@charset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@charset)
 and [`@import`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@import)
 rules, and precede all other at-rules and [style declarations](https://developer.mozilla.org/en-US/docs/Web/API/CSSStyleDeclaration)
 in a style sheet.

`@namespace` can be used to define the **default namespace** for the style sheet. When a default namespace is defined, all universal and type selectors (but not attribute selectors, see note below) apply only to elements in that namespace.

The `@namespace` rule can also be used to define a **namespace prefix**. When a universal, type, or attribute selector is prefixed with a namespace prefix, then that selector only matches if the namespace _and_ name of the element or attribute matches.

In HTML, known [foreign elements](https://html.spec.whatwg.org/multipage/syntax.html#foreign-elements "External link (opens in new tab)")
 will automatically be assigned namespaces. This means that HTML elements will act as though they are in the XHTML namespace (`http://www.w3.org/1999/xhtml`), even if there is no `xmlns` attribute anywhere in the document, and the [`<svg>`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/svg)
 and [`<math>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/math)
 elements will be assigned their proper namespaces (`http://www.w3.org/2000/svg` and `http://www.w3.org/1998/Math/MathML`, respectively).

**Note:** In XML, unless a prefix is defined directly on an attribute (_e.g._, `xlink:href`), that attribute has no namespace. In other words, attributes do not inherit the namespace of the element they're on. To match this behavior, the default namespace in CSS does not apply to attribute selectors.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#formal_syntax)

--------------------------------------------------------------------------------------------------------------

@namespace =   
  @namespace <namespace-prefix>[?](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#question_mark "Question mark: the entity is optional")
 [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)\
 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 [<url>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/url_value)\
 [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
 ;    
  
<namespace-prefix> =   
  [<ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#examples)

----------------------------------------------------------------------------------------------------

### [Specifying default and prefixed namespaces](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#specifying_default_and_prefixed_namespaces)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#specifications)

----------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Namespaces Module Level 3  <br>\# declaration](https://drafts.csswg.org/css-namespaces/#declaration) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace#see_also)

----------------------------------------------------------------------------------------------------

*   [Namespaces crash course](https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/Namespaces_crash_course)
    
*   [CSS at-rule functions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/At-rule_functions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@namespace/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@namespace (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40namespace&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40namespace%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40namespace%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40namespace%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe328268bb418551ab451881845881b5837c9da83%0A*+Document+last+modified%3A+2026-04-20T16%3A14%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")