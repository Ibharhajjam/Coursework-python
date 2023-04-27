import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input",type=str,dest="input")

def read_grid(variable_name: str, file_name: str):
    with open(file_name) as f:
        grid = f.read()
        grid = "[["+grid.replace("\n", "],\n[")+"]]"
        exec(variable_name+"="+grid, globals())

args = parser.parse_args()

read_grid("a", args.input)

print(a)

