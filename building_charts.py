import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Считывание данных из CSV файла с использованием pandas
data = pd.read_csv(r'C:*******.csv', sep=';')

# Группировка данных по загрязнителям
grouped = data.groupby('pollutant')

# Построение графика
plt.figure(figsize=(10, 6))

# Список шаблонов для колонок (можно дополнить по желанию)
patterns = ['/', 'x', '\\', '|', '-', '+', 'o', 'O', '.', '*']

for idx, (name, group) in enumerate(grouped):
    plt.bar(group['pollutant'], group['Custom'], label=name, hatch=patterns[idx % len(patterns)], color='gray')



plt.title('Pollutants in Ukraine 1991 - 2021', fontweight='bold')  # Добавление жирного шрифта к названию
plt.xlabel('Pollutant')
plt.ylabel('Value')
plt.grid(False)
plt.xticks(rotation=45)
plt.tight_layout()

# Добавление легенды
plt.legend()

# Сохранение графика в формате TIFF с разрешением 300 DPI
plt.savefig('Fig.1.tif', dpi=300, format='tiff')

plt.show()
