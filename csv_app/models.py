

# # Create your models here.
# from django.db import models
# import pandas as pd

# def create_model_from_csv(file):
#     df = pd.read_csv(file)
#     attributes = {field: models.CharField(max_length=50) for field in df.columns}
#     attributes['__module__'] = __name__  # Set the module name where the model is defined

#     model = type('DynamicModel', (models.Model,), attributes)
#     return model



from django.db import models

def create_dynamic_model(name, fields):
    """
    Dynamically create a model with the given name and fields.
    """
    attrs = {'__module__': __name__, '__str__': lambda self: f"{name} instance"}
    attrs.update(fields)

    model = type(name, (models.Model,), attrs)
    return model


# from django.db import models

# def create_dynamic_model(name, fields):
#     """
#     Dynamically create a model with the given name and fields.
#     """
#     attrs = {'__module__': __name__, '__str__': lambda self: f"{name} instance"}
#     attrs.update(fields)

#     model = type(name, (models.Model,), attrs)
#     return model
