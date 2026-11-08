*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator#mdn-search)
    

Namespace separator
===================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **namespace separator** (`|`) separates the selector from the namespace, identifying the [namespace](https://developer.mozilla.org/en-US/docs/Glossary/Namespace)
, or lack thereof, for a type selector.

css

    /* Links in the namespace named myNameSpace */
    myNameSpace|a {
      font-weight: bold;
    }
    /* paragraphs in any namespace (including no namespace) */
    *|p {
      color: darkblue;
    }
    /* heading level 2 not in a namespace */
    |h2 {
      margin-bottom: 0;
    }
    

[Type selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors)
 and the [universal selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)
 allow an optional namespace component. When a namespace has been previously declared via [`@namespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace)
, these selectors can be namespaced by prepending the selector with the name of the namespace separated by the namespace separator (`|`). This is useful when dealing with documents containing multiple namespaces such as HTML with inline SVG or MathML, or XML that mixes multiple vocabularies.

*   `ns|h1` - matches `<h1>` elements in namespace `ns`
*   `*|h1` - matches all `<h1>` elements
*   `|h1` - matches all `<h1>` elements outside of any declared or implied namespace

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator#syntax)

----------------------------------------------------------------------------------------------------------

css

    namespace|element { style properties }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator#examples)

--------------------------------------------------------------------------------------------------------------

By default, all elements in an HTML or SVG element have a namespace as the `http://www.w3.org/1999/xhtml` and `http://www.w3.org/2000/svg` namespace are implied. The [`document.createElementNS`](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElementNS)
 method, with an empty string for the namespace parameter, can be used to create elements with no namespace.

### [Named namespace example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator#named_namespace_example)

In this example, all elements are in a namespace.

#### HTML

No namespaces are explicitly declared in the HTML or within the SVG.

html

    <p>This paragraph <a href="#">has a link</a>.</p>
    
    <svg width="400" viewBox="0 0 400 20">
      <a href="#">
        <text x="0" y="15">Link created in SVG</text>
      </a>
    </svg>
    

#### CSS

The CSS declares two namespaces, then assigns styles to links globally (`a`), to links in no namespace (`|a`), to links in any namespace or no namespace (`*|a`), and then to two different named namespaces (`svgNamespace|a` and `htmlNameSpace|a`).

css

    @namespace svgNamespace url("http://www.w3.org/2000/svg");
    @namespace htmlNameSpace url("http://www.w3.org/1999/xhtml");
    /* All `<a>`s in the default namespace, in this case, all `<a>`s */
    a {
      font-size: 1.4rem;
    }
    /* no namespace */
    |a {
      text-decoration: wavy overline lime;
      font-weight: bold;
    }
    /* all namespaces (including no namespace) */
    *|a {
      color: red;
      fill: red;
      font-style: italic;
    }
    /* only the svgNamespace namespace, which is <svg> content */
    svgNamespace|a {
      color: green;
      fill: green;
    }
    /* The htmlNameSpace namespace, which is the HTML document */
    htmlNameSpace|a {
      text-decoration-line: line-through;
    }
    

#### Result

The selector `|a`, a link not in a namespace, doesn't match any links. In HTML, the `http://www.w3.org/1999/xhtml` is implied, meaning all HTML is in a namespace, even if none is explicitly declared. In SVG, even if not explicitly set, the `http://www.w3.org/2000/svg` namespace is also implied. This means all the content is within at least one namespace.

### [Default namespace and no namespace](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator#default_namespace_and_no_namespace)

In this example, we use JavaScript to create an element without a namespace and append it to the document. We set the SVG namespace to be the default namespace by defining the unnamed namespace with `@namespace`.

**Note:** If a default, or unnamed, namespace is defined, universal and type selectors apply only to elements in that namespace.

#### HTML

No namespaces are explicitly declared in the HTML or within the SVG.

html

    <p><a href="#">A link</a> in the implied HTML namespace.</p>
    
    <svg width="400" viewBox="0 0 400 20">
      <a href="#">
        <text x="0" y="15">Link created in SVG namespace</text>
      </a>
    </svg>
    

#### JavaScript

With JavaScript, with [`document.createElementNS`](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElementNS)
, we create an anchor link without a namespace, then append the link.

js

    // create 'no namespace' anchor
    const a = document.createElementNS("", "a");
    a.href = "#";
    a.appendChild(document.createTextNode("Link created without a namespace"));
    
    document.body.appendChild(a);
    

#### CSS

We declare a namespace with [`@namespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace)
. By omitting the name for the namespace, the `@namespace` declaration creates a default namespace.

css

    /* By omitting a name, this sets SVG as the default namespace */
    @namespace url("http://www.w3.org/2000/svg");
    
    /* `<a>` in the default (set to SVG) namespace */
    a {
      font-size: 1.4rem;
    }
    
    /* `<svg>` and `<p>` in the default (set to SVG) namespace */
    svg,
    p {
      border: 5px solid gold;
    }
    
    /* links outside of any namespace */
    |a {
      text-decoration: wavy underline purple;
      font-weight: bold;
    }
    
    /* links with any namespace or no namespace */
    *|a {
      font-style: italic;
      color: magenta;
      fill: magenta;
    }
    

#### Result

The selector with no namespace separator, the `a`, matched only the SVG `<a>` elements, as SVG was set as the default namespace.

The selector with no namespace, the `|a`, matched the JavaScript defined and appended `<a>`, as that node is the only node that doesn't have a default namespace.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Namespaces Module Level 3  <br>\# declaration](https://drafts.csswg.org/css-namespaces/#declaration) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`@namespace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@namespace)
    
*   [`Document.createElementNS()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/createElementNS)
     method
*   [`Element.namespaceURI`](https://developer.mozilla.org/en-US/docs/Web/API/Element/namespaceURI)
     property
*   [CSS type selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Type_selectors)
    
*   [CSS universal selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Universal_selectors)
    
*   [CSS selector module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 16, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Namespace_separator/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/namespace_separator/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/namespace_separator (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FNamespace_separator&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fnamespace_separator%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FNamespace_separator%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fnamespace_separator%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F33094d735e90b4dcae5733331b79c51fee997410%0A*+Document+last+modified%3A+2025-12-16T15%3A14%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")