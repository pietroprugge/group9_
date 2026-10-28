# Daneel — Computational Astrophysics 2026–27

A teaching package for modelling exoplanet transits and building detection
pipelines. 

Original documentation: <https://tiziano1590.github.io/comp_astro_26/>.

This repository contains the course example code, a runnable CLI,
and Sphinx documentation.

## Installation

### Prerequisites

- Python >= 3.10

### Install from source

```bash
git clone https://github.com/pietroprugge/group9_.git
cd group9_
pip install .
```

### Development installation

```bash
pip install -e '.[dev,docs]'
```

## Usage

After installation, you can run daneel from the command line:

```bash
daneel -i <input_file> --transit [--output planet.png]
```

### Command-line options

- `-i, --input`: Input parameter file (required)
- `-t, --transit`: Generate a transit light curve from the YAML input
- `-d, --detect`: Reserved for the course detection exercise
- `-a, --atmosphere`: Reserved for the course atmosphere exercise
- `-o, --output`: Output path for the transit plot (default: `lc.png`)

### Examples

```bash
# Run exoplanet detection and create a transit light curve
daneel -i examples/params.yaml --transit --output planet.png

# Run atmospheric characterization
daneel -i examples/params.yaml --detect

# Run both detection and atmospheric analysis
daneel -i examples/params.yaml --atmosphere
```

## Input File Format

The input file should be a YAML file containing the necessary parameters for the analysis.

## Development

Run the test suite and style checks with:

```bash
pytest
ruff check .
```

Build the documentation with `make -C docs html`.

## License

This project is licensed under the GNU General Public License v3.0.

## Authors

Tiziano Zingales (tiziano.zingales@unipd.it) (Professor of the course)

Pietro Ruggeri (pietro.ruggeri@studenti.unipd.it)
Matteo Oberti (matteo.oberti@studenti.unipd.it)
Stefano Bisignani (stefano.bisignani@studenti.unipd.it)
Nunzio Viola (nunzio.viola@studenti.unipd.it)
