from flask import Flask
import ujson

app = Flask(__name__)

@app.get("/")
def hello():
    return ujson.dumps({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)