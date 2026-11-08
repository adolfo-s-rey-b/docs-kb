*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#mdn-search)
    

`user-modify` CSS property
==========================

Deprecated

Avoid using this feature in new projects. This feature may be a candidate for removal from web standards or browsers.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Non-standard:** This feature is not standardized. We do not recommend using non-standard features in production, as they have limited browser support, and may change or be removed. However, they can be a suitable alternative in specific cases where no standard option exists.

The **`user-modify`** property has no effect in Firefox. It was originally planned to determine whether or not the content of an element can be edited by a user.

**Warning:** This property has been replaced by the [`contenteditable`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/contenteditable)
 attribute.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#syntax)

---------------------------------------------------------------------------------------------------

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#values)

This property is specified as one of the following keyword values:

[`read-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#read-only)

Default value. Contents are read-only.

[`read-write`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#read-write)

The user is able to read and write contents.

[`read-write-plaintext-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#read-write-plaintext-only)

Same as `read-write`, but rich text formatting will be lost.

[`write-only`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#write-only)

The user is able to edit the content, but not to read it.

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

user-modify =   
  read-only                  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  read-write                 [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  read-write-plaintext-only  [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  write-only                   

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#examples)

-------------------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#html)

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#css)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#specifications)

-------------------------------------------------------------------------------------------------------------------

Not part of any standard.

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify#see_also)

-------------------------------------------------------------------------------------------------------

*   [`-moz-user-focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-focus)
    
*   [`-moz-user-input`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/-moz-user-input)
    
*   [`-moz-user-select`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 21, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-modify/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/user-modify/index.md?plain=1 "Folder: en-us/web/css/reference/properties/user-modify (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fuser-modify&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fuser-modify%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fuser-modify%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fuser-modify%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fca6052779ddca9f6d99665f12c39aa2d85d85733%0A*+Document+last+modified%3A+2026-08-21T13%3A37%3A31.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")