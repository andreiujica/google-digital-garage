word = "alphabet"
word_list = []
for item in word:
    if item != word[0] and item != word[-1]:
        word_list.append("_")
    else:
        word_list.append(item)
print(word_list)
print(" ".join(word_list))

count_nr = 1
already_checked = []
new_word = " ".join(word_list)
while count_nr <= 7:
    user_letter = input("Choose a letter: ").lower()
    if user_letter == "":
        print("No letter chosen. Please choose a letter")
        continue
    if user_letter in new_word:
        print("Letter is already on the screen")
    elif user_letter in already_checked:
        print(f"Letter has already been checked. Checked letters are: {' '.join(already_checked)}")
    else:
        if user_letter in word:
            print("Great! Letter is in the word")
            for iterator, value in enumerate(word):
                # print(f"{iterator} => {value}")
                if user_letter == value:
                    word_list[iterator] = user_letter
            new_word = " ".join(word_list)
            print(new_word)
        else:
            count_nr += 1
        if "_" not in "".join(word_list):
            print("You won")
            break
        elif count_nr > 7:
            print(f"You lost. Word was {word}")
        already_checked.append(user_letter)
print("nu gata")
