def read_grid(variable_name: str, file_name: str):
    with open(file_name) as f:
        grid = f.read()
        grid = "[["+grid.replace("\n", "],\n[")+"]]"
        exec(variable_name+"="+grid, globals())

read_grid("easy", "easy1")

print(easy)
read_grid("easy2", "easy2")

print(easy2)
read_grid("easy3", "easy3")

print(easy3)

read_grid("easy4", "hard1")

print(easy4)

read_grid("easy5", "med1")

print(easy5)

read_grid("easy6", "med2")

print(easy6)