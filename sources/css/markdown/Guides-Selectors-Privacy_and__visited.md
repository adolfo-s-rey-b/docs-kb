*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Privacy_and_:visited#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Privacy_and_:visited#mdn-search)
    

Privacy and the :visited selector
=================================

Originally, the [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 [`:visited`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:visited)
 selector was a privacy and security risk. With a little bit of JavaScript, websites could uncover a user's browsing history and figure out what sites the user had visited. This was done using methods like [`window.getComputedStyle`](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle)
 and other techniques. This process was quick, enabling websites to not only determine where the user had been on the web, but also to guess a lot of information about the user's identity.

To mitigate this privacy concern, browsers limit the amount of information that can be obtained from visited links.

[Little white lies](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Privacy_and_:visited#little_white_lies)

------------------------------------------------------------------------------------------------------------------------------

To preserve users' privacy, browsers lie to web applications under certain circumstances:

*   The `window.getComputedStyle` method and similar functions, such as [`element.querySelector`](https://developer.mozilla.org/en-US/docs/Web/API/Element/querySelector)
    , always return values indicating that a user has never visited any of the links on a page.
*   When using a sibling selector, such as `:visited + span`, the adjacent element (`span` in this example) is styled as though the link were unvisited.
*   In rare scenarios, if you're using nested link elements and the element being matched is different from the link whose presence in history is being tested, the element will be rendered as though the link were unvisited.

[Limits to visited link styles](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Privacy_and_:visited#limits_to_visited_link_styles)

------------------------------------------------------------------------------------------------------------------------------------------------------

You can style visited links, but there are limits to which styles you can use. Only the following styles can be applied to visited links:

*   [`color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/color)
    
*   [`background-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-color)
    
*   [`border-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/border-color)
     (and its sub-properties)
*   [`column-rule-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/column-rule-color)
    
*   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
    
*   [`text-decoration-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-decoration-color)
    
*   [`text-emphasis-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/text-emphasis-color)
    
*   Color parts of the [`fill`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/fill)
     and [`stroke`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/stroke)
     attributes

In addition, even for the styles mentioned above, transparency differences between unvisited and visited links are not applied. This restriction prevents the use of the `alpha` parameter in various [`<color>`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/color_value)
 functions or the [`transparent`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/named-color#transparent)
 keyword to distinguish between the two states.

Here is an example of how to use styles with the aforementioned restrictions:

[Impact on web developers](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Privacy_and_:visited#impact_on_web_developers)

--------------------------------------------------------------------------------------------------------------------------------------------

You may want to consider the following when developing sites:

*   Changing [`background-image`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/background-image)
     values based on a link's visited state will not work since only colors can be used to style visited links.
*   Colors that are otherwise transparent will not apply when styled via a `:visited` selector.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Privacy_and_:visited#see_also)

------------------------------------------------------------------------------------------------------------

*   [Preventing attacks on a user's history through CSS `:visited` selectors](https://dbaron.org/mozilla/visited-privacy "External link (opens in new tab)")
     (2010)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Selectors/Privacy_and_:visited/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/selectors/privacy_and__colon_visited/index.md?plain=1 "Folder: en-us/web/css/guides/selectors/privacy_and__colon_visited (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSelectors%2FPrivacy_and_%3Avisited&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fselectors%2Fprivacy_and__colon_visited%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FSelectors%2FPrivacy_and_%3Avisited%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fselectors%2Fprivacy_and__colon_visited%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")