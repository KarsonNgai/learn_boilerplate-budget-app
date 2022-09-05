class Category:
    def __init__(self, name):
        self.name=name
        self.ledger=[] 
        #{'amount': amount, 'description': description}
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
    def withdraw(self,amount,description=''):
        if self.check_funds(amount) == True:
            self.deposit(-amount,description)
            return True #show有冇加到入去balance到
        else:
            return False
    def transfer(self, amount, location):
        if self.withdraw(amount,'Transfer to '+location.name) == True:
            location.deposit(amount,"Transfer from "+self.name)
            return True
        else:  #amount>budget
            return False
    def get_balance(self):
        self.sum_up=0
        for i in range(len(self.ledger)):
            self.sum_up+= self.ledger[i]['amount']
        return self.sum_up #本身withdraw 個amount冇pass sun_up,所以self.sum_up少一個number if 用係最後
    def check_funds(self,amount):
        if self.get_balance() >= amount: #budget>=total amount
            return True
        else:
            return False
    def __str__(self):
        first_line=(self.name.center(30,'*'))
        body_line=''
        for k in range(len(self.ledger)):
            body_line_description=self.ledger[k]['description'][0:23]
            body_line_amount= str(round(self.ledger[k]['amount'],2))
            if '.' not in body_line_amount:
                body_line_amount+='.00'
            body_line+= body_line_description.ljust(23)+ body_line_amount.rjust(7)+'\n'
        return(first_line + '\n'+ body_line+'Total: {}'.format(self.get_balance()))
def create_spend_chart(categories):
    #input % in the list
    percentage_list=[]
    name_list=[]
    for i in categories: #找百分比分母
        category_sum = 0
        for k in range(len(i.ledger)):
            if i.ledger[k]['amount']<0:
                category_sum+=i.ledger[k]['amount']
        category_sum*=-1
        percentage_list.append(category_sum)#[76.039999,25.55,15]
        #total_sum
        for k in i.name:
            #name
            if i.name not in name_list:
                name_list.append(i.name)
    total_sum=0
    for k in percentage_list:
        total_sum+=k
    #圖y
    y_show=''
    y_intercept=100
    y_final_word=''
    totaly_intercept=''
    for i in range(11):
        add_y=' '
        y=''
        for j in percentage_list:#outcome should be 6,2,1
            if (j/total_sum)*100<y_intercept: #j指number
                y='   '
            else:
                y='o  '
            add_y+=y
        y_final_word+=str(y_intercept).rjust(3)+'|'+add_y+'\n'
        y_intercept-=10
    #字的最大數字
    Max_name=0
    for i in name_list:
        if len(i)>Max_name:
            Max_name=len(i)
    #字x
    a=0
    b=1
    x_intercept=''
    x_show=''
    for i in range(Max_name):
        name_word='' 
        for j in range(len(name_list)):
            if name_list[j][a:b]!='':
                name_word+=name_list[j][a:b]+'  '
            else:
                name_word+='   '
        if i != Max_name-1:
            x_intercept+='     '+name_word+'\n'
        else:
            x_intercept+='     '+name_word
        a+=1
        b+=1
    x_show='    '+'----------'+'\n'+x_intercept
    print(x_show)
    return('Percentage spent by category\n'+y_final_word+x_show)
