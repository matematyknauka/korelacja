import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Dane wejściowe
data = {
    'Długość serii (szt.)': [80, 90, 100, 100, 110, 120],
    'Koszt jednostkowy (zł)': [12, 9, 10, 9, 8, 6]
}

# Tworzenie DataFrame
df = pd.DataFrame(data)

# Obliczanie współczynnika korelacji Pearsona
correlation = df.corr().iloc[0, 1]
print(f"Współczynnik korelacji Pearsona: {correlation:.2f}")

# Tworzenie wykresu
plt.figure(figsize=(8, 5))
plt.scatter(df['Długość serii (szt.)'], df['Koszt jednostkowy (zł)'], color='blue')
plt.title('Zależność między długością serii a kosztem jednostkowym')
plt.xlabel('Długość serii (szt.)')
plt.ylabel('Koszt jednostkowy (zł)')
plt.grid(True)

# Dodawanie linii regresji
m, b = np.polyfit(df['Długość serii (szt.)'], df['Koszt jednostkowy (zł)'], 1)
plt.plot(df['Długość serii (szt.)'], m * df['Długość serii (szt.)'] + b, color='red')

plt.show()
