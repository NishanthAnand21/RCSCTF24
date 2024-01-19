import os
import time
import demon

def write_and_delete():
    
    with open('/root/hint.txt', 'r') as hint_file:
        hint_content = hint_file.read()

    with open('/home/xavir/youneedme.txt', 'w') as user_file:
        user_file.write(hint_content)

    time.sleep(60)

    with open('/home/xavir/youneedme.txt', 'a') as user_file:
        user_file.write('\n' + demon.figlet())

    os.remove('/home/xavir/youneedme.txt')

write_and_delete()