import getpass as gpass

with open("users.txt", 'r') as f:
    users = {}
    for line in f:
        username, password = line.strip().split(':')
        users[username] = password


while True:
    username = input('Username: ')

    if username in users:
        password = gpass.getpass('Password: ')
        while password != users[username]:
            print('Password Incorrect')
            password = gpass.getpass('Password: ')
    
        print(f'''
              Welcome {username}
              Press the enter key at anytime to exit
              ''')

        while True:
            application = input('''
            What do you want to do?

            1 TEST
            2 User List
            3 Add User
            4 Remove User

            ''')

            print('\n')

            if application == '':
                break
            
            elif application.lower() == 'test':
                for i in range(11):
                    print(f'Testing: {i}0%')
                print('Testing complete')

            elif application.lower() == 'user list':
                with open("users.txt", 'r') as f:
                    users = [line.strip().split(':') for line in f.readlines()]
                for user in users:
                    print('\n' + user[0])

            elif application.lower() == 'add user':
                def add_user():
                    username = input("Enter username: ")
                    password = input("Enter password: ")
                                
                    with open("users.txt", 'r') as file:
                        existing_users = [line.strip().split(':') for line in file]

                    for user in existing_users:
                        if user[0] == username:
                            print("Username already exists.")
                            return

                    with open("users.txt", 'a') as file:
                        file.write(f"{username}:{password}\n")

                    print("User added successfully.")

                add_user()

            elif application.lower() == 'remove user':
                username = input("Enter username to remove: ")
                
                with open("users.txt", 'r') as file:
                    existing_users = [line.strip().split(':') for line in file]

                found = False

                with open("users.txt", 'w') as file:
                    for user in existing_users:
                        if user[0] == username:
                            found = True
                        else:
                            file.write(f"{user[0]}:{user[1]}\n")

                if found:
                    print("User removed successfully.")
                else:
                    print("User not found.")

            else:
                print('Application not found')

        print('Exiting program')
        break

    else:
        print(username + ' is not found')
