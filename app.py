# Yusmida Arien

# Chapter 3.1 Introduction, no code
# Chapter 3.2 Conditional Statements
print("Chapter 3.2 Conditional Statements")
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")

else:
    print("It's cold")
print("Done")
print("*" * 30)

# Chapter 3.3 Ternary Operator
print("Chapter 3.3 Ternary Operator")
age = 12
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

cost = 300
status = "Eligible" if cost > 100 else "cheap"
print(status)
print("*" * 30)
