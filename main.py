import modules
print()
rep = "y"
while not "n" in rep:
  choice = input("how would you like to run (1: file 2: paste) ")
  if "1" in choice:
    fi = (input("file to execute: "))
    exec(open(fi).read())
  elif "2" in choice:
    print("paste code here:")
    exec(input())
  else:
    print()
  rep = input("Continue running programs? y/n ")