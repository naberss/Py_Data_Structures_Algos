def permute(s, i, t):
    if i == t:
        print(s)
    else:
        for rec in range(i, t + 1):
            s[i], s[rec] = s[rec], s[i]
            permute(s, i + 1, t)
            s[rec], s[i] = s[i], s[rec]  #backtrack

s = list('ABC')
i = 0
t = len(s)

permute(s,i,t-1)