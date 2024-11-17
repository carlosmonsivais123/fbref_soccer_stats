from name_formatting import PlayerNameFormatting
from link_creator import FBREFLinkCreator
from link_parser import FBREFLinkParser


class FBREFPlayerSearch:
    def __init__(self):
        self.player_id_search_str = "player_id_search_by_last_name"
        self.player_general_home_page_str = "player_home_page_general"

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

        print(player_home_page_general_link)

    def execute_player_search_by_last_name(self, raw_player_name: str):
        self.player_search_by_last_name(raw_player_name=raw_player_name)
