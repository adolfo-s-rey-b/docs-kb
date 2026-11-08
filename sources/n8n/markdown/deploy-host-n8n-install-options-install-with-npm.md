For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm.md)
.

**Feature availability**

npm-based installs are deprecated from n8n 3.0.

**n8n Assistant not available**

n8n Assistant isn't available when using the npm installation method.

npm is a quick way to get started with n8n on your local machine. You must have [Node.js](https://nodejs.org/en/)
 installed. n8n requires a Node.js version between 20.19 and 24.x, inclusive.

### Try n8n with npx[](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm#try-n8n-with-npx)

You can try n8n without installing it using npx.

From the terminal, run:

Copy

    npx n8n

This command will download everything that's needed to start n8n. You can then access n8n and start building workflows by opening [http://localhost:5678](http://localhost:5678/)
.

### Install globally with npm[](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm#install-globally-with-npm)

To install n8n globally, use npm:

Copy

    npm install n8n -g

To install or update to a specific version of n8n use the `@` syntax to specify the version. For example:

Copy

    npm install -g n8n@0.126.1

To install `next`:

Copy

    npm install -g n8n@next

After the installation, start n8n by running:

Copy

    n8n
    # or <a href="#or" id="or"></a>
    n8n start

#### Next steps[](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm#next-steps)

Try out n8n using the [Quickstarts](https://docs.n8n.io/build-your-first-workflow)
.

### Updating[](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm#updating)

To update your n8n instance to the `latest` version, run:

Copy

    npm update -g n8n

To install the `next` version:

Copy

    npm install -g n8n@next

### n8n with tunnel[](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm#n8n-with-tunnel)

Use this for local development and testing. It isn't safe to use it in production.

**Development tooling**

The tunnel feature is a convenience tool for local development. The underlying implementation may change between n8n versions.

Watch a video guide to setting up the tunnel using Cloudflare or ngrok:

To use webhooks for trigger nodes of external services like GitHub, n8n has to be reachable from the web. n8n provides a tunnel service using [cloudflared](https://github.com/cloudflare/cloudflared)
 that redirects requests from the web to your local n8n instance. Docker must be installed for the tunnel to work.

There are two ways to use the tunnel, depending on how you run n8n:

**Docker required**

The tunnel uses cloudflared, which runs as a Docker container. Make sure [Docker](https://docs.docker.com/get-docker/)
 is installed on your machine, even when running n8n via npm.

For npm installations, use the **services only** approach. Start cloudflared as a standalone service, then run n8n locally:

Copy

    # Terminal 1: Start the cloudflared tunnel service <a href="#terminal-1-start-the-cloudflared-tunnel-service" id="terminal-1-start-the-cloudflared-tunnel-service"></a>
    pnpm --filter n8n-containers services --services cloudflared
    
    # Terminal 2: Start n8n locally <a href="#terminal-2-start-n8n-locally" id="terminal-2-start-n8n-locally"></a>
    pnpm dev

The `services` command starts cloudflared, fetches the public tunnel URL, and writes a `.env` file to `packages/cli/bin/.env` with `WEBHOOK_URL` and `N8N_PROXY_HOPS=1`. n8n picks up this `.env` automatically on startup.

Clean up when done:

Copy

    pnpm --filter n8n-containers services:clean

For the full stack approach (n8n and cloudflared both in containers), refer to the [Docker tunnel setup](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker#n8n-with-tunnel)
.

### Reverting an upgrade[](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm#reverting-an-upgrade)

Install the older version that you want to go back to.

If the upgrade involved a database migration:

1.  Check the feature documentation and release notes to see if there are any manual changes you need to make.
    
2.  Run `n8n db:revert` on your current version to roll back the database. If you want to revert more than one database migration, you need to repeat this process.
    

### Windows troubleshooting[](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm#windows-troubleshooting)

If you're experiencing issues running n8n on Windows, verify your Node.js environment setup. Follow Microsoft's guide to [Install NodeJS on Windows](https://learn.microsoft.com/en-us/windows/dev-environment/javascript/nodejs-on-windows)
.

### Related resources[](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-npm#related-resources)

*   [Install options](https://docs.n8n.io/deploy/host-n8n/install-options)
    
*   [One-line setup](https://docs.n8n.io/deploy/host-n8n/install-options/one-line-setup)
    
*   [Install using Docker Compose](https://docs.n8n.io/deploy/host-n8n/install-options/install-using-docker-compose)
    
*   [Install with Docker](https://docs.n8n.io/deploy/host-n8n/install-options/install-with-docker)
    
*   [Use a cloud provider](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider)
    

[PreviousInstall using Docker Compose](https://docs.n8n.io/deploy/host-n8n/install-options/install-using-docker-compose)
[NextUse a cloud provider](https://docs.n8n.io/deploy/host-n8n/install-options/use-a-cloud-provider)

Last updated 10 days ago

Was this helpful?