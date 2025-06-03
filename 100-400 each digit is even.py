
for i in range(100,401):
       num=i
       while i>0:
              digit=i%10
              i//=10
              if digit%2!=0:
                     break
       else:
              print(num)
