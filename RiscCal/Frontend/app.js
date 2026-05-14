let myChart = null;

async function analyzeStock() {
    let ticker = document.getElementById('tickerInput').value.trim().toUpperCase();
    if (!ticker) return;

    // Aliases for Vedanta, HCL, and Tata Motors
    if (ticker === "VEDANTA") ticker = "VEDL";
    if (ticker === "HCL") ticker = "HCLTECH";
    if (ticker === "TATA MOTORS") ticker = "TATAMOTORS";
    if (!ticker.includes('.') && isNaN(ticker)) ticker += ".NS";

    const btn = document.getElementById('analyzeBtn');
    btn.innerText = "Scanning...";

    try {
        const response = await fetch('http://127.0.0.1:5000/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ stock: ticker })
        });
        const data = await response.json();
        
        if (data.error) { alert(data.error); return; }
        
        updateUI(data);
    } catch (err) {
        alert("Server not responding. Make sure python app.py is running!");
    } finally {
        btn.innerText = "Run Scan";
    }
}

function updateUI(data) {
    document.getElementById('resultArea').classList.remove('hidden');
    const riskCard = document.getElementById('riskCard');
    
    riskCard.classList.remove('is-risky');
    document.getElementById('priceDisplay').innerText = `₹${data.price}`;
    document.getElementById('riskScore').innerText = data.risk_score;
    document.getElementById('conclusion').innerText = data.conclusion;
    document.getElementById('high52Display').innerText = `₹${data.high_52w}`;
    document.getElementById('dropDisplay').innerText = `${data.drop_percent}%`;

    if (data.risk_score >= 50) riskCard.classList.add('is-risky');
    
    document.getElementById('reasons').innerHTML = data.reasons.map(r => `<li>${r}</li>`).join('');
    renderChart(data.chart.dates, data.chart.prices);
}

function renderChart(dates, prices) {
    const ctx = document.getElementById('priceChart').getContext('2d');
    if (myChart) myChart.destroy();
    myChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: dates,
            datasets: [{ label: 'Price', data: prices, borderColor: '#0066ff', fill: false }]
        }
    });
}