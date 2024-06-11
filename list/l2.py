#excersise 3.4
guest_list = ["ragnar","ubbe","lagartha","ivar"]

print(f"hello {guest_list[0]} u r invited fr dinner ")
print(f"hello {guest_list[1]} u r invited fr dinner ")
print(f"hello {guest_list[2]} u r invited fr dinner ")
print(f"hello {guest_list[3]} u r invited fr dinner ")
not_coming = guest_list.pop()
print(f"sedly {not_coming} can't join us fr dinner")
print(guest_list)
guest_list.append("sigurd")
print(f"hello {guest_list[0]} u r invited fr dinner ")
print(f"hello {guest_list[1]} u r invited fr dinner ")
print(f"hello {guest_list[2]} u r invited fr dinner ")
print(f"hello {guest_list[3]} u r invited fr dinner ")

print("-----found a bigger table now more guest can be invited------")

guest_list.insert(0,"odin")
guest_list.insert(2,"thor")
guest_list.append("habard")

print(f"hello {guest_list[0]} u r invited fr dinner ")
print(f"hello {guest_list[1]} u r invited fr dinner ")
print(f"hello {guest_list[2]} u r invited fr dinner ")
print(f"hello {guest_list[3]} u r invited fr dinner ")
print(f"hello {guest_list[4]} u r invited fr dinner ")
print(f"hello {guest_list[5]} u r invited fr dinner ")
print(f"hello {guest_list[6]} u r invited fr dinner ")

#shrinking guest list 

print("----sry the bigger table could not be arranged on time so now only 2 person can join fr dinner----")
print(f"sry {guest_list.pop()} u r not invited fr dinner !!")
print(f"sry {guest_list.pop()} u r not invited fr dinner !!")
print(f"sry {guest_list.pop()} u r not invited fr dinner !!")
print(f"sry {guest_list.pop()} u r not invited fr dinner !!")
print(f"sry {guest_list.pop()} u r not invited fr dinner !!")
print(f"{guest_list[0]} u r still invited !!")
print(f"{guest_list[1]} u r still invited !!")
del guest_list[0]
del guest_list[0]

print(guest_list)

