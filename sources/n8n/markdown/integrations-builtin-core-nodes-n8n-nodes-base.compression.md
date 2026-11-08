For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression.md)
.

Use the Compression node to compress and decompress files. Supports Zip, Gzip, Tar, and Tar.gz formats.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression#node-parameters)

------------------------------------------------------------------------------------------------------------------

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

The node parameters depend on which **Operation** you select. Choose to:

*   **Compress**: Create a compressed file from your input data.
    
*   **Decompress**: Decompress an existing compressed file.
    

Refer to the sections below for parameters specific to each **Operation**.

### Compress[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression#compress)

*   **Input Binary Field(s)**: Enter the name of the fields in the input data that contain the binary files you want to compress. To compress more than one file, use a comma-separated list.
    
*   **Output Format**: Choose whether to format the compressed output as **Zip**, **Gzip**, **Tar**, or **Tar (Gzip)**.
    
*   **File Name**: Enter the name of the compressed file the node creates.
    
*   **Put Output File in Field**: Enter the name of the field in the output data to contain the file.
    

### Decompress[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression#decompress)

The Decompress operation detects the archive format from the file extension and supports the following formats:

*   `.zip`
    
*   `.gz` and `.gzip`
    
*   `.tar`
    
*   `.tar.gz` and `.tgz`
    

When you decompress a `.tar.gz` or `.tgz` archive, the node extracts all member files in a single step. You don't need to decompress the gzip layer separately.

*   **Input Binary Field(s)**: Enter the name of the fields in the input data that contain the binary files you want to decompress. To decompress more than one file, use a comma-separated list.
    
*   **Output Prefix**: Enter a prefix to add to the output file name. The node uses this prefix, followed by an incrementing index, to name each extracted file.
    

#### Unsupported formats[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression#unsupported-formats)

If you pass a file with an unsupported extension, the node throws an error instead of silently producing empty output. Supported formats are `zip`, `gzip`, `tar`, `tar.gz`, and `tgz`.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.compression#templates-and-examples)

--------------------------------------------------------------------------------------------------------------------------------

[Browse n8n-nodes-base.compression integration templates](https://n8n.io/integrations/compression)
 or [search all templates](https://n8n.io/workflows/)

[PreviousCompare Datasets](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.comparedatasets)
[NextChat Trigger](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.chattrigger)

Last updated 10 days ago

Was this helpful?