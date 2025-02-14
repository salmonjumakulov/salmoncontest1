
def typeBasedTransformer(**kwargs):

    transformed = {}
    for key, value in kwargs.items():
        if isinstance(value, (int, float)):
            transformed[key] = value ** 2
        elif isinstance(value, str):
            transformed[key] = value[::-1]
        elif isinstance(value, bool):
            transformed[key] = not value
        elif isinstance(value, (list, tuple)):
            transformed[key] = value[::-1]
        elif isinstance(value, dict):
            transformed[key] = {v: k for k, v in value.items()}
        else:
            transformed[key] = value  # Unsupported types remain unchanged
    return transformed
