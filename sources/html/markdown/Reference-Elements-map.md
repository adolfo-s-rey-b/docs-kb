*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#mdn-search)
    

`<map>` HTML image map element
==============================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<map>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element is used with [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
 elements to define an image map (a clickable link area).

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#try_it)

------------------------------------------------------------------------------------------

    <map name="infographic">
      <area
        shape="poly"
        coords="130,147,200,107,254,219,130,228"
        href="https://developer.mozilla.org/docs/Web/HTML"
        alt="HTML" />
      <area
        shape="poly"
        coords="130,147,130,228,6,219,59,107"
        href="https://developer.mozilla.org/docs/Web/CSS"
        alt="CSS" />
      <area
        shape="poly"
        coords="130,147,200,107,130,4,59,107"
        href="https://developer.mozilla.org/docs/Web/JavaScript"
        alt="JavaScript" />
    </map>
    <img
      usemap="#infographic"
      src="/shared-assets/images/examples/mdn-info2.png"
      alt="MDN infographic" />
    

    img {
      display: block;
      margin: 0 auto;
      width: 260px;
      height: 232px;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#attributes)

--------------------------------------------------------------------------------------------------

This element includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[`name`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#name)

The `name` attribute gives the map a name so that it can be referenced. The attribute must be present and must have a non-empty value with no space characters. The value of the `name` attribute must not be equal to the value of the `name` attribute of another `<map>` element in the same document. If the [`id`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/id)
 attribute is also specified, both attributes must have the same value.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#examples)

----------------------------------------------------------------------------------------------

### [Image map with two areas](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#image_map_with_two_areas)

Click the left-hand parrot for JavaScript, or the right-hand parrot for CSS.

#### HTML

html

    <!-- Photo by Juliana e Mariana Amorim on Unsplash -->
    <map name="primary">
      <area
        shape="circle"
        coords="75,75,75"
        href="https://developer.mozilla.org/docs/Web/JavaScript"
        target="_blank"
        alt="JavaScript" />
      <area
        shape="circle"
        coords="275,75,75"
        href="https://developer.mozilla.org/docs/Web/CSS"
        target="_blank"
        alt="CSS" />
    </map>
    <img
      usemap="#primary"
      src="parrots.jpg"
      alt="350 x 150 picture of two parrots" />
    

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | Any [transparent](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#transparent_content_model)<br> element. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | No `role` permitted |
| DOM interface | [`HTMLMapElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLMapElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-map-element](https://html.spec.whatwg.org/multipage/image-maps.html#the-map-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map#see_also)

----------------------------------------------------------------------------------------------

*   [`<a>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/a)
    
*   [`<area>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/area)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Apr 24, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/map/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/map/index.md?plain=1 "Folder: en-us/web/html/reference/elements/map (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmap&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmap%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fmap%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fmap%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F599ae8b7ad414e91df473d91983f4ffc5cafabb3%0A*+Document+last+modified%3A+2026-04-24T14%3A15%3A02.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")