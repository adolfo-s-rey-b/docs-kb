*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#mdn-search)
    

`hyphenate-character` CSS property
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`hyphenate-character`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the character (or string) used at the end of a line before a hyphenation break.

Both automatic and soft hyphens are displayed according to the specified hyphenate-character value.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#try_it)

-----------------------------------------------------------------------------------------------------------

    hyphenate-character: auto;
    

    hyphenate-character: "=";
    

    hyphenate-character: "—";
    

    <section id="default-example">
      <p id="example-element">An extra­ordinarily long English word!</p>
    </section>
    

    #example-element {
      border: 2px dashed #999999;
      font-size: 1.5rem;
      text-align: left;
      width: 7rem;
      hyphens: auto;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#syntax)

-----------------------------------------------------------------------------------------------------------

css

    hyphenate-character: <string>;
    hyphenate-character: auto;
    

The value either sets the string to use instead of a hyphen, or indicates that the user agent should select an appropriate string based on the current typographic conventions (default).

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#values)

[`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#string)

The [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 to use at the end of the line before a hyphenation break. The user agent may truncate this value if too many characters are used.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#auto)

The user-agent selects an appropriate string based on the content language's typographic conventions. This is the default property value, and only needs to be explicitly set in order to override a different inherited value.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#formal_definition)

---------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#formal_syntax)

-------------------------------------------------------------------------------------------------------------------------

hyphenate-character =   
  auto      [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#examples)

---------------------------------------------------------------------------------------------------------------

This example shows two identical blocks of text that have [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
 set to ensure that they break wherever needed, and on soft hyphen breaks (created using `&shy;`). The first block has the value of the hyphen changed to the equals symbol (`=`). The second block has no hyphenate-character set, which is equivalent to `hyphenate-character: auto` for user agents that support this property.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#html)

html

    <dl>
      <dt><code>hyphenate-character: "="</code></dt>
      <dd id="string" lang="en">Superc&shy;alifragilisticexpialidocious</dd>
      <dt><code>hyphenate-character is not set</code></dt>
      <dd lang="en">Superc&shy;alifragilisticexpialidocious</dd>
    </dl>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#css)

css

    dd {
      width: 90px;
      border: 1px solid black;
      hyphens: auto;
    }
    
    dd#string {
      -webkit-hyphenate-character: "=";
      hyphenate-character: "=";
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#specifications)

---------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 4  <br>\# propdef-hyphenate-character](https://drafts.csswg.org/css-text-4/#propdef-hyphenate-character) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character#see_also)

---------------------------------------------------------------------------------------------------------------

*   Related CSS properties: [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
    , [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
    .

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/hyphenate-character/index.md?plain=1 "Folder: en-us/web/css/reference/properties/hyphenate-character (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fhyphenate-character&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fhyphenate-character%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fhyphenate-character%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fhyphenate-character%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")