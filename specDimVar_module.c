/**
 * @Author: Paul Druce <pauldruce>
 * @Date:   2020-06-21T21:10:41+01:00
 * @Email:  pjdruce@gmail.com
 * @Last modified by:   pauldruce
 * @Last modified time: 2020-06-21T21:32:39+01:00
 */
 #define PY_SSIZE_T_CLEAN
 #include <Python.h>

static PyObject *
specDimVar(PyObject *self, PyObject *args)
{
    const char *command;
    int sts;

    if (!PyArg_ParseTuple(args, "s", &command))
        return NULL;
    sts = system(command);
    return PyLong_FromLong(sts);
}
