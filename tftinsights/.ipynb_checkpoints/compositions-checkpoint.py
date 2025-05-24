import pandas as pd
import numpy as np
import requests
import warnings
from .config import DATA_DRAGON_VERSION, UNIT_PREFIX 

def conditional_prob_unit_check ( conditional_units, target_unit , df:pd.DataFrame ):
    has_rows = df[df[conditional_units].ge(1).all(axis=1)]
    if has_rows.shape[0] == 0:
        warnings.warn(f"Nummber of rows containing the conditional units are zero. The conditional units are: {conditional_units}", category=UserWarning)
        
    non_zero_count = ((has_rows[conditional_units].ge(1).all(axis=1) >= 1) & (has_rows[target_unit] >= 1)).sum() / has_rows.shape[0]
    return non_zero_count

def build_conditional_comp ( team_size, conditional_units, unit_pool:list, df:pd.DataFrame, association_threshold = 1 ):

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
    # print ( conditional_units )
    # print ( target_prob[best_unit] )
    if target_prob[best_unit] <= association_threshold:
        print (f"{best_unit} is a weak recommendation.")
    
    unit_pool_current.remove ( best_unit )
    conditional_units.append(best_unit)
    return build_conditional_comp ( team_size,conditional_units, unit_pool_current, df, association_threshold )

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

    # print ( target_prob )
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
