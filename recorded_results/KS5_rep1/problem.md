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

w_1=1.8675849, w_2=1.7502732, w_3=1.3988936, w_4=0.79651576, w_5=0.50641436, w_6=1.2433723, w_7=1.116598, w_8=1.4305513, w_9=1.725617, w_10=1.5263671, w_11=1.1223054, w_12=1.7398845, w_13=1.7987377, w_14=1.1969787, w_15=0.82960232, w_16=1.7735721, w_17=1.1641385, w_18=1.6910795, w_19=1.1643062, w_20=0.70673479, w_21=1.5979191, w_22=0.76623577, w_23=1.0914116, w_24=0.90677527, w_25=1.2777857, w_26=1.3877108, w_27=0.92733158, w_28=0.5315285, w_29=0.50733235, w_30=1.2981736, w_31=1.2056698, w_32=0.63789062, w_33=1.0821345, w_34=1.1447937, w_35=1.0228829, w_36=0.63946453, w_37=1.1519884, w_38=0.607731, w_39=1.3745534, w_40=1.8602689, w_41=0.78139966, w_42=0.97979514, w_43=0.92049915, w_44=1.5718322, w_45=1.789544, w_46=1.6109202, w_47=1.9671235, w_48=1.5563397, w_49=1.371127, w_50=1.5101523, w_51=1.3903563, w_52=0.94845981, w_53=1.0448497, w_54=1.3038558, w_55=1.2291789, w_56=1.6509697, w_57=1.1569351, w_58=0.78317625, w_59=0.82147808, w_60=1.5857807, w_61=1.1036216, w_62=1.9085596, w_63=1.9367838, w_64=1.1625986, w_65=1.1185998, w_66=1.0860282, w_67=1.09507, w_68=1.8721921, w_69=0.67949215, w_70=0.96299987, w_71=1.632325, w_72=1.7826834, w_73=0.51013696, w_74=1.0625659, w_75=1.1384844, w_76=1.1677443, w_77=1.6101829, w_78=1.8575377, w_79=0.62763961, w_80=0.85653798, w_81=1.698904, w_82=1.3508011, w_83=0.75362042, w_84=1.9479882, w_85=0.89104231, w_86=1.6904529, w_87=1.1897377, w_88=0.95671244, w_89=1.3780829, w_90=1.5193874, w_91=1.4936991, w_92=1.4578118, w_93=1.2335432, w_94=0.81653117, w_95=0.56450458, w_96=0.6540918, w_97=1.0531733, w_98=0.56835393, w_99=1.8138639, w_100=1.3335315, w_101=1.2961946, w_102=0.50172018, w_103=1.8444272, w_104=0.62194659, w_105=1.5856478, w_106=1.2356615, w_107=1.066825, w_108=1.6504976, w_109=0.71167519, w_110=1.273467, w_111=0.53316767, w_112=1.364207, w_113=1.6968369, w_114=1.0197111, w_115=1.5651457, w_116=0.529246, w_117=0.77527187, w_118=0.57323571, w_119=0.81959406, w_120=0.95802409, w_121=1.0881921, w_122=1.5103127, w_123=1.5373551, w_124=1.7743972, w_125=0.92173631, w_126=0.91534659, w_127=0.80660325, w_128=1.1948892, w_129=0.8048719, w_130=0.7687323, w_131=0.76960441, w_132=1.9009609, w_133=1.0658973, w_134=1.2734782, w_135=0.84535515, w_136=1.6370078, w_137=1.6651736, w_138=1.4830615, w_139=1.4956986, w_140=1.8701065, w_141=1.9703924, w_142=1.6133247, w_143=1.9109557, w_144=0.75150314, w_145=1.5904093, w_146=1.0059475, w_147=0.76859766, w_148=0.74821245, w_149=0.72357127, w_150=0.91553876

## Candidate sets (variables)

- Variable `x_1` corresponds to set `A_1 = {3, 27, 30, 41, 42, 52}`
- Variable `x_2` corresponds to set `A_2 = {30, 40, 43, 49, 53, 54}`
- Variable `x_3` corresponds to set `A_3 = {6, 13, 17, 26, 34, 47}`
- Variable `x_4` corresponds to set `A_4 = {8, 11, 14, 28, 52, 58}`
- Variable `x_5` corresponds to set `A_5 = {2, 44, 52, 56, 59, 60}`
- Variable `x_6` corresponds to set `A_6 = {13, 32, 36, 46, 51, 55}`
- Variable `x_7` corresponds to set `A_7 = {2, 14, 26, 30, 45, 46}`
- Variable `x_8` corresponds to set `A_8 = {6, 13, 18, 26, 37, 43}`
- Variable `x_9` corresponds to set `A_9 = {8, 36, 40, 56, 57, 58}`
- Variable `x_10` corresponds to set `A_10 = {14, 15, 35, 36, 45, 56}`
- Variable `x_11` corresponds to set `A_11 = {1, 3, 4, 14, 56, 60}`
- Variable `x_12` corresponds to set `A_12 = {10, 13, 18, 43, 45, 48}`
- Variable `x_13` corresponds to set `A_13 = {5, 9, 14, 23, 34, 55}`
- Variable `x_14` corresponds to set `A_14 = {10, 18, 20, 27, 53, 60}`
- Variable `x_15` corresponds to set `A_15 = {5, 15, 25, 32, 34, 51}`
- Variable `x_16` corresponds to set `A_16 = {16, 20, 29, 30, 32, 47}`
- Variable `x_17` corresponds to set `A_17 = {8, 21, 24, 27, 30, 56}`
- Variable `x_18` corresponds to set `A_18 = {4, 7, 9, 25, 29, 56}`
- Variable `x_19` corresponds to set `A_19 = {29, 38, 45, 47, 52, 55}`
- Variable `x_20` corresponds to set `A_20 = {3, 13, 28, 29, 31, 36}`
- Variable `x_21` corresponds to set `A_21 = {5, 12, 27, 29, 30, 41}`
- Variable `x_22` corresponds to set `A_22 = {4, 7, 11, 33, 41, 58}`
- Variable `x_23` corresponds to set `A_23 = {19, 29, 32, 51, 55, 57}`
- Variable `x_24` corresponds to set `A_24 = {15, 16, 23, 45, 50, 55}`
- Variable `x_25` corresponds to set `A_25 = {12, 18, 24, 33, 42, 59}`
- Variable `x_26` corresponds to set `A_26 = {5, 17, 22, 35, 39, 58}`
- Variable `x_27` corresponds to set `A_27 = {8, 10, 18, 22, 43, 53}`
- Variable `x_28` corresponds to set `A_28 = {9, 12, 15, 20, 31, 35}`
- Variable `x_29` corresponds to set `A_29 = {1, 4, 24, 27, 28, 45}`
- Variable `x_30` corresponds to set `A_30 = {5, 8, 20, 23, 24, 38}`
- Variable `x_31` corresponds to set `A_31 = {4, 20, 29, 32, 48, 51}`
- Variable `x_32` corresponds to set `A_32 = {13, 35, 50, 53, 57, 59}`
- Variable `x_33` corresponds to set `A_33 = {1, 3, 32, 45, 49, 50}`
- Variable `x_34` corresponds to set `A_34 = {5, 9, 32, 40, 45, 55}`
- Variable `x_35` corresponds to set `A_35 = {24, 30, 34, 51, 58, 59}`
- Variable `x_36` corresponds to set `A_36 = {10, 15, 23, 37, 53, 56}`
- Variable `x_37` corresponds to set `A_37 = {11, 19, 27, 30, 36, 37}`
- Variable `x_38` corresponds to set `A_38 = {4, 19, 26, 30, 40, 49}`
- Variable `x_39` corresponds to set `A_39 = {5, 6, 15, 43, 52, 59}`
- Variable `x_40` corresponds to set `A_40 = {16, 19, 25, 37, 43, 48}`
- Variable `x_41` corresponds to set `A_41 = {2, 6, 11, 12, 50, 51}`
- Variable `x_42` corresponds to set `A_42 = {17, 21, 22, 43, 53, 58}`
- Variable `x_43` corresponds to set `A_43 = {13, 21, 23, 25, 36, 40}`
- Variable `x_44` corresponds to set `A_44 = {3, 17, 25, 34, 47, 55}`
- Variable `x_45` corresponds to set `A_45 = {7, 10, 13, 16, 30, 58}`
- Variable `x_46` corresponds to set `A_46 = {4, 15, 35, 41, 42, 47}`
- Variable `x_47` corresponds to set `A_47 = {6, 13, 39, 52, 53, 60}`
- Variable `x_48` corresponds to set `A_48 = {13, 14, 33, 40, 45, 53}`
- Variable `x_49` corresponds to set `A_49 = {6, 31, 34, 39, 45, 47}`
- Variable `x_50` corresponds to set `A_50 = {3, 20, 25, 31, 44, 48}`
- Variable `x_51` corresponds to set `A_51 = {3, 13, 29, 30, 45, 55}`
- Variable `x_52` corresponds to set `A_52 = {2, 13, 26, 44, 48, 58}`
- Variable `x_53` corresponds to set `A_53 = {6, 9, 22, 42, 46, 53}`
- Variable `x_54` corresponds to set `A_54 = {15, 18, 23, 39, 41, 57}`
- Variable `x_55` corresponds to set `A_55 = {5, 16, 18, 19, 43, 52}`
- Variable `x_56` corresponds to set `A_56 = {2, 13, 18, 20, 23, 45}`
- Variable `x_57` corresponds to set `A_57 = {23, 42, 44, 51, 53, 54}`
- Variable `x_58` corresponds to set `A_58 = {9, 19, 31, 32, 36, 59}`
- Variable `x_59` corresponds to set `A_59 = {3, 9, 19, 35, 45, 48}`
- Variable `x_60` corresponds to set `A_60 = {8, 17, 18, 51, 53, 55}`
- Variable `x_61` corresponds to set `A_61 = {7, 8, 22, 27, 35, 41}`
- Variable `x_62` corresponds to set `A_62 = {10, 14, 25, 35, 44, 51}`
- Variable `x_63` corresponds to set `A_63 = {8, 17, 34, 50, 58, 60}`
- Variable `x_64` corresponds to set `A_64 = {17, 30, 32, 40, 41, 42}`
- Variable `x_65` corresponds to set `A_65 = {5, 27, 42, 46, 50, 56}`
- Variable `x_66` corresponds to set `A_66 = {13, 15, 33, 43, 47, 58}`
- Variable `x_67` corresponds to set `A_67 = {20, 21, 35, 37, 54, 55}`
- Variable `x_68` corresponds to set `A_68 = {13, 15, 32, 42, 47, 52}`
- Variable `x_69` corresponds to set `A_69 = {3, 27, 30, 33, 39, 44}`
- Variable `x_70` corresponds to set `A_70 = {8, 14, 22, 25, 32, 33}`
- Variable `x_71` corresponds to set `A_71 = {8, 15, 23, 43, 52, 56}`
- Variable `x_72` corresponds to set `A_72 = {7, 17, 44, 49, 52, 57}`
- Variable `x_73` corresponds to set `A_73 = {1, 3, 9, 22, 28, 51}`
- Variable `x_74` corresponds to set `A_74 = {1, 8, 9, 12, 19, 50}`
- Variable `x_75` corresponds to set `A_75 = {6, 13, 24, 35, 52, 60}`
- Variable `x_76` corresponds to set `A_76 = {16, 27, 31, 47, 53, 59}`
- Variable `x_77` corresponds to set `A_77 = {6, 10, 17, 34, 44, 48}`
- Variable `x_78` corresponds to set `A_78 = {4, 8, 24, 38, 44, 59}`
- Variable `x_79` corresponds to set `A_79 = {10, 28, 35, 38, 46, 59}`
- Variable `x_80` corresponds to set `A_80 = {7, 28, 33, 45, 52, 57}`
- Variable `x_81` corresponds to set `A_81 = {15, 20, 23, 31, 49, 50}`
- Variable `x_82` corresponds to set `A_82 = {2, 7, 21, 22, 42, 55}`
- Variable `x_83` corresponds to set `A_83 = {21, 22, 39, 49, 52, 53}`
- Variable `x_84` corresponds to set `A_84 = {4, 6, 22, 32, 42, 59}`
- Variable `x_85` corresponds to set `A_85 = {4, 7, 24, 38, 40, 41}`
- Variable `x_86` corresponds to set `A_86 = {25, 26, 40, 42, 54, 59}`
- Variable `x_87` corresponds to set `A_87 = {21, 31, 32, 36, 42, 58}`
- Variable `x_88` corresponds to set `A_88 = {9, 15, 18, 39, 42, 54}`
- Variable `x_89` corresponds to set `A_89 = {5, 12, 32, 38, 44, 46}`
- Variable `x_90` corresponds to set `A_90 = {8, 10, 11, 29, 38, 56}`
- Variable `x_91` corresponds to set `A_91 = {8, 23, 25, 35, 36, 53}`
- Variable `x_92` corresponds to set `A_92 = {12, 18, 25, 38, 42, 58}`
- Variable `x_93` corresponds to set `A_93 = {12, 34, 36, 39, 40, 55}`
- Variable `x_94` corresponds to set `A_94 = {7, 19, 21, 29, 51, 53}`
- Variable `x_95` corresponds to set `A_95 = {4, 6, 7, 10, 32, 60}`
- Variable `x_96` corresponds to set `A_96 = {2, 5, 13, 24, 32, 45}`
- Variable `x_97` corresponds to set `A_97 = {5, 7, 23, 25, 32, 36}`
- Variable `x_98` corresponds to set `A_98 = {7, 8, 14, 19, 33, 51}`
- Variable `x_99` corresponds to set `A_99 = {22, 28, 32, 35, 52, 59}`
- Variable `x_100` corresponds to set `A_100 = {3, 7, 11, 13, 29, 57}`
- Variable `x_101` corresponds to set `A_101 = {2, 3, 13, 14, 19, 31}`
- Variable `x_102` corresponds to set `A_102 = {6, 28, 29, 46, 52, 54}`
- Variable `x_103` corresponds to set `A_103 = {6, 20, 30, 40, 51, 55}`
- Variable `x_104` corresponds to set `A_104 = {4, 18, 21, 32, 37, 44}`
- Variable `x_105` corresponds to set `A_105 = {8, 13, 22, 42, 52, 53}`
- Variable `x_106` corresponds to set `A_106 = {3, 17, 21, 45, 52, 53}`
- Variable `x_107` corresponds to set `A_107 = {17, 21, 25, 33, 46, 47}`
- Variable `x_108` corresponds to set `A_108 = {2, 5, 13, 33, 38, 59}`
- Variable `x_109` corresponds to set `A_109 = {8, 19, 24, 26, 48, 57}`
- Variable `x_110` corresponds to set `A_110 = {2, 13, 29, 33, 37, 50}`
- Variable `x_111` corresponds to set `A_111 = {4, 8, 21, 22, 35, 52}`
- Variable `x_112` corresponds to set `A_112 = {13, 14, 21, 33, 46, 47}`
- Variable `x_113` corresponds to set `A_113 = {1, 34, 39, 51, 53, 58}`
- Variable `x_114` corresponds to set `A_114 = {10, 26, 47, 50, 53, 55}`
- Variable `x_115` corresponds to set `A_115 = {2, 13, 30, 39, 44, 50}`
- Variable `x_116` corresponds to set `A_116 = {5, 7, 9, 15, 23, 34}`
- Variable `x_117` corresponds to set `A_117 = {7, 13, 32, 33, 44, 47}`
- Variable `x_118` corresponds to set `A_118 = {7, 17, 23, 43, 54, 59}`
- Variable `x_119` corresponds to set `A_119 = {16, 21, 27, 30, 33, 54}`
- Variable `x_120` corresponds to set `A_120 = {9, 32, 44, 48, 54, 55}`
- Variable `x_121` corresponds to set `A_121 = {4, 9, 11, 27, 36, 52}`
- Variable `x_122` corresponds to set `A_122 = {12, 18, 24, 35, 47, 57}`
- Variable `x_123` corresponds to set `A_123 = {6, 9, 19, 35, 56, 57}`
- Variable `x_124` corresponds to set `A_124 = {9, 12, 16, 35, 42, 60}`
- Variable `x_125` corresponds to set `A_125 = {1, 15, 20, 38, 44, 54}`
- Variable `x_126` corresponds to set `A_126 = {25, 28, 30, 34, 45, 60}`
- Variable `x_127` corresponds to set `A_127 = {9, 19, 33, 40, 52, 59}`
- Variable `x_128` corresponds to set `A_128 = {18, 21, 31, 34, 36, 50}`
- Variable `x_129` corresponds to set `A_129 = {7, 18, 28, 43, 46, 60}`
- Variable `x_130` corresponds to set `A_130 = {21, 29, 31, 33, 39, 58}`
- Variable `x_131` corresponds to set `A_131 = {14, 20, 29, 36, 39, 60}`
- Variable `x_132` corresponds to set `A_132 = {7, 11, 19, 22, 35, 49}`
- Variable `x_133` corresponds to set `A_133 = {11, 20, 22, 28, 46, 59}`
- Variable `x_134` corresponds to set `A_134 = {9, 25, 35, 45, 46, 48}`
- Variable `x_135` corresponds to set `A_135 = {1, 6, 26, 31, 42, 57}`
- Variable `x_136` corresponds to set `A_136 = {8, 14, 24, 25, 35, 39}`
- Variable `x_137` corresponds to set `A_137 = {1, 39, 40, 43, 44, 46}`
- Variable `x_138` corresponds to set `A_138 = {3, 8, 29, 44, 49, 60}`
- Variable `x_139` corresponds to set `A_139 = {28, 30, 35, 42, 46, 58}`
- Variable `x_140` corresponds to set `A_140 = {3, 17, 20, 35, 48, 52}`
- Variable `x_141` corresponds to set `A_141 = {23, 29, 49, 53, 55, 59}`
- Variable `x_142` corresponds to set `A_142 = {2, 8, 14, 37, 42, 51}`
- Variable `x_143` corresponds to set `A_143 = {8, 19, 20, 23, 43, 45}`
- Variable `x_144` corresponds to set `A_144 = {2, 4, 34, 37, 38, 60}`
- Variable `x_145` corresponds to set `A_145 = {19, 30, 36, 38, 56, 60}`
- Variable `x_146` corresponds to set `A_146 = {1, 2, 14, 38, 44, 56}`
- Variable `x_147` corresponds to set `A_147 = {7, 20, 24, 35, 38, 49}`
- Variable `x_148` corresponds to set `A_148 = {16, 20, 23, 24, 25, 29}`
- Variable `x_149` corresponds to set `A_149 = {5, 16, 30, 37, 53, 54}`
- Variable `x_150` corresponds to set `A_150 = {11, 17, 25, 39, 46, 47}`

## Exact constraints

- Constraint `1`: x_11 + x_29 + x_33 + x_73 + x_74 + x_113 + x_125 + x_135 + x_137 + x_146 <= 1
- Constraint `2`: x_5 + x_7 + x_41 + x_52 + x_56 + x_82 + x_96 + x_101 + x_108 + x_110 + x_115 + x_142 + x_144 + x_146 <= 1
- Constraint `3`: x_1 + x_11 + x_20 + x_33 + x_44 + x_50 + x_51 + x_59 + x_69 + x_73 + x_100 + x_101 + x_106 + x_138 + x_140 <= 1
- Constraint `4`: x_11 + x_18 + x_22 + x_29 + x_31 + x_38 + x_46 + x_78 + x_84 + x_85 + x_95 + x_104 + x_111 + x_121 + x_144 <= 1
- Constraint `5`: x_13 + x_15 + x_21 + x_26 + x_30 + x_34 + x_39 + x_55 + x_65 + x_89 + x_96 + x_97 + x_108 + x_116 + x_149 <= 1
- Constraint `6`: x_3 + x_8 + x_39 + x_41 + x_47 + x_49 + x_53 + x_75 + x_77 + x_84 + x_95 + x_102 + x_103 + x_123 + x_135 <= 1
- Constraint `7`: x_18 + x_22 + x_45 + x_61 + x_72 + x_80 + x_82 + x_85 + x_94 + x_95 + x_97 + x_98 + x_100 + x_116 + x_117 + x_118 + x_129 + x_132 + x_147 <= 1
- Constraint `8`: x_4 + x_9 + x_17 + x_27 + x_30 + x_60 + x_61 + x_63 + x_70 + x_71 + x_74 + x_78 + x_90 + x_91 + x_98 + x_105 + x_109 + x_111 + x_136 + x_138 + x_142 + x_143 <= 1
- Constraint `9`: x_13 + x_18 + x_28 + x_34 + x_53 + x_58 + x_59 + x_73 + x_74 + x_88 + x_116 + x_120 + x_121 + x_123 + x_124 + x_127 + x_134 <= 1
- Constraint `10`: x_12 + x_14 + x_27 + x_36 + x_45 + x_62 + x_77 + x_79 + x_90 + x_95 + x_114 <= 1
- Constraint `11`: x_4 + x_22 + x_37 + x_41 + x_90 + x_100 + x_121 + x_132 + x_133 + x_150 <= 1
- Constraint `12`: x_21 + x_25 + x_28 + x_41 + x_74 + x_89 + x_92 + x_93 + x_122 + x_124 <= 1
- Constraint `13`: x_3 + x_6 + x_8 + x_12 + x_20 + x_32 + x_43 + x_45 + x_47 + x_48 + x_51 + x_52 + x_56 + x_66 + x_68 + x_75 + x_96 + x_100 + x_101 + x_105 + x_108 + x_110 + x_112 + x_115 + x_117 <= 1
- Constraint `14`: x_4 + x_7 + x_10 + x_11 + x_13 + x_48 + x_62 + x_70 + x_98 + x_101 + x_112 + x_131 + x_136 + x_142 + x_146 <= 1
- Constraint `15`: x_10 + x_15 + x_24 + x_28 + x_36 + x_39 + x_46 + x_54 + x_66 + x_68 + x_71 + x_81 + x_88 + x_116 + x_125 <= 1
- Constraint `16`: x_16 + x_24 + x_40 + x_45 + x_55 + x_76 + x_119 + x_124 + x_148 + x_149 <= 1
- Constraint `17`: x_3 + x_26 + x_42 + x_44 + x_60 + x_63 + x_64 + x_72 + x_77 + x_106 + x_107 + x_118 + x_140 + x_150 <= 1
- Constraint `18`: x_8 + x_12 + x_14 + x_25 + x_27 + x_54 + x_55 + x_56 + x_60 + x_88 + x_92 + x_104 + x_122 + x_128 + x_129 <= 1
- Constraint `19`: x_23 + x_37 + x_38 + x_40 + x_55 + x_58 + x_59 + x_74 + x_94 + x_98 + x_101 + x_109 + x_123 + x_127 + x_132 + x_143 + x_145 <= 1
- Constraint `20`: x_14 + x_16 + x_28 + x_30 + x_31 + x_50 + x_56 + x_67 + x_81 + x_103 + x_125 + x_131 + x_133 + x_140 + x_143 + x_147 + x_148 <= 1
- Constraint `21`: x_17 + x_42 + x_43 + x_67 + x_82 + x_83 + x_87 + x_94 + x_104 + x_106 + x_107 + x_111 + x_112 + x_119 + x_128 + x_130 <= 1
- Constraint `22`: x_26 + x_27 + x_42 + x_53 + x_61 + x_70 + x_73 + x_82 + x_83 + x_84 + x_99 + x_105 + x_111 + x_132 + x_133 <= 1
- Constraint `23`: x_13 + x_24 + x_30 + x_36 + x_43 + x_54 + x_56 + x_57 + x_71 + x_81 + x_91 + x_97 + x_116 + x_118 + x_141 + x_143 + x_148 <= 1
- Constraint `24`: x_17 + x_25 + x_29 + x_30 + x_35 + x_75 + x_78 + x_85 + x_96 + x_109 + x_122 + x_136 + x_147 + x_148 <= 1
- Constraint `25`: x_15 + x_18 + x_40 + x_43 + x_44 + x_50 + x_62 + x_70 + x_86 + x_91 + x_92 + x_97 + x_107 + x_126 + x_134 + x_136 + x_148 + x_150 <= 1
- Constraint `26`: x_3 + x_7 + x_8 + x_38 + x_52 + x_86 + x_109 + x_114 + x_135 <= 1
- Constraint `27`: x_1 + x_14 + x_17 + x_21 + x_29 + x_37 + x_61 + x_65 + x_69 + x_76 + x_119 + x_121 <= 1
- Constraint `28`: x_4 + x_20 + x_29 + x_73 + x_79 + x_80 + x_99 + x_102 + x_126 + x_129 + x_133 + x_139 <= 1
- Constraint `29`: x_16 + x_18 + x_19 + x_20 + x_21 + x_23 + x_31 + x_51 + x_90 + x_94 + x_100 + x_102 + x_110 + x_130 + x_131 + x_138 + x_141 + x_148 <= 1
- Constraint `30`: x_1 + x_2 + x_7 + x_16 + x_17 + x_21 + x_35 + x_37 + x_38 + x_45 + x_51 + x_64 + x_69 + x_103 + x_115 + x_119 + x_126 + x_139 + x_145 + x_149 <= 1
- Constraint `31`: x_20 + x_28 + x_49 + x_50 + x_58 + x_76 + x_81 + x_87 + x_101 + x_128 + x_130 + x_135 <= 1
- Constraint `32`: x_6 + x_15 + x_16 + x_23 + x_31 + x_33 + x_34 + x_58 + x_64 + x_68 + x_70 + x_84 + x_87 + x_89 + x_95 + x_96 + x_97 + x_99 + x_104 + x_117 + x_120 <= 1
- Constraint `33`: x_22 + x_25 + x_48 + x_66 + x_69 + x_70 + x_80 + x_98 + x_107 + x_108 + x_110 + x_112 + x_117 + x_119 + x_127 + x_130 <= 1
- Constraint `34`: x_3 + x_13 + x_15 + x_35 + x_44 + x_49 + x_63 + x_77 + x_93 + x_113 + x_116 + x_126 + x_128 + x_144 <= 1
- Constraint `35`: x_10 + x_26 + x_28 + x_32 + x_46 + x_59 + x_61 + x_62 + x_67 + x_75 + x_79 + x_91 + x_99 + x_111 + x_122 + x_123 + x_124 + x_132 + x_134 + x_136 + x_139 + x_140 + x_147 <= 1
- Constraint `36`: x_6 + x_9 + x_10 + x_20 + x_37 + x_43 + x_58 + x_87 + x_91 + x_93 + x_97 + x_121 + x_128 + x_131 + x_145 <= 1
- Constraint `37`: x_8 + x_36 + x_37 + x_40 + x_67 + x_104 + x_110 + x_142 + x_144 + x_149 <= 1
- Constraint `38`: x_19 + x_30 + x_78 + x_79 + x_85 + x_89 + x_90 + x_92 + x_108 + x_125 + x_144 + x_145 + x_146 + x_147 <= 1
- Constraint `39`: x_26 + x_47 + x_49 + x_54 + x_69 + x_83 + x_88 + x_93 + x_113 + x_115 + x_130 + x_131 + x_136 + x_137 + x_150 <= 1
- Constraint `40`: x_2 + x_9 + x_34 + x_38 + x_43 + x_48 + x_64 + x_85 + x_86 + x_93 + x_103 + x_127 + x_137 <= 1
- Constraint `41`: x_1 + x_21 + x_22 + x_46 + x_54 + x_61 + x_64 + x_85 <= 1
- Constraint `42`: x_1 + x_25 + x_46 + x_53 + x_57 + x_64 + x_65 + x_68 + x_82 + x_84 + x_86 + x_87 + x_88 + x_92 + x_105 + x_124 + x_135 + x_139 + x_142 <= 1
- Constraint `43`: x_2 + x_8 + x_12 + x_27 + x_39 + x_40 + x_42 + x_55 + x_66 + x_71 + x_118 + x_129 + x_137 + x_143 <= 1
- Constraint `44`: x_5 + x_50 + x_52 + x_57 + x_62 + x_69 + x_72 + x_77 + x_78 + x_89 + x_104 + x_115 + x_117 + x_120 + x_125 + x_137 + x_138 + x_146 <= 1
- Constraint `45`: x_7 + x_10 + x_12 + x_19 + x_24 + x_29 + x_33 + x_34 + x_48 + x_49 + x_51 + x_56 + x_59 + x_80 + x_96 + x_106 + x_126 + x_134 + x_143 <= 1
- Constraint `46`: x_6 + x_7 + x_53 + x_65 + x_79 + x_89 + x_102 + x_107 + x_112 + x_129 + x_133 + x_134 + x_137 + x_139 + x_150 <= 1
- Constraint `47`: x_3 + x_16 + x_19 + x_44 + x_46 + x_49 + x_66 + x_68 + x_76 + x_107 + x_112 + x_114 + x_117 + x_122 + x_150 <= 1
- Constraint `48`: x_12 + x_31 + x_40 + x_50 + x_52 + x_59 + x_77 + x_109 + x_120 + x_134 + x_140 <= 1
- Constraint `49`: x_2 + x_33 + x_38 + x_72 + x_81 + x_83 + x_132 + x_138 + x_141 + x_147 <= 1
- Constraint `50`: x_24 + x_32 + x_33 + x_41 + x_63 + x_65 + x_74 + x_81 + x_110 + x_114 + x_115 + x_128 <= 1
- Constraint `51`: x_6 + x_15 + x_23 + x_31 + x_35 + x_41 + x_57 + x_60 + x_62 + x_73 + x_94 + x_98 + x_103 + x_113 + x_142 <= 1
- Constraint `52`: x_1 + x_4 + x_5 + x_19 + x_39 + x_47 + x_55 + x_68 + x_71 + x_72 + x_75 + x_80 + x_83 + x_99 + x_102 + x_105 + x_106 + x_111 + x_121 + x_127 + x_140 <= 1
- Constraint `53`: x_2 + x_14 + x_27 + x_32 + x_36 + x_42 + x_47 + x_48 + x_53 + x_57 + x_60 + x_76 + x_83 + x_91 + x_94 + x_105 + x_106 + x_113 + x_114 + x_141 + x_149 <= 1
- Constraint `54`: x_2 + x_57 + x_67 + x_86 + x_88 + x_102 + x_118 + x_119 + x_120 + x_125 + x_149 <= 1
- Constraint `55`: x_6 + x_13 + x_19 + x_23 + x_24 + x_34 + x_44 + x_51 + x_60 + x_67 + x_82 + x_93 + x_103 + x_114 + x_120 + x_141 <= 1
- Constraint `56`: x_5 + x_9 + x_10 + x_11 + x_17 + x_18 + x_36 + x_65 + x_71 + x_90 + x_123 + x_145 + x_146 <= 1
- Constraint `57`: x_9 + x_23 + x_32 + x_54 + x_72 + x_80 + x_100 + x_109 + x_122 + x_123 + x_135 <= 1
- Constraint `58`: x_4 + x_9 + x_22 + x_26 + x_35 + x_42 + x_45 + x_52 + x_63 + x_66 + x_87 + x_92 + x_113 + x_130 + x_139 <= 1
- Constraint `59`: x_5 + x_25 + x_32 + x_35 + x_39 + x_58 + x_76 + x_78 + x_79 + x_84 + x_86 + x_99 + x_108 + x_118 + x_127 + x_133 + x_141 <= 1
- Constraint `60`: x_5 + x_11 + x_14 + x_47 + x_63 + x_75 + x_95 + x_124 + x_126 + x_129 + x_131 + x_138 + x_144 + x_145 <= 1
