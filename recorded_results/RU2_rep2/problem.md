# Original problem: random_unit_n60_m120_mixed

This file records the exact original binary packing problem used for the matching run result.

## Optimization model

\[
\max_{x\in\{0,1\}^n}\ \sum_{i=1}^n w_i x_i
\qquad\text{s.t.}\qquad
\sum_{i\in S_k} x_i \le B_k,\quad k=1,\dots,m.
\]

- Number of variables: `60`
- Number of constraints: `120`
- Matching run-result file: `result.json`

## Metadata

- `generator`: `random_unit_packing`
- `row_size_range`: `[5, 10]`
- `capacity_mode`: `mixed`

## Weights

w_1=0.59765851, w_2=1.4838948, w_3=1.5453135, w_4=1.8534778, w_5=0.82665415, w_6=1.6920237, w_7=0.55170594, w_8=1.5552036, w_9=1.6150484, w_10=1.1465525, w_11=1.8277724, w_12=1.2708201, w_13=1.2721097, w_14=1.7537433, w_15=1.7426767, w_16=0.95178014, w_17=1.1320399, w_18=0.5574424, w_19=0.60819538, w_20=1.6467026, w_21=1.4541307, w_22=1.9243323, w_23=0.88413287, w_24=1.2117877, w_25=0.53487418, w_26=0.85071269, w_27=1.8743042, w_28=1.3758672, w_29=0.54059945, w_30=1.1553621, w_31=1.3297851, w_32=0.6736937, w_33=1.4188793, w_34=0.71801451, w_35=0.58755225, w_36=1.2761424, w_37=1.0370446, w_38=0.74966767, w_39=1.8848559, w_40=1.9667588, w_41=1.3096599, w_42=1.8450555, w_43=1.9000785, w_44=0.72502618, w_45=0.7399565, w_46=0.77866852, w_47=1.6908743, w_48=1.8969536, w_49=1.9112789, w_50=1.8803487, w_51=1.1781434, w_52=1.6653521, w_53=1.1781713, w_54=1.9993951, w_55=0.63347592, w_56=0.95290883, w_57=0.61935725, w_58=1.2492401, w_59=1.4461505, w_60=1.8606713

## Exact constraints

- Constraint `1`: x_16 + x_17 + x_32 + x_37 + x_48 + x_51 + x_57 + x_58 + x_59 <= 3
- Constraint `2`: x_1 + x_8 + x_12 + x_20 + x_21 + x_35 + x_40 + x_46 + x_54 <= 3
- Constraint `3`: x_3 + x_20 + x_27 + x_39 + x_43 + x_46 + x_49 + x_54 <= 3
- Constraint `4`: x_1 + x_4 + x_5 + x_9 + x_18 + x_35 + x_38 + x_51 <= 5
- Constraint `5`: x_14 + x_16 + x_20 + x_47 + x_58 <= 2
- Constraint `6`: x_2 + x_22 + x_23 + x_29 + x_37 + x_52 <= 4
- Constraint `7`: x_6 + x_7 + x_22 + x_31 + x_42 + x_47 + x_58 <= 6
- Constraint `8`: x_4 + x_5 + x_8 + x_15 + x_18 + x_20 + x_32 + x_36 + x_46 + x_50 <= 5
- Constraint `9`: x_17 + x_25 + x_27 + x_44 + x_49 + x_51 + x_56 <= 6
- Constraint `10`: x_1 + x_4 + x_20 + x_21 + x_37 + x_40 <= 2
- Constraint `11`: x_7 + x_16 + x_19 + x_24 + x_28 + x_30 + x_40 + x_43 + x_49 + x_50 <= 4
- Constraint `12`: x_1 + x_8 + x_13 + x_18 + x_20 + x_38 + x_42 + x_44 + x_47 <= 8
- Constraint `13`: x_16 + x_30 + x_39 + x_40 + x_56 <= 3
- Constraint `14`: x_6 + x_16 + x_33 + x_37 + x_40 + x_46 + x_47 <= 5
- Constraint `15`: x_8 + x_10 + x_38 + x_41 + x_42 + x_55 <= 3
- Constraint `16`: x_21 + x_29 + x_44 + x_45 + x_56 + x_57 <= 3
- Constraint `17`: x_2 + x_14 + x_20 + x_24 + x_34 + x_45 <= 5
- Constraint `18`: x_17 + x_37 + x_38 + x_44 + x_47 + x_53 + x_59 <= 6
- Constraint `19`: x_3 + x_12 + x_17 + x_18 + x_36 + x_43 + x_47 + x_52 + x_56 <= 7
- Constraint `20`: x_2 + x_5 + x_17 + x_31 + x_37 + x_60 <= 2
- Constraint `21`: x_1 + x_5 + x_17 + x_27 + x_33 + x_41 + x_56 <= 6
- Constraint `22`: x_10 + x_38 + x_42 + x_45 + x_48 + x_58 <= 3
- Constraint `23`: x_16 + x_21 + x_22 + x_35 + x_54 <= 4
- Constraint `24`: x_5 + x_20 + x_23 + x_25 + x_26 + x_29 <= 4
- Constraint `25`: x_8 + x_9 + x_24 + x_33 + x_41 + x_43 + x_51 <= 3
- Constraint `26`: x_9 + x_10 + x_18 + x_36 + x_40 + x_48 + x_49 + x_56 + x_59 + x_60 <= 8
- Constraint `27`: x_4 + x_5 + x_11 + x_12 + x_27 + x_33 + x_55 + x_57 + x_58 <= 1
- Constraint `28`: x_6 + x_8 + x_9 + x_11 + x_24 + x_25 + x_34 + x_44 + x_54 + x_59 <= 3
- Constraint `29`: x_7 + x_17 + x_25 + x_28 + x_33 + x_36 + x_41 + x_49 + x_52 + x_58 <= 4
- Constraint `30`: x_9 + x_20 + x_21 + x_54 + x_58 + x_59 <= 1
- Constraint `31`: x_5 + x_15 + x_40 + x_43 + x_58 <= 2
- Constraint `32`: x_5 + x_11 + x_24 + x_26 + x_33 + x_51 + x_52 + x_56 <= 2
- Constraint `33`: x_5 + x_20 + x_23 + x_25 + x_27 + x_30 + x_43 <= 5
- Constraint `34`: x_3 + x_19 + x_23 + x_45 + x_56 + x_60 <= 5
- Constraint `35`: x_2 + x_14 + x_17 + x_21 + x_25 + x_27 + x_42 + x_43 + x_49 + x_55 <= 6
- Constraint `36`: x_5 + x_13 + x_20 + x_27 + x_51 + x_53 + x_60 <= 2
- Constraint `37`: x_3 + x_13 + x_24 + x_34 + x_52 <= 2
- Constraint `38`: x_6 + x_12 + x_14 + x_24 + x_27 + x_38 + x_44 + x_53 + x_59 <= 6
- Constraint `39`: x_10 + x_16 + x_20 + x_21 + x_32 + x_34 + x_39 + x_47 + x_53 <= 4
- Constraint `40`: x_9 + x_11 + x_12 + x_21 + x_28 + x_30 + x_32 + x_35 + x_46 <= 5
- Constraint `41`: x_1 + x_8 + x_16 + x_17 + x_28 + x_35 + x_38 + x_41 + x_49 + x_55 <= 6
- Constraint `42`: x_6 + x_10 + x_22 + x_23 + x_26 + x_37 + x_45 + x_56 + x_58 <= 1
- Constraint `43`: x_3 + x_4 + x_15 + x_30 + x_31 + x_33 + x_36 + x_49 + x_54 + x_59 <= 3
- Constraint `44`: x_9 + x_14 + x_15 + x_25 + x_44 + x_52 + x_53 + x_57 <= 1
- Constraint `45`: x_1 + x_25 + x_27 + x_28 + x_35 + x_41 + x_45 + x_58 <= 2
- Constraint `46`: x_2 + x_15 + x_29 + x_35 + x_39 + x_45 + x_55 <= 4
- Constraint `47`: x_17 + x_46 + x_52 + x_57 + x_60 <= 1
- Constraint `48`: x_15 + x_24 + x_25 + x_44 + x_47 + x_58 + x_59 <= 6
- Constraint `49`: x_9 + x_26 + x_37 + x_40 + x_51 <= 3
- Constraint `50`: x_10 + x_17 + x_21 + x_34 + x_55 + x_56 <= 4
- Constraint `51`: x_1 + x_6 + x_11 + x_22 + x_29 + x_39 + x_52 <= 6
- Constraint `52`: x_17 + x_26 + x_36 + x_37 + x_51 + x_54 + x_55 + x_56 <= 7
- Constraint `53`: x_3 + x_9 + x_15 + x_16 + x_18 + x_45 + x_50 + x_53 + x_58 <= 2
- Constraint `54`: x_2 + x_3 + x_10 + x_12 + x_14 + x_23 + x_32 + x_35 + x_38 <= 5
- Constraint `55`: x_2 + x_23 + x_25 + x_29 + x_47 + x_55 <= 5
- Constraint `56`: x_11 + x_23 + x_31 + x_47 + x_51 + x_56 <= 5
- Constraint `57`: x_9 + x_26 + x_28 + x_41 + x_43 + x_50 <= 2
- Constraint `58`: x_5 + x_6 + x_17 + x_30 + x_35 + x_50 <= 3
- Constraint `59`: x_1 + x_6 + x_18 + x_20 + x_23 + x_45 + x_49 <= 4
- Constraint `60`: x_2 + x_3 + x_8 + x_10 + x_11 + x_15 + x_28 + x_37 + x_42 + x_56 <= 8
- Constraint `61`: x_2 + x_16 + x_17 + x_27 + x_40 + x_48 + x_49 + x_53 + x_54 + x_60 <= 4
- Constraint `62`: x_3 + x_7 + x_14 + x_23 + x_27 + x_48 + x_52 + x_53 <= 3
- Constraint `63`: x_1 + x_8 + x_23 + x_26 + x_30 + x_35 + x_39 + x_54 <= 1
- Constraint `64`: x_3 + x_8 + x_12 + x_17 + x_41 + x_54 + x_56 + x_58 + x_60 <= 6
- Constraint `65`: x_19 + x_44 + x_45 + x_53 + x_56 <= 2
- Constraint `66`: x_3 + x_5 + x_10 + x_20 + x_30 + x_51 + x_52 + x_55 <= 3
- Constraint `67`: x_1 + x_10 + x_16 + x_23 + x_25 + x_31 + x_42 + x_53 <= 2
- Constraint `68`: x_3 + x_12 + x_14 + x_20 + x_21 + x_29 + x_55 + x_57 <= 6
- Constraint `69`: x_3 + x_8 + x_15 + x_25 + x_59 + x_60 <= 3
- Constraint `70`: x_2 + x_5 + x_29 + x_42 + x_44 + x_60 <= 1
- Constraint `71`: x_3 + x_7 + x_14 + x_24 + x_38 + x_41 + x_42 + x_44 + x_51 + x_54 <= 6
- Constraint `72`: x_4 + x_10 + x_18 + x_26 + x_28 + x_34 + x_39 + x_47 <= 5
- Constraint `73`: x_17 + x_27 + x_38 + x_46 + x_51 + x_60 <= 3
- Constraint `74`: x_1 + x_10 + x_17 + x_37 + x_41 <= 3
- Constraint `75`: x_13 + x_14 + x_20 + x_30 + x_42 + x_43 + x_46 + x_52 + x_53 + x_60 <= 3
- Constraint `76`: x_2 + x_3 + x_14 + x_30 + x_34 + x_37 + x_38 + x_41 + x_47 <= 6
- Constraint `77`: x_5 + x_7 + x_10 + x_17 + x_28 + x_30 + x_34 + x_42 + x_56 + x_59 <= 7
- Constraint `78`: x_9 + x_21 + x_29 + x_30 + x_37 + x_39 + x_47 + x_50 + x_60 <= 6
- Constraint `79`: x_1 + x_9 + x_17 + x_25 + x_29 + x_42 + x_58 <= 6
- Constraint `80`: x_10 + x_18 + x_21 + x_28 + x_50 + x_54 + x_55 + x_58 <= 3
- Constraint `81`: x_4 + x_13 + x_30 + x_44 + x_45 + x_49 + x_56 + x_57 <= 4
- Constraint `82`: x_21 + x_28 + x_33 + x_35 + x_41 + x_46 + x_51 <= 5
- Constraint `83`: x_3 + x_4 + x_9 + x_15 + x_29 + x_31 + x_47 + x_48 + x_51 + x_53 <= 4
- Constraint `84`: x_9 + x_19 + x_20 + x_21 + x_30 + x_49 + x_50 <= 2
- Constraint `85`: x_6 + x_8 + x_32 + x_44 + x_52 + x_54 <= 2
- Constraint `86`: x_3 + x_4 + x_19 + x_32 + x_41 <= 1
- Constraint `87`: x_3 + x_7 + x_14 + x_27 + x_45 + x_55 + x_58 <= 3
- Constraint `88`: x_9 + x_27 + x_35 + x_52 + x_55 <= 3
- Constraint `89`: x_36 + x_38 + x_39 + x_46 + x_50 + x_52 <= 5
- Constraint `90`: x_2 + x_13 + x_18 + x_19 + x_31 + x_35 + x_46 + x_52 + x_56 + x_57 <= 3
- Constraint `91`: x_12 + x_26 + x_29 + x_33 + x_37 + x_39 + x_46 + x_47 + x_48 <= 5
- Constraint `92`: x_7 + x_13 + x_28 + x_29 + x_40 + x_48 + x_50 + x_51 + x_55 <= 8
- Constraint `93`: x_7 + x_8 + x_27 + x_41 + x_46 + x_49 <= 5
- Constraint `94`: x_6 + x_7 + x_10 + x_29 + x_43 + x_46 + x_49 + x_54 <= 1
- Constraint `95`: x_5 + x_15 + x_16 + x_38 + x_44 + x_46 + x_47 <= 5
- Constraint `96`: x_7 + x_20 + x_27 + x_43 + x_49 + x_51 <= 3
- Constraint `97`: x_1 + x_8 + x_21 + x_26 + x_35 + x_53 + x_55 + x_56 <= 6
- Constraint `98`: x_31 + x_32 + x_33 + x_53 + x_57 + x_59 <= 1
- Constraint `99`: x_4 + x_7 + x_10 + x_20 + x_32 + x_34 + x_38 + x_44 + x_53 + x_57 <= 1
- Constraint `100`: x_6 + x_8 + x_16 + x_31 + x_38 + x_40 + x_49 + x_51 + x_53 + x_54 <= 2
- Constraint `101`: x_10 + x_12 + x_22 + x_25 + x_30 + x_56 + x_57 <= 5
- Constraint `102`: x_7 + x_10 + x_12 + x_23 + x_32 + x_37 + x_39 + x_48 + x_56 <= 7
- Constraint `103`: x_2 + x_7 + x_9 + x_16 + x_22 + x_31 + x_39 + x_40 + x_41 + x_52 <= 1
- Constraint `104`: x_4 + x_10 + x_18 + x_25 + x_34 + x_38 + x_40 + x_45 + x_46 <= 7
- Constraint `105`: x_1 + x_36 + x_51 + x_53 + x_54 <= 2
- Constraint `106`: x_1 + x_16 + x_29 + x_32 + x_42 + x_48 + x_54 + x_58 + x_59 + x_60 <= 1
- Constraint `107`: x_11 + x_22 + x_24 + x_42 + x_47 + x_48 + x_59 <= 2
- Constraint `108`: x_4 + x_22 + x_29 + x_32 + x_39 + x_42 + x_54 <= 4
- Constraint `109`: x_12 + x_31 + x_34 + x_40 + x_42 + x_48 + x_55 + x_58 <= 4
- Constraint `110`: x_3 + x_9 + x_22 + x_26 + x_29 + x_35 + x_51 + x_52 + x_57 <= 7
- Constraint `111`: x_2 + x_12 + x_14 + x_18 + x_36 + x_38 + x_50 + x_59 <= 4
- Constraint `112`: x_3 + x_8 + x_17 + x_45 + x_56 <= 3
- Constraint `113`: x_7 + x_12 + x_29 + x_36 + x_46 + x_47 <= 1
- Constraint `114`: x_3 + x_13 + x_23 + x_25 + x_27 + x_34 + x_51 + x_52 + x_54 + x_58 <= 1
- Constraint `115`: x_2 + x_13 + x_17 + x_31 + x_32 + x_44 + x_49 + x_55 + x_59 <= 7
- Constraint `116`: x_1 + x_11 + x_19 + x_25 + x_30 + x_32 + x_38 + x_41 + x_46 <= 5
- Constraint `117`: x_13 + x_30 + x_34 + x_38 + x_53 + x_55 + x_56 <= 2
- Constraint `118`: x_2 + x_12 + x_16 + x_20 + x_34 + x_49 <= 4
- Constraint `119`: x_5 + x_6 + x_26 + x_31 + x_37 + x_42 + x_48 + x_49 <= 1
- Constraint `120`: x_15 + x_25 + x_33 + x_34 + x_44 + x_45 + x_46 + x_50 + x_55 + x_60 <= 6
