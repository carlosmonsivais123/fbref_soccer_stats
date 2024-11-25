import requests
from bs4 import BeautifulSoup
import re


class FBREFLinkParser:
    def search_for_player_id(self, link_list: list, player_name_dict: dict) -> dict:
        search_player_for_id_link = link_list[0]

        response = requests.get(search_player_for_id_link)
        print(response)
        soup = BeautifulSoup(response.content, "html.parser")

        formatted_name = player_name_dict["full_name_with_delimiter"]

        player_directory_link_search = soup.select(rf"a[href*= '/{formatted_name}']")
        player_directory_link = [
            i.attrs.get("href") for i in player_directory_link_search
        ][0].strip()

        player_unique_identifier = player_directory_link.split("/")[3].strip()

        player_unique_identifier_dictionary = {
            "player_unique_id": player_unique_identifier,
            "full_name_with_delimiter": formatted_name,
        }

        return player_unique_identifier_dictionary

    def search_for_player_game_data_links(
        self, link_list: list, player_name_dict: dict
    ) -> dict:
        search_for_years_competition = link_list[0]
        player_name = player_name_dict["full_name_with_delimiter"]

        response = requests.get(search_for_years_competition)
        print(response)
        # time.sleep(3)

        soup = BeautifulSoup(response.content, features="html.parser")

        player_seasons_links = soup.select(
            rf"a[href*= '/summary/{player_name}-Match-Logs']"
        )
        player_seasons_links_list = [i.attrs.get("href") for i in player_seasons_links]

        # Removing national team stats since they are already included in season stats
        national_team_filter_regex = re.compile(r"nat\_tm")
        player_seasons_links_list_filter_1 = [
            i
            for i in player_seasons_links_list
            if not national_team_filter_regex.search(i)
        ]

        season_filter_regex_1 = re.compile(r"matchlogs\/[0-9]{4}-[0-9]{4}\/summary")
        player_seasons_links_list_filter_2 = [
            i
            for i in player_seasons_links_list_filter_1
            if season_filter_regex_1.search(i)
        ]

        season_filter_regex_2 = re.compile(r"matchlogs\/[0-9]{4}\/summary")
        player_seasons_links_list_filter_3 = [
            i
            for i in player_seasons_links_list_filter_1
            if season_filter_regex_2.search(i)
        ]

        player_seasons_links_list_filter_4 = (
            player_seasons_links_list_filter_2 + player_seasons_links_list_filter_3
        )

        player_seasons_dict = {
            "player_season_links": player_seasons_links_list_filter_4
        }

        return player_seasons_dict

    def execute_fbref_link_parser(
        self, link_search_type: str, link_list: list, player_name_dict: dict
    ) -> dict:
        if link_search_type == "player_id_search_by_last_name":
            search_response = self.search_for_player_id(
                link_list=link_list, player_name_dict=player_name_dict
            )

        elif link_search_type == "player_season_years_competitions":
            search_response = self.search_for_player_game_data_links(
                link_list=link_list, player_name_dict=player_name_dict
            )

        return search_response
