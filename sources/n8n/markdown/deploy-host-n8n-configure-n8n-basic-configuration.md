For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration.md)
.

You can change n8n's settings using environment variables. For a full list of available configurations see [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
.

Set environment variables by command line[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#set-environment-variables-by-command-line)

-------------------------------------------------------------------------------------------------------------------------------------------------------------

### npm[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#npm)

For npm, set your desired environment variables in terminal. The command depends on your command line.

Bash CLIs:

Copy

    export <variable>=<value>

In cmd.exe:

Copy

    set <variable>=<value>

In PowerShell:

Copy

    $env:<variable>=<value>

### Docker[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#docker)

In Docker you can use the `-e` flag from the command line:

Copy

    docker run -it --rm \
     --name n8n \
     -p 5678:5678 \
     -e N8N_TEMPLATES_ENABLED="false" \
     n8nio/n8n

Docker Compose file[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#docker-compose-file)

-----------------------------------------------------------------------------------------------------------------

In Docker, you can set your environment variables in the `n8n: environment:` element of your `docker-compose.yaml` file.

For example:

Copy

    n8n:
        environment:
          - N8N_TEMPLATES_ENABLED=false

Keeping sensitive data in separate files[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#keeping-sensitive-data-in-separate-files)

-----------------------------------------------------------------------------------------------------------------------------------------------------------

You can append `_FILE` to individual environment variables to provide their configuration in a separate file, enabling you to avoid passing sensitive details using environment variables. n8n loads the data from the file with the given name, making it possible to load data from [Docker secrets](https://docs.docker.com/engine/swarm/secrets/)
 and [Kubernetes secrets](https://kubernetes.io/docs/concepts/configuration/secret/)
.

Refer to [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
 for details on each variable.

While most environment variables can use the `_FILE` suffix, it's more beneficial for sensitive data such as credentials and database configuration. Here are some examples:

Copy

    CREDENTIALS_OVERWRITE_DATA_FILE=/path/to/credentials_data
    DB_TYPE_FILE=/path/to/db_type
    DB_POSTGRESDB_DATABASE_FILE=/path/to/database_name
    DB_POSTGRESDB_HOST_FILE=/path/to/database_host
    DB_POSTGRESDB_PORT_FILE=/path/to/database_port
    DB_POSTGRESDB_USER_FILE=/path/to/database_user
    DB_POSTGRESDB_PASSWORD_FILE=/path/to/database_password
    DB_POSTGRESDB_SCHEMA_FILE=/path/to/database_schema
    DB_POSTGRESDB_SSL_CA_FILE=/path/to/ssl_ca
    DB_POSTGRESDB_SSL_CERT_FILE=/path/to/ssl_cert
    DB_POSTGRESDB_SSL_KEY_FILE=/path/to/ssl_key
    DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED_FILE=/path/to/ssl_reject_unauth

In this section[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#in-this-section)

---------------------------------------------------------------------------------------------------------

*   [Environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)
    : reference for every environment variable n8n supports.
    
*   [Configuration examples](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples)
    : examples for how to configure n8n to solve particular use cases.
    

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration#related-resources)

-------------------------------------------------------------------------------------------------------------

*   [Configure n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n)
    

[PreviousConfigure n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n)
[NextUse environment variables](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/use-environment-variables)

Last updated 10 days ago

Was this helpful?