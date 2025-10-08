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
    - Execute Python files with arguments via CLI within a secure sandbox
    - Read, write and overwrite files. 
    - Easily add new functionalities by creating 'mini-apps' in dedicated folders. 
    - Includes pre-built modules that can be expanded or replaced. 
- Example apps: 
    - [```calculator/```](https://github.com/kaylavera99/ai-agent/tree/b942e174a5e2833c8ff680be224ec30e2ba8f4ee/calculator#readme): Simple calculator app
    - [```converter/```](https://github.com/kaylavera99/ai-agent/tree/b942e174a5e2833c8ff680be224ec30e2ba8f4ee/converter#readme): Simple mass, temperature and distance converter


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
├─ new_app_template/
│  ├─ pkg/               # Core app functionality goes here
│     └── new_app.py     
│  ├─ main.py            # Ai Agent / CLI Entry point 
│  ├─ __init__.py        # This will tell Python to treat the mini app as a package
│  └─ tests.py           # (Optional tests)   
├─ functions/            # tools the agent can call
├─ templates/            # (in progress) Flask UI templates
├─ app.py                # (in progress) Flask UI to chat with the agent
├─ main.py               # agent CLI entrypoint
├─ tests.py              # unit tests
├─ config.py             # working dir and iteration limits
├─ prompts.py            # language prompt
├─ pyproject.toml        # project metadata and dependencies
├─ pytest.ini            # Pytest configuration
├─ uv.lock               # UVicorn lock file for ASGI server
└─ README.md

```

## Requirements
- Python 3.10+
- [```uv```](https://docs.astral.sh/uv/) Project/package manager (Optional: CLI convenience, not needed to run the agent)
- Unix-like shell (WSL Recommended)
- A Google API key in ```.env```:
    ```
    GEMINI_API_KEY = <your-api-key>
    ```

## Installation
### 1. Clone the repo
```
git clone https://github.com/kaylavera99/ai-agent
cd ai-agent
```
### 2. Create a virtual environment
```
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```

## Environment Variables
The AI Agent requires a Gemini API key for Google Gemini
- Option 1: Use .env file (Recommended)
  Create a new file named '.env' at the root of your project with your API key:
  ```
  GEMINI_API_KEY = your-api-key
  ```
- Option 2: Set it in your terminal
  ```
  export GEMINI_API_KEY = "your-api-key"

## Run the agent
The AI Agent can be ran in two ways:
### Using Python directorly (Recommended)
```
python main.py "<your-prompt-here>"
```
### Using uv
```
uv run main.py "<your-prompt-here>"
```

Note: ```uv``` is completely optional and is used for virtual enviornment awareness and makes this agent easier to scale in the future. On some systems, this can prevent using the incorrect Python version or wrong dependencies. You may see warnings like ```VIRTUAL_ENV=venv does not match the project environment path .venv```and they can safely be ignored. 

### Running the example apps directly
```
python calculator/main.py "2 + 3 - 8"
python converter/main.py "12 F to C"

uv run calculator/main.py "10 - 7"
uv run converter/main.py "12934 kgs to pounds"
```
## Tests
```
# AI-Agent Tests
python tests.py
uv run tests.py

# Mini-App Tests
python calculator/tests.py -verbose
uv run calculator/tests.py 

python converter/tests.py
uv run calculator/tests.py -verbose
```

## Adding your own mini-app
1. Create a new folder in the root of the ```ai-agent```, adjacent to ```calculator/``` and ```converter/```
2. Implement your application logic as such, having logic separated from entry point 
```
ai-agent/
├─ new_app_template/
│  ├─ pkg/              
│     └── new_app.py     # Core app functionality goes here
│  ├─ main.py            # Ai Agent / CLI Entry point 
│  ├─ __init__.py        # This will tell Python to treat the mini app as a package
│  └─ tests.py           # (Optional tests) 
....
```
3. Run:
```
# Run application directly
python new_app_template/main.py "your-prompt-here"

# Ask the Agent to evaluate your application directly from the root:
python main.py "What is the new app template?"

```


