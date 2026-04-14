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

w_1=1.8547585, w_2=0.59603048, w_3=1.311573, w_4=1.7436752, w_5=1.9736424, w_6=1.4241424, w_7=0.84188728, w_8=0.5100776, w_9=0.73547046, w_10=0.62879399, w_11=1.6246957, w_12=1.7435494, w_13=0.94593549, w_14=1.8134685, w_15=0.70266746, w_16=1.3697075, w_17=1.3494428, w_18=1.2270962, w_19=1.1621178, w_20=0.81686809, w_21=1.1052959, w_22=1.5765683, w_23=1.746631, w_24=1.1041695, w_25=0.98014745, w_26=1.5988757, w_27=1.0419089, w_28=1.2225828, w_29=1.6932595, w_30=0.51909792, w_31=0.98422783, w_32=0.78205868, w_33=1.7303592, w_34=0.80240699, w_35=0.85175862, w_36=0.52412941, w_37=1.5194116, w_38=1.3904496, w_39=0.84521156, w_40=1.5132841

## Exact constraints

- Constraint `1`: x_8 + x_9 + x_16 + x_20 <= 1
- Constraint `2`: x_2 + x_5 + x_13 + x_26 + x_32 + x_38 <= 5
- Constraint `3`: x_4 + x_5 + x_8 + x_16 + x_21 + x_39 <= 3
- Constraint `4`: x_5 + x_16 + x_21 + x_24 + x_30 + x_34 + x_39 <= 4
- Constraint `5`: x_3 + x_13 + x_17 + x_33 <= 2
- Constraint `6`: x_1 + x_8 + x_16 + x_29 + x_37 + x_38 + x_40 <= 5
- Constraint `7`: x_11 + x_19 + x_28 + x_29 + x_33 + x_34 <= 1
- Constraint `8`: x_12 + x_13 + x_16 + x_19 + x_29 + x_38 + x_39 <= 1
- Constraint `9`: x_3 + x_10 + x_35 + x_40 <= 1
- Constraint `10`: x_7 + x_15 + x_17 + x_21 + x_25 + x_31 + x_33 + x_39 <= 1
- Constraint `11`: x_7 + x_27 + x_29 + x_31 + x_34 + x_35 <= 2
- Constraint `12`: x_8 + x_19 + x_20 + x_39 <= 3
- Constraint `13`: x_3 + x_22 + x_34 + x_36 <= 1
- Constraint `14`: x_2 + x_4 + x_6 + x_24 + x_31 + x_37 + x_38 <= 3
- Constraint `15`: x_1 + x_19 + x_20 + x_26 + x_38 <= 4
- Constraint `16`: x_2 + x_7 + x_15 + x_23 + x_29 + x_30 + x_34 <= 4
- Constraint `17`: x_14 + x_17 + x_25 + x_34 <= 1
- Constraint `18`: x_10 + x_11 + x_17 + x_35 <= 3
- Constraint `19`: x_12 + x_21 + x_23 + x_26 + x_30 + x_36 + x_40 <= 3
- Constraint `20`: x_3 + x_9 + x_19 + x_24 + x_34 + x_36 + x_37 <= 2
- Constraint `21`: x_1 + x_25 + x_34 + x_39 + x_40 <= 3
- Constraint `22`: x_8 + x_10 + x_22 + x_24 + x_29 + x_30 + x_32 <= 3
- Constraint `23`: x_8 + x_16 + x_22 + x_28 <= 2
- Constraint `24`: x_10 + x_13 + x_16 + x_20 + x_22 + x_26 + x_30 + x_37 <= 4
- Constraint `25`: x_3 + x_6 + x_9 + x_23 + x_28 + x_37 <= 3
- Constraint `26`: x_5 + x_16 + x_20 + x_39 <= 3
- Constraint `27`: x_3 + x_10 + x_16 + x_18 + x_32 <= 1
- Constraint `28`: x_6 + x_10 + x_16 + x_17 + x_32 + x_33 <= 3
- Constraint `29`: x_1 + x_3 + x_6 + x_13 + x_28 <= 4
- Constraint `30`: x_9 + x_11 + x_21 + x_27 + x_31 + x_37 + x_39 <= 1
- Constraint `31`: x_2 + x_9 + x_11 + x_21 + x_22 + x_24 + x_26 + x_37 <= 6
- Constraint `32`: x_4 + x_6 + x_16 + x_23 <= 2
- Constraint `33`: x_5 + x_15 + x_16 + x_17 + x_22 + x_39 <= 5
- Constraint `34`: x_4 + x_7 + x_14 + x_15 + x_21 + x_22 + x_38 + x_39 <= 1
- Constraint `35`: x_4 + x_13 + x_15 + x_18 + x_21 + x_24 + x_32 + x_39 <= 1
- Constraint `36`: x_3 + x_8 + x_10 + x_14 + x_18 + x_21 + x_34 + x_39 <= 5
- Constraint `37`: x_1 + x_4 + x_12 + x_18 + x_20 + x_21 <= 2
- Constraint `38`: x_9 + x_17 + x_25 + x_36 + x_38 <= 3
- Constraint `39`: x_7 + x_15 + x_17 + x_22 + x_25 + x_33 + x_39 + x_40 <= 2
- Constraint `40`: x_8 + x_9 + x_10 + x_14 + x_25 + x_38 <= 1
- Constraint `41`: x_2 + x_16 + x_23 + x_26 + x_28 + x_39 <= 2
- Constraint `42`: x_7 + x_18 + x_21 + x_29 + x_32 <= 3
- Constraint `43`: x_12 + x_16 + x_18 + x_24 + x_28 + x_35 <= 4
- Constraint `44`: x_4 + x_13 + x_14 + x_18 + x_36 + x_38 + x_39 <= 6
- Constraint `45`: x_19 + x_28 + x_29 + x_31 + x_32 + x_36 + x_39 <= 2
- Constraint `46`: x_14 + x_20 + x_28 + x_29 + x_33 <= 2
- Constraint `47`: x_17 + x_19 + x_24 + x_28 + x_31 + x_32 + x_35 + x_38 <= 7
- Constraint `48`: x_10 + x_13 + x_25 + x_27 + x_29 + x_32 <= 3
- Constraint `49`: x_2 + x_7 + x_23 + x_24 + x_28 + x_30 + x_33 <= 4
- Constraint `50`: x_1 + x_3 + x_6 + x_15 + x_19 + x_35 <= 3
- Constraint `51`: x_4 + x_7 + x_10 + x_14 + x_25 + x_37 <= 1
- Constraint `52`: x_10 + x_13 + x_24 + x_28 + x_30 + x_33 + x_35 <= 4
- Constraint `53`: x_1 + x_5 + x_13 + x_17 + x_20 <= 1
- Constraint `54`: x_16 + x_23 + x_31 + x_33 + x_34 <= 4
- Constraint `55`: x_3 + x_10 + x_11 + x_12 + x_13 + x_15 + x_28 + x_33 <= 7
- Constraint `56`: x_1 + x_7 + x_13 + x_15 + x_16 + x_28 <= 3
- Constraint `57`: x_4 + x_8 + x_9 + x_15 + x_19 + x_22 + x_26 + x_28 <= 1
- Constraint `58`: x_23 + x_27 + x_35 + x_37 + x_38 <= 3
- Constraint `59`: x_7 + x_8 + x_11 + x_19 + x_23 + x_27 + x_28 <= 5
- Constraint `60`: x_1 + x_7 + x_24 + x_40 <= 3
- Constraint `61`: x_2 + x_8 + x_16 + x_18 + x_20 + x_21 + x_37 + x_40 <= 1
- Constraint `62`: x_7 + x_10 + x_17 + x_19 + x_25 + x_35 <= 5
- Constraint `63`: x_13 + x_14 + x_17 + x_32 + x_37 <= 1
- Constraint `64`: x_7 + x_15 + x_17 + x_20 + x_26 <= 2
- Constraint `65`: x_3 + x_4 + x_11 + x_16 + x_23 + x_36 + x_37 + x_40 <= 4
- Constraint `66`: x_4 + x_5 + x_16 + x_30 <= 3
- Constraint `67`: x_2 + x_6 + x_17 + x_20 + x_31 + x_40 <= 4
- Constraint `68`: x_4 + x_5 + x_15 + x_16 + x_24 + x_25 + x_32 <= 3
- Constraint `69`: x_4 + x_12 + x_19 + x_24 + x_25 <= 4
- Constraint `70`: x_11 + x_13 + x_16 + x_18 + x_21 + x_26 + x_31 + x_36 <= 4
- Constraint `71`: x_3 + x_6 + x_7 + x_21 + x_37 <= 2
- Constraint `72`: x_4 + x_17 + x_18 + x_23 + x_24 + x_30 + x_40 <= 1
- Constraint `73`: x_3 + x_10 + x_11 + x_17 + x_22 + x_23 + x_31 <= 6
- Constraint `74`: x_15 + x_20 + x_26 + x_27 + x_29 + x_32 <= 5
- Constraint `75`: x_2 + x_9 + x_22 + x_23 + x_30 + x_35 + x_36 <= 3
- Constraint `76`: x_6 + x_12 + x_21 + x_28 + x_29 + x_34 <= 3
- Constraint `77`: x_3 + x_7 + x_13 + x_22 + x_26 + x_34 <= 1
- Constraint `78`: x_5 + x_14 + x_15 + x_17 + x_22 + x_24 <= 5
- Constraint `79`: x_3 + x_18 + x_22 + x_34 <= 2
- Constraint `80`: x_3 + x_4 + x_15 + x_16 + x_19 + x_21 + x_22 + x_37 <= 1
