from mixpanel import Mixpanel

import csv
import random
import string

MIXPANEL_TOKEN = 'c213a0e77d7bdbcba0fd3bc7efd42cde'
mp = Mixpanel(MIXPANEL_TOKEN)
f = open('feedback.csv', 'rb')
reader = csv.reader(f)
for row in list(reader)[1:]:
    name = row[0]
    name1 = name.split()
    name1 = "".join(name1)
    username = name1 + str(random.randint(1, 1000)) + \
        random.choice(string.letters)
    phone_no = row[1]
    email = row[2]
    phone_type = row[5]
    android_version = row[6]
    if len(phone_no) == 10:
        if phone_no[:1] == '9':
            phone_no = '+977' + phone_no
            mp.people_set(username, {
                '$phone': phone_no,
                '$name': name,
                '$email': email,
                'phone_type': phone_type,
                'android_version': android_version
            })


f.close()

f = open('feedback2.csv', 'rb')
reader = csv.reader(f)
for row in list(reader)[1:]:
    name = row[0]
    name1 = name.split()
    name1 = "".join(name1)
    username = name1 + str(random.randint(1, 1000)) + \
        random.choice(string.letters)
    phone_no = row[1]
    email = row[2]
    phone_type = row[5]
    android_version = row[6]
    if len(phone_no) == 10:
        if phone_no[:1] == '9':
            phone_no = '+977' + phone_no
            mp.people_set(username, {
                '$phone': phone_no,
                '$name': name,
                '$email': email,
                'phone_type': phone_type,
                'android_version': android_version
            })


f.close()
