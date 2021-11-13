users = ['val', 'bob', 'mia', 'ron', 'ned']

# getting the first element
first_user = users[0]
# getting the second element
second_user = users[1]
# getting the last elements
newest_user = users[-1]

print(users)
print(first_user)
print(second_user)
print(newest_user)

# changing an element
users[0] = 'valerie'
users[1] = 'robert'
users[-2] = 'ronald'

print(users)

# adding an element to the end of the list
users.append('amy')
print(users)

# starting with an empty list

users = []
users.append('amy')
users.append('val')
users.append('bob')
users.append('mia')

print(users)

# inserting elements at a particular position
users.insert(0, 'joe')
users.insert(3, 'bea')
print(users)

# deleting an element by its position
del users [-1]
print(users)

# removing an item by its value
users.remove('amy')
print(users)

# pop the last item from a list
most_recent_user = users.pop()
print(most_recent_user)

# pop the first item in a list
first_user = users.pop(0)
print(first_user)

# find the length of a list
num_users = len(users)
print(f"We have {num_users} users.")

# sorting a list permanently
users.sort()
print(users)

# sorting a list permanently in reverse alphabetical order
users.sort(reverse=True)
print(users)

# sorting a list temporarily
print(sorted(users))
print(sorted(users, reverse=True))

# reversing the order of a list
users.reverse()
print(users)

# print all items in a list
for user in users:
    print(user)

# printgin a message for each item, and a separate message afterwards
for user in users:
    print(f"\nWelcome, {user}!")
    print("We're so glad you joined!")

print("\nWelcome, we're glad to see you all!")


















































































