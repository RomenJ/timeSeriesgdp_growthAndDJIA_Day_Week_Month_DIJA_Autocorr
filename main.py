import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf

def load_data(file_path, index_col='date'):
    """
    Carga datos desde un archivo CSV y establece la columna de fechas como índice.
    
    Args:
    file_path (str): Ruta del archivo CSV.
    index_col (str): Nombre de la columna de fechas. Por defecto, 'date'.
    
    Returns:
    DataFrame: Datos cargados con la columna de fechas como índice.
    """
    data = pd.read_csv(file_path, parse_dates=['date'], index_col=index_col)
    return data

def plot_data(data, title=''):
    """
    Grafica los datos.
    
    Args:
    data (DataFrame): Datos a graficar.
    title (str): Título del gráfico. Por defecto, vacío.
    """
    plt.figure(figsize=(10, 6))
    sns.set_style("whitegrid") 
    sns.lineplot(data=data, palette="tab10", linewidth=2.5)
    plt.title(title)
    plt.xlabel('Fecha')
    plt.ylabel('Valor')
    plt.legend(title='Variables', loc='upper left')
    filename_with_extension = f"{title}.png"
    plt.savefig(filename_with_extension)
    plt.show()

def main():
    # Cargar datos de crecimiento del PIB
    gdp_growth = load_data('gdp_growth.csv')
    
    # Visualizar datos de crecimiento del PIB
    print("Información de crecimiento del PIB:")
    print(gdp_growth.info())
    print(gdp_growth.head(10))
  

    # Remuestrear datos del PIB a frecuencia diaria y visualizar
    gdp_growth_daily = gdp_growth.asfreq('D')
    plot_data(gdp_growth_daily, title='Crecimiento del PIB (Diario)')
    
  # Remuestrear datos del PIB a frecuencia mensual y visualizar
   
    gdp_growth_weekly = gdp_growth.resample(rule='W').first()
    plot_data(gdp_growth_weekly, title='Crecimiento del PIB (Semanal)')
    
    
    # Remuestrear datos del PIB a frecuencia mensual y visualizar
    #borrar in the future: gdp_growth_monthly = gdp_growth.asfreq('M').first()
    gdp_growth_monthly = gdp_growth.resample(rule='M').first()

    plot_data(gdp_growth_monthly, title='Crecimiento del PIB (Mensual)')
   
    #Resamplear datos del PIB a frecuencia anual y visualizar
   
    gdp_growth_yearly = gdp_growth.resample(rule='A').first()

    plot_data(gdp_growth_yearly, title='Crecimiento del PIB (ANUAL)')
    
    
    # Cargar datos del Dow Jones Industrial Average (DJIA)
    djia = load_data('djia.csv')
    
    # Visualizar datos del DJIA
    print("Información del Dow Jones Industrial Average (DJIA):")
    print(djia.info())
    
    plot_data(djia, title='Dow Jones Industrial Average (DJIA) Diario')
    
    # Remuestrear datos del DJIA a frecuencia semanal y visualizar
    djia_weekly = djia.resample(rule='W').first()
    plot_data(djia_weekly, title='Dow Jones Industrial Average (Semanal)')
    
    # Remuestrear datos del DJIA a frecuencia mensual y visualizar
    djia_monthly = djia.resample(rule='M').first()
    plot_data(djia_monthly, title='Dow Jones Industrial Average (Mensual)')
    
    # Remuestrear datos del DJIA anual  y visualizar
    djia_monthly = djia.resample(rule='A').first()
    plot_data(djia_monthly, title='Dow Jones Industrial Average (Anual)')
    
    # Calcular los retornos trimestrales del DJIA y concatenar con el crecimiento del PIB
    djia_quarterly = djia.resample('QS').last()
    djia_quarterly_return = djia_quarterly.pct_change().mul(100)
    data = pd.concat([gdp_growth, djia_quarterly_return], axis=1)
    data.columns = ['Crecimiento del PIB', 'Retornos Trimestrales del DJIA']
    
    # Visualizar los retornos trimestrales del DJIA y el crecimiento del PIB
    plot_data(data, title='Retornos Trimestrales del DJIA y Crecimiento del PIB')


    #Calcular la autocorrelación de sendos datases.
    
    # Plot autocorrelation function of  gdp_growth
    sns.set_style("whitegrid") 
    plot_acf(gdp_growth, lags=20)
    plt.title('Autocorrelación de GDG (gdp_growth, lags=20) ')
    plt.savefig('Autocorrelación de GDG (gdp_growth, lags=20).jpg')
    plt.show()


    
if __name__ == "__main__":
    main()
