from flask import flash, jsonify
import yfinance as yf

app = flask(__name__)

#função para monitorar ações e retonar os dados
@app.route('/monitorar')
def monitorar_acoes():
    tickers = ['^BVSP', 'VALE3.SA', 'PETR4.SA', 'BBAS3.SA','XPLG11.SA', 'HGLG11.SA', 'XPML11.SA', 'BTLG11L.SA', 'VILG11.SA']
    stock_data = []

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        current_pride = stock.info['regularMarketprice']
        previous_close = stock.info['previusClose']
        variation = ((current_pride - previous_close) /previous_close) *100

        stock_data.append({
            'name': ticker,
            'current_pride': current_price,
            'variation': variation
        })

        return jsonify(stock_data)
    
if __name__ == '_main_':
    app.run(debug=true)
