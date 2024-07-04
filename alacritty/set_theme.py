import sys
from typing import Tuple
from pathlib import Path

path = Path(__file__).parent

THEME_TAG = "theme_choice"
OFF_STR = "  #"
ON_STR = "  "

class ThemeEnumerationDiscontinuity(IndexError):
    """The enumerations specified by the user are discontinuous. Make sure
    that the theme choices are enumerated starting at zero with a spacing of
    one."""
    pass

class NoThemePathError(ValueError):
    """The theme lines should each specify a path where the theme configuration
    can be found."""
    pass

class ThemeChoiceLine():

    def __init__(self, enum, theme_path, theme_tag=THEME_TAG):
        """This class will capture the content required for a line to be used and 
        updated as part of the set of 'theme choices'. 

        Themes in alacritty are basicically just [color] configuration in the
        form of another toml file. Importing the toml for the colorscheme of
        choice will impact the colors of the emulator"""

        self._tag = theme_tag
        self._theme_path = Path(theme_path)
        self._enum = int(enum)

    @property
    def enum(self) -> int:
        """current enumeration of the themeline. 0 is current."""
        return self._enum

    @property
    def theme_path(self) -> Path:
        """The theme_path property."""
        return self._theme_path

    @property
    def toml_str(self) -> str:
        """The theme line that can be written directly to a config file within
        an import list. Make sure that the `OFF_STR` and `ON_STR` match."""
        return ThemeChoiceLine.build_themeline(self._theme_path, self._enum, self._tag)
    
    @staticmethod
    def build_themeline(path: str, enum: int, theme_tag: str) -> str:
        """Make the line for the current state. It should be formatted and can
        be written into the file if `ON_STR` and `OFF_STR` match the config
        file formaatting."""

        def _theme_enum_tag(enum):
            return f", #{theme_tag} {int(enum)}"

        if enum == 0:
            return "".join([ON_STR, f"\"{path}\"", _theme_enum_tag(enum)])
        else:
            return "".join([OFF_STR, f"\"{path}\"", _theme_enum_tag(enum)])

    @staticmethod
    def increment_enum(enum: int, n_enums: int) -> int:
        """Wrap arround incrementing. An alternative would be circular
        permutation, but this would require the enumeration state of all the
        other ThemeChoice instances."""
        return (enum + 1) % n_enums

    @staticmethod
    def decriment_enum(enum: int, n_enums: int) -> int:
        """Wrap around decrimenting."""
        return ( enum + (n_enums - 1) ) % n_enums

    @staticmethod
    def parse_raw_themechoice_line(raw_line: str, theme_tag: str) -> Tuple[Path,int]:

        def _extract_path(path_portion: str) -> str:

            try:
                _, path, *_ = path_portion.split('\"')
            except ValueError:
                try:
                    _, path, *_ = path_portion.split("\'")
                except ValueError as e:
                    raise NoThemePathError() from e

            return path

        path_portion, _tag_portion, enum_portion = raw_line.partition(theme_tag)
        
        return Path(_extract_path(path_portion)), int(enum_portion)

    def increment(self, n_enums: int) -> None:
        self._enum = ThemeChoiceLine.increment_enum(self.enum, n_enums)

    def decriment(self, n_enums: int) -> None:
        self._enum = ThemeChoiceLine.decriment_enum(self.enum, n_enums)

def compute_n_enums(enums: list) -> int:
    """using the raw themelines, determine the number of enums"""
    infered_n_enums = max(enums) + 1

    if len(enums) == infered_n_enums:
        return infered_n_enums
    else:
        raise ThemeEnumerationDiscontinuity(f"The enumerations of the {THEME_TAG} lines contain a gap.")

def parse_config_for_theme_choices(toml_filepath):

    theme_choices = []
    print("parsing:", end=" ")
    with open(toml_filepath, "r") as at:
        for line in at.readlines():
            try:
                theme_path, enum = ThemeChoiceLine.parse_raw_themechoice_line(line, THEME_TAG)
                theme_choices.append(ThemeChoiceLine(enum, theme_path))
                print(f"{enum}", end="")
            except NoThemePathError:
                print("p", end = "")
            except ValueError:
                print("v", end = "")

    print("\t...done")
    return theme_choices

def increment_themelines(toml_filepath, n_enums, direction):

    updated_lines = []
    print("incrementing:", end=" ")
    with open(toml_filepath, "r") as at:
        for line in at.readlines():
            try:
                theme_path, enum = ThemeChoiceLine.parse_raw_themechoice_line(line, THEME_TAG)
                this_theme = ThemeChoiceLine(enum, theme_path)
                if direction == "reverse":
                    this_theme.increment(n_enums)
                else:
                    this_theme.decriment(n_enums)
                updated_lines.append(this_theme.toml_str + "\n")
                print(f"({enum}:{this_theme.enum})", end="")
            except NoThemePathError:
                updated_lines.append(line)
            except ValueError:
                updated_lines.append(line)

    print("\t(writing)", end="")
    with open(toml_filepath, "w") as at:
       at.writelines(updated_lines)

    print("\t...done")

def loop_through_themes(direction):
    config_path = path.joinpath("alacritty.toml")

    theme_choices = parse_config_for_theme_choices(config_path)
    n_enums = compute_n_enums([tc.enum for tc in theme_choices])
    increment_themelines(config_path, n_enums, direction)
                
if __name__ == "__main__":
    _, direction = sys.argv
    loop_through_themes(direction)
