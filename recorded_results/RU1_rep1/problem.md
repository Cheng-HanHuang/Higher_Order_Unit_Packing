# Original problem: random_unit_n40_m80_mixed

This file records the exact original binary packing problem used for the matching run result.

## Optimization model

\[
\max_{x\in\{0,1\}^n}\ \sum_{i=1}^n w_i x_i
\qquad\text{s.t.}\qquad
\sum_{i\in S_k} x_i \le B_k,\quad k=1,\dots,m.
\]

- Number of variables: `40`
- Number of constraints: `80`
- Matching run-result file: `result.json`

## Metadata

- `generator`: `random_unit_packing`
- `row_size_range`: `[4, 8]`
- `capacity_mode`: `mixed`

## Weights

w_1=1.8471408, w_2=1.1572796, w_3=0.64883407, w_4=1.2129144, w_5=1.9358299, w_6=1.7653139, w_7=1.9650837, w_8=1.4611214, w_9=1.7843255, w_10=1.8751933, w_11=1.3735885, w_12=0.71673101, w_13=1.8630396, w_14=0.74307546, w_15=1.4350028, w_16=1.0998168, w_17=1.5987087, w_18=0.87489721, w_19=1.4808872, w_20=0.88249282, w_21=1.4598842, w_22=1.9915298, w_23=0.58234876, w_24=1.3566959, w_25=1.8112465, w_26=1.3927456, w_27=0.76469562, w_28=1.5909776, w_29=1.2784677, w_30=1.4116039, w_31=1.6965943, w_32=1.6920853, w_33=0.93352342, w_34=1.7399646, w_35=1.7220341, w_36=1.6503986, w_37=1.0099036, w_38=0.96159794, w_39=1.9178674, w_40=0.71512681

## Exact constraints

- Constraint `1`: x_2 + x_7 + x_8 + x_21 + x_25 <= 3
- Constraint `2`: x_7 + x_16 + x_17 + x_35 + x_36 <= 1
- Constraint `3`: x_10 + x_20 + x_24 + x_30 + x_35 <= 1
- Constraint `4`: x_3 + x_5 + x_9 + x_19 + x_25 <= 2
- Constraint `5`: x_11 + x_19 + x_22 + x_26 + x_30 + x_34 + x_40 <= 1
- Constraint `6`: x_2 + x_9 + x_13 + x_16 + x_20 + x_22 <= 1
- Constraint `7`: x_4 + x_6 + x_13 + x_17 + x_30 + x_34 + x_35 <= 5
- Constraint `8`: x_10 + x_19 + x_20 + x_31 + x_32 + x_39 <= 5
- Constraint `9`: x_13 + x_17 + x_36 + x_40 <= 1
- Constraint `10`: x_12 + x_13 + x_18 + x_19 + x_32 + x_33 + x_37 <= 4
- Constraint `11`: x_4 + x_10 + x_12 + x_14 + x_19 + x_23 + x_24 <= 4
- Constraint `12`: x_3 + x_13 + x_14 + x_21 + x_27 <= 4
- Constraint `13`: x_2 + x_18 + x_19 + x_29 <= 3
- Constraint `14`: x_10 + x_23 + x_27 + x_34 + x_36 + x_37 + x_38 <= 4
- Constraint `15`: x_1 + x_3 + x_8 + x_13 + x_17 + x_36 + x_39 <= 5
- Constraint `16`: x_11 + x_12 + x_20 + x_27 + x_35 + x_37 + x_40 <= 5
- Constraint `17`: x_9 + x_10 + x_13 + x_15 + x_19 + x_31 + x_36 + x_39 <= 3
- Constraint `18`: x_5 + x_6 + x_10 + x_14 + x_25 + x_26 + x_31 + x_34 <= 6
- Constraint `19`: x_11 + x_14 + x_17 + x_22 + x_23 + x_27 + x_28 <= 6
- Constraint `20`: x_1 + x_5 + x_29 + x_37 <= 3
- Constraint `21`: x_2 + x_8 + x_14 + x_15 + x_24 + x_40 <= 3
- Constraint `22`: x_8 + x_23 + x_33 + x_34 <= 3
- Constraint `23`: x_1 + x_3 + x_30 + x_31 <= 3
- Constraint `24`: x_1 + x_4 + x_9 + x_12 + x_14 + x_17 + x_22 + x_37 <= 6
- Constraint `25`: x_2 + x_17 + x_19 + x_20 + x_30 + x_35 <= 4
- Constraint `26`: x_10 + x_14 + x_21 + x_25 + x_26 + x_27 <= 2
- Constraint `27`: x_4 + x_10 + x_13 + x_28 + x_32 + x_35 + x_39 <= 3
- Constraint `28`: x_7 + x_18 + x_36 + x_37 <= 3
- Constraint `29`: x_6 + x_10 + x_22 + x_40 <= 2
- Constraint `30`: x_13 + x_15 + x_35 + x_36 + x_39 <= 3
- Constraint `31`: x_2 + x_11 + x_15 + x_19 + x_25 + x_33 + x_36 + x_38 <= 3
- Constraint `32`: x_8 + x_16 + x_17 + x_22 + x_27 + x_30 + x_35 <= 3
- Constraint `33`: x_7 + x_9 + x_21 + x_22 + x_29 + x_31 <= 4
- Constraint `34`: x_8 + x_14 + x_16 + x_27 + x_30 + x_31 + x_37 + x_40 <= 3
- Constraint `35`: x_5 + x_6 + x_7 + x_11 + x_18 <= 1
- Constraint `36`: x_2 + x_4 + x_6 + x_8 + x_24 + x_33 + x_34 + x_40 <= 2
- Constraint `37`: x_2 + x_3 + x_4 + x_25 + x_27 + x_39 + x_40 <= 5
- Constraint `38`: x_1 + x_7 + x_18 + x_19 + x_20 + x_31 + x_37 <= 6
- Constraint `39`: x_18 + x_19 + x_26 + x_28 + x_35 + x_36 <= 3
- Constraint `40`: x_6 + x_13 + x_20 + x_21 + x_25 + x_35 <= 3
- Constraint `41`: x_2 + x_11 + x_34 + x_38 <= 2
- Constraint `42`: x_14 + x_16 + x_19 + x_21 + x_25 + x_37 <= 2
- Constraint `43`: x_6 + x_10 + x_15 + x_20 + x_21 + x_22 + x_32 + x_39 <= 5
- Constraint `44`: x_2 + x_10 + x_23 + x_36 <= 3
- Constraint `45`: x_2 + x_8 + x_23 + x_28 <= 1
- Constraint `46`: x_13 + x_15 + x_17 + x_29 <= 1
- Constraint `47`: x_6 + x_13 + x_16 + x_23 + x_28 + x_32 + x_34 <= 6
- Constraint `48`: x_8 + x_9 + x_15 + x_18 + x_20 + x_29 + x_36 + x_37 <= 5
- Constraint `49`: x_5 + x_6 + x_7 + x_9 + x_14 + x_35 + x_38 + x_39 <= 4
- Constraint `50`: x_3 + x_5 + x_8 + x_24 + x_29 + x_32 + x_33 <= 2
- Constraint `51`: x_5 + x_6 + x_10 + x_14 + x_26 + x_30 + x_38 + x_40 <= 4
- Constraint `52`: x_7 + x_17 + x_24 + x_31 + x_32 + x_40 <= 5
- Constraint `53`: x_3 + x_4 + x_9 + x_12 + x_24 + x_29 <= 4
- Constraint `54`: x_13 + x_15 + x_20 + x_23 + x_24 + x_29 + x_34 <= 5
- Constraint `55`: x_4 + x_5 + x_9 + x_12 + x_13 + x_23 + x_30 <= 4
- Constraint `56`: x_4 + x_6 + x_11 + x_40 <= 1
- Constraint `57`: x_7 + x_8 + x_15 + x_17 + x_18 + x_23 + x_31 + x_33 <= 2
- Constraint `58`: x_2 + x_17 + x_24 + x_32 + x_37 <= 1
- Constraint `59`: x_4 + x_9 + x_26 + x_28 + x_38 <= 4
- Constraint `60`: x_5 + x_22 + x_24 + x_26 + x_32 + x_33 <= 4
- Constraint `61`: x_7 + x_8 + x_16 + x_20 + x_27 + x_35 + x_38 <= 4
- Constraint `62`: x_8 + x_15 + x_24 + x_35 + x_38 + x_39 <= 3
- Constraint `63`: x_2 + x_13 + x_24 + x_30 + x_37 <= 1
- Constraint `64`: x_6 + x_12 + x_15 + x_17 + x_23 <= 1
- Constraint `65`: x_2 + x_4 + x_10 + x_19 + x_24 + x_31 + x_40 <= 4
- Constraint `66`: x_3 + x_4 + x_6 + x_10 + x_27 + x_32 + x_37 + x_40 <= 2
- Constraint `67`: x_2 + x_3 + x_6 + x_10 + x_19 + x_34 + x_39 + x_40 <= 7
- Constraint `68`: x_7 + x_8 + x_16 + x_19 + x_20 + x_33 + x_38 + x_39 <= 5
- Constraint `69`: x_2 + x_4 + x_5 + x_14 + x_18 + x_21 + x_25 <= 1
- Constraint `70`: x_3 + x_8 + x_10 + x_26 + x_39 + x_40 <= 1
- Constraint `71`: x_11 + x_22 + x_28 + x_29 + x_34 + x_36 <= 4
- Constraint `72`: x_2 + x_12 + x_18 + x_28 <= 1
- Constraint `73`: x_9 + x_12 + x_14 + x_15 + x_36 <= 1
- Constraint `74`: x_4 + x_6 + x_13 + x_19 + x_20 + x_21 + x_27 + x_40 <= 5
- Constraint `75`: x_13 + x_30 + x_34 + x_35 + x_39 <= 1
- Constraint `76`: x_1 + x_4 + x_5 + x_6 + x_9 + x_10 + x_16 + x_39 <= 6
- Constraint `77`: x_13 + x_23 + x_27 + x_28 + x_33 + x_34 + x_36 + x_38 <= 1
- Constraint `78`: x_10 + x_13 + x_18 + x_23 + x_25 + x_31 + x_37 <= 3
- Constraint `79`: x_9 + x_20 + x_25 + x_27 + x_29 + x_39 <= 4
- Constraint `80`: x_2 + x_6 + x_10 + x_12 + x_17 + x_24 <= 1
