import pandas as pd

def getDataframeSize(players: pd.Dataframe) ->list[int]:
    return list(players.shape)