*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child#mdn-search)
    

`:first-child` CSS pseudo-class
===============================

Baseline

Widely available

\*

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

\* Some parts of this feature may have varying levels of support.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:first-child`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 represents the first element among a group of sibling elements.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child#try_it)

---------------------------------------------------------------------------------------------------

    p {
      font-weight: bold;
    }
    
    li:first-child {
      border: 2px solid orange;
    }
    

    <p>Track &amp; field champions:</p>
    <ul>
      <li>Adhemar da Silva</li>
      <li>Wang Junxia</li>
      <li>Wilma Rudolph</li>
      <li>Babe Didrikson-Zaharias</li>
      <li>Betty Cuthbert</li>
      <li>Fanny Blankers-Koen</li>
      <li>Florence Griffith-Joyner</li>
      <li>Irena Szewinska</li>
      <li>Jackie Joyner-Kersee</li>
      <li>Shirley Strickland</li>
      <li>Carl Lewis</li>
      <li>Emil Zatopek</li>
      <li>Haile Gebrselassie</li>
      <li>Jesse Owens</li>
      <li>Jim Thorpe</li>
      <li>Paavo Nurmi</li>
      <li>Sergei Bubka</li>
      <li>Usain Bolt</li>
    </ul>
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child#syntax)

---------------------------------------------------------------------------------------------------

css

    :first-child {
      /* ... */
    }
    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child#examples)

-------------------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child#basic_example)

#### HTML

html

    <div>
      <p>This text is selected!</p>
      <p>This text isn't selected.</p>
    </div>
    
    <div>
      <h2>This text isn't selected: it's not a `p`.</h2>
      <p>This text isn't selected.</p>
    </div>
    

#### CSS

css

    p:first-child {
      color: lime;
      background-color: black;
      padding: 5px;
    }
    

#### Result

### [Styling a list](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child#styling_a_list)

#### HTML

html

    <ul>
      <li>Item 1</li>
      <li>Item 2</li>
      <li>
        Item 3
        <ul>
          <li>Item 3.1</li>
          <li>Item 3.2</li>
          <li>Item 3.3</li>
        </ul>
      </li>
    </ul>
    

#### CSS

css

    ul li {
      color: blue;
    }
    
    ul li:first-child {
      color: red;
      font-weight: bold;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [Selectors Level 4  <br>\# first-child-pseudo](https://drafts.csswg.org/selectors/#first-child-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child#see_also)

-------------------------------------------------------------------------------------------------------

*   [`:-moz-first-node`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:-moz-first-node)
    
*   [`:first-of-type`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-of-type)
    
*   [`:last-child`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:last-child)
    
*   [`:nth-child()`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:nth-child)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:first-child/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_first-child/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_first-child (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afirst-child&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_first-child%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Afirst-child%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_first-child%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")