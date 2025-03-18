import re

def validate_data(data_dict):
    errors = []
    validated_data = {}

    for key, value in data_dict.items():
        value = value.strip()

        if key in ["fname", "lname"]:
            pattern = r"^[A-Z][a-z]{2,}$"  # Name should start with a capital letter and have at least 2 lowercase letters
            if not re.fullmatch(pattern, value):
                errors.append(f"{key.replace('_', ' ').title()} must start with a capital letter and have at least 2 lowercase letters.")

        elif key == "phonenum":
            pattern = r"^\d{10}$"  # Phone number must be exactly 10 digits
            if not re.fullmatch(pattern, value):
                errors.append("Phone number must be exactly 10 digits.")

        elif key == "email":
            pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"  # Email format validation
            if not re.fullmatch(pattern, value):
                errors.append("Invalid email format.")

        elif key == "zip_code":
            pattern = r"^\d{5,6}$"  # ZIP Code should be 5 or 6 digits
            if not re.fullmatch(pattern, value):
                errors.append("ZIP Code must be 5 or 6 digits.")

        validated_data[key] = value  # Store the valid data

    if errors:
        raise ValueError("\n".join(errors))  

    return validated_data
