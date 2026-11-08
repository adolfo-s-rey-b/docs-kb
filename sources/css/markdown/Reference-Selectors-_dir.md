*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#mdn-search)
    

`:dir()` CSS pseudo-class
=========================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since December 2023.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`:dir()`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [pseudo-class](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Pseudo-classes)
 matches elements based on the directionality of the text contained in them.

css

    /* Selects any element with right-to-left text */
    :dir(rtl) {
      background-color: red;
    }
    

The `:dir()` pseudo-class uses only the _semantic_ value of the directionality, i.e., the one defined in the document itself. It doesn't account for _styling_ directionality, i.e., the directionality set by CSS properties such as [`direction`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/direction)
.

**Note:** Be aware that the behavior of the `:dir()` pseudo-class is not equivalent to the `[dir=…]` [attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/Attribute_selectors)
. The latter match the HTML [`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
 attribute, and ignore elements that lack it — even if they inherit a direction from their parent. (Similarly, `[dir=rtl]` and `[dir=ltr]` won't match the `auto` value.) In contrast, `:dir()` will match the value calculated by the [user agent](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
, even if inherited.

**Note:** In HTML, the direction is determined by the [`dir`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/dir)
 attribute. Other document types may have different methods.

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#syntax)

-------------------------------------------------------------------------------------------

css

    :dir([ltr | rtl]) {
      /* ... */
    }
    

### [Parameters](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#parameters)

The `:dir()` pseudo-class requires one parameter, representing the text directionality you want to target.

[`ltr`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#ltr)

Target left-to-right elements.

[`rtl`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#rtl)

Target right-to-left elements.

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#examples)

-----------------------------------------------------------------------------------------------

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#html)

html

    <div dir="rtl">
      <span>test1</span>
      <div dir="ltr">
        test2
        <div dir="auto">עִבְרִית</div>
      </div>
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#css)

css

    :dir(ltr) {
      background-color: yellow;
    }
    
    :dir(rtl) {
      background-color: powderblue;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#result)

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#specifications)

-----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# selector-ltr](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-ltr) |
| [HTML  <br>\# selector-rtl](https://html.spec.whatwg.org/multipage/semantics-other.html#selector-rtl) |
| [Selectors Level 4  <br>\# dir-pseudo](https://drafts.csswg.org/selectors/#dir-pseudo) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#browser_compatibility)

-------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir#see_also)

-----------------------------------------------------------------------------------------------

*   Language-related pseudo-classes: [`:lang`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:lang)
    
*   HTML [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang)
     attribute
*   HTML [`translate`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/translate)
     attribute

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 17, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:dir/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/selectors/_colon_dir/index.md?plain=1 "Folder: en-us/web/css/reference/selectors/_colon_dir (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Adir&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_dir%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FSelectors%2F%3Adir%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fselectors%2F_colon_dir%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Fbf90d24ddf56e3f60df25fcbc0d4e3e084004794%0A*+Document+last+modified%3A+2026-04-17T06%3A07%3A28.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")