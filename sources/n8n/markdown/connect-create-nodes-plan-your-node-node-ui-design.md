For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design.md)
.

Most nodes are a GUI (graphical user interface) representation of an API. Designing the interface means finding a user-friendly way to represent API endpoints and parameters. Directly translating an entire API into form fields in a node may not result in a good user experience.

This document provides design guidance and standards to follow. These guidelines are the same as those used by n8n. This helps provide a smooth and consistent user experience for users mixing community and built-in nodes.

Design guidance[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#design-guidance)

----------------------------------------------------------------------------------------------------------

All node's use n8n's [node UI elements](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements)
, so you don't need to consider style details such as colors, borders, and so on. However, it's still useful to go through a basic design process:

*   Review the documentation for the API you're integrating. Ask yourself:
    
    *   What can you leave out?
        
    *   What can you simplify?
        
    *   Which parts of the API are confusing? How can you help users understand them?
        
    
*   Use a wireframe tool to try out your field layout. If you find your node has a lot of fields and is getting confusing, consider n8n's guidance on [showing and hiding fields](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#showing-and-hiding-fields)
    .
    

Standards[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#standards)

----------------------------------------------------------------------------------------------

### UI text style[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#ui-text-style)

Element

Style

Drop-down value

Title case

Hint

Sentence case

Info box

Sentence case. Don't use a period (`.`) for one-sentence information. Always use a period if there's more than one sentence. This field can include links, which should open in a new tab.

Node name

Title case

Parameter name

Title case

Subtitle

Title case

Tooltip

Sentence case. Don't use a period (`.`) for one-sentence tooltips. Always use a period if there's more than one sentence. This field can include links, which should open in a new tab.

### UI text terminology[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#ui-text-terminology)

*   Use the same terminology as the service the node connects to. For example, a Notion node should refer to Notion blocks, not Notion paragraphs, because Notion calls these elements blocks. There are exceptions to this rule, usually to avoid technical terms (for example, refer to the guidance on [name and description for upsert operations](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#upsert-operations)
    ).
    
*   Sometimes a service has different terms for something in its API and in its GUI. Use the GUI language in your node, as this is what most users are familiar with. If you think some users may need to refer to the service's API docs, consider including this information in a hint.
    
*   Don't use technical jargon when there are simpler alternatives.
    
*   Be consistent when naming things. For example, choose one of `directory` or `folder` then stick to it.
    

### Node naming conventions[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#node-naming-conventions)

Convention

Correct

Incorrect

If a node is a trigger node, the displayed name should have 'Trigger' at the end, with a space before.

Shopify Trigger

ShopifyTrigger, Shopify trigger

Don't include 'node' in the name.

Asana

Asana Node, Asana node

### Showing and hiding fields[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#showing-and-hiding-fields)

Fields can either be:

*   Displayed when the node opens: use this for resources and operations, and required fields.
    
*   Hidden in the **Optional fields** section until a user clicks on that section: use this for optional fields.
    

Progressively disclose complexity: hide a field until any earlier fields it depends on have values. For example, if you have a **Filter by date** toggle, and a **Date to filter by** datepicker, don't display **Date to filter by** until the user enables **Filter by date**.

### Conventions by field type[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#conventions-by-field-type)

#### Credentials[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#credentials)

n8n automatically displays credential fields as the top fields in the node.

#### Resources and operations[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#resources-and-operations)

APIs usually involve doing something to data. For example, "get all tasks." In this example, "task" is the resource, and "get all" is the operation.

When your node has this resource and operation pattern, your first field should be **Resource**, and your second field should be **Operation**.

#### Required fields[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#required-fields)

Order fields by:

*   Most important to least important.
    
*   Scope: from broad to narrow. For example, you have fields for **Document**, **Page**, and **Text to insert**, put them in that order.
    

#### Optional fields[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#optional-fields)

*   Order fields alphabetically. To group similar things together, you can rename them. For example, rename **Email** and **Secondary Email** to **Email (primary)** and **Email (secondary)**.
    
*   If an optional field has a default value that the node uses when the value isn't set, load the field with that value. Explain this in the field description. For example, **Defaults to false**.
    
*   Connected fields: if one optional fields is dependent on another, bundle them together. They should both be under a single option that shows both fields when selected.
    
*   If you have a lot of optional fields, consider grouping them by theme.
    

#### Help[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#help)

There are five types of help built in to the GUI:

*   Info boxes: yellow boxes that appear between fields. Refer to [UI elements | Notice](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#notice)
     for more information.
    
    *   Use info boxes for essential information. Don't over-use them. By making them rare, they stand out more and grab the user's attention.
        
    
*   Parameter hints: lines of text displayed beneath a user input field. Use this when there's something the user needs to know, but an info box would be excessive.
    
*   Node hints: provide help in the input panel, output panel, or node details view. Refer to [UI elements | Hints](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/node-ui-elements#hints)
     for more information.
    
*   Tooltips: callouts that appear when the user hovers over the tooltip icon ![The tooltip icon: a question mark in a grey circle](https://docs.n8n.io/~gitbook/image?url=https%3A%2F%2F1078077037-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252Fr7wKI4I1BgdBCuq5Cvcx%252Fuploads%252Fgit-blob-01b43fd4b3a8165cc98b603e94f45f7ffcf84625%252Fhelp-tooltip.png%3Falt%3Dmedia&width=300&dpr=3&quality=100&sign=bfa4acd454a4529a9a688b37c09eaa3b&sv=3). Use tooltips for extra information that the user might need.
    
    *   You don't have to provide a tooltip for every field. Only add one if it contains useful information.
        
    *   When writing tooltips, think about what the user needs. Don't just copy-paste API parameter descriptions. If the description doesn't make sense, or has errors, improve it.
        
    
*   Placeholder text: n8n can display placeholder text in a field where the user hasn't entered a value. This can help the user know what's expected in that field.
    

Info boxes, hints, and tooltips can contain links to more information.

#### Errors[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#errors)

Make it clear which fields are required.

Add validation rules to fields if possible. For example, check for valid email patterns if the field expects an email.

When displaying errors, make sure only the main error message displays in the red error title. More information should go in **Details**.

Refer to [Node Error Handling](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/error-handling)
 for more information.

#### Toggles[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#toggles)

*   Tooltips for binary states should start with something like \*\*Whether to . . . \*\*.
    
*   You may need a list rather than a toggle:
    
    *   Use toggles when it's clear what happens in a false state. For example, **Simplify Output?**. The alternative (don't simplify output) is clear.
        
    *   Use a dropdown list with named options when you need more clarity. For example, **Append?**. What happens if you don't append is unclear (it could be that nothing happens, or information is overwritten, or discarded).
        
    

#### Lists[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#lists)

*   Set default values for lists whenever possible. The default should be the most-used option.
    
*   Sort list options alphabetically.
    
*   You can include list option descriptions. Only add descriptions if they provide useful information.
    
*   If there is an option like **All**, use the word **All**, not shorthand like \*\*\*\*\*.
    

#### Trigger node inputs[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#trigger-node-inputs)

When a trigger node has a parameter for specifying which events to trigger on:

*   Name the parameter **Trigger on**.
    
*   Don't include a tooltip.
    

#### Subtitles[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#subtitles)

Set subtitles based on the values of the main parameters. For example:

Copy

    subtitle: '={{$parameter["operation"] + ": " + $parameter["resource"]}}',

#### IDs[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#ids)

When performing an operation on a specific record, such as "update a task comment" you need a way to specify which record you want to change.

*   Wherever possible, provide two ways to specify a record:
    
    *   By choosing from a pre-populated list. You can generate this list using the `loadOptions` parameter. Refer to [Base files](https://docs.n8n.io/connect/create-nodes/build-your-node/reference/base-files)
         for more information.
        
    *   By entering an ID.
        
    
*   Name the field `<Record name> name or ID`. For example, **Workspace Name or ID**. Add a tooltip saying "Choose a name from the list, or specify an ID using an expression." Link to n8n's [Expressions](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
     documentation.
    
*   Build your node so that it can handle users providing more information than required. For example:
    
    *   If you need a relative path, handle the user pasting in the absolute path.
        
    *   If the user needs to get an ID from a URL, handle the user pasting in the entire URL.
        
    

#### Dates and timestamps[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#dates-and-timestamps)

n8n uses [ISO timestamp strings](https://en.wikipedia.org/wiki/ISO_8601)
 for dates and times. Make sure that any date or timestamp field you add supports all ISO 8601 formats.

#### JSON[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#json)

You should support two ways of specifying the content of a text input that expects JSON:

*   Typing JSON directly into the text input: you need to parse the resulting string into a JSON object.
    
*   Using an expression that returns JSON.
    

#### Node icons[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#node-icons)

n8n recommends using an SVG for your node icon, but you can also use PNG. If using PNG, the icon resolution should be 60x60px. Node icons should have a square or near-square aspect ratio.

**Don't reference Font Awesome**

If you want to use a Font Awesome icon in your node, download and embed the image. Don't set `defaults.color`: it only tints Font Awesome icons, and n8n 3.0 removes it.

### Common patterns and exceptions[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#common-patterns-and-exceptions)

This section provides guidance on handling common design patterns, including some edge cases and exceptions to the main standards.

#### Simplify responses[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#simplify-responses)

APIs can return a lot of data that isn't useful. Consider adding a toggle that allows users to choose to simplify the response data:

*   Name: **Simplify Response**
    
*   Description: **Whether to return a simplified version of the response instead of the raw data**
    

#### Upsert operations[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#upsert-operations)

This should always be a separate operation with:

*   Name: **Create or Update**
    
*   Description: **Create a new record, or update the current one if it already exists (upsert)**
    

#### Boolean operators[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#boolean-operators)

n8n doesn't have good support for combining boolean operators, such as AND and OR, in the GUI. Whenever possible, provide options for all ANDs or all ORs.

For example, you have a field called **Must match** to test if values match. Include options to test for **Any** and **All**, as separate options.

#### Source keys or binary properties[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#source-keys-or-binary-properties)

Binary data is file data, such as spreadsheets or images. In n8n, you need a named key to reference the data. Don't use the terms "binary data" or "binary property" for this field. Instead, use a more descriptive name: **Input data field name** / **Output data field name**.

Related resources[](https://docs.n8n.io/connect/create-nodes/plan-your-node/node-ui-design#related-resources)

--------------------------------------------------------------------------------------------------------------

*   [Plan your node](https://docs.n8n.io/connect/create-nodes/plan-your-node)
    
*   [Choose a node type](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-type)
    
*   [Choose a node building style](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-building-style)
    
*   [Choose node file structure](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-node-file-structure)
    

[PreviousChoose a node building style](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-a-node-building-style)
[NextChoose node file structure](https://docs.n8n.io/connect/create-nodes/plan-your-node/choose-node-file-structure)

Last updated 10 days ago

Was this helpful?