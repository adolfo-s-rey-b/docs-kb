*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#mdn-search)
    

`hyphens` CSS property
======================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since September 2023.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`hyphens`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies how words should be hyphenated when text wraps across multiple lines.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#try_it)

-----------------------------------------------------------------------------------------------

    hyphens: none;
    

    hyphens: manual;
    

    hyphens: auto;
    

    <section id="default-example">
      <p id="example-element">An extra­ordinarily long English word!</p>
    </section>
    

    #example-element {
      border: 2px dashed #999999;
      font-size: 1.5rem;
      text-align: left;
      width: 7rem;
    }
    

The example text "An extraordinarily long English word!" contains the hidden `&shy;` (soft hyphen) character: `An extra&shy;ordinarily long English word!`. This character is used to indicate a potential place to insert a hyphen when `hyphens: manual;` is specified.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#syntax)

-----------------------------------------------------------------------------------------------

css

    /* Keyword values */
    hyphens: none;
    hyphens: manual;
    hyphens: auto;
    
    /* Global values */
    hyphens: inherit;
    hyphens: initial;
    hyphens: revert;
    hyphens: revert-layer;
    hyphens: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#values)

This property is specified as one of the following keyword values:

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#none)

Words are not broken at line breaks, even if characters inside the words suggest line break points. Lines will only wrap at whitespace.

[`manual`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#manual)

Default value. Words are broken for line-wrapping only where characters inside the word suggest line break opportunities. See [Suggesting line break opportunities](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#suggesting_line_break_opportunities)
 below for details.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#auto)

The browser is free to automatically break words at appropriate hyphenation points, following whatever rules it chooses. However, suggested line break opportunities (see [Suggesting line break opportunities](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#suggesting_line_break_opportunities)
 below) will override automatic break point selection when present.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#description)

---------------------------------------------------------------------------------------------------------

The `hyphens` property can be used to define how words should be hyphenated when text wraps across multiple lines. It can prevent hyphenation entirely, hyphenate at manually-specified points within the text, or let the browser automatically insert hyphens where appropriate.

Hyphenation rules are language-specific. In HTML, the language is determined by the [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
 attribute. Browsers will only hyphenate if this attribute is present and the appropriate hyphenation dictionary is available. The `auto` setting's behavior depends on the language being properly tagged to select the appropriate hyphenation rules.

In XML, the [`xml:lang`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/xml:lang)
 attribute must be used. The specification does not define rules for hyphenation in XML content, so the exact hyphenation may vary from browser to browser.

The [`hyphenate-character`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-character)
 property can be used to specify an alternative hyphenation character to use at the end of the line, instead of the default language-specific hyphenation character.

If you apply [`word-break: break-all`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break#break-all)
 then no hyphens are shown, even if the word breaks at a hyphenation point. If you apply [`text-wrap-mode: nowrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-wrap-mode)
, no wrapping occurs, so no hyphens will appear.

### [Suggesting line break opportunities](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#suggesting_line_break_opportunities)

There are two Unicode characters used to manually specify potential line break points within text:

[U+2010 (HYPHEN)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#u2010_hyphen)

The "hard" hyphen character indicates a visible line break opportunity. Even if the line is not actually broken at that point, the hyphen is still rendered.

[U+00AD (SHY)](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#u00ad_shy)

An invisible, "**s**oft" **hy**phen. This character is not rendered visibly; instead, it marks a place where the browser should break the word if hyphenation is necessary. In HTML, use `&shy;` to insert a soft hyphen.

**Note:** When the HTML [`<wbr>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/wbr)
 element leads to a line break, no hyphen is added.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#formal_definition)

---------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `manual` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#formal_syntax)

-------------------------------------------------------------------------------------------------------------

hyphens =   
  none    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  manual  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  auto      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#examples)

---------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#basic_example)

This example demonstrates the three values of the `hyphens` property.

#### HTML

We include three [`<dd>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/dd)
 elements containing the same text but with three different classes.

html

    <dl>
      <dt><code>none</code>: no hyphen; overflow if needed</dt>
      <dd lang="en" class="none">An extreme&shy;ly long English word</dd>
      <dt>
        <code>manual</code>: hyphen only at &amp;hyphen; or &amp;shy; (if needed)
      </dt>
      <dd lang="en" class="manual">An extreme&shy;ly long English word</dd>
      <dt><code>auto</code>: hyphens where the algorithm decides (if needed)</dt>
      <dd lang="en" class="auto">An extreme&shy;ly long English word</dd>
    </dl>
    

#### CSS

Each of the three classes is set to a different `hyphens` value.

css

    dd {
      width: 55px;
      border: 1px solid black;
    }
    dd.none {
      hyphens: none;
    }
    dd.manual {
      hyphens: manual;
    }
    dd.auto {
      hyphens: auto;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#specifications)

---------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 3  <br>\# propdef-hyphens](https://drafts.csswg.org/css-text/#propdef-hyphens) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens#see_also)

---------------------------------------------------------------------------------------------------

*   [`content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/content)
    
*   [`overflow-wrap`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow-wrap)
     (formerly `word-wrap`)
*   [`word-break`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/word-break)
    
*   [Guide to wrapping and breaking text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text/Wrapping_breaking_text)
    
*   [CSS text](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/hyphens/index.md?plain=1 "Folder: en-us/web/css/reference/properties/hyphens (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fhyphens&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fhyphens%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fhyphens%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fhyphens%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fc0c85c3dc0d6ff4247c85b0144149e584d74b625%0A*+Document+last+modified%3A+2026-07-21T11%3A11%3A44.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")