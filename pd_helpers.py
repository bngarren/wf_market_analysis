import pandas as pd
from datetime import datetime, timedelta, timezone

def get_modified_isd_df(df):
  cols = [
          'item_url_name_rank',
          'date',
          'name',
          'rank',
          'set',
          'number_of_sellers',
          'quantity_available',
          'mean_price',
          'median_price',
          'min_price',
          'min_3_price_avg',
          'avg_listed_time_new_3'
          ]
  decimals = pd.Series(1,
                      index=['number_of_sellers',
                              'quantity_available',
                              'mean_price',
                              'median_price',
                              'min_price',
                              'min_3_price_avg',
                              'avg_listed_time_new_3'
                              ])
  df = (df
        [cols]
          .assign(
            rank=lambda x: x["rank"].astype("Int64"), # allow NA values
            date=lambda x: x["date"].dt.normalize() # reset to midnight
          )
          .round(decimals) # round floats
        )
  return df

def get_item_df(iunr, df):
  """Get a single item's data.
  iunr -- item_url_name_rank
  df -- dataframe that includes the item
  @returns an item-specific df that is grouped by date (indexed to date)
  """
  filter = df["item_url_name_rank"] == iunr

  def set_name(df_partial):
    global name
    name = df_partial["name"].iloc[0]
    return df_partial

  return (pd.DataFrame(df[filter])
    .pipe(set_name) # want to get the item name and keep it for after the group by
    .groupby("date")
    .mean()
    .assign(name=name)
    )

### FILTERS

def get_filtered_by_time(df, days=7):
  ago = pd.Timestamp.now(tz=timezone.utc) + timedelta(days=days*-1)
  return df[df["date"] >= ago]

def get_filtered_by_listed_time_and_quant(df, max_listed = 500, min_quant=3):
  return df[(df["quantity_available"] >= min_quant) & (df["avg_listed_time_new_3"] <= max_listed)]

def get_filtered_by_sellers(df, min_sellers=2):
  return df[df["number_of_sellers"] >= min_sellers]

def get_filtered_by_min_3_price_avg(df, min_price=15):
  return df[df["min_3_price_avg"] >= min_price]