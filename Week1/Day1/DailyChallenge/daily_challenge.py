user_input = input("Input exactly 10 character\n")
build_text = ""
if len(user_input) < 10:
    print("String not long enough")
elif len(user_input) > 10:
    print("String too long")
else:
    print("Perfect string")
    print(f'{user_input[0]} {user_input[-1]}')
    for character in user_input:
        build_text += character
        print(build_text)
        
