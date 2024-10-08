Got it! Here’s the updated `README.md` reflecting the use of `Poetry` for dependency management:

```markdown
# datadoc-example

This repository provides a simple notebook example demonstrating how to use [SSB's datadoc-model](https://github.com/statisticsnorway/ssb-datadoc-model) for documenting Parquet files with metadata. The purpose of this example is to show how to generate and validate metadata for a Parquet dataset using the `pydantic`-based datadoc model.

## Features

- **SSB datadoc-model**: Demonstrates how to utilize the `datadoc-model` to generate JSON metadata for datasets.
- **Metadata generation**: Metadata includes details such as data types, roles (e.g., measures, identifiers), and descriptions.
- **Parquet file validation**: Demonstrates how to validate Parquet files against the generated metadata.
- **JSON export**: Exports metadata to JSON for further use or documentation.
- **Rich integration**: Displays the JSON metadata in a tree-like format using the `rich` library for better visualization in the console.

## Prerequisites

To run this example, you will need `Poetry` for dependency management.

### Installing Poetry

If you haven't installed `Poetry` yet, you can do so by following the instructions on the [Poetry documentation](https://python-poetry.org/docs/#installation).

Alternatively, you can install it using this command:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

## Usage

### 1. Clone the Repository

```bash
git clone https://github.com/trygu/datatoc-example.git
cd datadoc-example
```

### 2. Install Dependencies with Poetry

Once you're in the project directory, use `Poetry` to install all required dependencies:

```bash
poetry install
```

This will create a virtual environment and install all the dependencies specified in the `pyproject.toml` file.

### 3. Activate the Poetry Environment

To activate the virtual environment created by `Poetry`, run:

```bash
poetry shell
```

### 4. Run the Example

The notebook in this repository demonstrates how to generate metadata for a Parquet file and validate it. You can open and run the notebook in Jupyter:

```bash
jupyter notebook datadoc-example.ipynb
```

### 5. View the Generated Metadata

After running the notebook, it will generate a JSON file containing the metadata for the dataset. The JSON will also be printed in a tree-like structure in the console for easier visualization.

### Example Output

Here’s an example of the generated metadata in JSON format:

```json
{
    "document_version": "0.0.1",
    "datadoc": {
        "percentage_complete": 97,
        "document_version": "4.0.0",
        "dataset": {
            "short_name": "person_testdata_p2021-12-31_p2021-12-31",
            "assessment": "PROTECTED",
            "dataset_status": "INTERNAL",
            "dataset_state": "PROCESSED_DATA",
            "name": { ... },
            "variables": [ ... ]
        }
    }
}
```
