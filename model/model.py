import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._graph = nx.Graph()
        self._attori = []
        self._idMapA = {}

    def buildGraph(self, genere):
        self._graph.clear()
        self._idMapA = {}
        self._attori = DAO.getAllAttori(genere)
        for a in self._attori:
            self._idMapA[a.id] = a
        self._graph.add_nodes_from(self._attori)
        allEdges = DAO.getAllEdges(genere, self._idMapA)
        for e in allEdges:
            self._graph.add_edge(e.a1, e.a2, weight=e.peso)

    def getGraphDetails(self):
        return len(self._graph.nodes), len(self._graph.edges)

    def getAllGeneri(self):
        return DAO.getAllGeneri()

    def getAttoriInGrafo(self):
        return self._graph.nodes

    def getAttoriConnessi(self, id_attore):
        attore = self._idMapA[int(id_attore)]
        connessi = list(nx.node_connected_component(self._graph, attore))
        connessi.remove(attore)
        connessi.sort(key=lambda a: a.last_name)
        return connessi

    def getAttoreDaId(self, id_attore):
        return self._idMapA[int(id_attore)]