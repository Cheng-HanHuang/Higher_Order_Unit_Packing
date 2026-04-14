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

w_1=1.3351946, w_2=0.76634462, w_3=1.5116311, w_4=1.0968535, w_5=1.3406986, w_6=1.6992547, w_7=1.1898324, w_8=1.3382226, w_9=0.92294071, w_10=1.4473833, w_11=0.59916173, w_12=0.50038351, w_13=1.446609, w_14=1.8924722, w_15=1.7428931, w_16=0.98550954, w_17=1.4482782, w_18=1.6007321, w_19=0.76402139, w_20=0.53965012, w_21=1.2307885, w_22=1.224393, w_23=1.5802474, w_24=0.58225937, w_25=1.9543893, w_26=0.98167052, w_27=0.64482114, w_28=0.83582518, w_29=1.9775468, w_30=1.5719691, w_31=1.2195979, w_32=1.8048141, w_33=1.1467299, w_34=0.5050496, w_35=1.4904228, w_36=0.60790337, w_37=1.7668862, w_38=1.4478737, w_39=1.6595718, w_40=0.83555945, w_41=1.4772811, w_42=0.85963471, w_43=1.9784019, w_44=1.5981504, w_45=1.2978121, w_46=1.2703077, w_47=0.63116521, w_48=1.7464269, w_49=1.8218462, w_50=0.64714247, w_51=1.5854171, w_52=0.97231478, w_53=0.52938889, w_54=1.1749906, w_55=1.9757611, w_56=1.656107, w_57=1.1828771, w_58=1.614798, w_59=1.251366, w_60=1.3861781

## Exact constraints

- Constraint `1`: x_7 + x_8 + x_9 + x_18 + x_36 + x_37 + x_41 + x_46 + x_50 + x_51 <= 8
- Constraint `2`: x_2 + x_6 + x_7 + x_14 + x_23 + x_27 + x_28 + x_49 + x_56 + x_59 <= 2
- Constraint `3`: x_5 + x_8 + x_11 + x_12 + x_13 + x_15 + x_43 + x_51 + x_52 + x_57 <= 3
- Constraint `4`: x_5 + x_8 + x_18 + x_28 + x_46 + x_53 + x_57 <= 2
- Constraint `5`: x_9 + x_14 + x_23 + x_37 + x_41 + x_60 <= 4
- Constraint `6`: x_1 + x_7 + x_8 + x_11 + x_21 + x_43 <= 4
- Constraint `7`: x_4 + x_11 + x_25 + x_31 + x_34 + x_39 <= 3
- Constraint `8`: x_23 + x_24 + x_26 + x_27 + x_31 + x_34 + x_41 + x_46 + x_56 + x_57 <= 5
- Constraint `9`: x_23 + x_25 + x_27 + x_32 + x_38 + x_46 + x_53 + x_54 <= 2
- Constraint `10`: x_14 + x_18 + x_20 + x_21 + x_29 + x_55 <= 1
- Constraint `11`: x_6 + x_25 + x_32 + x_33 + x_37 + x_38 + x_41 + x_58 <= 6
- Constraint `12`: x_13 + x_39 + x_42 + x_59 + x_60 <= 2
- Constraint `13`: x_5 + x_8 + x_12 + x_14 + x_16 + x_20 + x_31 + x_36 + x_42 <= 8
- Constraint `14`: x_2 + x_6 + x_9 + x_10 + x_16 + x_24 + x_25 + x_39 + x_46 <= 3
- Constraint `15`: x_2 + x_41 + x_45 + x_47 + x_56 + x_57 <= 2
- Constraint `16`: x_1 + x_12 + x_32 + x_33 + x_41 + x_46 + x_47 + x_55 + x_59 <= 7
- Constraint `17`: x_4 + x_5 + x_7 + x_34 + x_35 + x_52 + x_56 + x_58 <= 3
- Constraint `18`: x_5 + x_18 + x_26 + x_33 + x_37 + x_52 + x_58 <= 5
- Constraint `19`: x_9 + x_18 + x_27 + x_41 + x_44 + x_50 <= 4
- Constraint `20`: x_11 + x_12 + x_14 + x_49 + x_56 <= 4
- Constraint `21`: x_13 + x_24 + x_30 + x_38 + x_51 + x_59 <= 4
- Constraint `22`: x_17 + x_19 + x_22 + x_23 + x_36 + x_43 + x_53 <= 5
- Constraint `23`: x_4 + x_33 + x_39 + x_45 + x_46 <= 4
- Constraint `24`: x_5 + x_7 + x_23 + x_29 + x_35 + x_37 + x_42 <= 2
- Constraint `25`: x_13 + x_20 + x_27 + x_28 + x_39 + x_40 + x_43 + x_53 + x_54 + x_58 <= 3
- Constraint `26`: x_17 + x_22 + x_28 + x_34 + x_47 + x_49 + x_52 + x_55 <= 5
- Constraint `27`: x_4 + x_6 + x_14 + x_17 + x_23 + x_26 + x_31 + x_45 + x_50 <= 5
- Constraint `28`: x_9 + x_12 + x_15 + x_31 + x_35 + x_37 + x_50 + x_55 + x_57 <= 7
- Constraint `29`: x_1 + x_3 + x_4 + x_5 + x_41 + x_46 + x_47 + x_58 <= 3
- Constraint `30`: x_1 + x_11 + x_21 + x_27 + x_39 + x_42 <= 3
- Constraint `31`: x_10 + x_13 + x_24 + x_25 + x_27 + x_31 + x_43 + x_48 <= 7
- Constraint `32`: x_17 + x_21 + x_32 + x_45 + x_50 + x_59 <= 4
- Constraint `33`: x_2 + x_9 + x_10 + x_30 + x_31 + x_32 + x_42 + x_51 + x_58 + x_59 <= 3
- Constraint `34`: x_7 + x_8 + x_9 + x_12 + x_18 + x_22 + x_28 + x_31 + x_45 + x_48 <= 6
- Constraint `35`: x_7 + x_45 + x_47 + x_52 + x_56 + x_59 <= 4
- Constraint `36`: x_2 + x_14 + x_33 + x_35 + x_36 + x_50 + x_52 + x_54 <= 7
- Constraint `37`: x_2 + x_7 + x_14 + x_16 + x_22 + x_24 + x_25 + x_29 + x_41 + x_58 <= 9
- Constraint `38`: x_2 + x_6 + x_12 + x_17 + x_20 + x_31 + x_34 + x_55 <= 2
- Constraint `39`: x_1 + x_7 + x_23 + x_35 + x_42 + x_54 <= 3
- Constraint `40`: x_5 + x_7 + x_12 + x_21 + x_49 + x_50 + x_57 <= 3
- Constraint `41`: x_10 + x_17 + x_24 + x_32 + x_37 + x_49 + x_55 + x_59 + x_60 <= 1
- Constraint `42`: x_17 + x_21 + x_37 + x_39 + x_59 <= 1
- Constraint `43`: x_4 + x_17 + x_23 + x_28 + x_36 + x_38 + x_56 + x_57 + x_58 <= 8
- Constraint `44`: x_1 + x_3 + x_19 + x_22 + x_38 + x_46 + x_54 <= 5
- Constraint `45`: x_3 + x_9 + x_10 + x_11 + x_18 + x_23 + x_36 + x_43 + x_57 <= 3
- Constraint `46`: x_1 + x_39 + x_40 + x_41 + x_44 <= 1
- Constraint `47`: x_17 + x_20 + x_22 + x_25 + x_28 + x_40 + x_45 + x_46 + x_51 <= 8
- Constraint `48`: x_15 + x_18 + x_19 + x_40 + x_46 + x_49 + x_54 + x_58 + x_59 <= 7
- Constraint `49`: x_1 + x_2 + x_12 + x_31 + x_33 + x_47 + x_48 <= 6
- Constraint `50`: x_2 + x_23 + x_33 + x_38 + x_42 + x_47 + x_53 + x_55 <= 2
- Constraint `51`: x_25 + x_46 + x_50 + x_56 + x_59 <= 4
- Constraint `52`: x_6 + x_8 + x_11 + x_22 + x_23 + x_37 + x_38 + x_43 + x_54 + x_56 <= 7
- Constraint `53`: x_2 + x_3 + x_11 + x_12 + x_16 + x_23 + x_31 + x_43 + x_59 <= 3
- Constraint `54`: x_3 + x_7 + x_16 + x_18 + x_19 + x_22 + x_30 + x_48 <= 7
- Constraint `55`: x_2 + x_36 + x_48 + x_52 + x_57 + x_58 + x_60 <= 6
- Constraint `56`: x_1 + x_5 + x_6 + x_9 + x_11 + x_28 + x_29 + x_38 + x_46 + x_58 <= 3
- Constraint `57`: x_4 + x_10 + x_11 + x_23 + x_57 + x_59 <= 2
- Constraint `58`: x_1 + x_2 + x_19 + x_24 + x_30 + x_33 + x_43 + x_52 <= 6
- Constraint `59`: x_5 + x_9 + x_11 + x_12 + x_21 + x_46 + x_48 + x_50 <= 5
- Constraint `60`: x_11 + x_13 + x_14 + x_19 + x_26 + x_32 + x_35 + x_36 + x_44 <= 2
- Constraint `61`: x_3 + x_15 + x_25 + x_27 + x_31 + x_36 + x_43 + x_51 <= 7
- Constraint `62`: x_3 + x_9 + x_10 + x_11 + x_18 + x_41 + x_49 + x_51 + x_52 + x_58 <= 5
- Constraint `63`: x_8 + x_9 + x_13 + x_15 + x_23 + x_29 + x_39 + x_40 + x_54 + x_58 <= 7
- Constraint `64`: x_2 + x_3 + x_5 + x_23 + x_58 <= 1
- Constraint `65`: x_4 + x_12 + x_17 + x_25 + x_48 <= 3
- Constraint `66`: x_2 + x_11 + x_15 + x_21 + x_34 + x_38 + x_50 <= 1
- Constraint `67`: x_4 + x_11 + x_31 + x_32 + x_37 + x_38 + x_39 + x_46 + x_50 + x_56 <= 2
- Constraint `68`: x_11 + x_21 + x_27 + x_34 + x_37 + x_38 + x_51 + x_58 + x_60 <= 2
- Constraint `69`: x_13 + x_26 + x_28 + x_42 + x_47 + x_52 <= 2
- Constraint `70`: x_6 + x_11 + x_25 + x_37 + x_41 + x_44 + x_45 + x_57 <= 4
- Constraint `71`: x_3 + x_9 + x_11 + x_14 + x_24 + x_26 + x_36 + x_46 + x_49 <= 4
- Constraint `72`: x_4 + x_9 + x_20 + x_22 + x_37 + x_45 + x_48 + x_50 + x_54 + x_56 <= 1
- Constraint `73`: x_8 + x_11 + x_14 + x_21 + x_40 + x_43 + x_52 + x_60 <= 4
- Constraint `74`: x_9 + x_23 + x_25 + x_28 + x_31 + x_33 + x_37 + x_41 + x_46 + x_60 <= 9
- Constraint `75`: x_7 + x_19 + x_37 + x_43 + x_47 <= 2
- Constraint `76`: x_3 + x_8 + x_11 + x_13 + x_43 + x_44 + x_46 <= 6
- Constraint `77`: x_13 + x_19 + x_25 + x_32 + x_43 + x_53 <= 2
- Constraint `78`: x_22 + x_26 + x_32 + x_35 + x_44 + x_48 + x_52 + x_54 + x_60 <= 5
- Constraint `79`: x_8 + x_10 + x_21 + x_43 + x_44 + x_53 <= 5
- Constraint `80`: x_23 + x_25 + x_26 + x_29 + x_55 <= 1
- Constraint `81`: x_2 + x_10 + x_12 + x_23 + x_25 + x_27 + x_33 + x_38 + x_41 + x_42 <= 9
- Constraint `82`: x_6 + x_13 + x_21 + x_36 + x_43 + x_52 + x_57 <= 4
- Constraint `83`: x_3 + x_9 + x_11 + x_16 + x_21 + x_46 + x_49 <= 4
- Constraint `84`: x_1 + x_4 + x_7 + x_26 + x_38 + x_41 + x_42 + x_49 + x_54 + x_56 <= 3
- Constraint `85`: x_3 + x_6 + x_9 + x_49 + x_50 + x_56 <= 4
- Constraint `86`: x_4 + x_6 + x_20 + x_29 + x_30 + x_32 + x_33 + x_35 + x_39 + x_49 <= 5
- Constraint `87`: x_18 + x_22 + x_37 + x_47 + x_48 <= 2
- Constraint `88`: x_6 + x_9 + x_14 + x_26 + x_33 + x_55 <= 2
- Constraint `89`: x_25 + x_31 + x_35 + x_37 + x_38 + x_40 + x_43 + x_46 <= 7
- Constraint `90`: x_1 + x_9 + x_12 + x_39 + x_40 + x_48 <= 4
- Constraint `91`: x_1 + x_9 + x_28 + x_41 + x_42 + x_48 + x_54 <= 5
- Constraint `92`: x_9 + x_11 + x_14 + x_15 + x_19 <= 1
- Constraint `93`: x_2 + x_23 + x_31 + x_44 + x_45 + x_57 <= 5
- Constraint `94`: x_5 + x_9 + x_15 + x_23 + x_26 + x_37 + x_39 + x_58 <= 3
- Constraint `95`: x_18 + x_20 + x_37 + x_43 + x_45 + x_56 + x_60 <= 4
- Constraint `96`: x_8 + x_9 + x_25 + x_37 + x_49 <= 4
- Constraint `97`: x_14 + x_23 + x_35 + x_37 + x_39 + x_41 <= 3
- Constraint `98`: x_10 + x_11 + x_15 + x_17 + x_19 + x_39 + x_41 + x_43 + x_48 + x_59 <= 7
- Constraint `99`: x_11 + x_16 + x_27 + x_54 + x_55 <= 4
- Constraint `100`: x_6 + x_29 + x_31 + x_33 + x_43 + x_53 + x_57 + x_58 + x_59 <= 6
- Constraint `101`: x_2 + x_11 + x_13 + x_42 + x_43 <= 4
- Constraint `102`: x_5 + x_11 + x_20 + x_30 + x_35 + x_36 + x_38 + x_53 + x_56 + x_57 <= 7
- Constraint `103`: x_4 + x_5 + x_14 + x_20 + x_21 + x_22 + x_49 + x_51 + x_55 + x_57 <= 4
- Constraint `104`: x_10 + x_11 + x_28 + x_40 + x_42 + x_43 <= 2
- Constraint `105`: x_2 + x_8 + x_11 + x_23 + x_27 + x_30 + x_31 + x_34 + x_43 + x_53 <= 7
- Constraint `106`: x_14 + x_16 + x_26 + x_29 + x_32 + x_34 + x_37 + x_41 + x_48 + x_54 <= 4
- Constraint `107`: x_13 + x_14 + x_18 + x_21 + x_35 + x_49 <= 2
- Constraint `108`: x_2 + x_9 + x_10 + x_19 + x_22 + x_27 + x_29 + x_51 <= 5
- Constraint `109`: x_3 + x_8 + x_11 + x_38 + x_53 + x_55 <= 5
- Constraint `110`: x_2 + x_6 + x_13 + x_19 + x_22 + x_35 + x_40 + x_46 <= 6
- Constraint `111`: x_6 + x_9 + x_21 + x_23 + x_34 + x_44 + x_46 + x_49 + x_53 + x_60 <= 6
- Constraint `112`: x_6 + x_9 + x_17 + x_19 + x_45 + x_58 <= 2
- Constraint `113`: x_9 + x_11 + x_15 + x_28 + x_30 + x_39 + x_56 + x_57 + x_59 + x_60 <= 3
- Constraint `114`: x_3 + x_17 + x_19 + x_33 + x_34 + x_44 + x_48 + x_51 + x_54 <= 4
- Constraint `115`: x_20 + x_34 + x_36 + x_38 + x_39 + x_47 + x_48 + x_52 + x_54 + x_58 <= 2
- Constraint `116`: x_7 + x_19 + x_35 + x_38 + x_44 + x_51 <= 1
- Constraint `117`: x_7 + x_10 + x_23 + x_27 + x_37 + x_42 + x_45 + x_52 + x_58 <= 7
- Constraint `118`: x_2 + x_3 + x_11 + x_16 + x_19 + x_22 + x_27 + x_28 + x_55 <= 6
- Constraint `119`: x_4 + x_11 + x_12 + x_29 + x_33 + x_40 + x_45 + x_49 + x_58 <= 7
- Constraint `120`: x_16 + x_17 + x_22 + x_42 + x_49 <= 4
