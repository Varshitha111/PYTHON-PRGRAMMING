def sentence(s):
    # frst=s[0]
    s=s.split(" ")
    frst=s[0]
    for i in s:
        if i.lower()<frst.lower():
            frst=i
    print(frst)
sentence("I am varshitha")