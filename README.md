# CSV Data Manipulator (csv\_datamanp)

This was created to facilitate data manipulation, data filtering and lastly data mapping when working with response data from a service.

> How to use script jump to [Getting Started](#getting-started)

Current workflow, is to manipulate data directly via software that is cell or table based and this is not an optimal solution. Since every operation is made by a human, and human makes mistakes, humans might not share procedures and humans are bad at verifying the results after an operation has been carried out.

So to streamline the process i.e. removing the human factor from these operations we can achieve a more fluid way of dealing with large amount of data and also test and expect certain outcomes when doing so.

## The Pros of Automating Data Pipelines

- The greatest gain is in time, a task that might take between 5-10 minutes can be reduced to mere seconds.
- Consistent workflow, procedure is not dependent on the user's knowledge of the software or the familiarity of a certain software.
- Consistent work quality, meaning that actions carried via a script is not altered during an action like e.g. copy/paste action or other human mishaps.
- Verification a good in-house scripting solution should be covered by a defined set tests and be limited to solve well-define issue.

## The Cons of Automating Data Pipelines

- Code and additional library dependency.
- Bus factor i.e. the amount of people that could understand and edit/maintain the code base, carries out automation.
- Overestimating gain of automatizing task, not all problems are meant to be sent through pipeline and one should think twice before starting code a solution.

Now that we have covered the caveats for this project we can start to code, what I believe to be simple enough issues and should result in great gains.

## The issues

- Removing non-alphanumeric characters from a data set i.e. only allow 0-9 and letters.
- Map old user identity to another identity, think dictionary key-value pairs.
- Subset a pool of user from a larger set of data.

# Python + Pandas = Data Science Tool

This will not come as a surprise that programming language is Python and that the additional library is Pandas. Both are used ubiquitously in the data science community and are often paired with other languages as R, MATLAB etc.

The reason for picking Python is the readability aspect of the syntax that would be lighter to digest than other programming languages for non-coders/programmers.

The reason for Pandas, is that it is a fairly mature library and would suffice for most use cases as a complement to software used currently in-house.

# Limitations

This will be command line driven project, since this is a hobby build and for a more user-friendly version i.e. GUI, I would need to dedicate more time and effort.

## Getting Started

Quick setup steps to run project.

### Clone Project

#### Step 1

```sh
git clone https://github.com/efpcode/csv_datamanp.git
```

#### Step 2

Change directory with command below.

```sh
cd csv_datamanp
```

### Install Dependencies

> ** Python 3.11 or newer is required.**

#### uv Installation

```sh
uv sync --locked
```

#### pip installation

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Run Tests

> If you use uv

```sh
uv run pytest
```

> If installed with pip

```sh
pytest tests/
```

### Launch IPython

> If you use uv

```sh
uv run ipython
```

> If installed with pip

```sh
ipython
```

### Import csv\_datamanp functions

```sh
from csv_datamanp.csv_data_manager import data_cleaner, data_subsetter, data_mapper
```

> Load data by importing pandas as pd and create a DataFrame.

- data_cleaner: removes non-alphanumeric data from a single column
- data_subsetter: locates smaller set of data from a larger dataset
- data_mapper: needs lookup table and target table to work.

### Example: Map migrated user identifiers

The lookup DataFrame represents the migration table containing the relationship between old and new user identifiers.

The target DataFrame represents the current production data that needs to be mapped. The target controls which accounts appear in the result because some accounts from the original migration may no longer exist in production.

```python
import pandas as pd

from csv_datamanp.csv_data_manager import data_mapper

df_lookup = pd.read_csv(
    "tests/test_data/look_up_dataset.csv",
)

df_target = pd.read_csv(
    "tests/test_data/look_up_outcome.csv",
    usecols=["Key"],
)

df_mapped = data_mapper(df_lookup, df_target.copy())

df_mapped.head()
```

Expected output:

```text
     Key Mapped Values
0  A1003         Z5003
1  A1011         Z5011
2  A1017         Z5017
3  A1014         Z5014
4  A1012         Z5012
```

Entries present in the migration lookup but absent from the target data are not included. A target identifier without a matching lookup value is marked as `Not Found`.
