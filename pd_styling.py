def set_caption(df, caption, loc="bottom"):
  df.set_caption(caption)\
  .set_table_styles([{
      'selector': 'caption',
      'props': f'caption-side: {loc}; font-size:1.25em;'
  }], overwrite=False)
  return df