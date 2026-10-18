# Feeder provenance and teaching overlays

## Original dataset and scope

The included electrical model is one feeder from **SMART-DS Synthetic Electrical Network Data OpenDSS Models for SFO, GSO, and AUS**. SMART-DS provides synthetic networks and load data intended for distribution-system research. The source explicitly supports working with a region, substation, or individual feeder.

**Citation:** Bryan Palmintier, Carlos Mateo Domingo, Fernando Emilio Postigo Marcos, Tomas Gomez San Roman, Fernando de Cuadra, Nicolas Gensollen, Tarek Elgindy, and Pablo Duenas (2020). *SMART-DS Synthetic Electrical Network Data OpenDSS Models for SFO, GSO, and AUS*. National Renewable Energy Laboratory, Open Energy Data Initiative. [Dataset and source links](https://data.openei.org/submissions/2981).

This tutorial includes the feeder identified by substation **uhs20_1247** and feeder **udt8894**. Its source directory within the provided local dataset was:

~~~text
SMARTDS_GSO_solar_extreme_batt_high_peak_opendss/
  uhs20_1247/
    uhs20_1247--udt8894/
~~~

The copied files are in greensboro_udt8894/. The original master file names the circuit feeder_udt8894-uhs20_1247x and defines a 12.47 kV source at 1.03 p.u.

The included data describe a **synthetic feeder in the Greensboro area**, not an actual utility network or the entire city. No utility operating claim or exact correspondence to real facilities is made.

## Spatial extent and inventory

Buscoords.dss contains 2,235 coordinate records. The source coordinates span:

| Coordinate | Minimum | Maximum |
|---|---:|---:|
| Longitude-like x, degrees | −79.888869 | −79.864662 |
| Latitude-like y, degrees | 36.116397 | 36.129471 |

These are the coordinate bounds read from the supplied file. They are useful for displaying the selected feeder's footprint. They are not a municipal boundary or a verified utility service-area boundary. The tutorial does not assign a neighborhood name or identify real critical facilities from these points.

The following counts refer to original object declarations, before generated teaching overlays and scenario disconnections:

| Object class | Count |
|---|---:|
| Load | 2,173 |
| PVSystem | 930 |
| Storage | 436 |
| Line | 1,977 |
| Transformer | 258 |

A coordinate-record count is not necessarily the number of active solved buses. Counts of generic “New” statements also include other object classes and should not be interpreted as device counts.

## Source preservation and preparation

The files in greensboro_udt8894/ are retained as the source inputs. The preparation function writes generated copies and records SHA-256 hashes in results/source_manifest.json.

Preparation updates retired property spellings where present and disables automatic solve/plot commands in the generated master file. The source files remain separate from those generated copies. Scenario settings and additional lines are then applied at runtime.

The AC-table manifest records source hashes and the relevant physics/control code. Checkpoint metadata additionally records training inputs and weights. These records support reproduction of the included experiment; they do not validate the source data against a field system.

## Runtime settings

For the main experiments:

- A scenario uses a uniform load multiplier and a common PV %Pmpp cap.
- Autonomous OpenDSS controls are disabled so the selected control candidates can be inspected.
- Storage objects are held in IDLING mode with external dispatch.
- Each candidate starts from a newly compiled/reset feeder.
- Grid-following PV and storage disconnected from the source are disabled. They do not form intentional islands in this model.
- The main cases use selected operating snapshots and a short known demand sequence. They do not reproduce the dataset's complete year of time-series operation.

These settings are experimental choices, not recommended operating settings.

## Artificial restoration overlay

The source bus is udt8894-uhs20_1247x. The isolated branch is l(r:udt8894-uhs20_1247), and both teaching bypasses connect the source bus to udt8894-uhs20_1247x_b1_1.

| Overlay | Definition | Purpose |
|---|---|---|
| Short bypass | Three-phase, 0.25 km; scenario-selected ampacity | Alternate supply for normal and constrained-capacity cases |
| Long bypass | Three-phase, 2.0 km; 400 A nominal ampacity | A second permitted route when available |
| Bypass impedances | r1 = 0.2, x1 = 0.3, r0 = 0.5, x0 = 0.6 ohm/km | Explicit illustrative line parameters |
| Outage | The selected original branch is disabled | Represent an isolated unavailable path |
| Critical-load labels | Every tenth load in the lexicographically sorted load list | Reproducible teaching priorities |
| Load-relay action | Disable the first stated fraction of the sorted noncritical-load list | Illustrate partial restoration when capacity is limited |

The normal restoration case uses a 400 A short bypass. The constrained case uses 100 A, removes PV availability, and marks the long bypass unavailable. A separate rating fraction, where used, changes the permitted current in the checks rather than changing line impedance.

The critical-load set is artificial. The chosen loads are not identified hospitals, shelters, or other real critical facilities. Noncritical shedding follows the declared list order; it is not a geographically optimized sectioning plan.

The individual-load relay assumption is stronger than the switching capability of many real feeders. The tutorial does not infer that such relays exist. For a practical restoration study, replace the overlay with documented switches and service zones, device ratings, phase connectivity, protection information, and allowed switching sequences.

The outage represents an isolated unavailable branch. Fault-current behavior, fault clearing, protection coordination, and transient restoration dynamics are not simulated by merely disabling it.

## Interpretation limits

Reported service is nominal connected load in kW, not measured customer delivery or integrated energy. Connectivity is evaluated at bus level, and the medium-voltage cycle check is not a complete phase-specific restoration certificate. The source OpenDSS model and teaching overlays must be treated as explicit assumptions in every result.

Use the dataset source above for citation and provenance. This document makes no additional licensing assertion.

