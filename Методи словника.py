from copy import deepcopy
from os.path import exists

#our_dict = {"key_1":"value_1", "key_2":"value_2", "key_3":"value_3", "key_9": [1, 2, 3]}
# # print(our_dict["key_4"])
# print(our_dict.get("key_1"))
# print(our_dict.get("key_4", 'key not exists'))
# print(our_dict)
#
#
# print("last line")
# print(our_dict.setdefault("key_5", "value_6"))
# print(our_dict.setdefault("key_5", "value_5"))
#
# our_dict["key_1"] = "value_6"
# our_dict["key_6"] = "value_6"
#
# our_dict.update({"key_1": "value_7"})
# our_dict.update({"key_8": "value_8"})
#
# del our_dict["key_8"]
# print(our_dict.pop("key_6"))
# print(our_dict)
#
# our_dict.popitem()
# print(our_dict)
#
# our_dict.clear()
# print("->", our_dict)
# from  copy import deepcopy
#
# our_dict_2=deepcopy(our_dict)
# our_dict_2.update({"key_10": "value_10"})
# our_dict_2["key_9"].append("11")
# print(our_dict)
# print(our_dict_2)

# for values in our_dict.values():
#     print(values)
#
# for keys in our_dict.keys():
#     print(keys)

# for key, value in our_dict.items():
#     print(key)
#     print(value)

# d = { 'name': 'John Doe',  'age': 30, 'city': 'New York', 'email': 'johndoe@example.com'}
# key_to_delete=input("Enter key you want to delete: ")
# if key_to_delete in d:
#     del d[key_to_delete]
#     print(f"Key '{key_to_delete}' successfully deleted")
# print(d)

# d = {'name': 'Alice Smith', 'age': 25, 'city': 'Los Angeles',
#      'email': 'alice.smith@example.com',
#      'favorite_subjects': ['Mathematics', 'History', 'Literature']}
# for subjects in d['favorite_subjects']:
#     print(subjects)

favorites = {
    'movies': ['Interstellar', 'Fast & Furious', 'Pirates of the Caribbean'],
    'music': ['Queen', 'The Beatles', 'Coldplay'],
    'sports': ['football', 'basketball', 'tennis']}
del favorites['sports']
favorites.update({"serials": "APL"})
print(favorites)
