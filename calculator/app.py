from flask import Flask, request, render_template_string, redirect, url_for

from src.service import CalculatorService
from src.render import index_template


app = Flask(__name__)
service = CalculatorService()


@app.route("/", methods=["GET"])
def index():
    tpl = index_template()
    return render_template_string(tpl, history=service.get_history(), error=None)


@app.route("/calculate", methods=["POST"])
def calculate():
    expression = request.form.get("expression", "")
    try:
        result = service.evaluate(expression)
        # after successful evaluation redirect back to index (history shows results)
        return redirect(url_for("index"))
    except Exception as exc:
        tpl = index_template()
        return render_template_string(tpl, history=service.get_history(), error=str(exc)), 400


if __name__ == "__main__":
    # Run the Flask app when invoked directly.
    app.run(host="127.0.0.1", port=5000, debug=True)
