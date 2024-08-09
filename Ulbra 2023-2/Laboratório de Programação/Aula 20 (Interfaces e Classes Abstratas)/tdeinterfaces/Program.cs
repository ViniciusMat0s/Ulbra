SensorDeTemperatura Sensor = new SensorDeTemperatura();
Sensor.LerValor();

SensorDePressao SensorPressao = new SensorDePressao();
SensorPressao.LerValor();

Console.WriteLine($"{Sensor.LerValor()} e {SensorPressao.LerValor()}");