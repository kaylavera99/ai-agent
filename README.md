# AI Agent (Code Assistant)
A tiny AI code agent that can read files, list directories, execute Python files, and write files within a sandbox working directory. It's designed to be clear enough to learn from while also small enough to extend. You can add your own ```'mini-app'``` adjacent to folders like ```calculator/``` or ```converter/```, then ask the agent to explore, run, fix or explain them.

### Purpose
- Seeing how an LLM plans tool calls and uses functions
- Composable in that you can drop in new folders/apps and let the agent inspect or execute them
- All file operations are constrained to the working directory ```WORKING_DIR``` in ```config.py```

### Features
- Model: Google Gemini via ```google.genai```
- Secrets via ```.env``` (```GEMINI_API_KEY```)
- Tools:
    - List contents of directories with associated files
    - Read file contents
    - Execute Python files with arguments via CLI
    - Write and overwrite files.
- Example apps: 
    - [```calculator/```](https://github.com/kaylavera99/ai-agent/tree/b942e174a5e2833c8ff680be224ec30e2ba8f4ee/calculator#readme): Simple calculator app
    - [```converter/```](https://github.com/kaylavera99/ai-agent/tree/b942e174a5e2833c8ff680be224ec30e2ba8f4ee/converte#readme): Simple mass, temperature and distance converter


## Project Structure
```
ai-agent/
├─ calculator/
│  ├─ pkg/               # calculator application and render helpers
│  ├─ main.py            # CLI entry for calculator
│  └─ tests.py
├─ converter/
│  ├─ pkg/               # conversion tool application files and render helpers
│  ├─ main.py            # CLI entry for converter
│  └─ tests.py
├─ functions/            # tools the agent can call
├─ templates/            # (in progress) Flask UI templates
├─ app.py                # (in progress) Flask UI to chat with the agent
├─ main.py               # agent CLI entrypoint
├─ config.py             # working dir and iteration limits
├─ prompts.py            # language prompt
├─ pyproject.toml
├─ uv.lock
└─ README.md

```

## Requirements
- Python 3.10+
- [```uv```](https://docs.astral.sh/uv/) Project/package manager
- Unix-like shell (WSL Recommended)
- A Google API key in ```.env```:
    ```
    GEMINI_API_KEY = <your-api-key>
    ```

## Install

## Run the agent

### Running the example apps directly

## Tests

### Expected Output

## Adding your own mini-app



