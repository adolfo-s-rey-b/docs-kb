*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#mdn-search)
    

Center an element
=================

In this recipe, you will see how to center one box inside another by using [flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#using_flexbox)
 and [grid](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#using_grid)
, centering content both horizontally and vertically.

![an element centered inside a larger box](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element/cookbook-center.png)

[Requirements](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#requirements)

-----------------------------------------------------------------------------------------------------------------------

To place an item into the center of another box horizontally and vertically.

[Recipe](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#recipe)

-----------------------------------------------------------------------------------------------------------

Click "Play" in the code blocks below to edit the example in the MDN Playground:

html

    <div class="container">
      <div class="item">I am centered!</div>
    </div>
    

css

    .item {
      border: 2px solid rgb(95 97 110);
      border-radius: 0.5em;
      padding: 20px;
      width: 10em;
    }
    
    .container {
      border: 2px solid rgb(75 70 74);
      border-radius: 0.5em;
      font: 1.2em sans-serif;
    
      height: 200px;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    

[Using flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#using_flexbox)

-------------------------------------------------------------------------------------------------------------------------

To center a box within another box, first turn the containing box into a [flex container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Flexible_box_layout/Basic_concepts#the_flex_container)
 by setting its [`display`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/display)
 property to `flex`. Then set [`align-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-items)
 to `center` for vertical centering (on the block axis) and [`justify-content`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/justify-content)
 to `center` for horizontal centering (on the inline axis). And that's all it takes to center one box inside another!

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#html)

html

    <div class="container">
      <div class="item">I am centered!</div>
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#css)

css

    div {
      border: solid 3px;
      padding: 1em;
      max-width: 75%;
    }
    
    .item {
      border: 2px solid rgb(95 97 110);
      border-radius: 0.5em;
      padding: 20px;
      width: 10em;
    }
    
    .container {
      height: 8em;
      border: 2px solid rgb(75 70 74);
      border-radius: 0.5em;
      font: 1.2em sans-serif;
    
      display: flex;
      align-items: center;
      justify-content: center;
    }
    

We set a height for the container to demonstrate that the inner item is indeed vertically centered within the container.

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#result)

Instead of applying `align-items: center;` on the container, you can also vertically center the inner item by setting [`align-self`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/align-self)
 to `center` on the inner item itself.

[Using grid](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#using_grid)

-------------------------------------------------------------------------------------------------------------------

Another method you can use for centering one box inside another is to first make the containing box a [grid container](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Grid_layout/Basic_concepts#grid_container)
 and then set its [`place-items`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-items)
 property to `center` to center align its items on both the block and inline axes.

### [HTML](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#html_2)

html

    <div class="container">
      <div class="item">I am centered!</div>
    </div>
    

### [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#css_2)

css

    div {
      border: solid 3px;
      padding: 1em;
      max-width: 75%;
    }
    
    .item {
      border: 2px solid rgb(95 97 110);
      border-radius: 0.5em;
      padding: 20px;
      width: 10em;
    }
    
    .container {
      height: 8em;
      border: 2px solid rgb(75 70 74);
      border-radius: 0.5em;
      font: 1.2em sans-serif;
    
      display: grid;
      place-items: center;
    }
    

### [Result](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#result_2)

Instead of applying `place-items: center;` on the container, you can achieve the same centering by setting [`place-content: center;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-content)
 on the container or by applying either [`place-self: center`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/place-self)
 or [`margin: auto;`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/margin)
 on the inner item itself.

[Resources on MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element#resources_on_mdn)

-------------------------------------------------------------------------------------------------------------------------------

*   [Box alignment in flexbox](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment/In_flexbox)
    
*   [CSS box alignment guide](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Box_alignment)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Nov 7, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/how_to/layout_cookbook/center_an_element/index.md?plain=1 "Folder: en-us/web/css/how_to/layout_cookbook/center_an_element (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FCenter_an_element&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fcenter_an_element%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FCenter_an_element%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fcenter_an_element%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F85fccefc8066bd49af4ddafc12c77f35265c7e2d%0A*+Document+last+modified%3A+2025-11-07T15%3A58%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")