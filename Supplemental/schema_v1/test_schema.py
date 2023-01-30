import unittest

from xmlschema import XMLSchema
from xmlschema.validators import XMLSchemaValidationError

class TestSchema(unittest.TestCase):
    def test_schema(self):
        schema_file = "./src/movement_permit.xsd"
        example_file = "./examples/movement_permit_example.xml"

        try:
          schema = XMLSchema(schema_file)
          schema.validate(example_file)
          print(f"[OK] Schema {schema_file} validated test file {example_file}")
        except XMLSchemaValidationError as e:
          self.fail(f"exception while trying to validate {example_file} with {schema_file}: {e.reason}")

if __name__ == '__main__':
    unittest.main()
