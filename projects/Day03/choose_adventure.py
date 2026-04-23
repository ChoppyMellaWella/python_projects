# Notes:
    # got to play with strings and ascii art.
# Stuff I learned:
    # string.lower()
    # string.strip()
    # using match:case
    # using lists [] mutable and ordered. can have duplicates
    # using dictionaries {} key:value

# this took some time to do but it worked.
# 2nd thing. had to double escape sequence for these guys '\' anytime ther was a '\',
# i had to '\\'
def print_title():
    print(
        "   __ _                    _       _                 _                  \n"\
        "  / /(_)_ __  _   ___  __ /_\\   __| |_   _____ _ __ | |_ _   _ _ __ ___ \n"\
        " / / | | '_ \\| | | \\ \\/ ///_\\\\ / _` \\ \\ / / _ \\ '_ \\| __| | | | '__/ _ \\ \n"\
        "/ /__| | | | | |_| |>  </  _  \\ (_| |\\ V /  __/ | | | |_| |_| | | |  __/ \n"\
        "\\____/_|_| |_|\\__,_/_/\\_\\_/ \\_/\\__,_| \\_/ \\___|_| |_|\\__|\\__,_|_|  \\___|\n\n"
    )

print_title()

print("Welcome to the Linux Adventure! This is a sort of linux \"simulation\"" \
" Try see what you can and can\'t do!\n")
print('NOTE: If you want to end the program, just type \'exit\'. And if you want help type \'help\'\n')

# says whether or not to send the stuff
can_continue = True

# terminal prompt
terminal_prompt = 'sysadmin@sysadmin:'
# initial directory
directory = '~$ '
# folder contents in home
document_folder_contents = ["[Parent Folder]", "[Current Folder]"]
apps_folder_contents = ["[Parent Folder]", "[Current Folder]"]
pictures_folder_contents = ["[Parent Folder]", "[Current Folder]"]

# folders in home
document_folder = {"Documents": document_folder_contents}
apps_folder = {"Applications": apps_folder_contents}
pictures_folder = {"Pictures": pictures_folder_contents}

# initial directories in home
home_directories = [document_folder, apps_folder, pictures_folder]

# okay commands to use
valid_commands = [
    {'exit': "Ends the program"},
    {'ifconfig': "Prints current network config"},
    {'linuxart': "Reprints Linux Adventure title screen"},
    {'ls': "Prints out what\'s in some directory"},
    {'pwd': "Prints the current working directory"},
    {'help': "Gives a list of commands and their function"}
]

def get_help(valid_commands):
    for command_info in valid_commands:
        for key, value in command_info.items():
            print(f"{key}: {value}")
        

# keeps going until not_end is false
while (can_continue):
    user_option = input(terminal_prompt+directory)

    match user_option.strip().lower():
        case 'exit':
            can_continue = False
        case 'ls':
            print(f"{home_directories}")
        case 'pwd':
            print('/home/sysadmin')
        case 'ifconfig':
            print('IP: 192.168.12.23/24 DG: 192.168.12.1/24')
        case 'linuxart':
            print_title()
        case 'help':
            get_help(valid_commands)
        case _: # this _: is the default case. if nothing matches, this case is run
            print(f"bash: {user_option}: command not found")