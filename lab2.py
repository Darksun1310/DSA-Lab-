class stack:
    def __init__(self):
        self.stack = [] 

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty(): 
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class Calculator:
    def __init__(self,expression):
        self.stack=stack()
        
        for char in expression:
            if char.isdigit():
                self.stack.push(int(char))
            elif char in['+','-','*','/']:
                operand2= self.stack.pop()
                operand1= self.stack.pop()
                if char== '+':
                    self.stack.push
                    result=(operand1+operand2) 
                elif char== '-':
                    self.stack.push
                    result=(operand1-operand2)
                elif char=='*' :
                    self.stack.push
                    result=(operand1*operand2)
                elif char=='/' :
                    self.stack.push
                    result=(operand1/operand2)
                self.stack.push(result)
Calculator=Calculator
expression=586*8956
print(expression)

        
                    