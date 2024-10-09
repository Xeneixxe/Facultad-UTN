#lista comprehension, lista de comprension 
names = ["Pepe", "ivo", "Lupe", "Pablo"]
alongP = [p  for p in names if p[0] == 'P']# Esto regresa una nueva lista
print(alongP) 

bottleC = [{"name": "Quimes", "country":  "Arg"},
           {"name": "Corona", "country":  "Mx"},
           {"name": "Stella Artois", "country":  "Belgium"}],

Arg = [b for b in bottleC if b["country"] == -"Arg"]
print(Arg)
print(bottleC)