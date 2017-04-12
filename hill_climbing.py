# File containing CNF
cnf = file('./cnf.txt')
cnf_arr = []
for i in cnf.readlines():
    cnf_arr.append(i.strip().replace('&',''))
state = [True, True, True, True, True, True, True, True, True]
mappings = {'A1':0, 'A2':1, 'A3':2, 'B1':3, 'B2':4, 'B3':5, 'C1':6, 'C2':7, 'C3':8}
def cost(st):
    count = 0
    for i in cnf_arr:
        i = i.replace('(','')
        i = i.replace(')','')
        terms = i.split('V')
        for t in terms:
            t = t.strip()
            if t:
                if ('-' in t and not st[mappings[t.replace('-','')]]):
                    count = count+1
                    break
                elif (not '-' in t) and st[mappings[t]]:
                    count = count+1
                    break
    return count
c_max = 0
new_state = []

while c_max<165:
    for i in range(0,9):
        tmp_state = state[:]
        tmp_state[i] = False
        c = cost(tmp_state)
        if c > c_max:
            c_max = c
            max_state = tmp_state
    print c_max, tmp_state
    state = max_state
print state
    
