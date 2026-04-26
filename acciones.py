import yfinance as yf
from datetime import timedelta
 
class Acciones:
    def __init__(self, ticker):
        self.ticker = ticker
 
    def obtener_datos_dia(self, fecha):
        data = yf.download(self.ticker, start=fecha, end=fecha + timedelta(days=1), actions=True, progress=False)
 
        if not data.empty:
            try:
                close = float(data['Close'].iloc[0].item())
                low = float(data['Low'].iloc[0].item())
                high = float(data['High'].iloc[0].item())
 
                dividendo = 0.0
                if 'Dividends' in data.columns:
                    dividendo = float(data['Dividends'].iloc[0].item())
 
                return {
                    "close": close,
                    "low": low,
                    "high": high,
                    "dividendo": dividendo
                }
            except Exception as e:
                return None
        return None