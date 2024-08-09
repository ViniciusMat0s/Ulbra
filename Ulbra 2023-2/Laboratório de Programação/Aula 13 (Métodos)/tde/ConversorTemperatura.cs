// Classe: ConversorTemperatura
// Atributos: temperaturaCelsius
// Método: ConverterParaFahrenheit()
// Descrição: Crie um método que retorne a temperaturaCelsius convertida para Fahrenheit.

class ConversorTemperatura
{
    public double temperaturaCelsius;
    public double ConverterParaFahrenheit()
    {
        double fahrenheit =  temperaturaCelsius * 1.8 + 32;
        return fahrenheit;
    }
}

