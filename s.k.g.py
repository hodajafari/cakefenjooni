import random
user_score=0
pc_score=0
run = True
options=["s","k","gh"]
while run:
    print("s:sang, k:kaghaz, gh:gheychi")
    user_choice = input("lotfan az mavarede fogh yeki ra entekhab konid:\n")
    if user_choice in options:
        pc_choice = random.choice(options)
        print(f"pc choice is {pc_choice}")
        if pc_choice == user_choice:
            print("mosavi , ye bare dg test kon")
        elif user_choice == "s":
            if pc_choice == "k":
                pc_score+=1
            else:
                user_score+=1
        elif user_choice == "k":
            if pc_choice == "gh":
                pc_score+=1
            else:
                user_score+=1
        elif user_choice == "gh":
            if pc_choice == "s":
                pc_score+=1
            else:
                user_score+=1

        if user_score == 3 or pc_score == 3:
            if pc_score == 3:
                print("PC bord")
            else:
                print("USER bord")
            run = False
        else:
            print(f"user score is {user_score} and pc score is {pc_score} => berim daste bad")
    else:
        print("Error--->wrong choice , lotfan az bein gozineha entekhab konid:\n")


