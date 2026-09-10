lst=[1,2,3,5]

lst.clear()

print(lst)


from oops_proj import chatbook

user1=chatbook()
# print(user1.get_name())
# user1.set_name("Alice")
# print(user1.get_name())

# Using static method directly from class rather than obj
print(user1.id)
chatbook.set_id(10)

user2 = chatbook()
print(user2.id)

user3 = chatbook()
print(user3.id)