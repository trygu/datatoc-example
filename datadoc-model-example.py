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

# %% [markdown]
# # Simple example using ssb-datadoc-model to create a datadoc json document

# %%
import json
from uuid import UUID
from datetime import datetime, date
import pytz
from rich.tree import Tree
from rich import print as rich_print
from rich.json import JSON as RichJSON
from pydantic import AnyUrl
from datadoc_model.model import (
    MetadataContainer,
    DatadocMetadata,
    Dataset,
    DataSetStatus,
    DataSetState,
    Variable,
    DataType,
    VariableRole,
    LanguageStringTypeItem,
    LanguageStringType
)


# %%
# Custom JSON encoder to handle UUIDs, datetime, date, and Url objects
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, date):
            return obj.isoformat()  # Convert date to ISO format (YYYY-MM-DD)
        if isinstance(obj, AnyUrl):
            return str(obj)  # Convert URL to string
        return super().default(obj)

# Set timezone to UTC
utc = pytz.UTC

# %%
# Step 1: Define metadata for the Parquet file using the MetadataContainer
metadata_container = MetadataContainer(
    document_version="0.0.1",
    datadoc=DatadocMetadata(
        percentage_complete=97,
        document_version="4.0.0",  # Updated to the expected value
        dataset=Dataset(
            short_name="person_testdata_p2021-12-31_p2021-12-31",
            assessment="PROTECTED",
            dataset_status=DataSetStatus.INTERNAL,
            dataset_state=DataSetState.PROCESSED_DATA,
            name=LanguageStringType(root=[
                LanguageStringTypeItem(languageCode="nb", languageText="Persondata demo datasett"),
                LanguageStringTypeItem(languageCode="nn", languageText=""),
                LanguageStringTypeItem(languageCode="en", languageText="")
            ]),
            description=LanguageStringType(root=[
                LanguageStringTypeItem(languageCode="nb", languageText="Person-data til demo og testing av DataDoc"),
                LanguageStringTypeItem(languageCode="nn", languageText=""),
                LanguageStringTypeItem(languageCode="en", languageText="")
            ]),
            population_description=LanguageStringType(root=[
                LanguageStringTypeItem(languageCode="nb", languageText="Alle bosatte i Norge"),
                LanguageStringTypeItem(languageCode="nn", languageText=""),
                LanguageStringTypeItem(languageCode="en", languageText="")
            ]),
            version="1",
            version_description=LanguageStringType(root=[
                LanguageStringTypeItem(languageCode="nb", languageText="Opprettelse"),
                LanguageStringTypeItem(languageCode="nn", languageText=""),
                LanguageStringTypeItem(languageCode="en", languageText="")
            ]),
            unit_type="PERSON",
            temporality_type="STATUS",
            subject_field="befolkning",  # Should be a string, not a LanguageStringType
            keyword=["befolkning", "skatt"],
            spatial_coverage_description=LanguageStringType(root=[
                LanguageStringTypeItem(languageCode="nb", languageText="Norge"),
                LanguageStringTypeItem(languageCode="nn", languageText=""),
                LanguageStringTypeItem(languageCode="en", languageText="")
            ]),
            id=UUID("2f72477a-f051-43ee-bf8b-0d8f47b5e0a7"),
            owner="722",
            metadata_created_date=utc.localize(datetime(2022, 10, 7, 7, 35, 1)),  # Add timezone info
            metadata_created_by="default_user@ssb.no",
            metadata_last_updated_date=utc.localize(datetime(2024, 1, 8, 15, 49, 17, 489872)),  # Add timezone info
            metadata_last_updated_by="default_user@ssb.no",
            contains_data_from=date(2021, 12, 31),  # Ensure it's a date object
            contains_data_until=date(2021, 12, 31)   # Ensure it's a date object
        ),
        variables=[
            Variable(
                short_name="fnr",
                name=LanguageStringType(root=[
                    LanguageStringTypeItem(languageCode="nb", languageText="Fødselsnummer"),
                    LanguageStringTypeItem(languageCode="nn", languageText=""),
                    LanguageStringTypeItem(languageCode="en", languageText="Personal number")
                ]),
                data_type=DataType.STRING,
                variable_role=VariableRole.IDENTIFIER,
                definition_uri="https://www.ssb.no/a/metadata/conceptvariable/vardok/26/nb"
            ),
            Variable(
                short_name="sivilstand",
                name=LanguageStringType(root=[
                    LanguageStringTypeItem(languageCode="nb", languageText="Sivilstand"),
                    LanguageStringTypeItem(languageCode="nn", languageText=""),
                    LanguageStringTypeItem(languageCode="en", languageText="Marital status")
                ]),
                data_type=DataType.STRING,
                variable_role=VariableRole.MEASURE,
                definition_uri="https://www.ssb.no/a/metadata/conceptvariable/vardok/91/nb"
            ),
            Variable(
                short_name="bostedskommune",
                name=LanguageStringType(root=[
                    LanguageStringTypeItem(languageCode="nb", languageText="Bostedskommune"),
                    LanguageStringTypeItem(languageCode="nn", languageText=""),
                    LanguageStringTypeItem(languageCode="en", languageText="Residential district")
                ]),
                data_type=DataType.STRING,
                variable_role=VariableRole.MEASURE,
                definition_uri="https://www.ssb.no/a/metadata/conceptvariable/vardok/94/nb"
            ),
            Variable(
                short_name="inntekt",
                name=LanguageStringType(root=[
                    LanguageStringTypeItem(languageCode="nb", languageText="Alminnelig inntekt"),
                    LanguageStringTypeItem(languageCode="nn", languageText=""),
                    LanguageStringTypeItem(languageCode="en", languageText="Income")
                ]),
                data_type=DataType.INTEGER,
                variable_role=VariableRole.MEASURE,
                definition_uri="https://www.ssb.no/a/metadata/conceptvariable/vardok/3495/nb",
                measurement_unit="NOK"
            ),
            Variable(
                short_name="bankinnskudd",
                name=LanguageStringType(root=[
                    LanguageStringTypeItem(languageCode="nb", languageText="Bankinnskudd totalt"),
                    LanguageStringTypeItem(languageCode="nn", languageText=""),
                    LanguageStringTypeItem(languageCode="en", languageText="Bank transfer (total)")
                ]),
                data_type=DataType.INTEGER,
                variable_role=VariableRole.MEASURE,
                definition_uri="https://www.ssb.no/a/metadata/conceptvariable/vardok/591/nb",
                measurement_unit="NOK"
            ),
            Variable(
                short_name="dato",
                name=LanguageStringType(root=[
                    LanguageStringTypeItem(languageCode="nb", languageText="Registreringsdato"),
                    LanguageStringTypeItem(languageCode="nn", languageText=""),
                    LanguageStringTypeItem(languageCode="en", languageText="Date of registration")
                ]),
                data_type=DataType.DATETIME,
                variable_role=VariableRole.START_TIME,
                comment=LanguageStringType(root=[
                    LanguageStringTypeItem(languageCode="nb", languageText="Måletidspunkt for data"),
                    LanguageStringTypeItem(languageCode="nn", languageText=""),
                    LanguageStringTypeItem(languageCode="en", languageText="")
                ]),
                format="YYYY-MM-DD"
            )
        ]
    )
)

# %%
# Step 2: Use model_dump to get a dictionary and convert to JSON
metadata_dict = metadata_container.model_dump()

# %%
# Write the JSON file using the Dataset short_name
dataset_short_name = metadata_container.datadoc.dataset.short_name
filename = f"{dataset_short_name}_v1__DOC.json"

# Optionally, you can export this metadata to JSON for documentation
metadata_json = json.dumps(metadata_dict, indent=4, cls=CustomJSONEncoder)

# Write to file
with open(filename, "w") as json_file:
    json_file.write(metadata_json)

# %%
# Step 3: Display JSON as a tree
rich_json = RichJSON(metadata_json)
rich_print(rich_json)

print(f"Metadata JSON file '{filename}' created.")

# %%
