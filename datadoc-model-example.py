# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#   kernelspec:
#     display_name: datadoc-example
#     language: python
#     name: datadoc-example
# ---

# %%
# Import necessary modules
import json
from uuid import UUID, uuid4
from datetime import date
from datadoc_model.model import (
    MetadataContainer,
    DatadocMetadata,
    Dataset,
    DataSetStatus,
    DataSetState,
    Variable,
    DataType,
    VariableRole,
)

# Create an example of a MetadataContainer with some dummy data
metadata_container = MetadataContainer(
    datadoc=DatadocMetadata(
        document_version="4.0.0",
        dataset=Dataset(
            short_name="example_dataset",
            dataset_status=DataSetStatus.EXTERNAL,
            dataset_state=DataSetState.PROCESSED_DATA,
            version="1.0.0",
            id=uuid4(),  # This is a UUID, which needs to be converted to string for JSON
            contains_data_from=date(2023, 1, 1),
            contains_data_until=date(2024, 1, 1),
        )
    )
)

# Custom function to handle non-serializable types like UUID and date
def custom_encoder(obj):
    if isinstance(obj, UUID):
        return str(obj)
    if isinstance(obj, date):
        return obj.isoformat()
    return obj

# Convert the metadata container to a dictionary
metadata_dict = metadata_container.model_dump()

# Use the `json` module to convert the dictionary to a JSON string with indentation and the custom encoder
metadata_json = json.dumps(metadata_dict, indent=4, default=custom_encoder)

# Save the JSON string to a file
with open("person_testdata_p2021-12-31_p2021-12-31_v1__DOC.json", "w") as json_file:
    json_file.write(metadata_json)

print("Datadoc JSON file 'person_testdata_p2021-12-31_p2021-12-31_v1__DOC.json' created.")


# %%
