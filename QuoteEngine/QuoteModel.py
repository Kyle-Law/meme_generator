class QuoteModel(object):
  """
  A QuoteModel class.
  """
  def __init__(self,body,author):
    self.body = body
    self.author = author

  def __str__(self):
    return f"QuoteModel - '{self.body}' by {self.author}"
