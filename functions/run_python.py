import os
import subprocess
from google.genai import types


def run_python_file(working_directory, file_path, args=None):
    working_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))
    

    if not abs_path.startswith(working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory' 
    
    if not os.path.isfile(abs_path):
            return f'Error: File "{file_path}" not found'
    
    if not abs_path.endswith(".py"):
         return f'Error: "{file_path}" is not a Python file'
    
    try: 
        cmd = ["python", abs_path] 
        if args:
            cmd.extend(args)
        completed_run = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=working_dir,
            timeout=30  
        )

        output = []
        if completed_run.stdout:
            output.append(f"STDOUT:\n{completed_run.stdout}")
        if completed_run.stderr:
            output.append(f"STDERR:\n{completed_run.stderr}")
        if completed_run.returncode != 0:
            output.append(f"Process exited with code {completed_run.returncode}")

        if not output:
             return "No output produced"
        return "\n".join(output) if output else "No output produced"
    
    except Exception as e:
        return f'Error: executing Python file: {str(e)}'
    



schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Run specified python files, optionally passing arguments",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The python file to run",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of CLI arguments"
            )
        },
        required=["file_path"]
        
    ),
)