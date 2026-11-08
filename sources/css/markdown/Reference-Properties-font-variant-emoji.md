*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#mdn-search)
    

`font-variant-emoji` CSS property
=================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/262)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`font-variant-emoji`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the default presentation style for displaying emojis.

Traditionally, this was done by appending a _Variation Selector_, `U+FE0E` for text and `U+FE0F` for emoji, to the emoji code point. Only emojis listed as contributing to a [Unicode emoji presentation sequence](https://www.unicode.org/emoji/charts/emoji-variants.html "External link (opens in new tab)")
 are affected by this property.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#syntax)

----------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    font-variant-emoji: normal;
    font-variant-emoji: text;
    font-variant-emoji: emoji;
    font-variant-emoji: unicode;
    
    /* Global values */
    font-variant-emoji: inherit;
    font-variant-emoji: initial;
    font-variant-emoji: revert;
    font-variant-emoji: revert-layer;
    font-variant-emoji: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#values)

This property is specified as one of the following keyword values:

[`normal`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#normal)

Allows a browser to choose how to display the emoji. This often follows the operating system setting.

[`text`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#text)

Renders the emoji as if it were using the unicode text variation selector (`U+FE0E`).

[`emoji`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#emoji)

Renders the emoji as if it were using the unicode emoji variation selector (`U+FE0F`).

[`unicode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#unicode)

Renders the emoji in accordance with the [Emoji presentation properties](https://www.unicode.org/reports/tr51/tr51-23.html#Emoji_Presentation "External link (opens in new tab)")
. If the `U+FE0E` or `U+FE0F` variation selector is present, then it will override this value setting.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#formal_definition)

--------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `normal` |
| Applies to | all elements and text. It also applies to [`::first-letter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-letter)<br> and [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)<br>. |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | discrete |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#formal_syntax)

------------------------------------------------------------------------------------------------------------------------

font-variant-emoji =   
  normal   [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  text     [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  emoji    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  unicode    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#accessibility)

------------------------------------------------------------------------------------------------------------------------

While the use of emojis may seem fun, you should consider their impact on accessibility, specifically for users with visual and cognitive impairments. Consider the following factors while using emojis:

*   Display on screen-readers: Screen-readers will read out the alt text of an emoji. Keep this in mind to consider the position of an emoji in the content. Repeated and overuse of emojis will have a detrimental effect on screen-reader users. It is better to use emojis than emoticons; emoticons will be read out as punctuation characters.
    
*   Contrast with background: When using emojis, consider their colors and how that will work with the background color, especially if you have background colors that can change, such as light/dark modes.
    
*   Intent of use: Do not use emojis to replace words because your understanding of the emoji meaning may differ from that of the users'. Also consider that emojis might have different meanings in different cultures and geographies. Our recommendation is to preferably limit usage to commonly known emojis.
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#examples)

--------------------------------------------------------------------------------------------------------------

### [Changing the way an emoji is displayed](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#changing_the_way_an_emoji_is_displayed)

This example shows how you can render an emoji in its `text` or `emoji` presentation.

#### HTML

    <p class="no-support">
      Your Browser does not support <code>font-variant-emoji</code>. This image
      shows how it is rendered with support.
    </p>
    <img
      class="no-support"
      src="./font-variant-emoji-example.jpg"
      alt="a telephone emoji show as text, black and white next to a telephone emoji shown as emoji full color and graphical representation" />
    

html

    <section class="emojis">
      <div class="emoji">
        <h2>text presentation</h2>
        <div class="text-presentation">☎</div>
      </div>
      <div class="emoji">
        <h2>emoji presentation</h2>
        <div class="emoji-presentation">☎</div>
      </div>
    </section>
    

#### CSS

    @supports (font-variant-emoji: emoji) {
      .no-support {
        display: none;
      }
      .emojis {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        font-family:
          "Noto Color Emoji", "Segoe UI Emoji", "Apple Color Emoji", sans-serif;
      }
      .emoji > div {
        font-size: 2rem;
      }
    }
    
    @supports not (font-variant-emoji: emoji) {
      .emojis {
        display: none;
      }
    }
    

css

    .text-presentation {
      font-variant-emoji: text;
    }
    
    .emoji-presentation {
      font-variant-emoji: emoji;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#specifications)

--------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Fonts Module Level 4  <br>\# font-variant-emoji-prop](https://drafts.csswg.org/css-fonts/#font-variant-emoji-prop) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji#see_also)

--------------------------------------------------------------------------------------------------------------

*   [font-variant](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant)
    
*   [font-variant-alternates](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-alternates)
    
*   [font-variant-caps](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-caps)
    
*   [font-variant-east-asian](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-east-asian)
    
*   [font-variant-ligatures](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-ligatures)
    
*   [font-variant-numeric](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-numeric)
    
*   [Emojis and accessibility: How to use them properly](https://uxdesign.cc/emojis-in-accessibility-how-to-use-them-properly-66b73986b803 "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/font-variant-emoji/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/font-variant-emoji/index.md?plain=1 "Folder: en-us/web/css/reference/properties/font-variant-emoji (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-emoji&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-emoji%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Ffont-variant-emoji%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Ffont-variant-emoji%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fb7e9f482c51817d3a885e26092f8219fd0d9d278%0A*+Document+last+modified%3A+2026-09-28T21%3A00%3A55.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")