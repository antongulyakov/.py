a = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
print("a=", a)
for x in a:
    print(x, len(x))

print("b=")

c = a
print("c=", c)
for x in c[:]:
    if len(x) < 4:
        c.insert(0, x)
print("c=", c)

input()
