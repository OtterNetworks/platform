class ModelConflict(Exception):
  def __init__(self, model):
    self.model = model
