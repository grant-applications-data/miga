## Add your own just recipes here. This is imported by the main justfile.

# Override generate to use gen-pydantic
generate:
    uv run gen-pydantic src/miga/schema/miga.yaml > src/miga/datamodel/miga_pydantic.py
    uv run python scripts/fix_generated_types.py

# Custom Python test runner that uses gen-pydantic
_test-python-custom:
    just generate
    uv run python -m pytest
    uv run python scripts/fix_generated_types.py

_test-examples-custom:
    mkdir -p examples/output
    rm -rf examples/output/*.*
    # First pass: fix pydantic
    uv run python scripts/fix_generated_types.py
    # Run examples (this generates 'test')
    uv run linkml-run-examples \
        --input-formats json \
        --input-formats yaml \
        --output-formats json \
        --output-formats yaml \
        --counter-example-input-directory tests/data/invalid \
        --input-directory tests/data/valid \
        --output-directory examples/output \
        --schema src/miga/schema/miga.yaml > examples/output/README.md || true
    # Second pass: patch transient "test" module
    uv run python scripts/fix_generated_types.py
    # Run examples again, now that 'test' is patched
    uv run linkml-run-examples \
        --input-formats json \
        --input-formats yaml \
        --output-formats json \
        --output-formats yaml \
        --counter-example-input-directory tests/data/invalid \
        --input-directory tests/data/valid \
        --output-directory examples/output \
        --schema src/miga/schema/miga.yaml > examples/output/README.md || true

# Override test to use our custom runner instead of the default
test-custom: _test-schema _test-python-custom _test-examples-custom