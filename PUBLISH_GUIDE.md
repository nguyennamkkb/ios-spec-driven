# Publishing to PyPI (Optional)

This guide shows how to publish the iOS Spec-Driven installer to PyPI for easier distribution.

## Prerequisites

1. **PyPI Account**: Create account at https://pypi.org/account/register/
2. **API Token**: Generate at https://pypi.org/manage/account/token/
3. **UV installed**: `brew install uv` or see https://docs.astral.sh/uv/

## Build Package

```bash
# Build distribution files
uv build

# This creates:
# - dist/ios_spec_driven_installer-2.1.0.tar.gz (source)
# - dist/ios_spec_driven_installer-2.1.0-py3-none-any.whl (wheel)
```

## Test Package Locally

```bash
# Install from local build
uv pip install dist/ios_spec_driven_installer-2.1.0-py3-none-any.whl

# Test commands
ios-spec-driven --help
ios-spec-driven info
ios-spec-driven install /tmp/test-project
```

## Publish to TestPyPI (Recommended First)

```bash
# Install twine
uv pip install twine

# Upload to TestPyPI
twine upload --repository testpypi dist/*

# Test installation from TestPyPI
uvx --from-index https://test.pypi.org/simple/ ios-spec-driven-installer info
```

## Publish to PyPI

```bash
# Upload to PyPI
twine upload dist/*

# Enter your PyPI credentials or API token when prompted
```

## After Publishing

Users can install via:

```bash
# Using uvx (recommended)
uvx ios-spec-driven-installer install

# Using pip
pip install ios-spec-driven-installer
ios-spec-driven install
```

## Update Version

When releasing new version:

1. Update version in `pyproject.toml`
2. Update version in `src/ios_spec_driven_installer/__init__.py`
3. Update version in `src/ios_spec_driven_installer/cli.py`
4. Commit changes
5. Create git tag: `git tag v2.1.0 && git push origin v2.1.0`
6. Build and publish: `uv build && twine upload dist/*`

## Benefits of PyPI Publishing

### Without PyPI (Current)
```bash
# Long command
uvx --from git+https://github.com/nguyennamkkb/ios-spec-driven-claude ios-spec-driven install
```

### With PyPI
```bash
# Short command
uvx ios-spec-driven-installer install
```

## Notes

- PyPI publishing is **optional** - GitHub installation works perfectly
- PyPI makes installation shorter and easier
- Consider publishing when toolkit is stable and widely used
- Keep GitHub as primary source of truth

## Troubleshooting

### Build Fails

```bash
# Check pyproject.toml syntax
uv build --verbose

# Ensure templates directory exists
ls -la src/ios_spec_driven_installer/templates/
```

### Upload Fails

```bash
# Check credentials
twine check dist/*

# Use API token instead of password
# Username: __token__
# Password: pypi-xxxxx...
```

### Installation Fails

```bash
# Check package on PyPI
pip show ios-spec-driven-installer

# Reinstall
pip uninstall ios-spec-driven-installer
pip install ios-spec-driven-installer --force-reinstall
```

---

*Last updated: February 5, 2026*
