S = input()
alpa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for a in alpa:
    S = S.replace(a, "*")
        
print(len(S))  