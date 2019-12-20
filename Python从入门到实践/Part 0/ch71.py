responses = {}

poll_active = True
while poll_active:
    name = input("\nWhat is your name?")
    response = input("which mountain do you want to climb?")

    responses[name] = response

    new_name = input("Would you like another people to poll?(yes/no)")
    if new_name == 'no':
        poll_active = False

print("\n----The result of poll----")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + ".")
