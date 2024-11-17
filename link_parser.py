import requests
from bs4 import BeautifulSoup


class FBREFLinkParser:
    def search_for_player_id(self, link_list: list, player_name_dict: dict):
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

    def execute_fbref_link_parser(
        self, link_search_type: str, link_list: list, player_name_dict: dict
    ) -> dict:
        if link_search_type == "player_id_search_by_last_name":
            search_response = self.search_for_player_id(
                link_list=link_list, player_name_dict=player_name_dict
            )

        return search_response
