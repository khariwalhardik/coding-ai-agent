"""Top-level CLI to orchestrate local tools for the coding-ai-agent workspace.

This module provides a small command-line interface that uses utility
functions placed in `tools/` (for example `get_file_info` and
`run_file.run_python_file`) so you can inspect files and execute/python
scripts from the repository.

Subcommands:
  fileinfo   - print file/directory summary using tools.get_file_info
  run        - run a Python file using tools.run_file.run_python_file
  list-tools - list available tool modules under ./tools

The CLI is intentionally defensive: imports of optional tools happen
only when the corresponding command runs, so the module can be imported
or checked for syntax without requiring every third-party dependency.
"""

from __future__ import annotations

import argparse
import os
import sys
from typing import Optional


def cmd_fileinfo(working_dir: str, directory: Optional[str]):
    try:
        from tools.get_file_info import get_file_info
    except Exception as e:
        print(f"Failed to import get_file_info: {e}", file=sys.stderr)
        return 2

    out = get_file_info(working_dir, directory)
    print(out)
    return 0


def cmd_run(working_dir: str, file_path: str):
    try:
        from tools.run_file import run_python_file
    except Exception as e:
        print(f"Failed to import run_file: {e}", file=sys.stderr)
        return 2

    out = run_python_file(working_dir, file_path)
    print(out)
    return 0


def cmd_list_tools(tools_dir: str = "tools"):
    base = os.path.abspath(tools_dir)
    if not os.path.isdir(base):
        print(f"Tools directory not found: {base}", file=sys.stderr)
        return 2
    mods = []
    for entry in os.listdir(base):
        if entry.endswith(".py"):
            mods.append(entry)
        elif os.path.isdir(os.path.join(base, entry)) and "__init__.py" in os.listdir(os.path.join(base, entry)):
            mods.append(entry + "/")
    print("Available tools:")
    for m in sorted(mods):
        print(" -", m)
    return 0


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="coding-ai-agent helper CLI")
    sub = p.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("fileinfo", help="Show file/directory info using tools.get_file_info")
    a.add_argument("working_dir", nargs="?", default=".", help="Working directory (default: .)")
    a.add_argument("directory", nargs="?", default=None, help="Subdirectory to inspect (optional)")

    b = sub.add_parser("run", help="Run a Python file using tools.run_file.run_python_file")
    b.add_argument("working_dir", nargs="?", default=".", help="Working directory where the file should be run")
    b.add_argument("file_path", help="Path to the python file to run (relative to working_dir)")

    c = sub.add_parser("list-tools", help="List tool modules under ./tools")
    c.add_argument("tools_dir", nargs="?", default="tools", help="Path to tools directory")

    return p


def main(argv: Optional[list[str]] = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.cmd == "fileinfo":
        return cmd_fileinfo(args.working_dir, args.directory)
    if args.cmd == "run":
        return cmd_run(args.working_dir, args.file_path)
    if args.cmd == "list-tools":
        return cmd_list_tools(args.tools_dir)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())