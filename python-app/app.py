"""Simple Flask app used for GitHub Actions learning demos."""

import os
import platform
import socket
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
APP_ENV = os.getenv("APP_ENV", "dev")


def build_info():
    """Details that change per deploy, to see your workflow's effect."""
    return {
        "version": APP_VERSION,
        "environment": APP_ENV,
        "hostname": socket.gethostname(),
        "python": platform.python_version(),
        "commit": os.getenv("GIT_SHA", "local")[:7],
        "server_time": datetime.now(timezone.utc).strftime(
            "%Y-%m-%d %H:%M:%S UTC"
        ),
    }


@app.route("/")
def index():
    return render_template("index.html", info=build_info())


@app.route("/health")
def health():
    return jsonify(status="ok"), 200


@app.route("/api/info")
def info():
    return jsonify(build_info())


if __name__ == "__main__":
    # Local dev only; in production run via gunicorn (see gunicorn.conf.py)
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", "5000")), debug=True)
