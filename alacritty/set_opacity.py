from pathlib import Path

path = Path(__file__).parent

with open(path.joinpath("alacritty.toml"), "r") as f:
    lines = f.readlines()

with open(path.joinpath(".old.alacritty.toml"), "w") as f:
    f.writelines(lines)

with open(path.joinpath("alacritty.toml"), "w") as f:
    for line in lines:
        if line.rstrip() == "opacity = 1.0":
            f.write("opacity = 0.9\n")
        elif line.rstrip().startswith("opacity"):
            f.write("opacity = 1.0\n")
        else:
            f.write(line)
