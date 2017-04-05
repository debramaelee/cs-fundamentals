# A stack based efficient method to calculate s
def calculateSpan(prices, spans):
    # Create a stack and push index of fist element to it
    stack = Stack()
    stack.push(0)

    # Span value of first element is always 1
    spans[0] = 1

    # Calculate span values for rest of the elements
    for i in range(1, len(prices)):
        # Pop elements from stack whlie stack is not
        # empty and top of stack is smaller than price[i]
        while(not stack.isEmpty() and prices[stack.peek()] <= prices[i]):
            stack.pop()

        # If stack becomes empty, then price[i] is greater
        # than all elements on left of it, i.e. price[0],
        # price[1], ..price[i-1]. Else the price[i]  is
        # greater than elements after top of stack
        spans[i] = i + 1 if stack.size() <= 0 else (i - stack.peek())

        # Push this element to stack
        stack.push(i)