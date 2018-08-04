import random
def problem_gen():

    num1=int(round(random.uniform(0, 1),2)*100+1)
    num2=int(round(random.uniform(0,1),2)*100+1)
   
    #opreration genration
    opr_val = int(round(random.uniform(0, 1), 2)*2+1)
    if(opr_val==1):
        ans=int(num1+num2)
        oper='+'
    else:
        ans=int(num1-num2)
        oper='-'
    
    print('Question- '+str(num1)+' '+oper+' '+str(num2)+'?')
    user=int(input('A- '))
    if(user==ans):
        print('Your Answer is Correct\n')
        problem_gen()
    else:
        print('Incorrect Answer\n')
        problem_gen()

