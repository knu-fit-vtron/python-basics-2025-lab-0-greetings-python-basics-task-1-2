import subprocess
import sys
from pathlib import Path

ROOT = Path.cwd()

def run_prog(given: str) -> str:
    prog = ROOT / "main.py"
    assert prog.exists(), f"Не знайдено {prog}"
    cp = subprocess.run(
        [sys.executable, str(prog)],
        input=given,
        text=True,
        capture_output=True,
        timeout=2
    )
    assert cp.returncode == 0, f"Program exited with code {cp.returncode}. stderr:\n{cp.stderr}"
    return cp.stdout

def check(name: str):
    out = run_prog(name + "\n")
    assert out.strip() == f"Привіт, {name}!", (
        f"Очікував: 'Привіт, {name}!'\nОтримав: '{out.strip()}'"
    )

def test_greeting_cyrillic():
    check("Іван")

def test_greeting_latin():
    check("Anna")
