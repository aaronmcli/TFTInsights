import pandas as pd
import numpy as np
import requests
from .config import DATA_DRAGON_VERSION

def get_mapping_table_for_units():
    url = f"https://ddragon.leagueoflegends.com/cdn/{DATA_DRAGON_VERSION}/data/en_US/tft-champion.json"
    response = requests.get(url)
    data = response.json()
    champions_dict = data['data']  # Dictionary of champions keyed by their names
    champion_list = list(champions_dict.values())
    df = pd.DataFrame(champion_list)
    df = df[df['id'].str.contains('TFT14_')]
    #df['id'] = "unit_" + df['id']
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
    df['id'] = df['id']
    df.drop("image", axis=1, inplace=True)
    return df
    
units_dict = [
    {"name": "Alistar", "traits": ["Golden Ox", "Bruiser"], "cost": 1, "unitplannerid": 786 },
    {"name": "Annie", "traits": ["Golden Ox", "A.M.P."], "cost": 4, "unitplannerid": 790},
    {"name": "Aphelios", "traits": ["Golden Ox", "Marksman"], "cost": 4, "unitplannerid": 1818},
    {"name": "Aurora", "traits": ["Anima Squad", "Dynamo"], "cost": 5, "unitplannerid": 781},
    {"name": "Brand", "traits": ["Street Demon", "Techie"], "cost": 4, "unitplannerid": 737},
    {"name": "Braum", "traits": ["Syndicate", "Vanguard"], "cost": 3, "unitplannerid": 760},
    {"name": "Cho'Gath", "traits": ["BoomBots", "Bruiser"], "cost": 4, "unitplannerid": 778},
    {"name": "Darius", "traits": ["Syndicate", "Bruiser"], "cost": 2, "unitplannerid": 738},
    {"name": "Draven", "traits": ["Cypher", "Rapidfire"], "cost": 3, "unitplannerid": 796},
    {"name": "Dr. Mundo", "traits": ["Street Demon", "Bruiser", "Slayer"], "cost": 1, "unitplannerid": 739 },
    {"name": "Ekko", "traits": ["Street Demon", "Strategist"], "cost": 2, "unitplannerid": 799},
    {"name": "Elise", "traits": ["Nitro", "Dynamo"], "cost": 3, "unitplannerid": 740},
    {"name": "Fiddlesticks", "traits": ["BoomBots", "Techie"], "cost": 3, "unitplannerid": 741},
    {"name": "Galio", "traits": ["Cypher", "Bastion"], "cost": 3, "unitplannerid": 742},
    {"name": "Garen", "traits": ["God of the Net"], "cost": 5, "unitplannerid": 743},
    {"name": "Gragas", "traits": ["Divinicorp", "Bruiser"], "cost": 3, "unitplannerid": 770},
    {"name": "Graves", "traits": ["Golden Ox", "Executioner"], "cost": 2, "unitplannerid": 789},
    {"name": "Illaoi", "traits": ["Anima Squad", "Bastion"], "cost": 2, "unitplannerid": 765},
    {"name": "Jarvan IV", "traits": ["Golden Ox", "Vanguard", "Slayer"], "cost": 3, "unitplannerid": 788},
    {"name": "Jax", "traits": ["Exotech", "Bastion"], "cost": 1, "unitplannerid": 773},
    {"name": "Jhin", "traits": ["Exotech", "Marksman", "Dynamo"], "cost": 2, "unitplannerid": 768},
    {"name": "Jinx", "traits": ["Street Demon", "Marksman"], "cost": 3, "unitplannerid": 798},
    {"name": "Kindred", "traits": ["Nitro", "Rapidfire", "Marksman"], "cost": 1, "unitplannerid": 763},
    {"name": "Kobuko", "traits": ["Cyberboss", "Bruiser"], "cost": 5, "unitplannerid": 774},
    {"name": "Kog'Maw", "traits": ["BoomBots", "Rapidfire"], "cost": 1, "unitplannerid": 771},
    {"name": "LeBlanc", "traits": ["Cypher", "Strategist"], "cost": 2, "unitplannerid": 744},
    {"name": "Leona", "traits": ["Anima Squad", "Vanguard"], "cost": 4, "unitplannerid": 783},
    {"name": "Miss Fortune", "traits": ["Syndicate", "Dynamo"], "cost": 4, "unitplannerid": 745},
    {"name": "Mordekaiser", "traits": ["Exotech", "Bruiser", "Techie"], "cost": 3, "unitplannerid": 785},
    {"name": "Morgana", "traits": ["Divinicorp", "Dynamo"], "cost": 1, "unitplannerid": 746},
    {"name": "Naafiri", "traits": ["Exotech", "A.M.P."], "cost": 2, "unitplannerid": 769},
    {"name": "Neeko", "traits": ["Street Demon", "Strategist"], "cost": 4, "unitplannerid": 747},
    {"name": "Nidalee", "traits": ["Nitro", "A.M.P."], "cost": 1, "unitplannerid": 761},
    {"name": "Poppy", "traits": ["Cyberboss", "Bastion"], "cost": 1, "unitplannerid": 776},
    {"name": "Renekton", "traits": ["Overlord", "Divinicorp", "Bastion"], "cost": 5, "unitplannerid": 748},
    {"name": "Rengar", "traits": ["Street Demon", "Executioner"], "cost": 3, "unitplannerid": 749},
    {"name": "Rhaast", "traits": ["Divinicorp", "Vanguard"], "cost": 2, "unitplannerid": 791},
    {"name": "Samira", "traits": ["Street Demon", "A.M.P."], "cost": 5, "unitplannerid": 750},
    {"name": "Sejuani", "traits": ["Exotech", "Bastion"], "cost": 4, "unitplannerid": 775},
    {"name": "Senna", "traits": ["Divinicorp", "Slayer"], "cost": 3, "unitplannerid": 751},
    {"name": "Seraphine", "traits": ["Anima Squad", "Techie"], "cost": 1, "unitplannerid": 766},
    {"name": "Shaco", "traits": ["Syndicate", "Slayer"], "cost": 1, "unitplannerid": 752},
    {"name": "Shyvana", "traits": ["Nitro", "Bastion", "Techie"], "cost": 2, "unitplannerid": 762},
    {"name": "Skarner", "traits": ["BoomBots", "Vanguard"], "cost": 2, "unitplannerid": 772},
    {"name": "Sylas", "traits": ["Anima Squad", "Vanguard"], "cost": 1, "unitplannerid": 780},
    {"name": "Twisted Fate", "traits": ["Syndicate", "Rapidfire"], "cost": 2, "unitplannerid": 753},
    {"name": "Urgot", "traits": ["BoomBots", "Executioner"], "cost": 5, "unitplannerid": 779},
    {"name": "Varus", "traits": ["Exotech", "Executioner"], "cost": 3, "unitplannerid": 754},
    {"name": "Vayne", "traits": ["Anima Squad", "Slayer"], "cost": 2, "unitplannerid": 782},
    {"name": "Veigar", "traits": ["Cyberboss", "Techie"], "cost": 2, "unitplannerid": 755},
    {"name": "Vex", "traits": ["Divinicorp", "Executioner"], "cost": 4, "unitplannerid": 756},
    {"name": "Vi", "traits": ["Cypher", "Vanguard"], "cost": 1, "unitplannerid": 784},
    {"name": "Viego", "traits": ["Soul Killer", "Golden Ox", "Techie"], "cost": 5, "unitplannerid": 787},
    {"name": "Xayah", "traits": ["Anima Squad", "Marksman"], "cost": 4, "unitplannerid": 767},
    {"name": "Yuumi", "traits": ["Anima Squad", "A.M.P.", "Strategist"], "cost": 3, "unitplannerid": 764},
    {"name": "Zac", "traits": ["Virus"], "cost": 5, "unitplannerid": 797},
    {"name": "Zed", "traits": ["Cypher", "Slayer"], "cost": 4, "unitplannerid": 757},
    {"name": "Zeri", "traits": ["Exotech", "Rapidfire"], "cost": 4, "unitplannerid": 758},
    {"name": "Ziggs", "traits": ["Cyberboss", "Strategist"], "cost": 4, "unitplannerid": 777},
    {"name": "Zyra", "traits": ["Street Demon", "Techie"], "cost": 1, "unitplannerid": 759}
]
unit_df = pd.DataFrame(units_dict)
unit_df[['trait_1', 'trait_2', 'trait_3']] = unit_df['traits'].apply(pd.Series)
unit_df['id'] = unit_df['name'].map(get_mapping_table_for_units().set_index('name')['id'])



def get_unitplanneer_code ( target ):
    df = unit_df
    #print ( df )
    #h =  int ( df[df['name']== target ]['unitplannerid'].iloc[0] )
    return  f"{int ( df[df['id']== target ]['unitplannerid'].iloc[0] ):x}"

def get_unitplanneer_code_comp ( target_list ):
    code = "02"
    for t in target_list:
        code = code + ( get_unitplanneer_code (t) )

    zero_to_fill = 3*10 + 2 - len(code)
    for _ in range ( zero_to_fill ):
        code = code + "0"
    code = code + "TFTSet14"
    return code

#Get a list of all units
def get_unit_list (traits="",cost="", units_only=False, add_prefix=False):
    filter_df = unit_df
    if cost:
        # Convert cost string like "12" into [1, 2]
        if isinstance(cost, str):
            cost_include = [int(c) for c in cost if c.isdigit()]
        elif isinstance(cost, (list, tuple, set)):
            cost_include = list(map(int, cost))
        else:
            cost_include = [int(cost)]

        filter_df = filter_df[filter_df['cost'].isin(cost_include)]

    if traits:
        if isinstance(traits, str):
            traits = [traits]
            #Logical OR
            trait_columns = [col for col in filter_df.columns if col.startswith('trait_')]
            filter_df = filter_df[filter_df[trait_columns].apply(lambda row: any(trait in row.values for trait in traits), axis=1)]            
            # filter_df = filter_df[ filter_df[['trait1', 'trait2', 'trait3']].apply(lambda row: trait in set(row), axis=1) ] #Logical AND logic
            
    if units_only:
        filter_df = filter_df['id'].astype(str)
        if add_prefix:
            filter_df = "unit_" + filter_df
            #filter_df = filter_df[  filter_df[['trait1', 'trait2', 'trait3']].apply(lambda row: set(trait).issubset(set(row)), axis=1)] #interaction
    
    if isinstance(filter_df, pd.DataFrame):
        filter_df = filter_df.sort_values(by='cost', ascending=True)
    else:
        filter_df.sort_values(ascending=True, inplace=True)
        
    return filter_df


def count_traits ( unit_list ):    
    
    #Counts the total trait in a list of units provided. 
    #Cleans the listif it is accidentally prefixed with "unit_"    
    
    unit_list = [ u.replace('unit_','') for u in unit_list ]    
    unit_df = get_unit_list()        
    df = unit_df[unit_df['id'].isin(unit_list)]    
    traits_column = [ col for col in unit_df.columns if col.startswith('trait_')  ]    
    value_counts = df[traits_column].stack().value_counts()
    return value_counts

def count_trait_level ( unit_list ):
    
    #Cleans the listif it is accidentally prefixed with "unit_"    
    unit_list = [ u.replace('unit_','') for u in unit_list ] 
    traits_count = count_traits ( unit_list )
    
    #unit_df['id'] = unit_df['name'].map(get_mapping_table_for_units().set_index('name')['id'])
    trait_csv_df = pd.read_csv('csv/traits_csv.csv') # contains level information
    
    traits_count.index = traits_count.index.map(trait_mapping)
    #clean this table incase its still dirty
    trait_csv['trait'] = trait_csv['trait'].apply(lambda  trait: trait.replace('trait_',''))
    
    trait_mapping = get_mapping_table_for_traits()
    
    