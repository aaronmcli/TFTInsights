import pandas as pd
import numpy as np
import requests

DATA_DRAGON_VERSION = '15.9.1'
UNIT_PREFIX = "unit_TFT14_"

def conditional_prob_unit_check ( conditional_units, target_unit , df:pd.DataFrame ):
    has_rows = df[df[conditional_units].ge(1).all(axis=1)]

    non_zero_count = ((has_rows[conditional_units].ge(1).all(axis=1) >= 1) & (has_rows[target_unit] >= 1)).sum() / \
                     has_rows.shape[0]
    return non_zero_count

def build_conditional_comp ( team_size, conditional_units, unit_pool:list, df:pd.DataFrame ):

    conditional_units = [
        unit if unit.startswith(UNIT_PREFIX) else f"unit_TFT14_{unit}"
        for unit in conditional_units
    ]
    
    if len ( conditional_units ) >= team_size:
        return conditional_units

    unit_pool_current = unit_pool.copy()
    unit_pool_current = [u for u in unit_pool_current if u not in conditional_units]
    
    target_prob = { target: conditional_prob_unit_check (conditional_units,target, df) for target in unit_pool_current}
    best_unit = max( target_prob, key=target_prob.get )
    
    unit_pool_current.remove ( best_unit )
    conditional_units.append(best_unit)
    return build_conditional_comp ( team_size,conditional_units, unit_pool_current, df )

def build_naive_conditional_comp ( team_size, conditional_units, unit_pool, pre_computed_conditional_prob:pd.DataFrame ):
    
    conditional_units = [
        unit if unit.startswith(UNIT_PREFIX) else f"unit_TFT14_{unit}"
        for unit in conditional_units
    ]

    if len ( conditional_units ) >= team_size:
        return conditional_units
        
    unit_pool_current = unit_pool.copy()
    unit_pool_current = [u for u in unit_pool_current if u not in conditional_units]

    #print ( unit_pool_current )
    target_prob =  { target: average_conditional_prob (conditional_units,target, pre_computed_conditional_prob) for target in unit_pool_current}

    #print ( target_prob )
    best_unit = max( target_prob, key=target_prob.get )
    unit_pool_current.remove ( best_unit )
    conditional_units.append(best_unit)
    unit_pool_current = unit_pool.copy()
    return build_naive_conditional_comp ( team_size, conditional_units, unit_pool_current, pre_computed_conditional_prob )

def average_conditional_prob ( conditonal_units, target_unit,  pre_computed_conditional_prob:pd.DataFrame ):

    subset = pre_computed_conditional_prob.loc[
        pre_computed_conditional_prob.index.intersection(conditonal_units),
        pre_computed_conditional_prob.columns.intersection([target_unit])
    ]   
    return subset.mean().mean()

def get_mapping_table_for_units():
    url = f"https://ddragon.leagueoflegends.com/cdn/{DATA_DRAGON_VERSION}/data/en_US/tft-champion.json"
    response = requests.get(url)
    data = response.json()
    champions_dict = data['data']  # Dictionary of champions keyed by their names
    champion_list = list(champions_dict.values())
    df = pd.DataFrame(champion_list)
    df = df[df['id'].str.contains('TFT14_')]
    df['id'] = "trait_" + df['id']
    df.drop("image", axis=1, inplace=True)
    return df

def get_mapping_table_for_traits():
    url = f"https://ddragon.leagueoflegends.com/cdn/{DATA_DRAGON_VERSION}/data/en_US/tft-trait.json"
    response = requests.get(url)
    data = response.json()
    trait_dict = data['data']  # Dictionary of champions keyed by their names
    trait_list = list(trait_dict.values())
    df = pd.DataFrame(trait_list)
    df = df[df['id'].str.contains('TFT14_')]
    df['id'] = "unit_" + df['id']
    df.drop("image", axis=1, inplace=True)
    return df