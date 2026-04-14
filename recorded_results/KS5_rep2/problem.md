# Original problem: kset_u60_n150_k6

This file records the exact original binary packing problem used for the matching run result.

## Optimization model

\[
\max_{x\in\{0,1\}^n}\ \sum_{i=1}^n w_i x_i
\qquad\text{s.t.}\qquad
\sum_{i\in S_k} x_i \le B_k,\quad k=1,\dots,m.
\]

- Number of variables: `150`
- Number of constraints: `60`
- Matching run-result file: `result.json`

## Metadata

- `generator`: `random_k_set_packing`
- `universe_size`: `60`
- `k`: `6`
- `density`: `0.7`

## Weights

w_1=0.97954093, w_2=0.50014909, w_3=1.6744348, w_4=0.67871738, w_5=1.4681676, w_6=1.71252, w_7=0.50336595, w_8=0.72891623, w_9=1.0771376, w_10=0.89562938, w_11=1.903553, w_12=1.172986, w_13=1.9593268, w_14=1.6678242, w_15=1.3263597, w_16=1.4508333, w_17=1.1017216, w_18=1.0817633, w_19=1.0176181, w_20=1.9488602, w_21=0.68473029, w_22=1.3637563, w_23=0.73295932, w_24=1.6997634, w_25=1.9198765, w_26=1.8797241, w_27=1.5035605, w_28=1.65421, w_29=0.70402509, w_30=1.7768715, w_31=1.560707, w_32=0.52597838, w_33=0.87271818, w_34=1.0944197, w_35=1.7562264, w_36=1.794778, w_37=0.51346398, w_38=1.8394187, w_39=1.0357372, w_40=0.820094, w_41=1.3867643, w_42=0.65290762, w_43=1.842668, w_44=1.7053837, w_45=1.5518808, w_46=1.4280073, w_47=0.52428414, w_48=1.0612172, w_49=1.0347877, w_50=1.0651469, w_51=0.92341385, w_52=1.9191213, w_53=0.59399069, w_54=1.3269759, w_55=0.95237061, w_56=1.9645477, w_57=1.8241349, w_58=1.5650316, w_59=1.530781, w_60=1.2701814, w_61=0.71467658, w_62=0.66232046, w_63=0.88830701, w_64=1.5757059, w_65=1.3179867, w_66=1.9115226, w_67=1.6717181, w_68=1.8226795, w_69=1.5805195, w_70=1.3721732, w_71=1.5721771, w_72=1.8917866, w_73=0.66297112, w_74=1.9061478, w_75=0.74827117, w_76=1.3058432, w_77=1.5201802, w_78=0.80806694, w_79=1.2521674, w_80=0.88439382, w_81=1.8155742, w_82=1.1733022, w_83=1.8248157, w_84=0.63899555, w_85=1.6006389, w_86=1.4525186, w_87=0.71194955, w_88=1.1918182, w_89=1.2478937, w_90=1.8201286, w_91=0.686048, w_92=1.2135856, w_93=1.9596536, w_94=1.6447191, w_95=1.8533975, w_96=1.6436227, w_97=1.5808035, w_98=0.91665326, w_99=0.6546546, w_100=0.72077312, w_101=1.235239, w_102=1.4846852, w_103=1.3683462, w_104=0.63524538, w_105=1.9306678, w_106=1.5215886, w_107=1.749976, w_108=0.54376276, w_109=0.76058578, w_110=1.5289717, w_111=1.7385375, w_112=0.85846951, w_113=1.6905493, w_114=1.2420246, w_115=1.8328067, w_116=0.85380687, w_117=0.54864534, w_118=0.51065316, w_119=1.8766552, w_120=0.53612647, w_121=0.93451824, w_122=1.2048642, w_123=1.0082653, w_124=0.81876497, w_125=1.1334668, w_126=0.83980375, w_127=1.7078443, w_128=1.5173082, w_129=1.3381255, w_130=1.8803806, w_131=1.5790261, w_132=1.7701086, w_133=1.1926593, w_134=0.70322336, w_135=1.909053, w_136=1.293749, w_137=1.1252336, w_138=1.1391355, w_139=1.5522115, w_140=0.72735459, w_141=1.6277172, w_142=1.2806278, w_143=1.2624337, w_144=0.68917999, w_145=0.56320833, w_146=0.90145284, w_147=1.125382, w_148=0.73117901, w_149=0.63810211, w_150=1.6766007

## Candidate sets (variables)

- Variable `x_1` corresponds to set `A_1 = {29, 36, 40, 42, 43, 55}`
- Variable `x_2` corresponds to set `A_2 = {2, 4, 18, 28, 43, 57}`
- Variable `x_3` corresponds to set `A_3 = {3, 16, 31, 34, 57, 60}`
- Variable `x_4` corresponds to set `A_4 = {2, 14, 25, 36, 45, 58}`
- Variable `x_5` corresponds to set `A_5 = {10, 13, 15, 26, 38, 47}`
- Variable `x_6` corresponds to set `A_6 = {24, 28, 31, 41, 44, 48}`
- Variable `x_7` corresponds to set `A_7 = {3, 17, 18, 52, 54, 58}`
- Variable `x_8` corresponds to set `A_8 = {13, 14, 24, 42, 44, 51}`
- Variable `x_9` corresponds to set `A_9 = {6, 8, 14, 25, 50, 60}`
- Variable `x_10` corresponds to set `A_10 = {3, 10, 26, 30, 42, 57}`
- Variable `x_11` corresponds to set `A_11 = {8, 26, 32, 42, 48, 52}`
- Variable `x_12` corresponds to set `A_12 = {12, 15, 17, 38, 48, 49}`
- Variable `x_13` corresponds to set `A_13 = {12, 19, 31, 37, 41, 44}`
- Variable `x_14` corresponds to set `A_14 = {22, 31, 49, 51, 55, 57}`
- Variable `x_15` corresponds to set `A_15 = {4, 16, 30, 40, 42, 50}`
- Variable `x_16` corresponds to set `A_16 = {18, 19, 25, 34, 35, 60}`
- Variable `x_17` corresponds to set `A_17 = {14, 15, 19, 30, 38, 46}`
- Variable `x_18` corresponds to set `A_18 = {3, 30, 39, 42, 50, 55}`
- Variable `x_19` corresponds to set `A_19 = {13, 17, 24, 30, 37, 53}`
- Variable `x_20` corresponds to set `A_20 = {10, 17, 33, 38, 40, 59}`
- Variable `x_21` corresponds to set `A_21 = {19, 25, 42, 49, 58, 60}`
- Variable `x_22` corresponds to set `A_22 = {14, 25, 26, 31, 33, 40}`
- Variable `x_23` corresponds to set `A_23 = {5, 7, 17, 19, 23, 24}`
- Variable `x_24` corresponds to set `A_24 = {3, 26, 29, 34, 36, 45}`
- Variable `x_25` corresponds to set `A_25 = {9, 30, 44, 47, 56, 59}`
- Variable `x_26` corresponds to set `A_26 = {4, 6, 15, 25, 51, 60}`
- Variable `x_27` corresponds to set `A_27 = {16, 25, 28, 32, 34, 43}`
- Variable `x_28` corresponds to set `A_28 = {15, 19, 40, 51, 58, 60}`
- Variable `x_29` corresponds to set `A_29 = {8, 13, 21, 31, 44, 54}`
- Variable `x_30` corresponds to set `A_30 = {20, 24, 27, 37, 47, 54}`
- Variable `x_31` corresponds to set `A_31 = {1, 21, 41, 51, 54, 60}`
- Variable `x_32` corresponds to set `A_32 = {11, 14, 20, 39, 53, 55}`
- Variable `x_33` corresponds to set `A_33 = {8, 12, 37, 43, 46, 54}`
- Variable `x_34` corresponds to set `A_34 = {8, 11, 14, 17, 39, 53}`
- Variable `x_35` corresponds to set `A_35 = {6, 8, 16, 20, 37, 45}`
- Variable `x_36` corresponds to set `A_36 = {14, 29, 31, 48, 49, 54}`
- Variable `x_37` corresponds to set `A_37 = {1, 9, 10, 23, 38, 59}`
- Variable `x_38` corresponds to set `A_38 = {9, 16, 20, 25, 34, 49}`
- Variable `x_39` corresponds to set `A_39 = {5, 15, 21, 40, 43, 51}`
- Variable `x_40` corresponds to set `A_40 = {24, 39, 40, 41, 44, 48}`
- Variable `x_41` corresponds to set `A_41 = {7, 9, 10, 24, 45, 47}`
- Variable `x_42` corresponds to set `A_42 = {35, 36, 44, 46, 47, 48}`
- Variable `x_43` corresponds to set `A_43 = {7, 8, 9, 26, 33, 52}`
- Variable `x_44` corresponds to set `A_44 = {9, 16, 31, 41, 55, 60}`
- Variable `x_45` corresponds to set `A_45 = {7, 27, 33, 36, 49, 55}`
- Variable `x_46` corresponds to set `A_46 = {10, 16, 23, 25, 34, 51}`
- Variable `x_47` corresponds to set `A_47 = {16, 18, 31, 52, 55, 59}`
- Variable `x_48` corresponds to set `A_48 = {6, 9, 17, 22, 33, 35}`
- Variable `x_49` corresponds to set `A_49 = {1, 2, 19, 27, 58, 60}`
- Variable `x_50` corresponds to set `A_50 = {21, 31, 36, 41, 49, 59}`
- Variable `x_51` corresponds to set `A_51 = {15, 20, 28, 40, 43, 56}`
- Variable `x_52` corresponds to set `A_52 = {14, 15, 23, 42, 47, 51}`
- Variable `x_53` corresponds to set `A_53 = {12, 13, 15, 24, 46, 51}`
- Variable `x_54` corresponds to set `A_54 = {1, 16, 24, 28, 39, 49}`
- Variable `x_55` corresponds to set `A_55 = {1, 2, 31, 34, 44, 50}`
- Variable `x_56` corresponds to set `A_56 = {1, 7, 8, 13, 16, 60}`
- Variable `x_57` corresponds to set `A_57 = {4, 28, 32, 38, 51, 60}`
- Variable `x_58` corresponds to set `A_58 = {1, 22, 38, 42, 44, 46}`
- Variable `x_59` corresponds to set `A_59 = {13, 16, 27, 33, 37, 59}`
- Variable `x_60` corresponds to set `A_60 = {8, 13, 44, 47, 50, 54}`
- Variable `x_61` corresponds to set `A_61 = {26, 30, 32, 33, 40, 42}`
- Variable `x_62` corresponds to set `A_62 = {17, 19, 28, 36, 50, 58}`
- Variable `x_63` corresponds to set `A_63 = {12, 33, 36, 41, 47, 48}`
- Variable `x_64` corresponds to set `A_64 = {2, 10, 25, 27, 28, 59}`
- Variable `x_65` corresponds to set `A_65 = {5, 7, 12, 45, 52, 53}`
- Variable `x_66` corresponds to set `A_66 = {1, 10, 12, 19, 30, 58}`
- Variable `x_67` corresponds to set `A_67 = {3, 23, 38, 43, 57, 59}`
- Variable `x_68` corresponds to set `A_68 = {6, 43, 45, 47, 48, 55}`
- Variable `x_69` corresponds to set `A_69 = {11, 16, 23, 36, 56, 58}`
- Variable `x_70` corresponds to set `A_70 = {16, 23, 28, 31, 54, 55}`
- Variable `x_71` corresponds to set `A_71 = {4, 8, 17, 19, 45, 54}`
- Variable `x_72` corresponds to set `A_72 = {4, 10, 16, 38, 56, 57}`
- Variable `x_73` corresponds to set `A_73 = {20, 31, 36, 42, 47, 48}`
- Variable `x_74` corresponds to set `A_74 = {8, 10, 17, 19, 41, 59}`
- Variable `x_75` corresponds to set `A_75 = {6, 14, 17, 32, 49, 50}`
- Variable `x_76` corresponds to set `A_76 = {1, 8, 15, 21, 24, 56}`
- Variable `x_77` corresponds to set `A_77 = {1, 28, 31, 33, 50, 59}`
- Variable `x_78` corresponds to set `A_78 = {1, 11, 38, 49, 51, 58}`
- Variable `x_79` corresponds to set `A_79 = {11, 21, 29, 44, 45, 48}`
- Variable `x_80` corresponds to set `A_80 = {13, 14, 20, 49, 54, 59}`
- Variable `x_81` corresponds to set `A_81 = {5, 31, 35, 43, 55, 57}`
- Variable `x_82` corresponds to set `A_82 = {24, 33, 38, 39, 56, 60}`
- Variable `x_83` corresponds to set `A_83 = {20, 28, 31, 40, 44, 54}`
- Variable `x_84` corresponds to set `A_84 = {12, 23, 31, 36, 51, 56}`
- Variable `x_85` corresponds to set `A_85 = {10, 11, 14, 44, 50, 57}`
- Variable `x_86` corresponds to set `A_86 = {5, 9, 34, 35, 36, 58}`
- Variable `x_87` corresponds to set `A_87 = {19, 28, 30, 38, 50, 54}`
- Variable `x_88` corresponds to set `A_88 = {9, 20, 33, 35, 42, 43}`
- Variable `x_89` corresponds to set `A_89 = {15, 24, 27, 39, 54, 59}`
- Variable `x_90` corresponds to set `A_90 = {2, 29, 34, 36, 51, 53}`
- Variable `x_91` corresponds to set `A_91 = {3, 16, 21, 23, 43, 44}`
- Variable `x_92` corresponds to set `A_92 = {9, 10, 45, 57, 59, 60}`
- Variable `x_93` corresponds to set `A_93 = {2, 7, 26, 31, 42, 50}`
- Variable `x_94` corresponds to set `A_94 = {5, 10, 15, 18, 39, 52}`
- Variable `x_95` corresponds to set `A_95 = {26, 32, 39, 43, 48, 54}`
- Variable `x_96` corresponds to set `A_96 = {2, 16, 35, 40, 47, 58}`
- Variable `x_97` corresponds to set `A_97 = {3, 5, 36, 40, 41, 51}`
- Variable `x_98` corresponds to set `A_98 = {5, 11, 22, 27, 29, 56}`
- Variable `x_99` corresponds to set `A_99 = {2, 17, 28, 40, 46, 49}`
- Variable `x_100` corresponds to set `A_100 = {4, 10, 27, 49, 50, 55}`
- Variable `x_101` corresponds to set `A_101 = {11, 24, 39, 50, 52, 54}`
- Variable `x_102` corresponds to set `A_102 = {3, 7, 15, 30, 38, 60}`
- Variable `x_103` corresponds to set `A_103 = {1, 17, 30, 32, 58, 60}`
- Variable `x_104` corresponds to set `A_104 = {16, 24, 33, 43, 50, 58}`
- Variable `x_105` corresponds to set `A_105 = {13, 21, 31, 35, 47, 60}`
- Variable `x_106` corresponds to set `A_106 = {32, 44, 45, 47, 51, 54}`
- Variable `x_107` corresponds to set `A_107 = {7, 9, 31, 33, 53, 55}`
- Variable `x_108` corresponds to set `A_108 = {3, 12, 24, 34, 51, 57}`
- Variable `x_109` corresponds to set `A_109 = {6, 8, 16, 21, 41, 60}`
- Variable `x_110` corresponds to set `A_110 = {16, 23, 28, 37, 53, 58}`
- Variable `x_111` corresponds to set `A_111 = {6, 15, 24, 30, 35, 57}`
- Variable `x_112` corresponds to set `A_112 = {32, 43, 45, 53, 55, 59}`
- Variable `x_113` corresponds to set `A_113 = {34, 41, 43, 44, 55, 58}`
- Variable `x_114` corresponds to set `A_114 = {1, 13, 30, 37, 38, 41}`
- Variable `x_115` corresponds to set `A_115 = {4, 16, 18, 30, 31, 56}`
- Variable `x_116` corresponds to set `A_116 = {2, 17, 28, 30, 48, 59}`
- Variable `x_117` corresponds to set `A_117 = {2, 3, 20, 26, 31, 35}`
- Variable `x_118` corresponds to set `A_118 = {2, 14, 20, 26, 32, 38}`
- Variable `x_119` corresponds to set `A_119 = {10, 12, 14, 19, 27, 52}`
- Variable `x_120` corresponds to set `A_120 = {13, 19, 37, 51, 54, 56}`
- Variable `x_121` corresponds to set `A_121 = {5, 9, 33, 36, 57, 59}`
- Variable `x_122` corresponds to set `A_122 = {4, 16, 21, 40, 51, 57}`
- Variable `x_123` corresponds to set `A_123 = {9, 10, 42, 48, 56, 59}`
- Variable `x_124` corresponds to set `A_124 = {5, 6, 33, 35, 44, 46}`
- Variable `x_125` corresponds to set `A_125 = {10, 11, 26, 27, 54, 57}`
- Variable `x_126` corresponds to set `A_126 = {1, 15, 17, 26, 28, 43}`
- Variable `x_127` corresponds to set `A_127 = {2, 5, 11, 38, 41, 42}`
- Variable `x_128` corresponds to set `A_128 = {29, 30, 32, 40, 45, 60}`
- Variable `x_129` corresponds to set `A_129 = {7, 18, 31, 39, 46, 54}`
- Variable `x_130` corresponds to set `A_130 = {16, 39, 45, 49, 55, 56}`
- Variable `x_131` corresponds to set `A_131 = {19, 25, 36, 43, 46, 60}`
- Variable `x_132` corresponds to set `A_132 = {23, 34, 36, 37, 38, 45}`
- Variable `x_133` corresponds to set `A_133 = {2, 6, 9, 14, 26, 53}`
- Variable `x_134` corresponds to set `A_134 = {5, 9, 19, 31, 38, 49}`
- Variable `x_135` corresponds to set `A_135 = {9, 10, 19, 33, 45, 55}`
- Variable `x_136` corresponds to set `A_136 = {28, 31, 38, 45, 50, 56}`
- Variable `x_137` corresponds to set `A_137 = {6, 26, 43, 46, 56, 60}`
- Variable `x_138` corresponds to set `A_138 = {17, 24, 33, 41, 45, 51}`
- Variable `x_139` corresponds to set `A_139 = {2, 13, 15, 40, 44, 57}`
- Variable `x_140` corresponds to set `A_140 = {2, 6, 31, 41, 46, 51}`
- Variable `x_141` corresponds to set `A_141 = {2, 8, 13, 18, 23, 50}`
- Variable `x_142` corresponds to set `A_142 = {12, 15, 21, 28, 29, 54}`
- Variable `x_143` corresponds to set `A_143 = {5, 14, 18, 42, 48, 54}`
- Variable `x_144` corresponds to set `A_144 = {2, 7, 15, 21, 28, 38}`
- Variable `x_145` corresponds to set `A_145 = {3, 4, 5, 8, 35, 36}`
- Variable `x_146` corresponds to set `A_146 = {4, 20, 22, 34, 49, 59}`
- Variable `x_147` corresponds to set `A_147 = {13, 25, 36, 44, 46, 55}`
- Variable `x_148` corresponds to set `A_148 = {15, 35, 40, 42, 48, 50}`
- Variable `x_149` corresponds to set `A_149 = {5, 8, 16, 44, 52, 53}`
- Variable `x_150` corresponds to set `A_150 = {3, 26, 27, 29, 40, 52}`

## Exact constraints

- Constraint `1`: x_31 + x_37 + x_49 + x_54 + x_55 + x_56 + x_58 + x_66 + x_76 + x_77 + x_78 + x_103 + x_114 + x_126 <= 1
- Constraint `2`: x_2 + x_4 + x_49 + x_55 + x_64 + x_90 + x_93 + x_96 + x_99 + x_116 + x_117 + x_118 + x_127 + x_133 + x_139 + x_140 + x_141 + x_144 <= 1
- Constraint `3`: x_3 + x_7 + x_10 + x_18 + x_24 + x_67 + x_91 + x_97 + x_102 + x_108 + x_117 + x_145 + x_150 <= 1
- Constraint `4`: x_2 + x_15 + x_26 + x_57 + x_71 + x_72 + x_100 + x_115 + x_122 + x_145 + x_146 <= 1
- Constraint `5`: x_23 + x_39 + x_65 + x_81 + x_86 + x_94 + x_97 + x_98 + x_121 + x_124 + x_127 + x_134 + x_143 + x_145 + x_149 <= 1
- Constraint `6`: x_9 + x_26 + x_35 + x_48 + x_68 + x_75 + x_109 + x_111 + x_124 + x_133 + x_137 + x_140 <= 1
- Constraint `7`: x_23 + x_41 + x_43 + x_45 + x_56 + x_65 + x_93 + x_102 + x_107 + x_129 + x_144 <= 1
- Constraint `8`: x_9 + x_11 + x_29 + x_33 + x_34 + x_35 + x_43 + x_56 + x_60 + x_71 + x_74 + x_76 + x_109 + x_141 + x_145 + x_149 <= 1
- Constraint `9`: x_25 + x_37 + x_38 + x_41 + x_43 + x_44 + x_48 + x_86 + x_88 + x_92 + x_107 + x_121 + x_123 + x_133 + x_134 + x_135 <= 1
- Constraint `10`: x_5 + x_10 + x_20 + x_37 + x_41 + x_46 + x_64 + x_66 + x_72 + x_74 + x_85 + x_92 + x_94 + x_100 + x_119 + x_123 + x_125 + x_135 <= 1
- Constraint `11`: x_32 + x_34 + x_69 + x_78 + x_79 + x_85 + x_98 + x_101 + x_125 + x_127 <= 1
- Constraint `12`: x_12 + x_13 + x_33 + x_53 + x_63 + x_65 + x_66 + x_84 + x_108 + x_119 + x_142 <= 1
- Constraint `13`: x_5 + x_8 + x_19 + x_29 + x_53 + x_56 + x_59 + x_60 + x_80 + x_105 + x_114 + x_120 + x_139 + x_141 + x_147 <= 1
- Constraint `14`: x_4 + x_8 + x_9 + x_17 + x_22 + x_32 + x_34 + x_36 + x_52 + x_75 + x_80 + x_85 + x_118 + x_119 + x_133 + x_143 <= 1
- Constraint `15`: x_5 + x_12 + x_17 + x_26 + x_28 + x_39 + x_51 + x_52 + x_53 + x_76 + x_89 + x_94 + x_102 + x_111 + x_126 + x_139 + x_142 + x_144 + x_148 <= 1
- Constraint `16`: x_3 + x_15 + x_27 + x_35 + x_38 + x_44 + x_46 + x_47 + x_54 + x_56 + x_59 + x_69 + x_70 + x_72 + x_91 + x_96 + x_104 + x_109 + x_110 + x_115 + x_122 + x_130 + x_149 <= 1
- Constraint `17`: x_7 + x_12 + x_19 + x_20 + x_23 + x_34 + x_48 + x_62 + x_71 + x_74 + x_75 + x_99 + x_103 + x_116 + x_126 + x_138 <= 1
- Constraint `18`: x_2 + x_7 + x_16 + x_47 + x_94 + x_115 + x_129 + x_141 + x_143 <= 1
- Constraint `19`: x_13 + x_16 + x_17 + x_21 + x_23 + x_28 + x_49 + x_62 + x_66 + x_71 + x_74 + x_87 + x_119 + x_120 + x_131 + x_134 + x_135 <= 1
- Constraint `20`: x_30 + x_32 + x_35 + x_38 + x_51 + x_73 + x_80 + x_83 + x_88 + x_117 + x_118 + x_146 <= 1
- Constraint `21`: x_29 + x_31 + x_39 + x_50 + x_76 + x_79 + x_91 + x_105 + x_109 + x_122 + x_142 + x_144 <= 1
- Constraint `22`: x_14 + x_48 + x_58 + x_98 + x_146 <= 1
- Constraint `23`: x_23 + x_37 + x_46 + x_52 + x_67 + x_69 + x_70 + x_84 + x_91 + x_110 + x_132 + x_141 <= 1
- Constraint `24`: x_6 + x_8 + x_19 + x_23 + x_30 + x_40 + x_41 + x_53 + x_54 + x_76 + x_82 + x_89 + x_101 + x_104 + x_108 + x_111 + x_138 <= 1
- Constraint `25`: x_4 + x_9 + x_16 + x_21 + x_22 + x_26 + x_27 + x_38 + x_46 + x_64 + x_131 + x_147 <= 1
- Constraint `26`: x_5 + x_10 + x_11 + x_22 + x_24 + x_43 + x_61 + x_93 + x_95 + x_117 + x_118 + x_125 + x_126 + x_133 + x_137 + x_150 <= 1
- Constraint `27`: x_30 + x_45 + x_49 + x_59 + x_64 + x_89 + x_98 + x_100 + x_119 + x_125 + x_150 <= 1
- Constraint `28`: x_2 + x_6 + x_27 + x_51 + x_54 + x_57 + x_62 + x_64 + x_70 + x_77 + x_83 + x_87 + x_99 + x_110 + x_116 + x_126 + x_136 + x_142 + x_144 <= 1
- Constraint `29`: x_1 + x_24 + x_36 + x_79 + x_90 + x_98 + x_128 + x_142 + x_150 <= 1
- Constraint `30`: x_10 + x_15 + x_17 + x_18 + x_19 + x_25 + x_61 + x_66 + x_87 + x_102 + x_103 + x_111 + x_114 + x_115 + x_116 + x_128 <= 1
- Constraint `31`: x_3 + x_6 + x_13 + x_14 + x_22 + x_29 + x_36 + x_44 + x_47 + x_50 + x_55 + x_70 + x_73 + x_77 + x_81 + x_83 + x_84 + x_93 + x_105 + x_107 + x_115 + x_117 + x_129 + x_134 + x_136 + x_140 <= 1
- Constraint `32`: x_11 + x_27 + x_57 + x_61 + x_75 + x_95 + x_103 + x_106 + x_112 + x_118 + x_128 <= 1
- Constraint `33`: x_20 + x_22 + x_43 + x_45 + x_48 + x_59 + x_61 + x_63 + x_77 + x_82 + x_88 + x_104 + x_107 + x_121 + x_124 + x_135 + x_138 <= 1
- Constraint `34`: x_3 + x_16 + x_24 + x_27 + x_38 + x_46 + x_55 + x_86 + x_90 + x_108 + x_113 + x_132 + x_146 <= 1
- Constraint `35`: x_16 + x_42 + x_48 + x_81 + x_86 + x_88 + x_96 + x_105 + x_111 + x_117 + x_124 + x_145 + x_148 <= 1
- Constraint `36`: x_1 + x_4 + x_24 + x_42 + x_45 + x_50 + x_62 + x_63 + x_69 + x_73 + x_84 + x_86 + x_90 + x_97 + x_121 + x_131 + x_132 + x_145 + x_147 <= 1
- Constraint `37`: x_13 + x_19 + x_30 + x_33 + x_35 + x_59 + x_110 + x_114 + x_120 + x_132 <= 1
- Constraint `38`: x_5 + x_12 + x_17 + x_20 + x_37 + x_57 + x_58 + x_67 + x_72 + x_78 + x_82 + x_87 + x_102 + x_114 + x_118 + x_127 + x_132 + x_134 + x_136 + x_144 <= 1
- Constraint `39`: x_18 + x_32 + x_34 + x_40 + x_54 + x_82 + x_89 + x_94 + x_95 + x_101 + x_129 + x_130 <= 1
- Constraint `40`: x_1 + x_15 + x_20 + x_22 + x_28 + x_39 + x_40 + x_51 + x_61 + x_83 + x_96 + x_97 + x_99 + x_122 + x_128 + x_139 + x_148 + x_150 <= 1
- Constraint `41`: x_6 + x_13 + x_31 + x_40 + x_44 + x_50 + x_63 + x_74 + x_97 + x_109 + x_113 + x_114 + x_127 + x_138 + x_140 <= 1
- Constraint `42`: x_1 + x_8 + x_10 + x_11 + x_15 + x_18 + x_21 + x_52 + x_58 + x_61 + x_73 + x_88 + x_93 + x_123 + x_127 + x_143 + x_148 <= 1
- Constraint `43`: x_1 + x_2 + x_27 + x_33 + x_39 + x_51 + x_67 + x_68 + x_81 + x_88 + x_91 + x_95 + x_104 + x_112 + x_113 + x_126 + x_131 + x_137 <= 1
- Constraint `44`: x_6 + x_8 + x_13 + x_25 + x_29 + x_40 + x_42 + x_55 + x_58 + x_60 + x_79 + x_83 + x_85 + x_91 + x_106 + x_113 + x_124 + x_139 + x_147 + x_149 <= 1
- Constraint `45`: x_4 + x_24 + x_35 + x_41 + x_65 + x_68 + x_71 + x_79 + x_92 + x_106 + x_112 + x_128 + x_130 + x_132 + x_135 + x_136 + x_138 <= 1
- Constraint `46`: x_17 + x_33 + x_42 + x_53 + x_58 + x_99 + x_124 + x_129 + x_131 + x_137 + x_140 + x_147 <= 1
- Constraint `47`: x_5 + x_25 + x_30 + x_41 + x_42 + x_52 + x_60 + x_63 + x_68 + x_73 + x_96 + x_105 + x_106 <= 1
- Constraint `48`: x_6 + x_11 + x_12 + x_36 + x_40 + x_42 + x_63 + x_68 + x_73 + x_79 + x_95 + x_116 + x_123 + x_143 + x_148 <= 1
- Constraint `49`: x_12 + x_14 + x_21 + x_36 + x_38 + x_45 + x_50 + x_54 + x_75 + x_78 + x_80 + x_99 + x_100 + x_130 + x_134 + x_146 <= 1
- Constraint `50`: x_9 + x_15 + x_18 + x_55 + x_60 + x_62 + x_75 + x_77 + x_85 + x_87 + x_93 + x_100 + x_101 + x_104 + x_136 + x_141 + x_148 <= 1
- Constraint `51`: x_8 + x_14 + x_26 + x_28 + x_31 + x_39 + x_46 + x_52 + x_53 + x_57 + x_78 + x_84 + x_90 + x_97 + x_106 + x_108 + x_120 + x_122 + x_138 + x_140 <= 1
- Constraint `52`: x_7 + x_11 + x_43 + x_47 + x_65 + x_94 + x_101 + x_119 + x_149 + x_150 <= 1
- Constraint `53`: x_19 + x_32 + x_34 + x_65 + x_90 + x_107 + x_110 + x_112 + x_133 + x_149 <= 1
- Constraint `54`: x_7 + x_29 + x_30 + x_31 + x_33 + x_36 + x_60 + x_70 + x_71 + x_80 + x_83 + x_87 + x_89 + x_95 + x_101 + x_106 + x_120 + x_125 + x_129 + x_142 + x_143 <= 1
- Constraint `55`: x_1 + x_14 + x_18 + x_32 + x_44 + x_45 + x_47 + x_68 + x_70 + x_81 + x_100 + x_107 + x_112 + x_113 + x_130 + x_135 + x_147 <= 1
- Constraint `56`: x_25 + x_51 + x_69 + x_72 + x_76 + x_82 + x_84 + x_98 + x_115 + x_120 + x_123 + x_130 + x_136 + x_137 <= 1
- Constraint `57`: x_2 + x_3 + x_10 + x_14 + x_67 + x_72 + x_81 + x_85 + x_92 + x_108 + x_111 + x_121 + x_122 + x_125 + x_139 <= 1
- Constraint `58`: x_4 + x_7 + x_21 + x_28 + x_49 + x_62 + x_66 + x_69 + x_78 + x_86 + x_96 + x_103 + x_104 + x_110 + x_113 <= 1
- Constraint `59`: x_20 + x_25 + x_37 + x_47 + x_50 + x_59 + x_64 + x_67 + x_74 + x_77 + x_80 + x_89 + x_92 + x_112 + x_116 + x_121 + x_123 + x_146 <= 1
- Constraint `60`: x_3 + x_9 + x_16 + x_21 + x_26 + x_28 + x_31 + x_44 + x_49 + x_56 + x_57 + x_82 + x_92 + x_102 + x_103 + x_105 + x_109 + x_128 + x_131 + x_137 <= 1
