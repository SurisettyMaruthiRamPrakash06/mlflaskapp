a = "   abc   "
b = a.strip()
print(b)
c=b.lower()
d=b.upper()
print(c)
print(d)
e=["Hello","World"]
f=" + ".join(e)
print(f)
my_dict = {
    "key1": [1, 2, 3],
    "key2": ["a", "b", "c"],
    "key3": [True, False]
}
print(my_dict["key1"])
my_list = [42, "hello", 3.14, True]

print("Original list:", my_list)

my_list.append("new element")
print("After append:", my_list)

my_list.insert(2, {"key": "value"})
print("After insert:", my_list)

my_list.extend([False, 99, "extend"])
print("After extend:", my_list)
