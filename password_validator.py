import re
phrase = input()
if len(phrase) >= 7 and len(re.findall('[!,@,#,$,%,^,& ,*]', phrase)) >= 1:
    if len(re.findall('[0-9]', phrase)) >= 2:
        print('Strong')
else:
    print('Weak')
