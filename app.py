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
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
    <title>Simple Calculator</title>
</head>
<body >
 
 
<nav class="navbar navbar-expand-lg bg-body-tertiary bg-primary" data-bs-theme="dark">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <ul class="navbar-nav me-auto mb-2 mb-lg-0">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Link</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown
          </a>
          <ul class="dropdown-menu">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><hr class="dropdown-divider"></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
       
      </ul>
      <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search"/>
        <button class="btn btn-outline-success" type="submit">Search</button>
      </form>
    </div>
  </div>
</nav>

    <div class="container" style="font-family: Arial; text-align:center; margin-top:5em; >
    
     <div class="row">
   
   <div class="col-sm">
   </div>
   
    <div class="col-sm">
    <h2>Simple Calculator</h2>
    <form method="POST">
        <input type="number" name="num1" placeholder="enter 1st number" required>
        <select name="operation">
            <option value="+">+</option>
            <option value="-">-</option>
            <option value="*">*</option>
            <option value="/">/</option>
        </select>
        <input type="number" name="num2" placeholder="enter 2nd number" required>
        <button type="submit">Calculate</button>
    </form>
    {% if result is not none %}
        <h3>Result: {{ result }}</h3>
    {% endif %}

    </div>
    
    <div class="col-sm">
    </div>
    
  </div>
    
    
    </div>
    
    
    
    </div>
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js" integrity="sha384-FKyoEForCGlyvwx9Hj09JcYn3nv7wiPVlz7YYwJrWVcXK/BmnVDxM+D2scQbITxI" crossorigin="anonymous"></script>
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
