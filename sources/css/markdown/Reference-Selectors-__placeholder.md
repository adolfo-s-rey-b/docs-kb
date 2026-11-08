*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#mdn-search)
    

`::placeholder` CSS pseudo-element
==================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since January 2020.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`::placeholder`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-element](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-elements)
 represents the [placeholder text](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input#placeholder)
 in an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 element.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#try_it)

----------------------------------------------------------------------------------------------------

    input {
      margin-top: 0.5rem;
    }
    
    input::placeholder {
      font-weight: bold;
      opacity: 0.5;
      color: red;
    }
    

    <label for="first-name">Your phone number:</label><br />
    
    <input
      id="first-name"
      type="tel"
      name="phone"
      minlength="9"
      maxlength="9"
      placeholder="It must be 9 digits" />
    

Only the subset of CSS properties that apply to the [`::first-line`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::first-line)
 pseudo-element can be used in a rule using `::placeholder` in its selector.

**Note:** In most browsers, the appearance of placeholder text is a translucent or light gray color by default.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#syntax)

----------------------------------------------------------------------------------------------------

css

    ::placeholder {
      /* ... */
    }
    

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#accessibility)

------------------------------------------------------------------------------------------------------------------

### [Color contrast](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#color_contrast)

#### Contrast Ratio

Placeholder text typically has a lighter color treatment to indicate that it is a suggestion for what kind of input will be valid, and is not actual input of any kind.

It is important to ensure that the contrast ratio between the color of the placeholder text and the background of the input is high enough that people experiencing low vision conditions will be able to read it while also making sure there is enough of a difference between the placeholder text and input text color that users do not mistake the placeholder for inputted data.

Color contrast ratio is determined by comparing the luminosity of the placeholder text and the input background color values. In order to meet current [Web Content Accessibility Guidelines (WCAG)](https://www.w3.org/WAI/standards-guidelines/wcag/ "External link (opens in new tab)")
, a ratio of 4.5:1 is required for text content and 3:1 for larger text such as headings. Large text is defined as 18.66px and bold or larger, or 24px or larger.

*   [WebAIM: Color Contrast Checker](https://webaim.org/resources/contrastchecker/ "External link (opens in new tab)")
    
*   [MDN Understanding WCAG, Guideline 1.4 explanations](https://developer.mozilla.org/en-US/docs/Web/Accessibility/Guides/Understanding_WCAG/Perceivable#guideline_1.4_make_it_easier_for_users_to_see_and_hear_content_including_separating_foreground_from_background)
    
*   [Understanding Success Criterion 1.4.3 | W3C Understanding WCAG 2.0](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html "External link (opens in new tab)")
    

#### Usability

Placeholder text with sufficient color contrast may be interpreted as entered input. Placeholder text will also disappear when a person enters content into an [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 element. Both of these circumstances can interfere with successful form completion, especially for people with cognitive concerns.

An alternate approach to providing placeholder information is to include it outside of the input in close visual proximity, then use [`aria-describedby`](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Attributes/aria-describedby)
 to programmatically associate the [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 with its hint.

With this implementation, the hint content is available even if information is entered into the input field, and the input appears free of preexisting input when the page is loaded. Most screen reading technology will use `aria-describedby` to read the hint after the input's label text is announced, and the person using the screen reader can mute it if they find the extra information unnecessary.

html

    <label for="user-email">Your email address</label>
    <span id="user-email-hint" class="input-hint">Example: jane@sample.com</span>
    <input
      id="user-email"
      aria-describedby="user-email-hint"
      name="email"
      type="email" />
    

*   [Placeholders in Form Fields Are Harmful — Nielsen Norman Group](https://www.nngroup.com/articles/form-design-placeholders/ "External link (opens in new tab)")
    

### [Windows High Contrast Mode](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#windows_high_contrast_mode)

Placeholder text will appear with the same styling as user-entered text content when rendered in [Windows High Contrast Mode](https://www.smashingmagazine.com/2022/06/guide-windows-high-contrast-mode/ "External link (opens in new tab)")
. This will make it difficult for some people to determine which content has been entered, and which content is placeholder text.

### [Labels](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#labels)

Placeholders are not a replacement for the [`<label>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label)
 element. Without a label that has been programmatically associated with an input using a combination of the [`for`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/label#for)
 and [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attributes, assistive technology such as screen readers cannot parse [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 elements.

*   [Placeholders in Form Fields Are Harmful — Nielsen Norman Group](https://www.nngroup.com/articles/form-design-placeholders/ "External link (opens in new tab)")
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#examples)

--------------------------------------------------------------------------------------------------------

### [Change placeholder appearance](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#change_placeholder_appearance)

This example shows some of the adjustments that you can make to the styles of placeholder text.

#### HTML

html

    <input placeholder="Type here" />
    

#### CSS

css

    input::placeholder {
      color: red;
      font-size: 1.2em;
      font-style: italic;
      opacity: 0.5;
    }
    

#### Result

### [Opaque text](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#opaque_text)

Some browsers make placeholder text less opaque. If you want fully opaque text, then set the [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
 property value explicitly. The [`currentColor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value#currentcolor_keyword)
 value can be used to have the same color as the corresponding input element.

#### HTML

html

    <input placeholder="Color set by browser" />
    <input placeholder="Same color as input" class="explicit-color" />
    <input placeholder="Semi-opaque text color" class="opacity-change" />
    

#### CSS

css

    input {
      font-weight: bold;
      color: green;
    }
    
    .explicit-color::placeholder {
      /* use the same color as input element to avoid the browser set default color */
      color: currentColor;
    }
    
    .opacity-change::placeholder {
      /* less opaque text */
      color: color-mix(in srgb, currentColor 70%, transparent);
    }
    

#### Result

**Note:** Note that browsers use different default colors for placeholder text. For example, Firefox uses the input element's color with 54% opacity, and Chrome uses `darkgray` color. If you want consistent placeholder text color across the browsers, then set the `color` explicitly.

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#specifications)

--------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Pseudo-Elements Module Level 4  <br>\# placeholder-pseudo](https://drafts.csswg.org/css-pseudo/#placeholder-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#browser_compatibility)

----------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder#see_also)

--------------------------------------------------------------------------------------------------------

*   The [`:placeholder-shown`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:placeholder-shown)
     pseudo-class styles an element that _has_ an active placeholder.
*   Related HTML elements: [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
    , [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
    
*   [HTML forms](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::placeholder/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_doublecolon_placeholder/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_doublecolon_placeholder (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aplaceholder&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_placeholder%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3A%3Aplaceholder%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_doublecolon_placeholder%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F6cf697a8965ecdc4967258cc0282fe789b60318e%0A*+Document+last+modified%3A+2026-04-17T06%3A04%3A50.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")