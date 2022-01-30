from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        pass_fail_percentages=[("test1", 10, 90),
                               ("test2", 100, 0),
                               ("test3", 99, 1),
                               ("test4", 0, 100),
                               ("test5", 30, 70)])


if __name__ == "__main__":
    app.run()
    url_for('static', filename='styles.css')
    url_for('static', filename='dashboard.css')
