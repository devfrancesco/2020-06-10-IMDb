from dataclasses import dataclass

from model.Attore import Attore


@dataclass
class Arco:
    a1 : Attore
    a2 : Attore
    peso : int