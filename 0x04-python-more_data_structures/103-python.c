#include <Python.h>

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "[.] bytes object info\n");
        fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    char *str = PyBytes_AsString(p);

    fprintf(stderr, "[.] bytes object info\n");
    fprintf(stderr, "  size: %ld\n", size);
    fprintf(stderr, "  trying string: %s\n", str);
    fprintf(stderr, "  first 10 bytes:");

    for (Py_ssize_t i = 0; i < size && i < 10; ++i) {
        fprintf(stderr, " %02x", str[i]);
    }

    fprintf(stderr, "\n");
}

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "[*] Python list info\n");
        fprintf(stderr, "[ERROR] Invalid Python List\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t allocated = ((PyListObject *)p)->allocated;

    fprintf(stderr, "[*] Python list info\n");
    fprintf(stderr, "[*] Size of the Python List = %ld\n", size);
    fprintf(stderr, "[*] Allocated = %ld\n", allocated);

    for (Py_ssize_t i = 0; i < size; ++i) {
        fprintf(stderr, "Element %ld: ", i);

        PyObject *element = PyList_GetItem(p, i);
        if (PyBytes_Check(element)) {
            print_python_bytes(element);
        } else if (PyLong_Check(element)) {
            fprintf(stderr, "int\n");
        } else if (PyFloat_Check(element)) {
            fprintf(stderr, "float\n");
        } else if (PyTuple_Check(element)) {
            fprintf(stderr, "tuple\n");
        } else if (PyList_Check(element)) {
            fprintf(stderr, "list\n");
        } else if (PyUnicode_Check(element)) {
            fprintf(stderr, "str\n");
        } else {
            fprintf(stderr, "[ERROR] Unknown type\n");
        }
    }
}
