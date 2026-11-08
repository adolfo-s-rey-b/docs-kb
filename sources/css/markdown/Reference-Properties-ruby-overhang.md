*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#mdn-search)
    

`ruby-overhang` CSS property
============================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/268)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`ruby-overhang`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies whether or not a [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
 annotation overhangs any surrounding text.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#try_it)

-----------------------------------------------------------------------------------------------------

    ruby-overhang: auto;
    

    ruby-overhang: none;
    

    <section id="default-example">
      <p id="example-element">
        あの<ruby>表<rp>(</rp><rt>ひょう</rt><rp>)</rp></ruby
        ><ruby>現<rp>(</rp><rt>げん</rt><rp>)</rp></ruby>は面白い。
      </p>
    </section>
    

    #default-example {
      font-size: 2em;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#syntax)

-----------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    ruby-overhang: auto;
    ruby-overhang: none;
    
    /* Global values */
    ruby-overhang: inherit;
    ruby-overhang: initial;
    ruby-overhang: revert;
    ruby-overhang: revert-layer;
    ruby-overhang: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#auto)

When a ruby annotation container is longer than its corresponding base container, the annotation may partially overlap adjacent text. Whether, and how much to overhang are determined by the user agent.

[`none`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#none)

A keyword indicating that the ruby is never allowed to extend past adjacent containers.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#description)

---------------------------------------------------------------------------------------------------------------

The `ruby-overhang` property controls whether the ruby annotation text box ([`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
) may overlap adjacent text outside the `<ruby>` container box.

When ruby annotation text is not allowed to overhang — when `ruby-overhang: none` is set on the `<ruby>` element — that element behaves like an inline box, as if its [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property were set to `inline` with only its own contents rendered within its boundaries and adjacent elements not crossing the boundary box.

By default, the content of an `<rt>` element is allowed to overhang, so content may overlap the `<ruby>` container box, partially rendering over or under surrounding inline-level content. With `auto`, the default, content may overhang, but it will not overhang if doing so would overlap adjacent `<rt>` elements or elements with a `display` value resolving to `ruby-base` or `ruby-text`.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#formal_definition)

---------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | ruby annotation containers |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | the specified keyword |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#formal_syntax)

-------------------------------------------------------------------------------------------------------------------

ruby-overhang =   
  auto    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  spaces    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#examples)

---------------------------------------------------------------------------------------------------------

### [Ruby overhanging base text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#ruby_overhanging_base_text)

This examples demonstrates both values of the `ruby-overhang` property.

#### HTML

We include two paragraphs with identical `<ruby>` content and structures, other than their class names.

html

    <p class="auto">
      あの<ruby>表<rp>(</rp><rt>ひょう</rt><rp>)</rp></ruby
      ><ruby>現<rp>(</rp><rt>げん</rt><rp>)</rp></ruby>は面白い。
    </p>
    
    <p class="none">
      あの<ruby>表<rp>(</rp><rt>ひょう</rt><rp>)</rp></ruby
      ><ruby>現<rp>(</rp><rt>げん</rt><rp>)</rp></ruby>は面白い。
    </p>
    

#### CSS

A red `outline` of `1px` helps highlight the text annotation of [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
 elements. The first paragraph has `ruby-overhang: auto` and the second has `ruby-overhang: none`.

css

    p {
      font-size: 40px;
      display: block;
      margin: 0.5rem;
    }
    rt {
      font-size: 28px;
      outline: 1px solid red;
    }
    .auto {
      ruby-overhang: auto;
    }
    .none {
      ruby-overhang: none;
    }
    

#### Results

When `ruby-overhang` is set to `none`, the annotation text is not allowed to overlap the adjacent boxes of base ruby text. If you look closely, you may notice that in the first paragraph, the red box encasing the ruby text slightly overlaps parts of non-associated `<ruby>` content, whereas in the `none` example in supporting browsers, there is no overlap between ruby content and not-associated ruby text.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#specifications)

---------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Ruby Annotation Layout Module Level 1  <br>\# propdef-ruby-overhang](https://drafts.csswg.org/css-ruby/#propdef-ruby-overhang) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#browser_compatibility)

-----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang#see_also)

---------------------------------------------------------------------------------------------------------

*   [`ruby-align`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-align)
    
*   [`text-transform`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-transform)
    : full-size-kana
*   [`<ruby>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/ruby)
    
*   [`<rt>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rt)
    
*   [`<rp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/rp)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/ruby-overhang/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/ruby-overhang/index.md?plain=1 "Folder: en-us/web/css/reference/properties/ruby-overhang (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fruby-overhang&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fruby-overhang%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fruby-overhang%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fruby-overhang%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")