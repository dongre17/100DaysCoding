
invite_name_list = []

with open("Data/Names/invite_names.txt", mode='r') as invite_names:
    for name in invite_names:
        invite_name_list.append(name)

with open("Data/Letters/letter.txt", mode='r') as letter:
    content = letter.read()

    for name in invite_name_list:
        with open(f"Output/ReadyToSend/{name.strip()}.txt", mode='w') as file:
            letter_content = content.replace('{name}', name)
            file.write(letter_content)
