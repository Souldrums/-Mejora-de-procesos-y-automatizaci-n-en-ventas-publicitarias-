# Automatización de reportes de ventas publicitarias

import pandas as pd
import matplotlib.pyplot as plt

# Cargar datos
df = pd.read_csv('sales_data.csv')

# Limpiar datos (por si hay valores nulos)
df = df.dropna()

# Generar reporte resumen por plataforma
reporte = df.groupby('Platform').agg(
    Total_Revenue=('RevenueUSD', 'sum'),
    Sales_Count=('SaleID', 'count')
).reset_index()

print(reporte)

# Guardar reporte en CSV
reporte.to_csv('weekly_sales_report.csv', index=False)

# Visualizar ingresos por plataforma
plt.figure(figsize=(8,5))
plt.bar(reporte['Platform'], reporte['Total_Revenue'], color='skyblue')
plt.title('Ingresos totales por plataforma')
plt.xlabel('Plataforma')
plt.ylabel('Ingresos en USD')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('sales_by_platform.png')
plt.show()
