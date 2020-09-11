def valid_parentheses(string):
    f = list(filter(lambda x: x == "(" or x == ")", string))
    if len(f) == 0: return True
    if f[0] == ')' or f[len(f) - 1] == '(': return False
    return f.count("(") == f.count(")")

print(valid_parentheses("hi())("))
print(str(list(filter(lambda x: x == "(" or x == ")", "hi())("))))
#coś nie działa i nie wiem co
