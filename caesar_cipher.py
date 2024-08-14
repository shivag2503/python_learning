alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

flag = True


def caesar(action, original_text, shift_amount):
    output = ""
    if action == "encode":
        for i in original_text:
            if i not in alphabet:
                output += i
            else:
                val = alphabet.index(i) + shift_amount
                val %= len(alphabet)
                output += alphabet[val]
    else:
        for i in original_text:
            if i not in alphabet:
                output += i
            else:
                val = alphabet.index(i) - shift_amount
                output += alphabet[val]
    print(f"Here is the {direction}d result is: {output}")


while flag:
    direction = input("Type 'encode' for encrypt, type 'decode' for decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    choice = input("Do you want to use cypher again? Type 'yes' else type 'no'..\n").lower()
    if choice == 'no':
        flag = False
