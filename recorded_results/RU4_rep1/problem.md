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

w_1=0.74704904, w_2=0.80612451, w_3=0.76439708, w_4=1.9954792, w_5=0.52442242, w_6=1.7182448, w_7=0.83789442, w_8=1.6589211, w_9=1.1017484, w_10=1.6683891, w_11=1.334148, w_12=1.4987092, w_13=1.4514033, w_14=0.84053901, w_15=0.84641294, w_16=1.2565169, w_17=0.5879915, w_18=1.2891285, w_19=1.5734249, w_20=1.6710747, w_21=0.97219462, w_22=1.4066169, w_23=0.95975313, w_24=0.61411512, w_25=1.7600099, w_26=1.3608775, w_27=0.78843998, w_28=1.2219885, w_29=1.7582509, w_30=1.3797764, w_31=1.1243924, w_32=1.13328, w_33=1.7742385, w_34=0.66966337, w_35=0.94947855, w_36=1.2791172, w_37=1.4087833, w_38=0.90439227, w_39=0.82646195, w_40=0.74753052, w_41=0.97324866, w_42=1.2773578, w_43=0.68374136, w_44=0.96836599, w_45=0.5806066, w_46=0.9755942, w_47=1.0858708, w_48=1.2120738, w_49=1.727184, w_50=0.70090306, w_51=0.68086221, w_52=1.7841638, w_53=0.98398624, w_54=1.6333848, w_55=1.3847181, w_56=1.1122799, w_57=1.3662291, w_58=0.53009597, w_59=0.779704, w_60=1.2119167, w_61=1.076816, w_62=1.468891, w_63=1.148655, w_64=1.6407506, w_65=1.4245723, w_66=0.75241274, w_67=1.4753772, w_68=1.6420507, w_69=0.98806992, w_70=0.52518324, w_71=1.5353511, w_72=1.5447106, w_73=1.7216592, w_74=1.8414792, w_75=1.1892045, w_76=0.66395368, w_77=0.90492404, w_78=1.6633225, w_79=1.2749214, w_80=1.6867278

## Exact constraints

- Constraint `1`: x_8 + x_25 + x_44 + x_49 + x_67 <= 4
- Constraint `2`: x_2 + x_6 + x_18 + x_32 + x_53 + x_60 + x_70 + x_74 + x_80 <= 8
- Constraint `3`: x_1 + x_23 + x_34 + x_51 + x_68 + x_72 <= 5
- Constraint `4`: x_15 + x_46 + x_53 + x_74 + x_76 <= 4
- Constraint `5`: x_1 + x_16 + x_27 + x_51 + x_64 + x_68 + x_78 <= 6
- Constraint `6`: x_3 + x_5 + x_7 + x_15 + x_21 + x_22 + x_32 + x_46 + x_64 + x_65 <= 9
- Constraint `7`: x_4 + x_19 + x_31 + x_46 + x_51 + x_57 + x_70 <= 6
- Constraint `8`: x_14 + x_19 + x_21 + x_36 + x_41 + x_59 + x_64 <= 6
- Constraint `9`: x_6 + x_8 + x_24 + x_36 + x_47 + x_75 <= 5
- Constraint `10`: x_1 + x_9 + x_18 + x_21 + x_31 + x_33 + x_48 + x_56 + x_68 <= 8
- Constraint `11`: x_2 + x_19 + x_36 + x_52 + x_54 + x_57 + x_60 + x_67 <= 7
- Constraint `12`: x_4 + x_9 + x_28 + x_61 + x_69 + x_78 <= 5
- Constraint `13`: x_13 + x_25 + x_33 + x_37 + x_40 + x_46 + x_65 <= 6
- Constraint `14`: x_12 + x_23 + x_48 + x_49 + x_50 <= 4
- Constraint `15`: x_1 + x_20 + x_25 + x_34 + x_40 + x_50 + x_59 <= 6
- Constraint `16`: x_8 + x_19 + x_44 + x_61 + x_70 + x_71 <= 5
- Constraint `17`: x_4 + x_10 + x_12 + x_51 + x_53 + x_71 <= 5
- Constraint `18`: x_6 + x_11 + x_19 + x_27 + x_32 + x_43 + x_59 + x_67 + x_74 <= 8
- Constraint `19`: x_2 + x_4 + x_5 + x_7 + x_31 + x_62 <= 5
- Constraint `20`: x_1 + x_11 + x_19 + x_24 + x_51 + x_59 + x_61 + x_66 + x_80 <= 8
- Constraint `21`: x_5 + x_16 + x_20 + x_27 + x_31 + x_54 + x_59 + x_64 + x_74 <= 8
- Constraint `22`: x_10 + x_13 + x_17 + x_40 + x_49 + x_68 <= 5
- Constraint `23`: x_4 + x_7 + x_25 + x_31 + x_34 + x_39 + x_47 + x_57 + x_60 + x_71 <= 9
- Constraint `24`: x_10 + x_19 + x_33 + x_44 + x_50 + x_78 <= 5
- Constraint `25`: x_5 + x_6 + x_32 + x_38 + x_42 + x_45 + x_48 + x_64 + x_79 <= 8
- Constraint `26`: x_4 + x_20 + x_21 + x_23 + x_73 <= 4
- Constraint `27`: x_1 + x_9 + x_28 + x_30 + x_51 + x_63 + x_77 <= 6
- Constraint `28`: x_5 + x_13 + x_20 + x_38 + x_43 + x_75 <= 5
- Constraint `29`: x_4 + x_13 + x_23 + x_28 + x_35 + x_56 + x_60 + x_62 + x_71 <= 8
- Constraint `30`: x_13 + x_26 + x_33 + x_38 + x_47 + x_48 + x_54 <= 6
- Constraint `31`: x_34 + x_50 + x_58 + x_65 + x_71 + x_72 <= 5
- Constraint `32`: x_15 + x_29 + x_38 + x_39 + x_40 + x_46 + x_47 + x_70 <= 7
- Constraint `33`: x_8 + x_23 + x_28 + x_58 + x_76 + x_79 <= 5
- Constraint `34`: x_23 + x_37 + x_48 + x_50 + x_51 + x_61 + x_71 + x_75 <= 7
- Constraint `35`: x_17 + x_21 + x_24 + x_27 + x_57 + x_60 <= 5
- Constraint `36`: x_9 + x_24 + x_28 + x_29 + x_37 + x_52 + x_80 <= 6
- Constraint `37`: x_3 + x_7 + x_11 + x_24 + x_27 + x_48 + x_49 + x_78 <= 7
- Constraint `38`: x_20 + x_23 + x_26 + x_46 + x_48 + x_64 + x_73 <= 6
- Constraint `39`: x_7 + x_12 + x_30 + x_41 + x_45 + x_68 + x_72 + x_75 + x_79 <= 8
- Constraint `40`: x_8 + x_11 + x_22 + x_35 + x_39 + x_45 + x_53 + x_55 + x_57 + x_70 <= 9
- Constraint `41`: x_5 + x_30 + x_31 + x_38 + x_60 + x_71 + x_76 <= 6
- Constraint `42`: x_8 + x_16 + x_17 + x_27 + x_34 + x_35 + x_41 + x_46 + x_56 + x_70 <= 9
- Constraint `43`: x_5 + x_14 + x_39 + x_41 + x_48 + x_61 <= 5
- Constraint `44`: x_9 + x_11 + x_12 + x_54 + x_55 + x_75 <= 5
- Constraint `45`: x_20 + x_25 + x_31 + x_48 + x_60 + x_63 + x_75 + x_76 <= 7
- Constraint `46`: x_10 + x_11 + x_18 + x_55 + x_69 + x_73 + x_74 + x_75 <= 7
- Constraint `47`: x_4 + x_5 + x_42 + x_56 + x_62 + x_73 + x_75 <= 6
- Constraint `48`: x_10 + x_11 + x_13 + x_27 + x_38 + x_40 + x_42 + x_51 + x_74 + x_79 <= 9
- Constraint `49`: x_7 + x_16 + x_21 + x_39 + x_51 + x_65 + x_71 <= 6
- Constraint `50`: x_24 + x_33 + x_34 + x_73 + x_74 + x_79 <= 5
- Constraint `51`: x_6 + x_31 + x_44 + x_47 + x_61 + x_71 <= 5
- Constraint `52`: x_12 + x_29 + x_32 + x_36 + x_37 + x_39 + x_51 + x_52 + x_75 <= 8
- Constraint `53`: x_2 + x_27 + x_38 + x_54 + x_68 + x_74 <= 5
- Constraint `54`: x_5 + x_26 + x_43 + x_53 + x_65 <= 4
- Constraint `55`: x_9 + x_12 + x_20 + x_30 + x_32 + x_54 + x_56 + x_64 + x_80 <= 8
- Constraint `56`: x_9 + x_14 + x_34 + x_39 + x_45 + x_56 + x_74 <= 6
- Constraint `57`: x_1 + x_4 + x_23 + x_26 + x_28 + x_51 + x_53 + x_58 + x_68 <= 8
- Constraint `58`: x_3 + x_14 + x_40 + x_45 + x_54 + x_62 + x_63 <= 6
- Constraint `59`: x_4 + x_38 + x_54 + x_73 + x_76 <= 4
- Constraint `60`: x_24 + x_53 + x_57 + x_60 + x_67 + x_68 + x_71 <= 6
- Constraint `61`: x_22 + x_31 + x_40 + x_50 + x_67 <= 4
- Constraint `62`: x_13 + x_17 + x_36 + x_37 + x_49 + x_50 + x_52 + x_68 + x_70 <= 8
- Constraint `63`: x_13 + x_25 + x_36 + x_37 + x_43 + x_56 + x_66 + x_70 + x_79 <= 8
- Constraint `64`: x_14 + x_27 + x_32 + x_39 + x_47 + x_61 + x_73 + x_77 <= 7
- Constraint `65`: x_10 + x_18 + x_28 + x_36 + x_47 <= 4
- Constraint `66`: x_13 + x_14 + x_22 + x_27 + x_50 + x_55 + x_56 + x_66 + x_71 <= 8
- Constraint `67`: x_2 + x_30 + x_35 + x_42 + x_45 + x_58 + x_60 + x_66 + x_69 + x_76 <= 9
- Constraint `68`: x_31 + x_34 + x_38 + x_41 + x_42 <= 4
- Constraint `69`: x_5 + x_22 + x_44 + x_59 + x_60 + x_66 <= 5
- Constraint `70`: x_1 + x_21 + x_44 + x_45 + x_53 + x_61 + x_65 <= 6
- Constraint `71`: x_3 + x_13 + x_31 + x_41 + x_43 + x_54 + x_61 + x_62 + x_64 + x_80 <= 9
- Constraint `72`: x_4 + x_7 + x_8 + x_10 + x_36 + x_39 + x_56 + x_67 + x_71 + x_76 <= 9
- Constraint `73`: x_12 + x_37 + x_55 + x_63 + x_67 <= 4
- Constraint `74`: x_15 + x_23 + x_30 + x_38 + x_54 + x_62 + x_65 + x_72 + x_74 + x_77 <= 9
- Constraint `75`: x_10 + x_24 + x_34 + x_35 + x_45 + x_52 + x_70 + x_77 + x_80 <= 8
- Constraint `76`: x_7 + x_18 + x_22 + x_23 + x_27 + x_35 + x_53 + x_60 + x_75 + x_76 <= 9
- Constraint `77`: x_8 + x_26 + x_30 + x_72 + x_74 + x_75 <= 5
- Constraint `78`: x_5 + x_13 + x_24 + x_31 + x_56 + x_65 <= 5
- Constraint `79`: x_4 + x_8 + x_23 + x_42 + x_64 + x_80 <= 5
- Constraint `80`: x_1 + x_9 + x_47 + x_56 + x_80 <= 4
- Constraint `81`: x_22 + x_36 + x_37 + x_46 + x_78 <= 4
- Constraint `82`: x_28 + x_35 + x_66 + x_70 + x_78 <= 4
- Constraint `83`: x_32 + x_38 + x_39 + x_41 + x_45 + x_50 + x_57 + x_64 + x_66 <= 8
- Constraint `84`: x_15 + x_22 + x_39 + x_43 + x_52 + x_55 + x_60 + x_68 <= 7
- Constraint `85`: x_11 + x_48 + x_53 + x_56 + x_80 <= 4
- Constraint `86`: x_40 + x_44 + x_47 + x_50 + x_56 + x_58 + x_62 + x_63 <= 7
- Constraint `87`: x_4 + x_8 + x_24 + x_32 + x_36 + x_44 + x_47 + x_65 + x_68 <= 8
- Constraint `88`: x_14 + x_31 + x_32 + x_51 + x_58 + x_59 + x_62 + x_69 + x_75 + x_76 <= 9
- Constraint `89`: x_16 + x_20 + x_23 + x_31 + x_50 + x_56 + x_60 + x_63 + x_76 <= 8
- Constraint `90`: x_12 + x_38 + x_55 + x_59 + x_69 <= 4
- Constraint `91`: x_4 + x_8 + x_9 + x_12 + x_18 + x_27 + x_36 + x_49 + x_57 + x_76 <= 9
- Constraint `92`: x_4 + x_10 + x_11 + x_20 + x_37 + x_38 + x_49 + x_56 + x_70 <= 8
- Constraint `93`: x_5 + x_9 + x_14 + x_24 + x_29 + x_54 + x_62 + x_64 <= 7
- Constraint `94`: x_6 + x_11 + x_14 + x_17 + x_20 + x_22 + x_40 + x_60 + x_68 + x_77 <= 9
- Constraint `95`: x_9 + x_13 + x_19 + x_26 + x_32 + x_47 + x_65 + x_70 + x_72 + x_75 <= 9
- Constraint `96`: x_7 + x_8 + x_16 + x_19 + x_40 + x_51 + x_52 + x_70 + x_73 + x_78 <= 9
- Constraint `97`: x_8 + x_35 + x_55 + x_59 + x_68 <= 4
- Constraint `98`: x_2 + x_6 + x_13 + x_14 + x_28 + x_35 + x_49 + x_52 + x_60 + x_66 <= 9
- Constraint `99`: x_19 + x_26 + x_31 + x_40 + x_45 + x_60 + x_71 <= 6
- Constraint `100`: x_21 + x_27 + x_32 + x_52 + x_60 + x_63 + x_64 <= 6
- Constraint `101`: x_1 + x_4 + x_18 + x_25 + x_42 + x_59 + x_66 + x_79 + x_80 <= 8
- Constraint `102`: x_1 + x_9 + x_16 + x_34 + x_37 + x_47 + x_55 + x_59 + x_70 + x_71 <= 9
- Constraint `103`: x_6 + x_17 + x_19 + x_20 + x_33 + x_64 + x_68 + x_79 <= 7
- Constraint `104`: x_4 + x_12 + x_50 + x_58 + x_59 <= 4
- Constraint `105`: x_13 + x_25 + x_27 + x_31 + x_48 + x_52 + x_63 <= 6
- Constraint `106`: x_1 + x_10 + x_18 + x_20 + x_31 + x_41 + x_69 + x_70 + x_75 + x_77 <= 9
- Constraint `107`: x_14 + x_33 + x_35 + x_60 + x_72 <= 4
- Constraint `108`: x_11 + x_13 + x_22 + x_47 + x_48 + x_60 + x_63 + x_68 <= 7
- Constraint `109`: x_2 + x_17 + x_23 + x_28 + x_42 + x_45 + x_47 + x_51 + x_52 <= 8
- Constraint `110`: x_16 + x_21 + x_24 + x_25 + x_55 + x_58 + x_61 + x_78 <= 7
- Constraint `111`: x_10 + x_16 + x_19 + x_22 + x_29 + x_46 + x_52 + x_73 + x_76 <= 8
- Constraint `112`: x_9 + x_24 + x_27 + x_37 + x_39 + x_64 + x_74 + x_76 <= 7
- Constraint `113`: x_9 + x_25 + x_40 + x_52 + x_76 <= 4
- Constraint `114`: x_17 + x_25 + x_35 + x_53 + x_54 + x_58 + x_65 <= 6
- Constraint `115`: x_9 + x_13 + x_19 + x_26 + x_32 + x_57 + x_63 <= 6
- Constraint `116`: x_12 + x_20 + x_31 + x_37 + x_48 + x_56 + x_61 <= 6
- Constraint `117`: x_11 + x_21 + x_31 + x_54 + x_63 + x_79 <= 5
- Constraint `118`: x_9 + x_15 + x_19 + x_20 + x_41 + x_52 + x_63 + x_64 + x_76 + x_80 <= 9
- Constraint `119`: x_13 + x_20 + x_26 + x_30 + x_51 + x_56 + x_57 + x_58 + x_68 + x_78 <= 9
- Constraint `120`: x_11 + x_21 + x_35 + x_51 + x_76 <= 4
- Constraint `121`: x_4 + x_8 + x_75 + x_76 + x_80 <= 4
- Constraint `122`: x_1 + x_15 + x_27 + x_29 + x_30 + x_38 + x_53 + x_62 + x_63 <= 8
- Constraint `123`: x_6 + x_17 + x_18 + x_37 + x_38 + x_39 + x_57 <= 6
- Constraint `124`: x_16 + x_28 + x_30 + x_34 + x_44 + x_47 + x_52 + x_54 + x_58 + x_64 <= 9
- Constraint `125`: x_9 + x_10 + x_22 + x_28 + x_29 + x_53 + x_57 + x_73 + x_75 + x_77 <= 9
- Constraint `126`: x_3 + x_5 + x_16 + x_22 + x_24 + x_27 + x_44 + x_59 + x_65 + x_73 <= 9
- Constraint `127`: x_4 + x_22 + x_27 + x_28 + x_37 + x_65 + x_66 + x_70 + x_72 + x_78 <= 9
- Constraint `128`: x_10 + x_14 + x_17 + x_18 + x_21 + x_30 + x_32 + x_55 + x_69 <= 8
- Constraint `129`: x_10 + x_36 + x_44 + x_47 + x_52 + x_65 + x_79 <= 6
- Constraint `130`: x_14 + x_26 + x_28 + x_37 + x_77 <= 4
- Constraint `131`: x_11 + x_17 + x_18 + x_20 + x_32 + x_68 + x_78 + x_80 <= 7
- Constraint `132`: x_3 + x_14 + x_36 + x_52 + x_56 + x_59 + x_60 + x_66 + x_67 + x_78 <= 9
- Constraint `133`: x_3 + x_5 + x_10 + x_20 + x_42 + x_46 + x_57 + x_65 + x_67 <= 8
- Constraint `134`: x_4 + x_5 + x_17 + x_34 + x_38 + x_39 <= 5
- Constraint `135`: x_5 + x_9 + x_10 + x_16 + x_20 + x_23 + x_24 + x_28 + x_40 + x_69 <= 9
- Constraint `136`: x_9 + x_11 + x_20 + x_24 + x_27 + x_68 + x_74 <= 6
- Constraint `137`: x_6 + x_14 + x_19 + x_52 + x_57 + x_67 + x_78 <= 6
- Constraint `138`: x_5 + x_9 + x_12 + x_16 + x_24 + x_46 + x_58 + x_68 + x_69 + x_79 <= 9
- Constraint `139`: x_14 + x_27 + x_38 + x_40 + x_47 + x_55 + x_65 + x_74 + x_78 <= 8
- Constraint `140`: x_8 + x_25 + x_34 + x_38 + x_41 + x_51 + x_79 <= 6
- Constraint `141`: x_4 + x_16 + x_21 + x_29 + x_37 + x_52 + x_58 + x_78 <= 7
- Constraint `142`: x_2 + x_3 + x_14 + x_33 + x_53 <= 4
- Constraint `143`: x_36 + x_56 + x_70 + x_75 + x_79 <= 4
- Constraint `144`: x_1 + x_9 + x_18 + x_27 + x_43 + x_48 <= 5
- Constraint `145`: x_24 + x_31 + x_35 + x_45 + x_52 + x_77 <= 5
- Constraint `146`: x_7 + x_11 + x_19 + x_40 + x_42 + x_61 <= 5
- Constraint `147`: x_2 + x_12 + x_38 + x_55 + x_59 + x_70 <= 5
- Constraint `148`: x_4 + x_27 + x_34 + x_55 + x_61 + x_74 + x_77 <= 6
- Constraint `149`: x_17 + x_27 + x_52 + x_60 + x_68 <= 4
- Constraint `150`: x_13 + x_24 + x_35 + x_37 + x_50 + x_68 + x_72 <= 6
- Constraint `151`: x_8 + x_9 + x_18 + x_29 + x_44 + x_59 + x_62 + x_67 <= 7
- Constraint `152`: x_8 + x_13 + x_15 + x_33 + x_59 + x_74 <= 5
- Constraint `153`: x_1 + x_15 + x_18 + x_21 + x_39 + x_40 + x_47 + x_56 <= 7
- Constraint `154`: x_3 + x_11 + x_13 + x_27 + x_31 + x_34 + x_40 + x_43 + x_52 + x_71 <= 9
- Constraint `155`: x_10 + x_25 + x_32 + x_55 + x_60 + x_71 + x_76 <= 6
- Constraint `156`: x_13 + x_37 + x_48 + x_62 + x_69 + x_80 <= 5
- Constraint `157`: x_14 + x_25 + x_58 + x_75 + x_80 <= 4
- Constraint `158`: x_6 + x_16 + x_45 + x_57 + x_59 + x_60 + x_74 <= 6
- Constraint `159`: x_24 + x_25 + x_31 + x_35 + x_58 + x_59 + x_64 + x_65 + x_80 <= 8
- Constraint `160`: x_6 + x_18 + x_21 + x_31 + x_34 + x_35 + x_57 + x_58 + x_65 + x_69 <= 9
