#include <stdio.h>
#include <Python.h>

void print_python_string(PyObject *p) {
    if (!PyUnicode_Check(p)) {
        fprintf(stderr, "[.] string object info\n");
        fprintf(stderr, "  [ERROR] Invalid String Object\n");
        return;
    }

    if (PyUnicode_IS_COMPACT_ASCII(p)) {
        fprintf(stderr, "[.] string object info\n");
        fprintf(stderr, "  type: compact ascii\n");
        fprintf(stderr, "  length: %ld\n", PyUnicode_GET_LENGTH(p));
        fprintf(stderr, "  value: %s\n", PyUnicode_AsUTF8(p));
    } else if (PyUnicode_IS_COMPACT(p)) {
        fprintf(stderr, "[.] string object info\n");
        fprintf(stderr, "  type: compact unicode object\n");
        fprintf(stderr, "  length: %ld\n", PyUnicode_GET_LENGTH(p));
        fprintf(stderr, "  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
    } else {
        fprintf(stderr, "[.] string object info\n");
        fprintf(stderr, "  [ERROR] Unknown String Object Type\n");
    }
}

