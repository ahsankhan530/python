current_users=['Ahsan','KASHIF','jawad','abbas','daim']
new_users=[str(input())]
for new_user in new_users :
    if new_user in current_users  :
        print(new_user,"is available")
    else:
        print(new_user,"is not available")
