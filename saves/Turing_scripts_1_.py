# -*- PseudoCode -*-

BlockStmt([ForStmt('i', NumberNode(1), NumberNode(16), [IfStmt(BinOpNode(BinOpNode(IdentifierNode('i'), NumberNode(15), '%'), NumberNode(0), '=='), [DisplayStmt(StringNode('FizzBuzz')), DisplayStmt(StringNode('hello world'))]), ElseStmt([IfStmt(BinOpNode(BinOpNode(IdentifierNode('i'), NumberNode(3), '%'), NumberNode(0), '=='), [DisplayStmt(StringNode('Fizz'))]), ElseStmt([IfStmt(BinOpNode(BinOpNode(IdentifierNode('i'), NumberNode(5), '%'), NumberNode(0), '=='), [DisplayStmt(StringNode('Buzz'))]), ElseStmt([DisplayStmt(IdentifierNode('i'))])])])], None)])

# -*- End -*-
#
#
# -*- PythonCode -*-

print("lol")

# -*- End -*-