integer_value = 10
float_value = 10.5
string_value = "Python"
boolean_value = True
list_value = [1, 2, 3]
tuple_value = (1, 2, 3)
set_value = {1, 2, 3}
dictionary_value = {"name": "Alex"}

for value in (integer_value, float_value, string_value, boolean_value,
              list_value, tuple_value, set_value, dictionary_value):
    print(value, "->", type(value))
