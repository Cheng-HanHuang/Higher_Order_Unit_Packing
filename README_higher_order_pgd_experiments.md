# Higher-order PGD experiments for unit multi-constraint packing

This code tests the theorem-guided higher-order penalty

\[
\hat f(x) = -w^\top x + \gamma \sum_{k=1}^K e_{B_k+1}(x_{S_k}), \qquad x \in [0,1]^n,
\]

with \(\gamma = \max_i w_i + 0.1\), using projected gradient descent (PGD) with monotone Armijo backtracking.

## What the script checks

For each instance and multiple random initial points, it records:

1. whether the run converged to a first-order stationary point (via projected-gradient mapping norm);
2. whether the final point is binary;
3. whether the final point is feasible for the original packing constraints;
4. whether the final point has a practical local-minimum certificate;
5. whether there is saddle evidence.

For binary points, the code certifies a **strict local minimum** if the gradient is strictly inside the normal cone of the box:
- \(x_i = 0 \Rightarrow \nabla_i \hat f(x) > 0\)
- \(x_i = 1 \Rightarrow \nabla_i \hat f(x) < 0\)

For non-binary stationary points, the code estimates the Hessian on the free variables by finite differences and reports:
- `saddle_evidence = true` if the smallest free-subspace eigenvalue is negative;
- `local_min_evidence = true` if the free-subspace Hessian is positive definite and box first-order conditions hold.

## Datasets / instance families

The script includes two built-in families:

- `random_unit`: synthetic unit multi-constraint packing with arbitrary row capacities;
- `kset`: random k-set packing (all capacities equal to 1 after incidence conversion).

It also accepts a simple JSON loader for external instances.

## Usage

### Demo suite

```bash
python /mnt/data/higher_order_pgd_packing.py demo --outdir /mnt/data/demo_results
```

### One random theorem-matching unit packing instance

```bash
python /mnt/data/higher_order_pgd_packing.py random_unit \
  --n 25 --m 40 --row-min 3 --row-max 6 --capacity-mode mixed \
  --runs 20 --tune-runs 6 --out /mnt/data/random_unit_result.json
```

### One random k-set packing instance

```bash
python /mnt/data/higher_order_pgd_packing.py kset \
  --n-sets 30 --universe-size 20 --k 3 \
  --runs 20 --tune-runs 6 --out /mnt/data/kset_result.json
```

### External JSON instance format

```json
{
  "name": "my_instance",
  "weights": [1.2, 0.8, 1.6, 0.9],
  "constraints": [
    {"indices": [0, 1, 2], "capacity": 2},
    {"indices": [1, 2, 3], "capacity": 1}
  ]
}
```

Run it with:

```bash
python /mnt/data/higher_order_pgd_packing.py json /path/to/instance.json --out /mnt/data/result.json
```

## Notes

- The code uses a tuning phase for the initial PGD step size `eta0` from a small candidate grid. The algorithm itself still uses backtracking every iteration, so this tuning is mainly to reduce iterations and avoid slow progress.
- Results are saved as JSON for easy post-processing into tables / CSV later.
