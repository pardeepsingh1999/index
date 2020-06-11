
def checking(newDt):
    if(newDt<10):
        return '0'+str(newDt)
    else:
        return str(newDt)


def solution(D):
    #print(D)

    res = list(D.keys())
    
    for i in range(len(res)-1):
        #print(res[i].split('-'))
        cal = int(res[i+1].split('-')[2]) - int(res[i].split('-')[2])
        if(cal > 1):
            #print(cal)
            #print(res[i], res[i+1])
            #AP -> lastNo. = firstNo. + (n-1)diff 
            diff = (D[res[i+1]] - D[res[i]]) / cal
            #print(abs(int(diff)))
            for j in range(cal-1):
                newDt = int(res[i].split('-')[2]) + (j+1)
                newDate = res[i].split('-')[0]+'-'+res[i].split('-')[1]+'-'+checking(newDt)
                #print(newDate)
                res.append(newDate)
                res2 = sorted(res)
                D[newDate] = int(D[res2[i+j]]) + int(diff)
            print(D)
            sorted_D = sorted(D.items(), key=lambda t: t[0])
            print(sorted_D )

num = int(input('Enter Total Number: '))
# YYYY-MM-DD
dic = {}

for i in range(num):
    date = input('Enter Date(YYYY-MM-DD): ')
    n = int(input('Enter value(in integer): '))
    dic[date] = n


solution(dic)
