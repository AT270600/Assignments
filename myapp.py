from flask import Flask, render_template, request, redirect, url_for

myapp = Flask(__name__)

# Create a list to store tasks
tasks = []

@myapp.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@myapp.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect(url_for("index"))

if __name__ == "__main__":
    myapp.run(debug=True)
