import os
import subprocess
import sys

port = os.environ.get("PORT", "8080")

subprocess.run(
    [
        sys.executable,
        "-m",
        "streamlit",
        "run",
        "ui/streamlit_app.py",
        "--server.port",
        port,
        "--server.address",
        "0.0.0.0",
    ]
)