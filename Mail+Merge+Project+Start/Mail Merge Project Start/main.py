list_of_names = []
with open("./Input/Names/invited_names.txt") as names:
    for i in names:
        i = i.replace("\n", "")
        list_of_names.append(i)

with open("./Input/Letters/starting_letter.txt") as letter:
    content = letter.read()

for i in list_of_names:
    with open("./Output/ReadyToSend/letter_for_"+i+".txt", "w") as out:
        new_content = content.replace("[name]", i)
        out.write(new_content)


