
from main import get_exchange_rate

def main():
    data = get_exchange_rate()
    if data:
        usd_rate = data['cambio'][0]['venta']
        print(f'La tasa de cambio del USD a PEN es: {usd_rate}')
    else:
        print('No se pudo obtener la tasa de cambio')

if __name__ == '__main__':
    main()