import pandas as pd

from fbref_data_extraction.name_formatting import PlayerNameFormatting
from fbref_data_extraction.link_creator import FBREFLinkCreator
from fbref_data_extraction.link_parser import FBREFLinkParser
from fbref_data_extraction.player_data_extract import PlayerDataExtract


class FBREFPlayerSearch:
    """
    Class to execute the modules related to the specified player's links including unique FBREF ID, individual player season links
    and the data extraction for their seasons.

    Attributes:
        player_id_search_str (str): Indiciates to execute the FBREF player unique ID search
        player_general_home_page_str (str): Indiciates to execute the FBREF player general link search
        player_season_years_played_str (str): Indicates to execute the player individual season link search
    """

    def __init__(self):
        self.player_id_search_str = "player_id_search_by_last_name"
        self.player_general_home_page_str = "player_home_page_general"
        self.player_season_years_played_str = "player_season_years_competitions"

    def fbref_player_search(self, raw_player_name: str) -> pd.DataFrame:
        """
        Search for a player in FBREF throigh the repeition of link creation and parsing through CSS selectors to extract data for their
        careers and store it in a dataframe.

        Args:
            raw_player_name: Name of the player that is being extracted, as entered by the user

        Returns:
            player_raw_data_df: Dataframe with the raw player statistics for the specified seasons
        """
        player_name_dict = PlayerNameFormatting().execute_player_name_formatting(
            raw_player_name=raw_player_name
        )

        player_id_link_link = FBREFLinkCreator().execute_fbref_link_creator(
            link_creator_type=self.player_id_search_str,
            link_creator_input_dict=player_name_dict,
        )

        player_unique_id_link_dict = FBREFLinkParser().execute_fbref_link_parser(
            link_search_type=self.player_id_search_str,
            link_list=player_id_link_link,
            player_name_dict=player_name_dict,
        )

        player_home_page_general_link = FBREFLinkCreator().execute_fbref_link_creator(
            link_creator_type=self.player_general_home_page_str,
            link_creator_input_dict=player_unique_id_link_dict,
        )

        player_competitions_link_dict = FBREFLinkParser().execute_fbref_link_parser(
            link_search_type=self.player_season_years_played_str,
            link_list=player_home_page_general_link,
            player_name_dict=player_name_dict,
        )

        player_home_page_general_link = FBREFLinkCreator().execute_fbref_link_creator(
            link_creator_type=self.player_season_years_played_str,
            link_creator_input_dict=player_competitions_link_dict,
        )

        player_raw_data_df = PlayerDataExtract().execute_individual_player_data_extract(
            link_list=player_home_page_general_link, player_name_dict=player_name_dict
        )

        return player_raw_data_df

    def execute_fbref_player_search_stats(self, raw_player_name: str) -> pd.DataFrame:
        """
        Executes the process to extract the specified player's statistics from FBREF (https://fbref.com/en/) for
        the players given history.

        Args:
            raw_player_name: Name of the player that is being extracted, as entered by the user

        Returns:
            player_raw_data_df: Dataframe with the raw player statistics for the specified seasons
        """
        players_data_raw_df = self.fbref_player_search(raw_player_name=raw_player_name)

        return players_data_raw_df
