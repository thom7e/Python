import re
import string

with open('day4bla') as file:
    input = file.readlines()
    PP=[]
    pp_num = 0
    for line in input:
        fields = line.split(' ')
        if fields == ['\n']:
            pp_num += 1
            PP.append('NewID')
        for field in fields:
            if field != '\n':
                string1 = field.splitlines()[0]
                string1 = string1.split(':')
                if string1[0] != 'cid':
                    PP.append(string1)
    PP.append('NewID')
print(str(pp_num+1) +  ' Passports')

keys =[('byr','BirthYear'),('iyr','IssueYear'),('eyr','ExpirationYear'),('hgt','Height'),('hcl','HairColor'),('ecl','EyeColor'),('pid','PassportID'),('cid','CountryID')]
valid = ([False, False, False, False, False, False, False])

count = 0
for line in PP:
    # print(line)
    if line != 'NewID':
        # print(line)
        keynum = 0
        for key in keys:
             if line[0] == key[0] and key[0] == 'byr':
                 try:
                     num = int(line[1])
                 except ValueError:
                     pass
                 if len(line[1]) == 4 and num >= 1920 and num <= 2002:
                    valid[keynum] = True
                    # print('Birthyear ok!')

             if line[0] == key[0] and key[0] == 'iyr':
                 try:
                     num = int(line[1])
                 except ValueError:
                     pass
                 if len(line[1]) == 4 and num >= 2010 and num <= 2020:
                     valid[keynum] = True
                     # print('Issue Year ok!')

             if line[0] == key[0] and key[0] == 'eyr':
                 try:
                     num = int(line[1])
                 except ValueError:
                     pass
                 if len(line[1]) == 4 and num >= 2020 and num <= 2030:
                     valid[keynum] = True
                     # print('Expiration Year ok!')
             if line[0] == key[0] and key[0] == 'hgt':
                if line[1][-1].isalpha():


                     r = re.compile("([0-9]+)([a-zA-Z]+)")
                     m = r.match(line[1])
                     unit = m.group(2)
                     size = int(m.group(1))
                     if (unit == 'in' and size >= 59 and size <= 76) or ( unit == 'cm' and size >= 150 and size <= 193):
                         valid[keynum] = True
                     #     # print('Height ok!')


             if line[0] == key[0] and key[0] == 'hcl':
                 if len(line[1]) == 7 and line[1][0] == '#':
                     try:
                         int(line[1][1:], 16)
                         valid[keynum] = True
                         # print('Hair Color ok!')
                     except ValueError:
                         pass

             if line[0] == key[0] and key[0] == 'ecl':
                 if line[1] in ['amb','blu','brn','gry','grn','hzl','oth']:
                     valid[keynum] = True
                     # print('eye Color ok!')

             if line[0] == key[0] and key[0] == 'pid':
                 if len(line[1])==9:
                     try:
                         num = int(line[1])
                         valid[keynum] = True
                         # print('Passport ID ok!')
                     except ValueError:
                         pass
             keynum += 1
    else:
        if not False in valid:
            count +=1
        # print(valid)
        valid = ([False, False, False, False, False, False, False])

print(str(count), 'valid Passports')