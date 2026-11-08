*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors#mdn-search)
    

Class selectors
===============

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 **class selector** matches elements based on the contents of their [`class`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/class)
 attribute.

css

    /* All elements with class="spacious" */
    .spacious {
      margin: 2em;
    }
    
    /* All <li> elements with class="spacious" */
    li.spacious {
      margin: 2em;
    }
    
    /* All <li> elements with a class list that includes both "spacious" and "elegant" */
    /* For example, class="elegant retro spacious" */
    li.spacious.elegant {
      margin: 2em;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors#syntax)

------------------------------------------------------------------------------------------------------

css

    .class_name {
      /* … */
    }
    

Note that this is equivalent to the following [attribute selector](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
:

css

    [class~="class_name"] {
      /* … */
    }
    

The `class_name` value must be a valid [CSS identifier](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident)
. HTML `class` attributes which are not valid CSS identifiers must be [escaped](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/ident#escaping_characters)
 before they can be used in class selectors.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors#examples)

----------------------------------------------------------------------------------------------------------

### [Valid class selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors#valid_class_selectors)

#### HTML

html

    <p class="red">This paragraph has red text.</p>
    <p class="red yellow-bg">
      This paragraph has red text and a yellow background.
    </p>
    <p class="red fancy">This paragraph has red text and "fancy" styling.</p>
    <p>This is just a regular paragraph.</p>
    

html

    <!-- The next two paragraphs have class attributes
    that contain characters which must be escaped in CSS -->
    
    <p class="item?one">This paragraph has a pink background.</p>
    <p class="123item">This paragraph has a yellow background.</p>
    

#### CSS

css

    .red {
      color: #ff3333;
    }
    
    .yellow-bg {
      background: #ffffaa;
    }
    
    .fancy {
      font-weight: bold;
      text-shadow: 4px 4px 3px #7777ff;
    }
    

css

    /* In the next two rules, the class attributes must be escaped */
    
    .item\?one {
      background-color: pink;
    }
    
    .\00003123item {
      background-color: yellow;
    }
    

#### Result

### [Invalid class selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors#invalid_class_selectors)

The class selectors in the following rules are not valid CSS identifiers, and will be ignored.

css

    .item?one {
      background-color: green;
    }
    
    .123item {
      background-color: green;
    }
    

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors#specifications)

----------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# class-html](https://drafts.csswg.org/selectors/#class-html) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors#see_also)

----------------------------------------------------------------------------------------------------------

*   [CSS Selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors)
    
*   [Learn CSS: Basic selectors](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Basic_selectors)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Class_selectors/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/class_selectors/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/class_selectors (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FClass_selectors&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fclass_selectors%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2FClass_selectors%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2Fclass_selectors%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")