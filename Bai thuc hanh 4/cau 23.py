print("Nguyen Van Thai","\nMSSV: 235752021610005")
n=input('Nhap chuoi: ')
c,s=0,0
for a in n:
    if a.isalpha():
        c+=1
    elif a.isdigit():
        s+=1
print('Chuoi co ',c,'chu')
print('Chuoi co ',s,'so')

