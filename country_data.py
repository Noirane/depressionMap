'''
1: AE
2: AR
3: AT
4: AU
5: BE
6: BN
7: BR
8: CA
9: CH
10: CZ
11: DE
12: DK
13: EG
14: ES
15: FI
16: FR
17: GB
18: GR
19: HK
20: HR
21: HU
22: ID
23: IE
24: IN
25: IT
26: JM
27: JP
28: MX
29: MY
30: NL
31: NO
32: NZ
33: PH
34: PK
35: PL
36: PT
37: RO
38: RS
39: RU
40: SA
41: SE
42: SG
43: TR
44: US
45: VN
46: ZA'''

country_mapping = {
    1: 'United Arab Emirates',
    2: 'Argentina',
    3: 'Austria',
    4: 'Australia',
    5: 'Belgium',
    6: 'Brunei',
    7: 'Brazil',
    8: 'Canada',
    9: 'Switzerland',
    10: 'Czech Republic',
    11: 'Germany',
    12: 'Denmark',
    13: 'Egypt',
    14: 'Spain',
    15: 'Finland',
    16: 'France',
    17: 'United Kingdom',
    18: 'Greece',
    19: 'Hong Kong',
    20: 'Croatia',
    21: 'Hungary',
    22: 'Indonesia',
    23: 'Ireland',
    24: 'India',
    25: 'Italy',
    26: 'Jamaica',
    27: 'Japan',
    28: 'Mexico',
    29: 'Malaysia',
    30: 'Netherlands',
    31: 'Norway',
    32: 'New Zealand',
    33: 'Philippines',
    34: 'Pakistan',
    35: 'Poland',
    36: 'Portugal',
    37: 'Romania',
    38: 'Serbia',
    39: 'Russia',
    40: 'Saudi Arabia',
    41: 'Sweden',
    42: 'Singapore',
    43: 'Turkey',
    44: 'United States of America',
    45: 'Vietnam',
    46: 'South Africa'
}

country_coords = {
    'United Arab Emirates': [23.4241, 53.8478],
    'Argentina': [-38.4161, -63.6167],
    'Austria': [47.5162, 14.5501],
    'Australia': [-25.2744, 133.7751],
    'Belgium': [50.8503, 4.3517],
    'Brunei Darussalam': [4.5353, 114.7277],
    'Brazil': [-14.2350, -51.9253],
    'Canada': [56.1304, -106.3468],
    'Switzerland': [46.8182, 8.2275],
    'Czechia': [49.8175, 15.4730],
    'Germany': [51.1657, 10.4515],
    'Denmark': [56.2639, 9.5018],
    'Egypt': [26.8205, 30.8025],
    'Spain': [40.4637, -3.7492],
    'Finland': [61.9241, 25.7482],
    'France': [46.6034, 1.8883],
    'United Kingdom': [55.3781, -3.4360],
    'Greece': [39.0742, 21.8243],
    'Hong Kong': [22.3964, 114.1095],
    'Croatia': [45.1, 15.2],
    'Hungary': [47.1625, 19.5033],
    'Indonesia': [-0.7893, 113.9213],
    'Ireland': [53.4129, -8.2439],
    'India': [20.5937, 78.9629],
    'Italy': [41.8719, 12.5674],
    'Jamaica': [18.1096, -77.2975],
    'Japan': [36.2048, 138.2529],
    'Mexico': [23.6345, -102.5528],
    'Malaysia': [4.2105, 101.9758],
    'Netherlands': [52.1326, 5.2913],
    'Norway': [60.4720, 8.4689],
    'New Zealand': [-40.9006, 174.8860],
    'Philippines': [12.8797, 121.7740],
    'Pakistan': [30.3753, 69.3451],
    'Poland': [51.9194, 19.1451],
    'Portugal': [39.3999, -8.2245],
    'Romania': [45.9432, 24.9668],
    'Serbia': [44.0165, 21.0059],
    'Russia': [61.5240, 105.3188],
    'Saudi Arabia': [23.8859, 45.0792],
    'Sweden': [60.1282, 18.6435],
    'Singapore': [1.3521, 103.8198],
    'Turkey': [38.9637, 35.2433],
    'United States': [37.0902, -95.7129],
    'Vietnam': [14.0583, 108.2772],
    'South Africa': [-30.5595, 22.9375]
}
