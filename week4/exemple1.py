"""
Max este o pisica mare care doarme toata ziua.
obiectul -> Max (substantive, modalitate prin care putem sa personificam o clasa)
clasa -> pisica (substantiv, ne referim generic la o notiune ce vrem sa aiba o anumita activitate)
proprietatea -> marimea pisicii (mare) (adjectiv)
atributul -> doarme (adverb)

O masina Dacia merge repede.
obiectul -> Dacia (orice alta masina poate fi in loc)
clasa -> masina
proprietatea -> repede
atributul -> merge (adverb)
"""

# class PrimaClasa:
#     pass
#
# primul_obiect = Pisica() # O instanta de al clasei Pisica.
# Tom = Pisica()

stack = []

def push(val):
    stack.append(val)

def pop():
    value = stack[-1]
    del stack[-1]
    return value

push(3)
push(2)
push(1)

print(pop())
print(pop())
print(pop())