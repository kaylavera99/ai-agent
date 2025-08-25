import os
from google.genai import types
def write_file(working_directory, file_path, content):
    working_dir = os.path.abspath(working_directory)
    abs_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_path.startswith(working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory' 
    
    

    try:
        parent_dir = os.path.dirname(abs_path)
        os.makedirs(parent_dir, exist_ok=True)


        with open(abs_path, "w") as full:
            full.write(content)

        return f'Successfully wrote to "${file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: {str(e)}'



schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write to a file and if the file doesnt already exist, create it",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path (relative to the working directory) to write to",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file"
            )
        },
        required=["file_path", "content"]
    ),
)