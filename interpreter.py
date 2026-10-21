"""Your code goes here: turn player language into ONE proposed action.

The game loop calls interpret_request(text, observation, schema, history, ...).
You receive only PUBLIC data (not the private room State). Implement this
however you like: split it into prompt-building, API and parsing functions,
or add separate Python modules. The interface below is the only requirement
imposed by locked_in.py and evaluate.py.

Return:
    (action_dict, metrics_dict)

On network errors, unusable JSON or an invalid action, raise
    ModelError("short explanation", metrics_dict)
from errors.py. Do not return a guessed action after an API failure.

Metrics: model, temperature, attempts, elapsed_ms, raw_content,
first_response_contract_valid. The game adds the validated action and feedback.
"""


def interpret_request(text, observation, schema, history, *, prompt="revised",
                      model=None, base_url=None, api_key=None,
                      temperature=0.2, timeout=60.0):
    raise NotImplementedError("Implement the LLM interpreter in interpreter.py")
