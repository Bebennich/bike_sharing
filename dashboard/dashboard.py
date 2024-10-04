import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load datasets
day_data = pd.read_csv('https://raw.githubusercontent.com/Bebennich/bike-sharing-rifqi/refs/heads/main/day.csv')
hour_data = pd.read_csv('https://raw.githubusercontent.com/Bebennich/bike-sharing-rifqi/refs/heads/main/hour.csv')

# Preprocessing day_data
day_data['dteday'] = pd.to_datetime(day_data['dteday'])
day_data['year'] = day_data['dteday'].dt.year
day_data['month'] = day_data['dteday'].dt.month  # Menambahkan bulan ke day_data

# Preprocessing hour_data
hour_data['dteday'] = pd.to_datetime(hour_data['dteday'])
hour_data['year'] = hour_data['dteday'].dt.year
hour_data['hour'] = hour_data['dteday'].dt.hour

# Visualization 1: Tren Penggunaan Sepeda Tahunan
plt.figure(figsize=(15, 6))
sns.lineplot(x='dteday', y='cnt', data=day_data, marker='o', color='#3498db')
plt.title('Total Penyewaan Sepeda per Hari')
plt.xlabel('Tanggal')
plt.ylabel('Jumlah Penyewaan')
plt.axhline(y=day_data['cnt'].mean(), color='#e74c3c', linestyle='--', label='Mean Penyewaan')
plt.legend()
plt.grid()
plt.show()

# Visualization 2: Heatmap Penggunaan Sepeda per Jam
heatmap_data = hour_data.pivot_table(index='hour', columns=hour_data['dteday'].dt.date, values='cnt', aggfunc='sum')
plt.figure(figsize=(15, 6))
sns.heatmap(heatmap_data, cmap="YlGnBu", cbar_kws={'label': 'Jumlah Penyewaan'})
plt.title('Heatmap Penyewaan Sepeda per Jam')
plt.xlabel('Hari')
plt.ylabel('Jam')
plt.show()

# Visualization 3: Penggunaan Sepeda per Month
plt.figure(figsize=(10, 6))
seasonal_trends.plot(kind='bar', color='#3498db')
plt.title('Rata-rata Penyewaan Sepeda per Bulan')
plt.xlabel('Bulan')
plt.ylabel('Rata-rata Penyewaan')
plt.axhline(y=seasonal_trends.mean(), color='#e74c3c', linestyle='--', label='Mean Penyewaan')
plt.xticks(ticks=range(0, 12), labels=[str(m) for m in range(1, 13)], rotation=0)
plt.legend()
plt.grid()
plt.show()

# Faktor Cuaca
# Menghitung korelasi antara jumlah penyewaan dan faktor cuaca
weather_factors = hour_data[['season','temp','weathersit', 'windspeed', 'cnt']]  # Mengambil kolom cuaca dan cnt
correlation_weather = weather_factors.corr()['cnt'].sort_values(ascending=False)

# Menampilkan hasil korelasi
print("Korelasi dengan Faktor Cuaca:")
print(correlation_weather)

# Visualisasi: Matriks Korelasi
plt.figure(figsize=(8, 6))
sns.heatmap(weather_factors.corr(), annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Matriks Korelasi antara Penyewaan Sepeda dan Faktor Cuaca')
plt.show()

# Menampilkan faktor cuaca dengan pengaruh terbesar
strongest_factor = correlation_weather.index[1]  # Mengambil faktor dengan pengaruh terbesar setelah 'cnt'
strongest_correlation = correlation_weather.iloc[1]
print(f"Faktor cuaca yang memiliki pengaruh terbesar terhadap jumlah penyewaan sepeda: {strongest_factor} dengan korelasi {strongest_correlation:.2f}")