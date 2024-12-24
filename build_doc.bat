@echo off
for %%F in (*.py) do (
    python -m pydoc -w %%F
)