*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#mdn-search)
    

`speak-as` CSS at-rule descriptor
=================================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`speak-as`** descriptor specifies how a counter symbol constructed with a given [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
 will be represented in the spoken form. For example, an author can specify a counter symbol to be either spoken as its numerical value or just represented with an audio cue.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#syntax)

-------------------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    speak-as: auto;
    speak-as: bullets;
    speak-as: numbers;
    speak-as: words;
    speak-as: spell-out;
    
    /* @counter-style name value */
    speak-as: <counter-style-name>;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#values)

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#auto)

If the value of `speak-as` is specified as `auto`, then the effective value of `speak-as` will be determined based on the value of the [`system`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system)
 descriptor:

*   If the value of `system` is `alphabetic`, the effective value of `speak-as` will be `spell-out`.
*   If `system` is `cyclic`, the effective value of `speak-as` will be `bullets`.
*   If `system` is `extends`, the value of `speak-as` will be the same as if `speak-as: auto` is specified on the extended style.
*   For all other cases, specifying `auto` has the same effect as specifying `speak-as: numbers`.

[`bullets`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#bullets)

A phrase or an audio cue defined by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 for representing an unordered list item will be read out.

[`numbers`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#numbers)

The numerical value of the counter will be read out in the document language.

[`words`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#words)

The user agent will generate a counter value as normal and read it out as a word in the document language.

[`spell-out`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#spell-out)

The user agent will generate a counter representation as normal and would read it out letter by letter. If the user agent doesn't know how to read out a particular counter symbol, the user agent might read it out as if the value of `speak-as` was `numbers`.

[`<counter-style-name>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#counter-style-name)

The name of another counter style, specified as a [`<custom-ident>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
. If included, the counter will be spoken out in the form specified in that counter style, kind of like specifying the [`fallback`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/fallback)
 descriptor. If the specified style does not exist, `speak-as` defaults to `auto`.

[Accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#accessibility)

---------------------------------------------------------------------------------------------------------------------------

Assistive technology support is very limited for the `speak-as` property. Do not rely on it to convey information critical to understanding the page's purpose.

[Let's Talk About Speech CSS | CSS Tricks](https://css-tricks.com/lets-talk-speech-css/ "External link (opens in new tab)")
 (2017)

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#formal_definition)

-----------------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| Related [at-rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules) | [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style) |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

speak-as =   
  auto                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bullets               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  numbers               [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  words                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  spell-out             [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  <counter-style-name>    
  
<counter-style-name> =   
  [<custom-ident>](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/custom-ident)
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#examples)

-----------------------------------------------------------------------------------------------------------------

### [Setting the spoken form for a counter](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#setting_the_spoken_form_for_a_counter)

In this example, the counter system is fixed with unintelligible symbols used for the visual markers. However, the `speak-as` descriptor is used to set the list item markers as numbers in the accessibility tree. When supported, numbers rather than visual markers will be read out by screen readers.

To experience the result of the `speak-as` descriptor, use assistive technology such as VoiceOver or another screen reader or view the [accessibility panel](https://firefox-source-docs.mozilla.org/devtools-user/index.html#accessibility-inspector "External link (opens in new tab)")
 in the developer tools of a browser that supports `speak-as`.

#### HTML

html

    <ul class="list">
      <li>I had one apple</li>
      <li>I ate two bananas</li>
      <li>I devoured three oranges</li>
      <li>I am not hungry for dinner</li>
      <li>But I'll have five scoops of ice cream for dessert</li>
    </ul>
    

#### CSS

css

    @counter-style speak-as-example {
      system: fixed;
      symbols:     ;
      suffix: " ";
      speak-as: numbers;
    }
    
    .list {
      list-style: speak-as-example;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#specifications)

-----------------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Counter Styles Level 3  <br>\# counter-style-speak-as](https://drafts.csswg.org/css-counter-styles/#counter-style-speak-as) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as#see_also)

-----------------------------------------------------------------------------------------------------------------

*   Other [`@counter-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style)
     descriptors: [`system`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/system)
    , [`symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/symbols)
    , [`additive-symbols`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/additive-symbols)
    , [`negative`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/negative)
    , [`prefix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/prefix)
    , [`suffix`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/suffix)
    , [`range`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/range)
    , [`pad`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/pad)
    , and [`fallback`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/fallback)
    
*   [`list-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style)
    , [`list-style-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-image)
    , [`list-style-position`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/list-style-position)
    
*   [`symbols()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/symbols)
    : the functional notation for creating anonymous counter styles.
*   [CSS counter styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Counter_styles)
     module
*   [CSS lists and counters](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Lists)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/At-rules/@counter-style/speak-as/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/at-rules/@counter-style/speak-as/index.md?plain=1 "Folder: en-us/web/css/reference/at-rules/@counter-style/speak-as (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40counter-style%2Fspeak-as&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40counter-style%2Fspeak-as%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FAt-rules%2F%40counter-style%2Fspeak-as%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fat-rules%2F%40counter-style%2Fspeak-as%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff0094356d3acb19475dde45508dfeac6abf596db%0A*+Document+last+modified%3A+2026-04-20T00%3A36%3A32.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")