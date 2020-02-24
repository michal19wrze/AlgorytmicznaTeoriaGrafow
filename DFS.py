##Program zwraca odwiedzone wierzcholki grafu przez dfs
def dfs(graf, start):
    visited = set()
    stos = [start]
    while stos:
        vertex = stos.pop()
        if vertex not in visited:
            visited.add(vertex)
            stos.extend(graf[vertex] - visited)
    return visited


graf = {'1': set(['2', '3']),
         '2': set(['1', '4', '5']),
         '3': set(['1', '6']),
         '4': set(['2']),
         '5': set(['2', '6']),
         '6': set(['3', '5'])}

print dfs(graf, '1') 
