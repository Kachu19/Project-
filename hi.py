alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def cipher(user_text, user_direction, user_shift):
    final_word = ""
    # determine the direction
    if user_direction == "decode":
        user_shift *= -1
    for letter in user_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + user_shift
            final_word += alphabet[new_position]
        else:
            final_word += letter
    print(f"Here's the {user_direction}d {final_word}")




respond = False

while not respond:
    direction = input("Type encode to encrypt and decode to decrypt: ").lower()
    shift = int(input("Enter the number of shifts: "))
    word = input("Enter your word: ").lower()

    shift = shift % 26

    cipher(user_text=word, user_direction=direction, user_shift=shift)

    again = input("Do you want to continue, y-yes or n-no")

    if again == 'n':
        respond = True
        print("GOODBYE")