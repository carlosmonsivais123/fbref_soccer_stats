from fbref_data_extraction.player_search import FBREFPlayerSearch

# Extracts the data from FBREF
player_search_raw_df = FBREFPlayerSearch().execute_fbref_player_search_stats(
    raw_player_name="Lionel Messi"
)
