def is_positive(value):
    return value >= 0


def has_required_fields(data, fields):
    return all(field in data for field in fields)
