*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#mdn-search)
    

`hyphenate-limit-chars` CSS property
====================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/184)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`hyphenate-limit-chars`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property specifies the minimum word length to allow hyphenation of words as well as the minimum number of characters before and after the hyphen.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Numeric values */
    hyphenate-limit-chars: 10 4 4;
    hyphenate-limit-chars: 10 4;
    hyphenate-limit-chars: 10;
    
    /* Keyword values */
    hyphenate-limit-chars: auto auto auto;
    hyphenate-limit-chars: auto auto;
    hyphenate-limit-chars: auto;
    
    /* Mix of numeric and keyword values */
    hyphenate-limit-chars: 10 auto 4;
    hyphenate-limit-chars: 10 auto;
    hyphenate-limit-chars: auto 3;
    
    /* Global values */
    hyphenate-limit-chars: inherit;
    hyphenate-limit-chars: initial;
    hyphenate-limit-chars: revert;
    hyphenate-limit-chars: revert-layer;
    hyphenate-limit-chars: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#values)

This property is specified as one to three values from the following list:

[`<integer>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)

Specifies either the number of characters for the minimum word length for hyphenation, the minimum number of characters before the hyphen, or the minimum number of characters after the hyphen.

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#auto)

Specifies the user agent to choose appropriate values for the current layout. This is the default.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#description)

-----------------------------------------------------------------------------------------------------------------------

The `hyphenate-limit-chars` property provides fine-grained control over hyphenation in text. This control enables you to avoid awkward hyphenations and set appropriate hyphenation for different languages, which, in turn, allows for better typography.

The property accepts one to three values, each an `<integer>` or the keyword `auto`, specifying the number of characters for the minimum word length for hyphenation, the minimum number of characters before the hyphen, and the minimum number of characters after the hyphen, in that order:

*   If one `<integer>` is specified, it sets the word length for the minimum number of characters a word must have in order for it to be able to be hyphenated, while the minimum number of characters before and after the hyphen are set to `auto`.
*   If two values are specified, the first value sets the minimum word length and the second sets the minimum number of characters both before and after the hyphen; the omitted third value defaults to the second value.
*   If three values are specified, they set the minimum word length, the minimum number of characters before the hyphen, and the minimum number of characters after the hyphen, respectively.

For `auto`, the user agent will choose an appropriate value for the current layout. Unless the user agent can calculate a better value, the following default values will be used:

*   Minimum word length to allow hyphenation: 5
*   Minimum number of characters before the hyphen: 2
*   Minimum number of characters after the hyphen: 2

Note that if a word is too short to meet the given constraints, it will not be hyphenated. For example, given a value like `hyphenate-limit-chars: auto 3 4`, words shorter than 7 characters will never be hyphenated, since it is impossible to have 3 characters before the hyphen and 4 characters after it.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | all elements |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

hyphenate-limit-chars =   
  [\[](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")\
 auto [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")\
 <integer \[0,∞\]> [\]](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#brackets "Brackets: enclose several entities, combinators, and multipliers to transform them as a single component")
[{1,3}](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#curly_braces "Curly braces: encloses two integers defining the minimal and maximal numbers of occurrences of the entity, or a single integer defining the exact number required")
    
  
[<integer>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/integer)
 =   
  <number-token>    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#examples)

-----------------------------------------------------------------------------------------------------------------

### [Setting hyphenation limits](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#setting_hyphenation_limits)

In this example, we have four boxes each containing the same text. For the purpose of comparison, the first box shows the default hyphenation applied by the browser. The next three boxes demonstrate the result of constraining the browser's default behavior using different `hyphenate-limit-chars` values.

#### HTML

html

    <div class="container">
      <p id="ex1">juxtaposition and acknowledgement</p>
      <p id="ex2">juxtaposition and acknowledgement</p>
      <p id="ex3">juxtaposition and acknowledgement</p>
      <p id="ex4">juxtaposition and acknowledgement</p>
    </div>
    

#### CSS

css

    .container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
    }
    
    p {
      margin: 1rem;
      width: 120px;
      border: 2px dashed #999999;
      font-size: 1.5rem;
      hyphens: auto;
    }
    
    #ex2 {
      hyphenate-limit-chars: 14;
    }
    
    #ex3 {
      hyphenate-limit-chars: 5 9 2;
    }
    
    #ex4 {
      hyphenate-limit-chars: 5 2 7;
    }
    

#### Result

In the first box, we don't set `hyphenate-limit-chars`, allowing the browser to apply its default algorithm. By default, the browser uses the values `5 2 2` unless it can find better values.

In the second box, we prevent the browser from hyphenating words unless they are at least 14 characters long by setting `hyphenate-limit-chars: 14`. As a result, "juxtaposition" is not hyphenated in the second box because it is only 13 characters long.

In the third box, we constrain the browser to include at least 9 characters before the hyphen by setting `hyphenate-limit-chars: 5 9 2`. The effect is that "acknowledgement" is now hyphenated as "acknowledge-ment" rather than the default version "acknowl-edgement", as shown in the first box.

Note that the browser does not have to include exactly 9 characters before the hyphen: as long as the constraints given in `hyphenate-limit-chars` are satisfied, the browser can break the word in the place it considers best. So in this case, for example, it chooses "acknowledge-ment" rather than the less readable "acknowled-gement".

In the fourth box, we make the browser include at least 7 characters after the hyphen by setting `hyphenate-limit-chars: 5 2 7`. The effect is that "juxtaposition" is hyphenated as "juxta-position" rather than the default "juxtaposi-tion".

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Text Module Level 4  <br>\# propdef-hyphenate-limit-chars](https://drafts.csswg.org/css-text-4/#propdef-hyphenate-limit-chars) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [`hyphens`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphens)
    
*   [CSS Text module](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Text)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Sep 28, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/hyphenate-limit-chars/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/hyphenate-limit-chars/index.md?plain=1 "Folder: en-us/web/css/reference/properties/hyphenate-limit-chars (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fhyphenate-limit-chars&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fhyphenate-limit-chars%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fhyphenate-limit-chars%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fhyphenate-limit-chars%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F367f942b096f97d4c3063e31a0dc5002736db81b%0A*+Document+last+modified%3A+2026-09-28T19%3A19%3A08.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")