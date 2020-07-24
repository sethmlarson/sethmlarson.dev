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
        "--upgrade",
        "--no-header",
        "--generate-hashes",
    )
    session.run(sys.executable, "-m", "pip", "install", "-r", "requirements.txt")


@nox.session(reuse_venv=True)
def run(session):
    session.run(
        "docker", "build", "--tag=sethmlarson-dev", ".", external=True)
    session.run(
        "docker",
        "run",
        "--rm",
        "-it",
        "-p",
        "8080:8080",
        "-e",
        "PORT=8080",
        "sethmlarson-dev",
        external=True,
        success_codes=[0, 130],
    )
