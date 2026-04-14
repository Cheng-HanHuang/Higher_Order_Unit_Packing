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

w_1=0.59047449, w_2=1.7286533, w_3=1.7266326, w_4=1.9596639, w_5=0.55535455, w_6=1.6018711, w_7=0.84394019, w_8=0.67292505, w_9=1.1779034, w_10=1.1147193, w_11=0.94129322, w_12=1.9596128, w_13=1.8563397, w_14=1.4870392, w_15=1.1276965, w_16=0.74578304, w_17=1.1883787, w_18=1.3711343, w_19=1.845341, w_20=1.0237287, w_21=0.60844813, w_22=1.4889518, w_23=1.4577627, w_24=1.1593051, w_25=0.8460196, w_26=0.81628344, w_27=1.1230219, w_28=1.1685196, w_29=1.9452039, w_30=1.6252086, w_31=0.77237753, w_32=1.0687009, w_33=1.6698672, w_34=1.0641254, w_35=0.97272112, w_36=1.4978118, w_37=1.2828167, w_38=1.3384353, w_39=1.8277479, w_40=0.62097672, w_41=1.4545007, w_42=0.55267924, w_43=1.3737723, w_44=1.567778, w_45=1.1281809, w_46=1.2241983, w_47=0.9297024, w_48=0.86599831, w_49=1.8896595, w_50=0.55137959, w_51=1.2791974, w_52=0.98432055, w_53=1.6481016, w_54=1.3270719, w_55=1.7196878, w_56=1.4263538, w_57=1.1721889, w_58=1.7074635, w_59=1.7127098, w_60=1.402682, w_61=1.8847555, w_62=0.88229626, w_63=1.5351961, w_64=0.62383588, w_65=1.540926, w_66=1.1806001, w_67=1.5127071, w_68=0.92163648, w_69=1.7510786, w_70=0.57310479, w_71=1.6757395, w_72=1.4306729, w_73=1.9437728, w_74=0.55803568, w_75=0.70326101, w_76=0.9956368, w_77=1.8518058, w_78=1.3521829, w_79=0.82883853, w_80=0.99464888, w_81=1.857711, w_82=1.3683468, w_83=0.77774736, w_84=1.0323697, w_85=1.9336235, w_86=0.53912402, w_87=1.5005218, w_88=1.541786, w_89=0.52584664, w_90=0.58857021, w_91=1.5325214, w_92=0.513726, w_93=1.1748525, w_94=1.3781871, w_95=0.54345312, w_96=0.86465021, w_97=0.8448856, w_98=1.9710372, w_99=1.4031623, w_100=0.56696016, w_101=1.2716024, w_102=1.2138697, w_103=0.81858127, w_104=0.66685451, w_105=1.825557, w_106=1.1827975, w_107=1.2521337, w_108=1.9033864, w_109=0.51784068, w_110=1.7626961, w_111=0.95026356, w_112=0.96533714, w_113=1.1016229, w_114=1.9607687, w_115=1.7812246, w_116=1.3177582, w_117=1.6732409, w_118=1.4396646, w_119=1.5795213, w_120=0.76764698

## Candidate sets (variables)

- Variable `x_1` corresponds to set `A_1 = {7, 15, 19, 22, 26}`
- Variable `x_2` corresponds to set `A_2 = {6, 10, 22, 33, 47}`
- Variable `x_3` corresponds to set `A_3 = {9, 18, 19, 28, 36}`
- Variable `x_4` corresponds to set `A_4 = {5, 19, 36, 43, 47}`
- Variable `x_5` corresponds to set `A_5 = {8, 13, 17, 25, 41}`
- Variable `x_6` corresponds to set `A_6 = {4, 6, 8, 16, 49}`
- Variable `x_7` corresponds to set `A_7 = {3, 28, 29, 36, 39}`
- Variable `x_8` corresponds to set `A_8 = {11, 14, 19, 27, 48}`
- Variable `x_9` corresponds to set `A_9 = {14, 16, 23, 27, 31}`
- Variable `x_10` corresponds to set `A_10 = {2, 5, 10, 14, 25}`
- Variable `x_11` corresponds to set `A_11 = {14, 26, 28, 39, 40}`
- Variable `x_12` corresponds to set `A_12 = {13, 14, 22, 47, 48}`
- Variable `x_13` corresponds to set `A_13 = {3, 5, 31, 33, 38}`
- Variable `x_14` corresponds to set `A_14 = {6, 14, 41, 44, 47}`
- Variable `x_15` corresponds to set `A_15 = {9, 14, 32, 39, 43}`
- Variable `x_16` corresponds to set `A_16 = {3, 8, 16, 17, 42}`
- Variable `x_17` corresponds to set `A_17 = {1, 11, 19, 30, 31}`
- Variable `x_18` corresponds to set `A_18 = {5, 24, 25, 29, 35}`
- Variable `x_19` corresponds to set `A_19 = {4, 13, 18, 30, 44}`
- Variable `x_20` corresponds to set `A_20 = {9, 13, 26, 27, 45}`
- Variable `x_21` corresponds to set `A_21 = {22, 29, 32, 42, 49}`
- Variable `x_22` corresponds to set `A_22 = {2, 6, 10, 48, 49}`
- Variable `x_23` corresponds to set `A_23 = {2, 21, 30, 43, 45}`
- Variable `x_24` corresponds to set `A_24 = {17, 19, 27, 41, 47}`
- Variable `x_25` corresponds to set `A_25 = {8, 29, 30, 32, 36}`
- Variable `x_26` corresponds to set `A_26 = {14, 23, 46, 47, 50}`
- Variable `x_27` corresponds to set `A_27 = {5, 19, 20, 42, 50}`
- Variable `x_28` corresponds to set `A_28 = {1, 8, 10, 13, 23}`
- Variable `x_29` corresponds to set `A_29 = {1, 22, 24, 34, 50}`
- Variable `x_30` corresponds to set `A_30 = {2, 21, 28, 35, 44}`
- Variable `x_31` corresponds to set `A_31 = {20, 22, 25, 27, 50}`
- Variable `x_32` corresponds to set `A_32 = {14, 19, 28, 31, 40}`
- Variable `x_33` corresponds to set `A_33 = {16, 20, 30, 36, 44}`
- Variable `x_34` corresponds to set `A_34 = {6, 12, 30, 31, 46}`
- Variable `x_35` corresponds to set `A_35 = {1, 23, 24, 36, 43}`
- Variable `x_36` corresponds to set `A_36 = {2, 11, 22, 43, 49}`
- Variable `x_37` corresponds to set `A_37 = {2, 9, 17, 20, 32}`
- Variable `x_38` corresponds to set `A_38 = {4, 8, 34, 41, 44}`
- Variable `x_39` corresponds to set `A_39 = {7, 19, 24, 31, 40}`
- Variable `x_40` corresponds to set `A_40 = {9, 20, 21, 34, 39}`
- Variable `x_41` corresponds to set `A_41 = {8, 22, 23, 31, 50}`
- Variable `x_42` corresponds to set `A_42 = {2, 15, 34, 37, 40}`
- Variable `x_43` corresponds to set `A_43 = {12, 15, 20, 21, 32}`
- Variable `x_44` corresponds to set `A_44 = {7, 26, 28, 34, 42}`
- Variable `x_45` corresponds to set `A_45 = {11, 18, 22, 35, 42}`
- Variable `x_46` corresponds to set `A_46 = {5, 15, 24, 26, 39}`
- Variable `x_47` corresponds to set `A_47 = {12, 14, 26, 37, 38}`
- Variable `x_48` corresponds to set `A_48 = {8, 11, 23, 26, 47}`
- Variable `x_49` corresponds to set `A_49 = {13, 18, 24, 29, 39}`
- Variable `x_50` corresponds to set `A_50 = {2, 7, 36, 40, 47}`
- Variable `x_51` corresponds to set `A_51 = {3, 24, 33, 41, 45}`
- Variable `x_52` corresponds to set `A_52 = {21, 30, 45, 46, 50}`
- Variable `x_53` corresponds to set `A_53 = {4, 6, 13, 18, 46}`
- Variable `x_54` corresponds to set `A_54 = {7, 27, 32, 37, 45}`
- Variable `x_55` corresponds to set `A_55 = {13, 25, 29, 31, 39}`
- Variable `x_56` corresponds to set `A_56 = {2, 18, 33, 35, 46}`
- Variable `x_57` corresponds to set `A_57 = {13, 21, 23, 41, 47}`
- Variable `x_58` corresponds to set `A_58 = {34, 36, 43, 47, 48}`
- Variable `x_59` corresponds to set `A_59 = {13, 23, 30, 36, 45}`
- Variable `x_60` corresponds to set `A_60 = {6, 9, 24, 29, 31}`
- Variable `x_61` corresponds to set `A_61 = {8, 12, 24, 28, 45}`
- Variable `x_62` corresponds to set `A_62 = {8, 11, 33, 38, 44}`
- Variable `x_63` corresponds to set `A_63 = {10, 30, 37, 44, 45}`
- Variable `x_64` corresponds to set `A_64 = {8, 24, 34, 37, 39}`
- Variable `x_65` corresponds to set `A_65 = {13, 22, 23, 39, 47}`
- Variable `x_66` corresponds to set `A_66 = {5, 7, 41, 46, 48}`
- Variable `x_67` corresponds to set `A_67 = {7, 20, 25, 37, 38}`
- Variable `x_68` corresponds to set `A_68 = {4, 6, 29, 36, 50}`
- Variable `x_69` corresponds to set `A_69 = {5, 9, 30, 43, 45}`
- Variable `x_70` corresponds to set `A_70 = {10, 16, 18, 35, 45}`
- Variable `x_71` corresponds to set `A_71 = {10, 22, 31, 36, 40}`
- Variable `x_72` corresponds to set `A_72 = {2, 8, 29, 40, 46}`
- Variable `x_73` corresponds to set `A_73 = {5, 19, 20, 40, 41}`
- Variable `x_74` corresponds to set `A_74 = {5, 30, 33, 35, 38}`
- Variable `x_75` corresponds to set `A_75 = {25, 30, 32, 39, 45}`
- Variable `x_76` corresponds to set `A_76 = {4, 19, 28, 32, 44}`
- Variable `x_77` corresponds to set `A_77 = {15, 18, 20, 34, 36}`
- Variable `x_78` corresponds to set `A_78 = {1, 10, 11, 35, 45}`
- Variable `x_79` corresponds to set `A_79 = {2, 10, 11, 31, 48}`
- Variable `x_80` corresponds to set `A_80 = {3, 7, 8, 20, 44}`
- Variable `x_81` corresponds to set `A_81 = {18, 21, 31, 34, 35}`
- Variable `x_82` corresponds to set `A_82 = {21, 25, 31, 43, 44}`
- Variable `x_83` corresponds to set `A_83 = {12, 14, 16, 37, 47}`
- Variable `x_84` corresponds to set `A_84 = {5, 11, 12, 28, 39}`
- Variable `x_85` corresponds to set `A_85 = {4, 16, 22, 47, 50}`
- Variable `x_86` corresponds to set `A_86 = {19, 22, 23, 36, 39}`
- Variable `x_87` corresponds to set `A_87 = {15, 18, 31, 36, 43}`
- Variable `x_88` corresponds to set `A_88 = {12, 16, 19, 28, 33}`
- Variable `x_89` corresponds to set `A_89 = {2, 5, 15, 31, 44}`
- Variable `x_90` corresponds to set `A_90 = {6, 17, 20, 23, 37}`
- Variable `x_91` corresponds to set `A_91 = {1, 3, 18, 35, 49}`
- Variable `x_92` corresponds to set `A_92 = {6, 28, 33, 41, 43}`
- Variable `x_93` corresponds to set `A_93 = {2, 24, 40, 49, 50}`
- Variable `x_94` corresponds to set `A_94 = {7, 16, 41, 43, 50}`
- Variable `x_95` corresponds to set `A_95 = {12, 13, 19, 28, 32}`
- Variable `x_96` corresponds to set `A_96 = {2, 24, 26, 29, 37}`
- Variable `x_97` corresponds to set `A_97 = {4, 23, 29, 33, 37}`
- Variable `x_98` corresponds to set `A_98 = {9, 15, 30, 38, 40}`
- Variable `x_99` corresponds to set `A_99 = {10, 11, 22, 25, 48}`
- Variable `x_100` corresponds to set `A_100 = {1, 16, 23, 32, 42}`
- Variable `x_101` corresponds to set `A_101 = {8, 15, 25, 43, 48}`
- Variable `x_102` corresponds to set `A_102 = {3, 6, 15, 28, 43}`
- Variable `x_103` corresponds to set `A_103 = {17, 20, 32, 34, 47}`
- Variable `x_104` corresponds to set `A_104 = {3, 6, 13, 46, 49}`
- Variable `x_105` corresponds to set `A_105 = {7, 9, 17, 29, 31}`
- Variable `x_106` corresponds to set `A_106 = {1, 6, 36, 43, 47}`
- Variable `x_107` corresponds to set `A_107 = {2, 11, 23, 25, 38}`
- Variable `x_108` corresponds to set `A_108 = {12, 14, 22, 43, 49}`
- Variable `x_109` corresponds to set `A_109 = {2, 14, 22, 42, 46}`
- Variable `x_110` corresponds to set `A_110 = {6, 16, 21, 39, 41}`
- Variable `x_111` corresponds to set `A_111 = {16, 19, 26, 28, 33}`
- Variable `x_112` corresponds to set `A_112 = {3, 25, 30, 34, 44}`
- Variable `x_113` corresponds to set `A_113 = {3, 11, 14, 29, 38}`
- Variable `x_114` corresponds to set `A_114 = {6, 26, 33, 34, 39}`
- Variable `x_115` corresponds to set `A_115 = {1, 11, 25, 28, 42}`
- Variable `x_116` corresponds to set `A_116 = {10, 20, 38, 43, 47}`
- Variable `x_117` corresponds to set `A_117 = {11, 29, 32, 46, 49}`
- Variable `x_118` corresponds to set `A_118 = {3, 22, 29, 34, 50}`
- Variable `x_119` corresponds to set `A_119 = {8, 9, 35, 38, 48}`
- Variable `x_120` corresponds to set `A_120 = {14, 17, 24, 28, 31}`

## Exact constraints

- Constraint `1`: x_17 + x_28 + x_29 + x_35 + x_78 + x_91 + x_100 + x_106 + x_115 <= 1
- Constraint `2`: x_10 + x_22 + x_23 + x_30 + x_36 + x_37 + x_42 + x_50 + x_56 + x_72 + x_79 + x_89 + x_93 + x_96 + x_107 + x_109 <= 1
- Constraint `3`: x_7 + x_13 + x_16 + x_51 + x_80 + x_91 + x_102 + x_104 + x_112 + x_113 + x_118 <= 1
- Constraint `4`: x_6 + x_19 + x_38 + x_53 + x_68 + x_76 + x_85 + x_97 <= 1
- Constraint `5`: x_4 + x_10 + x_13 + x_18 + x_27 + x_46 + x_66 + x_69 + x_73 + x_74 + x_84 + x_89 <= 1
- Constraint `6`: x_2 + x_6 + x_14 + x_22 + x_34 + x_53 + x_60 + x_68 + x_90 + x_92 + x_102 + x_104 + x_106 + x_110 + x_114 <= 1
- Constraint `7`: x_1 + x_39 + x_44 + x_50 + x_54 + x_66 + x_67 + x_80 + x_94 + x_105 <= 1
- Constraint `8`: x_5 + x_6 + x_16 + x_25 + x_28 + x_38 + x_41 + x_48 + x_61 + x_62 + x_64 + x_72 + x_80 + x_101 + x_119 <= 1
- Constraint `9`: x_3 + x_15 + x_20 + x_37 + x_40 + x_60 + x_69 + x_98 + x_105 + x_119 <= 1
- Constraint `10`: x_2 + x_10 + x_22 + x_28 + x_63 + x_70 + x_71 + x_78 + x_79 + x_99 + x_116 <= 1
- Constraint `11`: x_8 + x_17 + x_36 + x_45 + x_48 + x_62 + x_78 + x_79 + x_84 + x_99 + x_107 + x_113 + x_115 + x_117 <= 1
- Constraint `12`: x_34 + x_43 + x_47 + x_61 + x_83 + x_84 + x_88 + x_95 + x_108 <= 1
- Constraint `13`: x_5 + x_12 + x_19 + x_20 + x_28 + x_49 + x_53 + x_55 + x_57 + x_59 + x_65 + x_95 + x_104 <= 1
- Constraint `14`: x_8 + x_9 + x_10 + x_11 + x_12 + x_14 + x_15 + x_26 + x_32 + x_47 + x_83 + x_108 + x_109 + x_113 + x_120 <= 1
- Constraint `15`: x_1 + x_42 + x_43 + x_46 + x_77 + x_87 + x_89 + x_98 + x_101 + x_102 <= 1
- Constraint `16`: x_6 + x_9 + x_16 + x_33 + x_70 + x_83 + x_85 + x_88 + x_94 + x_100 + x_110 + x_111 <= 1
- Constraint `17`: x_5 + x_16 + x_24 + x_37 + x_90 + x_103 + x_105 + x_120 <= 1
- Constraint `18`: x_3 + x_19 + x_45 + x_49 + x_53 + x_56 + x_70 + x_77 + x_81 + x_87 + x_91 <= 1
- Constraint `19`: x_1 + x_3 + x_4 + x_8 + x_17 + x_24 + x_27 + x_32 + x_39 + x_73 + x_76 + x_86 + x_88 + x_95 + x_111 <= 1
- Constraint `20`: x_27 + x_31 + x_33 + x_37 + x_40 + x_43 + x_67 + x_73 + x_77 + x_80 + x_90 + x_103 + x_116 <= 1
- Constraint `21`: x_23 + x_30 + x_40 + x_43 + x_52 + x_57 + x_81 + x_82 + x_110 <= 1
- Constraint `22`: x_1 + x_2 + x_12 + x_21 + x_29 + x_31 + x_36 + x_41 + x_45 + x_65 + x_71 + x_85 + x_86 + x_99 + x_108 + x_109 + x_118 <= 1
- Constraint `23`: x_9 + x_26 + x_28 + x_35 + x_41 + x_48 + x_57 + x_59 + x_65 + x_86 + x_90 + x_97 + x_100 + x_107 <= 1
- Constraint `24`: x_18 + x_29 + x_35 + x_39 + x_46 + x_49 + x_51 + x_60 + x_61 + x_64 + x_93 + x_96 + x_120 <= 1
- Constraint `25`: x_5 + x_10 + x_18 + x_31 + x_55 + x_67 + x_75 + x_82 + x_99 + x_101 + x_107 + x_112 + x_115 <= 1
- Constraint `26`: x_1 + x_11 + x_20 + x_44 + x_46 + x_47 + x_48 + x_96 + x_111 + x_114 <= 1
- Constraint `27`: x_8 + x_9 + x_20 + x_24 + x_31 + x_54 <= 1
- Constraint `28`: x_3 + x_7 + x_11 + x_30 + x_32 + x_44 + x_61 + x_76 + x_84 + x_88 + x_92 + x_95 + x_102 + x_111 + x_115 + x_120 <= 1
- Constraint `29`: x_7 + x_18 + x_21 + x_25 + x_49 + x_55 + x_60 + x_68 + x_72 + x_96 + x_97 + x_105 + x_113 + x_117 + x_118 <= 1
- Constraint `30`: x_17 + x_19 + x_23 + x_25 + x_33 + x_34 + x_52 + x_59 + x_63 + x_69 + x_74 + x_75 + x_98 + x_112 <= 1
- Constraint `31`: x_9 + x_13 + x_17 + x_32 + x_34 + x_39 + x_41 + x_55 + x_60 + x_71 + x_79 + x_81 + x_82 + x_87 + x_89 + x_105 + x_120 <= 1
- Constraint `32`: x_15 + x_21 + x_25 + x_37 + x_43 + x_54 + x_75 + x_76 + x_95 + x_100 + x_103 + x_117 <= 1
- Constraint `33`: x_2 + x_13 + x_51 + x_56 + x_62 + x_74 + x_88 + x_92 + x_97 + x_111 + x_114 <= 1
- Constraint `34`: x_29 + x_38 + x_40 + x_42 + x_44 + x_58 + x_64 + x_77 + x_81 + x_103 + x_112 + x_114 + x_118 <= 1
- Constraint `35`: x_18 + x_30 + x_45 + x_56 + x_70 + x_74 + x_78 + x_81 + x_91 + x_119 <= 1
- Constraint `36`: x_3 + x_4 + x_7 + x_25 + x_33 + x_35 + x_50 + x_58 + x_59 + x_68 + x_71 + x_77 + x_86 + x_87 + x_106 <= 1
- Constraint `37`: x_42 + x_47 + x_54 + x_63 + x_64 + x_67 + x_83 + x_90 + x_96 + x_97 <= 1
- Constraint `38`: x_13 + x_47 + x_62 + x_67 + x_74 + x_98 + x_107 + x_113 + x_116 + x_119 <= 1
- Constraint `39`: x_7 + x_11 + x_15 + x_40 + x_46 + x_49 + x_55 + x_64 + x_65 + x_75 + x_84 + x_86 + x_110 + x_114 <= 1
- Constraint `40`: x_11 + x_32 + x_39 + x_42 + x_50 + x_71 + x_72 + x_73 + x_93 + x_98 <= 1
- Constraint `41`: x_5 + x_14 + x_24 + x_38 + x_51 + x_57 + x_66 + x_73 + x_92 + x_94 + x_110 <= 1
- Constraint `42`: x_16 + x_21 + x_27 + x_44 + x_45 + x_100 + x_109 + x_115 <= 1
- Constraint `43`: x_4 + x_15 + x_23 + x_35 + x_36 + x_58 + x_69 + x_82 + x_87 + x_92 + x_94 + x_101 + x_102 + x_106 + x_108 + x_116 <= 1
- Constraint `44`: x_14 + x_19 + x_30 + x_33 + x_38 + x_62 + x_63 + x_76 + x_80 + x_82 + x_89 + x_112 <= 1
- Constraint `45`: x_20 + x_23 + x_51 + x_52 + x_54 + x_59 + x_61 + x_63 + x_69 + x_70 + x_75 + x_78 <= 1
- Constraint `46`: x_26 + x_34 + x_52 + x_53 + x_56 + x_66 + x_72 + x_104 + x_109 + x_117 <= 1
- Constraint `47`: x_2 + x_4 + x_12 + x_14 + x_24 + x_26 + x_48 + x_50 + x_57 + x_58 + x_65 + x_83 + x_85 + x_103 + x_106 + x_116 <= 1
- Constraint `48`: x_8 + x_12 + x_22 + x_58 + x_66 + x_79 + x_99 + x_101 + x_119 <= 1
- Constraint `49`: x_6 + x_21 + x_22 + x_36 + x_91 + x_93 + x_104 + x_108 + x_117 <= 1
- Constraint `50`: x_26 + x_27 + x_29 + x_31 + x_41 + x_52 + x_68 + x_85 + x_93 + x_94 + x_118 <= 1
