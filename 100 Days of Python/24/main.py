PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as in_names:
    names = in_names.readlines()


with open("./Input/Letters/starting_letter.txt") as letters:
    letter_con = letters.read()
    for name in names:
         stripped = name.strip()
         new =  letter_con.replace(PLACEHOLDER, name)
         with open(f"./Output/ReadyToSend/letter_for_{stripped}.txt",mode="w") as completed:
             completed.write(new)
