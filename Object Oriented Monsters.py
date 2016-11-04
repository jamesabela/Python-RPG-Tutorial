import random

def number_of_monsters():
    with open('Monsters.txt') as f:
        return len(list(f))-2
        # Take off 2 because it starts at 0 and there is a title line

def validate_number():
    while True:
        MyNumber = input("Please enter a number: ")
        try:
            valid_number = int(MyNumber)
            if 0 < valid_number < 31:
                break
            else:
                print("please enter a number between 1 & 30")

        except ValueError:
            print("Please enter a number!")

    print("Number entered",valid_number)
    MyNumber=int(MyNumber)
    return MyNumber;


def main_game():
    print("Welcome!")
    enemy_monster = Monster()
    enemy_monster.read_monster(random.randint(0,number_of_monsters()))
    print("You see the enemy Monster!")
    if my_monster.Intelligence >  enemy_monster.Intelligence:
        enemy_monster.print_monster_card()
    else:
        enemy_monster.print_monster_basics()
    while True:
        action = input("A - attack, M - use magic")
        if action.upper() == "A":
            enemy_monster.Health = int(my_monster.Attack) - int(enemy_monster.Defence)
        elif action.upper() == "M":
            enemy_monster.Health = int(my_monster.Magical_Force) - int(enemy_monster.Magical_Defence)

        print("Your Monster's Health:",my_monster.Health)
        print("Enemy Monster's Health:",enemy_monster.Health)

        if int(enemy_monster.Health) <= 0:
            print("The enemy monster is finished")
            break


class Monster:
    def __init__(self):
        self.id = ""
        self.Name = ""
        self.Origin = ""
        self.Description = ""
        self.Attack = 0
        self.Magical_Force = 0
        self.Magical_Defence = 0
        self.Defence = 0
        self.Intelligence = 0
        self.Health = 0

    def read_monster(self,monster_id):
        with open('Monsters.txt') as f:
            for line in f:
                parts = line.split(",")
                if str(monster_id) == parts[0]:
                    self.id = parts[0]
                    self.Name = parts [1]
                    self.Origin = parts [2]
                    self.Description = parts [3]
                    self.Attack = parts [4]
                    self.Magical_Force = parts [5]
                    self.Magical_Defence = parts [6]
                    self.Defence = parts [7]
                    self.Intelligence = parts [8]
                    self.Health = parts [9]
                    break

    def input_monster(self):
        self.Name = input("What is the monster's name?")
        self.Origin = input("Where did the monster come from?")
        self.Description = input("Describe the monster: ")
        print("Attack Force")
        self.Attack = validate_number()
        print("Magical Force")
        self.Magical_Force = validate_number()
        print("Magical Defence")
        self.Magical_Defence = validate_number()
        print("Defence")
        self.Defence = validate_number()
        print("Intelligence")
        self.Intelligence = validate_number()
        print("Health")
        self.Health = validate_number()

    def print_monster_card(self):
        print("Monster Card ID: ",self.id)
        print("\nName:            ", self.Name)
        print("Origin:          ",self.Origin)
        print("Description:     ",self.Description)
        print("\nAttack Force:    ",self.Attack)
        print("Magical Force:   ",self.Magical_Force)
        print("Magical Defence: ",self.Magical_Defence)
        print("Defence:         ",self.Defence)
        print("Intelligence:    ",self.Intelligence)
        print("Health:          ",self.Health)

    def print_monster_basics(self):
        print("Monster Card ID: ",self.id)
        print("\nName:            ", self.Name)
        print("Origin:          ",self.Origin)
        print("Description:     ",self.Description)

    def add_monster_to_file(self):
        lineadd=("%d,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (number_of_monsters()+1,self.Name,self.Origin,self.Description,self.Attack,self.Magical_Force,self.Magical_Defence,self.Defence,self.Intelligence,self.Health))
        print(lineadd)
        check = input("Do you want to add this to the file? (y/n)")
        if check in ["y","Y","yes"]:
            print("writing")
            with open("Monsters.txt", "a") as f:
                f.write("\n"+lineadd)

my_monster = Monster()

#Menu Loop

while True:
    print("Monster Management \n")
    print("1 - Input a Monster")
    print("2 - Add your Monster to file")
    print("3 - Choose a Random Monster")
    print("4 Display My Monster")
    print("5 - Play a Game")
    print("6 - Quick start with random monster")
    choice = input("Make your choice: ")

    if choice == "1":
        my_monster.input_monster()
    elif choice == "2":
        my_monster.add_monster_to_file()
    elif choice == "3":
        my_monster.read_monster(random.randint(0,number_of_monsters()))
        my_monster.print_monster_card()
    elif choice == "4":
        my_monster.print_monster_card()
    elif choice == "5":
        my_monster.print_monster_card()
        check = input("Do you want to play with this character? (y/n)")
        if check in ["y","Y","yes"]:
            main_game()
    elif choice =="6":
        my_monster.read_monster(random.randint(0,number_of_monsters()))
        my_monster.print_monster_card()
        main_game()

    else:
        break

