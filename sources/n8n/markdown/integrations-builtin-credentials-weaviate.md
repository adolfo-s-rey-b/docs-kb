For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/credentials/weaviate.md)
.

You can use these credentials to authenticate the following nodes:

*   [Weaviate Vector Store](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.vectorstoreweaviate)
    

Supported authentication methods[](https://docs.n8n.io/integrations/builtin/credentials/weaviate#supported-authentication-methods)

-----------------------------------------------------------------------------------------------------------------------------------

*   API key
    

Related resources[](https://docs.n8n.io/integrations/builtin/credentials/weaviate#related-resources)

-----------------------------------------------------------------------------------------------------

Refer to [Weaviate's connection documentation](https://docs.weaviate.io/weaviate/connections)
for more information on how to connect to Weaviate.

View n8n's [Advanced AI](https://docs.n8n.io/build/integrate-ai)
 documentation.

Using API key[](https://docs.n8n.io/integrations/builtin/credentials/weaviate#using-api-key)

---------------------------------------------------------------------------------------------

### Connection type: Weaviate Cloud[](https://docs.n8n.io/integrations/builtin/credentials/weaviate#connection-type-weaviate-cloud)

Create your [Weaviate Cloud Database](https://docs.weaviate.io/cloud/quickstart)
 and [follow these instructions get the following parameter values](https://docs.weaviate.io/cloud/quickstart#13-connect-to-your-weaviate-cloud-instance)
 from your Weaviate Cloud Database:

*   **Weaviate Cloud Endpoint**
    
*   **Weaviate Api Key**
    

Note: Weaviate provides a free sandbox option for testing.

### Connection type: Custom Connection[](https://docs.n8n.io/integrations/builtin/credentials/weaviate#connection-type-custom-connection)

For this Connection Type, you need to [deploy Weaviate](https://docs.weaviate.io/deploy)
 on your own server, configured so n8n can access it. Refer to [Weaviate's authentication documentation](https://docs.weaviate.io/deploy/configuration/authentication#api-key-authentication)
 for information on creating and using API keys.

You can then provide the arguments for your custom connection:

*   **Weaviate Api Key**: Your Weaviate API key.
    
*   **Custom Connection HTTP Host**: The domain name or IP address of your Weaviate instance to use for HTTP API calls.
    
*   **Custom Connection HTTP Port**: The port your Weaviate instance is running on for HTTP API calls. By default, this is 8080.
    
*   **Custom Connection HTTP Secure**: Whether to connect to the Weaviate through HTTPS for HTTP API calls.
    
*   **Custom Connection gRPC Host**: The hostname or IP address of your Weaviate instance to use for gRPC.
    
*   **Custom Connection gRPC Port**: The gRPC API port for your Weaviate instance. By default, this is 50051.
    
*   **Custom Connection gRPC Secure**: Whether to connect to the Weaviate through HTTPS for gRPC.
    

For community support, refer to [Weaviate Forums](https://forum.weaviate.io/)
.

[PreviousVonage credentials](https://docs.n8n.io/integrations/builtin/credentials/vonage)
[NextWebex by Cisco credentials](https://docs.n8n.io/integrations/builtin/credentials/ciscowebex)

Last updated 10 days ago

Was this helpful?