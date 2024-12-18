import pandas as pd
import requests
from bs4 import BeautifulSoup
import time


class PlayerDataExtract:
    """
    Class to extract the raw data from the FBREF website at the individual season level using CSS selectors from the HTML response.

    Attributes:
        data_extract_css_components_dict (dict): CSS selectors to extract the individual player statistics
    """

    def __init__(self):
        self.data_extract_css_components_dict = {
            "date": "th>a[href*= '/en/matches/']",
            "day_of_the_week": "td[data-stat='dayofweek'][class='left']",
            "competition": "td[data-stat='comp']>a",
            "round": "td[data-stat='round']>a",
            "venue": "td[data-stat='venue'][class='left']",
            "result": "td[data-stat='result'][class='center']",
            "squad": "td[data-stat='team']>a",
            "opponent": "td[data-stat='opponent']>a",
            "game_started": "td[data-stat='game_started'][class='center']",
            "position": "td[data-stat='position']",
            "minutes": "td[data-stat='minutes'][class='right']",
            "goals": "td[data-stat='goals']",
            "assists": "td[data-stat='assists']",
            "pens_made": "td[data-stat='pens_made']",
            "pens_attempted": "td[data-stat='pens_att']",
            "shots_total": "td[data-stat='shots']",
            "shots_on_target": "td[data-stat='shots_on_target']",
            "cards_yellow": "td[data-stat='cards_yellow']",
            "cards_red": "td[data-stat='cards_red']",
            "fouls": "td[data-stat='fouls']",
            "fouled": "td[data-stat='fouled']",
            "offsides": "td[data-stat='offsides']",
            "crosses": "td[data-stat='crosses']",
            "tackles_won": "td[data-stat='tackles_won']",
            "interceptions": "td[data-stat='interceptions']",
            "own_goals": "td[data-stat='own_goals']",
            "touches": "td[data-stat='touches']",
            "tackle": "td[data-stat='tackles']",
            "interceptions": "td[data-stat='interceptions']",
            "blocks": "td[data-stat='blocks']",
            "shot_creating_actions": "td[data-stat='sca']",
            "goal-creating_actions": "td[data-stat='gca']",
            "passes_completed": "td[data-stat='passes_completed']",
            "passes_attempted": "td[data-stat='passes']",
            "carries": "td[data-stat='carries']",
        }

    def search_player_season_data(
        self, link_list: list, player_name_dict: dict
    ) -> pd.DataFrame:
        """
        Searches the player's individual season link for the CSS selectors defined in the __init__ method and saves the values in
        a dataframe.

        Args:
            link_list (list): List of a link that represetnts the players main homepage that will be parsed for their season level links
            player_name_dict (dict): Dictionary with the stored formatted names

        Returns:
            store_data (pd.DataFrame): Dataframe with the stored fields and values extracted from the player's individual season
        """
        store_data = pd.DataFrame()

        for link in link_list:
            player_link_request = requests.get(link)

            print(player_link_request)
            print(link)
            print("\n\n\n")

            time.sleep(3)

            player_link_text = player_link_request.text
            soup_player_link_text = BeautifulSoup(
                player_link_text, features="html.parser"
            )

            css_extraction = f"table[id = 'matchlogs_all']>tbody>tr:not([class='spacer partial_table'])"
            extracted_data_list = soup_player_link_text.select(css_extraction)

            for data_value in extracted_data_list:
                row_text = BeautifulSoup(str(data_value), features="html.parser")
                store_data_dic = {}

                for key, value in self.data_extract_css_components_dict.items():
                    rows = row_text.select(value)
                    clean_data_list_1 = [
                        single_value.text.strip() for single_value in rows
                    ]

                    if len(clean_data_list_1) == 0:
                        clean_data_list_1 = [""]

                    store_data_dic[key] = clean_data_list_1[0]

                data_row = pd.DataFrame(store_data_dic, index=[0])
                store_data = pd.concat(
                    [store_data, data_row], axis=0, ignore_index=True
                )

        player_name_value = player_name_dict["raw_name"]
        store_data["player_name"] = player_name_value

        return store_data

    def execute_individual_player_data_extract(
        self, link_list: list, player_name_dict: dict
    ) -> pd.DataFrame:
        """
        Executes the process to extract the individual player's data from their specified season links.

        Args:
            link_list (list): List of a link that represetnts the players main homepage that will be parsed for their season level links
            player_name_dict (dict): Dictionary with the stored formatted names

        Returns:
            player_data_df (pd.DataFrame): Dataframe with the stored fields and values extracted from the player's individual season
        """
        player_data_df = self.search_player_season_data(
            link_list=link_list, player_name_dict=player_name_dict
        )

        return player_data_df
