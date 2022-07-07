from xmlschema import XMLSchema11


def main():
    schema = XMLSchema11("movement_permit_schema.xsd")
    # Will trow an exception if not valid
    schema.validate("example_valid_permit.xml")
    print("XML document is valid!!!")


if __name__ == '__main__':
   main()
