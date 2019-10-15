import sys
import nox


@nox.session(reuse_venv=True)
def deps(session):
    session.install("pip-tools")
    session.run(
        "pip-compile",
        "requirements.in",
        "-o",
        "requirements.txt",
        "--no-header",
        "--generate-hashes",
    )
    session.run(sys.executable, "-m", "pip", "install", "-r", "requirements.txt")
