"""""
from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Ank 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

"""

from flask import Flask, render_template_string, request
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Simple Calculator</title>
</head>
<body style="font-family: Arial; text-align:center; margin-top:50px;">
    <h2>Simple Calculator</h2>
    <form method="POST">
        <input type="number" name="num1" required>
        <select name="operation">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="number" name="num2" required>
        <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
  result = None
  if request.method == "POST":
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    op = request.form["operation"]

    if op == "+":
      result = num1 + num2
    elif op == "-":
      result = num1 - num2
    elif op == "*":
      result = num1 * num2
    elif op == "/":
      result = "Cannot divide by zero" if num2 == 0 else num1 / num2

  return render_template_string(HTML, result=result), 200


if __name__ == "__main__":
  port = int(os.environ.get("PORT", 8080))
  app.run(host="0.0.0.0", port=port)
