# Original problem: kset_u50_n120_k5

This file records the exact original binary packing problem used for the matching run result.

## Optimization model

\[
\max_{x\in\{0,1\}^n}\ \sum_{i=1}^n w_i x_i
\qquad\text{s.t.}\qquad
\sum_{i\in S_k} x_i \le B_k,\quad k=1,\dots,m.
\]

- Number of variables: `120`
- Number of constraints: `50`
- Matching run-result file: `result.json`

## Metadata

- `generator`: `random_k_set_packing`
- `universe_size`: `50`
- `k`: `5`
- `density`: `1.0`

## Weights

w_1=0.78848227, w_2=0.82298727, w_3=1.0977953, w_4=0.99727745, w_5=1.9220009, w_6=1.8899021, w_7=1.7211666, w_8=1.09285, w_9=0.64820201, w_10=1.927805, w_11=0.65479156, w_12=1.5163674, w_13=1.1008351, w_14=1.1210164, w_15=1.2278176, w_16=1.1976119, w_17=0.85408499, w_18=0.50904631, w_19=1.5476966, w_20=1.8744736, w_21=1.6294818, w_22=0.79508742, w_23=1.6255082, w_24=0.90630326, w_25=1.2690699, w_26=1.2373147, w_27=1.5146515, w_28=1.3326858, w_29=0.60272989, w_30=0.79002377, w_31=1.1750547, w_32=1.540585, w_33=1.446583, w_34=1.5060802, w_35=1.4380802, w_36=1.9331288, w_37=0.66082194, w_38=1.1939686, w_39=1.4897241, w_40=1.4914712, w_41=1.2653421, w_42=1.5782272, w_43=1.3502541, w_44=1.6705645, w_45=0.52650325, w_46=0.99144911, w_47=0.85207048, w_48=0.82476142, w_49=0.74291087, w_50=1.6806262, w_51=1.2120873, w_52=1.4199848, w_53=1.1247008, w_54=1.5950344, w_55=1.2180766, w_56=1.4636163, w_57=1.3516501, w_58=1.512673, w_59=1.5471225, w_60=1.3625892, w_61=1.3260855, w_62=1.5185072, w_63=1.0165442, w_64=1.4142603, w_65=1.1971024, w_66=1.7659137, w_67=0.84910042, w_68=1.36295, w_69=1.4395393, w_70=0.86687659, w_71=1.1958348, w_72=1.6426807, w_73=0.88004285, w_74=1.8247772, w_75=0.61294254, w_76=0.89430592, w_77=1.5081744, w_78=1.0554484, w_79=0.56548943, w_80=1.0960946, w_81=1.7940462, w_82=0.78816097, w_83=1.0271433, w_84=0.6078311, w_85=1.4351728, w_86=0.85330041, w_87=1.0908373, w_88=1.5287127, w_89=0.78030888, w_90=1.4590373, w_91=0.98908452, w_92=0.78417539, w_93=1.6209542, w_94=1.4834957, w_95=0.70149437, w_96=0.91712141, w_97=0.95575283, w_98=1.4207275, w_99=0.99319922, w_100=0.97435948, w_101=1.6197107, w_102=1.8863732, w_103=1.9047894, w_104=1.5622098, w_105=0.83931556, w_106=0.76611557, w_107=1.266818, w_108=1.6805427, w_109=1.7829409, w_110=1.5299091, w_111=1.4773545, w_112=0.93730906, w_113=1.0770806, w_114=1.1899522, w_115=1.7767534, w_116=1.3198655, w_117=0.59189061, w_118=1.0509974, w_119=1.2460431, w_120=1.3293551

## Candidate sets (variables)

- Variable `x_1` corresponds to set `A_1 = {5, 7, 9, 15, 23}`
- Variable `x_2` corresponds to set `A_2 = {7, 15, 24, 31, 46}`
- Variable `x_3` corresponds to set `A_3 = {3, 17, 29, 41, 44}`
- Variable `x_4` corresponds to set `A_4 = {1, 10, 35, 40, 48}`
- Variable `x_5` corresponds to set `A_5 = {19, 28, 37, 38, 39}`
- Variable `x_6` corresponds to set `A_6 = {7, 8, 29, 40, 42}`
- Variable `x_7` corresponds to set `A_7 = {1, 11, 14, 27, 44}`
- Variable `x_8` corresponds to set `A_8 = {3, 6, 13, 31, 47}`
- Variable `x_9` corresponds to set `A_9 = {7, 12, 17, 36, 44}`
- Variable `x_10` corresponds to set `A_10 = {3, 5, 27, 28, 37}`
- Variable `x_11` corresponds to set `A_11 = {6, 13, 31, 33, 46}`
- Variable `x_12` corresponds to set `A_12 = {3, 22, 26, 45, 47}`
- Variable `x_13` corresponds to set `A_13 = {9, 21, 34, 44, 49}`
- Variable `x_14` corresponds to set `A_14 = {11, 28, 29, 34, 46}`
- Variable `x_15` corresponds to set `A_15 = {11, 19, 22, 34, 45}`
- Variable `x_16` corresponds to set `A_16 = {1, 25, 34, 38, 42}`
- Variable `x_17` corresponds to set `A_17 = {5, 14, 15, 23, 47}`
- Variable `x_18` corresponds to set `A_18 = {3, 35, 38, 41, 50}`
- Variable `x_19` corresponds to set `A_19 = {4, 20, 30, 32, 35}`
- Variable `x_20` corresponds to set `A_20 = {3, 24, 31, 32, 40}`
- Variable `x_21` corresponds to set `A_21 = {2, 12, 23, 38, 42}`
- Variable `x_22` corresponds to set `A_22 = {1, 3, 11, 15, 28}`
- Variable `x_23` corresponds to set `A_23 = {19, 25, 27, 30, 41}`
- Variable `x_24` corresponds to set `A_24 = {13, 31, 41, 48, 50}`
- Variable `x_25` corresponds to set `A_25 = {5, 9, 35, 39, 46}`
- Variable `x_26` corresponds to set `A_26 = {13, 27, 38, 45, 47}`
- Variable `x_27` corresponds to set `A_27 = {3, 19, 22, 27, 45}`
- Variable `x_28` corresponds to set `A_28 = {1, 33, 35, 44, 45}`
- Variable `x_29` corresponds to set `A_29 = {12, 29, 33, 34, 46}`
- Variable `x_30` corresponds to set `A_30 = {7, 19, 31, 47, 48}`
- Variable `x_31` corresponds to set `A_31 = {1, 24, 45, 46, 49}`
- Variable `x_32` corresponds to set `A_32 = {22, 25, 29, 36, 44}`
- Variable `x_33` corresponds to set `A_33 = {1, 10, 12, 15, 31}`
- Variable `x_34` corresponds to set `A_34 = {14, 18, 25, 44, 49}`
- Variable `x_35` corresponds to set `A_35 = {9, 12, 19, 20, 47}`
- Variable `x_36` corresponds to set `A_36 = {2, 14, 16, 31, 41}`
- Variable `x_37` corresponds to set `A_37 = {14, 15, 24, 39, 50}`
- Variable `x_38` corresponds to set `A_38 = {2, 34, 39, 48, 50}`
- Variable `x_39` corresponds to set `A_39 = {6, 12, 13, 38, 44}`
- Variable `x_40` corresponds to set `A_40 = {5, 8, 14, 25, 31}`
- Variable `x_41` corresponds to set `A_41 = {12, 22, 26, 32, 47}`
- Variable `x_42` corresponds to set `A_42 = {2, 4, 9, 36, 44}`
- Variable `x_43` corresponds to set `A_43 = {17, 36, 38, 40, 46}`
- Variable `x_44` corresponds to set `A_44 = {6, 9, 32, 36, 41}`
- Variable `x_45` corresponds to set `A_45 = {11, 19, 31, 44, 50}`
- Variable `x_46` corresponds to set `A_46 = {3, 22, 35, 48, 50}`
- Variable `x_47` corresponds to set `A_47 = {1, 12, 22, 27, 33}`
- Variable `x_48` corresponds to set `A_48 = {10, 16, 28, 41, 47}`
- Variable `x_49` corresponds to set `A_49 = {9, 15, 17, 25, 27}`
- Variable `x_50` corresponds to set `A_50 = {11, 13, 15, 32, 35}`
- Variable `x_51` corresponds to set `A_51 = {24, 32, 37, 40, 45}`
- Variable `x_52` corresponds to set `A_52 = {5, 13, 18, 20, 44}`
- Variable `x_53` corresponds to set `A_53 = {16, 23, 31, 39, 42}`
- Variable `x_54` corresponds to set `A_54 = {6, 15, 37, 41, 50}`
- Variable `x_55` corresponds to set `A_55 = {8, 11, 29, 36, 38}`
- Variable `x_56` corresponds to set `A_56 = {9, 10, 16, 18, 33}`
- Variable `x_57` corresponds to set `A_57 = {2, 25, 29, 43, 49}`
- Variable `x_58` corresponds to set `A_58 = {3, 11, 18, 21, 43}`
- Variable `x_59` corresponds to set `A_59 = {1, 12, 24, 31, 44}`
- Variable `x_60` corresponds to set `A_60 = {17, 34, 36, 44, 50}`
- Variable `x_61` corresponds to set `A_61 = {1, 5, 12, 16, 32}`
- Variable `x_62` corresponds to set `A_62 = {20, 38, 48, 49, 50}`
- Variable `x_63` corresponds to set `A_63 = {3, 4, 18, 23, 42}`
- Variable `x_64` corresponds to set `A_64 = {2, 3, 19, 36, 45}`
- Variable `x_65` corresponds to set `A_65 = {7, 20, 30, 32, 45}`
- Variable `x_66` corresponds to set `A_66 = {2, 8, 15, 17, 31}`
- Variable `x_67` corresponds to set `A_67 = {3, 9, 10, 30, 45}`
- Variable `x_68` corresponds to set `A_68 = {3, 5, 10, 37, 42}`
- Variable `x_69` corresponds to set `A_69 = {2, 15, 21, 42, 50}`
- Variable `x_70` corresponds to set `A_70 = {18, 21, 28, 29, 40}`
- Variable `x_71` corresponds to set `A_71 = {2, 13, 27, 35, 45}`
- Variable `x_72` corresponds to set `A_72 = {8, 23, 28, 32, 44}`
- Variable `x_73` corresponds to set `A_73 = {3, 11, 21, 35, 37}`
- Variable `x_74` corresponds to set `A_74 = {3, 8, 13, 31, 35}`
- Variable `x_75` corresponds to set `A_75 = {14, 22, 30, 38, 43}`
- Variable `x_76` corresponds to set `A_76 = {2, 3, 14, 27, 40}`
- Variable `x_77` corresponds to set `A_77 = {4, 7, 18, 27, 46}`
- Variable `x_78` corresponds to set `A_78 = {1, 10, 18, 30, 50}`
- Variable `x_79` corresponds to set `A_79 = {10, 32, 33, 34, 44}`
- Variable `x_80` corresponds to set `A_80 = {8, 12, 20, 28, 44}`
- Variable `x_81` corresponds to set `A_81 = {18, 20, 23, 47, 50}`
- Variable `x_82` corresponds to set `A_82 = {5, 13, 23, 29, 44}`
- Variable `x_83` corresponds to set `A_83 = {14, 34, 36, 47, 50}`
- Variable `x_84` corresponds to set `A_84 = {9, 23, 27, 30, 38}`
- Variable `x_85` corresponds to set `A_85 = {2, 9, 12, 35, 49}`
- Variable `x_86` corresponds to set `A_86 = {2, 21, 43, 44, 50}`
- Variable `x_87` corresponds to set `A_87 = {17, 37, 38, 39, 46}`
- Variable `x_88` corresponds to set `A_88 = {7, 27, 43, 46, 47}`
- Variable `x_89` corresponds to set `A_89 = {3, 6, 19, 38, 48}`
- Variable `x_90` corresponds to set `A_90 = {6, 9, 15, 18, 47}`
- Variable `x_91` corresponds to set `A_91 = {13, 24, 33, 37, 50}`
- Variable `x_92` corresponds to set `A_92 = {1, 13, 15, 18, 48}`
- Variable `x_93` corresponds to set `A_93 = {1, 6, 22, 37, 45}`
- Variable `x_94` corresponds to set `A_94 = {8, 9, 17, 18, 29}`
- Variable `x_95` corresponds to set `A_95 = {21, 30, 32, 41, 45}`
- Variable `x_96` corresponds to set `A_96 = {2, 17, 33, 34, 46}`
- Variable `x_97` corresponds to set `A_97 = {6, 13, 35, 38, 42}`
- Variable `x_98` corresponds to set `A_98 = {2, 10, 15, 18, 35}`
- Variable `x_99` corresponds to set `A_99 = {10, 11, 22, 24, 25}`
- Variable `x_100` corresponds to set `A_100 = {3, 7, 10, 29, 48}`
- Variable `x_101` corresponds to set `A_101 = {2, 21, 23, 33, 46}`
- Variable `x_102` corresponds to set `A_102 = {7, 19, 24, 37, 44}`
- Variable `x_103` corresponds to set `A_103 = {9, 11, 17, 28, 32}`
- Variable `x_104` corresponds to set `A_104 = {10, 12, 24, 39, 43}`
- Variable `x_105` corresponds to set `A_105 = {2, 37, 41, 46, 48}`
- Variable `x_106` corresponds to set `A_106 = {2, 15, 16, 43, 47}`
- Variable `x_107` corresponds to set `A_107 = {23, 25, 42, 47, 50}`
- Variable `x_108` corresponds to set `A_108 = {11, 15, 17, 19, 26}`
- Variable `x_109` corresponds to set `A_109 = {33, 34, 35, 48, 49}`
- Variable `x_110` corresponds to set `A_110 = {5, 6, 11, 45, 47}`
- Variable `x_111` corresponds to set `A_111 = {6, 11, 16, 22, 35}`
- Variable `x_112` corresponds to set `A_112 = {5, 6, 29, 34, 45}`
- Variable `x_113` corresponds to set `A_113 = {3, 5, 8, 11, 37}`
- Variable `x_114` corresponds to set `A_114 = {5, 7, 8, 13, 29}`
- Variable `x_115` corresponds to set `A_115 = {17, 33, 46, 47, 50}`
- Variable `x_116` corresponds to set `A_116 = {8, 18, 21, 25, 30}`
- Variable `x_117` corresponds to set `A_117 = {2, 6, 9, 45, 48}`
- Variable `x_118` corresponds to set `A_118 = {11, 14, 19, 27, 34}`
- Variable `x_119` corresponds to set `A_119 = {21, 22, 26, 39, 44}`
- Variable `x_120` corresponds to set `A_120 = {1, 15, 27, 37, 47}`

## Exact constraints

- Constraint `1`: x_4 + x_7 + x_16 + x_22 + x_28 + x_31 + x_33 + x_47 + x_59 + x_61 + x_78 + x_92 + x_93 + x_120 <= 1
- Constraint `2`: x_21 + x_36 + x_38 + x_42 + x_57 + x_64 + x_66 + x_69 + x_71 + x_76 + x_85 + x_86 + x_96 + x_98 + x_101 + x_105 + x_106 + x_117 <= 1
- Constraint `3`: x_3 + x_8 + x_10 + x_12 + x_18 + x_20 + x_22 + x_27 + x_46 + x_58 + x_63 + x_64 + x_67 + x_68 + x_73 + x_74 + x_76 + x_89 + x_100 + x_113 <= 1
- Constraint `4`: x_19 + x_42 + x_63 + x_77 <= 1
- Constraint `5`: x_1 + x_10 + x_17 + x_25 + x_40 + x_52 + x_61 + x_68 + x_82 + x_110 + x_112 + x_113 + x_114 <= 1
- Constraint `6`: x_8 + x_11 + x_39 + x_44 + x_54 + x_89 + x_90 + x_93 + x_97 + x_110 + x_111 + x_112 + x_117 <= 1
- Constraint `7`: x_1 + x_2 + x_6 + x_9 + x_30 + x_65 + x_77 + x_88 + x_100 + x_102 + x_114 <= 1
- Constraint `8`: x_6 + x_40 + x_55 + x_66 + x_72 + x_74 + x_80 + x_94 + x_113 + x_114 + x_116 <= 1
- Constraint `9`: x_1 + x_13 + x_25 + x_35 + x_42 + x_44 + x_49 + x_56 + x_67 + x_84 + x_85 + x_90 + x_94 + x_103 + x_117 <= 1
- Constraint `10`: x_4 + x_33 + x_48 + x_56 + x_67 + x_68 + x_78 + x_79 + x_98 + x_99 + x_100 + x_104 <= 1
- Constraint `11`: x_7 + x_14 + x_15 + x_22 + x_45 + x_50 + x_55 + x_58 + x_73 + x_99 + x_103 + x_108 + x_110 + x_111 + x_113 + x_118 <= 1
- Constraint `12`: x_9 + x_21 + x_29 + x_33 + x_35 + x_39 + x_41 + x_47 + x_59 + x_61 + x_80 + x_85 + x_104 <= 1
- Constraint `13`: x_8 + x_11 + x_24 + x_26 + x_39 + x_50 + x_52 + x_71 + x_74 + x_82 + x_91 + x_92 + x_97 + x_114 <= 1
- Constraint `14`: x_7 + x_17 + x_34 + x_36 + x_37 + x_40 + x_75 + x_76 + x_83 + x_118 <= 1
- Constraint `15`: x_1 + x_2 + x_17 + x_22 + x_33 + x_37 + x_49 + x_50 + x_54 + x_66 + x_69 + x_90 + x_92 + x_98 + x_106 + x_108 + x_120 <= 1
- Constraint `16`: x_36 + x_48 + x_53 + x_56 + x_61 + x_106 + x_111 <= 1
- Constraint `17`: x_3 + x_9 + x_43 + x_49 + x_60 + x_66 + x_87 + x_94 + x_96 + x_103 + x_108 + x_115 <= 1
- Constraint `18`: x_34 + x_52 + x_56 + x_58 + x_63 + x_70 + x_77 + x_78 + x_81 + x_90 + x_92 + x_94 + x_98 + x_116 <= 1
- Constraint `19`: x_5 + x_15 + x_23 + x_27 + x_30 + x_35 + x_45 + x_64 + x_89 + x_102 + x_108 + x_118 <= 1
- Constraint `20`: x_19 + x_35 + x_52 + x_62 + x_65 + x_80 + x_81 <= 1
- Constraint `21`: x_13 + x_58 + x_69 + x_70 + x_73 + x_86 + x_95 + x_101 + x_116 + x_119 <= 1
- Constraint `22`: x_12 + x_15 + x_27 + x_32 + x_41 + x_46 + x_47 + x_75 + x_93 + x_99 + x_111 + x_119 <= 1
- Constraint `23`: x_1 + x_17 + x_21 + x_53 + x_63 + x_72 + x_81 + x_82 + x_84 + x_101 + x_107 <= 1
- Constraint `24`: x_2 + x_20 + x_31 + x_37 + x_51 + x_59 + x_91 + x_99 + x_102 + x_104 <= 1
- Constraint `25`: x_16 + x_23 + x_32 + x_34 + x_40 + x_49 + x_57 + x_99 + x_107 + x_116 <= 1
- Constraint `26`: x_12 + x_41 + x_108 + x_119 <= 1
- Constraint `27`: x_7 + x_10 + x_23 + x_26 + x_27 + x_47 + x_49 + x_71 + x_76 + x_77 + x_84 + x_88 + x_118 + x_120 <= 1
- Constraint `28`: x_5 + x_10 + x_14 + x_22 + x_48 + x_70 + x_72 + x_80 + x_103 <= 1
- Constraint `29`: x_3 + x_6 + x_14 + x_29 + x_32 + x_55 + x_57 + x_70 + x_82 + x_94 + x_100 + x_112 + x_114 <= 1
- Constraint `30`: x_19 + x_23 + x_65 + x_67 + x_75 + x_78 + x_84 + x_95 + x_116 <= 1
- Constraint `31`: x_2 + x_8 + x_11 + x_20 + x_24 + x_30 + x_33 + x_36 + x_40 + x_45 + x_53 + x_59 + x_66 + x_74 <= 1
- Constraint `32`: x_19 + x_20 + x_41 + x_44 + x_50 + x_51 + x_61 + x_65 + x_72 + x_79 + x_95 + x_103 <= 1
- Constraint `33`: x_11 + x_28 + x_29 + x_47 + x_56 + x_79 + x_91 + x_96 + x_101 + x_109 + x_115 <= 1
- Constraint `34`: x_13 + x_14 + x_15 + x_16 + x_29 + x_38 + x_60 + x_79 + x_83 + x_96 + x_109 + x_112 + x_118 <= 1
- Constraint `35`: x_4 + x_18 + x_19 + x_25 + x_28 + x_46 + x_50 + x_71 + x_73 + x_74 + x_85 + x_97 + x_98 + x_109 + x_111 <= 1
- Constraint `36`: x_9 + x_32 + x_42 + x_43 + x_44 + x_55 + x_60 + x_64 + x_83 <= 1
- Constraint `37`: x_5 + x_10 + x_51 + x_54 + x_68 + x_73 + x_87 + x_91 + x_93 + x_102 + x_105 + x_113 + x_120 <= 1
- Constraint `38`: x_5 + x_16 + x_18 + x_21 + x_26 + x_39 + x_43 + x_55 + x_62 + x_75 + x_84 + x_87 + x_89 + x_97 <= 1
- Constraint `39`: x_5 + x_25 + x_37 + x_38 + x_53 + x_87 + x_104 + x_119 <= 1
- Constraint `40`: x_4 + x_6 + x_20 + x_43 + x_51 + x_70 + x_76 <= 1
- Constraint `41`: x_3 + x_18 + x_23 + x_24 + x_36 + x_44 + x_48 + x_54 + x_95 + x_105 <= 1
- Constraint `42`: x_6 + x_16 + x_21 + x_53 + x_63 + x_68 + x_69 + x_97 + x_107 <= 1
- Constraint `43`: x_57 + x_58 + x_75 + x_86 + x_88 + x_104 + x_106 <= 1
- Constraint `44`: x_3 + x_7 + x_9 + x_13 + x_28 + x_32 + x_34 + x_39 + x_42 + x_45 + x_52 + x_59 + x_60 + x_72 + x_79 + x_80 + x_82 + x_86 + x_102 + x_119 <= 1
- Constraint `45`: x_12 + x_15 + x_26 + x_27 + x_28 + x_31 + x_51 + x_64 + x_65 + x_67 + x_71 + x_93 + x_95 + x_110 + x_112 + x_117 <= 1
- Constraint `46`: x_2 + x_11 + x_14 + x_25 + x_29 + x_31 + x_43 + x_77 + x_87 + x_88 + x_96 + x_101 + x_105 + x_115 <= 1
- Constraint `47`: x_8 + x_12 + x_17 + x_26 + x_30 + x_35 + x_41 + x_48 + x_81 + x_83 + x_88 + x_90 + x_106 + x_107 + x_110 + x_115 + x_120 <= 1
- Constraint `48`: x_4 + x_24 + x_30 + x_38 + x_46 + x_62 + x_89 + x_92 + x_100 + x_105 + x_109 + x_117 <= 1
- Constraint `49`: x_13 + x_31 + x_34 + x_57 + x_62 + x_85 + x_109 <= 1
- Constraint `50`: x_18 + x_24 + x_37 + x_38 + x_45 + x_46 + x_54 + x_60 + x_62 + x_69 + x_78 + x_81 + x_83 + x_86 + x_91 + x_107 + x_115 <= 1
