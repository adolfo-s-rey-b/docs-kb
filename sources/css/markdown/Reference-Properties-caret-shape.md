*   [Skip to main content](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#content)
    
*   [Skip to search](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#mdn-search)
    

`caret-shape` CSS property
==========================

Limited availability

This feature is not Baseline because it does not work in some of the most widely-used browsers.

Want more browser support for this feature? [Tell us why.](https://github.com/web-platform-dx/developer-signals/issues/424)

*   [See full compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#browser_compatibility)
    
*   [Learn more](https://developer.mozilla.org/en-US/docs/Glossary/Baseline/Compatibility)
    

**Experimental:** **This is an [experimental technology](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Experimental_deprecated_obsolete#experimental)
**  
Check the [Browser compatibility table](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#browser_compatibility)
 carefully before using this in production.

The **`caret-shape`** [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
 property sets the shape of the **insertion caret**, the visible marker that appears in editable elements to indicate where the next character will be inserted or deleted.

The `caret-shape` property can also be set as part of the [`caret`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret)
 shorthand property.

[Try it](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#try_it)

---------------------------------------------------------------------------------------------------

    caret-shape: auto;
    

    caret-shape: bar;
    

    caret-shape: block;
    

    caret-shape: underscore;
    

    <section class="default-example container" id="default-example">
      <div>
        <label for="example-element">Edit text field:</label>
        <input id="example-element" type="text" value="Sample text" />
      </div>
    </section>
    

    div {
      text-align: left;
    }
    
    #example-element {
      font-size: 1.2rem;
      padding: 8px;
      width: 300px;
    }
    

[Syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#syntax)

---------------------------------------------------------------------------------------------------

css

    /* Keyword values */
    caret-shape: auto;
    caret-shape: bar;
    caret-shape: block;
    caret-shape: underscore;
    
    /* Global values */
    caret-shape: inherit;
    caret-shape: initial;
    caret-shape: revert;
    caret-shape: revert-layer;
    caret-shape: unset;
    

### [Values](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#values)

This property is specified as one of the following keyword values:

[`auto`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#auto)

The default value. The browser determines the caret shape. This typically follows platform conventions and may change based on context.

[`bar`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#bar)

The caret appears as a thin vertical line at the insertion point, positioned between characters rather than over them.

[`block`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#block)

The caret appears as a rectangle that overlaps the next character after the insertion point. If no character follows, it appears after the last character.

[`underscore`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#underscore)

The caret appears as a thin horizontal line underneath the next character after the insertion point. If no character follows, it appears after the last character.

[Description](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#description)

-------------------------------------------------------------------------------------------------------------

The insertion caret is the blinking cursor that indicates where text will be inserted when typing. Different caret shapes can provide visual feedback about the current editing mode or offer visual customization.

### [Editing modes and caret shapes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#editing_modes_and_caret_shapes)

Text editors typically operate in one of two modes:

*   **Insert mode**: New characters are inserted at the caret position, pushing existing text to the end of the line. This is the default behavior in most modern applications.
*   **Overtype mode** (also called "overwrite mode"): New characters replace existing characters at the caret position instead of being inserted between them. This mode is often toggled with the Insert key.

Different caret shapes have traditional uses, for example:

*   **Bar carets** are positioned between characters and are most common in modern interfaces.
*   **Block carets** overlay the next character and are often used in terminal applications or to indicate overtype mode.
*   **Underscore carets** appear below characters and can be useful for certain design aesthetics, such as mimicking typewriter or underline text input styles.

### [Caret positioning and behavior](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#caret_positioning_and_behavior)

The `caret-shape` property affects how the caret is visually rendered but doesn't change its logical position in the text. The caret always represents the insertion point between characters, regardless of its visual shape.

### [Interaction with writing modes](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#interaction_with_writing_modes)

The caret shape adapts to the [`writing-mode`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/writing-mode)
 of the text. In vertical writing modes, bar carets become horizontal, and underscore carets position themselves appropriately relative to the text direction.

[Formal definition](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#formal_definition)

-------------------------------------------------------------------------------------------------------------------------

|     |     |
| --- | --- |
| [Initial value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#initial_value) | `auto` |
| Applies to | Text or elements that accept text input |
| [Inherited](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Inheritance) | yes |
| [Computed value](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Cascade/Property_value_processing#computed_value) | as specified |
| [Animation type](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Animations/Animatable_properties) | by computed value type |

[Formal syntax](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#formal_syntax)

-----------------------------------------------------------------------------------------------------------------

caret-shape =   
  auto        [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  bar         [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  block       [|](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Values_and_units/Value_definition_syntax#single_bar "Single bar: exactly one of the entities must be present")
  
  underscore    

[Examples](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#examples)

-------------------------------------------------------------------------------------------------------

### [Retro terminal with animated caret](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#retro_terminal_with_animated_caret)

This example shows how to create a vintage terminal interface using `caret-shape: block` with animated caret color, replacing the old technique of using borders.

The key part is using the modern caret properties instead of the old border-based technique. We set the caret to block shape, disable the default blinking, and create our own custom animation.

#### HTML

html

    <label for="terminal">Enter a command</label>
    <div class="old-screen">
      <span>></span>
      <textarea id="terminal" class="terminal-input"></textarea>
    </div>
    

#### CSS

    label {
      background: #092104;
      display: block;
      padding: 10px 20px;
      color: #00ad00;
      font-weight: bold;
      font-family: monospace;
    }
    
    .old-screen {
      background: repeating-linear-gradient(
        #092104,
        #092104 2px,
        #123208 2px,
        #123208 4px
      );
      height: 140px;
      display: flex;
      align-items: flex-start;
      padding: 20px;
      font-family: monospace;
    }
    
    span {
      display: inline-block;
      padding: 2px 5px;
      color: #00ad00;
      font-weight: bold;
      margin-right: 8px;
    }
    
    .terminal-input {
      background: transparent;
      height: 100%;
      border: none;
      color: #00ad00;
      font-family: inherit;
      font-size: 1rem;
      outline: none;
      flex: 1;
      resize: none;
    }
    

css

    .terminal-input {
      caret-shape: block;
      caret-animation: manual;
      animation: old-caret 2s infinite;
    }
    
    @keyframes old-caret {
      0%,
      50% {
        caret-color: #00ad00;
      }
      75%,
      100% {
        caret-color: transparent;
      }
    }
    

#### Result

### [Console interface with underscore caret](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#console_interface_with_underscore_caret)

This example demonstrates using `caret-shape: underscore` to create a console-style interface where the underscore caret complements the terminal aesthetic.

#### HTML

html

    <label for="console">Enter a command</label>
    <div class="console-demo">
      <div class="console-output">
        <p>user@host:css-ui-4 $ ls -a</p>
        <p>. .. Overview.bs Overview.html</p>
      </div>
      <div class="console-input">
        <span class="prompt">user@host:css-ui-4 $ </span>
        <input type="text" id="console" class="console" value="cd" />
      </div>
    </div>
    

#### CSS

    label {
      background: #2a2a2c;
      color: white;
      display: block;
      padding: 10px 20px;
      font-weight: bold;
      font-family: monospace;
    }
    
    .console-demo {
      background: black;
      color: white;
      font-family: monospace;
      padding: 10px 20px;
      height: 60px;
    }
    
    .console-output {
      margin-bottom: 0.5rem;
    }
    
    .console-output p {
      margin: 0 0.25rem;
    }
    
    .console-input {
      display: flex;
      align-items: center;
    }
    
    .prompt {
      margin-right: 0;
    }
    
    .console {
      background: transparent;
      border: none;
      color: white;
      padding-left: 1ch;
      font-family: inherit;
      outline: none;
      flex: 1;
    }
    

css

    .console {
      caret-shape: underscore;
    }
    

#### Result

[Specifications](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#specifications)

-------------------------------------------------------------------------------------------------------------------

| Specification |
| --- |
| [CSS Basic User Interface Module Level 4  <br>\# propdef-caret-shape](https://drafts.csswg.org/css-ui/#propdef-caret-shape) |

[Browser compatibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#browser_compatibility)

---------------------------------------------------------------------------------------------------------------------------------

[See also](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape#see_also)

-------------------------------------------------------------------------------------------------------

*   [`caret-color`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-color)
    , [`caret-animation`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-animation)
    
*   [`caret`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret)
     shorthand
*   [CSS basic user interface](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Basic_user_interface)
     module

Help improve MDN
----------------

[Learn how to contribute](https://developer.mozilla.org/en-US/docs/MDN/Community/Getting_started)

This page was last modified on Jul 26, 2026 by [MDN contributors](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/caret-shape/contributors.txt)
.

[View this page on GitHub](https://github.com/mdn/content/blob/main/files/en-us/web/css/reference/properties/caret-shape/index.md?plain=1 "Folder: en-us/web/css/reference/properties/caret-shape (Opens in a new tab)")
 • [Report a problem with this content](https://github.com/mdn/content/issues/new?template=page-report.yml&mdn-url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcaret-shape&metadata=%3C%21--+Do+not+make+changes+below+this+line+--%3E%0A%3Cdetails%3E%0A%3Csummary%3EPage+report+details%3C%2Fsummary%3E%0A%0A*+Folder%3A+%60en-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcaret-shape%60%0A*+MDN+URL%3A+https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FCSS%2FReference%2FProperties%2Fcaret-shape%0A*+GitHub+URL%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fblob%2Fmain%2Ffiles%2Fen-us%2Fweb%2Fcss%2Freference%2Fproperties%2Fcaret-shape%2Findex.md%0A*+Last+commit%3A+https%3A%2F%2Fgithub.com%2Fmdn%2Fcontent%2Fcommit%2F071fd0613b1b5728d2d83845ea11512cb615067a%0A*+Document+last+modified%3A+2026-07-26T23%3A33%3A26.000Z%0A%0A%3C%2Fdetails%3E "This will take you to GitHub to file a new issue.")