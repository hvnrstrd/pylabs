import datetime
out = datetime.datetime.now()-datetime.timedelta(5)
print(out.strftime('%d-%m-%Y'))