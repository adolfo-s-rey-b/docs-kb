For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys.md)
.

Use the Rename Keys node to rename the keys of a key-value pair in n8n.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys#node-parameters)

-----------------------------------------------------------------------------------------------------------------

You can rename one or multiple keys using the Rename Keys node. Select the **Add new key** button to rename a key.

For each key, enter the:

*   **Current Key Name**: The current name of the key you want to rename.
    
*   **New Key Name**: The new name you want to assign to the key.
    

Node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys#node-options)

-----------------------------------------------------------------------------------------------------------

Choose whether to use a **Regex** regular expression to identify keys to rename. To use this option, you must also enter:

*   The **Regular Expression** you'd like to use.
    
*   **Replace With**: Enter the new name you want to assign to the key(s) that match the **Regular Expression**.
    
*   You can also choose these Regex-specific options:
    
    *   **Case Insensitive**: Set whether the regular expression should match case (turned off) or be case insensitive (turned on).
        
    *   **Max Depth**: Enter the maximum depth to replace keys, using `-1` for unlimited and `0` for top-level only.
        
    

**Regex impacts**

Using a regular expression can affect any keys that match the expression, including keys you've already renamed.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.renamekeys#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------------

[Browse Rename Keys integration templates](https://n8n.io/integrations/rename-keys)
 or [search all templates](https://n8n.io/workflows/)

[PreviousTemplates and examples](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.removeduplicates/templates-and-examples)
[NextChat](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chat)

Last updated 10 days ago

Was this helpful?