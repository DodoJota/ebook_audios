from networkx.utils.backends import _dispatch

@_dispatch
def trophic_levels(G, weight: str = "weight"): ...
@_dispatch
def trophic_differences(G, weight: str = "weight"): ...
@_dispatch
def trophic_incoherence_parameter(G, weight: str = "weight", cannibalism: bool = False): ...
