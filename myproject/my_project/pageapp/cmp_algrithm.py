




import datetime

previous_minutes = 200

current_time = datetime.datetime.utcnow()
#end_time = str(current_time).replace(' ','T').split('.')[0]

start_time = current_time - datetime.timedelta(minutes=previous_minutes)#.replace(' ','T').split('.')[0]
print(start_time)

for tm in range((previous_minutes//1440)+1):
    if previous_minutes > 1440:
        # previous_minutes - 1440
        end_time = start_time + datetime.timedelta(minutes=1440)#.replace(' ','T').split('.')[0]
        print("Passing time to office365 API")
        start_time1 = str(start_time).replace(' ','T').split('.')[0]
        end_time1 = str(end_time).replace(' ','T').split('.')[0]
        print("Passing time is {}     and     {}".format(start_time1,end_time1))
        print('\n')
        start_time = end_time
    else:
        end_time1 = str(current_time).replace(' ', 'T').split('.')[0]
        start_time1 = str(current_time - datetime.timedelta(minutes=previous_minutes)).replace(' ','T').split('.')[0]
        print(start_time1)
        print(end_time1)
