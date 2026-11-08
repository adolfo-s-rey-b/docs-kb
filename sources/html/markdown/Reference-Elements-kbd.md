*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#mdn-search)
    

`<kbd>` HTML keyboard input element
===================================

Baseline

Widely available

This feature is well established and works across many devices and browser versions. It’s been available across browsers since July 2015.

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

The **`<kbd>`** [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
 element represents user input (typically keyboard input). By default, the content text is displayed using the [user agent's](https://developer.mozilla.org/en-US/docs/Glossary/User_agent)
 default monospace font.

`<kbd>` may be nested in various combinations with the [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
 (Sample Output) element to represent various forms of input or output based on visual cues.

[Try it](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#try_it)

------------------------------------------------------------------------------------------

    <p>
      Please press <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>R</kbd> to re-render an
      MDN page.
    </p>
    

    kbd {
      background-color: #eeeeee;
      border-radius: 3px;
      border: 1px solid #b4b4b4;
      box-shadow:
        0 1px 1px rgb(0 0 0 / 0.2),
        0 2px 0 0 rgb(255 255 255 / 0.7) inset;
      color: #333333;
      display: inline-block;
      font-size: 0.85em;
      font-weight: bold;
      line-height: 1;
      padding: 2px 4px;
      white-space: nowrap;
    }
    

[Attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#attributes)

--------------------------------------------------------------------------------------------------

This element only includes the [global attributes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes)
.

[Usage notes](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#usage_notes)

----------------------------------------------------------------------------------------------------

Other elements can be used in tandem with `<kbd>` to represent more specific scenarios:

*   Nesting a `<kbd>` element within another `<kbd>` element represents an actual key or other unit of input as a portion of a larger input. See [Representing keystrokes within an input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#representing_keystrokes_within_an_input)
     below.
*   Nesting a `<kbd>` element inside a [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
     element represents input that has been echoed back to the user by the system. See [Echoed input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#echoed_input)
    , below, for an example.
*   Nesting a `<samp>` element inside a `<kbd>` element, on the other hand, represents input which is based on text presented by the system, such as the names of menus and menu items, or the names of buttons displayed on the screen. See the example under [Representing onscreen input options](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#representing_onscreen_input_options)
     below.

**Note:** You can define a custom style to override the browser's default font selection for the `<kbd>` element, although the user's preferences may potentially override your CSS.

[Examples](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#examples)

----------------------------------------------------------------------------------------------

### [Basic example](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#basic_example)

html

    <p>
      Use the command <kbd>help my-command</kbd> to view documentation for the
      command "my-command".
    </p>
    

#### Result

### [Representing keystrokes within an input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#representing_keystrokes_within_an_input)

To describe an input comprised of multiple keystrokes, you can nest multiple `<kbd>` elements, with an outer `<kbd>` element representing the overall input and each individual keystroke or component of the input enclosed within its own `<kbd>`.

#### Unstyled

First, let's look at what this looks like as just plain HTML.

##### HTML

html

    <p>
      You can also create a new document using the
      <kbd><kbd>Ctrl</kbd>+<kbd>N</kbd></kbd> keyboard shortcut.
    </p>
    

This wraps the entire key sequence in an outer `<kbd>` element, then each individual key within its own, in order to denote the components of the sequence.

**Note:** You don't need to do all this wrapping; you can choose to simplify it by leaving out the external `<kbd>` element. In other words, simplifying this to just `<kbd>Ctrl</kbd>+<kbd>N</kbd>` would be perfectly valid.

Depending on your style sheet, though, you may find it useful to do this kind of nesting.

##### Result

The output looks like this without a style sheet applied:

#### With custom styles

We can make more sense of this by adding some CSS:

##### CSS

We add a new selector for nested `<kbd>` elements, `kbd>kbd`, which we can apply when rendering keyboard keys:

css

    kbd > kbd {
      border-radius: 3px;
      padding: 1px 2px 0;
      border: 1px solid black;
    }
    

##### HTML

Then we update the HTML to use this class on the keys in the output to be presented:

html

    <p>
      You can also create a new document by pressing the
      <kbd><kbd>Ctrl</kbd>+<kbd>N</kbd></kbd> shortcut.
    </p>
    

##### Result

The result is just what we want!

### [Echoed input](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#echoed_input)

Nesting a `<kbd>` element inside a [`<samp>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/samp)
 element represents input that has been echoed back to the user by the system.

html

    <p>
      If a syntax error occurs, the tool will output the initial command you typed
      for your review:
    </p>
    <blockquote>
      <samp><kbd>custom-git ad my-new-file.cpp</kbd></samp>
    </blockquote>
    

#### Result

### [Representing onscreen input options](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#representing_onscreen_input_options)

Nesting a `<samp>` element inside a `<kbd>` element represents input which is based on text presented by the system, such as the names of menus and menu items, or the names of buttons displayed on the screen.

For example, you can explain how to choose the "New Document" option in the "File" menu using HTML that looks like this:

html

    <p>
      To create a new file, choose the <kbd><kbd><samp>File</samp></kbd>
      ⇒<kbd><samp>New Document</samp></kbd></kbd> menu option.
    </p>
    
    <p>
      Don't forget to click the <kbd><samp>OK</samp></kbd> button to confirm once
      you've entered the name of the new file.
    </p>
    

This does some interesting nesting. For the menu option description, the entire input is enclosed in a `<kbd>` element. Then, inside that, both the menu and menu item names are contained within both `<kbd>` and `<samp>`, indicating an input which is selected from a screen widget.

#### Result

[Technical summary](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#technical_summary)

----------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Content categories](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories) | [Flow content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#flow_content)<br>, [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>, palpable content. |
| Permitted content | [Phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Tag omission | None, both the starting and ending tag are mandatory. |
| Permitted parents | Any element that accepts [phrasing content](https://developer.mozilla.org/en-US/docs/Web/HTML/Guides/Content_categories#phrasing_content)<br>. |
| Implicit ARIA role | [No corresponding role](https://w3c.github.io/html-aria/#dfn-no-corresponding-role "External link (opens in new tab)") |
| Permitted ARIA roles | Any |
| DOM interface | [`HTMLElement`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement) |

[Specifications](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#specifications)

----------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [HTML  <br>\# the-kbd-element](https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-kbd-element) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#browser_compatibility)

------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd#see_also)

----------------------------------------------------------------------------------------------

*   [`<code>`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/code)
    

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Aug 12, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/kbd/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/html/reference/elements/kbd/index.md?plain=1 "Folder: en-us/web/html/reference/elements/kbd (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fkbd&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fhtml%2Freference%2Felements%2Fkbd%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTML%2FReference%2FElements%2Fkbd%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fhtml%2Freference%2Felements%2Fkbd%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2Ff201fb25d8aeda059065686c180e161c995369d2%0A*+Document+last+modified%3A+2026-08-12T04%3A55%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")