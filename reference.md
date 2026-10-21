# Reference
## EulaResponses
<details><summary><code>client.eula_responses.<a href="src/hiddenlayer/eula_responses/client.py">self</a>() -> SelfEulaResponsesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves the current EULA acceptance status for the authenticated user's tenant, including the version responded to and when it was last updated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.eula_responses.self_()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Credentials
<details><summary><code>client.credentials.<a href="src/hiddenlayer/credentials/client.py">list</a>(...) -> ListCredentialsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Lists all API credentials for the requester's tenant. API credentials can be used to authenticate automated processes and integrations with the HiddenLayer API. The list includes both active and inactive credentials, along with their associated metadata. If the `embed` parameter is used with `created_by_user`, the response will also include details about the user who created each credential. The response includes up to 1000 items.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.credentials.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**embed:** `typing.Optional[str]` — A comma-separated list of optional fields to embed in the response. Currently, the only supported value is `created_by_user`.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/hiddenlayer/credentials/client.py">create</a>(...) -> CredentialsWithSecret</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new API credential for authenticating automated processes and integrations with the HiddenLayer API. The credential consists of an immutable client ID and client secret pair.

If no expiry is provided, the credential will automatically expire one year from creation. In accordance with standard industry best practices, it is not recommended to set an expiration date-time more than 365 days in the future.
If an expiration date is set more than 365 days in the future, the request will be rejected with a 422 Unprocessable Entity response.

By default, if no permissions are specified, the credential will be granted all available permissions. To restrict the credential to specific permissions, provide a list of permission identifiers (scopes).
The available permissions can be found by calling [`GET /api/v2/permissions`](#operation/list_permissions_api_v2_permissions_get).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.credentials.create(
    name="some-name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**expires_at:** `typing.Optional[datetime.datetime]` 

If no expiry is provided, the credentials will automatically expire one year from creation.
In accordance with standard industry best practices, it is not recommended to set an expiration date-time
more than 365 days in the future.
    
</dd>
</dl>

<dl>
<dd>

**permissions:** `typing.Optional[typing.List[str]]` — Specifies permissions granted to the credential. If this property is omitted, then the credential will effectively have administrator permissions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.credentials.<a href="src/hiddenlayer/credentials/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently deletes an API credential. Once deleted, the credential can no longer be used to authenticate with the HiddenLayer API.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.credentials.delete(
    id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Permissions
<details><summary><code>client.permissions.<a href="src/hiddenlayer/permissions/client.py">list</a>() -> ListPermissionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Gets a list of valid permissions that can be assigned to users or API credentials.

HiddenLayer permissions follow a `{area}:{action}` format, where:
- The area name uses kebab-case (e.g., `model-version`)
- The action specifies what can be done with the resource area (e.g., r/read, w/write, or d/delete)
- Area and action are separated by a colon (:)

Hypothetical Example: `model-version:read` would grant permission to read model versions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.permissions.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Roles
<details><summary><code>client.roles.<a href="src/hiddenlayer/roles/client.py">list</a>() -> ListRolesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of roles that can be assigned to users. The platform provides several predefined roles, each with its own set of permissions:

**Admin**
- Full system access with broad privileges
- Can manage integrations, model assets, detections, and users
- Has create, delete, edit, and configuration capabilities

**Analyst**
- Focused on model scanning and detection workflows
- Can submit and update scan results
- Can review details, add notes, and close detections

**Viewer**
- Read-only access to system resources
- Can view assets, results, models, and detections
- Cannot create, edit, or delete resources

**User Admin**
- Specialized in user management
- Can create, edit, and delete users
- Limited to user administration tasks

Note: Some resources are restricted to specific service integrations and are not accessible through these roles.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.roles.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Users
<details><summary><code>client.users.<a href="src/hiddenlayer/users/client.py">list</a>() -> ListUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all users belonging to the authenticated user's tenant. The response includes up to 1000 items. **Deprecated** — use [List Users (paginated)](#tag/Users/operation/list_users_access_v2_users_get) instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.users.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/hiddenlayer/users/client.py">create</a>(...) -> CreateUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new user in the tenant. The user's email address must be unique within the tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.users.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `UserRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/hiddenlayer/users/client.py">get</a>(...) -> GetUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves details for the specified user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.users.get(
    id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/hiddenlayer/users/client.py">update</a>(...) -> User</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates details for the specified user. The user's email address must remain unique within the tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.users.update(
    id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request:** `UserRequestBody` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/hiddenlayer/users/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Permanently removes the specified user from the tenant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.users.delete(
    id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/hiddenlayer/users/client.py">reset</a>(...) -> ResetUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Initiates a password reset for the specified user by sending a password reset email.
The user must complete the reset workflow themselves via the link in the email.
The `password` field in the response is deprecated and included only for backwards compatibility.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.users.reset(
    email="email",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**email:** `str` — A user email address
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.users.<a href="src/hiddenlayer/users/client.py">me</a>() -> MeUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieves profile and role details for the currently authenticated user.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.users.me()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SsoIntegrations
<details><summary><code>client.sso_integrations.<a href="src/hiddenlayer/sso_integrations/client.py">list</a>() -> ListSsoIntegrationsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of SSO integrations associated with the requester's tenant. The results will be sorted by age in descending order (i.e. newest to oldest).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.sso_integrations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sso_integrations.<a href="src/hiddenlayer/sso_integrations/client.py">create</a>(...) -> SsoIntegrationSamlV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates an SSO integration record that can be used to authenticate users with HiddenLayer. SSO integrations
cannot be enabled until all required information is populated to form a trusted connection between the HiddenLayer
and the Identity Provider (IdP).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.sso_integrations.create(
    type="saml_v2",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `SsoIntegrationsCreateRequestType` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `SsoIntegrationName` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sso_integrations.<a href="src/hiddenlayer/sso_integrations/client.py">get</a>(...) -> SsoIntegrationSamlV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get SSO Integration
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.sso_integrations.get(
    id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sso_integrations.<a href="src/hiddenlayer/sso_integrations/client.py">update</a>(...) -> SsoIntegrationSamlV2</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing SSO integration record that can be used to authenticate users with HiddenLayer. SSO integrations
cannot be enabled until all required information is populated to form a trusted connection between the HiddenLayer
and the Identity Provider (IdP).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.sso_integrations.update(
    id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[SsoIntegrationName]` 
    
</dd>
</dl>

<dl>
<dd>

**is_enabled:** `typing.Optional[bool]` — Indicates whether or not the SSO integration is enabled
    
</dd>
</dl>

<dl>
<dd>

**request_signing:** `typing.Optional[SsoIntegrationRequestSigning]` 
    
</dd>
</dl>

<dl>
<dd>

**managed_domains:** `typing.Optional[SsoIntegrationManagedDomains]` 
    
</dd>
</dl>

<dl>
<dd>

**identity_provider:** `typing.Optional[SamlIdentityProvider]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Interactions
<details><summary><code>client.interactions.<a href="src/hiddenlayer/interactions/client.py">analyze</a>(...) -> EnrichedResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs a detailed security analysis of the input and/or output of LLM interactions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer, InteractionsMetadata
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.interactions.analyze(
    hl_project_id="internal-search-chatbot",
    metadata=InteractionsMetadata(
        model="gpt-5",
        requester_id="user-1234",
        provider="openai",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**metadata:** `InteractionsMetadata` 
    
</dd>
</dl>

<dl>
<dd>

**hl_project_id:** `typing.Optional[str]` — The ID or alias for the Project to govern the request processing.
    
</dd>
</dl>

<dl>
<dd>

**input:** `typing.Optional[InteractionsInput]` 
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[InteractionsOutput]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## PromptAnalyzer
<details><summary><code>client.prompt_analyzer.<a href="src/hiddenlayer/prompt_analyzer/client.py">create</a>(...) -> HiddenLayerPromptAnalyzerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyze LLM Prompt and Response
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.prompt_analyzer.create(
    hl_project_id="internal-search-chatbot",
    prompt="Hello World",
    output="Hello, how can I help you today?",
    model="mistral-tiny",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**prompt:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**hl_project_id:** `typing.Optional[str]` — The ID or alias for the Project to govern the request processing.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — The identifier for the requester to be used if MLDR is enabled
    
</dd>
</dl>

<dl>
<dd>

**output:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**model:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Runtime
<details><summary><code>client.runtime.<a href="src/hiddenlayer/runtime/client.py">evaluate_interaction</a>(...) -> InteractionEvaluationResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Performs synchronous security evaluation on an LLM **interaction**. The
interaction can be a standalone user prompt, a standalone model response,
a partial exchange, or a long multi-turn message history. The endpoint 
imposes no requirement that the messages form a complete request/response pair.

The request carries `metadata` and an `interaction` payload. The `interaction`
field accepts either:

- the **canonical**, provider-agnostic form (`CanonicalInteraction`) —
  an ordered sequence of messages (user, assistant, system, tool) with their
  role and content parts, and optionally the tool catalog that was in scope; or
- a **native LLM-provider payload** passed through verbatim. Supported
  provider formats:
  - [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat)
  - [OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)
  - [Anthropic Messages](https://docs.anthropic.com/en/api/messages)

Returns the evaluation context (`evaluated_interaction`): the canonicalized messages
with per-message signals and findings attached. Also returns the policy
outcome, which carries the enforcement action, threat level, any detections,
and the effective payload the caller should forward (`outcome.effective_interaction`).

Use this endpoint when you need full evaluation results. For inline pass-through
(provider request/response payloads returned in the same provider format), use
the request-evaluations and response-evaluations endpoints instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer, InteractionEvaluationRequestMetadata, CanonicalInteraction, CanonicalInteractionMessage, ContentPart_Text
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.runtime.evaluate_interaction(
    hl_project_id="internal-search-chatbot",
    metadata=InteractionEvaluationRequestMetadata(
        model="gpt-4-turbo",
        requester_id="user-12345",
        provider="openai",
        external_session_id="sess_4b8cde94604f4c389406a0b2f806069a",
    ),
    interaction=CanonicalInteraction(
        messages=[
            CanonicalInteractionMessage(
                role="user",
                content=[
                    ContentPart_Text(
                        text="Hello, how can I help you today?",
                    )
                ],
            ),
            CanonicalInteractionMessage(
                role="assistant",
                content=[
                    ContentPart_Text(
                        text="Hello, how can I help you today?",
                    )
                ],
            )
        ],
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**metadata:** `InteractionEvaluationRequestMetadata` 
    
</dd>
</dl>

<dl>
<dd>

**interaction:** `InteractionEvaluationRequestInteraction` 

The interaction to evaluate. Accepts either the canonical form
(`CanonicalInteraction` — `messages` and optional `tools_available`)
or a native LLM-provider payload passed through verbatim. Supported
provider formats are OpenAI Chat Completions, OpenAI Responses, and
Anthropic Messages. `ProviderPayload` is intentionally permissive
(any JSON object) so callers can supply provider-native shapes
without schema constraints.
    
</dd>
</dl>

<dl>
<dd>

**hl_project_id:** `typing.Optional[str]` — The ID or alias for the Project to govern the request processing.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runtime.<a href="src/hiddenlayer/runtime/client.py">evaluate_request</a>(...) -> ProviderPayload</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyzes an LLM request payload for security threats before it is sent to the model.

Accepts any valid provider request payload and returns:
- If detect or redact action: the request payload (potentially modified) in the provider's request format
- If block action: a canned block message in the provider's response format

If the project is in monitor mode, the endpoint does not block or redact. It returns the
request payload unchanged.

Use this endpoint inline in your LLM pipeline to evaluate prompts before they reach the model.

Supported provider formats:
- [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat)
- [OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)
- [Anthropic Messages](https://docs.anthropic.com/en/api/messages)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.runtime.evaluate_request(
    hl_project_id="internal-search-chatbot",
    hl_runtime_session_id="sess_4b8cde94604f4c389406a0b2f806069a",
    request={
        "model": "gpt-4",
        "messages": [{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": "What is the capital of France?"}],
        "max_tokens": 1000,
        "temperature": 0.7
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ProviderPayload` 
    
</dd>
</dl>

<dl>
<dd>

**hl_project_id:** `typing.Optional[str]` — The ID or alias for the Project to govern the request processing.
    
</dd>
</dl>

<dl>
<dd>

**hl_runtime_session_id:** `typing.Optional[str]` 

An externally-defined session identifier to group interactions in separate requests into a
single session. The identifier should be unique across the all sessions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.runtime.<a href="src/hiddenlayer/runtime/client.py">evaluate_response</a>(...) -> ProviderPayload</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Analyzes an LLM response payload for security threats after it is received from the model.

Accepts any valid provider response payload and returns:
- If detect or redact action: the response payload (potentially modified) in the provider's response format
- If block action: a canned block message in the provider's response format

If the project is in monitor mode, the endpoint does not block or redact. It returns the
response payload unchanged.

Use this endpoint inline in your LLM pipeline to evaluate model outputs before returning them to users.

Supported provider formats:
- [OpenAI Chat Completions](https://platform.openai.com/docs/api-reference/chat)
- [OpenAI Responses](https://platform.openai.com/docs/api-reference/responses)
- [Anthropic Messages](https://docs.anthropic.com/en/api/messages)
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.runtime.evaluate_response(
    hl_project_id="internal-search-chatbot",
    hl_runtime_session_id="sess_4b8cde94604f4c389406a0b2f806069a",
    request={
        "id": "chatcmpl-abc123",
        "object": "chat.completion",
        "created": 1704067200,
        "model": "gpt-4",
        "choices": [{"index": 0, "message": {"role": "assistant", "content": "The capital of France is Paris."}, "finish_reason": "stop"}],
        "usage": {"prompt_tokens": 25, "completion_tokens": 10, "total_tokens": 35}
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `ProviderPayload` 
    
</dd>
</dl>

<dl>
<dd>

**hl_project_id:** `typing.Optional[str]` — The ID or alias for the Project to govern the request processing.
    
</dd>
</dl>

<dl>
<dd>

**hl_runtime_session_id:** `typing.Optional[str]` 

An externally-defined session identifier to group interactions in separate requests into a
single session. The identifier should be unique across the all sessions.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sensors
<details><summary><code>client.sensors.<a href="src/hiddenlayer/sensors/client.py">create</a>(...) -> SensorSorItemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.sensors.create(
    plaintext_name="plaintext_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**plaintext_name:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**version:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**adhoc:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sensors.<a href="src/hiddenlayer/sensors/client.py">retrieve</a>(...) -> SensorSorItemResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.sensors.retrieve(
    sensor_id="sensor_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sensor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sensors.<a href="src/hiddenlayer/sensors/client.py">update</a>(...) -> SensorSorUpdateResponseModel</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.sensors.update(
    sensor_id="sensor_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sensor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**plaintext_name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**active:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Dict[str, typing.Any]]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sensors.<a href="src/hiddenlayer/sensors/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.sensors.delete(
    sensor_id="sensor_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sensor_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sensors.<a href="src/hiddenlayer/sensors/client.py">query_legacy</a>(...) -> SensorSorQueryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.sensors.query_legacy()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SensorSorQueryRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sensors.<a href="src/hiddenlayer/sensors/client.py">query</a>(...) -> SensorSorQueryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

⚠️ **DEPRECATED**: This endpoint will be removed after April 13, 2026.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.sensors.query()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `SensorSorQueryRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Models
<details><summary><code>client.models.<a href="src/hiddenlayer/models/client.py">retrieve</a>(...) -> SensorSorModel</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.retrieve(
    model_id="model_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/hiddenlayer/models/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.delete(
    model_id="model_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/hiddenlayer/models/client.py">list</a>() -> typing.List[SensorSorModel]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.<a href="src/hiddenlayer/models/client.py">update</a>(...) -> UpdateModelsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer, SensorSorModel
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.update(
    request=[
        SensorSorModel(
            name="loan application",
            source="azure",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `typing.List[SensorSorModel]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Access Users
<details><summary><code>client.access.users.<a href="src/hiddenlayer/access/users/client.py">list</a>(...) -> ListUsersResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of users belonging to the authenticated user's tenant. Use the `cursor` parameter to navigate through pages of results. Replaces the deprecated `GET /api/v2/users` endpoint.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.access.users.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[Limit]` — Limit the number of items returned
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort by email or created_at, ascending (+ or no prefix) or descending (-). Ignored when a cursor is supplied — the cursor preserves the sort from the page it was issued on.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Access Permissions
<details><summary><code>client.access.permissions.<a href="src/hiddenlayer/access/permissions/client.py">list</a>() -> ListPermissionsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Returns permissions grouped by platform area, ready for rendering in a UI permission selector.

Use this endpoint when building interfaces that let users choose permissions — for example,
an API key creation modal. Each area group represents a platform capability (such as **AI Portfolio**
or **Runtime Security**) and contains the individual permission area elements — and the permissions
available on each — within it.

If you need a flat list of all permissions, use
[`GET /api/v2/permissions`](#operation/list_permissions_api_v2_permissions_get) instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.access.permissions.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Access Tokens
<details><summary><code>client.access.tokens.<a href="src/hiddenlayer/access/tokens/client.py">short_lived</a>() -> ShortLivedTokenResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Exchange a valid user access token for a short-lived JWT with minimal scopes. This endpoint is suitable for scenarios where a long-lived or broad-scope token is inappropriate. A typical use case is authenticating WebSocket connections, where the token may be passed via query parameters.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.access.tokens.short_lived()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory Assets
<details><summary><code>client.asset_inventory.assets.<a href="src/hiddenlayer/asset_inventory/assets/client.py">list_v1</a>(...) -> ListV1AssetsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.list_v1(
    sort="+discovered_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**provider:** `typing.Optional[ListV1AssetsRequestProvider]` — Filter by service provider (providers are OR'ed)
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[ListV1AssetsRequestAccountId]` — Filter by account ID
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[ListV1AssetsRequestRegion]` — Filter by region
    
</dd>
</dl>

<dl>
<dd>

**service:** `typing.Optional[ListV1AssetsRequestService]` — Filter by service (services are OR'ed)
    
</dd>
</dl>

<dl>
<dd>

**asset_type:** `typing.Optional[ListV1AssetsRequestAssetType]` — Filter by asset type
    
</dd>
</dl>

<dl>
<dd>

**is_public:** `typing.Optional[ListV1AssetsRequestIsPublic]` — Filter by public status
    
</dd>
</dl>

<dl>
<dd>

**is_retrievable:** `typing.Optional[ListV1AssetsRequestIsRetrievable]` — Filter by retrievability status
    
</dd>
</dl>

<dl>
<dd>

**hl_resource_type:** `typing.Optional[ListV1AssetsRequestHlResourceType]` — Filter by AI Asset being linked to a HiddenLayer resource
    
</dd>
</dl>

<dl>
<dd>

**policy_status:** `typing.Optional[ListV1AssetsRequestPolicyStatus]` — Filter by policy status
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `typing.Optional[TagNameFilter]` — Filter by tag name regardless of source. Matches across both custom and discovered tags.
    
</dd>
</dl>

<dl>
<dd>

**tag_def:** `typing.Optional[TagDefFilter]` — Filter by tag definition (source + name). The top-level operator (`in` or `all`) governs how all entries across sources are combined. Within each operator, use `custom` and/or `discovered` keys to specify tag names by source.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[TagValueFilter]` — Filter by tag (source + name + value). The top-level operator (`in` or `all`) governs how all entries across sources are combined. Within each operator, use `custom` and/or `discovered` keys to specify tag name/value pairs by source.
    
</dd>
</dl>

<dl>
<dd>

**embed:** `typing.Optional[typing.Union[Embed, typing.Sequence[Embed]]]` — Sub-resources to include in the response
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — allow sorting by discovery timestamp or last sync time, ascending (+) or the default descending (-)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.<a href="src/hiddenlayer/asset_inventory/assets/client.py">get_v1</a>(...) -> AiAsset</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.get_v1(
    asset_id="asset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The ID of the AI asset
    
</dd>
</dl>

<dl>
<dd>

**embed:** `typing.Optional[typing.Union[Embed, typing.Sequence[Embed]]]` — Sub-resources to include in the response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.<a href="src/hiddenlayer/asset_inventory/assets/client.py">graph</a>(...) -> AiAssetInventoryV1AssetGraphNode</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.graph(
    asset_id="asset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The ID of the root AI asset
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` — The depth of the graph to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.<a href="src/hiddenlayer/asset_inventory/assets/client.py">filters_v1</a>() -> FiltersV1AssetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the available filter fields and their values. Tag names are included as a filter field.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.filters_v1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.<a href="src/hiddenlayer/asset_inventory/assets/client.py">tags_v1</a>(...) -> AiAssetInventoryV1AssetTagMap</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns all custom and discovered tags assigned to the given asset.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.tags_v1(
    asset_id="asset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The ID of the AI asset
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.<a href="src/hiddenlayer/asset_inventory/assets/client.py">list</a>(...) -> ListAssetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Search and list the AI assets in your inventory. Provide a
full-text search query with `q`, and optionally narrow the
results with the available filters such as provider, cloud
account, region, service, asset type, policy status, tags
(`tag_name`, `tag_def`, and `tag`), relationship to another
asset (`related_to`), and — for MODEL assets — the model id
(`model_id`), model name (`model_name`), or the latest scan's
start time (`scan_started_at`).
Results are returned in cursor-paginated pages of `page_size`
items; follow the `next` cursor to retrieve subsequent pages.
See the `sort` parameter for available sort fields.

To discover the filterable fields and their available values for
your tenant, call
[`GET /asset-inventory/v2/assets/filters`](/api/assets-and-integrations/ai-asset-inventory/v2/ai-asset-inventory/inventory/get_ai_asset_filters_v2).

The underlying query runs under a configurable server-side
statement timeout. A filter or sort combination expensive
enough to exceed it — typically an arbitrary-attribute filter or
sort over a very large tenant — receives `422 Unprocessable
Entity` with a "query exceeds allowed cost/time limit" message
suggesting index-backed sort fields to retry with.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.list(
    page_size=50,
    sort="-created_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `typing.Optional[str]` — Search query string
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**annotating_service:** `typing.Optional[ListAssetsRequestAnnotatingService]` 

Filter by annotating service; returns only assets that carry at least one
annotation from the given service(s). Multiple values are OR'ed.
The annotating service is a free-form identifier (for example, `discovery`).

When sorting by an annotation attribute (`sort=attributes.*`), this
parameter must specify exactly one service.
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[AttributeFilter]` 

Filter by annotation attributes. Each key is a dotted path
into an annotation's `attributes` map (for example, `provider`
or `configuration.model.layers`); its value is a set of
comparison operators (`eq`, `in`, `gt`, `gte`, `lt`, `lte`,
`contains`) applied to the value at that path. Attribute names
and paths are not fixed by this API — any attribute a
contributing service records can be filtered on.

All conditions are combined with AND: across different paths,
and across multiple operators on the same path (so `gte` and
`lte` together form a range). The only OR available is `in`,
which matches a single path against any of several values;
there is no OR or grouping across different paths.

Serialized as a deepObject. A scalar operator carries a single
value (for example, `attributes[configuration.model.layers][gte]=5`),
while `in` carries a comma-separated list (for example,
`attributes[provider][in]=AWS,AZURE`).
    
</dd>
</dl>

<dl>
<dd>

**asset_type:** `typing.Optional[ListAssetsRequestAssetType]` — Filter by asset type (free-form string); multiple values are OR'ed
    
</dd>
</dl>

<dl>
<dd>

**policy_status:** `typing.Optional[ListAssetsRequestPolicyStatus]` — Filter by policy status
    
</dd>
</dl>

<dl>
<dd>

**scan_started_at:** `typing.Optional[ListAssetsRequestScanStartedAt]` 

Filter MODEL assets by the start time of their latest
supply-chain scan. Combine a `gt`/`gte` bound with a
`lt`/`lte` bound to express a range. Assets with no
supply-chain scan data are excluded when this filter is
applied.

This is the indexed, purpose-built filter for scan start
time — prefer it over the equivalent
`attributes[latest_scan.start_time]` path on the generic
`attributes` filter, which reaches the same data without
index support.
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `typing.Optional[ListAssetsRequestModelId]` 

Filter MODEL assets by the model id assigned by the scanning
pipeline (the supply-chain annotation's own identifier, returned
as that annotation's `key`). Assets with no supply-chain scan
data are excluded when this filter is applied.
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `typing.Optional[ListAssetsRequestModelName]` 

Filter MODEL assets by the name reported by their latest
supply-chain scan. Use `eq` for an exact match or `contains`
for a substring match. Assets with no supply-chain scan data
are excluded when this filter is applied.

This is the indexed, purpose-built filter for model name —
prefer it over the equivalent
`attributes[model_card.name]` path on the generic `attributes`
filter, whose `contains` is not index-backed.
    
</dd>
</dl>

<dl>
<dd>

**related_to:** `typing.Optional[ListAssetsRequestRelatedTo]` 

Filter to assets directly related to the given asset. An asset
matches when a relationship connects it to the given asset ID,
in either direction (as source or target). Only direct
(one-hop) relationships are considered.
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `typing.Optional[TagNameFilter]` — Filter by tag name regardless of source. Matches across both custom and discovered tags.
    
</dd>
</dl>

<dl>
<dd>

**tag_def:** `typing.Optional[TagDefFilter]` — Filter by tag definition (source + name). The top-level operator (`in` or `all`) governs how all entries across sources are combined. Within each operator, use `custom` and/or `discovered` keys to specify tag names by source.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[TagValueFilter]` — Filter by tag (source + name + value). The top-level operator (`in` or `all`) governs how all entries across sources are combined. Within each operator, use `custom` and/or `discovered` keys to specify tag name/value pairs by source.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` 

Sort by field, ascending (+) or descending (-).

Sort on a top-level field (`created_at`, `updated_at`,
`first_synced_at`, `asset_type`, `policy_status`) or on an annotation attribute by
prefixing a dotted path into the `attributes` map with
`attributes.` — for example, `attributes.provider` or
`attributes.configuration.model.layers`. This mirrors the
`attributes` filter: the same dotted paths that can be filtered
on can also be sorted on. Attribute names and paths are not
fixed by this API, so the set of sortable paths grows with your
data; attribute values are ordered as strings.

For the supply-chain view (`annotating_service[in]=supply-chain`),
`attributes.scan_started_at` and `attributes.model_name` are
curated field names, not literal attribute paths — they resolve
to that annotation's `latest_scan.start_time` and
`model_card.name` respectively.

Ordering semantics: an asset whose annotation does not carry
the sorted attribute is still returned — the missing value
sorts as the empty string, placing the asset first ascending
and last descending. Assets with equal sort values are
ordered by asset `id` ascending, so the overall order (and
cursor pagination over it) is deterministic.

Sorting by an annotation attribute (`attributes.*`) requires
`annotating_service[in]` to specify **exactly one** service. An
asset can carry annotations from multiple services, each with its
own `attributes` map; without a single-service constraint the sort
key is ambiguous. Requests that combine an `attributes.*` sort with
zero or multiple annotating services are rejected with
`422 Unprocessable Entity`.

When `annotating_service[in]=supply-chain` and no `sort` is
given, results default to `attributes.scan_started_at`
descending (most recently scanned first).
    
</dd>
</dl>

<dl>
<dd>

**embed:** `typing.Optional[typing.Union[ListAssetsRequestEmbedItem, typing.Sequence[ListAssetsRequestEmbedItem]]]` — Sub-resources to include in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.<a href="src/hiddenlayer/asset_inventory/assets/client.py">suggestions</a>(...) -> SuggestionsAssetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Return typeahead suggestions for a partial search term, to help
build asset search queries as the user types. The same filters
available on the asset list endpoint can be applied to scope the
suggestions.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.suggestions(
    q="q",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Prefix text to get suggestions for
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of suggestions to return
    
</dd>
</dl>

<dl>
<dd>

**annotating_service:** `typing.Optional[SuggestionsAssetsRequestAnnotatingService]` 

Filter by annotating service; returns only assets that carry at least one
annotation from the given service(s). Multiple values are OR'ed.
The annotating service is a free-form identifier (for example, `discovery`).
    
</dd>
</dl>

<dl>
<dd>

**attributes:** `typing.Optional[AttributeFilter]` 

Filter by annotation attributes. Each key is a dotted path
into an annotation's `attributes` map (for example, `provider`
or `configuration.model.layers`); its value is a set of
comparison operators (`eq`, `in`, `gt`, `gte`, `lt`, `lte`,
`contains`) applied to the value at that path. Attribute names
and paths are not fixed by this API — any attribute a
contributing service records can be filtered on.

All conditions are combined with AND: across different paths,
and across multiple operators on the same path (so `gte` and
`lte` together form a range). The only OR available is `in`,
which matches a single path against any of several values;
there is no OR or grouping across different paths.

Serialized as a deepObject. A scalar operator carries a single
value (for example, `attributes[configuration.model.layers][gte]=5`),
while `in` carries a comma-separated list (for example,
`attributes[provider][in]=AWS,AZURE`).
    
</dd>
</dl>

<dl>
<dd>

**asset_type:** `typing.Optional[SuggestionsAssetsRequestAssetType]` — Filter by asset type (free-form string); multiple values are OR'ed
    
</dd>
</dl>

<dl>
<dd>

**policy_status:** `typing.Optional[SuggestionsAssetsRequestPolicyStatus]` — Filter by policy status
    
</dd>
</dl>

<dl>
<dd>

**scan_started_at:** `typing.Optional[SuggestionsAssetsRequestScanStartedAt]` 

Filter MODEL assets by the start time of their latest
supply-chain scan. Combine a `gt`/`gte` bound with a
`lt`/`lte` bound to express a range. Assets with no
supply-chain scan data are excluded when this filter is
applied.

This is the indexed, purpose-built filter for scan start
time — prefer it over the equivalent
`attributes[latest_scan.start_time]` path on the generic
`attributes` filter, which reaches the same data without
index support.
    
</dd>
</dl>

<dl>
<dd>

**model_id:** `typing.Optional[SuggestionsAssetsRequestModelId]` 

Filter MODEL assets by the model id assigned by the scanning
pipeline (the supply-chain annotation's own identifier, returned
as that annotation's `key`). Assets with no supply-chain scan
data are excluded when this filter is applied.
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `typing.Optional[SuggestionsAssetsRequestModelName]` 

Filter MODEL assets by the name reported by their latest
supply-chain scan. Use `eq` for an exact match or `contains`
for a substring match. Assets with no supply-chain scan data
are excluded when this filter is applied.

This is the indexed, purpose-built filter for model name —
prefer it over the equivalent
`attributes[model_card.name]` path on the generic `attributes`
filter, whose `contains` is not index-backed.
    
</dd>
</dl>

<dl>
<dd>

**related_to:** `typing.Optional[SuggestionsAssetsRequestRelatedTo]` 

Filter to assets directly related to the given asset. An asset
matches when a relationship connects it to the given asset ID,
in either direction (as source or target). Only direct
(one-hop) relationships are considered.
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `typing.Optional[TagNameFilter]` — Filter by tag name regardless of source. Matches across both custom and discovered tags.
    
</dd>
</dl>

<dl>
<dd>

**tag_def:** `typing.Optional[TagDefFilter]` — Filter by tag definition (source + name). The top-level operator (`in` or `all`) governs how all entries across sources are combined. Within each operator, use `custom` and/or `discovered` keys to specify tag names by source.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[TagValueFilter]` — Filter by tag (source + name + value). The top-level operator (`in` or `all`) governs how all entries across sources are combined. Within each operator, use `custom` and/or `discovered` keys to specify tag name/value pairs by source.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.<a href="src/hiddenlayer/asset_inventory/assets/client.py">filters</a>(...) -> FilterFacetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Return the filterable fields of the
[asset list endpoint](/api/assets-and-integrations/ai-asset-inventory/v2/ai-asset-inventory/inventory/list_ai_assets_v2)
together with their available values for your tenant, for
building a filter UI. Each facet identifies the exact list
filter it maps to: apply a selection by sending the facet's
`param` with the chosen `values` to
`GET /asset-inventory/v2/assets` — no field-name translation
layer required.

- **Unscoped** (no parameters) — returns the service-independent
  facets: `asset_type`, `policy_status`, and
  `annotating_service`. The `annotating_service` facet lists the
  services that have annotated assets in your tenant, so it
  doubles as the bootstrap for the scoped call.
- **Scoped** (`annotating_service[eq]` naming one service) —
  additionally returns that service's annotation attribute
  facets (for example, `attributes.provider` for the `discovery`
  service), with values enumerated from that service's
  annotations only. The attribute facets a service exposes are
  server-defined and evolve as annotating services register
  them; a service exposing none returns just the
  service-independent facets.
- The scope takes the scalar `[eq]` operator because it is a
  single service; the list endpoint's many-valued
  `annotating_service[in]` filter form is rejected here with
  `422 Unprocessable Entity`. (An `annotating_service` facet
  selection still round-trips to the list endpoint via `[in]`,
  as its `param` states.)

The underlying query runs under a configurable server-side
statement timeout; a tenant whose data exceeds it receives
`422 Unprocessable Entity` with a
"query exceeds allowed cost/time limit" message rather than an
unbounded query.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.filters()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**annotating_service:** `typing.Optional[FiltersAssetsRequestAnnotatingService]` 

Scope the facets to a single annotating service: the
response additionally includes that service's annotation
attribute facets. The scope is one service, so it takes the
scalar `[eq]` operator (`annotating_service[eq]=discovery`);
the list endpoint's many-valued `[in]` form is rejected
with `422 Unprocessable Entity`. Omit to receive only the
service-independent facets.

This is the only parameter the endpoint honors. Other list
endpoint filter parameters are accepted for wire
compatibility but do not narrow the facet values (malformed
ones are still rejected with `422 Unprocessable Entity`).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.<a href="src/hiddenlayer/asset_inventory/assets/client.py">get</a>(...) -> Asset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Retrieve a single asset by its unique ID. The response contains
the full asset, including its creation and last-updated
timestamps and its current set of annotations. Each annotation
carries its `annotating_service` and an `attributes` property
map holding the details that service observed.

Embedding `projects` additionally requires the `project:read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.get(
    asset_id="asset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The server-assigned UUID of the asset.
    
</dd>
</dl>

<dl>
<dd>

**embed:** `typing.Optional[typing.Union[GetAssetsRequestEmbedItem, typing.Sequence[GetAssetsRequestEmbedItem]]]` — Sub-resources to include in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.<a href="src/hiddenlayer/asset_inventory/assets/client.py">discovered_graph</a>(...) -> AssetGraphNode</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Retrieve the relationship graph for an AI asset, starting from that
asset and following its relationships to the assets it connects to.
Use this to show how an asset relates to others — for example, the
models an endpoint serves, or the assets derived from a given model.

The asset is identified by its `asset_id`. The response is a tree
rooted at that asset: each node lists its outgoing `relationships`,
and each relationship gives its `relationship_type`, optional
`metadata`, and the target `asset` it points to. Only outgoing
relationships are followed, and traversal stops once `depth` levels
have been reached.

Requires the `asset:read` scope.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.discovered_graph(
    asset_id="asset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The server-assigned UUID of the asset at the root of the graph.
    
</dd>
</dl>

<dl>
<dd>

**depth:** `typing.Optional[int]` 

Maximum number of outbound hops to traverse from the root
asset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.<a href="src/hiddenlayer/asset_inventory/assets/client.py">tags</a>(...) -> AssetTagMap</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Returns all custom and discovered tags assigned to the given asset.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.tags(
    asset_id="asset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The server-assigned UUID of the asset.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory Relationships
<details><summary><code>client.asset_inventory.relationships.<a href="src/hiddenlayer/asset_inventory/relationships/client.py">get</a>(...) -> AiAssetInventoryV1AssetRelationship</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.relationships.get(
    relationship_id="relationship_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**relationship_id:** `str` — The ID of the AI asset relationship
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory Metrics
<details><summary><code>client.asset_inventory.metrics.<a href="src/hiddenlayer/asset_inventory/metrics/client.py">provider_counts_v1</a>() -> AiAssetInventoryV1ProviderCounts</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.metrics.provider_counts_v1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.metrics.<a href="src/hiddenlayer/asset_inventory/metrics/client.py">region_counts_v1</a>() -> AiAssetInventoryV1RegionCounts</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.metrics.region_counts_v1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.metrics.<a href="src/hiddenlayer/asset_inventory/metrics/client.py">asset_type_counts_v1</a>() -> AiAssetInventoryV1AssetTypeCounts</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.metrics.asset_type_counts_v1()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.metrics.<a href="src/hiddenlayer/asset_inventory/metrics/client.py">provider_counts</a>() -> ProviderCounts</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Return the number of AI assets in your inventory grouped by
cloud provider (for example, AWS, Azure, GCP, and Databricks).
Assets from providers outside this set are counted under
`other`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.metrics.provider_counts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.metrics.<a href="src/hiddenlayer/asset_inventory/metrics/client.py">region_counts</a>() -> RegionCounts</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Return the number of AI assets in your inventory grouped by
geographic location, broken down both by country and by
higher-level geographic region (for example, North America or
Europe).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.metrics.region_counts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.metrics.<a href="src/hiddenlayer/asset_inventory/metrics/client.py">asset_type_counts</a>() -> AssetTypeCounts</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Return the number of AI assets in your inventory grouped by
asset type (for example, model, endpoint, or agent).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.metrics.asset_type_counts()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory Resources
<details><summary><code>client.asset_inventory.resources.<a href="src/hiddenlayer/asset_inventory/resources/client.py">list</a>(...) -> ListResourcesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.resources.list(
    page_size=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListResourcesRequestType]` — The type of HiddenLayer resource
    
</dd>
</dl>

<dl>
<dd>

**resource_id:** `typing.Optional[ListResourcesRequestResourceId]` — The ID of the HiddenLayer resource
    
</dd>
</dl>

<dl>
<dd>

**linked_at:** `typing.Optional[ListResourcesRequestLinkedAt]` — The datetime when the HiddenLayer resource was linked to the AI asset
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — The field to sort by
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory Scans
<details><summary><code>client.asset_inventory.scans.<a href="src/hiddenlayer/asset_inventory/scans/client.py">get</a>(...) -> AssetScan</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.scans.get(
    scan_id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scan_id:** `str` — A Model Scan ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory Tags
<details><summary><code>client.asset_inventory.tags.<a href="src/hiddenlayer/asset_inventory/tags/client.py">list_v1</a>(...) -> AiAssetInventoryV1TagDefinitionList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of tag definitions. Optionally filter by source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.tags.list_v1(
    sort="+name",
    page_size=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source:** `typing.Optional[ListV1TagsRequestSource]` — Filter by tag source
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Prefix text to match against tag names
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort by field, ascending (+) or descending (-). Defaults to +name for a stable alphabetical order.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.tags.<a href="src/hiddenlayer/asset_inventory/tags/client.py">list</a>(...) -> TagDefinitionList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Returns a cursor-paginated list of tag definitions. Optionally filter by source.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.tags.list(
    sort="+name",
    page_size=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**source:** `typing.Optional[ListTagsRequestSource]` — Filter by tag source.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Prefix text to match against tag names.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort by field, ascending (+) or descending (-). Defaults to +name for a stable alphabetical order.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory CustomTags
<details><summary><code>client.asset_inventory.custom_tags.<a href="src/hiddenlayer/asset_inventory/custom_tags/client.py">update_v1</a>(...) -> AiAssetInventoryV1TagDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates a tag definition. Only the name can be changed at this time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.custom_tags.update_v1(
    tag_name="tag_name",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_name:** `str` — The current tag name
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The new tag name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.custom_tags.<a href="src/hiddenlayer/asset_inventory/custom_tags/client.py">values_v1</a>(...) -> AiAssetInventoryV1TagValueList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of values for a given custom tag name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.custom_tags.values_v1(
    tag_name="tag_name",
    sort="+value",
    page_size=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_name:** `str` — The custom tag name
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort by field, ascending (+) or descending (-). Defaults to +value for a stable alphabetical order.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Prefix text to match against tag values
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.custom_tags.<a href="src/hiddenlayer/asset_inventory/custom_tags/client.py">update</a>(...) -> TagDefinition</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Updates a tag definition. Only the name can be changed at this time.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.custom_tags.update(
    tag_name="tag_name",
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_name:** `str` — The current tag name.
    
</dd>
</dl>

<dl>
<dd>

**name:** `str` — The new tag name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.custom_tags.<a href="src/hiddenlayer/asset_inventory/custom_tags/client.py">values</a>(...) -> TagValueList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Returns a cursor-paginated list of values for a given custom tag name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.custom_tags.values(
    tag_name="tag_name",
    sort="+value",
    page_size=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_name:** `str` — The custom tag name.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort by field, ascending (+) or descending (-). Defaults to +value for a stable alphabetical order.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Prefix text to match against tag values.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory DiscoveredTags
<details><summary><code>client.asset_inventory.discovered_tags.<a href="src/hiddenlayer/asset_inventory/discovered_tags/client.py">values_v1</a>(...) -> AiAssetInventoryV1TagValueList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a paginated list of values for a given discovered tag name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.discovered_tags.values_v1(
    tag_name="tag_name",
    sort="+value",
    page_size=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_name:** `str` — The discovered tag name
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort by field, ascending (+) or descending (-). Defaults to +value for a stable alphabetical order.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Prefix text to match against tag values
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.discovered_tags.<a href="src/hiddenlayer/asset_inventory/discovered_tags/client.py">values</a>(...) -> TagValueList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Returns a cursor-paginated list of values for a given discovered tag name.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.discovered_tags.values(
    tag_name="tag_name",
    sort="+value",
    page_size=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tag_name:** `str` — The discovered tag name.
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort by field, ascending (+) or descending (-). Defaults to +value for a stable alphabetical order.
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Prefix text to match against tag values.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory Annotations
<details><summary><code>client.asset_inventory.annotations.<a href="src/hiddenlayer/asset_inventory/annotations/client.py">get</a>(...) -> Asset</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Resolve an asset by the pair of `annotating_service` and that service's
`key`. Use this when the producer's identifier is known but the
server-generated asset ID is not.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.annotations.get(
    annotating_service="annotating_service",
    annotating_service_key="annotating_service_key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**annotating_service:** `str` 

The service that contributed the annotation used to resolve the asset.
Must be URL-encoded if it contains special characters.
    
</dd>
</dl>

<dl>
<dd>

**annotating_service_key:** `str` 

The contributing service's stable key for the asset. Must be
URL-encoded if it contains special characters, including `/`.
    
</dd>
</dl>

<dl>
<dd>

**embed:** `typing.Optional[typing.Union[GetAnnotationsRequestEmbedItem, typing.Sequence[GetAnnotationsRequestEmbedItem]]]` — Sub-resources to include in the response.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory Jobs
<details><summary><code>client.asset_inventory.jobs.<a href="src/hiddenlayer/asset_inventory/jobs/client.py">custom_tags</a>(...) -> CustomTagsJobsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Apply a custom-tag change to every asset matching a filter in one request, instead of calling the single-asset tag endpoints once per asset. The `action` (`PUT` or `DELETE`) is applied to each matched asset exactly as `PUT /asset-inventory/v2/assets/{asset_id}/custom-tags/{tag_name}` or `DELETE /asset-inventory/v2/assets/{asset_id}/custom-tags/{tag_name}` would apply it.
The filter accepts the same criteria as `GET /asset-inventory/v2/assets`, so you can preview exactly which assets a job will touch by running that search first.
The request is processed synchronously: the response is the finished `Job`, always in a terminal state (`COMPLETED` or `FAILED`), with `matched_count`, `succeeded_count`, `failed_count`, and per-asset `failures[]` filled in. A filter that matches no assets returns `COMPLETED` with `matched_count: 0`. Jobs are not stored, so there is no job ID to poll — the response is the only report of the outcome.
A job matches at most 10,000 assets; a filter that would match more is rejected with `422 Unprocessable Entity`. Narrow the filter and retry.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer, AssetFilterV2, AssetFilterV2AssetType, AssetFilterV2AnnotatingService, AttributeCondition
from hiddenlayer.environment import HiddenLayerEnvironment
from hiddenlayer.asset_inventory.jobs import BulkCustomTagJobRequestV2Filter

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.jobs.custom_tags(
    filter=BulkCustomTagJobRequestV2Filter(
        assets=AssetFilterV2(
            asset_type=AssetFilterV2AssetType(
                in_=[
                    "MODEL",
                    "ENDPOINT"
                ],
            ),
            annotating_service=AssetFilterV2AnnotatingService(
                in_=[
                    "discovery"
                ],
            ),
            attributes={
                "provider": AttributeCondition(
                    eq="AWS",
                ),
                "region": AttributeCondition(
                    in_=[
                        "us-east-1",
                        "eu-west-1"
                    ],
                )
            },
        ),
    ),
    action="PUT",
    body={
        "team": "ml-platform",
        "environment": "production",
        "cost-center": "ai-inference",
        "managed-by": "terraform",
        "data-classification": "confidential"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**filter:** `BulkCustomTagJobRequestV2Filter` — Filter criteria identifying the target assets.
    
</dd>
</dl>

<dl>
<dd>

**action:** `BulkCustomTagJobRequestV2Action` — Per-asset operation to perform. `PUT` applies `PUT /asset-inventory/v2/assets/{asset_id}/custom-tags/{tag_name}` to each matched asset; `DELETE` applies `DELETE /asset-inventory/v2/assets/{asset_id}/custom-tags/{tag_name}`.
    
</dd>
</dl>

<dl>
<dd>

**body:** `BulkCustomTagJobRequestV2Body` — Shape depends on `action`. For `PUT`: an object of custom tag name → value pairs to set on every matched asset (upsert semantics). For `DELETE`: an array of custom tag names to remove from every matched asset (tags not present on an asset are silently ignored).
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory Assets Search
<details><summary><code>client.asset_inventory.assets.search.<a href="src/hiddenlayer/asset_inventory/assets/search/client.py">list</a>(...) -> SearchResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.search.list(
    q="q",
    sort="+discovered_at",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Search query string
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of items to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of items to skip before starting to collect the result set
    
</dd>
</dl>

<dl>
<dd>

**bandit_arm_override:** `typing.Optional[int]` — Optional bandit arm to force for this search
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[ListSearchRequestProvider]` — Filter by service provider (providers are OR'ed)
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[ListSearchRequestAccountId]` — Filter by account ID
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[ListSearchRequestRegion]` — Filter by region
    
</dd>
</dl>

<dl>
<dd>

**service:** `typing.Optional[ListSearchRequestService]` — Filter by service (services are OR'ed)
    
</dd>
</dl>

<dl>
<dd>

**asset_type:** `typing.Optional[ListSearchRequestAssetType]` — Filter by asset type
    
</dd>
</dl>

<dl>
<dd>

**is_public:** `typing.Optional[ListSearchRequestIsPublic]` — Filter by public status
    
</dd>
</dl>

<dl>
<dd>

**is_retrievable:** `typing.Optional[ListSearchRequestIsRetrievable]` — Filter by retrievability status
    
</dd>
</dl>

<dl>
<dd>

**hl_resource_type:** `typing.Optional[ListSearchRequestHlResourceType]` — Filter by AI Asset being linked to a HiddenLayer resource
    
</dd>
</dl>

<dl>
<dd>

**policy_status:** `typing.Optional[ListSearchRequestPolicyStatus]` — Filter by policy status
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `typing.Optional[TagNameFilter]` — Filter by tag name regardless of source. Matches across both custom and discovered tags.
    
</dd>
</dl>

<dl>
<dd>

**tag_def:** `typing.Optional[TagDefFilter]` — Filter by tag definition (source + name). The top-level operator (`in` or `all`) governs how all entries across sources are combined. Within each operator, use `custom` and/or `discovered` keys to specify tag names by source.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[TagValueFilter]` — Filter by tag (source + name + value). The top-level operator (`in` or `all`) governs how all entries across sources are combined. Within each operator, use `custom` and/or `discovered` keys to specify tag name/value pairs by source.
    
</dd>
</dl>

<dl>
<dd>

**embed:** `typing.Optional[typing.Union[Embed, typing.Sequence[Embed]]]` — Sub-resources to include in the response
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — allow sorting by listed fields, ascending (+) or descending (-); multiple fields may be comma-separated
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.search.<a href="src/hiddenlayer/asset_inventory/assets/search/client.py">suggestions</a>(...) -> SearchSuggestionsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.search.suggestions(
    q="q",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — Prefix text to get suggestions for
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of suggestions to return
    
</dd>
</dl>

<dl>
<dd>

**bandit_arm_override:** `typing.Optional[int]` — Optional bandit arm to force for suggestions threshold
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[SuggestionsSearchRequestProvider]` — Filter by service provider (providers are OR'ed)
    
</dd>
</dl>

<dl>
<dd>

**account_id:** `typing.Optional[SuggestionsSearchRequestAccountId]` — Filter by account ID
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[SuggestionsSearchRequestRegion]` — Filter by region
    
</dd>
</dl>

<dl>
<dd>

**service:** `typing.Optional[SuggestionsSearchRequestService]` — Filter by service (services are OR'ed)
    
</dd>
</dl>

<dl>
<dd>

**asset_type:** `typing.Optional[SuggestionsSearchRequestAssetType]` — Filter by asset type
    
</dd>
</dl>

<dl>
<dd>

**is_public:** `typing.Optional[SuggestionsSearchRequestIsPublic]` — Filter by public status
    
</dd>
</dl>

<dl>
<dd>

**is_retrievable:** `typing.Optional[SuggestionsSearchRequestIsRetrievable]` — Filter by retrievability status
    
</dd>
</dl>

<dl>
<dd>

**policy_status:** `typing.Optional[SuggestionsSearchRequestPolicyStatus]` — Filter by policy status
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `typing.Optional[TagNameFilter]` — Filter by tag name regardless of source. Matches across both custom and discovered tags.
    
</dd>
</dl>

<dl>
<dd>

**tag_def:** `typing.Optional[TagDefFilter]` — Filter by tag definition (source + name). The top-level operator (`in` or `all`) governs how all entries across sources are combined. Within each operator, use `custom` and/or `discovered` keys to specify tag names by source.
    
</dd>
</dl>

<dl>
<dd>

**tag:** `typing.Optional[TagValueFilter]` — Filter by tag (source + name + value). The top-level operator (`in` or `all`) governs how all entries across sources are combined. Within each operator, use `custom` and/or `discovered` keys to specify tag name/value pairs by source.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## AssetInventory Assets CustomTags
<details><summary><code>client.asset_inventory.assets.custom_tags.<a href="src/hiddenlayer/asset_inventory/assets/custom_tags/client.py">update_v1</a>(...) -> AiAssetInventoryV1TagValue</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Assigns a custom tag to an asset. If the tag already exists on the asset, its value is updated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.custom_tags.update_v1(
    asset_id="asset_id",
    tag_name="tag_name",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The ID of the AI asset
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `str` — The tag name
    
</dd>
</dl>

<dl>
<dd>

**request:** `AiAssetInventoryV1TagValue` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.custom_tags.<a href="src/hiddenlayer/asset_inventory/assets/custom_tags/client.py">delete_v1</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Removes a custom tag assignment from an asset.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.custom_tags.delete_v1(
    asset_id="asset_id",
    tag_name="tag_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The ID of the AI asset
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `str` — The tag name
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.custom_tags.<a href="src/hiddenlayer/asset_inventory/assets/custom_tags/client.py">update</a>(...) -> TagValue</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Assigns a custom tag to an asset. If the tag already exists on the asset, its value is updated.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.custom_tags.update(
    asset_id="asset_id",
    tag_name="tag_name",
    value="value",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The server-assigned UUID of the asset.
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `str` — The custom tag name.
    
</dd>
</dl>

<dl>
<dd>

**request:** `TagValue` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.asset_inventory.assets.custom_tags.<a href="src/hiddenlayer/asset_inventory/assets/custom_tags/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Removes a custom tag assignment from an asset.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.asset_inventory.assets.custom_tags.delete(
    asset_id="asset_id",
    tag_name="tag_name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The server-assigned UUID of the asset.
    
</dd>
</dl>

<dl>
<dd>

**tag_name:** `str` — The custom tag name.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Audit Entries
<details><summary><code>client.audit.entries.<a href="src/hiddenlayer/audit/entries/client.py">list</a>(...) -> ListEntriesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns audit log entries for the tenant, sorted by time with the most recent first. Results can be filtered by time range, actor, role, action, and resource type, or searched by free text.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.audit.entries.list(
    start_time=datetime.datetime.fromisoformat("2025-05-27T00:00:00+00:00"),
    end_time=datetime.datetime.fromisoformat("2025-05-27T23:59:59+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_time:** `typing.Optional[datetime.datetime]` — Filter audit entries by time range
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[datetime.datetime]` — Filter audit entries by time range
    
</dd>
</dl>

<dl>
<dd>

**role:** `typing.Optional[str]` — Filter audit entries by role
    
</dd>
</dl>

<dl>
<dd>

**action:** `typing.Optional[str]` — Filter audit entries by action
    
</dd>
</dl>

<dl>
<dd>

**resource_type:** `typing.Optional[str]` — Filter audit entries by resource_type
    
</dd>
</dl>

<dl>
<dd>

**actor_type:** `typing.Optional[ActorType]` — Filter audit entries by actor_type
    
</dd>
</dl>

<dl>
<dd>

**search:** `typing.Optional[str]` — Search for audit entries by text (searches user, role, action, resource type)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Audit ActivityTypes
<details><summary><code>client.audit.activity_types.<a href="src/hiddenlayer/audit/activity_types/client.py">list</a>() -> ActivityTypeList</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the list of all auditable activity types. Use this to understand what actions are tracked and to build filters when querying audit entries.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.audit.activity_types.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Compliance Projects
<details><summary><code>client.compliance.projects.<a href="src/hiddenlayer/compliance/projects/client.py">list</a>(...) -> ListProjectsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.projects.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[ListProjectsRequestName]` — filter by the name
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Default search parameter for general searching
    
</dd>
</dl>

<dl>
<dd>

**default:** `typing.Optional[str]` — Return only the default project for the querying tenant
    
</dd>
</dl>

<dl>
<dd>

**rule_set_id:** `typing.Optional[ListProjectsRequestRuleSetId]` — filter by rule set ID
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `typing.Optional[ListProjectsRequestPolicyId]` — filter by policy ID
    
</dd>
</dl>

<dl>
<dd>

**policy_pack_id:** `typing.Optional[ListProjectsRequestPolicyPackId]` — filter by policy pack ID
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[Limit]` — Limit the number of items returned
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — allow sorting by name or modified_at, ascending (+) or the default descending (-)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.projects.<a href="src/hiddenlayer/compliance/projects/client.py">create</a>(...) -> ProjectId</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns the new project ID; retrieve the project by ID to read its settings.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.projects.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**project_alias:** `typing.Optional[str]` — Alias to the project ID
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Dict[str, str]]` — Deprecated - use system_annotations to read system-assigned project metadata.
    
</dd>
</dl>

<dl>
<dd>

**system_annotations:** `typing.Optional[typing.Dict[str, str]]` — System-assigned project metadata.
    
</dd>
</dl>

<dl>
<dd>

**assets:** `typing.Optional[typing.List[AssetId]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**modified_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**modified_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rule_set_id:** `typing.Optional[str]` 

Deprecated - use policy_pack_id to assign a project's ruleset and policy.
When creating a project, omitting this  field causes the project to inherit the default project's ruleset unless the project has a selected policy pack (in which case the policy pack takes precedence).
On update, supplying this field with policy_pack_id returns 422. Otherwise, rule_set_id and policy_id replace the stored assignment, and an omitted one keeps its stored value. If the result differs from the stored ruleset and policy, the project's policy pack is removed; if it matches, the pack is kept.
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `typing.Optional[str]` 

Deprecated - use policy_pack_id to assign a project's ruleset and policy.
On creation, omission inherits the default project's policy and returns 422 if no policy is available; a selected policy pack takes precedence over this field.
On update, supplying this field with policy_pack_id returns 422. Otherwise, it is applied with or without rule_set_id, as described for rule_set_id; omission preserves the current policy.
    
</dd>
</dl>

<dl>
<dd>

**policy_pack_id:** `typing.Optional[str]` 

Selecting a policy pack applies its ruleset and policy.
On creation, a selected pack takes precedence over rule_set_id and policy_id. Omission inherits the default project's pack only when rule_set_id and policy_id are also omitted.
On update, an explicit pack ID selects or switches packs and replaces the project's ruleset and policy with the pack's values. Supplying rule_set_id or policy_id alongside it returns 422.
Supplying a rule_set_id or policy_id that differs from the stored value removes the project's pack. The tenant's default project always has a pack: when a change leaves it without one, the built-in Default pack is updated to its ruleset and policy and assigned to it, and projects assigned to the Default pack follow the same change.
Omitting policy_pack_id, rule_set_id, and policy_id preserves the stored assignment.
    
</dd>
</dl>

<dl>
<dd>

**policy_pack:** `typing.Optional[ProjectPolicyPack]` 
    
</dd>
</dl>

<dl>
<dd>

**monitor_mode:** `typing.Optional[bool]` 

Enables detect-only runtime evaluation for this project without blocking or redaction.
On creation, omission sets false; this setting is never inherited from the default project.
On update, omission preserves the stored value; send false explicitly to disable monitor mode.
    
</dd>
</dl>

<dl>
<dd>

**is_editable:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**escalation_details:** `typing.Optional[ProjectDetailsEscalationDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**risk_level:** `typing.Optional[ProjectDetailsRiskLevel]` — Deprecated - this field will be removed. Do not send it, and do not depend on it in responses.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.projects.<a href="src/hiddenlayer/compliance/projects/client.py">get</a>(...) -> GetProjectsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.projects.get(
    id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A project ID or alias in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.projects.<a href="src/hiddenlayer/compliance/projects/client.py">update</a>(...) -> ProjectId</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Updates an existing project and returns its ID; retrieve the project by ID to read its settings. A missing project returns 404.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.projects.update(
    id="00000000-0000-0000-0000-000000000000",
    if_unmodified_since="Sat, 29 Oct 1994 19:43:31 GMT",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A project ID or alias in the request URI
    
</dd>
</dl>

<dl>
<dd>

**if_unmodified_since:** `typing.Optional[str]` 

The "If-Unmodified-Since" header field makes the request method
conditional on the selected representation's last modification date
being earlier than or equal to the date provided in the field-value.
This field accomplishes the same purpose as If-Match for cases where
the user agent does not have an entity-tag for the representation.

https://www.rfc-editor.org/rfc/rfc7232.html#section-3.4
    
</dd>
</dl>

<dl>
<dd>

**project_alias:** `typing.Optional[str]` — Alias to the project ID
    
</dd>
</dl>

<dl>
<dd>

**tags:** `typing.Optional[typing.Dict[str, str]]` — Deprecated - use system_annotations to read system-assigned project metadata.
    
</dd>
</dl>

<dl>
<dd>

**system_annotations:** `typing.Optional[typing.Dict[str, str]]` — System-assigned project metadata.
    
</dd>
</dl>

<dl>
<dd>

**assets:** `typing.Optional[typing.List[AssetId]]` 
    
</dd>
</dl>

<dl>
<dd>

**created_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**created_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**modified_at:** `typing.Optional[datetime.datetime]` 
    
</dd>
</dl>

<dl>
<dd>

**modified_by:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**rule_set_id:** `typing.Optional[str]` 

Deprecated - use policy_pack_id to assign a project's ruleset and policy.
When creating a project, omitting this  field causes the project to inherit the default project's ruleset unless the project has a selected policy pack (in which case the policy pack takes precedence).
On update, supplying this field with policy_pack_id returns 422. Otherwise, rule_set_id and policy_id replace the stored assignment, and an omitted one keeps its stored value. If the result differs from the stored ruleset and policy, the project's policy pack is removed; if it matches, the pack is kept.
    
</dd>
</dl>

<dl>
<dd>

**policy_id:** `typing.Optional[str]` 

Deprecated - use policy_pack_id to assign a project's ruleset and policy.
On creation, omission inherits the default project's policy and returns 422 if no policy is available; a selected policy pack takes precedence over this field.
On update, supplying this field with policy_pack_id returns 422. Otherwise, it is applied with or without rule_set_id, as described for rule_set_id; omission preserves the current policy.
    
</dd>
</dl>

<dl>
<dd>

**policy_pack_id:** `typing.Optional[str]` 

Selecting a policy pack applies its ruleset and policy.
On creation, a selected pack takes precedence over rule_set_id and policy_id. Omission inherits the default project's pack only when rule_set_id and policy_id are also omitted.
On update, an explicit pack ID selects or switches packs and replaces the project's ruleset and policy with the pack's values. Supplying rule_set_id or policy_id alongside it returns 422.
Supplying a rule_set_id or policy_id that differs from the stored value removes the project's pack. The tenant's default project always has a pack: when a change leaves it without one, the built-in Default pack is updated to its ruleset and policy and assigned to it, and projects assigned to the Default pack follow the same change.
Omitting policy_pack_id, rule_set_id, and policy_id preserves the stored assignment.
    
</dd>
</dl>

<dl>
<dd>

**policy_pack:** `typing.Optional[ProjectPolicyPack]` 
    
</dd>
</dl>

<dl>
<dd>

**monitor_mode:** `typing.Optional[bool]` 

Enables detect-only runtime evaluation for this project without blocking or redaction.
On creation, omission sets false; this setting is never inherited from the default project.
On update, omission preserves the stored value; send false explicitly to disable monitor mode.
    
</dd>
</dl>

<dl>
<dd>

**is_editable:** `typing.Optional[bool]` 
    
</dd>
</dl>

<dl>
<dd>

**escalation_details:** `typing.Optional[ProjectDetailsEscalationDetails]` 
    
</dd>
</dl>

<dl>
<dd>

**risk_level:** `typing.Optional[ProjectDetailsRiskLevel]` — Deprecated - this field will be removed. Do not send it, and do not depend on it in responses.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.projects.<a href="src/hiddenlayer/compliance/projects/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.projects.delete(
    id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Compliance RuleSets
<details><summary><code>client.compliance.rule_sets.<a href="src/hiddenlayer/compliance/rule_sets/client.py">list</a>(...) -> ListRuleSetsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.rule_sets.list(
    limit=50,
    page_size=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `typing.Optional[ListRuleSetsRequestName]` — filter by the name
    
</dd>
</dl>

<dl>
<dd>

**q:** `typing.Optional[str]` — Default search parameter for general searching
    
</dd>
</dl>

<dl>
<dd>

**feature:** `typing.Optional[ListRuleSetsRequestFeature]` — Select cursor pagination for this endpoint. Required for cursor pagination while the legacy list response remains available.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[Limit]` — Limit the number of items returned
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Deprecated alias for `limit`; use `limit` instead.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — allow sorting by name, ascending (+) or the default descending (-)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.rule_sets.<a href="src/hiddenlayer/compliance/rule_sets/client.py">create</a>(...) -> GetRuleSetItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.rule_sets.create(
    name="name",
    description="description",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `RuleSetDetails` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.rule_sets.<a href="src/hiddenlayer/compliance/rule_sets/client.py">get</a>(...) -> GetRuleSetItem</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.rule_sets.get(
    id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.rule_sets.<a href="src/hiddenlayer/compliance/rule_sets/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.rule_sets.update(
    id="00000000-0000-0000-0000-000000000000",
    if_unmodified_since="Sat, 29 Oct 1994 19:43:31 GMT",
    name="name",
    description="description",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request:** `RuleSetDetails` 
    
</dd>
</dl>

<dl>
<dd>

**if_unmodified_since:** `typing.Optional[str]` 

The "If-Unmodified-Since" header field makes the request method
conditional on the selected representation's last modification date
being earlier than or equal to the date provided in the field-value.
This field accomplishes the same purpose as If-Match for cases where
the user agent does not have an entity-tag for the representation.

https://www.rfc-editor.org/rfc/rfc7232.html#section-3.4
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.rule_sets.<a href="src/hiddenlayer/compliance/rule_sets/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.rule_sets.delete(
    id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Compliance RuleSets Settings
<details><summary><code>client.compliance.rule_sets.settings.<a href="src/hiddenlayer/compliance/rule_sets/settings/client.py">list</a>(...) -> ListSettingsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.rule_sets.settings.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**category:** `typing.Optional[ListSettingsRequestCategory]` — filter by settings category name as a query parameter
    
</dd>
</dl>

<dl>
<dd>

**overlay:** `typing.Optional[str]` 

specify that settings response is enriched with a JSON schema that details the
constraints that apply for the entire object in the settings property
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.rule_sets.settings.<a href="src/hiddenlayer/compliance/rule_sets/settings/client.py">create</a>(...) -> SettingsId</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.rule_sets.settings.create(
    id="00000000-0000-0000-0000-000000000000",
    settings_id="settings_id",
    settings={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**settings_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**settings:** `typing.Dict[str, typing.Any]` — object as described by the schema property, if not provided, free form object
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.rule_sets.settings.<a href="src/hiddenlayer/compliance/rule_sets/settings/client.py">get</a>(...) -> SettingsDetailsWithSchema</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.rule_sets.settings.get(
    id="00000000-0000-0000-0000-000000000000",
    settings_id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**settings_id:** `str` — A settings ID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**overlay:** `typing.Optional[str]` 

specify that settings response is enriched with a JSON schema that details the
constraints that apply for the entire object in the settings property
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.rule_sets.settings.<a href="src/hiddenlayer/compliance/rule_sets/settings/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.rule_sets.settings.update(
    id="00000000-0000-0000-0000-000000000000",
    settings_id="00000000-0000-0000-0000-000000000000",
    if_match="\"7da7a728-f910-11e6-942a-68f728c1ba70\"",
    settings={
        "key": "value"
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**settings_id:** `str` — A settings ID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request:** `Settings` 
    
</dd>
</dl>

<dl>
<dd>

**if_match:** `typing.Optional[str]` 

The "If-Match" header field makes the request method conditional on
the recipient origin server either having at least one current
representation of the target resource, when the field-value is "*",
or having a current representation of the target resource that has an
entity-tag matching a member of the list of entity-tags provided in
the field-value.

https://www.rfc-editor.org/rfc/rfc7232.html#section-3.1
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.compliance.rule_sets.settings.<a href="src/hiddenlayer/compliance/rule_sets/settings/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.compliance.rule_sets.settings.delete(
    id="00000000-0000-0000-0000-000000000000",
    settings_id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — A UUID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**settings_id:** `str` — A settings ID in the request URI
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Evaluations RedTeam
<details><summary><code>client.evaluations.red_team.<a href="src/hiddenlayer/evaluations/red_team/client.py">list</a>(...) -> RedTeamListResultsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

List completed red team workflow results with filtering and bidirectional pagination.

Results are ordered by completed_at DESC (newest first).
Returns metadata only - use GET /evaluations/v1/red-team/{workflow_id} for full payload.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**target_model:** `typing.Optional[str]` — Filter by target model
    
</dd>
</dl>

<dl>
<dd>

**workflow_type:** `typing.Optional[str]` — Filter by workflow type
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[str]` — Filter by workflow status
    
</dd>
</dl>

<dl>
<dd>

**start_time_from:** `typing.Optional[datetime.datetime]` — Filter for results started after this time
    
</dd>
</dl>

<dl>
<dd>

**start_time_to:** `typing.Optional[datetime.datetime]` — Filter for results started before this time
    
</dd>
</dl>

<dl>
<dd>

**project_id:** `typing.Optional[ListRedTeamRequestProjectId]` 

Filter to evaluations started under any of the given HiddenLayer
projects. Evaluations without a project never match.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Deprecated alias for `limit`. Use `limit` instead. Will be removed after SDK regen.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination cursor from previous response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluations.red_team.<a href="src/hiddenlayer/evaluations/red_team/client.py">create</a>(...) -> StartWorkflowResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Start a new red team client workflow.
Auto-triggers planning phase. Client should then poll /next-action.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.create(
    name="name",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**name:** `str` — Name for this evaluation
    
</dd>
</dl>

<dl>
<dd>

**config_id:** `typing.Optional[str]` 

Optional preset config (see /evaluations/v1/red-team/configs) to seed the
workflow settings. Any field also present in this body overrides the
corresponding value from the config.
    
</dd>
</dl>

<dl>
<dd>

**target_model:** `typing.Optional[str]` 

Target model identifier. Freeform for the client-driven workflow: the
client owns and drives its own target, so this is NOT validated against
the servable-model catalog. (The simulated start and config presets do
validate against the catalog.)
    
</dd>
</dl>

<dl>
<dd>

**target_system_prompt:** `typing.Optional[str]` — System prompt for the target
    
</dd>
</dl>

<dl>
<dd>

**objective_ids:** `typing.Optional[typing.List[str]]` — Objective IDs to evaluate
    
</dd>
</dl>

<dl>
<dd>

**severity_mapping:** `typing.Optional[SeverityMapping]` 
    
</dd>
</dl>

<dl>
<dd>

**execution_strategy_type:** `typing.Optional[ClientRedTeamBodyExecutionStrategyType]` — Execution strategy type
    
</dd>
</dl>

<dl>
<dd>

**n_random_techniques:** `typing.Optional[int]` — Number of random techniques to use
    
</dd>
</dl>

<dl>
<dd>

**max_parallel_techniques:** `typing.Optional[int]` — Maximum parallel techniques
    
</dd>
</dl>

<dl>
<dd>

**max_turns:** `typing.Optional[int]` — Maximum conversation turns
    
</dd>
</dl>

<dl>
<dd>

**attacker_max_generation_attempts:** `typing.Optional[int]` 

Internal override; service default applies if omitted. Maximum number of
generation attempts for the attacker model per turn.
    
</dd>
</dl>

<dl>
<dd>

**refusal_judge_model:** `typing.Optional[str]` — Internal override; service default applies if omitted.
    
</dd>
</dl>

<dl>
<dd>

**objective_judge_model:** `typing.Optional[str]` — Internal override; service default applies if omitted.
    
</dd>
</dl>

<dl>
<dd>

**evaluation_report_model:** `typing.Optional[str]` — Internal override; service default applies if omitted.
    
</dd>
</dl>

<dl>
<dd>

**attacker_model:** `typing.Optional[str]` — Internal override; service default applies if omitted.
    
</dd>
</dl>

<dl>
<dd>

**hl_project_id:** `typing.Optional[str]` — HiddenLayer project UUID or alias
    
</dd>
</dl>

<dl>
<dd>

**prompt_set_id:** `typing.Optional[str]` — Prompt set UUID (built-in catalog or tenant DB)
    
</dd>
</dl>

<dl>
<dd>

**sessions_per_technique:** `typing.Optional[int]` — Number of sessions per technique
    
</dd>
</dl>

<dl>
<dd>

**attacker_guidance:** `typing.Optional[str]` 

Optional intent-only natural-language text the operator supplies to
focus the attacker LLM within the configured APE objectives. Example:
"try to get the model to recommend candy with nuts to a user who's
allergic to nuts."

Sanitized server-side: input is NFKC-normalized, trimmed, and
checked against a strict character whitelist (ASCII letters, digits,
spaces/newlines/tabs, and sentence-level punctuation `. , ? ! ' " - : ; ( )`).
Inputs containing XML/JSON/code/control/markdown characters are
rejected with 422.

No-op for the `STATIC_PROMPT_SET` execution strategy.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluations.red_team.<a href="src/hiddenlayer/evaluations/red_team/client.py">retrieve_status</a>(...) -> WorkflowStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Get current status of a red team workflow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.retrieve_status(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The workflow identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluations.red_team.<a href="src/hiddenlayer/evaluations/red_team/client.py">retrieve_next_action</a>(...) -> NextActionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Poll for next action - CLIENT'S MAIN POLLING ENDPOINT.

This endpoint is designed to be polled repeatedly by the client.
Returns immediately with current state:
- If attack ready: Returns attack_task with prompt
- If processing: Returns processing=true (client continues polling)
- If complete: Returns action_type=complete
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.retrieve_next_action(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The workflow identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluations.red_team.<a href="src/hiddenlayer/evaluations/red_team/client.py">submit_target_response</a>(...) -> SubmitTargetResponseResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Submit target's response.

This triggers the ProcessTargetResponseWorkflow child workflow
for the specified session. Returns immediately.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.submit_target_response(
    workflow_id="workflow_id",
    session_id="session_id",
    target_response="target_response",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The workflow identifier
    
</dd>
</dl>

<dl>
<dd>

**session_id:** `str` — Session identifier
    
</dd>
</dl>

<dl>
<dd>

**target_response:** `str` — Target's response text
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluations.red_team.<a href="src/hiddenlayer/evaluations/red_team/client.py">retrieve_evaluation_results</a>(...) -> WorkflowResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Get the complete result of a red team workflow.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.retrieve_evaluation_results(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The workflow identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluations.red_team.<a href="src/hiddenlayer/evaluations/red_team/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Delete a red team workflow result from storage.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.delete(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The workflow identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluations.red_team.<a href="src/hiddenlayer/evaluations/red_team/client.py">terminate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Terminate a running workflow job.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.terminate(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The workflow identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Evaluations RedTeam RuleSuggestions
<details><summary><code>client.evaluations.red_team.rule_suggestions.<a href="src/hiddenlayer/evaluations/red_team/rule_suggestions/client.py">list</a>(...) -> RuleSuggestionListResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

List rule suggestion runs generated for a red team evaluation, newest first.

Each run is independent - triggering a new run does not replace or affect prior runs.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.rule_suggestions.list(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The source red team evaluation's workflow identifier
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Pagination cursor from previous response
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluations.red_team.rule_suggestions.<a href="src/hiddenlayer/evaluations/red_team/rule_suggestions/client.py">create</a>(...) -> StartRuleSuggestionResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Start a new rule suggestion run for a completed red team evaluation. Analyzes the
evaluation's successful attacks and generates a detection rule suggestion that can be
reviewed and added to a project's runtime security policy.

Callable multiple times for the same evaluation; each call starts an independent run.
The response's `suggestion_id` identifies the new run - use it in the status, result,
and list endpoints (the `{workflow_id}` path segment continues to identify the source
red team evaluation). Client should poll /status, then fetch the full result once
complete.

An empty JSON object `{}` is the minimal valid request body.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.rule_suggestions.create(
    workflow_id="workflow_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The source red team evaluation's workflow identifier
    
</dd>
</dl>

<dl>
<dd>

**name:** `typing.Optional[str]` — Optional name for this rule suggestion run. When omitted, the server derives one from the source evaluation (e.g. "Rule suggestions for {evaluation name}").
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluations.red_team.rule_suggestions.<a href="src/hiddenlayer/evaluations/red_team/rule_suggestions/client.py">status</a>(...) -> RuleSuggestionStatusResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Get current status of a rule suggestion run (polling endpoint).
Returns immediately with current state.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.rule_suggestions.status(
    workflow_id="workflow_id",
    suggestion_id="suggestion_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The source red team evaluation's workflow identifier
    
</dd>
</dl>

<dl>
<dd>

**suggestion_id:** `str` — The rule suggestion run identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.evaluations.red_team.rule_suggestions.<a href="src/hiddenlayer/evaluations/red_team/rule_suggestions/client.py">get</a>(...) -> RuleSuggestionResultResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Get the complete result of a rule suggestion run, including any generated rules.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.evaluations.red_team.rule_suggestions.get(
    workflow_id="workflow_id",
    suggestion_id="suggestion_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**workflow_id:** `str` — The source red team evaluation's workflow identifier
    
</dd>
</dl>

<dl>
<dd>

**suggestion_id:** `str` — The rule suggestion run identifier
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Governance Evaluations
<details><summary><code>client.governance.evaluations.<a href="src/hiddenlayer/governance/evaluations/client.py">list</a>(...) -> BulkEvaluationResults</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the governance evaluation results for multiple artifacts by their unique identifiers.
Each artifact will have a corresponding status to indicate whether evaluation results exist for that ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.evaluations.list(
    artifact_ids=[
        "artifact_ids"
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artifact_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — list of unique artifact identifiers to retrieve evaluation results for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.evaluations.<a href="src/hiddenlayer/governance/evaluations/client.py">get</a>(...) -> EvaluationResult</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve the governance evaluation results for a specific artifact by its unique identifier.
The response includes whether the artifact is compliant with the defined policies and an explanation of the evaluation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.evaluations.get(
    artifact_id="artifact_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**artifact_id:** `str` — Unique identifier for the artifact to retrieve evaluation results for
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Governance Licenses
<details><summary><code>client.governance.licenses.<a href="src/hiddenlayer/governance/licenses/client.py">list</a>() -> ListLicensesResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns every license value a `license` condition accepts, including `unknown` and `custom`
alongside the named licenses. Rules store each license's `id`; `name` is for display only.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.licenses.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Governance RuleSets
<details><summary><code>client.governance.rule_sets.<a href="src/hiddenlayer/governance/rule_sets/client.py">list</a>(...) -> ListRuleSetsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a list of rule sets that can be used to evaluate artifacts against governance policies.
This endpoint supports pagination with the `page_size` and `cursor` parameters.
Rule sets are ordered by their creation time, with the oldest rule sets listed first.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.rule_sets.list(
    page_size=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**include_disabled:** `typing.Optional[bool]` — When `true`, each returned rule set's `rules` includes disabled rules alongside enabled ones. Defaults to `false`, which returns only enabled rules.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.rule_sets.<a href="src/hiddenlayer/governance/rule_sets/client.py">create</a>(...) -> RuleSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a new rule set for evaluating artifacts against governance policies.
Rule sets can contain multiple rules, each with a set of conditions to evaluate.
This endpoint allows you to create a new set of rules with their compliance criteria.
Order matters; later rules may override earlier ones. Each rule's `is_disabled` value is
honored as submitted, so a rule set can be created with some of its rules already disabled.

When `replace_active_policy` is `true`, creating a rule set also disables whichever
custom rule set is currently enabled for the tenant, so the newly created rule set
becomes the tenant's sole active custom policy. The default rule set is never disabled
by this operation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer, Rule, Condition
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.rule_sets.create(
    display_name="display_name",
    rules=[
        Rule(
            is_compliant_when_conditions_met=True,
            conditions=[
                Condition(
                    field="field",
                    condition_operator="equals",
                )
            ],
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `RuleSet` 
    
</dd>
</dl>

<dl>
<dd>

**replace_active_policy:** `typing.Optional[bool]` — When `true`, disables the tenant's currently active custom rule set as part of creating this one, so this rule set becomes the tenant's sole active custom policy. Defaults to `false`, which leaves any currently active custom rule set untouched.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.rule_sets.<a href="src/hiddenlayer/governance/rule_sets/client.py">get</a>(...) -> RuleSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve a specific rule set by its unique identifier. This endpoint returns the details of the rule set, including its rules and compliance criteria.
The response includes the rule set's ID, display name, and the list of rules it contains.
If the rule set does not exist, a 404 Not Found error is returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.rule_sets.get(
    rule_set_id="rule_set_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule_set_id:** `str` — Unique identifier for the rule set to retrieve
    
</dd>
</dl>

<dl>
<dd>

**include_disabled:** `typing.Optional[bool]` — When `true`, the returned rule set's `rules` includes disabled rules alongside enabled ones. Defaults to `false`, which returns only enabled rules.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.rule_sets.<a href="src/hiddenlayer/governance/rule_sets/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a rule set by its unique identifier. This operation disables the rule set so it cannot be applied to artifacts during evaluation.
If the rule set does not exist, a 404 Not Found error is returned.
This operation is irreversible; once deleted, the rule set cannot be recovered.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.rule_sets.delete(
    rule_set_id="rule_set_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule_set_id:** `str` — Unique identifier for the rule set to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Governance PolicyPacks
<details><summary><code>client.governance.policy_packs.<a href="src/hiddenlayer/governance/policy_packs/client.py">list</a>(...) -> ListPolicyPacksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Returns pack summaries without `settings` or `detection_rules`. To read those, get the policy pack by ID.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.policy_packs.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `typing.Optional[str]` — Search policy pack name and description
    
</dd>
</dl>

<dl>
<dd>

**type:** `typing.Optional[ListPolicyPacksRequestType]` — Filter policy packs by type
    
</dd>
</dl>

<dl>
<dd>

**is_enabled:** `typing.Optional[ListPolicyPacksRequestIsEnabled]` — Filter policy packs by whether at least one project in the tenant uses the pack
    
</dd>
</dl>

<dl>
<dd>

**detection_rule_id:** `typing.Optional[ListPolicyPacksRequestDetectionRuleId]` — Filter to policy definitions or policy packs that reference detection rule(s)
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[Limit]` — Limit the number of items returned
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort by name, ascending (+) or descending (-)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.policy_packs.<a href="src/hiddenlayer/governance/policy_packs/client.py">create</a>(...) -> PolicyPack</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

The pack must assign at least one detection rule through `rule_pack_ids` or `individual_rules`; otherwise returns 422.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer, PolicyPackWriteRequestSettingsItem
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.policy_packs.create(
    name="name",
    settings=[
        PolicyPackWriteRequestSettingsItem(
            settings_id="settings_id",
            settings={
                "key": "value"
            },
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request:** `PolicyPackWriteRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.policy_packs.<a href="src/hiddenlayer/governance/policy_packs/client.py">recommendations</a>(...) -> PolicyPackRecommendation</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

To apply the recommendation, set the returned `id` as the project's `policy_pack_id`.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.policy_packs.recommendations(
    application_type="GENERAL",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**application_type:** `PolicyPackApplicationType` 
    
</dd>
</dl>

<dl>
<dd>

**exposure:** `typing.Optional[PolicyPackApplicationExposure]` — Needed unless `application_type` is CODING_HARNESS, which ignores it; omitting it when needed returns 422. An empty string is the same as an omitted value.
    
</dd>
</dl>

<dl>
<dd>

**deployment_stage:** `typing.Optional[PolicyPackDeploymentStage]` — Needed only when `application_type` is GENERAL and `exposure` is INTERNET_FACING, and ignored otherwise; omitting it when needed returns 422. An empty string is the same as an omitted value.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.policy_packs.<a href="src/hiddenlayer/governance/policy_packs/client.py">get</a>(...) -> PolicyPack</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.policy_packs.get(
    policy_pack_id="policy_pack_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**policy_pack_id:** `str` — Unique identifier for the policy pack
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.policy_packs.<a href="src/hiddenlayer/governance/policy_packs/client.py">update</a>(...) -> PolicyPack</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Replaces the entire pack, including `settings`; omitted optional fields are cleared.
- **403** when the pack is HiddenLayer-authored; only custom packs can be modified.
- **422** when the pack would assign no detection rules.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer, PolicyPackWriteRequestSettingsItem
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.policy_packs.update(
    policy_pack_id="policy_pack_id",
    name="name",
    settings=[
        PolicyPackWriteRequestSettingsItem(
            settings_id="settings_id",
            settings={
                "key": "value"
            },
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**policy_pack_id:** `str` — Unique identifier for the policy pack
    
</dd>
</dl>

<dl>
<dd>

**request:** `PolicyPackWriteRequest` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.policy_packs.<a href="src/hiddenlayer/governance/policy_packs/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Projects using the pack are moved to the pack assigned to the tenant's default project. The pack's policy, ruleset, and ruleset settings are also deleted unless another project or pack still references them.
Returns 403 when the pack is HiddenLayer-authored; only custom packs can be deleted.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.policy_packs.delete(
    policy_pack_id="policy_pack_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**policy_pack_id:** `str` — Unique identifier for the policy pack
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Governance RulePacks
<details><summary><code>client.governance.rule_packs.<a href="src/hiddenlayer/governance/rule_packs/client.py">list</a>(...) -> ListRulePacksResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.rule_packs.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**type:** `typing.Optional[ListRulePacksRequestType]` — Filter rule packs by type
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[Limit]` — Limit the number of items returned
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — Sort by name, ascending (+) or descending (-)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Governance RuleSets Rules
<details><summary><code>client.governance.rule_sets.rules.<a href="src/hiddenlayer/governance/rule_sets/rules/client.py">create</a>(...) -> RuleSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Add a new rule to an existing rule set. This endpoint allows you to define a rule with its compliance criteria and conditions.
The new rule will be appended to the existing rules in the specified rule set.
If the rule set does not exist, a 404 Not Found error is returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer, Condition
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.rule_sets.rules.create(
    rule_set_id="rule_set_id",
    is_compliant_when_conditions_met=True,
    conditions=[
        Condition(
            field="field",
            condition_operator="equals",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule_set_id:** `str` — Unique identifier for the rule set to append the rule to
    
</dd>
</dl>

<dl>
<dd>

**request:** `Rule` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.rule_sets.rules.<a href="src/hiddenlayer/governance/rule_sets/rules/client.py">update</a>(...) -> RuleSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Replace an existing rule in a rule set with a new definition. This endpoint allows you to update the compliance criteria and conditions of a rule, preserving
 the rule's order in the rule set. If the rule set or the rule does not exist, a 404 Not Found error is returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer, Condition
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.rule_sets.rules.update(
    rule_set_id="rule_set_id",
    rule_id="rule_id",
    is_compliant_when_conditions_met=True,
    conditions=[
        Condition(
            field="field",
            condition_operator="equals",
        )
    ],
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule_set_id:** `str` — Unique identifier for the rule set to which the rule belongs
    
</dd>
</dl>

<dl>
<dd>

**rule_id:** `str` — Unique identifier for the rule to modify/replace
    
</dd>
</dl>

<dl>
<dd>

**request:** `Rule` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.governance.rule_sets.rules.<a href="src/hiddenlayer/governance/rule_sets/rules/client.py">delete</a>(...) -> RuleSet</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Disable a rule in a rule set. This endpoint allows you to remove a rule. It will no longer affect artifact evaluations.
If the rule set or the rule does not exist, a 404 Not Found error is returned.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.governance.rule_sets.rules.delete(
    rule_set_id="rule_set_id",
    rule_id="rule_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**rule_set_id:** `str` — Unique identifier for the rule set to which the rule belongs
    
</dd>
</dl>

<dl>
<dd>

**rule_id:** `str` — Unique identifier for the rule to disable/remove
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Integrations Assets
<details><summary><code>client.integrations.assets.<a href="src/hiddenlayer/integrations/assets/client.py">scans</a>(...) -> AssetScanTriggerResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Triggers an on-demand retrieval and scan workflow for a discovered AI asset. This endpoint validates the asset exists and has a matching integration, then sends a message to initiate the asset retrieval and scanning process.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.integrations.assets.scans(
    asset_id="asset_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**asset_id:** `str` — The ID of the AI asset to scan
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Metrics TimeseriesInferences
<details><summary><code>client.metrics.timeseries_inferences.<a href="src/hiddenlayer/metrics/timeseries_inferences/client.py">list_v2</a>(...) -> InferenceTimeseriesResponseV2</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.metrics.timeseries_inferences.list_v2(
    start_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
    end_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_timestamp:** `datetime.datetime` 

The point in time to start the time series. The specified time must be 90 days or less from the current time.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `typing.Optional[datetime.datetime]` 

The point in time to end the time series. If not provided, the current time is used.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — Filters results to only inferences that are associated with the specified requester ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metrics.timeseries_inferences.<a href="src/hiddenlayer/metrics/timeseries_inferences/client.py">list</a>(...) -> InferenceTimeseriesResponseV3</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.metrics.timeseries_inferences.list(
    start_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
    end_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_timestamp:** `datetime.datetime` 

The point in time to start the time series. The specified time must be 90 days or less from the current time.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `typing.Optional[datetime.datetime]` 

The point in time to end the time series. If not provided, the current time is used.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — Filters results to only inferences that are associated with the specified requester ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Metrics TimeseriesIncidents
<details><summary><code>client.metrics.timeseries_incidents.<a href="src/hiddenlayer/metrics/timeseries_incidents/client.py">list_v2</a>(...) -> IncidentTimeseriesResponseV2</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.metrics.timeseries_incidents.list_v2(
    start_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
    end_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_timestamp:** `datetime.datetime` 

The point in time to start the time series. The specified time must be 90 days or less from the current time.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `typing.Optional[datetime.datetime]` 

The point in time to end the time series. If not provided, the current time is used.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — Filters results to only inferences that are associated with the specified requester ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metrics.timeseries_incidents.<a href="src/hiddenlayer/metrics/timeseries_incidents/client.py">list</a>(...) -> IncidentTimeseriesResponseV3</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.metrics.timeseries_incidents.list(
    start_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
    end_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_timestamp:** `datetime.datetime` 

The point in time to start the time series. The specified time must be 90 days or less from the current time.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `typing.Optional[datetime.datetime]` 

The point in time to end the time series. If not provided, the current time is used.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — Filters results to only inferences that are associated with the specified requester ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Metrics TimeseriesConvictions
<details><summary><code>client.metrics.timeseries_convictions.<a href="src/hiddenlayer/metrics/timeseries_convictions/client.py">list_v2</a>(...) -> ConvictionTimeseriesResponseV2</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.metrics.timeseries_convictions.list_v2(
    start_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
    end_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_timestamp:** `datetime.datetime` 

The point in time to start the time series. The specified time must be 90 days or less from the current time.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `typing.Optional[datetime.datetime]` 

The point in time to end the time series. If not provided, the current time is used.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — Filters results to only inferences that are associated with the specified requester ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metrics.timeseries_convictions.<a href="src/hiddenlayer/metrics/timeseries_convictions/client.py">list</a>(...) -> ConvictionTimeseriesResponseV3</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.metrics.timeseries_convictions.list(
    start_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
    end_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_timestamp:** `datetime.datetime` 

The point in time to start the time series. The specified time must be 90 days or less from the current time.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `typing.Optional[datetime.datetime]` 

The point in time to end the time series. If not provided, the current time is used.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — Filters results to only inferences that are associated with the specified requester ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Metrics TimeseriesScans
<details><summary><code>client.metrics.timeseries_scans.<a href="src/hiddenlayer/metrics/timeseries_scans/client.py">list_v2</a>(...) -> ScanTimeseriesResponseV2</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.metrics.timeseries_scans.list_v2(
    start_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
    end_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_timestamp:** `datetime.datetime` 

The point in time to start the time series. The specified time must be 90 days or less from the current time.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `typing.Optional[datetime.datetime]` 

The point in time to end the time series. If not provided, the current time is used.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — Filters results to only inferences that are associated with the specified requester ID.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.metrics.timeseries_scans.<a href="src/hiddenlayer/metrics/timeseries_scans/client.py">list</a>(...) -> ScanTimeseriesResponseV3</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.metrics.timeseries_scans.list(
    start_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
    end_timestamp=datetime.datetime.fromisoformat("2024-01-01T00:00:00+00:00"),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**start_timestamp:** `datetime.datetime` 

The point in time to start the time series. The specified time must be 90 days or less from the current time.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**end_timestamp:** `typing.Optional[datetime.datetime]` 

The point in time to end the time series. If not provided, the current time is used.

[ISO-8601](https://www.w3.org/TR/NOTE-datetime) formatted string.
    
</dd>
</dl>

<dl>
<dd>

**requester_id:** `typing.Optional[str]` — Filters results to only inferences that are associated with the specified requester ID.
    
</dd>
</dl>

<dl>
<dd>

**bin_size:** `typing.Optional[ListTimeseriesScansRequestBinSize]` — Controls the granularity of the time series aggregation. If not provided, the bin size is determined using the date range.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Mitre Atlas Tactics
<details><summary><code>client.mitre.atlas.tactics.<a href="src/hiddenlayer/mitre/atlas/tactics/client.py">get</a>(...) -> MitreAtlasTacticV1</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.mitre.atlas.tactics.get(
    tactic_id="AML.TA0001",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**tactic_id:** `str` — MITRE Atlas Tactic ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Mitre Atlas Techniques
<details><summary><code>client.mitre.atlas.techniques.<a href="src/hiddenlayer/mitre/atlas/techniques/client.py">get</a>(...) -> GetTechniquesResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.mitre.atlas.techniques.get(
    technique_id="AML.T0043",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**technique_id:** `str` — MITRE Atlas (Sub)Technique ID
    
</dd>
</dl>

<dl>
<dd>

**include_sub_techniques:** `typing.Optional[bool]` — Include sub-techniques
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ModelIntel File
<details><summary><code>client.model_intel.file.<a href="src/hiddenlayer/model_intel/file/client.py">get</a>(...) -> GetFileResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve detailed file information including all associated instances, repositories, and metadata
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.model_intel.file.get(
    sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
    page_size=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sha256:** `str` — SHA256 hash of the file (64 hexadecimal characters)
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.model_intel.file.<a href="src/hiddenlayer/model_intel/file/client.py">metadata</a>(...) -> File</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Retrieve file information such as filetype, file size in bytes, and MIME type
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.model_intel.file.metadata(
    sha256="e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**sha256:** `str` — SHA256 hash of the file (64 hexadecimal characters)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Models Cards
<details><summary><code>client.models.cards.<a href="src/hiddenlayer/models/cards/client.py">list_v3</a>(...) -> ModelCardV3QueryResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.cards.list_v3(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_name:** `typing.Optional[ListV3CardsRequestModelName]` — substring match on model name
    
</dd>
</dl>

<dl>
<dd>

**model_created:** `typing.Optional[ListV3CardsRequestModelCreated]` — match on models created between dates
    
</dd>
</dl>

<dl>
<dd>

**aidr_severity:** `typing.Optional[typing.Union[ListV3CardsRequestAidrSeverityItem, typing.Sequence[ListV3CardsRequestAidrSeverityItem]]]` — Deprecated - use ModelCardAIDRThreatLevel(aidr_threat_level) instead
    
</dd>
</dl>

<dl>
<dd>

**aidr_threat_level:** `typing.Optional[typing.Union[ListV3CardsRequestAidrThreatLevelItem, typing.Sequence[ListV3CardsRequestAidrThreatLevelItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**aidr_status:** `typing.Optional[AidrStatus]` — filter by aidr enabled
    
</dd>
</dl>

<dl>
<dd>

**modscan_severity:** `typing.Optional[typing.Union[ModelCardScanSafeUnsafe, typing.Sequence[ModelCardScanSafeUnsafe]]]` 
    
</dd>
</dl>

<dl>
<dd>

**modscan_status:** `typing.Optional[AidrStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[ListV3CardsRequestSource]` — substring and full match on model source
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[typing.Union[ListV3CardsRequestProviderItem, typing.Sequence[ListV3CardsRequestProviderItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[Limit]` — Limit the number of items returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Begin returning the results from this offset
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — allow sorting by model name or created at timestamp, ascending (+) or the default descending (-)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.cards.<a href="src/hiddenlayer/models/cards/client.py">list</a>(...) -> ModelCardV4QueryResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Deprecated in favor of `GET /asset-inventory/v2/assets`
(`asset_type[in]=MODEL`), which returns the same model-card data —
scan status/timing and findings from the `supply-chain` annotation —
alongside the rest of an asset's data, with matching filters
(`model_id[eq]`, `scan_started_at[gt/gte/lt/lte]`) and sorts
(`model_name`, `scan_started_at`).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.cards.list(
    limit=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_name:** `typing.Optional[ListCardsRequestModelName]` — substring match on model name
    
</dd>
</dl>

<dl>
<dd>

**model_created:** `typing.Optional[ListCardsRequestModelCreated]` — match on models created between dates
    
</dd>
</dl>

<dl>
<dd>

**aidr_severity:** `typing.Optional[typing.Union[ListCardsRequestAidrSeverityItem, typing.Sequence[ListCardsRequestAidrSeverityItem]]]` — Deprecated - use ModelCardAIDRThreatLevel(aidr_threat_level) instead
    
</dd>
</dl>

<dl>
<dd>

**aidr_status:** `typing.Optional[AidrStatus]` — filter by aidr enabled
    
</dd>
</dl>

<dl>
<dd>

**modscan_severity:** `typing.Optional[typing.Union[ListCardsRequestModscanSeverityItem, typing.Sequence[ListCardsRequestModscanSeverityItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**policy_status:** `typing.Optional[typing.Union[PolicyStatus, typing.Sequence[PolicyStatus]]]` 
    
</dd>
</dl>

<dl>
<dd>

**modscan_status:** `typing.Optional[AidrStatus]` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[ListCardsRequestSource]` — substring and full match on model source
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[typing.Union[ListCardsRequestProviderItem, typing.Sequence[ListCardsRequestProviderItem]]]` 
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[Limit]` — Limit the number of items returned
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Begin returning the results from this offset
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — allow sorting by model name or created at timestamp, ascending (+) or the default descending (-)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.cards.<a href="src/hiddenlayer/models/cards/client.py">suggestions</a>(...) -> SuggestionsCardsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.cards.suggestions(
    q="tes",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**q:** `str` — The prefix from which to suggest completions
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — The number of suggestions to return
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Models PolicyCompliance
<details><summary><code>client.models.policy_compliance.<a href="src/hiddenlayer/models/policy_compliance/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Override the policy compliance status for a model. Send {"compliant": true} to mark as compliant, or {"compliant": false} to mark as noncompliant.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.policy_compliance.update(
    model_id="model_id",
    compliant=True,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**compliant:** `bool` — Set to true to mark the model as compliant, or false to mark it as noncompliant. This overrides the policy-derived status.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.policy_compliance.<a href="src/hiddenlayer/models/policy_compliance/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Remove the manual policy compliance override for a model, reverting to the policy-derived compliance status.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.policy_compliance.delete(
    model_id="model_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Models Versions Location
<details><summary><code>client.models.versions.location.<a href="src/hiddenlayer/models/versions/location/client.py">internal</a>(...) -> InternalLocationResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.versions.location.internal(
    version_id="version_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**version_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Models Versions Locations
<details><summary><code>client.models.versions.locations.<a href="src/hiddenlayer/models/versions/locations/client.py">get</a>(...) -> GetLocationsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.versions.locations.get(
    version_id="version_id",
    key="key",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**version_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.models.versions.locations.<a href="src/hiddenlayer/models/versions/locations/client.py">update</a>(...) -> UpdateLocationsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.models.versions.locations.update(
    version_id="version_id",
    key="key",
    request="string",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**version_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**key:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## ScanIndices Submission
<details><summary><code>client.scan_indices.submission.<a href="src/hiddenlayer/scan_indices/submission/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
from hiddenlayer.scan_indices.submission import ScanSubmissionSource, ScanSubmissionSourceSaas

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scan_indices.submission.create(
    scanner_type="hl_model_scanner",
    source=ScanSubmissionSource(
        saas=ScanSubmissionSourceSaas(
            requester_id="someone@hiddenlayer.com",
        ),
    ),
    scan_result={
        "file_results": [{"status": "done", "details": {"sha256": "fae6d75cb56ba5d9bf898b5b49a83d635668cf726f0a1b25cf7dbb1b299101d6"}}]
    },
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scanner_type:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**source:** `ScanSubmissionSource` 
    
</dd>
</dl>

<dl>
<dd>

**scan_result:** `typing.Dict[str, typing.Any]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scans Jobs
<details><summary><code>client.scans.jobs.<a href="src/hiddenlayer/scans/jobs/client.py">request</a>(...) -> ScanJob</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer, ScanJobInventory
from hiddenlayer.environment import HiddenLayerEnvironment
from hiddenlayer.scans.jobs import ScanJobRequestAccess

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.jobs.request(
    inventory=ScanJobInventory(
        model_name="some-model",
        model_version="",
        requesting_entity="some-user@example.com",
    ),
    access=ScanJobRequestAccess(
        source="HUGGING_FACE",
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**inventory:** `ScanJobInventory` 
    
</dd>
</dl>

<dl>
<dd>

**access:** `ScanJobRequestAccess` — Access method for the location of files associated with the scan
    
</dd>
</dl>

<dl>
<dd>

**scan_id:** `typing.Optional[str]` — unique identifier for the scan
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[Status]` — Status of the scan
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scans.jobs.<a href="src/hiddenlayer/scans/jobs/client.py">retrieve</a>(...) -> ScanReportOfRecordV3</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.jobs.retrieve(
    scan_id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scan_id:** `str` — A Model Scan ID
    
</dd>
</dl>

<dl>
<dd>

**has_detections:** `typing.Optional[bool]` — Filter file_results to only those that have detections (and parents)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scans.jobs.<a href="src/hiddenlayer/scans/jobs/client.py">list</a>(...) -> ListJobsResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.jobs.list(
    start_time=datetime.datetime.fromisoformat("2025-05-27T00:00:00+00:00"),
    end_time=datetime.datetime.fromisoformat("2025-05-27T23:59:59+00:00"),
    scanner_version="1.0.0",
    detection_category="Embedded Payloads",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_version_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Model Version IDs
    
</dd>
</dl>

<dl>
<dd>

**model_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Model ID
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[datetime.datetime]` — Start Time
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[datetime.datetime]` — End Time
    
</dd>
</dl>

<dl>
<dd>

**severity:** `typing.Optional[ListJobsRequestSeverity]` — Severities
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Statuses
    
</dd>
</dl>

<dl>
<dd>

**request_source:** `typing.Optional[typing.Union[ScanJobRequestSource, typing.Sequence[ScanJobRequestSource]]]` — Filter by request source using a comma-separated list
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by region of the discovered asset
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by model provider name
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` 
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[str]` — allow sorting by model name, status, severity, scan start time, asset region, or model provider ascending (+) or the default descending (-)
    
</dd>
</dl>

<dl>
<dd>

**latest_per_model_version_only:** `typing.Optional[bool]` — only return latest result per model version
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[ListJobsRequestSource]` — source of model related to scans
    
</dd>
</dl>

<dl>
<dd>

**scanner_version:** `typing.Optional[str]` — filter by version of the scanner
    
</dd>
</dl>

<dl>
<dd>

**detection_category:** `typing.Optional[str]` — filter by a single detection category
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `typing.Optional[ListJobsRequestModelName]` — filter by the model name
    
</dd>
</dl>

<dl>
<dd>

**compliance_status:** `typing.Optional[typing.Union[PolicyStatus, typing.Sequence[PolicyStatus]]]` — A comma separated list of rule set evaluation statuses to include
    
</dd>
</dl>

<dl>
<dd>

**deep_scan:** `typing.Optional[bool]` — When true, returns only scans that with files. When false, returns only scans without files. When not provided, returns all scans.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scans Upload
<details><summary><code>client.scans.upload.<a href="src/hiddenlayer/scans/upload/client.py">start</a>(...) -> StartUploadResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.upload.start(
    model_version="model_version",
    model_name="model_name",
    requesting_entity="requesting_entity",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**model_version:** `str` — Model version
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `str` — Model name
    
</dd>
</dl>

<dl>
<dd>

**requesting_entity:** `str` — Requesting entity
    
</dd>
</dl>

<dl>
<dd>

**location_alias:** `typing.Optional[str]` — Requested location alias
    
</dd>
</dl>

<dl>
<dd>

**request_source:** `typing.Optional[ScanJobRequestSource]` 
    
</dd>
</dl>

<dl>
<dd>

**origin:** `typing.Optional[str]` — Specifies the platform or service where the model originated before being scanned
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scans.upload.<a href="src/hiddenlayer/scans/upload/client.py">complete_all</a>(...) -> CompleteAllUploadResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.upload.complete_all(
    scan_id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scan_id:** `str` — A Model Scan ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scans Results
<details><summary><code>client.scans.results.<a href="src/hiddenlayer/scans/results/client.py">list_files</a>(...) -> ListFilesResultsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a cursor-paginated list of file results for a given scan. Results are sorted by compliance status, then highest detection severity, then file path.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.results.list_files(
    scan_id="00000000-0000-0000-0000-000000000000",
    page_size=50,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scan_id:** `str` — A Model Scan ID
    
</dd>
</dl>

<dl>
<dd>

**has_detections:** `typing.Optional[bool]` — When true, only return files that have detections
    
</dd>
</dl>

<dl>
<dd>

**page_size:** `typing.Optional[int]` — Number of items to return per page
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scans.results.<a href="src/hiddenlayer/scans/results/client.py">sarif</a>(...) -> str</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.results.sarif(
    scan_id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scan_id:** `str` — A Model Scan ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scans.results.<a href="src/hiddenlayer/scans/results/client.py">retrieve_summary</a>(...) -> ScanReportSummaryResponseV3</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns aggregated summary information for a scan without file-level results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.results.retrieve_summary(
    scan_id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scan_id:** `str` — A Model Scan ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scans Reports
<details><summary><code>client.scans.reports.<a href="src/hiddenlayer/scans/reports/client.py">list</a>(...) -> ListReportsResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Returns a cursor-paginated list of scan reports.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.reports.list(
    page_size=5,
    limit=5,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**page_size:** `typing.Optional[int]` 

Number of items to return per page.
The use of `limit` is preferred, and it takes precedence over `page_size`.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Number of items to return per page.
    
</dd>
</dl>

<dl>
<dd>

**cursor:** `typing.Optional[str]` — Cursor for pagination, used to navigate through pages of results
    
</dd>
</dl>

<dl>
<dd>

**time:** `typing.Optional[ListReportsRequestTime]` — Time range for the report
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scans Reports Csv
<details><summary><code>client.scans.reports.csv.<a href="src/hiddenlayer/scans/reports/csv/client.py">create</a>(...) -> CreateCsvResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asynchronously initiates generation of a CSV scan report containing all scan results for the given time range.
Returns an ephemeral job ID that can be used to check the status of the export and download the file.
File is stored for 30 days once generated.

Constraints:
- Both `time[gte]` and `time[lte]` are required
- Date range cannot exceed 31 days
- Dates must be in RFC3339 format (e.g., 2023-01-01T00:00:00Z)
- Only scans with status "done" will be included in the export
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
from hiddenlayer.scans.reports.csv import CreateCsvRequestTime
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.reports.csv.create(
    time=CreateCsvRequestTime(
        gte=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
        lte=datetime.datetime.fromisoformat("2024-01-15T09:30:00+00:00"),
    ),
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**time:** `CreateCsvRequestTime` — Time range for scan results (both gte and lte are required, max 31 day range)
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scans.reports.csv.<a href="src/hiddenlayer/scans/reports/csv/client.py">get</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks the status to see if the CSV file is ready to download.  If the CSV file is ready the file will be returned in the response.  Files are stored for 30 days. If the report_id is lost, the report can be re-generated by re-submitting the request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.reports.csv.get(
    report_id="report_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**report_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scans Reports SupplyChain Csv
<details><summary><code>client.scans.reports.supply_chain.csv.<a href="src/hiddenlayer/scans/reports/supply_chain/csv/client.py">create</a>(...) -> CreateCsvResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Asynchronously initiates generation of a supply chain CSV report containing scan results matching the specified filters.
Returns an ephemeral report ID that can be used to check the status of the export and download the file.
File is stored for 30 days once generated.

**Row Limit**: Returns up to 10,000 most recent scan results.

**Filtering**: Supports the same filtering parameters as the Query endpoint (GET /scan/v3/results).

**Sorting**: Supports sorting via the `sort` parameter. Results can be ordered by any CSV column.

**Columns**: The CSV columns can be customized using the optional `column_list` query parameter.
If not specified, defaults to: name, detections, scanned_on, policy_status, origin, threat_level.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment
import datetime

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.reports.supply_chain.csv.create(
    start_time=datetime.datetime.fromisoformat("2025-05-27T00:00:00+00:00"),
    end_time=datetime.datetime.fromisoformat("2025-05-27T23:59:59+00:00"),
    scanner_version="1.0.0",
    detection_category="Embedded Payloads",
    region="us-east-1",
    provider="aws",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**column_list:** `typing.Optional[str]` 

Comma-separated list of columns to include in the CSV export.
Allowed values: name, detections, scanned_on, policy_status, origin, region, provider, threat_level.
If not specified, defaults to: name, detections, scanned_on, policy_status, origin, threat_level.
    
</dd>
</dl>

<dl>
<dd>

**model_version_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by model version IDs (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**model_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by model IDs (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**start_time:** `typing.Optional[datetime.datetime]` — Filter scans with start time greater than or equal to this value
    
</dd>
</dl>

<dl>
<dd>

**end_time:** `typing.Optional[datetime.datetime]` — Filter scans with start time less than or equal to this value
    
</dd>
</dl>

<dl>
<dd>

**severity:** `typing.Optional[CreateCsvRequestSeverity]` — Filter by severity levels (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — Filter by scan status (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**compliance_status:** `typing.Optional[typing.Union[PolicyStatus, typing.Sequence[PolicyStatus]]]` — Filter by compliance status (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**request_source:** `typing.Optional[typing.Union[ScanJobRequestSource, typing.Sequence[ScanJobRequestSource]]]` — Filter by request source (comma-separated)
    
</dd>
</dl>

<dl>
<dd>

**scanner_version:** `typing.Optional[str]` — Filter by scanner version
    
</dd>
</dl>

<dl>
<dd>

**detection_category:** `typing.Optional[str]` — Filter by detection category
    
</dd>
</dl>

<dl>
<dd>

**model_name:** `typing.Optional[CreateCsvRequestModelName]` — Filter by model name (supports exact match or contains)
    
</dd>
</dl>

<dl>
<dd>

**source:** `typing.Optional[CreateCsvRequestSource]` — Filter by model source
    
</dd>
</dl>

<dl>
<dd>

**latest_per_model_version_only:** `typing.Optional[bool]` — Only return latest scan result per model version
    
</dd>
</dl>

<dl>
<dd>

**region:** `typing.Optional[str]` — Filter by asset region
    
</dd>
</dl>

<dl>
<dd>

**provider:** `typing.Optional[str]` — Filter by model provider
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Maximum number of results to return
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Number of results to skip for pagination
    
</dd>
</dl>

<dl>
<dd>

**sort:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` 

Sort results by specified field. Prefix with `-` for descending order, `+` or no prefix for ascending.
Supported fields: name, detections, scanned_on, policy_status, origin, region, provider, threat_level, start_time, model_name, severity, status.

Note: If multiple sort parameters are provided, only the first one will be applied.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scans.reports.supply_chain.csv.<a href="src/hiddenlayer/scans/reports/supply_chain/csv/client.py">get</a>(...) -> typing.Iterator[bytes]</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Checks the status to see if the supply chain CSV file is ready to download.
If the CSV file is ready the file will be returned in the response.
Files are stored for 30 days. If the report_id is lost, the report can be re-generated by re-submitting the request.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.reports.supply_chain.csv.get(
    report_id="report_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**report_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Scans Upload File
<details><summary><code>client.scans.upload.file.<a href="src/hiddenlayer/scans/upload/file/client.py">add</a>(...) -> AddFileResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.upload.file.add(
    scan_id="00000000-0000-0000-0000-000000000000",
    file_content_length=1,
    file_name="exampleFile.txt",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scan_id:** `str` — A Model Scan ID
    
</dd>
</dl>

<dl>
<dd>

**file_content_length:** `int` — Added file size in bytes
    
</dd>
</dl>

<dl>
<dd>

**file_name:** `typing.Optional[str]` 

File name. One of `file-name` or `file-name-base64` must be provided.
When `file-name-base64` is present it takes precedence; otherwise this value is used.
    
</dd>
</dl>

<dl>
<dd>

**file_name_base64:** `typing.Optional[str]` 

UTF-8 friendly base64-encoded file name. Optional; when omitted, the server uses the `file-name` header.
One of `file-name` or `file-name-base64` must be provided.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.scans.upload.file.<a href="src/hiddenlayer/scans/upload/file/client.py">complete</a>(...) -> CompleteFileResponse</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.scans.upload.file.complete(
    scan_id="00000000-0000-0000-0000-000000000000",
    file_id="file_id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scan_id:** `str` — A Model Scan ID
    
</dd>
</dl>

<dl>
<dd>

**file_id:** `str` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## SupplyChain Scans
<details><summary><code>client.supply_chain.scans.<a href="src/hiddenlayer/supply_chain/scans/client.py">get</a>(...) -> typing.Optional[typing.Dict[str, typing.Any]]</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.supply_chain.scans.get(
    scan_id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scan_id:** `str` — A Model Scan ID
    
</dd>
</dl>

<dl>
<dd>

**accept:** `typing.Optional[GetScansRequestAccept]` 
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.supply_chain.scans.<a href="src/hiddenlayer/supply_chain/scans/client.py">guidance</a>(...) -> GuidanceScansResponse</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

[BETA] This endpoint is not GA or Production ready and is subject to changes at any time. Breaking changes may occur.

Remediation guidance is generated on-demand with AI assistance and may not be
immediately available.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from hiddenlayer import HiddenLayer
from hiddenlayer.environment import HiddenLayerEnvironment

client = HiddenLayer(
    token="<token>",
    environment=HiddenLayerEnvironment.PROD_US,
)

client.supply_chain.scans.guidance(
    scan_id="00000000-0000-0000-0000-000000000000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**scan_id:** `str` — A Model Scan ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

