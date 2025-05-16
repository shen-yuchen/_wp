def dict_to_string(d):
parts = []
for key in d:
parts.append(f"{key}:{d[key]}")
return ', '.join(parts)
print(dict_to_string({'a': 1, 'b': 2}))
