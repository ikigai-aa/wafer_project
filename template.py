import os 

dirs =[
    os.path.join("data","raw"),
 os.path.join("data","processed"),
 "notebooks",
 "saved_models",
 "src"
 ]

for dir_ in dirs:
    os.makedirs(dir_, exist_ok=True)



file = [
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py")

]

for _ in file:
    with open(os.path.join(_,".gitkeep")) as f:
        pass