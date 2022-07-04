from random import randint

word_list = ["Brasil", "Japão", "China", "Canadá", "México", "Alemanha", "França", "Austrália"]
selected_word = word_list[randint(0, len(word_list) - 1)].upper()
print(f"A palavra selecionada tem {len(selected_word)} letras!")
print("Selecione a dificuldade: \n[1] Fácil \n[2] Médio \n[3] Difícil")
user_option = input("Digite uma opção válida: ")
while user_option != "1" and user_option != "2" and user_option != "3":
    print("Opção inválida!")
    user_option = input("Digite uma opção válida: ")
user_chances = 0
if user_option == "1":
    user_chances = len(selected_word) + 5
if user_option == "2":
    user_chances = len(selected_word) + 3
if user_option == "3":
    user_chances = len(selected_word)
user = []
user_mistakes = []
print(f"Lembre-se, você só pode errar {user_chances} vezes!")
while True:
    if set(user) == set(selected_word):
        break
    if user_chances == 0:
        break
    print(f"Você tem: {user_chances} chances!")
    user_option = input("Digite uma letra: ").upper()
    if user_option in selected_word:
        if user_option not in set(user):
            print("Você acertou!")
            user.append(user_option)
    else:
        print("Você errou!")
        user_mistakes.append(user_option)
        user_chances -= 1
    print(f"Letras acertadas: {user}")
    print(f"Letras erradas: {user_mistakes}")
if set(user) == set(selected_word):
    print(f"Parabéns, você venceu! A palavra era: {selected_word}")
else:
    print(f"Você perdeu! A palavra era: {selected_word}")
