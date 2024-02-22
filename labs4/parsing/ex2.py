import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(1)
tomorrow = today + datetime.timedelta(1)

print(" Yesterday: ", yesterday.strftime('%d-%m-%Y'),'\n', "Today:     ", 
today.strftime('%d-%m-%Y'),'\n', "Tomorrow:  ", tomorrow.strftime('%d-%m-%Y'))