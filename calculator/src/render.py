"""Rendering helpers (small HTML templates used by the Flask app)."""
from typing import Any


def index_template() -> str:
    return """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Calculator</title>
    <style>
      body { font-family: Arial, Helvetica, sans-serif; margin: 2rem }
      form { margin-bottom: 1rem }
      input[type=text] { width: 300px; padding: 6px }
      .history { margin-top: 1rem }
      .error { color: red }
    </style>
  </head>
  <body>
    <h1>Calculator</h1>
    {% if error %}<p class="error">{{ error }}</p>{% endif %}
    <form action="/calculate" method="post">
      <input name="expression" type="text" placeholder="e.g. 2 + 2 * (3 - 1)" required />
      <button type="submit">Calculate</button>
    </form>

    <div class="history">
      <h2>History</h2>
      <ul>
        {% for item in history %}
          <li><strong>{{ item.expression }}</strong> = {{ item.result }}</li>
        {% else %}
          <li><em>No history yet</em></li>
        {% endfor %}
      </ul>
    </div>
  </body>
</html>
"""
