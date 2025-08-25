import os
from google.genai import types
from config import MAXCHARS
def get_file_content(working_directory, file_path):

    MAX_CHARS = 10000
    working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory' 
    if not os.path.isfile(abs_file_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        
        
        with open(abs_file_path, "r") as full:
            file_contents = full.read()

        if len(file_contents) > MAX_CHARS:
            file_contents= file_contents[:MAX_CHARS]
            file_contents += (f'[...File path {file_path} truncated at 10000 characters]')

        return file_contents

    except Exception as e:
         return f'Error: {str(e)}'  


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Lists contents of a file truncated to 10000 chars",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Getting content from this file",
            ),
        },
        required=["file_path"]
    ),
)

        