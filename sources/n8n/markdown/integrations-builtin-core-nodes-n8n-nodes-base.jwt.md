For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt.md)
.

Work with JSON web tokens in your n8n workflows.

**Credentials**

Refer to the [JWT credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/jwt)
 for authentication information for this node.

Operations[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#operations)

------------------------------------------------------------------------------------------------

*   Decode
    
*   Sign
    
*   Verify
    

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#node-parameters)

----------------------------------------------------------------------------------------------------------

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

*   **Credential to connect with**: Select or create a [JWT credential](https://docs.n8n.io/integrations/builtin/credentials/jwt)
     to connect with.
    
*   **Token**: Enter the token to **Verify** or **Decode**.
    
*   If you select the **Sign** operation, you'll also have this parameter:
    
    *   **Use JSON to Build Payload**: When turned on, the node uses JSON to build the claims. The selection here influences what appears in the Payload Claims section.
        
    

Payload Claims[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#payload-claims)

--------------------------------------------------------------------------------------------------------

The node only displays payload claims if you select the **Sign** operation. What you see depends on what you select for **Use JSON to Build Payload**:

*   If you select **Use JSON to Build Payload**, this section displays a JSON editor where you can construct the claims.
    
*   If you don't select **Use JSON to Build Payload**, this section prompts you to **Add Claim**.
    

You can add the following claims.

### Audience[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#audience)

The **Audience** or `aud` claim identifies the intended recipients of the JWT.

Refer to ["aud" (Audience) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.3)
 for more information.

### Expires In[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#expires-in)

The **Expires In** or `exp` claim identifies the time after which the JWT expires and must not be accepted for processing.

Refer to ["exp" (Expiration Time) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4)
 for more information.

### Issuer[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#issuer)

The **Issuer** or `iss` claim identifies the principal that issued the JWT.

Refer to ["iss" (Issuer) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.1)
 for more information.

### JWT ID[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#jwt-id)

The **JWT ID** or `jti` claim provides a unique identifier for the JWT.

Refer to ["jti" (JWT ID) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.7)
 for more information.

### Not Before[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#not-before)

The **Not Before** or `nbf` claim identifies the time before which the JWT must not be accepted for processing.

Refer to ["nbf" (Not Before) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.5)
 for more information.

### Subject[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#subject)

The **Subject** or `sub` claim identifies the principal that's the subject of the JWT.

Refer to ["sub" (Subject) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.2)
 for more information.

Node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#node-options)

----------------------------------------------------------------------------------------------------

### Decode node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#decode-node-options)

The **Return Additional Info** toggle controls how much information the node returns.

When turned on, the node returns the complete decoded token with information about the header and signature. When turned off, the node only returns the payload.

### Sign node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#sign-node-options)

Use the **Override Algorithm** control to select the algorithm to use for verifying the token. This algorithm will override the algorithm selected in the credentials.

### Verify node options[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#verify-node-options)

This operation includes several node options:

*   **Return Additional Info**: This toggle controls how much information the node returns. When turned on, the node returns the complete decoded token with information about the header and signature. When turned off, the node only returns the payload.
    
*   **Ignore Expiration**: This toggle controls whether the node should ignore the token's expiration time claim (`exp`). Refer to ["exp" (Expiration Time) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4)
     for more information.
    
*   **Ignore Not Before Claim**: This toggle controls whether to ignore the token's not before claim (`nbf`). Refer to ["nbf" (Not Before) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.5)
     for more information.
    
*   **Clock Tolerance**: Enter the number of seconds to tolerate when checking the `nbf` and `exp` claims. This allows you to deal with small clock differences among different servers. Refer to ["exp" (Expiration Time) Claim](https://datatracker.ietf.org/doc/html/rfc7519#section-4.1.4)
     for more information.
    
*   **Override Algorithm**: The algorithm to use for verifying the token. This algorithm will override the algorithm selected in the credentials.
    

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.jwt#templates-and-examples)

------------------------------------------------------------------------------------------------------------------------

[Browse JWT integration templates](https://n8n.io/integrations/jwt)
 or [search all templates](https://n8n.io/workflows/)

[PreviousIf](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.if)
[NextLDAP](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.ldap)

Last updated 10 days ago

Was this helpful?