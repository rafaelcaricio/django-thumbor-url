all:
	@PYTHONPATH=$$PYTHONPATH:.:tests/testproj nosetests tests/
