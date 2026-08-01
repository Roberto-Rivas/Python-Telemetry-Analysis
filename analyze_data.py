import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('log.csv')

#plotting time and altitude
plt.figure()
plt.plot (df['time_ms'], df['altitude_m'])
plt.xlabel ('time (ms)')
plt.ylabel('altitude (m)')
plt.show()

#plotting time and acceleration
plt.figure()
plt.plot (df['time_ms'], df['accel_x'], label = 'acceleration X')
plt.plot (df['time_ms'], df['accel_y'], label = 'acceleration Y')
plt.plot (df['time_ms'], df['accel_z'], label = 'acceleration Z')
plt.xlabel ('time (ms)')
plt.ylabel('acceleration (m/s^2)')
plt.legend()
plt.show()

#plotting time and gyroscope
plt.figure()
plt.plot (df['time_ms'], df['gyro_x'], label = 'gyroscope X')
plt.plot (df['time_ms'], df['gyro_y'], label = 'gyroscope Y')
plt.plot (df['time_ms'], df['gyro_z'], label = 'gyroscope Z')
plt.xlabel ('time (ms)')
plt.ylabel('gyroscope (deg/s)')
plt.legend()
plt.show()      

#plotting time and temperature/humidity
fig, ax1 = plt.subplots()

ax1.plot(df['time_ms'], df['temp_sht'], color='red')
ax1.set_xlabel('Time (ms)')
ax1.set_ylabel('Temperature (°C)', color='red')

ax2 = ax1.twinx()
ax2.plot(df['time_ms'], df['humidity'], color='blue')
ax2.set_ylabel('Humidity (%)', color='blue')
plt.show()