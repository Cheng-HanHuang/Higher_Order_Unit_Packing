# Original problem: random_unit_n80_m160_tight

This file records the exact original binary packing problem used for the matching run result.

## Optimization model

\[
\max_{x\in\{0,1\}^n}\ \sum_{i=1}^n w_i x_i
\qquad\text{s.t.}\qquad
\sum_{i\in S_k} x_i \le B_k,\quad k=1,\dots,m.
\]

- Number of variables: `80`
- Number of constraints: `160`
- Matching run-result file: `result.json`

## Metadata

- `generator`: `random_unit_packing`
- `row_size_range`: `[5, 10]`
- `capacity_mode`: `tight`

## Weights

w_1=0.60442153, w_2=0.82332425, w_3=0.57350626, w_4=0.97342949, w_5=0.55967522, w_6=0.58462218, w_7=1.2606611, w_8=1.6181209, w_9=1.2622091, w_10=1.2150105, w_11=1.6920201, w_12=1.7982114, w_13=1.1960303, w_14=1.2172707, w_15=1.5119231, w_16=0.68781598, w_17=1.6274496, w_18=1.5725059, w_19=1.6600389, w_20=0.79035078, w_21=1.8567338, w_22=1.9784407, w_23=1.4303758, w_24=0.78997929, w_25=1.5823633, w_26=0.70553976, w_27=0.54025606, w_28=1.4238868, w_29=1.6212163, w_30=1.8785216, w_31=1.4454465, w_32=1.7618999, w_33=0.68205953, w_34=1.574341, w_35=0.6329687, w_36=0.78739239, w_37=0.90872546, w_38=1.3107693, w_39=0.89678088, w_40=1.15316, w_41=0.70830688, w_42=0.99259807, w_43=0.53919237, w_44=1.6136689, w_45=1.8601722, w_46=1.2062478, w_47=1.5953733, w_48=0.92509296, w_49=1.9217317, w_50=1.0577609, w_51=0.7512373, w_52=1.6900283, w_53=1.5499348, w_54=1.8046987, w_55=1.0694314, w_56=0.6549336, w_57=1.9620976, w_58=0.54131388, w_59=0.51328981, w_60=1.8544749, w_61=1.150225, w_62=0.53809079, w_63=1.5379459, w_64=0.92963335, w_65=1.8852639, w_66=0.90837172, w_67=1.2681335, w_68=1.5863392, w_69=0.71800318, w_70=1.1321958, w_71=1.6137792, w_72=1.6892298, w_73=0.80613467, w_74=1.6109764, w_75=1.3085081, w_76=0.62610723, w_77=0.85551943, w_78=1.4488972, w_79=1.4134647, w_80=1.7707642

## Exact constraints

- Constraint `1`: x_1 + x_17 + x_22 + x_37 + x_53 + x_57 + x_66 <= 6
- Constraint `2`: x_8 + x_11 + x_18 + x_28 + x_42 + x_52 + x_54 <= 6
- Constraint `3`: x_16 + x_22 + x_40 + x_43 + x_61 + x_67 <= 5
- Constraint `4`: x_14 + x_28 + x_29 + x_63 + x_71 <= 4
- Constraint `5`: x_5 + x_11 + x_18 + x_21 + x_22 + x_23 + x_29 + x_59 + x_75 + x_78 <= 9
- Constraint `6`: x_6 + x_29 + x_40 + x_60 + x_72 <= 4
- Constraint `7`: x_4 + x_14 + x_23 + x_41 + x_58 <= 4
- Constraint `8`: x_5 + x_20 + x_28 + x_67 + x_70 <= 4
- Constraint `9`: x_6 + x_16 + x_19 + x_36 + x_37 + x_77 + x_80 <= 6
- Constraint `10`: x_1 + x_15 + x_19 + x_23 + x_33 + x_46 + x_51 + x_62 + x_63 <= 8
- Constraint `11`: x_7 + x_8 + x_12 + x_51 + x_67 + x_68 + x_80 <= 6
- Constraint `12`: x_7 + x_14 + x_18 + x_24 + x_32 + x_36 + x_46 + x_60 + x_62 + x_67 <= 9
- Constraint `13`: x_5 + x_15 + x_21 + x_36 + x_40 <= 4
- Constraint `14`: x_20 + x_27 + x_37 + x_38 + x_41 + x_43 + x_46 + x_53 + x_64 <= 8
- Constraint `15`: x_14 + x_22 + x_33 + x_43 + x_47 + x_50 + x_53 + x_56 + x_71 + x_75 <= 9
- Constraint `16`: x_4 + x_20 + x_21 + x_26 + x_30 + x_47 + x_49 + x_55 + x_67 <= 8
- Constraint `17`: x_22 + x_32 + x_36 + x_44 + x_47 + x_49 + x_65 + x_66 <= 7
- Constraint `18`: x_5 + x_42 + x_43 + x_61 + x_69 <= 4
- Constraint `19`: x_2 + x_11 + x_45 + x_68 + x_75 <= 4
- Constraint `20`: x_17 + x_20 + x_21 + x_26 + x_41 + x_43 <= 5
- Constraint `21`: x_4 + x_10 + x_19 + x_40 + x_49 + x_59 + x_70 + x_72 <= 7
- Constraint `22`: x_4 + x_10 + x_49 + x_51 + x_70 <= 4
- Constraint `23`: x_10 + x_20 + x_37 + x_41 + x_47 + x_59 + x_64 + x_65 + x_74 <= 8
- Constraint `24`: x_23 + x_40 + x_68 + x_70 + x_80 <= 4
- Constraint `25`: x_5 + x_6 + x_26 + x_46 + x_48 + x_63 + x_64 + x_78 + x_80 <= 8
- Constraint `26`: x_11 + x_14 + x_24 + x_28 + x_30 + x_54 + x_55 + x_75 <= 7
- Constraint `27`: x_2 + x_5 + x_21 + x_23 + x_28 + x_32 + x_41 + x_54 + x_56 + x_59 <= 9
- Constraint `28`: x_11 + x_16 + x_20 + x_27 + x_33 + x_56 + x_67 + x_68 + x_77 <= 8
- Constraint `29`: x_40 + x_43 + x_59 + x_65 + x_66 + x_70 + x_79 <= 6
- Constraint `30`: x_2 + x_11 + x_12 + x_37 + x_43 + x_52 + x_55 + x_74 <= 7
- Constraint `31`: x_7 + x_16 + x_39 + x_51 + x_64 + x_77 <= 5
- Constraint `32`: x_10 + x_29 + x_40 + x_42 + x_69 + x_71 <= 5
- Constraint `33`: x_10 + x_20 + x_31 + x_43 + x_47 + x_51 + x_66 <= 6
- Constraint `34`: x_10 + x_14 + x_19 + x_21 + x_30 + x_32 + x_67 + x_78 <= 7
- Constraint `35`: x_34 + x_52 + x_55 + x_56 + x_72 + x_79 <= 5
- Constraint `36`: x_1 + x_4 + x_31 + x_39 + x_63 + x_80 <= 5
- Constraint `37`: x_1 + x_3 + x_41 + x_57 + x_62 + x_71 <= 5
- Constraint `38`: x_2 + x_6 + x_10 + x_43 + x_50 + x_60 <= 5
- Constraint `39`: x_6 + x_18 + x_25 + x_41 + x_43 + x_47 + x_68 + x_69 <= 7
- Constraint `40`: x_13 + x_27 + x_29 + x_30 + x_39 + x_42 + x_62 + x_66 <= 7
- Constraint `41`: x_2 + x_19 + x_32 + x_35 + x_50 + x_72 <= 5
- Constraint `42`: x_14 + x_30 + x_38 + x_42 + x_49 + x_50 + x_72 + x_74 <= 7
- Constraint `43`: x_10 + x_12 + x_15 + x_39 + x_47 + x_49 + x_53 + x_64 <= 7
- Constraint `44`: x_7 + x_10 + x_36 + x_40 + x_47 + x_57 + x_58 + x_79 <= 7
- Constraint `45`: x_14 + x_24 + x_34 + x_35 + x_39 + x_42 + x_44 + x_59 + x_73 + x_76 <= 9
- Constraint `46`: x_3 + x_28 + x_30 + x_31 + x_33 + x_38 + x_41 + x_54 + x_58 + x_65 <= 9
- Constraint `47`: x_13 + x_20 + x_23 + x_24 + x_27 + x_52 + x_59 + x_80 <= 7
- Constraint `48`: x_8 + x_21 + x_22 + x_26 + x_42 + x_58 <= 5
- Constraint `49`: x_13 + x_22 + x_28 + x_54 + x_62 + x_67 <= 5
- Constraint `50`: x_1 + x_14 + x_15 + x_22 + x_42 + x_46 + x_47 + x_59 <= 7
- Constraint `51`: x_10 + x_18 + x_19 + x_21 + x_37 + x_43 + x_46 + x_49 + x_61 + x_67 <= 9
- Constraint `52`: x_5 + x_20 + x_35 + x_41 + x_44 + x_57 + x_60 + x_61 + x_63 <= 8
- Constraint `53`: x_22 + x_44 + x_45 + x_46 + x_54 <= 4
- Constraint `54`: x_2 + x_19 + x_29 + x_42 + x_54 + x_66 <= 5
- Constraint `55`: x_1 + x_14 + x_40 + x_60 + x_62 + x_76 <= 5
- Constraint `56`: x_9 + x_21 + x_26 + x_52 + x_54 + x_64 + x_68 + x_76 + x_80 <= 8
- Constraint `57`: x_5 + x_23 + x_32 + x_45 + x_46 + x_52 + x_55 + x_62 + x_65 + x_74 <= 9
- Constraint `58`: x_3 + x_7 + x_44 + x_47 + x_62 + x_71 <= 5
- Constraint `59`: x_4 + x_5 + x_41 + x_53 + x_63 + x_67 + x_79 <= 6
- Constraint `60`: x_31 + x_44 + x_49 + x_54 + x_56 <= 4
- Constraint `61`: x_3 + x_14 + x_21 + x_47 + x_75 <= 4
- Constraint `62`: x_3 + x_8 + x_12 + x_14 + x_22 + x_28 + x_31 + x_49 + x_63 + x_72 <= 9
- Constraint `63`: x_33 + x_35 + x_54 + x_59 + x_63 + x_65 + x_71 + x_75 <= 7
- Constraint `64`: x_13 + x_38 + x_39 + x_55 + x_58 + x_59 + x_65 + x_67 + x_69 + x_78 <= 9
- Constraint `65`: x_5 + x_11 + x_15 + x_16 + x_19 + x_24 + x_52 + x_60 + x_68 + x_73 <= 9
- Constraint `66`: x_3 + x_9 + x_12 + x_18 + x_23 + x_26 + x_35 + x_45 + x_54 <= 8
- Constraint `67`: x_12 + x_15 + x_30 + x_41 + x_44 + x_49 + x_60 + x_61 + x_78 <= 8
- Constraint `68`: x_4 + x_28 + x_33 + x_37 + x_59 + x_67 + x_79 <= 6
- Constraint `69`: x_5 + x_13 + x_15 + x_18 + x_29 + x_30 + x_55 + x_60 + x_79 <= 8
- Constraint `70`: x_4 + x_24 + x_31 + x_33 + x_40 + x_72 <= 5
- Constraint `71`: x_4 + x_7 + x_14 + x_48 + x_55 + x_56 + x_62 + x_75 <= 7
- Constraint `72`: x_11 + x_30 + x_32 + x_42 + x_59 + x_62 + x_71 + x_74 <= 7
- Constraint `73`: x_9 + x_15 + x_22 + x_57 + x_61 <= 4
- Constraint `74`: x_1 + x_57 + x_64 + x_75 + x_80 <= 4
- Constraint `75`: x_30 + x_40 + x_46 + x_58 + x_65 + x_66 + x_77 + x_80 <= 7
- Constraint `76`: x_28 + x_29 + x_30 + x_56 + x_63 + x_64 + x_68 <= 6
- Constraint `77`: x_19 + x_30 + x_31 + x_35 + x_72 <= 4
- Constraint `78`: x_2 + x_8 + x_27 + x_31 + x_48 + x_50 + x_65 + x_75 <= 7
- Constraint `79`: x_18 + x_30 + x_31 + x_34 + x_49 + x_59 + x_60 + x_80 <= 7
- Constraint `80`: x_13 + x_16 + x_18 + x_28 + x_37 + x_47 + x_48 + x_77 <= 7
- Constraint `81`: x_16 + x_19 + x_21 + x_48 + x_53 + x_56 + x_77 <= 6
- Constraint `82`: x_7 + x_29 + x_49 + x_53 + x_61 + x_68 <= 5
- Constraint `83`: x_20 + x_24 + x_39 + x_47 + x_75 + x_77 <= 5
- Constraint `84`: x_9 + x_17 + x_24 + x_26 + x_36 + x_41 + x_63 + x_71 + x_73 <= 8
- Constraint `85`: x_1 + x_11 + x_40 + x_48 + x_55 + x_58 + x_61 + x_78 <= 7
- Constraint `86`: x_16 + x_17 + x_29 + x_38 + x_41 + x_59 <= 5
- Constraint `87`: x_42 + x_48 + x_49 + x_55 + x_59 + x_78 + x_80 <= 6
- Constraint `88`: x_15 + x_27 + x_48 + x_70 + x_71 + x_75 + x_78 <= 6
- Constraint `89`: x_1 + x_19 + x_31 + x_47 + x_55 + x_64 + x_66 + x_72 + x_74 + x_75 <= 9
- Constraint `90`: x_22 + x_27 + x_32 + x_41 + x_45 + x_49 + x_65 <= 6
- Constraint `91`: x_15 + x_21 + x_38 + x_46 + x_62 + x_70 + x_78 <= 6
- Constraint `92`: x_7 + x_43 + x_61 + x_71 + x_74 <= 4
- Constraint `93`: x_11 + x_20 + x_29 + x_32 + x_37 + x_46 + x_48 + x_50 + x_65 <= 8
- Constraint `94`: x_3 + x_40 + x_48 + x_55 + x_68 + x_75 + x_77 + x_79 <= 7
- Constraint `95`: x_23 + x_31 + x_51 + x_54 + x_60 + x_63 + x_79 <= 6
- Constraint `96`: x_5 + x_6 + x_16 + x_19 + x_42 + x_61 + x_63 + x_64 + x_65 + x_67 <= 9
- Constraint `97`: x_2 + x_4 + x_7 + x_28 + x_29 + x_34 + x_40 + x_52 + x_58 + x_65 <= 9
- Constraint `98`: x_3 + x_4 + x_20 + x_30 + x_32 + x_69 + x_79 <= 6
- Constraint `99`: x_1 + x_5 + x_6 + x_8 + x_15 + x_29 + x_43 + x_50 + x_57 + x_64 <= 9
- Constraint `100`: x_4 + x_9 + x_13 + x_23 + x_46 + x_54 + x_55 + x_56 + x_63 + x_78 <= 9
- Constraint `101`: x_1 + x_11 + x_19 + x_25 + x_41 + x_42 + x_49 + x_54 <= 7
- Constraint `102`: x_4 + x_5 + x_22 + x_23 + x_44 + x_47 + x_48 + x_65 + x_74 <= 8
- Constraint `103`: x_27 + x_32 + x_40 + x_48 + x_79 <= 4
- Constraint `104`: x_8 + x_12 + x_27 + x_46 + x_69 + x_73 + x_78 + x_80 <= 7
- Constraint `105`: x_1 + x_4 + x_20 + x_32 + x_33 + x_37 + x_64 + x_70 <= 7
- Constraint `106`: x_21 + x_28 + x_39 + x_57 + x_71 + x_77 + x_78 <= 6
- Constraint `107`: x_12 + x_20 + x_25 + x_49 + x_72 <= 4
- Constraint `108`: x_2 + x_8 + x_11 + x_13 + x_19 + x_37 + x_44 + x_52 + x_56 + x_58 <= 9
- Constraint `109`: x_7 + x_19 + x_24 + x_28 + x_44 + x_53 + x_75 + x_78 + x_79 <= 8
- Constraint `110`: x_12 + x_24 + x_32 + x_42 + x_48 <= 4
- Constraint `111`: x_2 + x_4 + x_5 + x_13 + x_22 + x_29 + x_59 + x_67 + x_69 <= 8
- Constraint `112`: x_22 + x_25 + x_26 + x_27 + x_32 + x_37 + x_58 + x_75 <= 7
- Constraint `113`: x_1 + x_5 + x_7 + x_9 + x_10 + x_34 + x_37 + x_52 + x_60 + x_68 <= 9
- Constraint `114`: x_21 + x_25 + x_29 + x_31 + x_58 + x_71 <= 5
- Constraint `115`: x_9 + x_21 + x_28 + x_37 + x_45 + x_64 + x_65 + x_67 + x_69 <= 8
- Constraint `116`: x_5 + x_15 + x_36 + x_38 + x_40 + x_51 <= 5
- Constraint `117`: x_12 + x_25 + x_31 + x_43 + x_55 + x_62 <= 5
- Constraint `118`: x_18 + x_20 + x_22 + x_27 + x_29 + x_31 + x_64 + x_71 + x_77 <= 8
- Constraint `119`: x_17 + x_20 + x_28 + x_58 + x_62 + x_64 + x_68 + x_75 + x_79 + x_80 <= 9
- Constraint `120`: x_12 + x_14 + x_16 + x_21 + x_29 + x_42 + x_43 + x_45 + x_65 + x_68 <= 9
- Constraint `121`: x_14 + x_33 + x_34 + x_45 + x_69 + x_77 <= 5
- Constraint `122`: x_5 + x_19 + x_51 + x_54 + x_59 + x_61 + x_67 + x_68 + x_75 <= 8
- Constraint `123`: x_5 + x_21 + x_25 + x_39 + x_44 + x_77 <= 5
- Constraint `124`: x_2 + x_3 + x_4 + x_8 + x_13 + x_14 + x_29 + x_44 + x_48 + x_75 <= 9
- Constraint `125`: x_2 + x_4 + x_37 + x_44 + x_60 <= 4
- Constraint `126`: x_10 + x_34 + x_37 + x_38 + x_45 + x_51 + x_67 <= 6
- Constraint `127`: x_5 + x_6 + x_9 + x_28 + x_29 + x_66 + x_67 + x_77 + x_79 <= 8
- Constraint `128`: x_12 + x_24 + x_39 + x_62 + x_64 + x_71 + x_76 <= 6
- Constraint `129`: x_3 + x_7 + x_22 + x_32 + x_34 + x_39 + x_55 + x_65 + x_72 <= 8
- Constraint `130`: x_14 + x_18 + x_25 + x_31 + x_62 <= 4
- Constraint `131`: x_14 + x_19 + x_22 + x_33 + x_46 + x_54 + x_56 + x_76 <= 7
- Constraint `132`: x_2 + x_7 + x_20 + x_21 + x_36 + x_41 + x_56 <= 6
- Constraint `133`: x_5 + x_38 + x_45 + x_51 + x_55 + x_69 <= 5
- Constraint `134`: x_1 + x_4 + x_17 + x_23 + x_29 + x_62 + x_64 + x_69 + x_77 <= 8
- Constraint `135`: x_1 + x_2 + x_6 + x_20 + x_23 + x_33 + x_44 + x_54 + x_64 <= 8
- Constraint `136`: x_26 + x_31 + x_40 + x_55 + x_66 + x_72 + x_78 + x_80 <= 7
- Constraint `137`: x_4 + x_42 + x_44 + x_61 + x_76 <= 4
- Constraint `138`: x_2 + x_3 + x_8 + x_39 + x_64 + x_76 <= 5
- Constraint `139`: x_3 + x_18 + x_22 + x_54 + x_68 + x_71 + x_74 + x_78 <= 7
- Constraint `140`: x_14 + x_17 + x_28 + x_30 + x_33 + x_47 + x_53 + x_61 + x_68 + x_77 <= 9
- Constraint `141`: x_9 + x_17 + x_38 + x_40 + x_61 + x_63 + x_72 + x_73 + x_80 <= 8
- Constraint `142`: x_20 + x_28 + x_31 + x_43 + x_44 + x_49 + x_63 + x_69 + x_74 <= 8
- Constraint `143`: x_4 + x_20 + x_21 + x_31 + x_51 <= 4
- Constraint `144`: x_3 + x_22 + x_30 + x_44 + x_64 <= 4
- Constraint `145`: x_6 + x_9 + x_17 + x_20 + x_53 + x_55 + x_67 + x_69 <= 7
- Constraint `146`: x_36 + x_39 + x_48 + x_63 + x_64 + x_69 + x_72 <= 6
- Constraint `147`: x_6 + x_8 + x_44 + x_60 + x_62 + x_72 <= 5
- Constraint `148`: x_1 + x_44 + x_45 + x_46 + x_67 + x_76 <= 5
- Constraint `149`: x_4 + x_6 + x_10 + x_16 + x_37 + x_42 + x_46 + x_53 + x_65 <= 8
- Constraint `150`: x_1 + x_8 + x_9 + x_23 + x_31 + x_38 + x_41 + x_43 + x_46 + x_67 <= 9
- Constraint `151`: x_8 + x_10 + x_22 + x_54 + x_73 + x_77 <= 5
- Constraint `152`: x_35 + x_41 + x_57 + x_61 + x_65 + x_74 <= 5
- Constraint `153`: x_5 + x_10 + x_19 + x_41 + x_56 + x_59 + x_62 + x_68 + x_69 <= 8
- Constraint `154`: x_2 + x_3 + x_11 + x_14 + x_36 + x_43 + x_56 + x_71 <= 7
- Constraint `155`: x_22 + x_25 + x_35 + x_47 + x_51 + x_75 <= 5
- Constraint `156`: x_8 + x_17 + x_20 + x_24 + x_34 + x_42 + x_47 + x_51 + x_52 + x_80 <= 9
- Constraint `157`: x_10 + x_18 + x_25 + x_28 + x_42 + x_45 + x_58 + x_75 <= 7
- Constraint `158`: x_3 + x_18 + x_38 + x_39 + x_48 + x_50 + x_56 + x_59 + x_69 + x_72 <= 9
- Constraint `159`: x_8 + x_11 + x_23 + x_31 + x_38 + x_62 <= 5
- Constraint `160`: x_4 + x_6 + x_41 + x_79 + x_80 <= 4
