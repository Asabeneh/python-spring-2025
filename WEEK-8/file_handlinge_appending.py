from datetime import datetime
now = datetime.now()
with open('log.txt', 'a') as f:
    f.write(f'Some one loggedin - {now}\n ')