//Função para buscar dados da API
async function getstockData() {
    const response = await fetch('https://finance.yahoo.com/quote/$%7Bticker%7D?p=${ticker}`','https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=UPV0BW801OBD78NA') //url das apis para monitoaramento
    const data = await response.json();

    const table = document.getElementById('stocksTable');

    data.foreaEach(stock => {
        const row = document.createElement('tr');
        row.innerHTML = `
        <td>${stock.name}<td>
        <td>${stock.current_price}</td>
        <td>${stock.variation}%</td>

    `;
    table.appendChild(row);

    });
    
}

//atualizar dados a cada 5 minutos
setInterval(getstockData, 300000);
getstockData();
