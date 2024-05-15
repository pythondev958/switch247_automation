# from django.shortcuts import render
# from django.http import HttpResponse
# from django.db import connection
# import pandas as pd

# def upload_csv(request):
#     if request.method == "POST":
#         file = request.FILES['csvfile']
#         df = pd.read_csv(file)
        
#         # Generate a unique table name based on the file name or use a UUID
#         table_name = 'table_' + file.name.replace('.csv', '').replace(' ', '_').lower()
        
#         # Generate SQL to create a table
#         fields_sql = ', '.join([f'"{col}" VARCHAR(50)' for col in df.columns])
#         sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({fields_sql});'

#         with connection.cursor() as cursor:
#             cursor.execute(sql)

#         return HttpResponse(f"Table '{table_name}' created successfully!")
#     return render(request, 'upload.html')




# from django.shortcuts import render
# from django.http import HttpResponse
# from django.db import connection,models
# import pandas as pd
# from .models import create_dynamic_model

# def upload_csv(request):
#     if request.method == "POST":
#         file = request.FILES['csvfile']
#         df = pd.read_csv(file)

#         # Generate a unique model and table name
#         model_name = 'DynamicModel_' + file.name.replace('.csv', '').replace(' ', '_').lower()
#         table_name = model_name.lower()

#         # Create dynamic model
#         fields = {col: models.CharField(max_length=50) for col in df.columns}
#         dynamic_model = create_dynamic_model(model_name, fields)

#         # Generate SQL to create a table
#         fields_sql = ', '.join([f'"{col}" VARCHAR(50)' for col in df.columns])
#         sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({fields_sql});'

#         with connection.cursor() as cursor:
#             cursor.execute(sql)

#         return HttpResponse(f"Model and table '{table_name}' created successfully!")
#     return render(request, 'upload.html')






from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection,models
import pandas as pd
from .models import create_dynamic_model

def upload_csv(request):
    if request.method == "POST":
        file = request.FILES['csvfile']
        df = pd.read_csv(file)

        # Clean the file name to create a valid Python class name and SQL table name
        base_name = file.name.replace('.csv', '').replace(' ', '_').replace('-', '_').lower()
        model_name = ''.join([c for c in base_name.title() if c.isalnum()])
        table_name = base_name.lower()

        # Create dynamic model
        fields = {col.replace(' ', '_').replace('-', '_'): models.CharField(max_length=50) for col in df.columns}
        dynamic_model = create_dynamic_model(model_name, fields)

        # Generate SQL to create a table
        fields_sql = ', '.join([f'"{col.replace(' ', '_').replace('-', '_')}" VARCHAR(50)' for col in df.columns])
        sql = f'CREATE TABLE IF NOT EXISTS "{table_name}" ({fields_sql});'

        with connection.cursor() as cursor:
            cursor.execute(sql)

        return HttpResponse(f"Model and table '{table_name}' created successfully!")
    return render(request, 'upload.html')

