*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#mdn-search)
    

Contribute a recipe
===================

If you would like to contribute an example for the Layout Cookbook, then this page explains the steps to take to have your example published.

[What makes a good recipe?](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#what_makes_a_good_recipe)

--------------------------------------------------------------------------------------------------------------------------------------------------

**The simplest possible version of any useful web design pattern**. Each line of CSS that you include should be there to help demonstrate the pattern, so leave out anything there purely to make the example look pretty. The idea is that someone can take the pattern and use it in a site with their own styles.

A recipe consists of:

*   A live example, stored in the [CSS Examples GitHub repo](https://github.com/mdn/css-examples "External link (opens in new tab)")
    .
*   A downloadable version of that example, also stored in the CSS Examples repo.
*   A page in the [CSS layout cookbook](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook)
     section of the site, which should include the following components:
    1.  Introduction
    2.  Requirements
    3.  Recipe
    4.  Decisions
    5.  Useful fallbacks or alternative methods (when relevant)
    6.  Accessibility concerns
    7.  Browser compatibility (only for CSS properties not fully supported)
    8.  Additional resources

[Steps to publish a recipe](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#steps_to_publish_a_recipe)

---------------------------------------------------------------------------------------------------------------------------------------------------

To create a recipe and add it to the CSS layout cookbook, follow these steps:

*   [What makes a good recipe?](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#what_makes_a_good_recipe)
    
*   [Steps to publish a recipe](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#steps_to_publish_a_recipe)
    *   [1\. Build a pattern](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#1._build_a_pattern)
        
    *   [2\. Create a live example](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#2._create_a_live_example)
        
    *   [3\. Create a downloadable version](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#3._create_a_downloadable_version)
        
    *   [4\. Open a pull request with your example](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#4._open_a_pull_request_with_your_example)
        
    *   [5\. Create your page](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#5._create_your_page)
        

### [1\. Build a pattern](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#1._build_a_pattern)

Before turning your example into a recipe, start by creating your pattern as a basic HTML page. Think about what you are trying to demonstrate and keep it as simple as possible. Use descriptive words like "container" or "item" if adding class names.

Ensure that you've tested the HTML and CSS across multiple browsers, viewport sizes, and devices. Also ensure that any CSS styling follows accessibility guidelines. While it's okay to use CSS properties with limited support, be sure to include browser support information when creating the page, particularly in the browser compatibility section. In some cases, creating a second version of your example with fallback support can be helpful.

### [2\. Create a live example](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#2._create_a_live_example)

The live examples on cookbook pages, such as for [centering an element](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element)
, and elsewhere on MDN allow readers to play with the code and change relevant parts without being overwhelmed with all of the code. Your recipe will be demonstrated by way of one or more examples.

Fork the [CSS Examples repo](https://github.com/mdn/css-examples "External link (opens in new tab)")
 and then take a look in the `css-cookbook` folder. There is a [cookbook-template.html](https://github.com/mdn/css-examples/blob/main/css-cookbook/cookbook-template.html "External link (opens in new tab)")
 file. Copy this file and use it as a starting point. Save this in the `css-cookbook` directory with a name that makes sense for your pattern. The template contains comments to guide you in adding various parts at the appropriate places.

The important parts of this template are as follows:

*   There is a stylesheet for the editor panels with some basic body styling and a JavaScript file for the editor functionality. Leave these files as they are.
    
*   The `<head>` contains two style blocks. The first style block is for elements that readers do not need to change to play with the example. The second style block contains items that readers might want to play with. We typically add all our CSS to the first block, then choose the rules to move to the second block. The rules in the second block should be those that are fundamental to the pattern, perhaps those where a reader can change a CSS value and see the pattern update.
    
*   You need to add the HTML for your component twice: first inside the section with the class `preview`, and then inside the `<textarea>` with the class `playable-html`.
    
*   The editable CSS from the second `<head>` block must also be copied into the `playable-css` section.
    

A working example is [center.html](https://github.com/mdn/css-examples/blob/main/css-cookbook/center.html "External link (opens in new tab)")
, which is embedded on the page [Center an element](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Center_an_element)
. You can use this to see how to add the various bits correctly.

If you've forked the repo and have our CSS and JavaScript files with your example, opening your live example in a browser should display everything working exactly as it would appear on an MDN page.

#### Useful tips

*   Do not indent the CSS and HTML inside the text areas; instead, align the code with the start of the lines. This will look better when it is rendered.
*   If any images are required, put them in the directory with the examples. You are welcome to use any images already present.
*   You can adjust the height of the text areas by changing the height in the inline styles.

### [3\. Create a downloadable version](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#3._create_a_downloadable_version)

As the examples include all of our live example code, we want to provide readers with just the code they need for their example, omitting any unnecessary items. Create a copy of your live example, and add `--download` to its name. For example, the download version of `center.html` is `center--download.html`. This file will be similar to your initial example. It should be a basic version of your pattern as a single HTML page.

It can be handy to include the body CSS rules from our included stylesheet. Take a look at [`cookbook-template--download.html`](https://github.com/mdn/css-examples/blob/main/css-cookbook/cookbook-template--download.html "External link (opens in new tab)")
 as a guide; these rules are provided as a starting point.

### [4\. Open a pull request with your example](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#4._open_a_pull_request_with_your_example)

Open a pull request (PR) on the [CSS Examples repo](https://github.com/mdn/css-examples/pulls "External link (opens in new tab)")
. This allows us to help you with any changes to the example that may be needed before you create your page. Plus, the example will need to be live to be included. This is why it makes sense to first create the code examples and then the explanatory guide. In your PR, explain the pattern and what you are demonstrating. See our [guidelines for opening a pull request](https://developer.mozilla.org/en-US/docs/MDN/Community/Pull_requests#open_a_pull_request)
.

### [5\. Create your page](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#5._create_your_page)

After your example PR is merged, open a pull request to create a new page in the [Layout Cookbook directory](https://github.com/mdn/content/tree/main/files/en-us/web/css/how_to/layout_cookbook "External link (opens in new tab)")
. Use our [template for Cookbook pages](https://github.com/mdn/content/blob/main/files/en-us/web/css/how_to/layout_cookbook/contribute_a_recipe/cookbook_template/index.md?plain=1 "External link (opens in new tab)")
. The template explains the requirements of each section, and you can refer to other cookbook examples for more help.

Remember to add a link to your new recipe on the main [Layout cookbook](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook)
 page.

If you have any questions or want someone to take a look at your page, get in touch via any of our [communication channels](https://developer.mozilla.org/en-US/docs/MDN/Community/Communication_channels)
.

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe#see_also)

-----------------------------------------------------------------------------------------------------------------

*   [Cookbook page template](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe/Cookbook_template)
    
*   [CSS Examples repo](https://github.com/mdn/css-examples "External link (opens in new tab)")
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Oct 31, 2025 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/How_to/Layout_cookbook/Contribute_a_recipe/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/how_to/layout_cookbook/contribute_a_recipe/index.md?plain=1 "Folder: en-us/web/css/how_to/layout_cookbook/contribute_a_recipe (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FContribute_a_recipe&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fcontribute_a_recipe%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FHow_to%2FLayout_cookbook%2FContribute_a_recipe%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Fhow_to%2Flayout_cookbook%2Fcontribute_a_recipe%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F55326f330a6ae829494c7606b1bd47b2c0f9d888%0A*+Document+last+modified%3A+2025-10-31T00%3A41%3A06.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")