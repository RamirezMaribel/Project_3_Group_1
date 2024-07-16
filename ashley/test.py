import pypokedex

pokemon = pypokedex.get(dex=1)  # DEX must be a valid _national_ pokedex
                                  # number
print(pokemon)
