# 3.4 Guest List

guests = ['napoleon', 'augustus', 'hypatia']

print("Dear " + guests[0].title() + ", you are hereby invited to dinner.")
print("Dear " + guests[1].title() + ", you are hereby invited to dinner.")
print("Dear " + guests[2].title() + ", you are hereby invited to dinner.")

guest_declined = guests.pop(0)

print("Sorry to hear you can't make it,  " + guest_declined.title() + ".")

guests.insert(0, 'aurelius')

print("Dear " + guests[0].title() + ", you are hereby invited to dinner.")
print("Dear " + guests[1].title() + ", you are hereby invited to dinner.")
print("Dear " + guests[2].title() + ", you are hereby invited to dinner.")

print("Dear " + guests[0].title() + ", a bigger table has been found.")
print("Dear " + guests[1].title() + ", a bigger table has been found.")
print("Dear " + guests[2].title() + ", a bigger table has been found.")

guests.insert(0, 'peter I')
guests.insert(3, 'Lenin')
guests.append('Catherine II')
invitation = " you are hereby invited to dinner."


print("Dear " + guests[0].title() + invitation)
print("Dear " + guests[1].title() + invitation)
print("Dear " + guests[2].title() + invitation)
print("Dear " + guests[3].title() + invitation)
print("Dear " + guests[4].title() + invitation)
print("Dear " + guests[5].title() + invitation)

print("Apologies, but the new table will be late in arriving.")

guest_cancelled = guests.pop()
print("Apologies, " + guest_cancelled.title() + ", the invitation no longer stands")
guest_cancelled = guests.pop()
print("Apologies, " + guest_cancelled.title() + ", the invitation no longer stands")
guest_cancelled = guests.pop()
print("Apologies, " + guest_cancelled.title() + ", the invitation no longer stands")
guest_cancelled = guests.pop()
print("Apologies, " + guest_cancelled.title() + ", the invitation no longer stands")

print(guests)
