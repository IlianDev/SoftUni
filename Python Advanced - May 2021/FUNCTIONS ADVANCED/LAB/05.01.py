def get_info(**kwargs):
    return f"This is {kwargs.get('name')} f" \
           f"rom {kwargs.get('town')} and he " \
           f"is {kwargs.get('age')} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
# print(get_info(name="Test", town="Test town", age=20))
