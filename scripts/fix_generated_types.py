#!/usr/bin/env python3
"""
Script to fix generated types in miga_pydantic.py and transient LinkML modules.
Replaces 'integer' → 'int', 'string' → 'str', 'boolean' → 'bool'.
"""

import re
import os
import pathlib
import fileinput

def fix_types_in_file(file_path: str):
    path = pathlib.Path(file_path)
    print(f"🔍 Checking file: {file_path}")
    if not path.exists():
        print(f"⚠️ File not found: {file_path}")
        return

    content = path.read_text()
    print(f"📄 File content length: {len(content)}")

    # Count occurrences
    integer_count = content.count("integer")
    string_count = content.count("string")
    boolean_count = content.count("boolean")
    print(f"🔢 Found {integer_count} occurrences of 'integer'")
    print(f"🔢 Found {string_count} occurrences of 'string'")
    print(f"🔢 Found {boolean_count} occurrences of 'boolean'")

    new_content = content.replace("integer", "int").replace("string", "str").replace("boolean", "bool")

    if new_content != content:
        path.write_text(new_content)
        print(f"✅ Fixed types in {file_path}")
    else:
        print(f"✅ No changes needed in {file_path}")

if __name__ == "__main__":
    filepath = "src/miga/datamodel/miga_pydantic.py"
    fix_types_in_file(filepath)

    # Also patch the transient "test" module used by linkml-run-examples
    test_module = pathlib.Path("test")
    if test_module.exists():
        print(f"🧩 Patching transient test module: {test_module}")
        fix_types_in_file(str(test_module))
    else:
        print("⚠️ No transient 'test' module found to patch")