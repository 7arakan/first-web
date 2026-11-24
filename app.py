import os
import socket
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "v1.0.0")
    env = os.getenv("APP_ENV", "dev")
    hostname = socket.gethostname()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"""
    <html>
      <head><title>First Web {version}</title></head>
      <body style="font-family: sans-serif; background: #111827; color: #f3f4f6; text-align: center; padding-top: 60px;">
        <div style="background: #1f2937; display: inline-block; padding: 30px 50px; border-radius: 12px;">
          <h1 style="color: #38bdf8;">First Web Service</h1>
          <p><strong>Версия:</strong> <span style="background: #0284c7; padding: 4px 10px; border-radius: 6px;">{version}</span></p>
          <p><strong>Окружение:</strong> {env}</p>
          <p><strong>Контейнер (Hostname):</strong> <code>{hostname}</code></p>
          <p><strong>Время:</strong> {now}</p>
        </div>
      </body>
    </html>
    """

@app.route("/health")
def health():
    return jsonify(status="ok", version=os.getenv("APP_VERSION", "v1.0.0")), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
