# MVP: 
# starts off with asking user if they want to play easy mode or hard mode. easy mode allows for unlimited lives
# while hard mode gives user a max of 5 lives. if their lives are used up, program will be prompt stuff (introduced later)
# prompted to guess a number, when you guess some number, program will tell you if the number you chose is
# higher or lower than the number needed to be guessed, if you get it correct, the program will then prompt you
# to play again or ultimately end. 

# stuff i learned: 
# r"" will use the raw characters. will not process any escape sequences

def start_game():
    artwork = r"""

     _______               ___.                    ________                            .__                   ________                       
     \      \  __ __  _____\_ |__   ___________   /  _____/ __ __   ____   ______ _____|__| ____    ____    /  _____/_____    _____   ____  
     /   |   \|  |  \/     \| __ \_/ __ \_  __ \ /   \  ___|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\  /   \  ___\__  \  /     \_/ __ \ 
    /    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/ \    \_\  \  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  > \    \_\  \/ __ \|  Y Y  \  ___/ 
    \____|__  /____/|__|_|  /___  /\___  >__|     \______  /____/  \___  >____  >____  >__|___|  /\___  /   \______  (____  /__|_|  /\___  >
            \/            \/    \/     \/                \/            \/     \/     \/        \//_____/           \/     \/      \/     \/ 

"""
    print(artwork)
    print('Welcome to the number guessing game!')


def ask_difficulty(answer):
    match answer.lowercase().replace(" ",""):
        case 'e':
            return 
        case 'h':
            pass

start_game()
ask_difficulty(input('To start off- what difficulty do you want to play on? Easy [e] / Hard [h]'))