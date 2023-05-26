answer = input("Select a calculator mode (add/sub/divide/multi) ")
if answer == "add":
    first_num = input("First: ")

    second_num = input("Second: ")

    sum = float(first_num) + float(second_num)

    print(sum)
if answer == "sub":
    fir_num = input("First: ")

    sec_num = input("Second: ")

    sol = float(fir_num) - float(sec_num)

    print (sol)
if answer == "divide":
    fn = input("First: ")

    sn = input("Second: ")

    sl = float(fn) / float(sn)

    print(sl)
if answer == "multi":
    f = input("First: ")

    s = input("Second: ")

    ans = float(f) * float(s)

    print(ans)
