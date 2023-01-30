# movement-xsd
XML Schema defining the data required for a Movement Permit.

The repository follows the structure below:

- `movement_permit_schema.xsd`: The XML Schema;
- `example_valid_permit.xml`: Sample valid XML file to be used as testing data;
- `test-xsd.py`: Python script that runs validation using the provided schema and sample data;
- `requirements.txt`: Python dependencies needed to run the validation script.


## Testing against sample data
Testing the script can be done by running the `test-xsd.py` python script. This
script only requires that you have a [Python
3](https://www.python.org/downloads/) installed in your system.

With python installed, to test the validation, you can just run the following
commands.

Install dependencies:
``` sh
python -m venv .venv # create a virtual environment in the .venv folder
. .venv/bin/activate # activate the virtual environment
pip install -r requirements.txt # install de dependencies.
```

Run the test:
``` sh
python -m unittest
```

Running the command above should print "XML document is valid!!!" or a stack
trace informing an error in the validation.
