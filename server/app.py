from flask import Flask

TEMPLATES_DIR = "templates"

app = Flask(__name__, template_folder=TEMPLATES_DIR)

@app.route('/')
def index():
    return 'Hello World!'

@app.route("/<project>/<bid>")
def display_bug(project, bid):
    # bug = Bug(proj=project, bid=bid)
    return {'pid': project, 'bid': bid}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)