# Original problem: kset_u40_n100_k5

This file records the exact original binary packing problem used for the matching run result.

## Optimization model

\[
\max_{x\in\{0,1\}^n}\ \sum_{i=1}^n w_i x_i
\qquad\text{s.t.}\qquad
\sum_{i\in S_k} x_i \le B_k,\quad k=1,\dots,m.
\]

- Number of variables: `100`
- Number of constraints: `40`
- Matching run-result file: `result.json`

## Metadata

- `generator`: `random_k_set_packing`
- `universe_size`: `40`
- `k`: `5`
- `density`: `1.0`

## Weights

w_1=1.2351921, w_2=0.59130489, w_3=0.7513369, w_4=0.81608164, w_5=1.1155269, w_6=1.995072, w_7=0.96880856, w_8=1.4733759, w_9=1.2686446, w_10=1.7194176, w_11=1.1991192, w_12=0.99230857, w_13=0.63416077, w_14=1.1160725, w_15=0.57876277, w_16=1.043469, w_17=0.88289401, w_18=1.4654343, w_19=1.3191682, w_20=1.71303, w_21=0.95175029, w_22=0.98679899, w_23=0.69710848, w_24=1.417869, w_25=1.7136227, w_26=0.7372261, w_27=1.6661273, w_28=1.843701, w_29=0.93529978, w_30=1.832286, w_31=1.9391386, w_32=0.63095994, w_33=1.3377698, w_34=1.6530631, w_35=1.7959406, w_36=0.75574796, w_37=1.8652969, w_38=1.279528, w_39=1.5163078, w_40=0.56425268, w_41=0.85844244, w_42=0.84908747, w_43=1.1770721, w_44=1.1948424, w_45=0.72672596, w_46=1.1978078, w_47=1.0199882, w_48=1.4966034, w_49=1.0536321, w_50=0.88987154, w_51=0.60814813, w_52=1.8205611, w_53=1.1367723, w_54=0.7339999, w_55=1.6801776, w_56=0.86328632, w_57=0.55600288, w_58=0.82249555, w_59=1.9221643, w_60=1.0250581, w_61=1.7320894, w_62=1.9694653, w_63=1.4711938, w_64=0.76025288, w_65=0.61415414, w_66=1.5501828, w_67=1.4125593, w_68=1.1849788, w_69=0.6688834, w_70=1.1244522, w_71=1.7377329, w_72=1.6218287, w_73=0.57174007, w_74=1.7760546, w_75=1.6726101, w_76=1.2479595, w_77=1.9419859, w_78=1.374804, w_79=1.5930078, w_80=0.79119757, w_81=0.63820392, w_82=1.7309168, w_83=1.7835111, w_84=0.84535984, w_85=1.3735275, w_86=1.8509273, w_87=0.90212274, w_88=1.0650664, w_89=1.5428936, w_90=1.7664634, w_91=0.66830351, w_92=0.70700114, w_93=1.030389, w_94=1.9196694, w_95=1.8020731, w_96=0.77012346, w_97=0.85115449, w_98=1.6480575, w_99=1.6512647, w_100=0.9926899

## Candidate sets (variables)

- Variable `x_1` corresponds to set `A_1 = {9, 13, 18, 19, 29}`
- Variable `x_2` corresponds to set `A_2 = {4, 6, 25, 28, 35}`
- Variable `x_3` corresponds to set `A_3 = {1, 11, 13, 27, 33}`
- Variable `x_4` corresponds to set `A_4 = {18, 25, 26, 32, 40}`
- Variable `x_5` corresponds to set `A_5 = {1, 7, 13, 20, 26}`
- Variable `x_6` corresponds to set `A_6 = {15, 16, 19, 24, 28}`
- Variable `x_7` corresponds to set `A_7 = {14, 23, 31, 36, 38}`
- Variable `x_8` corresponds to set `A_8 = {18, 28, 30, 33, 34}`
- Variable `x_9` corresponds to set `A_9 = {15, 18, 28, 36, 38}`
- Variable `x_10` corresponds to set `A_10 = {6, 16, 27, 34, 39}`
- Variable `x_11` corresponds to set `A_11 = {2, 5, 9, 19, 35}`
- Variable `x_12` corresponds to set `A_12 = {20, 21, 24, 29, 34}`
- Variable `x_13` corresponds to set `A_13 = {4, 15, 17, 25, 27}`
- Variable `x_14` corresponds to set `A_14 = {4, 5, 31, 33, 39}`
- Variable `x_15` corresponds to set `A_15 = {1, 8, 13, 27, 35}`
- Variable `x_16` corresponds to set `A_16 = {4, 7, 14, 21, 40}`
- Variable `x_17` corresponds to set `A_17 = {2, 23, 24, 27, 28}`
- Variable `x_18` corresponds to set `A_18 = {6, 23, 28, 37, 40}`
- Variable `x_19` corresponds to set `A_19 = {11, 14, 32, 36, 37}`
- Variable `x_20` corresponds to set `A_20 = {12, 17, 26, 29, 38}`
- Variable `x_21` corresponds to set `A_21 = {15, 17, 18, 19, 20}`
- Variable `x_22` corresponds to set `A_22 = {1, 8, 25, 27, 36}`
- Variable `x_23` corresponds to set `A_23 = {8, 10, 17, 38, 40}`
- Variable `x_24` corresponds to set `A_24 = {1, 18, 22, 27, 35}`
- Variable `x_25` corresponds to set `A_25 = {5, 7, 8, 10, 25}`
- Variable `x_26` corresponds to set `A_26 = {5, 10, 20, 21, 27}`
- Variable `x_27` corresponds to set `A_27 = {4, 6, 8, 20, 40}`
- Variable `x_28` corresponds to set `A_28 = {6, 8, 12, 20, 32}`
- Variable `x_29` corresponds to set `A_29 = {2, 20, 27, 28, 34}`
- Variable `x_30` corresponds to set `A_30 = {5, 11, 27, 30, 33}`
- Variable `x_31` corresponds to set `A_31 = {2, 4, 10, 12, 28}`
- Variable `x_32` corresponds to set `A_32 = {1, 8, 24, 25, 33}`
- Variable `x_33` corresponds to set `A_33 = {2, 25, 35, 36, 39}`
- Variable `x_34` corresponds to set `A_34 = {2, 3, 9, 13, 30}`
- Variable `x_35` corresponds to set `A_35 = {4, 26, 37, 39, 40}`
- Variable `x_36` corresponds to set `A_36 = {18, 19, 26, 37, 40}`
- Variable `x_37` corresponds to set `A_37 = {10, 25, 28, 35, 37}`
- Variable `x_38` corresponds to set `A_38 = {8, 11, 17, 32, 35}`
- Variable `x_39` corresponds to set `A_39 = {13, 33, 36, 38, 40}`
- Variable `x_40` corresponds to set `A_40 = {1, 11, 18, 32, 34}`
- Variable `x_41` corresponds to set `A_41 = {10, 12, 19, 28, 38}`
- Variable `x_42` corresponds to set `A_42 = {6, 9, 32, 33, 36}`
- Variable `x_43` corresponds to set `A_43 = {4, 6, 36, 38, 39}`
- Variable `x_44` corresponds to set `A_44 = {4, 23, 28, 35, 39}`
- Variable `x_45` corresponds to set `A_45 = {13, 21, 22, 34, 37}`
- Variable `x_46` corresponds to set `A_46 = {6, 8, 21, 22, 36}`
- Variable `x_47` corresponds to set `A_47 = {3, 5, 16, 27, 34}`
- Variable `x_48` corresponds to set `A_48 = {3, 10, 12, 16, 26}`
- Variable `x_49` corresponds to set `A_49 = {6, 10, 20, 31, 37}`
- Variable `x_50` corresponds to set `A_50 = {10, 12, 20, 26, 40}`
- Variable `x_51` corresponds to set `A_51 = {1, 4, 17, 31, 34}`
- Variable `x_52` corresponds to set `A_52 = {11, 17, 24, 36, 38}`
- Variable `x_53` corresponds to set `A_53 = {4, 8, 19, 24, 35}`
- Variable `x_54` corresponds to set `A_54 = {15, 16, 21, 35, 39}`
- Variable `x_55` corresponds to set `A_55 = {8, 17, 23, 25, 34}`
- Variable `x_56` corresponds to set `A_56 = {3, 12, 14, 20, 21}`
- Variable `x_57` corresponds to set `A_57 = {10, 11, 28, 30, 39}`
- Variable `x_58` corresponds to set `A_58 = {3, 10, 12, 18, 26}`
- Variable `x_59` corresponds to set `A_59 = {12, 18, 23, 32, 38}`
- Variable `x_60` corresponds to set `A_60 = {11, 15, 17, 21, 32}`
- Variable `x_61` corresponds to set `A_61 = {4, 6, 28, 31, 37}`
- Variable `x_62` corresponds to set `A_62 = {14, 26, 29, 33, 40}`
- Variable `x_63` corresponds to set `A_63 = {1, 4, 10, 17, 23}`
- Variable `x_64` corresponds to set `A_64 = {19, 20, 23, 27, 33}`
- Variable `x_65` corresponds to set `A_65 = {3, 11, 12, 19, 22}`
- Variable `x_66` corresponds to set `A_66 = {5, 12, 18, 22, 35}`
- Variable `x_67` corresponds to set `A_67 = {7, 10, 28, 30, 36}`
- Variable `x_68` corresponds to set `A_68 = {11, 15, 21, 23, 37}`
- Variable `x_69` corresponds to set `A_69 = {15, 18, 35, 39, 40}`
- Variable `x_70` corresponds to set `A_70 = {11, 19, 22, 32, 36}`
- Variable `x_71` corresponds to set `A_71 = {1, 2, 17, 19, 27}`
- Variable `x_72` corresponds to set `A_72 = {13, 22, 27, 31, 39}`
- Variable `x_73` corresponds to set `A_73 = {5, 6, 16, 36, 37}`
- Variable `x_74` corresponds to set `A_74 = {16, 27, 34, 36, 38}`
- Variable `x_75` corresponds to set `A_75 = {5, 12, 15, 19, 26}`
- Variable `x_76` corresponds to set `A_76 = {3, 10, 21, 22, 40}`
- Variable `x_77` corresponds to set `A_77 = {2, 19, 24, 28, 32}`
- Variable `x_78` corresponds to set `A_78 = {6, 17, 32, 34, 39}`
- Variable `x_79` corresponds to set `A_79 = {4, 19, 20, 29, 39}`
- Variable `x_80` corresponds to set `A_80 = {3, 13, 22, 31, 37}`
- Variable `x_81` corresponds to set `A_81 = {15, 22, 25, 35, 40}`
- Variable `x_82` corresponds to set `A_82 = {9, 15, 16, 21, 40}`
- Variable `x_83` corresponds to set `A_83 = {13, 19, 20, 33, 39}`
- Variable `x_84` corresponds to set `A_84 = {7, 14, 23, 24, 35}`
- Variable `x_85` corresponds to set `A_85 = {10, 14, 18, 35, 37}`
- Variable `x_86` corresponds to set `A_86 = {4, 19, 27, 28, 30}`
- Variable `x_87` corresponds to set `A_87 = {14, 17, 18, 22, 24}`
- Variable `x_88` corresponds to set `A_88 = {16, 23, 37, 38, 40}`
- Variable `x_89` corresponds to set `A_89 = {9, 16, 17, 29, 39}`
- Variable `x_90` corresponds to set `A_90 = {8, 14, 23, 34, 38}`
- Variable `x_91` corresponds to set `A_91 = {7, 18, 30, 31, 32}`
- Variable `x_92` corresponds to set `A_92 = {5, 8, 9, 14, 40}`
- Variable `x_93` corresponds to set `A_93 = {1, 3, 15, 23, 26}`
- Variable `x_94` corresponds to set `A_94 = {3, 6, 31, 32, 37}`
- Variable `x_95` corresponds to set `A_95 = {2, 7, 14, 26, 38}`
- Variable `x_96` corresponds to set `A_96 = {7, 13, 14, 28, 30}`
- Variable `x_97` corresponds to set `A_97 = {1, 5, 14, 15, 18}`
- Variable `x_98` corresponds to set `A_98 = {1, 4, 16, 17, 40}`
- Variable `x_99` corresponds to set `A_99 = {11, 16, 20, 21, 32}`
- Variable `x_100` corresponds to set `A_100 = {3, 12, 19, 26, 40}`

## Exact constraints

- Constraint `1`: x_3 + x_5 + x_15 + x_22 + x_24 + x_32 + x_40 + x_51 + x_63 + x_71 + x_93 + x_97 + x_98 <= 1
- Constraint `2`: x_11 + x_17 + x_29 + x_31 + x_33 + x_34 + x_71 + x_77 + x_95 <= 1
- Constraint `3`: x_34 + x_47 + x_48 + x_56 + x_58 + x_65 + x_76 + x_80 + x_93 + x_94 + x_100 <= 1
- Constraint `4`: x_2 + x_13 + x_14 + x_16 + x_27 + x_31 + x_35 + x_43 + x_44 + x_51 + x_53 + x_61 + x_63 + x_79 + x_86 + x_98 <= 1
- Constraint `5`: x_11 + x_14 + x_25 + x_26 + x_30 + x_47 + x_66 + x_73 + x_75 + x_92 + x_97 <= 1
- Constraint `6`: x_2 + x_10 + x_18 + x_27 + x_28 + x_42 + x_43 + x_46 + x_49 + x_61 + x_73 + x_78 + x_94 <= 1
- Constraint `7`: x_5 + x_16 + x_25 + x_67 + x_84 + x_91 + x_95 + x_96 <= 1
- Constraint `8`: x_15 + x_22 + x_23 + x_25 + x_27 + x_28 + x_32 + x_38 + x_46 + x_53 + x_55 + x_90 + x_92 <= 1
- Constraint `9`: x_1 + x_11 + x_34 + x_42 + x_82 + x_89 + x_92 <= 1
- Constraint `10`: x_23 + x_25 + x_26 + x_31 + x_37 + x_41 + x_48 + x_49 + x_50 + x_57 + x_58 + x_63 + x_67 + x_76 + x_85 <= 1
- Constraint `11`: x_3 + x_19 + x_30 + x_38 + x_40 + x_52 + x_57 + x_60 + x_65 + x_68 + x_70 + x_99 <= 1
- Constraint `12`: x_20 + x_28 + x_31 + x_41 + x_48 + x_50 + x_56 + x_58 + x_59 + x_65 + x_66 + x_75 + x_100 <= 1
- Constraint `13`: x_1 + x_3 + x_5 + x_15 + x_34 + x_39 + x_45 + x_72 + x_80 + x_83 + x_96 <= 1
- Constraint `14`: x_7 + x_16 + x_19 + x_56 + x_62 + x_84 + x_85 + x_87 + x_90 + x_92 + x_95 + x_96 + x_97 <= 1
- Constraint `15`: x_6 + x_9 + x_13 + x_21 + x_54 + x_60 + x_68 + x_69 + x_75 + x_81 + x_82 + x_93 + x_97 <= 1
- Constraint `16`: x_6 + x_10 + x_47 + x_48 + x_54 + x_73 + x_74 + x_82 + x_88 + x_89 + x_98 + x_99 <= 1
- Constraint `17`: x_13 + x_20 + x_21 + x_23 + x_38 + x_51 + x_52 + x_55 + x_60 + x_63 + x_71 + x_78 + x_87 + x_89 + x_98 <= 1
- Constraint `18`: x_1 + x_4 + x_8 + x_9 + x_21 + x_24 + x_36 + x_40 + x_58 + x_59 + x_66 + x_69 + x_85 + x_87 + x_91 + x_97 <= 1
- Constraint `19`: x_1 + x_6 + x_11 + x_21 + x_36 + x_41 + x_53 + x_64 + x_65 + x_70 + x_71 + x_75 + x_77 + x_79 + x_83 + x_86 + x_100 <= 1
- Constraint `20`: x_5 + x_12 + x_21 + x_26 + x_27 + x_28 + x_29 + x_49 + x_50 + x_56 + x_64 + x_79 + x_83 + x_99 <= 1
- Constraint `21`: x_12 + x_16 + x_26 + x_45 + x_46 + x_54 + x_56 + x_60 + x_68 + x_76 + x_82 + x_99 <= 1
- Constraint `22`: x_24 + x_45 + x_46 + x_65 + x_66 + x_70 + x_72 + x_76 + x_80 + x_81 + x_87 <= 1
- Constraint `23`: x_7 + x_17 + x_18 + x_44 + x_55 + x_59 + x_63 + x_64 + x_68 + x_84 + x_88 + x_90 + x_93 <= 1
- Constraint `24`: x_6 + x_12 + x_17 + x_32 + x_52 + x_53 + x_77 + x_84 + x_87 <= 1
- Constraint `25`: x_2 + x_4 + x_13 + x_22 + x_25 + x_32 + x_33 + x_37 + x_55 + x_81 <= 1
- Constraint `26`: x_4 + x_5 + x_20 + x_35 + x_36 + x_48 + x_50 + x_58 + x_62 + x_75 + x_93 + x_95 + x_100 <= 1
- Constraint `27`: x_3 + x_10 + x_13 + x_15 + x_17 + x_22 + x_24 + x_26 + x_29 + x_30 + x_47 + x_64 + x_71 + x_72 + x_74 + x_86 <= 1
- Constraint `28`: x_2 + x_6 + x_8 + x_9 + x_17 + x_18 + x_29 + x_31 + x_37 + x_41 + x_44 + x_57 + x_61 + x_67 + x_77 + x_86 + x_96 <= 1
- Constraint `29`: x_1 + x_12 + x_20 + x_62 + x_79 + x_89 <= 1
- Constraint `30`: x_8 + x_30 + x_34 + x_57 + x_67 + x_86 + x_91 + x_96 <= 1
- Constraint `31`: x_7 + x_14 + x_49 + x_51 + x_61 + x_72 + x_80 + x_91 + x_94 <= 1
- Constraint `32`: x_4 + x_19 + x_28 + x_38 + x_40 + x_42 + x_59 + x_60 + x_70 + x_77 + x_78 + x_91 + x_94 + x_99 <= 1
- Constraint `33`: x_3 + x_8 + x_14 + x_30 + x_32 + x_39 + x_42 + x_62 + x_64 + x_83 <= 1
- Constraint `34`: x_8 + x_10 + x_12 + x_29 + x_40 + x_45 + x_47 + x_51 + x_55 + x_74 + x_78 + x_90 <= 1
- Constraint `35`: x_2 + x_11 + x_15 + x_24 + x_33 + x_37 + x_38 + x_44 + x_53 + x_54 + x_66 + x_69 + x_81 + x_84 + x_85 <= 1
- Constraint `36`: x_7 + x_9 + x_19 + x_22 + x_33 + x_39 + x_42 + x_43 + x_46 + x_52 + x_67 + x_70 + x_73 + x_74 <= 1
- Constraint `37`: x_18 + x_19 + x_35 + x_36 + x_37 + x_45 + x_49 + x_61 + x_68 + x_73 + x_80 + x_85 + x_88 + x_94 <= 1
- Constraint `38`: x_7 + x_9 + x_20 + x_23 + x_39 + x_41 + x_43 + x_52 + x_59 + x_74 + x_88 + x_90 + x_95 <= 1
- Constraint `39`: x_10 + x_14 + x_33 + x_35 + x_43 + x_44 + x_54 + x_57 + x_69 + x_72 + x_78 + x_79 + x_83 + x_89 <= 1
- Constraint `40`: x_4 + x_16 + x_18 + x_23 + x_27 + x_35 + x_36 + x_39 + x_50 + x_62 + x_69 + x_76 + x_81 + x_82 + x_88 + x_92 + x_98 + x_100 <= 1
