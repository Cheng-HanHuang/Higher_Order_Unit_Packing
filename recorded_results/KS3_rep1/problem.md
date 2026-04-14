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
- `density`: `0.7`

## Weights

w_1=1.2782366, w_2=1.8307418, w_3=1.3659101, w_4=1.529402, w_5=0.73550163, w_6=0.72473421, w_7=1.1271795, w_8=1.3899615, w_9=1.8947863, w_10=1.1893976, w_11=1.4093105, w_12=1.1698438, w_13=1.4673194, w_14=0.80080366, w_15=1.3818272, w_16=0.57014292, w_17=1.6150569, w_18=0.73944933, w_19=1.978699, w_20=1.7967062, w_21=0.99551638, w_22=1.8331076, w_23=0.63738446, w_24=1.1776921, w_25=0.94117905, w_26=1.1938913, w_27=1.8981128, w_28=1.601832, w_29=1.4052702, w_30=1.2491389, w_31=1.597705, w_32=1.4904964, w_33=1.8403618, w_34=1.049213, w_35=1.3983333, w_36=1.8437154, w_37=1.0143881, w_38=1.3668172, w_39=0.78037449, w_40=0.91890885, w_41=0.76806425, w_42=1.332075, w_43=0.84461312, w_44=1.1858234, w_45=0.88096307, w_46=0.64715753, w_47=0.96645865, w_48=1.1499493, w_49=1.2618547, w_50=1.4217002, w_51=0.57655409, w_52=1.7754124, w_53=1.7228422, w_54=0.50832727, w_55=1.4723639, w_56=1.1652826, w_57=1.3534716, w_58=1.7409391, w_59=1.2078877, w_60=1.2307271, w_61=1.8146256, w_62=0.93862641, w_63=1.2568752, w_64=1.6968535, w_65=0.76454489, w_66=1.6269821, w_67=1.863264, w_68=1.2087407, w_69=0.65549873, w_70=0.63557421, w_71=1.6827495, w_72=0.96203085, w_73=1.0475129, w_74=1.7627632, w_75=0.99432579, w_76=1.8454226, w_77=0.62761153, w_78=0.59896644, w_79=1.5952137, w_80=1.5728237, w_81=1.8866769, w_82=1.1519115, w_83=0.58037577, w_84=0.81383037, w_85=0.91604727, w_86=1.0713433, w_87=1.9448318, w_88=0.70211574, w_89=1.4032434, w_90=1.776983, w_91=1.6092772, w_92=1.6800414, w_93=1.0469555, w_94=1.7400446, w_95=0.87298821, w_96=1.8030583, w_97=1.9274332, w_98=1.2374083, w_99=1.6376713, w_100=0.54813915

## Candidate sets (variables)

- Variable `x_1` corresponds to set `A_1 = {21, 23, 26, 29, 35}`
- Variable `x_2` corresponds to set `A_2 = {2, 4, 26, 29, 40}`
- Variable `x_3` corresponds to set `A_3 = {12, 14, 16, 19, 39}`
- Variable `x_4` corresponds to set `A_4 = {8, 10, 13, 14, 32}`
- Variable `x_5` corresponds to set `A_5 = {3, 15, 17, 35, 37}`
- Variable `x_6` corresponds to set `A_6 = {8, 12, 16, 22, 30}`
- Variable `x_7` corresponds to set `A_7 = {11, 18, 31, 35, 38}`
- Variable `x_8` corresponds to set `A_8 = {25, 29, 36, 37, 39}`
- Variable `x_9` corresponds to set `A_9 = {15, 21, 22, 27, 39}`
- Variable `x_10` corresponds to set `A_10 = {5, 7, 27, 28, 34}`
- Variable `x_11` corresponds to set `A_11 = {4, 11, 17, 21, 34}`
- Variable `x_12` corresponds to set `A_12 = {1, 20, 32, 37, 38}`
- Variable `x_13` corresponds to set `A_13 = {4, 9, 15, 33, 35}`
- Variable `x_14` corresponds to set `A_14 = {8, 27, 30, 33, 40}`
- Variable `x_15` corresponds to set `A_15 = {8, 26, 27, 30, 38}`
- Variable `x_16` corresponds to set `A_16 = {8, 13, 14, 16, 33}`
- Variable `x_17` corresponds to set `A_17 = {1, 11, 21, 23, 24}`
- Variable `x_18` corresponds to set `A_18 = {19, 29, 33, 36, 37}`
- Variable `x_19` corresponds to set `A_19 = {3, 4, 13, 26, 28}`
- Variable `x_20` corresponds to set `A_20 = {3, 8, 21, 25, 35}`
- Variable `x_21` corresponds to set `A_21 = {6, 18, 25, 26, 30}`
- Variable `x_22` corresponds to set `A_22 = {3, 20, 28, 34, 39}`
- Variable `x_23` corresponds to set `A_23 = {4, 14, 17, 20, 39}`
- Variable `x_24` corresponds to set `A_24 = {6, 10, 14, 22, 34}`
- Variable `x_25` corresponds to set `A_25 = {2, 9, 16, 28, 37}`
- Variable `x_26` corresponds to set `A_26 = {2, 11, 17, 24, 36}`
- Variable `x_27` corresponds to set `A_27 = {14, 18, 21, 24, 28}`
- Variable `x_28` corresponds to set `A_28 = {16, 18, 25, 31, 34}`
- Variable `x_29` corresponds to set `A_29 = {5, 7, 8, 13, 24}`
- Variable `x_30` corresponds to set `A_30 = {5, 7, 8, 15, 39}`
- Variable `x_31` corresponds to set `A_31 = {2, 15, 35, 36, 39}`
- Variable `x_32` corresponds to set `A_32 = {15, 17, 29, 33, 37}`
- Variable `x_33` corresponds to set `A_33 = {1, 30, 32, 35, 36}`
- Variable `x_34` corresponds to set `A_34 = {3, 19, 24, 30, 31}`
- Variable `x_35` corresponds to set `A_35 = {11, 12, 15, 16, 40}`
- Variable `x_36` corresponds to set `A_36 = {3, 11, 20, 27, 38}`
- Variable `x_37` corresponds to set `A_37 = {6, 9, 21, 37, 40}`
- Variable `x_38` corresponds to set `A_38 = {6, 7, 11, 12, 39}`
- Variable `x_39` corresponds to set `A_39 = {5, 8, 22, 23, 25}`
- Variable `x_40` corresponds to set `A_40 = {6, 10, 20, 21, 40}`
- Variable `x_41` corresponds to set `A_41 = {5, 16, 22, 37, 38}`
- Variable `x_42` corresponds to set `A_42 = {12, 14, 16, 23, 26}`
- Variable `x_43` corresponds to set `A_43 = {2, 8, 10, 13, 19}`
- Variable `x_44` corresponds to set `A_44 = {3, 5, 7, 16, 18}`
- Variable `x_45` corresponds to set `A_45 = {1, 4, 5, 7, 9}`
- Variable `x_46` corresponds to set `A_46 = {10, 11, 17, 20, 37}`
- Variable `x_47` corresponds to set `A_47 = {1, 10, 20, 23, 26}`
- Variable `x_48` corresponds to set `A_48 = {7, 8, 19, 21, 26}`
- Variable `x_49` corresponds to set `A_49 = {19, 22, 28, 35, 37}`
- Variable `x_50` corresponds to set `A_50 = {4, 6, 8, 14, 38}`
- Variable `x_51` corresponds to set `A_51 = {15, 20, 21, 36, 40}`
- Variable `x_52` corresponds to set `A_52 = {11, 14, 22, 31, 32}`
- Variable `x_53` corresponds to set `A_53 = {3, 15, 26, 30, 31}`
- Variable `x_54` corresponds to set `A_54 = {11, 19, 22, 31, 32}`
- Variable `x_55` corresponds to set `A_55 = {6, 13, 22, 30, 40}`
- Variable `x_56` corresponds to set `A_56 = {1, 8, 9, 11, 27}`
- Variable `x_57` corresponds to set `A_57 = {15, 20, 21, 30, 33}`
- Variable `x_58` corresponds to set `A_58 = {3, 10, 26, 30, 34}`
- Variable `x_59` corresponds to set `A_59 = {4, 13, 15, 17, 23}`
- Variable `x_60` corresponds to set `A_60 = {14, 17, 24, 27, 31}`
- Variable `x_61` corresponds to set `A_61 = {16, 22, 23, 25, 34}`
- Variable `x_62` corresponds to set `A_62 = {1, 3, 8, 13, 18}`
- Variable `x_63` corresponds to set `A_63 = {11, 17, 26, 31, 36}`
- Variable `x_64` corresponds to set `A_64 = {12, 20, 27, 32, 36}`
- Variable `x_65` corresponds to set `A_65 = {1, 4, 19, 30, 37}`
- Variable `x_66` corresponds to set `A_66 = {6, 24, 26, 36, 38}`
- Variable `x_67` corresponds to set `A_67 = {8, 11, 14, 16, 21}`
- Variable `x_68` corresponds to set `A_68 = {13, 20, 28, 38, 40}`
- Variable `x_69` corresponds to set `A_69 = {1, 11, 15, 32, 33}`
- Variable `x_70` corresponds to set `A_70 = {2, 6, 17, 25, 35}`
- Variable `x_71` corresponds to set `A_71 = {5, 23, 27, 33, 38}`
- Variable `x_72` corresponds to set `A_72 = {5, 11, 17, 28, 40}`
- Variable `x_73` corresponds to set `A_73 = {4, 7, 24, 34, 40}`
- Variable `x_74` corresponds to set `A_74 = {1, 6, 20, 38, 39}`
- Variable `x_75` corresponds to set `A_75 = {24, 25, 26, 29, 35}`
- Variable `x_76` corresponds to set `A_76 = {1, 12, 25, 31, 35}`
- Variable `x_77` corresponds to set `A_77 = {23, 25, 27, 30, 36}`
- Variable `x_78` corresponds to set `A_78 = {7, 10, 15, 24, 27}`
- Variable `x_79` corresponds to set `A_79 = {6, 8, 10, 12, 24}`
- Variable `x_80` corresponds to set `A_80 = {3, 8, 23, 24, 37}`
- Variable `x_81` corresponds to set `A_81 = {5, 27, 33, 36, 37}`
- Variable `x_82` corresponds to set `A_82 = {13, 21, 30, 33, 40}`
- Variable `x_83` corresponds to set `A_83 = {16, 19, 26, 28, 35}`
- Variable `x_84` corresponds to set `A_84 = {9, 17, 18, 28, 36}`
- Variable `x_85` corresponds to set `A_85 = {2, 12, 19, 33, 34}`
- Variable `x_86` corresponds to set `A_86 = {21, 22, 35, 37, 38}`
- Variable `x_87` corresponds to set `A_87 = {14, 21, 22, 24, 37}`
- Variable `x_88` corresponds to set `A_88 = {11, 25, 28, 29, 32}`
- Variable `x_89` corresponds to set `A_89 = {3, 7, 15, 31, 32}`
- Variable `x_90` corresponds to set `A_90 = {17, 24, 25, 34, 40}`
- Variable `x_91` corresponds to set `A_91 = {18, 23, 24, 29, 39}`
- Variable `x_92` corresponds to set `A_92 = {3, 18, 23, 33, 38}`
- Variable `x_93` corresponds to set `A_93 = {8, 9, 16, 27, 40}`
- Variable `x_94` corresponds to set `A_94 = {1, 16, 34, 35, 40}`
- Variable `x_95` corresponds to set `A_95 = {1, 4, 6, 11, 27}`
- Variable `x_96` corresponds to set `A_96 = {6, 9, 27, 33, 34}`
- Variable `x_97` corresponds to set `A_97 = {3, 9, 26, 30, 34}`
- Variable `x_98` corresponds to set `A_98 = {13, 18, 31, 34, 36}`
- Variable `x_99` corresponds to set `A_99 = {9, 20, 31, 33, 39}`
- Variable `x_100` corresponds to set `A_100 = {9, 19, 26, 28, 32}`

## Exact constraints

- Constraint `1`: x_12 + x_17 + x_33 + x_45 + x_47 + x_56 + x_62 + x_65 + x_69 + x_74 + x_76 + x_94 + x_95 <= 1
- Constraint `2`: x_2 + x_25 + x_26 + x_31 + x_43 + x_70 + x_85 <= 1
- Constraint `3`: x_5 + x_19 + x_20 + x_22 + x_34 + x_36 + x_44 + x_53 + x_58 + x_62 + x_80 + x_89 + x_92 + x_97 <= 1
- Constraint `4`: x_2 + x_11 + x_13 + x_19 + x_23 + x_45 + x_50 + x_59 + x_65 + x_73 + x_95 <= 1
- Constraint `5`: x_10 + x_29 + x_30 + x_39 + x_41 + x_44 + x_45 + x_71 + x_72 + x_81 <= 1
- Constraint `6`: x_21 + x_24 + x_37 + x_38 + x_40 + x_50 + x_55 + x_66 + x_70 + x_74 + x_79 + x_95 + x_96 <= 1
- Constraint `7`: x_10 + x_29 + x_30 + x_38 + x_44 + x_45 + x_48 + x_73 + x_78 + x_89 <= 1
- Constraint `8`: x_4 + x_6 + x_14 + x_15 + x_16 + x_20 + x_29 + x_30 + x_39 + x_43 + x_48 + x_50 + x_56 + x_62 + x_67 + x_79 + x_80 + x_93 <= 1
- Constraint `9`: x_13 + x_25 + x_37 + x_45 + x_56 + x_84 + x_93 + x_96 + x_97 + x_99 + x_100 <= 1
- Constraint `10`: x_4 + x_24 + x_40 + x_43 + x_46 + x_47 + x_58 + x_78 + x_79 <= 1
- Constraint `11`: x_7 + x_11 + x_17 + x_26 + x_35 + x_36 + x_38 + x_46 + x_52 + x_54 + x_56 + x_63 + x_67 + x_69 + x_72 + x_88 + x_95 <= 1
- Constraint `12`: x_3 + x_6 + x_35 + x_38 + x_42 + x_64 + x_76 + x_79 + x_85 <= 1
- Constraint `13`: x_4 + x_16 + x_19 + x_29 + x_43 + x_55 + x_59 + x_62 + x_68 + x_82 + x_98 <= 1
- Constraint `14`: x_3 + x_4 + x_16 + x_23 + x_24 + x_27 + x_42 + x_50 + x_52 + x_60 + x_67 + x_87 <= 1
- Constraint `15`: x_5 + x_9 + x_13 + x_30 + x_31 + x_32 + x_35 + x_51 + x_53 + x_57 + x_59 + x_69 + x_78 + x_89 <= 1
- Constraint `16`: x_3 + x_6 + x_16 + x_25 + x_28 + x_35 + x_41 + x_42 + x_44 + x_61 + x_67 + x_83 + x_93 + x_94 <= 1
- Constraint `17`: x_5 + x_11 + x_23 + x_26 + x_32 + x_46 + x_59 + x_60 + x_63 + x_70 + x_72 + x_84 + x_90 <= 1
- Constraint `18`: x_7 + x_21 + x_27 + x_28 + x_44 + x_62 + x_84 + x_91 + x_92 + x_98 <= 1
- Constraint `19`: x_3 + x_18 + x_34 + x_43 + x_48 + x_49 + x_54 + x_65 + x_83 + x_85 + x_100 <= 1
- Constraint `20`: x_12 + x_22 + x_23 + x_36 + x_40 + x_46 + x_47 + x_51 + x_57 + x_64 + x_68 + x_74 + x_99 <= 1
- Constraint `21`: x_1 + x_9 + x_11 + x_17 + x_20 + x_27 + x_37 + x_40 + x_48 + x_51 + x_57 + x_67 + x_82 + x_86 + x_87 <= 1
- Constraint `22`: x_6 + x_9 + x_24 + x_39 + x_41 + x_49 + x_52 + x_54 + x_55 + x_61 + x_86 + x_87 <= 1
- Constraint `23`: x_1 + x_17 + x_39 + x_42 + x_47 + x_59 + x_61 + x_71 + x_77 + x_80 + x_91 + x_92 <= 1
- Constraint `24`: x_17 + x_26 + x_27 + x_29 + x_34 + x_60 + x_66 + x_73 + x_75 + x_78 + x_79 + x_80 + x_87 + x_90 + x_91 <= 1
- Constraint `25`: x_8 + x_20 + x_21 + x_28 + x_39 + x_61 + x_70 + x_75 + x_76 + x_77 + x_88 + x_90 <= 1
- Constraint `26`: x_1 + x_2 + x_15 + x_19 + x_21 + x_42 + x_47 + x_48 + x_53 + x_58 + x_63 + x_66 + x_75 + x_83 + x_97 + x_100 <= 1
- Constraint `27`: x_9 + x_10 + x_14 + x_15 + x_36 + x_56 + x_60 + x_64 + x_71 + x_77 + x_78 + x_81 + x_93 + x_95 + x_96 <= 1
- Constraint `28`: x_10 + x_19 + x_22 + x_25 + x_27 + x_49 + x_68 + x_72 + x_83 + x_84 + x_88 + x_100 <= 1
- Constraint `29`: x_1 + x_2 + x_8 + x_18 + x_32 + x_75 + x_88 + x_91 <= 1
- Constraint `30`: x_6 + x_14 + x_15 + x_21 + x_33 + x_34 + x_53 + x_55 + x_57 + x_58 + x_65 + x_77 + x_82 + x_97 <= 1
- Constraint `31`: x_7 + x_28 + x_34 + x_52 + x_53 + x_54 + x_60 + x_63 + x_76 + x_89 + x_98 + x_99 <= 1
- Constraint `32`: x_4 + x_12 + x_33 + x_52 + x_54 + x_64 + x_69 + x_88 + x_89 + x_100 <= 1
- Constraint `33`: x_13 + x_14 + x_16 + x_18 + x_32 + x_57 + x_69 + x_71 + x_81 + x_82 + x_85 + x_92 + x_96 + x_99 <= 1
- Constraint `34`: x_10 + x_11 + x_22 + x_24 + x_28 + x_58 + x_61 + x_73 + x_85 + x_90 + x_94 + x_96 + x_97 + x_98 <= 1
- Constraint `35`: x_1 + x_5 + x_7 + x_13 + x_20 + x_31 + x_33 + x_49 + x_70 + x_75 + x_76 + x_83 + x_86 + x_94 <= 1
- Constraint `36`: x_8 + x_18 + x_26 + x_31 + x_33 + x_51 + x_63 + x_64 + x_66 + x_77 + x_81 + x_84 + x_98 <= 1
- Constraint `37`: x_5 + x_8 + x_12 + x_18 + x_25 + x_32 + x_37 + x_41 + x_46 + x_49 + x_65 + x_80 + x_81 + x_86 + x_87 <= 1
- Constraint `38`: x_7 + x_12 + x_15 + x_36 + x_41 + x_50 + x_66 + x_68 + x_71 + x_74 + x_86 + x_92 <= 1
- Constraint `39`: x_3 + x_8 + x_9 + x_22 + x_23 + x_30 + x_31 + x_38 + x_74 + x_91 + x_99 <= 1
- Constraint `40`: x_2 + x_14 + x_35 + x_37 + x_40 + x_51 + x_55 + x_68 + x_72 + x_73 + x_82 + x_90 + x_93 + x_94 <= 1
