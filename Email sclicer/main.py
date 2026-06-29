# Email slicer

email = input("Enter your email: ")

index = email.index("@")
                                #index - It finds the position of a character inside a string.
username = email[:index]
domain = email[index + 1:]

print(f"Your username is {username} and domain is {domain}")

# OR

'''email = input("Enter your email: ")

username = email[:email.index("@")]
domain = email[email.index("@") + 1:]
print(f"Your username is {username} and domain is {domain}")'''