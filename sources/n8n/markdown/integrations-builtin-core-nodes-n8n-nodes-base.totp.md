For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp.md)
.

The TOTP node provides a way to generate a TOTP (time-based one-time password).

**Credentials**

Refer to [TOTP credentials](https://docs.n8n.io/integrations/builtin/credentials/totp)
 for guidance on setting up authentication.

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp#node-parameters)

-----------------------------------------------------------------------------------------------------------

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Configure this node with these parameters.

### Credential to connect with[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp#credential-to-connect-with)

Select or create a [TOTP credential](https://docs.n8n.io/integrations/builtin/credentials/totp)
 for the node to use.

### Operation[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp#operation)

**Generate Secret** is the only operation currently supported.

Node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp#node-options)

-----------------------------------------------------------------------------------------------------

Use these **Options** to further configure the node.

### Algorithm[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp#algorithm)

Select the HMAC hashing algorithm to use. Default is SHA1.

### Digits[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp#digits)

Enter the number of digits in the generated code. Default is `6`.

### Period[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp#period)

Enter how many seconds the TOTP is valid for. Default is `30`.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.totp#templates-and-examples)

-------------------------------------------------------------------------------------------------------------------------

[Browse TOTP integration templates](https://n8n.io/integrations/totp)
 or [search all templates](https://n8n.io/workflows/)

[PreviousSwitch](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.switch)
[NextTrack Time Saved](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.timesaved)

Last updated 10 days ago

Was this helpful?