*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface#mdn-search)
    

CSS basic user interface
========================

The **CSS basic user interface** module allows you to define the rendering and functionality of features related to the user interface, including outline properties, visual feedback for pointing devices and keyboards, and modifying the default appearance of UI widgets.

Basic user interface properties can be used to improve user experience and accessibility by providing visual cues to elements that are being interacted with, including styling mouse cursors and keyboard directional focus navigation, and styling caret cursors when an editable element has focus. The module includes features for providing outlines to focused (or unfocused) elements without impacting an element's [box model](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/Styling_basics/Box_model#what_is_the_css_box_model)
 dimensions and styling. This UI module also enables the styling of user interface controls.

[Basic user interface in action](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface#basic_user_interface_in_action)

----------------------------------------------------------------------------------------------------------------------------------------------

To view how basic user interface properties can alter the appearance of UI features, interact with the elements in this sample. Note that some features in this sample improve usability while others harm user experience.

The CSS [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
 and [`outline-offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset)
 properties were used to provide feedback to users on which element currently has focus. An [`accent-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/accent-color)
 provides a theme color to all the form controls. The caret that appears when the text is edited has the same color thanks to the [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
 property. These can all be considered UI improvements.

Some features harm usability. The [`cursor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor)
 property was used to change cursors from the browser default, which is confusing. The [`resize`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize)
 property prevents the second [`<textarea>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/textarea)
 from being resizable while the [`pointer-events`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events)
 property prevents the third `<textarea>` from receiving click events. It is still focusable using the keyboard.

Click "Play" in the example above to see or edit the code for the animation in the MDN Playground.

[Reference](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface#reference)

----------------------------------------------------------------------------------------------------

### [Properties](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface#properties)

*   [`accent-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/accent-color)
    
*   [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
    
*   [`caret-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)
    
*   [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
    
*   [`caret-shape`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape)
    
*   [`cursor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor)
    
*   [`interest-delay`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay)
    , shorthand for:
    *   [`interest-delay-start`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-start)
        
    *   [`interest-delay-end`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/interest-delay-end)
        
*   [`outline`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline)
    , shorthand for:
    *   [`outline-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-color)
        
    *   [`outline-style`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-style)
        
    *   [`outline-width`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-width)
        
*   [`outline-offset`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/outline-offset)
    
*   [`pointer-events`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/pointer-events)
    
*   [`resize`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/resize)
    
*   [`user-select`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/user-select)
    

The CSS basic user interface module also defines the [`caret`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret)
, `nav-down`, `nav-left`, `nav-right`, and `nav-up` properties. Currently, no browsers support these features.

[Guides](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface#guides)

----------------------------------------------------------------------------------------------

[Learn forms: advanced form styling](https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Forms/Advanced_form_styling)

Explains how [`appearance`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/appearance)
 can be used to style form controls.

[Related concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface#related_concepts)

------------------------------------------------------------------------------------------------------------------

*   CSS [`cursor`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/cursor)
     property
*   SVG [`cursor`](https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Attribute/cursor)
     attribute
*   CSS [`:focus`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus)
    , [`:focus-within`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-within)
    , and [`:focus-visible`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:focus-visible)
     pseudoclasses
*   [`CaretPosition`](https://developer.mozilla.org/en-US/docs/Web/API/CaretPosition)
     Interface

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface#specifications)

--------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 3 (CSS3 UI)](https://drafts.csswg.org/css-ui-3/) |
| [CSS Basic User Interface Module Level 4](https://drafts.csswg.org/css-ui/) |

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface#see_also)

--------------------------------------------------------------------------------------------------

*   [Tips for Designing Useful and Usable Focus Indicators](https://www.deque.com/blog/give-site-focus-tips-designing-usable-focus-indicators/ "External link (opens in new tab)")
     (2016)

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Dec 5, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/guides/basic_user_interface/index.md?plain=1 "Folder: en-us/web/css/guides/basic_user_interface (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBasic_user_interface&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fguides%2Fbasic_user_interface%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FGuides%2FBasic_user_interface%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fguides%2Fbasic_user_interface%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F1dbba9f7a2c2e35c6e01e8a63159e2aac64b601b%0A*+Document+last+modified%3A+2025-12-05T16%3A09%3A35.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")