from enum import Enum

class state(Enum):
    ACTIVE = 1
    INACTIVE = 0

print(state.ACTIVE.value)
print(state.INACTIVE.value)
print(list(state))

age = input("what is ur age ?")
print("ur age is "  + age)