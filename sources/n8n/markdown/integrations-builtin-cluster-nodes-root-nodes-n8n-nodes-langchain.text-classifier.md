For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier.md)
.

Use the Text Classifier node to classify (categorize) incoming data. Using the categories provided in the parameters (see below), each item is passed to the model to determine its category.

On this page, you'll find the node parameters for the Text Classifier node, and links to more resources.

Node parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier#node-parameters)

-----------------------------------------------------------------------------------------------------------------------------------------

*   **Input Prompt** defines the input to classify. This is usually an expression that references a field from the input items. For example, this could be `{{ $json.chatInput }}` if the input is a chat trigger. By default it references the `text` field.
    
*   **Categories**: Add the categories that you want to classify your input as. Categories have a name and a description. Use the description to tell the model what the category means. This is important if the meaning isn't obvious. You can add as many categories as you like.
    

Node options[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier#node-options)

-----------------------------------------------------------------------------------------------------------------------------------

*   **Allow Multiple Classes To Be True**: You can configure the classifier to always output a single class per item (turned off), or allow the model to select multiple classes (turned on).
    
*   **When No Clear Match**: Define what happens if the model can't find a good match for an item. There are two options:
    
    *   **Discard Item** (the default): If the node doesn't detect any of the categories, it drops the item.
        
    *   **Output on Extra, 'Other' Branch**: Creates a separate output branch called **Other**. When the node doesn't detect any of the categories, it outputs items in this branch.
        
    
*   **System Prompt Template**: Use this option to change the system prompt that's used for the classification. It uses the `{categories}` placeholder for the categories.
    
*   **Enable Auto-Fixing**: When enabled, the node automatically fixes model outputs to ensure they match the expected format. Do this by sending the schema parsing error to the LLM and asking it to fix it.
    

Related resources[](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.text-classifier#related-resources)

---------------------------------------------------------------------------------------------------------------------------------------------

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

[PreviousInformation Extractor](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.information-extractor)
[NextSentiment Analysis](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.sentimentanalysis)

Last updated 10 days ago

Was this helpful?