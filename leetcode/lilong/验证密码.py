import re

while True:
    try:
        # pwd = input().strip()
        pwd = "021Abc9Abc1"
        res = 'NG'

        if len(pwd) >8:

            a1 = re.findall(r'[A-Z]', pwd)
            a2 = re.findall(r'[a-z]', pwd)
            a3 = re.findall(r'\d', pwd)
            a4 = re.findall(r'[^A-Z a-z \d]', pwd)

            ar = re.findall(r'(.{3}).*', pwd)
            print(ar)
            if [a1,a2,a3,a4].count(None) <= 1  and ar == []:
                res = "OK"
        print(res)
        break
    except Exception as e:
        break