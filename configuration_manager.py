test_settings = {'theme': 'dark', 'notifications': 'enabled', 'volume': 'high'}

def add_setting(dictionary, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()

    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    dictionary[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()

    if key in dictionary:
        dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    elif key not in dictionary:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary, key_value):
    key = key_value
    key = key.lower()

    if key in dictionary:
        dictionary.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"

def view_settings(dictionary):
    if not dictionary:
        return 'No settings available.'
    
    line = [f"{key.capitalize()}: {value}" for key, value in dictionary.items()]
    return 'Current User Settings:\n' + '\n'.join(line) + "\n"
    

print(view_settings(test_settings))

print(add_setting(test_settings, ('THEME', 'dark')))

print(add_setting(test_settings, ('volume', 'high')))

print(update_setting(test_settings, ('theme', 'dark')))

print(update_setting(test_settings, ('volume', 'high')))

print(delete_setting(test_settings, 'theme'))

print(view_settings({}))

print(view_settings(test_settings))