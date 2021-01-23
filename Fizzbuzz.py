#VS Github Testing
class Solution():
    def FizzBuzz(self):
        x=self.getInput()
        for i in range(1,x):
            if(i%15==0):
                print('FizzBuzz')
            elif(i%3==0):
                print('Fizz')
            elif(i%5==0):
                print('Buzz')
            else:
                print(i)
    def getInput(self):
        while(True):
            i= input('Enter the number of ints you want: ')
            if (i.isalpha()):
                print('Error!\nTry again, positive intergers above 0 only!')
                continue
            elif(int(i)<=0):
                print('Error!\nTry again, positive intergers above 0 only!')
                continue
            else:
                return int(i)+1
myAnswer=Solution()
myAnswer.FizzBuzz()
