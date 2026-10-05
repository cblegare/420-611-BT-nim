#!/usr/bin/env -S uv run --script --quiet

# /// script
# dependencies = ["nox[uv]"]
# ///

from __future__ import annotations

from pathlib import Path

import nox

PYTHON_VERSIONS = [
    # "3.11",
    "3.12",
    # "3.13",
    # "3.14"
]
DEFAULT_PYTHON = max(PYTHON_VERSIONS)

REPO_ROOT = Path(__file__).parent.resolve()

BUILD_ROOT = REPO_ROOT / "build"
REPORT_ROOT = BUILD_ROOT / "report"
SRC_ROOT = REPO_ROOT / "src"
DOCS_ROOT = REPO_ROOT / "docs"
TEST_ROOT = REPO_ROOT / "test"

nox.options.default_venv_backend = "uv"
nox.options.parallel = True


@nox.session(python=DEFAULT_PYTHON, tags=["py", "format"])
def format_py(session: nox.Session):
    session.install("ruff")
    session.run("ruff", "format", ".")


@nox.session(python=DEFAULT_PYTHON, tags=["py", "fix", "lint"])
def lint_py(session: nox.Session):
    session.install("ruff")
    session.run("ruff", "check", "--fix", "--unsafe-fixes", ".")


@nox.session(python=PYTHON_VERSIONS, tags=["py", "test"])
def pytest(session: nox.Session):
    session.run_install(
        "uv",
        "sync",
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run(*_coverage_cmd(session.name, ["pytest", "."]))


@nox.session(python=PYTHON_VERSIONS, tags=["py", "lint", "typing"], default=False)
def typing(session: nox.Session):
    targets = [path for path in (SRC_ROOT,) if path.exists()]

    if not targets:
        session.skip("No suitable target paths found")

    session.run_install(
        "uv",
        "sync",
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.run("mypy", "--python-version", session.python, "src")


@nox.session(python=DEFAULT_PYTHON, tags=["py", "report"])
def coverage(session: nox.Session):
    targets = [path for path in (TEST_ROOT,) if path.exists()]

    if not targets:
        session.skip("No suitable target paths found")

    session.run_install(
        "uv",
        "sync",
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    session.install("coverage[xml]")
    session.run("coverage", "combine", "--keep")
    session.run("coverage", "xml")
    session.run("coverage", "html")
    session.run("coverage", "report")

    html_report = REPORT_ROOT / "coverage/html/index.html"
    xml_report = REPORT_ROOT / "coverage.xml"

    session.log(f"Cobertura-compatible test coverage report at {xml_report.resolve()}")
    session.log(f"Browse HTML test coverage report at {html_report.resolve()}")


def _coverage_cmd(context: str, modulecmd: list[Path | str]) -> list[str]:
    return [
        "python",
        "-m",
        "coverage",
        "run",
        f"--context={context}",
        "-m",
        *(str(part) for part in modulecmd),
    ]


if __name__ == "__main__":
    nox.main()
