# Locked In

The room and command-line game are provided. You will write the LLM integration in `interpreter.py`.

Follow the assignment on Moodle for the eight steps and submission requirements. The assignment document is distributed separately from this repository.

## Setup

Use Python 3.10 or newer. The supplied starter uses only the Python standard library; no packages need to be installed.

From this repository's root, create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

The natural-language game and evaluator need your implementation of `interpret_request(...)` before they can make model requests. The manual explorer and API probe can be used immediately.

## Explore the room

These commands work without an API key:

```bash
python manual_room.py --demo
python manual_room.py
```

`world.py` contains the room and its rules. The manual explorer lets you try actions before you connect a model.

## Connect to an API

Pick an OpenAI-compatible Chat Completions API from [awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis), or another provider with the same interface. Check that your model is available on a free tier.

Example setup for macOS and Linux:

```bash
export LLM_BASE_URL="https://api.groq.com/openai/v1"
export LLM_MODEL="llama-3.3-70b-versatile"
export LLM_API_KEY="your-api-key"
python api_probe.py
```

For PowerShell, set variables using `$env:LLM_API_KEY="..."` and the same syntax for the other settings.

Provider models, availability and limits can change; confirm the values in your provider's documentation.

`api_probe.py` is an example of a single HTTP request. Use it to see how the authentication header, endpoint and request body work. Never commit an API key.

## Build the interpreter

Implement `interpret_request(...)` in `interpreter.py`. The function interface is already defined and is used by `locked_in.py` and `evaluate.py`.

Your implementation needs to:

- Send the player's message, known objects, action schema and recent conversation to the LLM.
- Convert the reply into one valid action dictionary.
- Return request measurements alongside the action.
- Report failed calls and unusable replies using `ModelError`.
- Support `baseline` and `revised` prompts for evaluation.

You're free to use helper functions or extra modules. The other files are provided so you can focus on the API integration and language handling.

## Run and evaluate

```bash
python locked_in.py --show-actions
python evaluate.py --cases C01,C03,C04 --output trial.jsonl
python evaluate.py --output comparison.jsonl
```

A full evaluation makes 37 API requests before any retries. Check your provider's rate limit. The evaluator supports `--pause` and `--cases` for smaller batches.

Your interpreter must return `model`, `temperature`, `attempts`, `elapsed_ms`, `raw_content` and `first_response_contract_valid` in the measurements dictionary. `locked_in.py` adds the accepted action, room feedback and public state. On failure, raise `ModelError("message", metrics)`. The game will keep the current state and conversation history.

## File guide

- `locked_in.py`: game loop, action checks and logs
- `world.py`: room, discoveries, inventory and puzzle rules
- `errors.py`: error class for failed API calls
- `cases.py`: test situations and expected actions
- `evaluate.py`: comparison of prompt behaviour and response times
