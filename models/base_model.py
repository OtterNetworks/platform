class BaseModel:
    def __init__(self):
        self._validators = []
        self.errors = {}

    def validate(self):
        self.errors = {}
        for v in self._validators:
            v.validate()

        invalid = filter(lambda x: not x.valid, self._validators)
        for v in invalid:
            if v.field_name not in self.errors.keys():
                self.errors[v.field_name] = []
            self.errors[v.field_name].append(v.error_message)

    def is_invalid(self):
        self.validate()
        # False if self.errors is empty. Otherwise, True
        return bool(self.errors)