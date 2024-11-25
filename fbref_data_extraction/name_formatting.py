class PlayerNameFormatting:
    """
    Class to format the player name in the needed manner to use throughout the project.
    """

    def name_first_two_letters_last_name(self, raw_player_name: str) -> str:
        """
        Extracts the first two letters of a player's last name to be used to search the player ID on FBREF.

        Args:
            raw_player_name (str): Name of the player that is being extracted, as entered by the user

        Returns:
            first_two_letters_ln (str): First two letters of the player's last name
        """
        raw_ln = raw_player_name.split()[-1]
        first_two_letters_ln = raw_ln[0:2]
        first_two_letters_ln = first_two_letters_ln.lower()

        return first_two_letters_ln

    def name_with_delimiter(self, raw_player_name: str) -> str:
        """
        Adds a delimiter for the player name to be used as a search variable for the FBREF player ID.

        Args:
            raw_player_name (str): Name of the player that is being extracted, as entered by the user

        Returns:
            player_name_delimiter (str): The name of the player with the added (_) delimiter
        """
        player_name_delimiter = "-".join(raw_player_name.split())

        return player_name_delimiter

    def execute_player_name_formatting(self, raw_player_name: str) -> dict:
        """
        Executes the name formatting functions needed to be used throughout the project and strores them
        in a dictionary which includes first two letters of a players last name, adding a delimiter and storing
        the raw name as entrerd by the user.

        Args:
            raw_player_name (str): Name of the player that is being extracted, as entered by the user

        Returns:
            player_name_format_dict (dict): Dictionary with the stored formatted names
        """
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
