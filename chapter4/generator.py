def doh2():
  yield "Homer: D'oh!"
  yield "Marge: A deer!"
  yield "Lisa: A female deer!"

for line in doh2():
  print(line)
  