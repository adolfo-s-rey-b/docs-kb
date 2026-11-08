*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#mdn-search)
    

`scrollbar-color` CSS property
==============================

Baseline 2025

Newly available

Since December 2025, this feature works across the latest devices and browser versions. This feature might not work in older devices or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`scrollbar-color`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the color of the scrollbar track and thumb.

The **track** refers to the background of the scrollbar, which is generally fixed regardless of the scrolling position.

The **thumb** refers to the moving part of the scrollbar, which usually floats on top of the track.

When `scrollbar-color` value is set on the document's root element, the values are applied to the viewport scrollbars.

**Note:** Browsers ignore the non-standard [`::-webkit-scrollbar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar)
 family of pseudo-elements on any element whose _computed_ `scrollbar-color` value is anything other than `auto`. Because `scrollbar-color` is inherited, this includes elements that don't set it themselves but inherit a non-`auto` value from an ancestor. Setting `scrollbar-color: auto` on such an element restores its `::-webkit-scrollbar-*` styling if it was previously removed by a `scrollbar-color` setting on an ancestor. See [Adding a fallback for scrollbar styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::-webkit-scrollbar#adding_a_fallback_for_scrollbar_styles)
.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#syntax)

-------------------------------------------------------------------------------------------------------

css

    /* Keyword value */
    scrollbar-color: auto;
    
    /* <color> values */
    scrollbar-color: rebeccapurple green; /* Two valid colors.
    The first applies to the thumb of the scrollbar, the second to the track. */
    
    /* Global values */
    scrollbar-color: inherit;
    scrollbar-color: initial;
    scrollbar-color: revert;
    scrollbar-color: revert-layer;
    scrollbar-color: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#values)

[`<scrollbar-color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#scrollbar-color_2)

Defines the color of the scrollbar.

|     |     |
| --- | --- |
| `auto` | Default platform rendering for the track portion of the scrollbar, in the absence of any other related scrollbar color properties. |
| `<color> <color>` | Applies the first color to the scrollbar thumb, the second to the scrollbar track. |

**Note:** [`@media (forced-colors: active)`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@media/forced-colors)
 sets `scrollbar-color` to `auto`.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#accessibility)

---------------------------------------------------------------------------------------------------------------------

When using `scrollbar-color` property with specific color values, authors should ensure the specified colors have enough contrast between them. For keyword values, UAs should ensure the colors they use have enough contrast. See [Techniques for WCAG 2.0: G183: Using a contrast ratio of 3:1](https://www.w3.org/TR/WCAG20-TECHS/G183.html "External link (opens in new tab)")
.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | scrolling boxes |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#formal_syntax)

---------------------------------------------------------------------------------------------------------------------

scrollbar-color =   
  auto        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  [<color>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
[{2}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#examples)

-----------------------------------------------------------------------------------------------------------

### [Coloring overflow scrollbars](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#coloring_overflow_scrollbars)

#### CSS

css

    .scroller {
      width: 300px;
      height: 100px;
      overflow-y: scroll;
      scrollbar-color: #000077 #bada55;
    }
    

#### HTML

html

    <div class="scroller">
      Veggies es bonus vobis, proinde vos postulo essum magis kohlrabi welsh onion
      daikon amaranth tatsoi tomatillo melon azuki bean garlic. Gumbo beet greens
      corn soko endive gumbo gourd. Parsley shallot courgette tatsoi pea sprouts
      fava bean collard greens dandelion okra wakame tomato. Dandelion cucumber
      earthnut pea peanut soko zucchini.
    </div>
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#specifications)

-----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Scrollbars Styling Module Level 1  <br>\# scrollbar-color](https://drafts.csswg.org/css-scrollbars/#scrollbar-color) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color#see_also)

-----------------------------------------------------------------------------------------------------------

*   [CSS overflow](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Overflow)
     module
*   [CSS scrollbars styling](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scrollbars_styling)
     module
*   [`overflow`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/overflow)
    
*   [`scrollbar-gutter`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-gutter)
    
*   [`scrollbar-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-width)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 16, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/scrollbar-color/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/scrollbar-color/index.md?plain=1 "Folder: en-us/web/css/reference/properties/scrollbar-color (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscrollbar-color&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscrollbar-color%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fscrollbar-color%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fscrollbar-color%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F880c2c4b113c6fe127ca3ae3603a56ef7a2eb9a6%0A*+Document+last+modified%3A+2026-09-16T20%3A20%3A23.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")