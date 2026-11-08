*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-security#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-security#mdn-search)
    

`-webkit-text-security` CSS property
====================================

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

**`-webkit-text-security`** is a non-standard CSS property that obfuscates characters in a [`<form>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/form)
 field (such as [`<input>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/input)
 or [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
) by replacing them with a shape. It only affects fields that are _not_ of `type=password`.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-security#syntax)

-------------------------------------------------------------------------------------------------------------

css

    -webkit-text-security: circle;
    -webkit-text-security: disc;
    -webkit-text-security: square;
    -webkit-text-security: none;
    
    /* Global values */
    -webkit-text-security: inherit;
    -webkit-text-security: initial;
    -webkit-text-security: revert;
    -webkit-text-security: revert-layer;
    -webkit-text-security: unset;
    

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-security#formal_syntax)

---------------------------------------------------------------------------------------------------------------------------

\-webkit-text-security =   
  circle  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  disc    [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  square  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  none      

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-security#examples)

-----------------------------------------------------------------------------------------------------------------

### [Obscuring a text input](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-security#obscuring_a_text_input)

Try typing in the field below. If your browser supports this property, the characters should be visually replaced with squares.

#### HTML

html

    <label for="name">Name:</label> <input type="text" name="name" id="name" />
    

#### CSS

css

    input {
      -webkit-text-security: square;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-security#specifications)

-----------------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-security#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-security#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [WebKit CSS extensions](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Webkit_extensions)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 20, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-webkit-text-security/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/-webkit-text-security/index.md?plain=1 "Folder: en-us/web/css/reference/properties/-webkit-text-security (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-text-security&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-text-security%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2F-webkit-text-security%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2F-webkit-text-security%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbcbb4bd6a80292c0663b723d5466759cfaaa8315%0A*+Document+last+modified%3A+2026-04-20T01%3A47%3A07.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")