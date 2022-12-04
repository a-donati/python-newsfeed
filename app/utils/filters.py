# use jinja "filters" to filter info through template and reformat date etc
def format_date(date):
  return date.strftime('%m/%d/%y')