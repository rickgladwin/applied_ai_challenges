from pandas import Timestamp
from pandera import DataFrameSchema, Column, Check, Index, MultiIndex

schema = DataFrameSchema(
    columns={
        "Date": Column(
            dtype="datetime64[ns]",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=Timestamp("2017-07-01 00:00:00"),
                    raise_warning=False,
                    ignore_na=True,
                ),
                Check.less_than_or_equal_to(
                    max_value=Timestamp("2017-12-31 23:45:00"),
                    raise_warning=False,
                    ignore_na=True,
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed48M": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.79, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=16.12, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed100M": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.81, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=18.45, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed152M": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.82, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=19.79, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_direction48M": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=359.75, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_direction100M": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=360.0, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_direction152M": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=360.0, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed_100MP10": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=16.57, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed_100MP20": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=17.2, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed_100MP30": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.26, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=17.54, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed_100MP40": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.5, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=17.98, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed_100MP50": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.83, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=18.46, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed_100MP60": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=1.23, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=18.78, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed_100MP70": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=1.53, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=19.27, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed_100MP80": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=1.92, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=20.09, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "wind_speed_100MP90": Column(
            dtype="float64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=2.37, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=21.35, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "Interpolated": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=0.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=1.0, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "available_capacity": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=91800.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=122400.0, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
        "Output": Column(
            dtype="int64",
            checks=[
                Check.greater_than_or_equal_to(
                    min_value=-976.0, raise_warning=False, ignore_na=True
                ),
                Check.less_than_or_equal_to(
                    max_value=120460.0, raise_warning=False, ignore_na=True
                ),
            ],
            nullable=False,
            unique=False,
            coerce=False,
            required=True,
            regex=False,
            description=None,
            title=None,
        ),
    },
    checks=None,
    index=Index(
        dtype="int64",
        checks=[
            Check.greater_than_or_equal_to(
                min_value=0.0, raise_warning=False, ignore_na=True
            ),
            Check.less_than_or_equal_to(
                max_value=17667.0, raise_warning=False, ignore_na=True
            ),
        ],
        nullable=False,
        coerce=False,
        name=None,
        description=None,
        title=None,
    ),
    dtype=None,
    coerce=True,
    strict=False,
    name=None,
    ordered=False,
    unique=None,
    report_duplicates="all",
    unique_column_names=False,
    add_missing_columns=False,
    title=None,
    description=None,
)
