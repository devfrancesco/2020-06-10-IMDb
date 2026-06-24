import flet as ft


class Controller:
    def __init__(self, view, model):
        # I riferimenti alla view e al model vengono passati all'atto della creazione nel main
        self._view = view
        self._model = model

    def handleCreaGrafo(self, e):
        self._view.txt_result.controls.clear()
        genere = self._view._dd_genere.value
        if genere is None:
            self._view.create_alert("Seleziona un genere")
            return
        self._model.buildGraph(genere)
        nNodes, nEdges = self._model.getGraphDetails()
        self._view.txt_result.controls.append(ft.Text(f"Grafo creato correttamente"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {nNodes} nodi e {nEdges} archi"))
        self._view._dd_attore.clean()
        self.fillDDAttori()
        self._view.update_page()


    def handleAttoriSimili(self, e):
        attore_id = self._view._dd_attore.value #restituisce l'id
        attore = self._model.getAttoreDaId(attore_id)
        if attore is None:
            self._view.create_alert("Seleziona un attore")
            return
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Attori simili a {attore}"))
        attori_simili = self._model.getAttoriConnessi(attore_id) #perchè l'abbiamo implementato a partire dall'id
        if attori_simili == []:
            self._view.txt_result.controls.append(ft.Text(f"Non esistono attori simili as {attore}"))
            self._view.update_page()
            return
        for a in attori_simili:
            self._view.txt_result.controls.append(ft.Text(a))
        self._view.update_page()

    def handleSimulazione(self, e):
        pass

    def fillDDGeneri(self):
        generi = self._model.getAllGeneri()
        for gen in generi:
            self._view._dd_genere.options.append(ft.dropdown.Option(gen))
        self._view.update_page()

    def fillDDAttori(self):
        attori = self._model.getAttoriInGrafo()
        for a in attori:
            self._view._dd_attore.options.append(ft.dropdown.Option(key=str(a.id), text=a))
        self._view.update_page()