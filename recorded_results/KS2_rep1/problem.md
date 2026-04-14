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

w_1=0.70571869, w_2=1.8379764, w_3=0.82039278, w_4=0.85118296, w_5=1.4989083, w_6=0.87101261, w_7=1.7453413, w_8=1.8119799, w_9=1.7956471, w_10=1.4548465, w_11=1.0569613, w_12=1.9905737, w_13=0.8368494, w_14=0.80870155, w_15=1.5258184, w_16=1.9039423, w_17=0.51450473, w_18=1.3087067, w_19=1.9257294, w_20=1.7074115, w_21=0.54767885, w_22=1.6095745, w_23=1.9498425, w_24=1.5692243, w_25=1.3455715, w_26=1.9528459, w_27=0.58026754, w_28=1.2987706, w_29=1.8780094, w_30=0.59098742, w_31=0.61344715, w_32=1.3124506, w_33=1.5148677, w_34=0.97013705, w_35=1.4458402, w_36=1.8505268, w_37=0.7310224, w_38=0.53718413, w_39=1.9431125, w_40=1.825739, w_41=1.2814237, w_42=1.0650479, w_43=1.638882, w_44=1.3800844, w_45=1.4665594, w_46=1.934258, w_47=0.67039527, w_48=1.8401421, w_49=1.2856603, w_50=0.81679989, w_51=0.99185907, w_52=0.71947954, w_53=0.94758292, w_54=0.98114603, w_55=1.2727931, w_56=1.6796981, w_57=1.501545, w_58=1.1363887, w_59=1.4707323, w_60=1.8347233, w_61=1.1237127, w_62=0.94662141, w_63=1.1180353, w_64=1.892548, w_65=0.62503675, w_66=1.0879068, w_67=0.94034148, w_68=0.54241971, w_69=1.6984095, w_70=1.0856135, w_71=0.71424591, w_72=1.9691263, w_73=1.7907838, w_74=1.5287295, w_75=1.2326478, w_76=1.9282389, w_77=1.9927854, w_78=1.8977466, w_79=1.1208449, w_80=1.7327584, w_81=1.6084014, w_82=1.5866932, w_83=1.9074448, w_84=0.552971, w_85=1.1552011, w_86=0.93834644, w_87=0.9326326, w_88=1.9531727, w_89=1.5326473, w_90=1.3832871, w_91=1.3635151, w_92=1.8050798, w_93=1.466317, w_94=0.85741586, w_95=1.4391582, w_96=1.5605561, w_97=0.86298489, w_98=1.7984175, w_99=1.7123702, w_100=1.5553552

## Candidate sets (variables)

- Variable `x_1` corresponds to set `A_1 = {14, 26, 28, 29, 34}`
- Variable `x_2` corresponds to set `A_2 = {3, 9, 26, 29, 31}`
- Variable `x_3` corresponds to set `A_3 = {5, 27, 30, 31, 36}`
- Variable `x_4` corresponds to set `A_4 = {12, 14, 22, 30, 36}`
- Variable `x_5` corresponds to set `A_5 = {2, 6, 13, 29, 38}`
- Variable `x_6` corresponds to set `A_6 = {3, 15, 16, 18, 34}`
- Variable `x_7` corresponds to set `A_7 = {9, 15, 17, 23, 34}`
- Variable `x_8` corresponds to set `A_8 = {13, 24, 26, 30, 34}`
- Variable `x_9` corresponds to set `A_9 = {7, 14, 25, 37, 39}`
- Variable `x_10` corresponds to set `A_10 = {14, 15, 27, 33, 35}`
- Variable `x_11` corresponds to set `A_11 = {1, 7, 10, 21, 36}`
- Variable `x_12` corresponds to set `A_12 = {10, 18, 24, 25, 30}`
- Variable `x_13` corresponds to set `A_13 = {5, 25, 27, 36, 39}`
- Variable `x_14` corresponds to set `A_14 = {5, 11, 12, 22, 33}`
- Variable `x_15` corresponds to set `A_15 = {4, 11, 18, 27, 35}`
- Variable `x_16` corresponds to set `A_16 = {16, 17, 19, 25, 34}`
- Variable `x_17` corresponds to set `A_17 = {15, 17, 26, 31, 36}`
- Variable `x_18` corresponds to set `A_18 = {4, 10, 18, 23, 24}`
- Variable `x_19` corresponds to set `A_19 = {9, 18, 24, 26, 35}`
- Variable `x_20` corresponds to set `A_20 = {15, 18, 20, 25, 28}`
- Variable `x_21` corresponds to set `A_21 = {1, 17, 18, 31, 33}`
- Variable `x_22` corresponds to set `A_22 = {1, 8, 13, 23, 31}`
- Variable `x_23` corresponds to set `A_23 = {2, 25, 27, 30, 32}`
- Variable `x_24` corresponds to set `A_24 = {5, 7, 9, 10, 35}`
- Variable `x_25` corresponds to set `A_25 = {4, 6, 7, 14, 33}`
- Variable `x_26` corresponds to set `A_26 = {9, 13, 18, 23, 34}`
- Variable `x_27` corresponds to set `A_27 = {4, 9, 10, 16, 31}`
- Variable `x_28` corresponds to set `A_28 = {6, 12, 29, 33, 34}`
- Variable `x_29` corresponds to set `A_29 = {5, 10, 21, 28, 40}`
- Variable `x_30` corresponds to set `A_30 = {2, 12, 23, 25, 33}`
- Variable `x_31` corresponds to set `A_31 = {12, 13, 18, 29, 40}`
- Variable `x_32` corresponds to set `A_32 = {4, 14, 17, 28, 37}`
- Variable `x_33` corresponds to set `A_33 = {5, 17, 22, 24, 25}`
- Variable `x_34` corresponds to set `A_34 = {7, 16, 17, 29, 37}`
- Variable `x_35` corresponds to set `A_35 = {5, 19, 23, 28, 39}`
- Variable `x_36` corresponds to set `A_36 = {2, 4, 6, 28, 37}`
- Variable `x_37` corresponds to set `A_37 = {10, 16, 21, 24, 34}`
- Variable `x_38` corresponds to set `A_38 = {2, 15, 27, 29, 40}`
- Variable `x_39` corresponds to set `A_39 = {3, 12, 32, 37, 38}`
- Variable `x_40` corresponds to set `A_40 = {1, 8, 28, 31, 35}`
- Variable `x_41` corresponds to set `A_41 = {7, 11, 18, 34, 40}`
- Variable `x_42` corresponds to set `A_42 = {1, 7, 9, 11, 21}`
- Variable `x_43` corresponds to set `A_43 = {1, 3, 15, 18, 37}`
- Variable `x_44` corresponds to set `A_44 = {13, 14, 30, 33, 34}`
- Variable `x_45` corresponds to set `A_45 = {3, 4, 16, 32, 35}`
- Variable `x_46` corresponds to set `A_46 = {7, 16, 25, 28, 40}`
- Variable `x_47` corresponds to set `A_47 = {15, 21, 22, 25, 37}`
- Variable `x_48` corresponds to set `A_48 = {1, 7, 13, 25, 36}`
- Variable `x_49` corresponds to set `A_49 = {2, 4, 9, 25, 32}`
- Variable `x_50` corresponds to set `A_50 = {4, 24, 28, 29, 33}`
- Variable `x_51` corresponds to set `A_51 = {8, 16, 28, 31, 32}`
- Variable `x_52` corresponds to set `A_52 = {7, 18, 20, 24, 37}`
- Variable `x_53` corresponds to set `A_53 = {13, 14, 18, 22, 30}`
- Variable `x_54` corresponds to set `A_54 = {12, 20, 26, 37, 39}`
- Variable `x_55` corresponds to set `A_55 = {8, 20, 26, 27, 33}`
- Variable `x_56` corresponds to set `A_56 = {5, 20, 31, 38, 39}`
- Variable `x_57` corresponds to set `A_57 = {17, 21, 22, 28, 32}`
- Variable `x_58` corresponds to set `A_58 = {14, 17, 22, 23, 35}`
- Variable `x_59` corresponds to set `A_59 = {3, 15, 20, 37, 38}`
- Variable `x_60` corresponds to set `A_60 = {15, 20, 24, 27, 40}`
- Variable `x_61` corresponds to set `A_61 = {2, 8, 10, 19, 37}`
- Variable `x_62` corresponds to set `A_62 = {16, 25, 31, 32, 37}`
- Variable `x_63` corresponds to set `A_63 = {6, 9, 16, 24, 36}`
- Variable `x_64` corresponds to set `A_64 = {6, 10, 24, 26, 28}`
- Variable `x_65` corresponds to set `A_65 = {7, 9, 14, 29, 33}`
- Variable `x_66` corresponds to set `A_66 = {8, 17, 18, 29, 36}`
- Variable `x_67` corresponds to set `A_67 = {16, 21, 23, 36, 40}`
- Variable `x_68` corresponds to set `A_68 = {1, 4, 5, 22, 28}`
- Variable `x_69` corresponds to set `A_69 = {3, 16, 23, 25, 29}`
- Variable `x_70` corresponds to set `A_70 = {5, 24, 32, 33, 37}`
- Variable `x_71` corresponds to set `A_71 = {5, 7, 27, 30, 38}`
- Variable `x_72` corresponds to set `A_72 = {3, 7, 25, 30, 38}`
- Variable `x_73` corresponds to set `A_73 = {31, 32, 34, 39, 40}`
- Variable `x_74` corresponds to set `A_74 = {3, 21, 22, 28, 36}`
- Variable `x_75` corresponds to set `A_75 = {3, 7, 19, 22, 30}`
- Variable `x_76` corresponds to set `A_76 = {2, 13, 14, 17, 30}`
- Variable `x_77` corresponds to set `A_77 = {15, 21, 32, 33, 39}`
- Variable `x_78` corresponds to set `A_78 = {4, 9, 14, 17, 34}`
- Variable `x_79` corresponds to set `A_79 = {11, 20, 22, 23, 36}`
- Variable `x_80` corresponds to set `A_80 = {4, 6, 11, 21, 22}`
- Variable `x_81` corresponds to set `A_81 = {8, 29, 31, 35, 40}`
- Variable `x_82` corresponds to set `A_82 = {4, 14, 21, 27, 34}`
- Variable `x_83` corresponds to set `A_83 = {5, 9, 14, 17, 27}`
- Variable `x_84` corresponds to set `A_84 = {11, 12, 15, 21, 37}`
- Variable `x_85` corresponds to set `A_85 = {3, 4, 14, 15, 40}`
- Variable `x_86` corresponds to set `A_86 = {4, 7, 20, 31, 39}`
- Variable `x_87` corresponds to set `A_87 = {12, 18, 21, 23, 34}`
- Variable `x_88` corresponds to set `A_88 = {13, 24, 25, 26, 35}`
- Variable `x_89` corresponds to set `A_89 = {12, 13, 20, 21, 40}`
- Variable `x_90` corresponds to set `A_90 = {9, 21, 28, 29, 40}`
- Variable `x_91` corresponds to set `A_91 = {3, 6, 13, 36, 40}`
- Variable `x_92` corresponds to set `A_92 = {1, 26, 29, 31, 35}`
- Variable `x_93` corresponds to set `A_93 = {1, 10, 16, 32, 37}`
- Variable `x_94` corresponds to set `A_94 = {22, 26, 29, 31, 39}`
- Variable `x_95` corresponds to set `A_95 = {4, 6, 15, 18, 22}`
- Variable `x_96` corresponds to set `A_96 = {3, 7, 14, 21, 40}`
- Variable `x_97` corresponds to set `A_97 = {10, 21, 23, 27, 36}`
- Variable `x_98` corresponds to set `A_98 = {7, 9, 27, 29, 34}`
- Variable `x_99` corresponds to set `A_99 = {3, 12, 13, 16, 32}`
- Variable `x_100` corresponds to set `A_100 = {6, 21, 24, 26, 37}`

## Exact constraints

- Constraint `1`: x_11 + x_21 + x_22 + x_40 + x_42 + x_43 + x_48 + x_68 + x_92 + x_93 <= 1
- Constraint `2`: x_5 + x_23 + x_30 + x_36 + x_38 + x_49 + x_61 + x_76 <= 1
- Constraint `3`: x_2 + x_6 + x_39 + x_43 + x_45 + x_59 + x_69 + x_72 + x_74 + x_75 + x_85 + x_91 + x_96 + x_99 <= 1
- Constraint `4`: x_15 + x_18 + x_25 + x_27 + x_32 + x_36 + x_45 + x_49 + x_50 + x_68 + x_78 + x_80 + x_82 + x_85 + x_86 + x_95 <= 1
- Constraint `5`: x_3 + x_13 + x_14 + x_24 + x_29 + x_33 + x_35 + x_56 + x_68 + x_70 + x_71 + x_83 <= 1
- Constraint `6`: x_5 + x_25 + x_28 + x_36 + x_63 + x_64 + x_80 + x_91 + x_95 + x_100 <= 1
- Constraint `7`: x_9 + x_11 + x_24 + x_25 + x_34 + x_41 + x_42 + x_46 + x_48 + x_52 + x_65 + x_71 + x_72 + x_75 + x_86 + x_96 + x_98 <= 1
- Constraint `8`: x_22 + x_40 + x_51 + x_55 + x_61 + x_66 + x_81 <= 1
- Constraint `9`: x_2 + x_7 + x_19 + x_24 + x_26 + x_27 + x_42 + x_49 + x_63 + x_65 + x_78 + x_83 + x_90 + x_98 <= 1
- Constraint `10`: x_11 + x_12 + x_18 + x_24 + x_27 + x_29 + x_37 + x_61 + x_64 + x_93 + x_97 <= 1
- Constraint `11`: x_14 + x_15 + x_41 + x_42 + x_79 + x_80 + x_84 <= 1
- Constraint `12`: x_4 + x_14 + x_28 + x_30 + x_31 + x_39 + x_54 + x_84 + x_87 + x_89 + x_99 <= 1
- Constraint `13`: x_5 + x_8 + x_22 + x_26 + x_31 + x_44 + x_48 + x_53 + x_76 + x_88 + x_89 + x_91 + x_99 <= 1
- Constraint `14`: x_1 + x_4 + x_9 + x_10 + x_25 + x_32 + x_44 + x_53 + x_58 + x_65 + x_76 + x_78 + x_82 + x_83 + x_85 + x_96 <= 1
- Constraint `15`: x_6 + x_7 + x_10 + x_17 + x_20 + x_38 + x_43 + x_47 + x_59 + x_60 + x_77 + x_84 + x_85 + x_95 <= 1
- Constraint `16`: x_6 + x_16 + x_27 + x_34 + x_37 + x_45 + x_46 + x_51 + x_62 + x_63 + x_67 + x_69 + x_93 + x_99 <= 1
- Constraint `17`: x_7 + x_16 + x_17 + x_21 + x_32 + x_33 + x_34 + x_57 + x_58 + x_66 + x_76 + x_78 + x_83 <= 1
- Constraint `18`: x_6 + x_12 + x_15 + x_18 + x_19 + x_20 + x_21 + x_26 + x_31 + x_41 + x_43 + x_52 + x_53 + x_66 + x_87 + x_95 <= 1
- Constraint `19`: x_16 + x_35 + x_61 + x_75 <= 1
- Constraint `20`: x_20 + x_52 + x_54 + x_55 + x_56 + x_59 + x_60 + x_79 + x_86 + x_89 <= 1
- Constraint `21`: x_11 + x_29 + x_37 + x_42 + x_47 + x_57 + x_67 + x_74 + x_77 + x_80 + x_82 + x_84 + x_87 + x_89 + x_90 + x_96 + x_97 + x_100 <= 1
- Constraint `22`: x_4 + x_14 + x_33 + x_47 + x_53 + x_57 + x_58 + x_68 + x_74 + x_75 + x_79 + x_80 + x_94 + x_95 <= 1
- Constraint `23`: x_7 + x_18 + x_22 + x_26 + x_30 + x_35 + x_58 + x_67 + x_69 + x_79 + x_87 + x_97 <= 1
- Constraint `24`: x_8 + x_12 + x_18 + x_19 + x_33 + x_37 + x_50 + x_52 + x_60 + x_63 + x_64 + x_70 + x_88 + x_100 <= 1
- Constraint `25`: x_9 + x_12 + x_13 + x_16 + x_20 + x_23 + x_30 + x_33 + x_46 + x_47 + x_48 + x_49 + x_62 + x_69 + x_72 + x_88 <= 1
- Constraint `26`: x_1 + x_2 + x_8 + x_17 + x_19 + x_54 + x_55 + x_64 + x_88 + x_92 + x_94 + x_100 <= 1
- Constraint `27`: x_3 + x_10 + x_13 + x_15 + x_23 + x_38 + x_55 + x_60 + x_71 + x_82 + x_83 + x_97 + x_98 <= 1
- Constraint `28`: x_1 + x_20 + x_29 + x_32 + x_35 + x_36 + x_40 + x_46 + x_50 + x_51 + x_57 + x_64 + x_68 + x_74 + x_90 <= 1
- Constraint `29`: x_1 + x_2 + x_5 + x_28 + x_31 + x_34 + x_38 + x_50 + x_65 + x_66 + x_69 + x_81 + x_90 + x_92 + x_94 + x_98 <= 1
- Constraint `30`: x_3 + x_4 + x_8 + x_12 + x_23 + x_44 + x_53 + x_71 + x_72 + x_75 + x_76 <= 1
- Constraint `31`: x_2 + x_3 + x_17 + x_21 + x_22 + x_27 + x_40 + x_51 + x_56 + x_62 + x_73 + x_81 + x_86 + x_92 + x_94 <= 1
- Constraint `32`: x_23 + x_39 + x_45 + x_49 + x_51 + x_57 + x_62 + x_70 + x_73 + x_77 + x_93 + x_99 <= 1
- Constraint `33`: x_10 + x_14 + x_21 + x_25 + x_28 + x_30 + x_44 + x_50 + x_55 + x_65 + x_70 + x_77 <= 1
- Constraint `34`: x_1 + x_6 + x_7 + x_8 + x_16 + x_26 + x_28 + x_37 + x_41 + x_44 + x_73 + x_78 + x_82 + x_87 + x_98 <= 1
- Constraint `35`: x_10 + x_15 + x_19 + x_24 + x_40 + x_45 + x_58 + x_81 + x_88 + x_92 <= 1
- Constraint `36`: x_3 + x_4 + x_11 + x_13 + x_17 + x_48 + x_63 + x_66 + x_67 + x_74 + x_79 + x_91 + x_97 <= 1
- Constraint `37`: x_9 + x_32 + x_34 + x_36 + x_39 + x_43 + x_47 + x_52 + x_54 + x_59 + x_61 + x_62 + x_70 + x_84 + x_93 + x_100 <= 1
- Constraint `38`: x_5 + x_39 + x_56 + x_59 + x_71 + x_72 <= 1
- Constraint `39`: x_9 + x_13 + x_35 + x_54 + x_56 + x_73 + x_77 + x_86 + x_94 <= 1
- Constraint `40`: x_29 + x_31 + x_38 + x_41 + x_46 + x_60 + x_67 + x_73 + x_81 + x_85 + x_89 + x_90 + x_91 + x_96 <= 1
