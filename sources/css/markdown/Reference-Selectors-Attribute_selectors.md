*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#mdn-search)
    

Attribute selectors
===================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The CSS **attribute selector** matches elements based on the element having a given attribute explicitly set, with options for defining an attribute value or substring value match.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* <a> elements with a title attribute */
    a[title] {
      color: purple;
    }
    
    /* <a> elements with an href matching "https://example.org" */
    a[href="https://example.org"] {
      color: green;
    }
    
    /* <a> elements with an href containing "example" */
    a[href*="example"] {
      font-size: 2em;
    }
    
    /* <a> elements with an href ending ".org", case-insensitive */
    a[href$=".org" i] {
      font-style: italic;
    }
    
    /* <a> elements whose class attribute contains the word "logo" */
    a[class~="logo"] {
      padding: 2px;
    }
    

[`[attr]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#attr)

Represents elements with an attribute name of _attr_.

[`[attr=value]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#attrvalue)

Represents elements with an attribute name of _attr_ whose value is exactly _value_.

[`[attr~=value]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#attrvalue_2)

Represents elements with an attribute name of _attr_ whose value is a whitespace-separated list of words, one of which is exactly _value_.

[`[attr|=value]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#attrvalue_3)

Represents elements with an attribute name of _attr_ whose value can be exactly _value_ or can begin with _value_ immediately followed by a hyphen, `-` (U+002D). It is often used for language subcode matches.

[`[attr^=value]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#attrvalue_4)

Represents elements with an attribute name of _attr_ whose value is prefixed (preceded) by _value_.

[`[attr$=value]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#attrvalue_5)

Represents elements with an attribute name of _attr_ whose value is suffixed (followed) by _value_.

[`[attr*=value]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#attrvalue_6)

Represents elements with an attribute name of _attr_ whose value contains at least one occurrence of _value_ within the string.

[`[attr operator value i]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#attr_operator_value_i)

Adding an `i` (or `I`) before the closing bracket causes the value to be compared case-insensitively (for characters within the [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 range).

[`[attr operator value s]`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#attr_operator_value_s)

Adding an `s` (or `S`) before the closing bracket causes the value to be compared case-sensitively (for characters within the [ASCII](https://developer.mozilla.org/en-US/docs/Glossary/ASCII)
 range).

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#values)

[`<attr>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#attr_2)

An [`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
, that is, the unquoted name of the attribute. This can be any valid language-specific attribute (SVG, HTML, XML, etc.), a [`data-*` attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*)
, or an author-created attribute.

[`<value>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#value)

An [`<ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
 or [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
, representing the attribute value. The value must be quoted if it contains spaces or special characters.

[`s` or `i`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#s)

Case sensitivity or insensitivity flag. If included before the closing bracket (`]`), makes the value case sensitive or insensitive, irrespective of the markup language.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#description)

--------------------------------------------------------------------------------------------------------------------

The case sensitivity of attribute names and values depends on the document language. In HTML, attribute names are case-insensitive, as are spec-defined [enumerated](https://developer.mozilla.org/en-US/docs/Glossary/Enumerated)
 values. The [case-insensitive HTML attribute values](https://html.spec.whatwg.org/multipage/semantics-other.html#case-sensitivity-of-selectors "External link (opens in new tab)")
 are listed in the HTML spec. For these attributes, the attribute value in the selector is case-insensitive, regardless of whether the value is invalid or the attribute for the element on which it is set is invalid.

If the attribute value is case-sensitive, like [`class`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class)
, [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
, and [`data-*`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/data-*)
 attributes, the attribute selector value match is case-sensitive. Attributes defined outside of the HTML specification, like [`role`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles)
 and [`aria-*`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes)
 attributes, are also case-sensitive. Case-sensitive attribute selectors can be made case-insensitive with the inclusion of the case-insensitive modifier (`i`).

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#examples)

--------------------------------------------------------------------------------------------------------------

### [Links](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#links)

#### CSS

css

    a {
      color: blue;
    }
    
    /* Internal links, beginning with "#" */
    a[href^="#"] {
      background-color: gold;
    }
    
    /* Links with "example" anywhere in the URL */
    a[href*="example"] {
      background-color: silver;
    }
    
    /* Links with "insensitive" anywhere in the URL,
       regardless of capitalization */
    a[href*="insensitive" i] {
      color: cyan;
    }
    
    /* Links with "cAsE" anywhere in the URL,
    with matching capitalization */
    a[href*="cAsE" s] {
      color: pink;
    }
    
    /* Links that end in ".org" */
    a[href$=".org"] {
      color: red;
    }
    
    /* Links that start with "https://" and end in ".org" */
    a[href^="https://"][href$=".org"] {
      color: green;
    }
    

#### HTML

html

    <ul>
      <li><a href="#internal">Internal link</a></li>
      <li><a href="http://example.com">Example link</a></li>
      <li><a href="#InSensitive">Insensitive internal link</a></li>
      <li><a href="http://example.org">Example org link</a></li>
      <li><a href="https://example.org">Example https org link</a></li>
    </ul>
    

#### Result

### [Languages](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#languages)

#### CSS

css

    /* All divs with a `lang` attribute are bold. */
    div[lang] {
      font-weight: bold;
    }
    
    /* All divs without a `lang` attribute are italicized. */
    div:not([lang]) {
      font-style: italic;
    }
    
    /* All divs in US English are blue. */
    div[lang~="en-us"] {
      color: blue;
    }
    
    /* All divs in Portuguese are green. */
    div[lang="pt"] {
      color: green;
    }
    
    /* All divs in Chinese are red, whether
       simplified (zh-Hans-CN) or traditional (zh-Hant-TW). */
    div[lang|="zh"] {
      color: red;
    }
    
    /* All divs with a Traditional Chinese
       `data-lang` are purple. */
    /* Note: You could also use hyphenated attributes
       without double quotes */
    div[data-lang="zh-Hant-TW"] {
      color: purple;
    }
    

#### HTML

html

    <div lang="en-us en-gb en-au en-nz">Hello World!</div>
    <div lang="pt">Olá Mundo!</div>
    <div lang="zh-Hans-CN">世界您好！</div>
    <div lang="zh-Hant-TW">世界您好！</div>
    <div data-lang="zh-Hant-TW">世界您好！</div>
    

#### Result

### [HTML ordered lists](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#html_ordered_lists)

The HTML specification requires the [`type`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#type)
 attribute to be matched case-insensitively because it is primarily used in the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element. Note that if a modifier is not supported by the user agent, then the selector will not match.

#### CSS

css

    /* Case-sensitivity depends on document language */
    ol[type="a"]:first-child {
      list-style-type: lower-alpha;
      background: red;
    }
    
    ol[type="i" s] {
      list-style-type: lower-alpha;
      background: lime;
    }
    
    ol[type="I" s] {
      list-style-type: upper-alpha;
      background: grey;
    }
    
    ol[type="a" i] {
      list-style-type: upper-alpha;
      background: green;
    }
    

#### HTML

html

    <ol type="A">
      <li>
        Red background for case-insensitive matching (default for the type selector)
      </li>
    </ol>
    <ol type="i">
      <li>Lime background if `s` modifier is supported (case-sensitive match)</li>
    </ol>
    <ol type="I">
      <li>Grey background if `s` modifier is supported (case-sensitive match)</li>
    </ol>
    <ol type="A">
      <li>
        Green background if `i` modifier is supported (case-insensitive match)
      </li>
    </ol>
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# attribute-selectors](https://drafts.csswg.org/selectors/#attribute-selectors) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors#see_also)

--------------------------------------------------------------------------------------------------------------

*   [`attr()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/attr)
    
*   Selecting a single element: [`Document.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelector)
    , [`DocumentFragment.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/querySelector)
    , or [`Element.querySelector()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector)
    
*   Selecting all matching elements: [`Document.querySelectorAll()`](https://developer.mozilla.org/en-US/docs/Web/API/Document/querySelectorAll)
    , [`DocumentFragment.querySelectorAll()`](https://developer.mozilla.org/en-US/docs/Web/API/DocumentFragment/querySelectorAll)
    , or [`Element.querySelectorAll()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelectorAll)
    
*   [Case-insensitive attribute selector values](https://html.spec.whatwg.org/multipage/semantics-other.html#case-sensitivity-of-selectors "External link (opens in new tab)")
     on WHATWG

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 4, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/attribute_selectors/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/attribute_selectors (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FAttribute_selectors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fattribute_selectors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FAttribute_selectors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fattribute_selectors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe2c34c75df6238fbeff790100cea1ab7e552e49e%0A*+Document+last+modified%3A+2026-09-04T19%3A00%3A00.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")