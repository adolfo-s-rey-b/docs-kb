For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto.md)
.

Use the Crypto node to perform cryptographic operations in workflows.

**Credentials**

Refer to the [Crypto credentials documentation](https://docs.n8n.io/integrations/builtin/credentials/crypto)
 for authentication information for this node.

Actions[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#actions)

---------------------------------------------------------------------------------------------

*   [**Decrypt** a string](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#decrypt-parameters)
     with a passphrase or private key
    
*   [**Encrypt** a string](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#encrypt-parameters)
     with a passphrase or public key
    
*   [**Generate** a random string](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#generate-parameters)
    
*   [**Hash** a text or file](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#hash-parameters)
     in a specified format
    
*   [**Hmac** a text or file](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#hmac-parameters)
     in a specified format
    
*   [**Sign** a string](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#sign-parameters)
     using a private key
    

Node parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#node-parameters)

-------------------------------------------------------------------------------------------------------------

**This node can be used as an AI tool**

This node can be used to enhance the capabilities of an AI agent. When used in this way, many parameters can be set automatically, or with information directed by AI - find out more in the [AI tool parameters documentation](https://docs.n8n.io/build/integrate-ai/ai-examples/use-ai-for-parameters)
.

Node parameters depend on the action you select.

The **Hmac**, **Sign**, **Encrypt**, and **Decrypt** actions need [Crypto credentials](https://docs.n8n.io/integrations/builtin/credentials/crypto)
. Each action uses the credential field it needs:

*   **Hmac** uses the **Hmac Secret**.
    
*   **Sign** uses the **Private Key**.
    
*   **Encrypt** and **Decrypt** use the **Encryption Passphrase** for symmetric mode, or the **Encryption Public Key** and **Encryption Private Key** for asymmetric mode.
    

### Decrypt parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#decrypt-parameters)

*   **Mode**: Select the mode to use. This must match the mode used to encrypt the value. Choose from:
    
    *   **Symmetric (Passphrase)**: Decrypt with a passphrase using an authenticated cipher.
        
    *   **Asymmetric (RSA)**: Decrypt with an RSA private key.
        
    
*   **Cipher**: When you select **Symmetric (Passphrase)**, choose the authenticated cipher to use. This must match the cipher used to encrypt the value. Choose from:
    
    *   **AES-256-GCM**
        
    *   **AES-192-GCM**
        
    *   **AES-128-GCM**
        
    *   **ChaCha20-Poly1305**
        
    
*   **Value**: Enter the base64 string produced by the **Encrypt** action.
    
*   **Property Name**: Enter the name of the property you want to write the decrypted value to.
    

### Encrypt parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#encrypt-parameters)

*   **Mode**: Select the mode to use. Choose from:
    
    *   **Symmetric (Passphrase)**: Encrypt with a passphrase using an authenticated cipher.
        
    *   **Asymmetric (RSA)**: Encrypt with an RSA public key.
        
    
*   **Cipher**: When you select **Symmetric (Passphrase)**, choose the authenticated cipher to use. You must select the same cipher when you decrypt the value. Choose from:
    
    *   **AES-256-GCM**
        
    *   **AES-192-GCM**
        
    *   **AES-128-GCM**
        
    *   **ChaCha20-Poly1305**
        
    
*   **Value**: Enter the value you want to encrypt.
    
*   **Property Name**: Enter the name of the property you want to write the encrypted value to. The node writes the result as a base64 string.
    

**RSA payload size**

Asymmetric (RSA) mode can only encrypt small payloads, around 190 bytes with a 2048-bit key. Use symmetric mode for larger data.

### Generate parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#generate-parameters)

*   **Property Name**: Enter the name of the property to write the random string to.
    
*   **Type**: Select the encoding type to use to generate the string. Choose from:
    
    *   **ASCII**
        
    *   **BASE64**
        
    *   **HEX**
        
    *   **UUID**
        
    
*   **Length**: When you select **ASCII**, **BASE64**, or **HEX**, enter the length of the generated string. The default is `32`.
    

### Hash parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#hash-parameters)

*   **Type**: Select the hash type to use. Choose from:
    
    *   **MD5**
        
    *   **SHA256**
        
    *   **SHA3-256**
        
    *   **SHA3-384**
        
    *   **SHA3-512**
        
    *   **SHA384**
        
    *   **SHA512**
        
    
*   **Binary File**: Turn this parameter on if the data you want to hash is from a binary file.
    
    *   **Value**: If you turn off **Binary File**, enter the value you want to hash.
        
    *   **Binary Property Name**: If you turn on **Binary File**, enter the name of the binary property that contains the data you want to hash.
        
    
*   **Property Name**: Enter the name of the property you want to write the hash to.
    
*   **Encoding**: Select the encoding type to use. Choose from:
    
    *   **BASE64**
        
    *   **HEX**
        
    

### Hmac parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#hmac-parameters)

*   **Binary File**: Turn this parameter on if the data you want to create an Hmac for is from a binary file.
    
    *   **Value**: If you turn off **Binary File**, enter the value you want to create an Hmac for.
        
    *   **Binary Property Name**: If you turn on **Binary File**, enter the name of the binary property that contains the data you want to create an Hmac for.
        
    
*   **Type**: Select the hash type to use. Choose from:
    
    *   **MD5**
        
    *   **SHA256**
        
    *   **SHA3-256**
        
    *   **SHA3-384**
        
    *   **SHA3-512**
        
    *   **SHA384**
        
    *   **SHA512**
        
    
*   **Property Name**: Enter the name of the property you want to write the Hmac to.
    
*   **Encoding**: Select the encoding type to use. Choose from:
    
    *   **BASE64**
        
    *   **HEX**
        
    

This action uses the **Hmac Secret** from your [Crypto credentials](https://docs.n8n.io/integrations/builtin/credentials/crypto)
.

### Sign parameters[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#sign-parameters)

*   **Value**: Enter the value you want to sign.
    
*   **Property Name**: Enter the name of the property you want to write the signed value to.
    
*   **Algorithm Name or ID**: Choose an algorithm name from the list or specify an ID using an [expression](https://docs.n8n.io/build/work-with-data/expressions-versus-data-nodes)
    .
    
*   **Encoding**: Select the encoding type to use. Choose from:
    
    *   **BASE64**
        
    *   **HEX**
        
    

This action uses the **Private Key** from your [Crypto credentials](https://docs.n8n.io/integrations/builtin/credentials/crypto)
.

Templates and examples[](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.crypto#templates-and-examples)

---------------------------------------------------------------------------------------------------------------------------

[Browse Crypto integration templates](https://n8n.io/integrations/crypto)
 or [search all templates](https://n8n.io/workflows/)

[PreviousConvert to File](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.converttofile)
[NextData Table](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.datatable)

Last updated 10 days ago

Was this helpful?