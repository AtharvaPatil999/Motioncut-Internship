import random

def generate_username(adj, nouns, numbers=False, special_char=False):
    adj = random.choice(adj)
    noun = random.choice(nouns)
    username = f"{adj}{noun}"

    if numbers:
        username += str(random.randint(0, 9))

    if special_char:
        special_characters = "!@#$%^&*?"
        username += random.choice(special_characters)

    # Ensure username length is greater than 7
    while len(username) <= 7:
        username += random.choice('abcdefghijklmnopqrstuvwxyz')

    return username

def generate_and_save_usernames(adjectives, nouns, num_usernames, include_numbers=False, include_special_chars=False, filename="E:/Motioncut Internship/usernames.txt"):
    usernames = [
        generate_username(adjectives, nouns, numbers=include_numbers, special_char=include_special_chars)
        for _ in range(num_usernames)
    ]

    
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")

    return usernames

def get_user_input(prompt):
   
    while True:
        user_input = input(prompt).lower()
        if user_input in ['yes', 'no']:
            return user_input == 'yes'
        else:
            print("Please enter either 'yes' or 'no'.")


adjectives = ["Cool", "Happy", "Smart", "Brave", "Funny", "Amazing"]
nouns = ["Tiger", "Dragon", "Eagle", "Wolf", "Shark", "Lion"]

num_usernames = int(input("How many usernames would you like to generate? "))


include_numbers = get_user_input("Include numbers? (yes/no): ")
include_special_chars = get_user_input("Include special characters? (yes/no): ")

usernames = generate_and_save_usernames(adjectives, nouns, num_usernames, include_numbers, include_special_chars)

print("\nGenerated usernames:")
print("\n".join(usernames))
