### Hexlet tests and linter status:
[![Actions Status](https://github.com/SemYakovlev/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/SemYakovlev/python-project-50/actions)  [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=SemYakovlev_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=SemYakovlev_python-project-50) [![build_50.yml](https://github.com/SemYakovlev/python-project-50/actions/workflows/build_50.yml/badge.svg)](https://github.com/SemYakovlev/python-project-50/actions/workflows/build_50.yml)


# Gendiff

**Gendiff** is a command-line utility that compares two configuration files and displays the differences between them.

The utility supports JSON and YAML files, including nested structures, and provides three output formats.

## Features

- Compare two JSON or YAML files.
- Detect added, removed, and modified values.
- Compare nested structures.
- Display differences in three formats: `stylish`, `plain`, and `json`.

## Output formats

### Stylish

Displays differences in a structured, readable format. Added and removed keys are marked with `+` and `-`.

### Plain

Displays changes as text descriptions. Unchanged nested structures are represented as `[complex value]` when describing changes to their contents.

### JSON

Displays the difference as JSON data.

## Requirements

- Python 3.12 or later
- [uv](https://docs.astral.sh/uv/)
- Git

## Installation

Clone the repository and navigate to the project directory:

```bash
git clone https://github.com/SemYakovlev/python-project-50.git
cd python-project-50
```

Install dependencies and build the package:

```bash
uv sync
make build
make package-install
```

[![asciicast](https://asciinema.org/a/Lgg6jRcn8qeot5sK.svg)](https://asciinema.org/a/Lgg6jRcn8qeot5sK)

[![asciicast](https://asciinema.org/a/bYilt4haVrXEqcSt.svg)](https://asciinema.org/a/bYilt4haVrXEqcSt)

[![asciicast](https://asciinema.org/a/kgAfs5imYPs2Bt6k.svg)](https://asciinema.org/a/kgAfs5imYPs2Bt6k)

[![asciicast](https://asciinema.org/a/WefcnpSmI9fJmREp.svg)](https://asciinema.org/a/WefcnpSmI9fJmREp)
