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

w_1=0.68324817, w_2=1.7996505, w_3=1.2953118, w_4=1.8339267, w_5=1.0050675, w_6=1.0260358, w_7=1.4497261, w_8=0.54287935, w_9=0.78730827, w_10=0.97539295, w_11=1.9296795, w_12=1.7660904, w_13=1.0921443, w_14=1.9110359, w_15=0.98253478, w_16=1.3342277, w_17=1.1943121, w_18=0.63534528, w_19=1.5364584, w_20=0.72884859, w_21=0.78976401, w_22=0.82644393, w_23=0.97310043, w_24=0.6350575, w_25=0.52197983, w_26=1.8212195, w_27=1.020616, w_28=1.0058114, w_29=1.0393401, w_30=0.56312702, w_31=1.9950096, w_32=1.3299083, w_33=1.3316395, w_34=0.80868413, w_35=1.1579511, w_36=1.7407738, w_37=1.8530774, w_38=0.98297219, w_39=1.9721959, w_40=0.90480964, w_41=1.7049845, w_42=1.8189541, w_43=1.0219457, w_44=1.5766683, w_45=0.84561669, w_46=0.98444531, w_47=0.94427129, w_48=1.2523809, w_49=1.0936989, w_50=0.93125607, w_51=0.53393468, w_52=1.9726255, w_53=1.4859985, w_54=0.84561124, w_55=1.6412165, w_56=1.1226452, w_57=0.63942009, w_58=0.87726775, w_59=0.94107815, w_60=1.7733989

## Candidate sets (variables)

- Variable `x_1` corresponds to set `A_1 = {8, 13, 19, 30}`
- Variable `x_2` corresponds to set `A_2 = {16, 18, 26, 27}`
- Variable `x_3` corresponds to set `A_3 = {7, 12, 21, 28}`
- Variable `x_4` corresponds to set `A_4 = {6, 11, 20, 28}`
- Variable `x_5` corresponds to set `A_5 = {7, 12, 25, 30}`
- Variable `x_6` corresponds to set `A_6 = {9, 10, 21, 25}`
- Variable `x_7` corresponds to set `A_7 = {1, 14, 24, 29}`
- Variable `x_8` corresponds to set `A_8 = {4, 15, 23, 27}`
- Variable `x_9` corresponds to set `A_9 = {7, 11, 26, 29}`
- Variable `x_10` corresponds to set `A_10 = {4, 6, 13, 15}`
- Variable `x_11` corresponds to set `A_11 = {4, 5, 20, 23}`
- Variable `x_12` corresponds to set `A_12 = {1, 9, 14, 18}`
- Variable `x_13` corresponds to set `A_13 = {1, 3, 16, 24}`
- Variable `x_14` corresponds to set `A_14 = {5, 6, 16, 24}`
- Variable `x_15` corresponds to set `A_15 = {17, 23, 25, 28}`
- Variable `x_16` corresponds to set `A_16 = {9, 20, 24, 30}`
- Variable `x_17` corresponds to set `A_17 = {17, 19, 21, 23}`
- Variable `x_18` corresponds to set `A_18 = {2, 15, 18, 27}`
- Variable `x_19` corresponds to set `A_19 = {2, 14, 18, 26}`
- Variable `x_20` corresponds to set `A_20 = {4, 10, 18, 28}`
- Variable `x_21` corresponds to set `A_21 = {2, 16, 17, 19}`
- Variable `x_22` corresponds to set `A_22 = {2, 17, 18, 19}`
- Variable `x_23` corresponds to set `A_23 = {9, 16, 24, 26}`
- Variable `x_24` corresponds to set `A_24 = {2, 8, 19, 24}`
- Variable `x_25` corresponds to set `A_25 = {21, 24, 29, 30}`
- Variable `x_26` corresponds to set `A_26 = {1, 5, 21, 22}`
- Variable `x_27` corresponds to set `A_27 = {10, 12, 16, 25}`
- Variable `x_28` corresponds to set `A_28 = {6, 8, 17, 22}`
- Variable `x_29` corresponds to set `A_29 = {4, 5, 16, 21}`
- Variable `x_30` corresponds to set `A_30 = {7, 24, 25, 29}`
- Variable `x_31` corresponds to set `A_31 = {2, 5, 28, 29}`
- Variable `x_32` corresponds to set `A_32 = {16, 23, 26, 29}`
- Variable `x_33` corresponds to set `A_33 = {7, 14, 17, 20}`
- Variable `x_34` corresponds to set `A_34 = {1, 5, 9, 19}`
- Variable `x_35` corresponds to set `A_35 = {1, 19, 20, 21}`
- Variable `x_36` corresponds to set `A_36 = {5, 11, 27, 30}`
- Variable `x_37` corresponds to set `A_37 = {8, 19, 20, 29}`
- Variable `x_38` corresponds to set `A_38 = {7, 10, 14, 18}`
- Variable `x_39` corresponds to set `A_39 = {7, 11, 20, 27}`
- Variable `x_40` corresponds to set `A_40 = {1, 2, 23, 27}`
- Variable `x_41` corresponds to set `A_41 = {16, 17, 21, 25}`
- Variable `x_42` corresponds to set `A_42 = {6, 13, 14, 29}`
- Variable `x_43` corresponds to set `A_43 = {8, 16, 22, 26}`
- Variable `x_44` corresponds to set `A_44 = {12, 18, 21, 27}`
- Variable `x_45` corresponds to set `A_45 = {1, 4, 19, 27}`
- Variable `x_46` corresponds to set `A_46 = {2, 11, 14, 16}`
- Variable `x_47` corresponds to set `A_47 = {9, 13, 17, 30}`
- Variable `x_48` corresponds to set `A_48 = {3, 5, 14, 23}`
- Variable `x_49` corresponds to set `A_49 = {1, 14, 20, 29}`
- Variable `x_50` corresponds to set `A_50 = {2, 4, 8, 23}`
- Variable `x_51` corresponds to set `A_51 = {2, 8, 11, 19}`
- Variable `x_52` corresponds to set `A_52 = {8, 12, 15, 23}`
- Variable `x_53` corresponds to set `A_53 = {3, 9, 15, 21}`
- Variable `x_54` corresponds to set `A_54 = {1, 15, 24, 26}`
- Variable `x_55` corresponds to set `A_55 = {4, 20, 22, 24}`
- Variable `x_56` corresponds to set `A_56 = {5, 23, 25, 26}`
- Variable `x_57` corresponds to set `A_57 = {3, 11, 15, 25}`
- Variable `x_58` corresponds to set `A_58 = {9, 11, 22, 23}`
- Variable `x_59` corresponds to set `A_59 = {12, 17, 29, 30}`
- Variable `x_60` corresponds to set `A_60 = {1, 2, 17, 19}`

## Exact constraints

- Constraint `1`: x_7 + x_12 + x_13 + x_26 + x_34 + x_35 + x_40 + x_45 + x_49 + x_54 + x_60 <= 1
- Constraint `2`: x_18 + x_19 + x_21 + x_22 + x_24 + x_31 + x_40 + x_46 + x_50 + x_51 + x_60 <= 1
- Constraint `3`: x_13 + x_48 + x_53 + x_57 <= 1
- Constraint `4`: x_8 + x_10 + x_11 + x_20 + x_29 + x_45 + x_50 + x_55 <= 1
- Constraint `5`: x_11 + x_14 + x_26 + x_29 + x_31 + x_34 + x_36 + x_48 + x_56 <= 1
- Constraint `6`: x_4 + x_10 + x_14 + x_28 + x_42 <= 1
- Constraint `7`: x_3 + x_5 + x_9 + x_30 + x_33 + x_38 + x_39 <= 1
- Constraint `8`: x_1 + x_24 + x_28 + x_37 + x_43 + x_50 + x_51 + x_52 <= 1
- Constraint `9`: x_6 + x_12 + x_16 + x_23 + x_34 + x_47 + x_53 + x_58 <= 1
- Constraint `10`: x_6 + x_20 + x_27 + x_38 <= 1
- Constraint `11`: x_4 + x_9 + x_36 + x_39 + x_46 + x_51 + x_57 + x_58 <= 1
- Constraint `12`: x_3 + x_5 + x_27 + x_44 + x_52 + x_59 <= 1
- Constraint `13`: x_1 + x_10 + x_42 + x_47 <= 1
- Constraint `14`: x_7 + x_12 + x_19 + x_33 + x_38 + x_42 + x_46 + x_48 + x_49 <= 1
- Constraint `15`: x_8 + x_10 + x_18 + x_52 + x_53 + x_54 + x_57 <= 1
- Constraint `16`: x_2 + x_13 + x_14 + x_21 + x_23 + x_27 + x_29 + x_32 + x_41 + x_43 + x_46 <= 1
- Constraint `17`: x_15 + x_17 + x_21 + x_22 + x_28 + x_33 + x_41 + x_47 + x_59 + x_60 <= 1
- Constraint `18`: x_2 + x_12 + x_18 + x_19 + x_20 + x_22 + x_38 + x_44 <= 1
- Constraint `19`: x_1 + x_17 + x_21 + x_22 + x_24 + x_34 + x_35 + x_37 + x_45 + x_51 + x_60 <= 1
- Constraint `20`: x_4 + x_11 + x_16 + x_33 + x_35 + x_37 + x_39 + x_49 + x_55 <= 1
- Constraint `21`: x_3 + x_6 + x_17 + x_25 + x_26 + x_29 + x_35 + x_41 + x_44 + x_53 <= 1
- Constraint `22`: x_26 + x_28 + x_43 + x_55 + x_58 <= 1
- Constraint `23`: x_8 + x_11 + x_15 + x_17 + x_32 + x_40 + x_48 + x_50 + x_52 + x_56 + x_58 <= 1
- Constraint `24`: x_7 + x_13 + x_14 + x_16 + x_23 + x_24 + x_25 + x_30 + x_54 + x_55 <= 1
- Constraint `25`: x_5 + x_6 + x_15 + x_27 + x_30 + x_41 + x_56 + x_57 <= 1
- Constraint `26`: x_2 + x_9 + x_19 + x_23 + x_32 + x_43 + x_54 + x_56 <= 1
- Constraint `27`: x_2 + x_8 + x_18 + x_36 + x_39 + x_40 + x_44 + x_45 <= 1
- Constraint `28`: x_3 + x_4 + x_15 + x_20 + x_31 <= 1
- Constraint `29`: x_7 + x_9 + x_25 + x_30 + x_31 + x_32 + x_37 + x_42 + x_49 + x_59 <= 1
- Constraint `30`: x_1 + x_5 + x_16 + x_25 + x_36 + x_47 + x_59 <= 1
