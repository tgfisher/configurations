#!/usr/bin/python3

from pathlib import Path
from string import Template

def fill_template(template_path, filling_content):

    with open(template_path, "r") as f:
        template = Template(f.read())

    filled_template = template.substitute(filling_content)

    return filled_template

def write_config(config_path, config_toml_content):

    with open(config_path, "w") as f:
        f.write(config_toml_content)

if __name__ == "__main__":
    
    alacritty_template = Path("./alacritty.template.toml")
    alacrity_toml = Path("./alacritty.toml")
    substitute_content = {
        "alacritty_config_dir": alacritty_template.parent.absolute(),
    }

    write_config(
        alacrity_toml, 
        fill_template(alacritty_template, substitute_content),
    )
