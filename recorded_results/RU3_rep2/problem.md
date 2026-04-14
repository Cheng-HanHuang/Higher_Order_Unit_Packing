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

w_1=0.51691487, w_2=1.1767797, w_3=1.2163042, w_4=1.2192682, w_5=1.3664153, w_6=1.9322369, w_7=0.84864957, w_8=1.1321049, w_9=1.3195318, w_10=1.120819, w_11=1.3562001, w_12=0.98594503, w_13=0.91746032, w_14=0.68578809, w_15=0.63728549, w_16=0.66580142, w_17=1.3031254, w_18=0.64847763, w_19=0.97263391, w_20=1.6632839, w_21=0.7878815, w_22=1.3976496, w_23=1.9032441, w_24=0.80798456, w_25=1.6817433, w_26=1.2671241, w_27=0.53511771, w_28=1.9162467, w_29=0.86000553, w_30=1.430498, w_31=1.565075, w_32=1.2496683, w_33=1.0238636, w_34=1.28937, w_35=0.91350423, w_36=1.0739319, w_37=0.60080978, w_38=1.313177, w_39=0.52166376, w_40=1.2415592, w_41=1.7550254, w_42=0.75212319, w_43=1.9444618, w_44=1.8371424, w_45=1.240192, w_46=1.8385151, w_47=0.9385948, w_48=0.90012283, w_49=1.3925319, w_50=1.1314992, w_51=1.2184467, w_52=0.81750427, w_53=0.52112502, w_54=1.3975613, w_55=0.88683517, w_56=0.8745623, w_57=1.9777014, w_58=1.3573238, w_59=0.71762481, w_60=0.84316968

## Exact constraints

- Constraint `1`: x_28 + x_31 + x_32 + x_40 + x_48 + x_57 <= 1
- Constraint `2`: x_1 + x_13 + x_16 + x_29 + x_40 <= 1
- Constraint `3`: x_14 + x_27 + x_35 + x_38 + x_40 <= 1
- Constraint `4`: x_11 + x_24 + x_42 + x_48 + x_55 + x_58 <= 1
- Constraint `5`: x_12 + x_19 + x_23 + x_34 + x_38 + x_41 + x_42 + x_54 <= 1
- Constraint `6`: x_7 + x_10 + x_36 + x_49 + x_58 + x_59 + x_60 <= 1
- Constraint `7`: x_5 + x_10 + x_13 + x_17 + x_24 + x_36 + x_45 + x_53 + x_58 <= 1
- Constraint `8`: x_14 + x_23 + x_43 + x_47 + x_57 <= 1
- Constraint `9`: x_37 + x_38 + x_39 + x_56 + x_58 <= 1
- Constraint `10`: x_12 + x_38 + x_44 + x_49 + x_53 <= 1
- Constraint `11`: x_12 + x_15 + x_19 + x_22 + x_27 + x_28 + x_36 <= 1
- Constraint `12`: x_5 + x_8 + x_14 + x_22 + x_23 + x_38 + x_50 + x_55 + x_56 <= 1
- Constraint `13`: x_5 + x_25 + x_33 + x_37 + x_49 <= 1
- Constraint `14`: x_8 + x_18 + x_24 + x_35 + x_41 + x_45 + x_53 + x_56 + x_57 <= 1
- Constraint `15`: x_1 + x_6 + x_21 + x_45 + x_59 <= 1
- Constraint `16`: x_21 + x_30 + x_41 + x_43 + x_45 + x_47 + x_49 + x_52 + x_57 <= 1
- Constraint `17`: x_5 + x_6 + x_7 + x_13 + x_33 + x_40 <= 1
- Constraint `18`: x_1 + x_5 + x_35 + x_48 + x_57 + x_59 <= 1
- Constraint `19`: x_17 + x_24 + x_38 + x_46 + x_47 + x_56 <= 1
- Constraint `20`: x_11 + x_23 + x_32 + x_35 + x_44 + x_46 + x_53 + x_54 <= 1
- Constraint `21`: x_5 + x_19 + x_35 + x_43 + x_49 + x_58 <= 1
- Constraint `22`: x_1 + x_17 + x_25 + x_53 + x_55 + x_58 <= 1
- Constraint `23`: x_6 + x_11 + x_25 + x_26 + x_28 + x_35 + x_38 + x_45 + x_57 <= 1
- Constraint `24`: x_6 + x_8 + x_10 + x_18 + x_19 + x_20 + x_26 + x_35 + x_52 <= 1
- Constraint `25`: x_12 + x_18 + x_20 + x_24 + x_25 + x_34 <= 1
- Constraint `26`: x_5 + x_13 + x_27 + x_28 + x_37 + x_38 + x_60 <= 1
- Constraint `27`: x_17 + x_27 + x_41 + x_46 + x_52 <= 1
- Constraint `28`: x_5 + x_23 + x_28 + x_41 + x_44 + x_58 <= 1
- Constraint `29`: x_1 + x_10 + x_12 + x_13 + x_30 + x_36 + x_48 <= 1
- Constraint `30`: x_1 + x_6 + x_13 + x_26 + x_40 + x_46 + x_47 + x_48 + x_55 <= 1
- Constraint `31`: x_19 + x_20 + x_21 + x_30 + x_34 + x_44 <= 1
- Constraint `32`: x_4 + x_10 + x_12 + x_30 + x_34 + x_35 + x_40 + x_49 + x_53 + x_57 <= 1
- Constraint `33`: x_14 + x_25 + x_38 + x_40 + x_41 + x_43 + x_49 + x_53 + x_58 <= 1
- Constraint `34`: x_26 + x_34 + x_38 + x_39 + x_41 + x_52 + x_57 <= 1
- Constraint `35`: x_10 + x_21 + x_27 + x_34 + x_44 + x_46 + x_49 + x_59 <= 1
- Constraint `36`: x_2 + x_13 + x_19 + x_20 + x_22 + x_27 + x_30 + x_31 + x_48 <= 1
- Constraint `37`: x_1 + x_4 + x_8 + x_20 + x_31 + x_32 + x_33 + x_40 + x_42 + x_53 <= 1
- Constraint `38`: x_12 + x_16 + x_26 + x_28 + x_52 <= 1
- Constraint `39`: x_15 + x_17 + x_25 + x_30 + x_38 + x_39 + x_46 + x_49 + x_51 <= 1
- Constraint `40`: x_4 + x_9 + x_24 + x_25 + x_31 + x_42 + x_51 + x_54 <= 1
- Constraint `41`: x_10 + x_19 + x_21 + x_25 + x_30 + x_40 + x_46 <= 1
- Constraint `42`: x_7 + x_15 + x_32 + x_36 + x_48 <= 1
- Constraint `43`: x_2 + x_27 + x_34 + x_35 + x_50 <= 1
- Constraint `44`: x_5 + x_6 + x_7 + x_22 + x_25 + x_28 + x_36 + x_46 + x_50 + x_57 <= 1
- Constraint `45`: x_3 + x_17 + x_23 + x_45 + x_47 + x_59 <= 1
- Constraint `46`: x_5 + x_10 + x_17 + x_37 + x_41 + x_54 <= 1
- Constraint `47`: x_4 + x_19 + x_21 + x_27 + x_37 + x_38 <= 1
- Constraint `48`: x_12 + x_17 + x_22 + x_29 + x_46 + x_47 + x_53 + x_56 <= 1
- Constraint `49`: x_3 + x_5 + x_7 + x_21 + x_23 + x_31 + x_37 + x_46 <= 1
- Constraint `50`: x_3 + x_8 + x_11 + x_12 + x_15 + x_18 + x_33 + x_50 + x_52 + x_57 <= 1
- Constraint `51`: x_5 + x_10 + x_13 + x_15 + x_16 + x_36 + x_40 + x_54 + x_56 <= 1
- Constraint `52`: x_12 + x_13 + x_38 + x_40 + x_44 + x_52 <= 1
- Constraint `53`: x_11 + x_18 + x_25 + x_30 + x_39 + x_41 + x_56 + x_57 + x_58 + x_60 <= 1
- Constraint `54`: x_1 + x_12 + x_14 + x_16 + x_32 + x_59 <= 1
- Constraint `55`: x_1 + x_8 + x_18 + x_42 + x_48 <= 1
- Constraint `56`: x_5 + x_16 + x_18 + x_36 + x_40 + x_44 + x_48 + x_54 <= 1
- Constraint `57`: x_3 + x_24 + x_28 + x_29 + x_34 + x_57 <= 1
- Constraint `58`: x_17 + x_29 + x_37 + x_42 + x_48 + x_49 <= 1
- Constraint `59`: x_10 + x_15 + x_21 + x_26 + x_28 + x_29 + x_39 + x_45 + x_48 + x_59 <= 1
- Constraint `60`: x_1 + x_4 + x_5 + x_6 + x_23 + x_41 + x_45 + x_52 <= 1
- Constraint `61`: x_29 + x_31 + x_48 + x_51 + x_53 <= 1
- Constraint `62`: x_11 + x_14 + x_16 + x_22 + x_24 + x_33 + x_53 + x_54 <= 1
- Constraint `63`: x_1 + x_7 + x_12 + x_17 + x_26 + x_29 + x_38 + x_44 + x_46 <= 1
- Constraint `64`: x_4 + x_9 + x_24 + x_26 + x_32 + x_33 + x_37 + x_41 + x_43 + x_59 <= 1
- Constraint `65`: x_2 + x_5 + x_8 + x_14 + x_23 + x_33 + x_37 + x_40 + x_41 + x_53 <= 1
- Constraint `66`: x_3 + x_4 + x_11 + x_13 + x_21 + x_29 + x_38 + x_43 + x_50 + x_60 <= 1
- Constraint `67`: x_18 + x_27 + x_54 + x_56 + x_57 <= 1
- Constraint `68`: x_10 + x_15 + x_17 + x_36 + x_40 + x_41 + x_45 + x_49 + x_52 + x_54 <= 1
- Constraint `69`: x_2 + x_7 + x_14 + x_24 + x_39 + x_41 + x_45 <= 1
- Constraint `70`: x_11 + x_25 + x_30 + x_32 + x_37 + x_51 + x_52 + x_57 <= 1
- Constraint `71`: x_8 + x_34 + x_48 + x_55 + x_57 + x_59 <= 1
- Constraint `72`: x_23 + x_26 + x_30 + x_32 + x_37 <= 1
- Constraint `73`: x_3 + x_8 + x_9 + x_30 + x_33 + x_38 + x_56 + x_57 + x_60 <= 1
- Constraint `74`: x_6 + x_15 + x_17 + x_27 + x_37 + x_44 <= 1
- Constraint `75`: x_1 + x_3 + x_11 + x_15 + x_44 + x_50 <= 1
- Constraint `76`: x_2 + x_14 + x_22 + x_24 + x_39 + x_40 + x_56 <= 1
- Constraint `77`: x_2 + x_11 + x_12 + x_14 + x_24 + x_30 + x_41 + x_60 <= 1
- Constraint `78`: x_13 + x_30 + x_46 + x_48 + x_50 + x_51 + x_53 <= 1
- Constraint `79`: x_1 + x_6 + x_17 + x_26 + x_31 + x_41 + x_55 <= 1
- Constraint `80`: x_7 + x_12 + x_19 + x_26 + x_45 + x_48 + x_53 <= 1
- Constraint `81`: x_17 + x_19 + x_21 + x_25 + x_32 + x_53 <= 1
- Constraint `82`: x_2 + x_14 + x_26 + x_33 + x_41 + x_49 + x_51 + x_54 <= 1
- Constraint `83`: x_8 + x_18 + x_21 + x_24 + x_25 + x_33 + x_47 + x_48 + x_54 + x_58 <= 1
- Constraint `84`: x_1 + x_3 + x_17 + x_19 + x_32 + x_49 + x_53 + x_59 + x_60 <= 1
- Constraint `85`: x_4 + x_13 + x_18 + x_19 + x_24 + x_26 + x_32 + x_39 + x_53 + x_59 <= 1
- Constraint `86`: x_3 + x_10 + x_15 + x_22 + x_32 + x_46 <= 1
- Constraint `87`: x_2 + x_5 + x_8 + x_18 + x_19 + x_22 + x_23 + x_47 + x_55 <= 1
- Constraint `88`: x_9 + x_11 + x_27 + x_43 + x_51 + x_54 <= 1
- Constraint `89`: x_3 + x_7 + x_17 + x_22 + x_28 + x_35 + x_36 + x_46 + x_51 + x_59 <= 1
- Constraint `90`: x_5 + x_9 + x_15 + x_35 + x_44 + x_50 <= 1
- Constraint `91`: x_2 + x_7 + x_10 + x_14 + x_15 + x_25 + x_35 + x_36 + x_37 + x_42 <= 1
- Constraint `92`: x_1 + x_3 + x_9 + x_14 + x_31 + x_41 <= 1
- Constraint `93`: x_12 + x_19 + x_35 + x_49 + x_59 <= 1
- Constraint `94`: x_8 + x_16 + x_22 + x_26 + x_36 + x_40 + x_43 + x_53 + x_55 <= 1
- Constraint `95`: x_5 + x_7 + x_10 + x_12 + x_19 + x_20 + x_41 + x_44 + x_60 <= 1
- Constraint `96`: x_15 + x_21 + x_24 + x_28 + x_32 + x_38 + x_44 + x_54 + x_56 <= 1
- Constraint `97`: x_3 + x_8 + x_11 + x_16 + x_24 + x_30 + x_36 + x_39 + x_44 + x_56 <= 1
- Constraint `98`: x_16 + x_23 + x_27 + x_33 + x_34 + x_35 + x_40 + x_48 + x_50 <= 1
- Constraint `99`: x_14 + x_26 + x_28 + x_47 + x_51 <= 1
- Constraint `100`: x_11 + x_17 + x_18 + x_20 + x_26 + x_51 + x_55 + x_60 <= 1
- Constraint `101`: x_14 + x_29 + x_35 + x_56 + x_57 <= 1
- Constraint `102`: x_2 + x_16 + x_25 + x_38 + x_45 + x_47 + x_48 <= 1
- Constraint `103`: x_10 + x_26 + x_37 + x_40 + x_41 + x_43 + x_52 <= 1
- Constraint `104`: x_6 + x_23 + x_30 + x_38 + x_41 + x_47 <= 1
- Constraint `105`: x_1 + x_5 + x_7 + x_24 + x_27 + x_45 + x_59 <= 1
- Constraint `106`: x_3 + x_25 + x_43 + x_46 + x_52 + x_55 + x_58 <= 1
- Constraint `107`: x_4 + x_10 + x_15 + x_17 + x_21 + x_34 + x_44 + x_45 + x_47 + x_59 <= 1
- Constraint `108`: x_3 + x_4 + x_5 + x_21 + x_29 + x_33 + x_37 + x_38 + x_46 + x_52 <= 1
- Constraint `109`: x_3 + x_4 + x_7 + x_15 + x_22 + x_31 + x_42 + x_48 + x_58 <= 1
- Constraint `110`: x_17 + x_26 + x_35 + x_37 + x_42 + x_50 + x_55 + x_60 <= 1
- Constraint `111`: x_7 + x_18 + x_25 + x_27 + x_47 + x_50 + x_51 + x_52 <= 1
- Constraint `112`: x_2 + x_7 + x_9 + x_15 + x_39 + x_43 + x_46 + x_49 <= 1
- Constraint `113`: x_1 + x_27 + x_33 + x_36 + x_43 + x_57 + x_60 <= 1
- Constraint `114`: x_20 + x_34 + x_41 + x_42 + x_43 <= 1
- Constraint `115`: x_8 + x_15 + x_19 + x_20 + x_22 + x_24 + x_30 + x_53 + x_60 <= 1
- Constraint `116`: x_4 + x_8 + x_10 + x_11 + x_29 + x_34 + x_35 + x_51 + x_59 <= 1
- Constraint `117`: x_3 + x_8 + x_11 + x_19 + x_38 + x_53 + x_60 <= 1
- Constraint `118`: x_3 + x_10 + x_39 + x_52 + x_53 + x_55 + x_58 <= 1
- Constraint `119`: x_4 + x_7 + x_13 + x_14 + x_15 + x_24 + x_36 + x_50 + x_55 <= 1
- Constraint `120`: x_3 + x_4 + x_12 + x_25 + x_29 + x_36 + x_39 + x_41 + x_53 + x_58 <= 1
