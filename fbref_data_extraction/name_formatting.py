class PlayerNameFormatting:
    def name_first_two_letters_last_name(self, raw_player_name):
        raw_ln = raw_player_name.split()[-1]
        first_two_letters_ln = raw_ln[0:2]
        first_two_letters_ln = first_two_letters_ln.lower()

        return first_two_letters_ln

    def name_with_delimiter(self, raw_player_name):
        player_name_delimiter = "-".join(raw_player_name.split())

        return player_name_delimiter

    def execute_player_name_formatting(self, raw_player_name: str) -> dict:

        first_two_letters_last_name = self.name_first_two_letters_last_name(
            raw_player_name=raw_player_name
        )
        name_delimiter = self.name_with_delimiter(raw_player_name=raw_player_name)

        player_name_format_dict = {
            "raw_name": raw_player_name,
            "ln_first_two_letters": first_two_letters_last_name,
            "full_name_with_delimiter": name_delimiter,
        }

        return player_name_format_dict
