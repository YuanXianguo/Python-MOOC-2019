current_users = ['daguo','bobo','luo','wu','deng']

new_users = ['daguo','ahang','bai','xiong']

for new_user in new_users:
    if new_user in current_users:
        print(new_user+"is already in current_users.")
    else:
        print("Add "+ new_user + " to current_users.")
    print("\nFinished adding !")
