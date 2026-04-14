# Original problem: random_unit_n60_m120_set_packing

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
- `capacity_mode`: `set_packing`

## Weights

w_1=0.56846617, w_2=0.50075437, w_3=0.90313194, w_4=0.61136648, w_5=1.3922364, w_6=1.6399253, w_7=0.72633968, w_8=1.0164513, w_9=1.4907513, w_10=1.6755737, w_11=0.75461357, w_12=0.72604446, w_13=0.68928621, w_14=1.566953, w_15=1.4076927, w_16=0.52494943, w_17=1.5317716, w_18=1.3437344, w_19=0.75084018, w_20=0.97414584, w_21=0.87419071, w_22=1.9510225, w_23=0.68826347, w_24=1.2434172, w_25=1.4006588, w_26=1.5886594, w_27=1.2179335, w_28=0.88666328, w_29=1.5571307, w_30=1.9971699, w_31=1.6808459, w_32=1.1888313, w_33=0.91428055, w_34=1.0552576, w_35=0.63740005, w_36=1.745301, w_37=0.84896492, w_38=1.3198716, w_39=0.50698126, w_40=1.0952427, w_41=1.2838396, w_42=1.3986289, w_43=1.1195992, w_44=1.6337445, w_45=0.94824284, w_46=0.80568617, w_47=0.97493412, w_48=1.0274079, w_49=1.0069889, w_50=1.5723663, w_51=1.2884315, w_52=1.0426447, w_53=1.2188937, w_54=0.82994637, w_55=1.9440002, w_56=1.6318459, w_57=1.8762019, w_58=1.9410628, w_59=1.120069, w_60=1.5551566

## Exact constraints

- Constraint `1`: x_16 + x_27 + x_33 + x_34 + x_39 + x_41 + x_42 + x_52 + x_55 <= 1
- Constraint `2`: x_4 + x_26 + x_36 + x_42 + x_43 <= 1
- Constraint `3`: x_9 + x_17 + x_33 + x_41 + x_46 + x_52 + x_55 + x_57 <= 1
- Constraint `4`: x_8 + x_26 + x_36 + x_39 + x_45 <= 1
- Constraint `5`: x_18 + x_21 + x_22 + x_50 + x_59 <= 1
- Constraint `6`: x_4 + x_8 + x_29 + x_30 + x_39 + x_44 + x_50 + x_54 + x_57 <= 1
- Constraint `7`: x_9 + x_16 + x_27 + x_37 + x_50 + x_51 + x_52 <= 1
- Constraint `8`: x_6 + x_7 + x_11 + x_21 + x_32 + x_35 + x_52 <= 1
- Constraint `9`: x_6 + x_20 + x_26 + x_38 + x_39 + x_44 + x_47 + x_50 + x_59 <= 1
- Constraint `10`: x_1 + x_4 + x_7 + x_23 + x_29 + x_30 + x_35 + x_52 + x_59 <= 1
- Constraint `11`: x_11 + x_19 + x_22 + x_33 + x_35 + x_45 + x_49 + x_56 <= 1
- Constraint `12`: x_24 + x_38 + x_39 + x_49 + x_57 <= 1
- Constraint `13`: x_1 + x_4 + x_7 + x_18 + x_25 + x_46 + x_57 + x_60 <= 1
- Constraint `14`: x_4 + x_10 + x_12 + x_13 + x_15 + x_24 + x_38 + x_47 + x_50 <= 1
- Constraint `15`: x_1 + x_21 + x_53 + x_54 + x_60 <= 1
- Constraint `16`: x_4 + x_13 + x_17 + x_19 + x_22 + x_25 + x_40 + x_41 + x_46 + x_55 <= 1
- Constraint `17`: x_2 + x_6 + x_9 + x_14 + x_17 + x_26 + x_40 + x_49 + x_50 + x_59 <= 1
- Constraint `18`: x_7 + x_20 + x_24 + x_45 + x_51 + x_52 + x_57 <= 1
- Constraint `19`: x_10 + x_12 + x_15 + x_22 + x_27 + x_32 + x_39 + x_48 + x_55 + x_56 <= 1
- Constraint `20`: x_7 + x_18 + x_19 + x_20 + x_28 + x_45 + x_52 + x_54 + x_59 <= 1
- Constraint `21`: x_1 + x_38 + x_39 + x_56 + x_57 <= 1
- Constraint `22`: x_19 + x_27 + x_48 + x_49 + x_53 <= 1
- Constraint `23`: x_1 + x_17 + x_19 + x_24 + x_29 + x_30 + x_36 + x_37 + x_57 <= 1
- Constraint `24`: x_4 + x_25 + x_29 + x_30 + x_39 <= 1
- Constraint `25`: x_4 + x_10 + x_16 + x_28 + x_32 + x_46 + x_49 + x_50 <= 1
- Constraint `26`: x_24 + x_27 + x_35 + x_47 + x_56 + x_57 + x_60 <= 1
- Constraint `27`: x_1 + x_2 + x_25 + x_32 + x_54 <= 1
- Constraint `28`: x_5 + x_7 + x_19 + x_23 + x_33 + x_47 + x_55 + x_56 <= 1
- Constraint `29`: x_3 + x_29 + x_36 + x_37 + x_53 <= 1
- Constraint `30`: x_4 + x_7 + x_9 + x_30 + x_38 + x_42 + x_49 + x_50 <= 1
- Constraint `31`: x_2 + x_6 + x_8 + x_25 + x_30 + x_35 + x_46 + x_50 + x_56 + x_60 <= 1
- Constraint `32`: x_1 + x_8 + x_36 + x_42 + x_48 + x_60 <= 1
- Constraint `33`: x_3 + x_12 + x_21 + x_27 + x_38 + x_39 + x_40 + x_48 + x_54 + x_57 <= 1
- Constraint `34`: x_19 + x_20 + x_32 + x_33 + x_34 + x_39 + x_42 <= 1
- Constraint `35`: x_15 + x_18 + x_25 + x_27 + x_41 + x_43 + x_58 <= 1
- Constraint `36`: x_10 + x_25 + x_30 + x_47 + x_54 + x_55 <= 1
- Constraint `37`: x_2 + x_5 + x_10 + x_14 + x_20 + x_21 + x_22 + x_23 + x_40 + x_49 <= 1
- Constraint `38`: x_13 + x_17 + x_33 + x_34 + x_35 + x_40 + x_45 + x_53 + x_55 <= 1
- Constraint `39`: x_6 + x_10 + x_14 + x_26 + x_31 + x_42 + x_51 + x_59 <= 1
- Constraint `40`: x_2 + x_4 + x_11 + x_13 + x_30 <= 1
- Constraint `41`: x_4 + x_6 + x_20 + x_26 + x_30 + x_33 + x_35 + x_46 <= 1
- Constraint `42`: x_6 + x_20 + x_30 + x_33 + x_41 + x_52 + x_54 + x_59 <= 1
- Constraint `43`: x_1 + x_3 + x_17 + x_21 + x_23 + x_36 + x_42 + x_55 <= 1
- Constraint `44`: x_18 + x_21 + x_24 + x_25 + x_29 + x_40 + x_55 <= 1
- Constraint `45`: x_17 + x_40 + x_45 + x_58 + x_60 <= 1
- Constraint `46`: x_19 + x_26 + x_31 + x_32 + x_58 <= 1
- Constraint `47`: x_14 + x_15 + x_21 + x_23 + x_47 + x_49 <= 1
- Constraint `48`: x_9 + x_14 + x_23 + x_27 + x_52 <= 1
- Constraint `49`: x_2 + x_5 + x_6 + x_8 + x_9 + x_24 + x_43 + x_52 + x_53 + x_60 <= 1
- Constraint `50`: x_9 + x_13 + x_18 + x_21 + x_47 + x_55 <= 1
- Constraint `51`: x_1 + x_4 + x_8 + x_12 + x_15 + x_22 + x_25 + x_42 + x_51 + x_59 <= 1
- Constraint `52`: x_5 + x_7 + x_9 + x_15 + x_19 + x_24 + x_43 + x_49 <= 1
- Constraint `53`: x_15 + x_26 + x_29 + x_43 + x_55 + x_56 <= 1
- Constraint `54`: x_20 + x_22 + x_28 + x_50 + x_53 <= 1
- Constraint `55`: x_20 + x_22 + x_24 + x_26 + x_34 + x_37 + x_40 + x_46 + x_47 <= 1
- Constraint `56`: x_5 + x_8 + x_13 + x_17 + x_18 + x_25 + x_38 <= 1
- Constraint `57`: x_1 + x_8 + x_19 + x_25 + x_32 + x_35 + x_38 + x_39 <= 1
- Constraint `58`: x_3 + x_20 + x_28 + x_39 + x_42 <= 1
- Constraint `59`: x_27 + x_48 + x_52 + x_53 + x_55 <= 1
- Constraint `60`: x_6 + x_32 + x_45 + x_47 + x_53 <= 1
- Constraint `61`: x_1 + x_14 + x_24 + x_26 + x_28 + x_32 + x_38 + x_42 + x_46 <= 1
- Constraint `62`: x_12 + x_16 + x_19 + x_27 + x_38 + x_40 + x_42 + x_44 + x_53 <= 1
- Constraint `63`: x_2 + x_6 + x_10 + x_18 + x_36 + x_47 + x_59 <= 1
- Constraint `64`: x_4 + x_8 + x_17 + x_21 + x_28 + x_53 + x_58 + x_59 <= 1
- Constraint `65`: x_29 + x_35 + x_37 + x_43 + x_47 + x_54 + x_57 + x_58 <= 1
- Constraint `66`: x_18 + x_43 + x_47 + x_51 + x_55 + x_56 <= 1
- Constraint `67`: x_2 + x_24 + x_30 + x_33 + x_41 + x_58 <= 1
- Constraint `68`: x_8 + x_18 + x_27 + x_33 + x_39 + x_40 + x_46 <= 1
- Constraint `69`: x_6 + x_7 + x_17 + x_33 + x_40 <= 1
- Constraint `70`: x_3 + x_9 + x_11 + x_15 + x_27 + x_38 + x_39 + x_53 <= 1
- Constraint `71`: x_4 + x_5 + x_12 + x_16 + x_31 + x_38 + x_39 + x_43 + x_48 <= 1
- Constraint `72`: x_1 + x_2 + x_11 + x_13 + x_19 + x_48 + x_50 + x_54 + x_58 <= 1
- Constraint `73`: x_6 + x_8 + x_9 + x_16 + x_25 + x_31 + x_49 + x_52 + x_57 + x_58 <= 1
- Constraint `74`: x_8 + x_12 + x_20 + x_22 + x_23 + x_27 + x_37 + x_50 + x_58 <= 1
- Constraint `75`: x_22 + x_24 + x_28 + x_31 + x_41 + x_45 + x_48 + x_51 <= 1
- Constraint `76`: x_2 + x_7 + x_29 + x_39 + x_42 + x_43 + x_60 <= 1
- Constraint `77`: x_21 + x_24 + x_25 + x_26 + x_27 + x_37 + x_44 + x_57 <= 1
- Constraint `78`: x_2 + x_3 + x_38 + x_43 + x_44 + x_46 + x_57 + x_59 <= 1
- Constraint `79`: x_4 + x_22 + x_27 + x_32 + x_43 + x_44 + x_57 + x_58 + x_59 <= 1
- Constraint `80`: x_5 + x_7 + x_9 + x_33 + x_40 + x_42 + x_52 <= 1
- Constraint `81`: x_5 + x_22 + x_28 + x_34 + x_40 + x_51 <= 1
- Constraint `82`: x_13 + x_15 + x_18 + x_36 + x_46 <= 1
- Constraint `83`: x_2 + x_6 + x_9 + x_36 + x_52 + x_55 + x_57 + x_60 <= 1
- Constraint `84`: x_10 + x_15 + x_26 + x_33 + x_35 + x_36 + x_40 + x_52 <= 1
- Constraint `85`: x_12 + x_16 + x_29 + x_51 + x_57 <= 1
- Constraint `86`: x_4 + x_42 + x_52 + x_54 + x_59 <= 1
- Constraint `87`: x_2 + x_14 + x_31 + x_34 + x_35 <= 1
- Constraint `88`: x_17 + x_18 + x_24 + x_36 + x_37 + x_39 <= 1
- Constraint `89`: x_15 + x_16 + x_30 + x_44 + x_45 + x_47 + x_48 + x_52 + x_53 + x_58 <= 1
- Constraint `90`: x_2 + x_22 + x_30 + x_37 + x_40 + x_41 + x_45 + x_51 + x_54 + x_58 <= 1
- Constraint `91`: x_8 + x_10 + x_22 + x_30 + x_51 + x_54 <= 1
- Constraint `92`: x_2 + x_8 + x_15 + x_26 + x_28 + x_39 + x_47 + x_52 + x_60 <= 1
- Constraint `93`: x_15 + x_25 + x_34 + x_37 + x_40 + x_48 <= 1
- Constraint `94`: x_7 + x_17 + x_35 + x_36 + x_45 <= 1
- Constraint `95`: x_8 + x_10 + x_11 + x_22 + x_50 + x_59 <= 1
- Constraint `96`: x_2 + x_6 + x_16 + x_28 + x_34 + x_36 + x_43 + x_51 + x_52 <= 1
- Constraint `97`: x_10 + x_12 + x_17 + x_20 + x_21 + x_29 + x_30 + x_35 + x_51 <= 1
- Constraint `98`: x_9 + x_23 + x_30 + x_39 + x_42 + x_52 + x_56 + x_58 + x_59 <= 1
- Constraint `99`: x_4 + x_7 + x_9 + x_23 + x_25 + x_33 + x_43 + x_44 + x_47 + x_55 <= 1
- Constraint `100`: x_2 + x_7 + x_12 + x_41 + x_43 + x_48 + x_49 + x_57 <= 1
- Constraint `101`: x_2 + x_10 + x_18 + x_23 + x_29 + x_34 + x_37 + x_40 + x_42 <= 1
- Constraint `102`: x_7 + x_40 + x_44 + x_49 + x_50 + x_52 + x_57 <= 1
- Constraint `103`: x_6 + x_8 + x_13 + x_16 + x_17 + x_19 + x_21 + x_24 + x_32 <= 1
- Constraint `104`: x_8 + x_11 + x_13 + x_21 + x_26 + x_31 + x_36 + x_37 + x_44 + x_57 <= 1
- Constraint `105`: x_6 + x_7 + x_10 + x_11 + x_30 + x_32 + x_39 + x_47 + x_58 + x_60 <= 1
- Constraint `106`: x_16 + x_19 + x_25 + x_29 + x_30 + x_32 + x_35 + x_40 + x_60 <= 1
- Constraint `107`: x_3 + x_6 + x_9 + x_21 + x_37 + x_38 + x_44 + x_48 + x_49 + x_58 <= 1
- Constraint `108`: x_11 + x_12 + x_14 + x_19 + x_33 + x_36 + x_38 + x_42 + x_53 <= 1
- Constraint `109`: x_9 + x_10 + x_15 + x_35 + x_37 + x_42 <= 1
- Constraint `110`: x_4 + x_8 + x_12 + x_13 + x_18 + x_23 + x_32 + x_40 + x_45 + x_48 <= 1
- Constraint `111`: x_4 + x_27 + x_31 + x_37 + x_40 <= 1
- Constraint `112`: x_3 + x_12 + x_14 + x_25 + x_26 + x_33 + x_36 + x_40 + x_48 + x_53 <= 1
- Constraint `113`: x_7 + x_8 + x_13 + x_23 + x_27 + x_34 + x_35 + x_36 + x_52 <= 1
- Constraint `114`: x_21 + x_23 + x_24 + x_37 + x_40 + x_49 <= 1
- Constraint `115`: x_1 + x_3 + x_4 + x_5 + x_29 + x_30 + x_34 + x_45 + x_47 + x_59 <= 1
- Constraint `116`: x_5 + x_9 + x_10 + x_27 + x_32 + x_33 + x_36 + x_50 + x_56 <= 1
- Constraint `117`: x_5 + x_18 + x_29 + x_32 + x_33 + x_38 + x_41 + x_48 <= 1
- Constraint `118`: x_2 + x_26 + x_33 + x_38 + x_50 + x_53 + x_58 + x_60 <= 1
- Constraint `119`: x_7 + x_8 + x_19 + x_24 + x_27 + x_28 + x_34 + x_36 + x_44 + x_52 <= 1
- Constraint `120`: x_3 + x_15 + x_19 + x_45 + x_54 <= 1
