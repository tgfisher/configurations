from pathlib import Path

path = Path(__file__).parent

with open(path.joinpath("alacritty.toml"), "r") as f:
    lines = f.readlines()

with open(path.joinpath(".old.alacritty.toml"), "w") as f:
    f.writelines(lines)

with open(path.joinpath("alacritty.toml"), "w") as f:
    for line in lines:
        if line.rstrip() == "blur = true":
            f.write("blur = false\n")
        elif line.rstrip().startswith("blur"):
            f.write("blur = true\n")
        else:
            f.write(line)
