import yaml
import json
import argparse
import sys

def fix_example(schema):
    if not isinstance(schema, dict):
        return schema

    keys = list(schema.keys())

    for key in keys:
        v = fix_example(schema[key])

        if key == "example":
            schema["examples"] = [v]
            del schema["example"]
    
    return schema


def oa2js(schema):
    """
    Convert an OpenAPI schema to JSON schema
    """

    # add schema key
    schema["$schema"] = "https://json-schema.org/draft/2020-12/schema"

    schema = fix_example(schema)

    return schema


def main():
    parser = argparse.ArgumentParser(
        description="Convert OpenAPI Specification components to JSON Schema"
    )
    parser.add_argument(
        "-o",
        "--output",
        help="output JSON Schema file",
        default="-",
        type=lambda output: sys.stdout if output == "-" else open(output, "w"),
    )
    parser.add_argument("oas", help="OpenAPI Specification (OAS) file")
    parser.add_argument("component", help="Name of component schema in OAS file")
    args = parser.parse_args()

    # load and read YAML
    with open(args.oas, "r") as f:
        oas = yaml.safe_load(f)

    # pull out the schema component
    component_schema = (
        oas.get("components", {}).get("schemas", {}).get(args.component, {})
    )

    json.dump(oa2js(component_schema), args.output)


if __name__ == "__main__":
    main()
