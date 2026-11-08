For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt)
. This page is also available as [Markdown](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database.md)
.

By default, n8n uses SQLite to save credentials, past executions, and workflows. n8n also supports PostgresDB. Refer to [Supported PostgreSQL versions](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#supported-postgresql-versions)
 for n8n's PostgreSQL version policy.

Database type by n8n installation[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#database-type-by-n8n-installation)

----------------------------------------------------------------------------------------------------------------------------------------------

The database type used varies depending on your n8n installation:

### Self-hosted n8n[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#self-hosted-n8n)

By default, self-hosted installations use **SQLite**. You can optionally configure PostgreSQL by setting the appropriate environment variables (see [PostgresDB configuration](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#postgresdb)
).

### n8n Cloud[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#n8n-cloud)

n8n Cloud installations use different databases depending on your plan tier:

*   **SQLite**: Starter, Pro, and legacy Enterprise plans
    
*   **PostgreSQL**: Enterprise Scaling plans only
    

Shared settings[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#shared-settings)

----------------------------------------------------------------------------------------------------------

The following environment variables get used by all databases:

*   `DB_TABLE_PREFIX` (default: -) - Prefix for table names
    

PostgresDB[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#postgresdb)

------------------------------------------------------------------------------------------------

### Supported PostgreSQL versions[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#supported-postgresql-versions)

n8n supports:

*   The latest two actively maintained PostgreSQL major versions (**17** and **18**, as of July 2026).
    
*   One additional major version for compatibility (**16**).
    

Run the latest minor release within your major version.

Amazon Aurora PostgreSQL is **experimental**. n8n's hosting templates offer it for high-availability setups, where Aurora recovers faster when the primary database goes down. n8n doesn't test or certify Aurora, and n8n's PostgreSQL version support doesn't extend to it. Use upstream PostgreSQL unless you specifically need what Aurora offers.

n8n doesn't support other PostgreSQL-compatible derivatives, such as AlloyDB, CockroachDB, or YugabyteDB.

The PostgreSQL project retires its oldest maintained major version and releases a new one every November, so n8n's supported version range shifts each year. Check this page for the current supported versions, rather than relying on a specific version number you've seen elsewhere.

To use PostgresDB as the database, you can provide the following environment variables:

*   `DB_TYPE=postgresdb`
    
*   `DB_POSTGRESDB_DATABASE` (default: 'n8n')
    
*   `DB_POSTGRESDB_HOST` (default: 'localhost')
    
*   `DB_POSTGRESDB_PORT` (default: 5432)
    
*   `DB_POSTGRESDB_USER` (default: 'postgres')
    
*   `DB_POSTGRESDB_PASSWORD` (default: empty)
    
*   `DB_POSTGRESDB_SCHEMA` (default: 'public')
    
*   `DB_POSTGRESDB_SSL_CA` (default: undefined): Path to the server's CA certificate used to validate the connection (opportunistic encryption isn't supported)
    
*   `DB_POSTGRESDB_SSL_CERT` (default: undefined): Path to the client's TLS certificate
    
*   `DB_POSTGRESDB_SSL_KEY` (default: undefined): Path to the client's private key corresponding to the certificate
    
*   `DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED` (default: true): If TLS connections that fail validation should be rejected
    

Copy

    export DB_TYPE=postgresdb
    export DB_POSTGRESDB_DATABASE=n8n
    export DB_POSTGRESDB_HOST=postgresdb
    export DB_POSTGRESDB_PORT=5432
    export DB_POSTGRESDB_USER=n8n
    export DB_POSTGRESDB_PASSWORD=n8n
    export DB_POSTGRESDB_SCHEMA=n8n
    
    # optional: <a href="#optional" id="optional"></a>
    export DB_POSTGRESDB_SSL_CA_FILE=$(pwd)/ca.crt
    export DB_POSTGRESDB_SSL_REJECT_UNAUTHORIZED=false
    
    n8n start

### Required permissions[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#required-permissions)

n8n needs to create and modify the schemas of the tables it uses.

Recommended permissions:

Copy

    CREATE DATABASE n8n-db;
    CREATE USER n8n-user WITH PASSWORD 'random-password';
    GRANT ALL PRIVILEGES ON DATABASE n8n-db TO n8n-user;

### TLS[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#tls)

You can choose between these configurations:

*   Not declaring (default): Connect with `SSL=off`
    
*   Declaring only the CA and unauthorized flag: Connect with `SSL=on` and verify the server's signature
    
*   Declaring `_{CERT,KEY}` and the above: Use the certificate and key for client TLS authentication
    

SQLite[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#sqlite)

----------------------------------------------------------------------------------------

This is the default database that gets used if nothing is defined.

The database file is located at: `~/.n8n/database.sqlite`

Related resources[](https://docs.n8n.io/deploy/host-n8n/configure-n8n/choose-n8ns-database#related-resources)

--------------------------------------------------------------------------------------------------------------

*   [Configure n8n](https://docs.n8n.io/deploy/host-n8n/configure-n8n)
    

[PreviousConfigure a custom workflow templates library](https://docs.n8n.io/deploy/host-n8n/configure-n8n/basic-configuration/configuration-examples/configure-a-custom-workflow-templates-library)
[NextExternal hooks](https://docs.n8n.io/deploy/host-n8n/configure-n8n/external-hooks)

Last updated 10 days ago

Was this helpful?