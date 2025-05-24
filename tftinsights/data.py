import pandas as pd
import numpy as np
from tftinsights.units import get_summon_units
from .config import hot_encode_csv

def get_tft_dataset ( include_traits  =True, include_units =True, include_items =True, include_units_item=False, ranked_queue=True, include_player_data=True, rankFilter=""):
    """ This function ensures we are getting the same dataset everytime we are calling it in our numerious notebooks"""
    
    df = pd.read_csv(hot_encode_csv, low_memory=False)
    if ranked_queue:
        df = df[df['queue_id']== 1100].copy() #ranked data only


    #remove summoned units
    summonUnits = get_summon_units()
    df.drop(summonUnits,axis='columns',inplace=True)
    
    # This one-hot dataset has too many dimensions. we need to reduce it
    # switching to bag of tokens / words approach 
    column_key = list(df.keys())
    
    
    #item_TFT5_Item_LastWhisperRadiant	item_TFT5_Item_LeviathanRadiant	item_TFT5_Item_MorellonomiconRadiant	item_TFT5_Item_NightHarvesterRadiant	item_TFT5_Item_QuicksilverRadiant	item_TFT5_Item_RabadonsDeathcapRadiant
    item_columns = [item for item in column_key if (  item.startswith('item_' )) ]
    
    
    #unit_TFT14_Graves	unit_TFT14_Illaoi	unit_TFT14_Jarvan	unit_TFT14_Jax	unit_TFT14_Jhin	unit_TFT14_Jinx
    unit_column = [item for item in column_key if (   "unit_" in item  ) ]

    #trait_TFT14_AnimaSquad	trait_TFT14_Armorclad	trait_TFT14_BallisTek	trait_TFT14_Bruiser	trait_TFT14_Controller
    traits_column = [item for item in column_key if (   "trait_" in item ) ]

    # ie TFT14_Gragas_item_1	TFT14_Gragas_item_2	TFT14_Graves_item_0	TFT14_Graves_item_1	TFT14_Graves_item_2
    unit_item_column = [item for item in column_key if (  item.endswith('_item_0') or  item.endswith('_item_1') or  item.endswith('_item_2') )]
    df[unit_item_column] = df[unit_item_column].fillna(0)
    
    player_data_column = [item for item in column_key if (   item not in item_columns 
                                                         and item not in unit_column
                                                         and item not in traits_column
                                                         and item not in unit_item_column) ]

    # Determine which columns to keep
    columns_to_keep = []
    if include_items:
        columns_to_keep += item_columns
        
    if include_traits:
        columns_to_keep += traits_column
        
    if include_units:
        columns_to_keep += unit_column
        
    if include_units_item:
        columns_to_keep += unit_item_column
        
    if include_player_data:
        columns_to_keep += player_data_column
    else:
        columns_to_keep += ["placement"]

        # Optional rank filtering if provided (e.g., "Gold", "Platinum")
    if rankFilter:
        if "rank_at_match_time.tier" in df.columns:
            if isinstance(rankFilter, list):
                df = df[df["rank_at_match_time.tier"].isin(rankFilter)]
            else:
                df = df[df["rank_at_match_time.tier"].str.contains(rankFilter, na=False)]
        else:
            import warnings
            warnings.warn("No column for ranked information found.")
            
    df = df[columns_to_keep].copy()

    return df 