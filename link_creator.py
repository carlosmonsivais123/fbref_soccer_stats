class FBREFLinkCreator:
    def __init__(self):
        # self.fbref_home_link="https://fbref.com"
        self.fbref_home_link_english = "https://fbref.com/en/"

        self.fbref_home_link_players = "https://fbref.com/en/players/"

    def player_id_search_by_last_name_link_creator(
        self, link_creator_input_dict: dict
    ) -> list:
        player_search_by_ln = (
            self.fbref_home_link_english
            + "players/"
            + link_creator_input_dict["ln_first_two_letters"]
            + "/"
        )

        player_search_by_ln_list = [player_search_by_ln]

        return player_search_by_ln_list

    def player_home_page_general_link_creator(self, link_creator_input_dict):
        player_unique_id = link_creator_input_dict["player_unique_id"]
        player_name = link_creator_input_dict["full_name_with_delimiter"]

        player_all_competitions_general = (
            self.fbref_home_link_players
            + player_unique_id
            + f"/all_comps/{player_name}-Stats---All-Competitions"
        )

        player_general_home_page_link_list = [player_all_competitions_general]

        return player_general_home_page_link_list

    def execute_fbref_link_creator(
        self, link_creator_type: str, link_creator_input_dict: dict
    ) -> list:
        if link_creator_type == "player_id_search_by_last_name":
            link_list = self.player_id_search_by_last_name_link_creator(
                link_creator_input_dict=link_creator_input_dict
            )

        if link_creator_type == "player_home_page_general":
            link_list = self.player_home_page_general_link_creator(
                link_creator_input_dict=link_creator_input_dict
            )

        return link_list
