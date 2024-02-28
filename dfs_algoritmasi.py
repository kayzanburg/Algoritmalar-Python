graph = {
    "A": set(["B", "C"]),
    "B": set(["A", "D", "E"]),
    "C": set(["A", "F"]),
    "D": set(["B"]),
    "E": set(["B", "F"]),
    "F": set(["C", "E"])
}

def dfs(graph, baslangic):
    ziyaret_edilen = set()
    stack = [baslangic]
    while stack:
        dugum = stack.pop()
        if dugum not in ziyaret_edilen:
            ziyaret_edilen.add(dugum)
            stack.extend(graph[dugum] - ziyaret_edilen)
    return ziyaret_edilen
