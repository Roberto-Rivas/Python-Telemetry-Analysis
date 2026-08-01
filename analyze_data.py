import pandas as pd
import matplotlib.pyplot as plt

# Load the data
df = pd.read_csv('log.csv')

# Convert time from ms to seconds for readability
df['time_s'] = df['time_ms'] / 1000.0

# 1. Altitude vs Time
plt.figure()
plt.plot(df['time_s'], df['altitude_m'])
plt.xlabel('Time (s)')
plt.ylabel('Altitude (m)')
plt.title('Altitude vs Time')
plt.grid(True)
plt.savefig('altitude_plot.png')

# 2. Acceleration (X, Y, Z) vs Time
plt.figure()
plt.plot(df['time_s'], df['accel_x'], label='X')
plt.plot(df['time_s'], df['accel_y'], label='Y')
plt.plot(df['time_s'], df['accel_z'], label='Z')
plt.xlabel('Time (s)')
plt.ylabel('Acceleration (m/s²)')
plt.title('Acceleration vs Time')
plt.legend()
plt.grid(True)
plt.savefig('acceleration_plot.png')

# 3. Gyro (X, Y, Z) vs Time
plt.figure()
plt.plot(df['time_s'], df['gyro_x'], label='X')
plt.plot(df['time_s'], df['gyro_y'], label='Y')
plt.plot(df['time_s'], df['gyro_z'], label='Z')
plt.xlabel('Time (s)')
plt.ylabel('Angular Velocity (rad/s)')
plt.title('Gyroscope vs Time')
plt.legend()
plt.grid(True)
plt.savefig('gyro_plot.png')

# 4. Temperature and Humidity vs Time
fig, ax1 = plt.subplots()
ax1.plot(df['time_s'], df['temp_sht'], color='tab:red', label='Temp (°C)')
ax1.set_xlabel('Time (s)')
ax1.set_ylabel('Temperature (°C)', color='tab:red')
ax1.tick_params(axis='y', labelcolor='tab:red')

ax2 = ax1.twinx()
ax2.plot(df['time_s'], df['humidity'], color='tab:blue', label='Humidity (%)')
ax2.set_ylabel('Humidity (%)', color='tab:blue')
ax2.tick_params(axis='y', labelcolor='tab:blue')

plt.title('Temperature & Humidity vs Time')
fig.tight_layout()
plt.savefig('temp_humidity_plot.png')

print("All plots saved as PNG files in this folder.")
plt.show()