FG_FILES = '../Data/FG/'
H_FILES = '../Data/H/'

LIST_OF_QUESTIONS = '../Data/Helpers/List_of_questions.xlsx'
PAIRED_SESSIONS = '../Data/Helpers/Paired_sessions.xlsx'

SESSION_EVENTS_FROM_BAKED_JSON = '../Data/Session_events/session_events_from_baked.json'
SESSION_METRICS_FROM_BAKED_JSON = '../Data/Session_events/session_metrics_from_baked.json'
MERGED_DATA_FROM_BAKED_JSON = '../Data/Session_events/merged_data_from_baked.json'

LIMESURVEY_FG = '../Data/Limesurvey_data/220405-FG-v0.csv'
LIMESURVEY_H = '../Data/Limesurvey_data/220405-H-v0.csv'
ALL_LIMESURVEY_DATA = '../Data/Limesurvey_data/All_Limesurvey_data.xlsx'

CLEANED_DATASET_JSON_INTERMEDIATE = '../Data/Prepared_datasets/clean_dataset_intermediate.json'
CLEANED_DATASET_XLSX_PREVIEW_INTERMEDIATE = '../Data/Prepared_datasets/clean_dataset_intermediate.xlsx'
DATASET_ONE_PV_PER_ONE_ROW = '../Data/Prepared_datasets/dataset_one_pv_per_one_row.json'

REPORTS = './Reports/'
CONSTANT_DATASET_FOR_VALIDATION = '../Data/Prepared_datasets/Constant_dataset_for_validation/'

COLUMNS_STATIC = [ 
                  'mean_points', 
                  'mean_bfi2_e',
                  'mean_bfi2_a',
                  'mean_bfi2_c',
                  'mean_bfi2_n',
                  'mean_bfi2_e_sociability',
                  'mean_bfi2_e_assertiveness',
                  'mean_bfi2_e_energy_level',
                  'mean_bfi2_a_compassion',
                  'mean_bfi2_a_respectfulness',
                  'mean_bfi2_a_trust',
                  'mean_bfi2_c_organization',
                  'mean_bfi2_c_productiveness',
                  'mean_bfi2_c_responsibility',
                  'mean_bfi2_n_anxiety',
                  'mean_bfi2_n_depression',
                  'mean_bfi2_n_emotional_volatility'
]

BIG5_MEAN_COLS = [
                'big5_mean_time', 
                'big5_mean_duration', 
                'big5_mean_distance',
                'big5_mean_x_axis_distance',
                'big5_mean_y_axis_distance',
                'big5_mean_real_ideal_trajectory_diff',
                'big5_mean_max_deviation',
                'big5_mean_velocity', 
                'big5_mean_x_axis_vel', 
                'big5_mean_y_axis_vel', 
                'big5_mean_acc', 
                'big5_mean_x_axis_acc', 
                'big5_mean_y_axis_acc', 
                'big5_mean_auc_diff', 
                'big5_mean_clicks', 
                'big5_mean_x_flips', 
                'big5_mean_y_flips',
                'big5_mean_init_time', 
                'big5_mean_react_time'
            ]
BIG5_SUM_COLS = [   
                'big5_sum_visits',
                'big5_sum_scrolling',
                'big5_sum_x_flips', 
                'big5_sum_y_flips'
            ]

DEM_MEAN_COLS = [
                'dem_mean_time', 
                'dem_mean_duration', 
                'dem_mean_distance',
                'dem_mean_x_axis_distance',
                'dem_mean_y_axis_distance',
                'dem_mean_real_ideal_trajectory_diff',
                'dem_mean_max_deviation',
                'dem_mean_velocity', 
                'dem_mean_x_axis_vel', 
                'dem_mean_y_axis_vel', 
                'dem_mean_acc', 
                'dem_mean_x_axis_acc', 
                'dem_mean_y_axis_acc', 
                'dem_mean_auc_diff', 
                'dem_mean_clicks', 
                'dem_mean_x_flips', 
                'dem_mean_y_flips',
                'dem_mean_init_time', 
                'dem_mean_react_time'
            ]
DEM_SUM_COLS = [
                'dem_sum_visits',
                'dem_sum_scrolling',
                'dem_sum_x_flips', 
                'dem_sum_y_flips'
            ]