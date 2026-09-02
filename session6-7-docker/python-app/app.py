from flask import Flask

app = Flask(__name__)

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Python Hello World</title>
  <style>
    body { margin: 0; font-family: Arial, sans-serif; background: #1e3a5f; color: #f9fafb;
           display: flex; align-items: center; justify-content: center; height: 100vh; }
    .card { background: #274b73; padding: 40px 60px; border-radius: 12px; text-align: center;
            box-shadow: 0 8px 24px rgba(0,0,0,0.4); }
    h1 { margin: 0 0 10px; color: #ffd43b; }
    p { margin: 0; color: #d1d5db; }
  </style>
</head>
<body>
  <div class="card">
    <h1>Hello World from Python!</h1>
    <p>Served by Flask inside a Docker container on port 5000</p>
  </div>
</body>
</html>"""


@app.route("/")
def hello():
    return PAGE


@app.route("/health")
def health():
    return {"status": "ok", "app": "python-app"}


if __name__ == "__main__":
    # 0.0.0.0 so the server is reachable from outside the container
    app.run(host="0.0.0.0", port=5000)
