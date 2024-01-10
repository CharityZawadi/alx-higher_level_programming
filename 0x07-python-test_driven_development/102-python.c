#include <Python.h>

/**
* print_python_string - Prints Python strings
* @p: PyObject string
*/
void print_python_string(PyObject *p)
{
	if (PyUnicode_Check(p))
	{
	printf("[.] string object info\n");
	printf("  type: compact unicode object\n");
	printf("  length: %ld\n", PyUnicode_GET_LENGTH(p));
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
	}
	else
	{
	PyErr_Print();
	fprintf(stderr, "[.] string object info\n");
	fprintf(stderr, "  [ERROR] Invalid String Object\n");
	}
}

