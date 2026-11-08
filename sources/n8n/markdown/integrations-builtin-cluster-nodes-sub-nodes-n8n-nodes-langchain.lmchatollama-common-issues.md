For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues.md)
.

Here are some common errors and issues with the [Ollama Chat Model node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama)
 and steps to resolve or troubleshoot them.

Processing parameters[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues#processing-parameters)

---------------------------------------------------------------------------------------------------------------------------------------------------------------

The Ollama Chat Model node is a sub-node. Sub-nodes behave differently than other nodes when processing multiple items using expressions.

Most nodes, including root nodes, take any number of items as input, process these items, and output the results. You can use expressions to refer to input items, and the node resolves the expression for each item in turn. For example, given an input of five name values, the expression `{{ $json.name }}` resolves to each name in turn.

In sub-nodes, the expression always resolves to the first item. For example, given an input of five name values, the expression `{{ $json.name }}` always resolves to the first name.

Can't connect to a remote Ollama instance[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues#cant-connect-to-a-remote-ollama-instance)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Ollama Chat Model node supports Bearer token authentication for connecting to remote Ollama instances behind authenticated proxies (such as Open WebUI).

For remote authenticated connections, configure both the remote URL and API key in your Ollama credentials.

Follow the [Ollama credentials instructions](https://docs.n8n.io/integrations/builtin/credentials/ollama)
 for more information.

Can't connect to a local Ollama instance when using Docker[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues#cant-connect-to-a-local-ollama-instance-when-using-docker)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

The Ollama Chat Model node connects to a locally hosted Ollama instance using the base URL defined by [Ollama credentials](https://docs.n8n.io/integrations/builtin/credentials/ollama)
. When you run either n8n or Ollama in Docker, you need to configure the network so that n8n can connect to Ollama.

Ollama typically listens for connections on `localhost`, the local network address. In Docker, by default, each container has its own `localhost` which is only accessible from within the container. If either n8n or Ollama are running in containers, they won't be able to connect over `localhost`.

The solution depends on how you're hosting the two components.

### If only Ollama is in Docker[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues#if-only-ollama-is-in-docker)

If only Ollama is running in Docker, configure Ollama to listen on all interfaces by binding to `0.0.0.0` inside of the container (the official images are already configured this way).

When running the container, [publish the ports](https://docs.docker.com/get-started/docker-concepts/running-containers/publishing-ports/)
 with the `-p` flag. By default, Ollama runs on port 11434, so your Docker command should look like this:

Copy

    docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama

When configuring [Ollama credentials](https://docs.n8n.io/integrations/builtin/credentials/ollama)
, the `localhost` address should work without a problem (set the **base URL** to `http://localhost:11434`).

### If only n8n is in Docker[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues#if-only-n8n-is-in-docker)

If only n8n is running in Docker, configure Ollama to listen on all interfaces by binding to `0.0.0.0` on the host.

If you are running n8n in Docker on **Linux**, use the `--add-host` flag to map `host.docker.internal` to `host-gateway` when you start the container. For example:

Copy

    docker run -it --rm --add-host host.docker.internal:host-gateway --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n n8nio/n8n

If you are using Docker Desktop, this is automatically configured for you.

When configuring [Ollama credentials](https://docs.n8n.io/integrations/builtin/credentials/ollama)
, use `host.docker.internal` as the host address instead of `localhost`. For example, to bind to the default port 11434, you could set the base URL to `http://host.docker.internal:11434`.

### If Ollama and n8n are running in separate Docker containers[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues#if-ollama-and-n8n-are-running-in-separate-docker-containers)

Connect both containers to the same user-defined bridge network. For more information, refer to the Docker [bridge network driver documentation](https://docs.docker.com/engine/network/drivers/bridge/)
. The default Docker bridge network doesn't resolve container names. Using a container name on the default bridge can cause an `ENOTFOUND` error, even when Ollama is running.

Configure Ollama to listen on `0.0.0.0` inside its container. The official Ollama image already uses this setting.

To connect existing containers, follow these steps. Replace `<ollama-container>` and `<n8n-container>` with the names of your existing containers. Run `docker ps` to find their names.

1.  Create a shared network:
    
    Copy
    
        docker network create n8n-ollama
    
2.  Connect the Ollama container:
    
    Copy
    
        docker network connect n8n-ollama <ollama-container>
    
3.  Connect the n8n container:
    
    Copy
    
        docker network connect n8n-ollama <n8n-container>
    
4.  In your [Ollama credentials](https://docs.n8n.io/integrations/builtin/credentials/ollama)
    , set **Base URL** to `http://<ollama-container>:11434`. Replace `<ollama-container>` with your Ollama container's name. For example, for a container with the name `ollama`, use `http://ollama:11434`.
    

Both containers must be running. Containers on the same network communicate directly, so you don't need to publish Ollama's port to the host.

### If Ollama and n8n are running in the same Docker container[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues#if-ollama-and-n8n-are-running-in-the-same-docker-container)

If Ollama and n8n are running in the same Docker container, the `localhost` address doesn't need any special configuration. You can configure Ollama to listen on localhost and configure the base URL in the [Ollama credentials in n8n](https://docs.n8n.io/integrations/builtin/credentials/ollama)
 to use localhost: `http://localhost:11434`.

Error: connect ECONNREFUSED ::1:11434[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues#error-connect-econnrefused-111434)

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This error occurs when your computer has IPv6 enabled, but Ollama is listening to an IPv4 address.

To fix this, change the base URL in your [Ollama credentials](https://docs.n8n.io/integrations/builtin/credentials/ollama)
 to connect to `127.0.0.1`, the IPv4-specific local address, instead of the `localhost` alias that can resolve to either IPv4 or IPv6: `http://127.0.0.1:11434`.

Ollama and HTTP/HTTPS proxies[](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama/common-issues#ollama-and-httphttps-proxies)

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Ollama doesn't support custom HTTP agents in its configuration. This makes it difficult to use Ollama behind custom HTTP/HTTPS proxies. Depending on your proxy configuration, it might not work at all, despite setting the `HTTP_PROXY` or `HTTPS_PROXY` environment variables.

Refer to [Ollama's FAQ](https://docs.ollama.com/faq#how-do-i-use-ollama-behind-a-proxy)
 for more information.

[PreviousOllama Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatollama)
[NextOpenAI Chat Model](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.lmchatopenai)

Last updated 10 days ago

Was this helpful?