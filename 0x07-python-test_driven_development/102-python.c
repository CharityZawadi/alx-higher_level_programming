#define PY_SSIZE_T_CLEAN
#include <Python.h>

/**
 * print_python_string - Prints Python string information
 * @p: PyObject string
 */
void print_python_string(PyObject *p)
{
    Py_ssize_t length;
    Py_ssize_t i;
    wchar_t *unicode_str;

    printf("[.] string object info\n");

    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    length = PyUnicode_GET_LENGTH(p);
    unicode_str = PyUnicode_AsWideCharString(p, NULL);

    printf("  type: compact %s\n", PyUnicode_IS_COMPACT_ASCII(p) ? "ascii" : "unicode object");
    printf("  length: %ld\n", length);
    printf("  value: %ls\n", unicode_str);

    PyMem_Free(unicode_str);

    /* Print address information of each character in unicode string */
    if (PyUnicode_IS_COMPACT_ASCII(p))
    {
        for (i = 0; i < length; i++)
        {
            printf("  character %ld: %c\n", i, PyUnicode_READ_COMPACT_DATA(p, i));
        }
    }
    else
    {
        for (i = 0; i < length; i++)
        {
            printf("  character %ld: U+%04x\n", i, PyUnicode_READ_COMPACT_DATA(p, i));
        }
    }
}

