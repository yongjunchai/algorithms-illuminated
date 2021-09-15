

class Calculator:
    def __init__(self):
        self.operators = dict()
        self.operators["+"] = 1
        self.operators["-"] = 1
        self.operators["*"] = 2
        self.operators["/"] = 2
        self.parenthesis = set()
        self.parenthesis.add("(")
        self.parenthesis.add(")")

    def getNextToken(self, expression: str, index: int):
        if index >= len(expression) or index < 0:
            return (None, None)
        token = ""
        curIndex = index
        for i in range(index, len(expression)):
            curIndex = i
            if expression[i] == " " or expression[i] == "\t":
                # skip space and tab
                continue
            if expression[i] in self.operators.keys() or expression[i] in self.parenthesis:
                if len(token) > 0:
                    curIndex -= 1
                    break
                token = expression[i]
                break
            else:
                token += expression[i]
        if token == "":
            token = None
        return (token, curIndex + 1)

    def calculateUtilLowerPriorityOperator(self, stack: list, operatorToBePushed: str):
        if len(stack) < 3:
            print("no enough items in stack")
            return
        if self.operators[stack[len(stack) - 2]] <= self.operators[operatorToBePushed]:
            stack.append(operatorToBePushed)
            return
        rightOperand = stack.pop()
        operator = stack.pop()
        leftOperand = stack.pop()
        stack.append(self.doCalculate(leftOperand, rightOperand, operator))
        self.calculateUtilLowerPriorityOperator(stack, operatorToBePushed)

    def calculateUntilRightParenthesis(self, stack: list):
        if len(stack) < 2:
            raise Exception("not expected stack length")
        rightOperand = stack.pop()
        operator = stack.pop()
        if operator == "(":
            stack.append(rightOperand)
            return
        if len(stack) == 0:
            raise Exception("empty stack")
        leftOperand = stack.pop()
        stack.append(self.doCalculate(leftOperand, rightOperand, operator))
        self.calculateUntilRightParenthesis(stack)

    def doCalculate(self, leftOperand: int, rightOperand: int, operator: str):
        leftOperand = int(leftOperand)
        rightOperand = int(rightOperand)
        if operator not in self.operators.keys():
            raise Exception("not supported operator [{}]".format(operator))
        if operator == "+":
            return leftOperand + rightOperand
        if operator == "-":
            return leftOperand - rightOperand
        if operator == "*":
            return leftOperand * rightOperand
        if operator == "/":
            return leftOperand / rightOperand

    def calculate(self, expression: str):
        nextIndex = 0
        stack = list()
        previousOperator = None
        result = None
        while True:
            token, nextIndex = self.getNextToken(expression, nextIndex)
            if token is None:
                break
            if token not in self.operators.keys() and token not in self.parenthesis:
                #operand
                stack.append(token)
                continue
            if token in self.operators:
                if previousOperator is None:
                    previousOperator = token
                    stack.append(token)
                    continue
                if self.operators[previousOperator] <= self.operators[token]:
                    previousOperator = token
                    stack.append(token)
                    continue
                # the priority of current operator is lower than what on the top of the stack
                # pop stack items to do calculation until lower priority operator encountered
                self.calculateUtilLowerPriorityOperator(stack, token)
                previousOperator = token
                continue
            # this token is parenthesis
            if token == "(":
                stack.append(token)
                continue
            # ")" case
            self.calculateUntilRightParenthesis(stack)
        while len(stack) > 0:
            if len(stack) == 1:
                result = stack.pop()
                break
            if len(stack) < 3:
                raise Exception("not expected stack length [{}]".format(len(stack)))
            rightOperand = stack.pop()
            operator = stack.pop()
            leftOperand = stack.pop()
            stack.append(self.doCalculate(leftOperand, rightOperand, operator))
        return result



