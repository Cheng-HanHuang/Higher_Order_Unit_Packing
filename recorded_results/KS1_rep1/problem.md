# Original problem: kset_u30_n60_k4

This file records the exact original binary packing problem used for the matching run result.

## Optimization model

\[
\max_{x\in\{0,1\}^n}\ \sum_{i=1}^n w_i x_i
\qquad\text{s.t.}\qquad
\sum_{i\in S_k} x_i \le B_k,\quad k=1,\dots,m.
\]

- Number of variables: `60`
- Number of constraints: `30`
- Matching run-result file: `result.json`

## Metadata

- `generator`: `random_k_set_packing`
- `universe_size`: `30`
- `k`: `4`
- `density`: `1.0`

## Weights

w_1=1.990394, w_2=1.146683, w_3=1.2232783, w_4=1.0424389, w_5=1.6195255, w_6=0.64257539, w_7=1.351097, w_8=1.1264322, w_9=1.0563843, w_10=1.6009585, w_11=1.5214997, w_12=1.4867241, w_13=1.5462168, w_14=1.9704061, w_15=1.1657548, w_16=1.9935403, w_17=1.6022013, w_18=1.3660221, w_19=1.9144406, w_20=0.98642259, w_21=1.4299057, w_22=1.5981634, w_23=0.56771679, w_24=1.709499, w_25=1.1371816, w_26=1.512724, w_27=1.1750491, w_28=1.2213369, w_29=0.9294852, w_30=1.7631222, w_31=1.717901, w_32=1.2443709, w_33=1.808373, w_34=0.96735892, w_35=1.4250597, w_36=1.7153183, w_37=0.96744097, w_38=0.8010732, w_39=1.5583544, w_40=1.8999313, w_41=1.2012182, w_42=1.523288, w_43=0.91179159, w_44=1.5735568, w_45=1.7091813, w_46=1.7433106, w_47=1.1764123, w_48=1.518252, w_49=1.8317328, w_50=1.7671299, w_51=0.72968348, w_52=1.2427832, w_53=1.3051673, w_54=1.8011461, w_55=0.98832563, w_56=0.5025728, w_57=0.67758978, w_58=1.9256639, w_59=0.6125871, w_60=1.9035238

## Candidate sets (variables)

- Variable `x_1` corresponds to set `A_1 = {3, 7, 14, 24}`
- Variable `x_2` corresponds to set `A_2 = {8, 22, 23, 24}`
- Variable `x_3` corresponds to set `A_3 = {8, 19, 22, 24}`
- Variable `x_4` corresponds to set `A_4 = {5, 7, 12, 17}`
- Variable `x_5` corresponds to set `A_5 = {5, 6, 10, 22}`
- Variable `x_6` corresponds to set `A_6 = {3, 13, 16, 18}`
- Variable `x_7` corresponds to set `A_7 = {5, 9, 15, 26}`
- Variable `x_8` corresponds to set `A_8 = {1, 12, 17, 23}`
- Variable `x_9` corresponds to set `A_9 = {6, 10, 17, 25}`
- Variable `x_10` corresponds to set `A_10 = {6, 14, 20, 21}`
- Variable `x_11` corresponds to set `A_11 = {4, 5, 9, 12}`
- Variable `x_12` corresponds to set `A_12 = {2, 9, 17, 27}`
- Variable `x_13` corresponds to set `A_13 = {4, 5, 11, 21}`
- Variable `x_14` corresponds to set `A_14 = {11, 21, 22, 29}`
- Variable `x_15` corresponds to set `A_15 = {9, 15, 25, 28}`
- Variable `x_16` corresponds to set `A_16 = {12, 23, 24, 27}`
- Variable `x_17` corresponds to set `A_17 = {5, 16, 21, 22}`
- Variable `x_18` corresponds to set `A_18 = {10, 11, 23, 26}`
- Variable `x_19` corresponds to set `A_19 = {5, 8, 13, 14}`
- Variable `x_20` corresponds to set `A_20 = {5, 20, 23, 28}`
- Variable `x_21` corresponds to set `A_21 = {10, 16, 23, 25}`
- Variable `x_22` corresponds to set `A_22 = {1, 8, 10, 26}`
- Variable `x_23` corresponds to set `A_23 = {11, 16, 19, 20}`
- Variable `x_24` corresponds to set `A_24 = {1, 6, 17, 26}`
- Variable `x_25` corresponds to set `A_25 = {5, 13, 19, 21}`
- Variable `x_26` corresponds to set `A_26 = {12, 18, 21, 27}`
- Variable `x_27` corresponds to set `A_27 = {2, 15, 26, 28}`
- Variable `x_28` corresponds to set `A_28 = {3, 5, 15, 25}`
- Variable `x_29` corresponds to set `A_29 = {11, 15, 27, 28}`
- Variable `x_30` corresponds to set `A_30 = {5, 12, 14, 15}`
- Variable `x_31` corresponds to set `A_31 = {10, 12, 13, 21}`
- Variable `x_32` corresponds to set `A_32 = {4, 10, 12, 28}`
- Variable `x_33` corresponds to set `A_33 = {8, 12, 14, 17}`
- Variable `x_34` corresponds to set `A_34 = {1, 14, 24, 25}`
- Variable `x_35` corresponds to set `A_35 = {9, 23, 26, 28}`
- Variable `x_36` corresponds to set `A_36 = {10, 20, 23, 24}`
- Variable `x_37` corresponds to set `A_37 = {1, 8, 11, 27}`
- Variable `x_38` corresponds to set `A_38 = {3, 6, 10, 24}`
- Variable `x_39` corresponds to set `A_39 = {6, 15, 18, 28}`
- Variable `x_40` corresponds to set `A_40 = {5, 15, 25, 30}`
- Variable `x_41` corresponds to set `A_41 = {8, 24, 26, 29}`
- Variable `x_42` corresponds to set `A_42 = {5, 19, 20, 25}`
- Variable `x_43` corresponds to set `A_43 = {8, 13, 15, 25}`
- Variable `x_44` corresponds to set `A_44 = {5, 10, 20, 23}`
- Variable `x_45` corresponds to set `A_45 = {2, 7, 12, 19}`
- Variable `x_46` corresponds to set `A_46 = {10, 18, 19, 27}`
- Variable `x_47` corresponds to set `A_47 = {21, 23, 24, 25}`
- Variable `x_48` corresponds to set `A_48 = {5, 7, 11, 24}`
- Variable `x_49` corresponds to set `A_49 = {11, 13, 18, 30}`
- Variable `x_50` corresponds to set `A_50 = {4, 13, 18, 22}`
- Variable `x_51` corresponds to set `A_51 = {5, 25, 26, 30}`
- Variable `x_52` corresponds to set `A_52 = {4, 8, 11, 28}`
- Variable `x_53` corresponds to set `A_53 = {5, 10, 13, 30}`
- Variable `x_54` corresponds to set `A_54 = {1, 11, 14, 20}`
- Variable `x_55` corresponds to set `A_55 = {2, 4, 25, 27}`
- Variable `x_56` corresponds to set `A_56 = {3, 12, 18, 27}`
- Variable `x_57` corresponds to set `A_57 = {3, 6, 7, 21}`
- Variable `x_58` corresponds to set `A_58 = {4, 12, 21, 26}`
- Variable `x_59` corresponds to set `A_59 = {1, 7, 21, 25}`
- Variable `x_60` corresponds to set `A_60 = {6, 20, 28, 30}`

## Exact constraints

- Constraint `1`: x_8 + x_22 + x_24 + x_34 + x_37 + x_54 + x_59 <= 1
- Constraint `2`: x_12 + x_27 + x_45 + x_55 <= 1
- Constraint `3`: x_1 + x_6 + x_28 + x_38 + x_56 + x_57 <= 1
- Constraint `4`: x_11 + x_13 + x_32 + x_50 + x_52 + x_55 + x_58 <= 1
- Constraint `5`: x_4 + x_5 + x_7 + x_11 + x_13 + x_17 + x_19 + x_20 + x_25 + x_28 + x_30 + x_40 + x_42 + x_44 + x_48 + x_51 + x_53 <= 1
- Constraint `6`: x_5 + x_9 + x_10 + x_24 + x_38 + x_39 + x_57 + x_60 <= 1
- Constraint `7`: x_1 + x_4 + x_45 + x_48 + x_57 + x_59 <= 1
- Constraint `8`: x_2 + x_3 + x_19 + x_22 + x_33 + x_37 + x_41 + x_43 + x_52 <= 1
- Constraint `9`: x_7 + x_11 + x_12 + x_15 + x_35 <= 1
- Constraint `10`: x_5 + x_9 + x_18 + x_21 + x_22 + x_31 + x_32 + x_36 + x_38 + x_44 + x_46 + x_53 <= 1
- Constraint `11`: x_13 + x_14 + x_18 + x_23 + x_29 + x_37 + x_48 + x_49 + x_52 + x_54 <= 1
- Constraint `12`: x_4 + x_8 + x_11 + x_16 + x_26 + x_30 + x_31 + x_32 + x_33 + x_45 + x_56 + x_58 <= 1
- Constraint `13`: x_6 + x_19 + x_25 + x_31 + x_43 + x_49 + x_50 + x_53 <= 1
- Constraint `14`: x_1 + x_10 + x_19 + x_30 + x_33 + x_34 + x_54 <= 1
- Constraint `15`: x_7 + x_15 + x_27 + x_28 + x_29 + x_30 + x_39 + x_40 + x_43 <= 1
- Constraint `16`: x_6 + x_17 + x_21 + x_23 <= 1
- Constraint `17`: x_4 + x_8 + x_9 + x_12 + x_24 + x_33 <= 1
- Constraint `18`: x_6 + x_26 + x_39 + x_46 + x_49 + x_50 + x_56 <= 1
- Constraint `19`: x_3 + x_23 + x_25 + x_42 + x_45 + x_46 <= 1
- Constraint `20`: x_10 + x_20 + x_23 + x_36 + x_42 + x_44 + x_54 + x_60 <= 1
- Constraint `21`: x_10 + x_13 + x_14 + x_17 + x_25 + x_26 + x_31 + x_47 + x_57 + x_58 + x_59 <= 1
- Constraint `22`: x_2 + x_3 + x_5 + x_14 + x_17 + x_50 <= 1
- Constraint `23`: x_2 + x_8 + x_16 + x_18 + x_20 + x_21 + x_35 + x_36 + x_44 + x_47 <= 1
- Constraint `24`: x_1 + x_2 + x_3 + x_16 + x_34 + x_36 + x_38 + x_41 + x_47 + x_48 <= 1
- Constraint `25`: x_9 + x_15 + x_21 + x_28 + x_34 + x_40 + x_42 + x_43 + x_47 + x_51 + x_55 + x_59 <= 1
- Constraint `26`: x_7 + x_18 + x_22 + x_24 + x_27 + x_35 + x_41 + x_51 + x_58 <= 1
- Constraint `27`: x_12 + x_16 + x_26 + x_29 + x_37 + x_46 + x_55 + x_56 <= 1
- Constraint `28`: x_15 + x_20 + x_27 + x_29 + x_32 + x_35 + x_39 + x_52 + x_60 <= 1
- Constraint `29`: x_14 + x_41 <= 1
- Constraint `30`: x_40 + x_49 + x_51 + x_53 + x_60 <= 1
