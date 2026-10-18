# Quantitative evidence for the rigorous tutorial

Reviewed 17 October 2026. Machine-readable values and uncertainty calculations are in `rigor_benchmarks.json`. These are research prototype experiments, not measurements of operating utility reliability.

## R02: repeated attempts and increasing difficulty

[Capability Gaps, v1](https://arxiv.org/pdf/2607.28822v1), Table II, PDF page 4, reports eight cells: DeepSeek L1 succeeds 5/10 times at both 100 and 1,000 buses; DeepSeek L2 and the OpenAI configuration L1/L2 succeed 10/10 at both sizes. Larger grids and L3–6 have narrative failures but no reported count cells. Do not encode them as numerical zeroes. All systems are tiled synthetic grids.

The added Wilson two-sided 95% intervals are calculated teaching aids: 5/10 gives 23.7–76.3%; 10/10 gives 72.2–100%. They require comparable independent Bernoulli attempts; those assumptions and field representativeness are not established by this paper. Cite R03 for the method, not for the experimental counts.

## R01: a plausible answer can still miss an engineering issue

[AgentiGrid, v1](https://arxiv.org/pdf/2609.04544v1), Table III and discussion on PDF pages 4–5, gives 12 searches: four backends times three applications on one synthetic 200-bus grid. These are not 12 repetitions of one task. In the four security-constrained runs, all four identify the economic critical outage (reported cost impact +21.6%), three identify one infeasible outage, and none identify the second. Keep the denominator as four backend runs, not an estimated probability.

Reported PFLOW cost reductions of 36.9% and 34.9% come from unit commitment when the requested action was dispatch optimization. Show this as a scope violation, not a successful improvement. Wall times and tokens describe the stated hardware and settings, not general runtime guarantees. Full row data are preserved in JSON.

## Suggested teaching sequence

1. Show the eight measured R02 counts with explicitly calculated intervals; leave unquantified regions unplotted.
2. Walk through an R01 failure: the solver may correctly evaluate the submitted cases while the agent omits a relevant case or misstates the conclusion.
3. Define two validation stages: numerical result validity for the supplied model and constraints; then task interpretation, scenario coverage and authorization. A framework can automate execution and records without establishing either stage automatically.

## Statistical illustrations, not empirical grid results

For zero observed failures in `n` independent fixed-setting Bernoulli trials, the one-sided exact 95% upper failure bound is `1 - 0.05^(1/n)`. It is 25.9% for n=10, 13.9% for n=20, 2.95% for n=100 and 0.994% for n=300. This is derived by setting the zero-failure probability `(1-p)^n` to 0.05. Cite R04 for the exact binomial method. It does not cover unknown operating conditions or correlated errors.

The separate serial-step illustration `q^L` assumes independent steps of identical correctness probability. With hypothetical q=0.98, all-step correctness is 98.0%, 90.4%, 81.7% and 66.8% for L=1,5,10,20. Label it an illustrative model; do not attach a research-paper model or utility name.

## Quantitative Harvard-affiliated research option

POPPER's Table 3 (PDF page 6) reports means and standard deviations over five independent runs, separating false positives from power. This offers a research lesson about explicit error budgets, but a biomedical benchmark would distract from the two directly relevant grid papers. The tutorial can explain the error-control principle without adding another performance chart. Do not turn a nominal error guarantee under stated assumptions into a grid-readiness claim.

## Source handling

`rigor_source_additions.json` contains R03/R04 only, ready for the parent's source registry merge. R01 and R02 already exist in the registry and retain their fixed v1 URLs. No production-deployment claim follows from any of these experimental numbers.
