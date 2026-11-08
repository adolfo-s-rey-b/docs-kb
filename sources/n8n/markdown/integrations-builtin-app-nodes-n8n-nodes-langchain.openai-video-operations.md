For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations.md)
.

Use this operation to generate a video in OpenAI. Refer to [OpenAI](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai)
 for more information on the OpenAI node itself.

Generate Video[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations#generate-video)

--------------------------------------------------------------------------------------------------------------------------------

Use this operation to generate a video from a text prompt.

Enter these parameters:

*   **Credential to connect with**: Create or select an existing [OpenAI credential](https://docs.n8n.io/integrations/builtin/credentials/openai)
    .
    
*   **Resource**: Select **Video**.
    
*   **Operation**: Select **Generate Video**.
    
*   **Model**: Select the model you want to use to generate a video. Currently supports `sora-2` and `sora-2-pro`.
    
*   **Prompt**: The prompt to generate a video from.
    
*   **Seconds**: Clip duration in seconds (up to 25).
    
*   **Size**: Output resolution formatted as width x height. 1024x1792 and 1792x1024 are only supported by Sora 2 Pro.
    

### Options[](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/video-operations#options)

*   **Reference**: Optional image reference that guides generation. Has to be passed in as a binary item.
    
*   **Wait Timeout**: Time to wait for the video to be generated in seconds. Defaults to 300.
    
*   **Output Field Name**: The name of the output field to put the binary file data in. Defaults to `data`.
    

Refer to [Video Generation | OpenAI](https://platform.openai.com/docs/guides/video-generation)
 for more information.

[PreviousText operations](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/text-operations)
[NextCommon issues](https://docs.n8n.io/integrations/builtin/app-nodes/n8n-nodes-langchain.openai/common-issues)

Last updated 10 days ago

Was this helpful?