# Storing Dictionaries in a list
users = []

new_user = {"first_name": "Samrat", "last_name": "Som", "username": "samgegr8"}
users.append(new_user)

new_user = {"first_name": "Amrita", "last_name": "Shome", "username": "shomeamrita"}
users.append(new_user)

# Show all users of Each User

for user_dict in users:
    for k, v in user_dict.items():
        print(f"{k},{v}")

# Storing list in a dictionary
fav_languages = {"Jen": ["python", "ruby", "c"], "Sam": ["python", "c", "Java"]}

for name, key in fav_languages.items():
    print(f"{name} loves ::", end="")
    keycount = len(key)
    count = 1
    for key_list in key:
        if count < keycount:
            print(f" {key_list} ", end="")
        else:
            print(f"{key_list}")
        count = count + 1
