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

w_1=0.54160509, w_2=1.281022, w_3=1.3280098, w_4=1.5947225, w_5=1.5546121, w_6=0.69708686, w_7=1.6553107, w_8=0.82299208, w_9=0.80172491, w_10=1.4116272, w_11=1.1267159, w_12=1.3210445, w_13=0.88497792, w_14=1.9632404, w_15=1.4151547, w_16=1.7494198, w_17=1.9387494, w_18=1.2966444, w_19=1.0574729, w_20=0.62644998, w_21=1.1835252, w_22=0.55552444, w_23=0.70597354, w_24=0.72581961, w_25=1.4013202, w_26=1.1262938, w_27=1.8814123, w_28=1.0252158, w_29=1.4462308, w_30=1.2483017, w_31=1.4414765, w_32=1.8392981, w_33=1.9439172, w_34=1.0362082, w_35=0.76367775, w_36=0.71009859, w_37=0.7589762, w_38=1.1778828, w_39=1.9758537, w_40=1.4771642, w_41=1.823938, w_42=0.89146188, w_43=1.5475783, w_44=0.57453804, w_45=0.90653279, w_46=1.3091112, w_47=1.6759036, w_48=0.84693837, w_49=1.5412443, w_50=0.93644762, w_51=0.68745818, w_52=0.82079949, w_53=1.0717148, w_54=1.0248723, w_55=1.4738514, w_56=1.212821, w_57=1.0444975, w_58=1.6126112, w_59=0.86701973, w_60=1.1694405, w_61=1.0644748, w_62=0.66854591, w_63=1.1968078, w_64=1.3596898, w_65=1.9132063, w_66=0.99349349, w_67=0.90773024, w_68=1.5547568, w_69=1.5968537, w_70=0.64455742, w_71=1.866496, w_72=1.9250133, w_73=1.3731037, w_74=1.1589569, w_75=0.92369914, w_76=0.83313698, w_77=0.71237764, w_78=1.6475037, w_79=1.3577789, w_80=1.1357335, w_81=0.65414685, w_82=1.7709744, w_83=0.51481793, w_84=0.51567164, w_85=0.96352989, w_86=0.60530988, w_87=1.4802369, w_88=1.9434034, w_89=1.7296408, w_90=1.6518283, w_91=1.859647, w_92=0.9292975, w_93=1.0721262, w_94=1.851825, w_95=0.65760601, w_96=1.6360055, w_97=0.5084473, w_98=1.752428, w_99=1.8668105, w_100=1.2670229

## Candidate sets (variables)

- Variable `x_1` corresponds to set `A_1 = {2, 6, 14, 18, 39}`
- Variable `x_2` corresponds to set `A_2 = {4, 21, 24, 28, 35}`
- Variable `x_3` corresponds to set `A_3 = {1, 15, 18, 23, 31}`
- Variable `x_4` corresponds to set `A_4 = {19, 20, 21, 23, 33}`
- Variable `x_5` corresponds to set `A_5 = {7, 9, 12, 22, 38}`
- Variable `x_6` corresponds to set `A_6 = {12, 17, 24, 28, 36}`
- Variable `x_7` corresponds to set `A_7 = {1, 14, 24, 25, 26}`
- Variable `x_8` corresponds to set `A_8 = {3, 4, 7, 10, 31}`
- Variable `x_9` corresponds to set `A_9 = {3, 5, 19, 22, 37}`
- Variable `x_10` corresponds to set `A_10 = {13, 17, 18, 24, 39}`
- Variable `x_11` corresponds to set `A_11 = {2, 12, 20, 26, 29}`
- Variable `x_12` corresponds to set `A_12 = {6, 28, 32, 33, 34}`
- Variable `x_13` corresponds to set `A_13 = {15, 26, 28, 30, 37}`
- Variable `x_14` corresponds to set `A_14 = {8, 17, 20, 29, 38}`
- Variable `x_15` corresponds to set `A_15 = {2, 7, 8, 16, 23}`
- Variable `x_16` corresponds to set `A_16 = {6, 12, 26, 29, 35}`
- Variable `x_17` corresponds to set `A_17 = {6, 9, 26, 31, 36}`
- Variable `x_18` corresponds to set `A_18 = {5, 14, 18, 33, 37}`
- Variable `x_19` corresponds to set `A_19 = {6, 10, 20, 31, 36}`
- Variable `x_20` corresponds to set `A_20 = {2, 17, 32, 36, 37}`
- Variable `x_21` corresponds to set `A_21 = {10, 14, 23, 28, 29}`
- Variable `x_22` corresponds to set `A_22 = {8, 16, 21, 37, 40}`
- Variable `x_23` corresponds to set `A_23 = {8, 17, 18, 29, 35}`
- Variable `x_24` corresponds to set `A_24 = {4, 12, 20, 29, 39}`
- Variable `x_25` corresponds to set `A_25 = {17, 18, 21, 27, 34}`
- Variable `x_26` corresponds to set `A_26 = {1, 10, 11, 15, 22}`
- Variable `x_27` corresponds to set `A_27 = {4, 9, 20, 25, 34}`
- Variable `x_28` corresponds to set `A_28 = {9, 17, 19, 25, 28}`
- Variable `x_29` corresponds to set `A_29 = {9, 15, 17, 26, 38}`
- Variable `x_30` corresponds to set `A_30 = {2, 8, 9, 18, 31}`
- Variable `x_31` corresponds to set `A_31 = {3, 4, 7, 11, 13}`
- Variable `x_32` corresponds to set `A_32 = {6, 17, 28, 29, 39}`
- Variable `x_33` corresponds to set `A_33 = {9, 11, 14, 32, 36}`
- Variable `x_34` corresponds to set `A_34 = {2, 9, 18, 22, 30}`
- Variable `x_35` corresponds to set `A_35 = {1, 11, 17, 22, 35}`
- Variable `x_36` corresponds to set `A_36 = {4, 8, 17, 27, 34}`
- Variable `x_37` corresponds to set `A_37 = {1, 3, 8, 24, 32}`
- Variable `x_38` corresponds to set `A_38 = {4, 7, 12, 17, 36}`
- Variable `x_39` corresponds to set `A_39 = {2, 5, 11, 12, 21}`
- Variable `x_40` corresponds to set `A_40 = {2, 19, 26, 28, 31}`
- Variable `x_41` corresponds to set `A_41 = {3, 15, 18, 23, 26}`
- Variable `x_42` corresponds to set `A_42 = {15, 17, 18, 26, 39}`
- Variable `x_43` corresponds to set `A_43 = {1, 18, 25, 31, 40}`
- Variable `x_44` corresponds to set `A_44 = {5, 17, 24, 29, 39}`
- Variable `x_45` corresponds to set `A_45 = {7, 12, 15, 16, 35}`
- Variable `x_46` corresponds to set `A_46 = {2, 3, 23, 26, 38}`
- Variable `x_47` corresponds to set `A_47 = {6, 14, 17, 18, 40}`
- Variable `x_48` corresponds to set `A_48 = {2, 3, 5, 13, 19}`
- Variable `x_49` corresponds to set `A_49 = {10, 14, 22, 28, 33}`
- Variable `x_50` corresponds to set `A_50 = {1, 7, 21, 23, 32}`
- Variable `x_51` corresponds to set `A_51 = {16, 17, 18, 38, 40}`
- Variable `x_52` corresponds to set `A_52 = {19, 22, 31, 35, 40}`
- Variable `x_53` corresponds to set `A_53 = {8, 14, 23, 25, 36}`
- Variable `x_54` corresponds to set `A_54 = {16, 21, 27, 28, 38}`
- Variable `x_55` corresponds to set `A_55 = {1, 3, 18, 31, 32}`
- Variable `x_56` corresponds to set `A_56 = {11, 15, 23, 34, 40}`
- Variable `x_57` corresponds to set `A_57 = {3, 9, 21, 22, 27}`
- Variable `x_58` corresponds to set `A_58 = {6, 11, 16, 27, 31}`
- Variable `x_59` corresponds to set `A_59 = {2, 12, 14, 26, 35}`
- Variable `x_60` corresponds to set `A_60 = {4, 15, 23, 30, 33}`
- Variable `x_61` corresponds to set `A_61 = {15, 23, 34, 38, 40}`
- Variable `x_62` corresponds to set `A_62 = {5, 11, 27, 35, 39}`
- Variable `x_63` corresponds to set `A_63 = {3, 9, 16, 20, 30}`
- Variable `x_64` corresponds to set `A_64 = {1, 14, 17, 26, 32}`
- Variable `x_65` corresponds to set `A_65 = {17, 22, 23, 27, 28}`
- Variable `x_66` corresponds to set `A_66 = {12, 13, 14, 28, 36}`
- Variable `x_67` corresponds to set `A_67 = {1, 3, 22, 26, 37}`
- Variable `x_68` corresponds to set `A_68 = {1, 6, 30, 36, 37}`
- Variable `x_69` corresponds to set `A_69 = {15, 18, 21, 26, 36}`
- Variable `x_70` corresponds to set `A_70 = {5, 23, 30, 32, 37}`
- Variable `x_71` corresponds to set `A_71 = {12, 21, 26, 28, 39}`
- Variable `x_72` corresponds to set `A_72 = {24, 25, 28, 29, 40}`
- Variable `x_73` corresponds to set `A_73 = {7, 13, 17, 19, 34}`
- Variable `x_74` corresponds to set `A_74 = {3, 5, 14, 16, 18}`
- Variable `x_75` corresponds to set `A_75 = {2, 8, 16, 25, 31}`
- Variable `x_76` corresponds to set `A_76 = {2, 12, 21, 24, 35}`
- Variable `x_77` corresponds to set `A_77 = {3, 4, 20, 23, 27}`
- Variable `x_78` corresponds to set `A_78 = {5, 13, 20, 27, 36}`
- Variable `x_79` corresponds to set `A_79 = {18, 28, 33, 35, 39}`
- Variable `x_80` corresponds to set `A_80 = {4, 10, 13, 25, 33}`
- Variable `x_81` corresponds to set `A_81 = {9, 18, 20, 28, 39}`
- Variable `x_82` corresponds to set `A_82 = {1, 6, 15, 17, 29}`
- Variable `x_83` corresponds to set `A_83 = {2, 14, 15, 28, 29}`
- Variable `x_84` corresponds to set `A_84 = {1, 2, 15, 19, 35}`
- Variable `x_85` corresponds to set `A_85 = {4, 13, 16, 20, 27}`
- Variable `x_86` corresponds to set `A_86 = {2, 3, 20, 22, 36}`
- Variable `x_87` corresponds to set `A_87 = {7, 10, 11, 13, 32}`
- Variable `x_88` corresponds to set `A_88 = {11, 13, 18, 24, 31}`
- Variable `x_89` corresponds to set `A_89 = {4, 15, 21, 24, 32}`
- Variable `x_90` corresponds to set `A_90 = {2, 10, 20, 32, 37}`
- Variable `x_91` corresponds to set `A_91 = {4, 18, 20, 27, 31}`
- Variable `x_92` corresponds to set `A_92 = {5, 7, 10, 16, 28}`
- Variable `x_93` corresponds to set `A_93 = {8, 12, 14, 15, 39}`
- Variable `x_94` corresponds to set `A_94 = {4, 15, 16, 18, 32}`
- Variable `x_95` corresponds to set `A_95 = {2, 8, 9, 12, 27}`
- Variable `x_96` corresponds to set `A_96 = {4, 15, 32, 34, 37}`
- Variable `x_97` corresponds to set `A_97 = {2, 10, 17, 25, 32}`
- Variable `x_98` corresponds to set `A_98 = {2, 5, 6, 14, 16}`
- Variable `x_99` corresponds to set `A_99 = {8, 11, 25, 30, 38}`
- Variable `x_100` corresponds to set `A_100 = {5, 10, 16, 27, 40}`

## Exact constraints

- Constraint `1`: x_3 + x_7 + x_26 + x_35 + x_37 + x_43 + x_50 + x_55 + x_64 + x_67 + x_68 + x_82 + x_84 <= 1
- Constraint `2`: x_1 + x_11 + x_15 + x_20 + x_30 + x_34 + x_39 + x_40 + x_46 + x_48 + x_59 + x_75 + x_76 + x_83 + x_84 + x_86 + x_90 + x_95 + x_97 + x_98 <= 1
- Constraint `3`: x_8 + x_9 + x_31 + x_37 + x_41 + x_46 + x_48 + x_55 + x_57 + x_63 + x_67 + x_74 + x_77 + x_86 <= 1
- Constraint `4`: x_2 + x_8 + x_24 + x_27 + x_31 + x_36 + x_38 + x_60 + x_77 + x_80 + x_85 + x_89 + x_91 + x_94 + x_96 <= 1
- Constraint `5`: x_9 + x_18 + x_39 + x_44 + x_48 + x_62 + x_70 + x_74 + x_78 + x_92 + x_98 + x_100 <= 1
- Constraint `6`: x_1 + x_12 + x_16 + x_17 + x_19 + x_32 + x_47 + x_58 + x_68 + x_82 + x_98 <= 1
- Constraint `7`: x_5 + x_8 + x_15 + x_31 + x_38 + x_45 + x_50 + x_73 + x_87 + x_92 <= 1
- Constraint `8`: x_14 + x_15 + x_22 + x_23 + x_30 + x_36 + x_37 + x_53 + x_75 + x_93 + x_95 + x_99 <= 1
- Constraint `9`: x_5 + x_17 + x_27 + x_28 + x_29 + x_30 + x_33 + x_34 + x_57 + x_63 + x_81 + x_95 <= 1
- Constraint `10`: x_8 + x_19 + x_21 + x_26 + x_49 + x_80 + x_87 + x_90 + x_92 + x_97 + x_100 <= 1
- Constraint `11`: x_26 + x_31 + x_33 + x_35 + x_39 + x_56 + x_58 + x_62 + x_87 + x_88 + x_99 <= 1
- Constraint `12`: x_5 + x_6 + x_11 + x_16 + x_24 + x_38 + x_39 + x_45 + x_59 + x_66 + x_71 + x_76 + x_93 + x_95 <= 1
- Constraint `13`: x_10 + x_31 + x_48 + x_66 + x_73 + x_78 + x_80 + x_85 + x_87 + x_88 <= 1
- Constraint `14`: x_1 + x_7 + x_18 + x_21 + x_33 + x_47 + x_49 + x_53 + x_59 + x_64 + x_66 + x_74 + x_83 + x_93 + x_98 <= 1
- Constraint `15`: x_3 + x_13 + x_26 + x_29 + x_41 + x_42 + x_45 + x_56 + x_60 + x_61 + x_69 + x_82 + x_83 + x_84 + x_89 + x_93 + x_94 + x_96 <= 1
- Constraint `16`: x_15 + x_22 + x_45 + x_51 + x_54 + x_58 + x_63 + x_74 + x_75 + x_85 + x_92 + x_94 + x_98 + x_100 <= 1
- Constraint `17`: x_6 + x_10 + x_14 + x_20 + x_23 + x_25 + x_28 + x_29 + x_32 + x_35 + x_36 + x_38 + x_42 + x_44 + x_47 + x_51 + x_64 + x_65 + x_73 + x_82 + x_97 <= 1
- Constraint `18`: x_1 + x_3 + x_10 + x_18 + x_23 + x_25 + x_30 + x_34 + x_41 + x_42 + x_43 + x_47 + x_51 + x_55 + x_69 + x_74 + x_79 + x_81 + x_88 + x_91 + x_94 <= 1
- Constraint `19`: x_4 + x_9 + x_28 + x_40 + x_48 + x_52 + x_73 + x_84 <= 1
- Constraint `20`: x_4 + x_11 + x_14 + x_19 + x_24 + x_27 + x_63 + x_77 + x_78 + x_81 + x_85 + x_86 + x_90 + x_91 <= 1
- Constraint `21`: x_2 + x_4 + x_22 + x_25 + x_39 + x_50 + x_54 + x_57 + x_69 + x_71 + x_76 + x_89 <= 1
- Constraint `22`: x_5 + x_9 + x_26 + x_34 + x_35 + x_49 + x_52 + x_57 + x_65 + x_67 + x_86 <= 1
- Constraint `23`: x_3 + x_4 + x_15 + x_21 + x_41 + x_46 + x_50 + x_53 + x_56 + x_60 + x_61 + x_65 + x_70 + x_77 <= 1
- Constraint `24`: x_2 + x_6 + x_7 + x_10 + x_37 + x_44 + x_72 + x_76 + x_88 + x_89 <= 1
- Constraint `25`: x_7 + x_27 + x_28 + x_43 + x_53 + x_72 + x_75 + x_80 + x_97 + x_99 <= 1
- Constraint `26`: x_7 + x_11 + x_13 + x_16 + x_17 + x_29 + x_40 + x_41 + x_42 + x_46 + x_59 + x_64 + x_67 + x_69 + x_71 <= 1
- Constraint `27`: x_25 + x_36 + x_54 + x_57 + x_58 + x_62 + x_65 + x_77 + x_78 + x_85 + x_91 + x_95 + x_100 <= 1
- Constraint `28`: x_2 + x_6 + x_12 + x_13 + x_21 + x_28 + x_32 + x_40 + x_49 + x_54 + x_65 + x_66 + x_71 + x_72 + x_79 + x_81 + x_83 + x_92 <= 1
- Constraint `29`: x_11 + x_14 + x_16 + x_21 + x_23 + x_24 + x_32 + x_44 + x_72 + x_82 + x_83 <= 1
- Constraint `30`: x_13 + x_34 + x_60 + x_63 + x_68 + x_70 + x_99 <= 1
- Constraint `31`: x_3 + x_8 + x_17 + x_19 + x_30 + x_40 + x_43 + x_52 + x_55 + x_58 + x_75 + x_88 + x_91 <= 1
- Constraint `32`: x_12 + x_20 + x_33 + x_37 + x_50 + x_55 + x_64 + x_70 + x_87 + x_89 + x_90 + x_94 + x_96 + x_97 <= 1
- Constraint `33`: x_4 + x_12 + x_18 + x_49 + x_60 + x_79 + x_80 <= 1
- Constraint `34`: x_12 + x_25 + x_27 + x_36 + x_56 + x_61 + x_73 + x_96 <= 1
- Constraint `35`: x_2 + x_16 + x_23 + x_35 + x_45 + x_52 + x_59 + x_62 + x_76 + x_79 + x_84 <= 1
- Constraint `36`: x_6 + x_17 + x_19 + x_20 + x_33 + x_38 + x_53 + x_66 + x_68 + x_69 + x_78 + x_86 <= 1
- Constraint `37`: x_9 + x_13 + x_18 + x_20 + x_22 + x_67 + x_68 + x_70 + x_90 + x_96 <= 1
- Constraint `38`: x_5 + x_14 + x_29 + x_46 + x_51 + x_54 + x_61 + x_99 <= 1
- Constraint `39`: x_1 + x_10 + x_24 + x_32 + x_42 + x_44 + x_62 + x_71 + x_79 + x_81 + x_93 <= 1
- Constraint `40`: x_22 + x_43 + x_47 + x_51 + x_52 + x_56 + x_61 + x_72 + x_100 <= 1
