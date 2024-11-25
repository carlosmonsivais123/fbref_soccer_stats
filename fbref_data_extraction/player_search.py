import pandas as pd

from fbref_data_extraction.name_formatting import PlayerNameFormatting
from fbref_data_extraction.link_creator import FBREFLinkCreator
from fbref_data_extraction.link_parser import FBREFLinkParser
from fbref_data_extraction.player_data_extract import PlayerDataExtract


class FBREFPlayerSearch:
    def __init__(self):
        self.player_id_search_str = "player_id_search_by_last_name"
        self.player_general_home_page_str = "player_home_page_general"
        self.player_season_years_played_str = "player_season_years_competitions"

    def player_search_by_last_name(self, raw_player_name: str) -> str:
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

    def execute_fbref_search_player_stats(self, raw_player_name: str) -> pd.DataFrame:
        players_data_raw_df = self.player_search_by_last_name(
            raw_player_name=raw_player_name
        )

        return players_data_raw_df
