# Red Team Integrations

Example notebooks for driving HiddenLayer red team evaluations against different
kinds of targets using the [HiddenLayer Python SDK](https://github.com/hiddenlayerai/hiddenlayer-sdk-python).

Every notebook follows the same pattern:

1. Configure the target and the evaluation parameters.
2. Implement an async `handler(prompt, history, session_id, target_system_prompt)`
   that calls your target and returns its reply as a string.
3. Start a session with `client.evaluation_sessions.red_team.start_session(...)`
   and drive it with `session.run_with_callback_parallel(handler=handler)`.
4. Retrieve the report with `client.evaluations.red_team.retrieve_evaluation_results(...)`.

The `handler` is the only integration point — swap it to point at any target.

`red_team_openai.ipynb` additionally shows how to **resume** an existing
workflow (`resume_session` + `retrieve_status`), and `red_team_http_api.ipynb`
shows scoping a run to a project via `hiddenlayer_project_id`.

## Notebooks

| Notebook | Target |
|----------|--------|
| [`red_team_openai.ipynb`](./red_team_openai.ipynb) | An OpenAI Chat Completions model |
| [`red_team_http_api.ipynb`](./red_team_http_api.ipynb) | A custom LLM app/agent behind an HTTP/REST endpoint |
| [`red_team_playwright.ipynb`](./red_team_playwright.ipynb) | A web chat UI driven via Playwright browser automation |
| [`red_team_static_prompts.ipynb`](./red_team_static_prompts.ipynb) | A target tested with a pre-written static prompt set |
| [`red_team_template.ipynb`](./red_team_template.ipynb) | Generic skeleton — drop in any target |

## Setup

```bash
pip install hiddenlayer-sdk jupyter

# Per-notebook extras:
pip install openai        # red_team_openai.ipynb
pip install playwright    # red_team_playwright.ipynb
playwright install chromium
```

Provide credentials via environment variables (read automatically by the SDK):

- `HIDDENLAYER_CLIENT_ID` and `HIDDENLAYER_CLIENT_SECRET` (OAuth2), **or**
- `HIDDENLAYER_TOKEN` (Bearer token)
- `OPENAI_API_KEY` for `red_team_openai.ipynb`

By default the client targets US production (`prod-us`). For EU production pass
`environment="prod-eu"`, and for a self-hosted deployment pass
`base_url="http://your-host:port"` to `AsyncHiddenLayer()`.

## Run

```bash
jupyter lab examples/red_team/red_team_openai.ipynb
```

Run the cells top to bottom. Results are viewable in the
[HiddenLayer Console](https://console.hiddenlayer.ai/).
