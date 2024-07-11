class Solution:
    def reverseParentheses (self, s) -> str:
        stack = [] # empty stack to keep track of the characters
        for char in s:
            if char == ')':
                temp =[] #initialize a teporary list to store characters to be reversed
                while stack and stack [-1] != "(": #pop haracters in the stack until an opening parentheses is found
                    temp.append(stack.pop()) #append the popped characters to the temporary list
                stack.pop()  #remove the opening parentheses from the stack
                stack.extend(temp)
            else:
                stack.append(char) #if the characters is not a closing parentheses, push it onto the stack
        return ''.join(stack)


