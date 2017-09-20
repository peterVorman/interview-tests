import decimal


def is_hashable(a):
    if hasattr(a, '__hash__') and a.__hash__ is not None:
        print("\tHashable.")
        return True
    print("\tNot Hashable")


def is_mutable(a):
    if not isinstance(a, tuple([int, float, decimal.Decimal, complex, bool, str, tuple, range, frozenset, bytes])):
        print("\tMutable.")
        return True
    print("\tImmutable")
    return False


def analyze_obj(a):
    print(a.__class__.__name__)
    is_hashable(a)
    is_mutable(a)


none_inst = None
bool_inst = True
int_inst = 1
complex_inst = complex(int_inst, int_inst)
float_inst = 1.1
decimal_inst = decimal.Decimal.from_float(float_inst)
str_inst = 'str'
bytes_inst = bytes(str_inst, 'utf-8')
bytearray_inst = bytearray(bytes_inst)
list_inst = ['a', 'b', 1, 1.1]
tuple_inst = tuple(list_inst)
set_inst = set(tuple_inst)
frozenset_inst = frozenset(str_inst)
range_inst = range(1, 1, 1)
object_inst = object()
dict_inst = {str_inst: int_inst}
code_inst = compile('a=q', filename='temp', mode='single')

analyze_obj(range_inst)
analyze_obj(bool_inst)
analyze_obj(complex_inst)
analyze_obj(int_inst)
analyze_obj(float_inst)
analyze_obj(str_inst)
analyze_obj(bytes_inst)
analyze_obj(decimal_inst)
analyze_obj(frozenset_inst)
analyze_obj(tuple_inst)
analyze_obj(object_inst)
analyze_obj(none_inst)
analyze_obj(analyze_obj)
analyze_obj(code_inst)
analyze_obj(list_inst)
analyze_obj(set_inst)
analyze_obj(bytearray_inst)
analyze_obj(dict_inst)
