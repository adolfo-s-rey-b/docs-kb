*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#mdn-search)
    

`font-family` CSS property
==========================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-family`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies a prioritized list of one or more font family names and/or generic family names for the selected element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#try_it)

---------------------------------------------------------------------------------------------------

    font-family: "Georgia", serif;
    

    font-family: "Gill Sans", sans-serif;
    

    font-family: sans-serif;
    

    font-family: serif;
    

    font-family: cursive;
    

    font-family: system-ui;
    

    <section id="default-example">
      <p id="example-element">
        London. Michaelmas term lately over, and the Lord Chancellor sitting in
        Lincoln's Inn Hall. Implacable November weather. As much mud in the streets
        as if the waters had but newly retired from the face of the earth, and it
        would not be wonderful to meet a Megalosaurus, forty feet long or so,
        waddling like an elephantine lizard up Holborn Hill.
      </p>
    </section>
    

    section {
      font-size: 1.2em;
    }
    

Values are separated by commas to indicate that they are alternatives. The browser will select the first font in the list that is installed or that can be downloaded using a [`@font-face`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@font-face)
 at-rule.

It is often convenient to use the shorthand property [`font`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font)
 to set `font-size` and other font related properties all at once.

You should always include at least one generic family name in a `font-family` list, since there's no guarantee that any given font is available. This lets the browser select an acceptable fallback font when necessary.

The `font-family` property specifies a list of fonts, from highest priority to lowest. Font selection _does not_ stop at the first font in the list that is on the user's system. Rather, font selection is done _one character at a time_, so that if an available font does not have a glyph for a needed character, the latter fonts are tried. When a font is only available in some [styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
, [variants](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
, or [sizes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
, those properties may also influence which font family is chosen.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#syntax)

---------------------------------------------------------------------------------------------------

css

    /* A font family name and a generic family name */
    font-family: "Gill Sans Extrabold", sans-serif;
    font-family: "Goudy Bookletter 1911", sans-serif;
    
    /* A generic family name only */
    font-family: serif;
    font-family: sans-serif;
    font-family: monospace;
    font-family: cursive;
    font-family: fantasy;
    font-family: system-ui;
    font-family: ui-serif;
    font-family: ui-sans-serif;
    font-family: ui-monospace;
    font-family: ui-rounded;
    font-family: math;
    font-family: fangsong;
    
    /* Global values */
    font-family: inherit;
    font-family: initial;
    font-family: revert;
    font-family: revert-layer;
    font-family: unset;
    

The `font-family` property lists one or more font families, separated by commas. Each font family is specified as either a `<family-name>` or a `<generic-name>` value.

The example below lists two font families, the first with a `<family-name>` and the second with a `<generic-name>`:

css

    font-family: "Gill Sans Extrabold", sans-serif;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#values)

[`<family-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#family-name)

The name of a font family. This must be either a single [`<string>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
 value or a space-separated sequence of [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
 values. String values must be quoted but may contain any Unicode character. Custom identifiers are not quoted, but certain characters must be escaped.

It is good practice to quote font family names that contain white space, digits, or punctuation characters other than hyphens.

See also [Valid family names](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#valid_family_names)
.

[`<generic-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#generic-name)

Generic font families are a fallback mechanism, a means of preserving some of the style sheet author's intent when none of the specified fonts are available. Generic family names are keywords and must not be quoted. A generic font family should be the last item in the list of font family names. The following keywords are defined:

[`serif`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#serif)

Glyphs have finishing strokes, flared or tapering ends, or have actual serifed endings.

For example: Lucida Bright, Lucida Fax, Palatino, Palatino Linotype, Palladio, URW Palladio, serif.

[`sans-serif`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#sans-serif)

Glyphs have stroke endings that are plain.

For example: Open Sans, Fira Sans, Lucida Sans, Lucida Sans Unicode, Trebuchet MS, Liberation Sans, Nimbus Sans L, sans-serif.

[`monospace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#monospace)

All glyphs have the same fixed width.

For example: Fira Mono, DejaVu Sans Mono, Menlo, Consolas, Liberation Mono, Monaco, Lucida Console, monospace.

**Note:** When `font-family` is set to the single keyword `monospace` and no `font-size` is set, browsers use the user's monospace font size preference, which is often smaller than the size used for proportional fonts. See [Monospace font size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#monospace_font_size)
 for details and how to control this.

[`cursive`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#cursive)

Glyphs in cursive fonts generally have either joining strokes or other cursive characteristics beyond those of italic typefaces. The glyphs are partially or completely connected, and the result looks more like handwritten pen or brush writing than printed letter work.

For example: Brush Script MT, Brush Script Std, Lucida Calligraphy, Lucida Handwriting, Apple Chancery, cursive.

**Note:** On Windows, browsers use Comic Sans MS as the `cursive` font, a casual font with completely disconnected glyphs.

[`fantasy`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#fantasy)

Fantasy fonts are primarily decorative fonts that contain playful representations of characters.

For example: Papyrus, Herculanum, Party LET, Curlz MT, Harrington, fantasy.

[`system-ui`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#system-ui)

Glyphs are taken from the default user interface font on a given platform. Because typographic traditions vary widely across the world, this generic is provided for typefaces that don't map cleanly into the other generics.

**Note:** As the name implies, `system-ui` is intended to make UI elements look like native apps, and not for typesetting large paragraphs of text. It may cause the displayed typeface to be undesirable for some users—for example, the default Windows CJK font may render Latin scripts poorly, and the `lang` attribute may not affect the displayed font. Some operating systems do not allow customizing `system-ui`, while browsers generally allow customizing the `sans-serif` font family. For large paragraphs, use `sans-serif` or some other non-UI font family instead.

[`ui-serif`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#ui-serif)

The default user interface serif font.

[`ui-sans-serif`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#ui-sans-serif)

The default user interface sans-serif font.

[`ui-monospace`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#ui-monospace)

The default user interface monospace font.

[`ui-rounded`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#ui-rounded)

The default user interface font that has rounded features.

[`math`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#math)

Font that addresses the particular stylistic concerns of representing mathematics: superscript and subscript, brackets that cross several lines, nesting expressions, and double struck glyphs with distinct meanings. UA stylesheets may set `math { font-family: math }` so that the [`<math>`](https://developer.mozilla.org/en-US/docs/Web/MathML/Reference/Element/math "<math>")
 element uses appropriate fonts by default.

[`fangsong`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#fangsong)

A particular style of Chinese characters that are between serif-style Song and cursive-style Kai forms. This style is often used for government documents.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | depends on user agent |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

font-family =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 <font-family-name> [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <generic-font-family> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[#](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#hash_mark "Hash mark: the entity is repeated one or several times, each occurrence separated by a comma")
    
  
<font-family-name> =   
  [<string>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/string)
         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
[+](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#plus "Plus: the entity may occur one or several times")
    
  
<generic-font-family> =   
  <generic-font-script-specific>  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <generic-font-complete>         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <generic-font-incomplete>         
  
<generic-font-script-specific> =   
  generic( fangsong )   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  generic( kai )        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  generic( khmer-mul )  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  generic( nastaliq )     
  
<generic-font-complete> =   
  serif       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  sans-serif  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  system-ui   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  cursive     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  fantasy     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  math        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  monospace     
  
<generic-font-incomplete> =   
  ui-serif       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ui-sans-serif  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ui-monospace   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  ui-rounded       

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#examples)

-------------------------------------------------------------------------------------------------------

### [Some common font families](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#some_common_font_families)

css

    .serif {
      font-family: "Times", "Times New Roman", "Georgia", serif;
    }
    
    .sansserif {
      font-family: "Verdana", "Helvetica", "Arial", sans-serif;
    }
    
    .monospace {
      font-family: "Lucida Console", "Courier New", monospace;
    }
    
    .cursive {
      font-family: cursive;
    }
    
    .fantasy {
      font-family: fantasy;
    }
    
    .math {
      font-family: math;
    }
    
    .fangsong {
      font-family: fangsong;
    }
    

    div {
      margin: 0.5rem;
    }
    

    <div class="serif">This is an example of a serif font.</div>
    
    <div class="sansserif">This is an example of a sans-serif font.</div>
    
    <div class="monospace">This is an example of a monospace font.</div>
    
    <div class="cursive">This is an example of a cursive font.</div>
    
    <div class="fantasy">This is an example of a fantasy font.</div>
    
    <div class="fangsong">This is an example of a fangsong font.</div>
    
    <div class="math">This is an example of a math font: ℝ, ∫, ∑…</div>
    

### [Monospace font size](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#monospace_font_size)

Browsers maintain separate default font size preferences for proportional fonts (such as `serif` and `sans-serif`) and for monospace fonts. Typical defaults are `16px` for proportional fonts and `13px` for monospace fonts.

When `font-family` is set to the single keyword `monospace`, browsers apply the monospace size preference. If users have not changed their browser preferences and [`font-size`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-size)
 is not explicitly set, monospace text may be rendered smaller than surrounding content. The same reduction applies to elements whose user agent stylesheet sets `font-family: monospace`, such as [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
 and [`<pre>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/pre)
.

If the `font-family` value includes more than one family, even if the value is `monospace, monospace`, browsers do not apply the monospace font size preference, and will render the text at the inherited `font-size`. Declaring `font-family: monospace, monospace` (or a named monospace font followed by `monospace`) therefore renders at the same size as surrounding proportional text. This behavior is not specified in CSS, but it is interoperable across the major browser engines.

html

    <p class="proportional">
      This proportional text is at the default size; generally 16px.
    </p>
    <p class="mono-only">
      This monospace text is at the preferred size for monospace fonts; generally
      13px.
    </p>
    <p class="mono-list">
      This is in "monospace, monospace" font, rendered at the same size as
      proportional text; generally 16px.
    </p>
    

css

    .mono-only {
      font-family: monospace;
    }
    
    .mono-list {
      font-family: monospace, monospace;
    }
    

If you haven't changed your font size in your browser settings, the first and last paragraphs will be the same font-size, rendered at the browser preferred font size. The middle paragraph will be rendered at the preferred mono-space font size, which is generally set to be smaller than the preferred font-size for other text.

### [Valid family names](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#valid_family_names)

The following declarations are valid:

css

    font-family: "Goudy Bookletter 1911", sans-serif;
    

The following declarations are invalid:

css

    font-family: Goudy Bookletter 1911, sans-serif;
    font-family: Red/Black, sans-serif;
    font-family: "Lucida" Grande, sans-serif;
    font-family: Ahem!, sans-serif;
    font-family: test@foo, sans-serif;
    font-family: #POUND, sans-serif;
    font-family: Hawaii 5-0, sans-serif;
    

The following example is technically valid but is not recommended:

css

    font-family:
      Gill Sans Extrabold,
      sans-serif;
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# generic-font-families](https://drafts.csswg.org/css-fonts/#generic-font-families) |
| [CSS Fonts Module Level 4  <br>\# font-family-prop](https://drafts.csswg.org/css-fonts/#font-family-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family#see_also)

-------------------------------------------------------------------------------------------------------

*   [`font-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-style)
    
*   [`font-weight`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-weight)
    
*   [`font-variant-emoji`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji)
    
*   SVG [`font-family`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/font-family)
     attribute
*   [Learn: Fundamental text and font styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Text_styling/Fundamentals)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-family/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-family/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-family (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-family&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-family%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-family%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-family%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fe7ee9edb037573b84aca121a0bce4f3f700f3fa3%0A*+Document+last+modified%3A+2026-10-21T20%3A37%3A24.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")