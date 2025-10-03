from flask import Flask, render_template, request
import json
from default_api import default_api

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ''
    error = ''
    if request.method == "POST":
        command = request.form["command"]
        try:
            result = default_api.get_files_info(directory=command)
            output = json.dumps(result)
        except Exception as e:
            error = str(e)

        return render_template("index.html", command=command, output=output, error=error)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
