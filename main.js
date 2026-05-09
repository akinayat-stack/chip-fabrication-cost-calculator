function renderResult(data) {
  const result = document.getElementById('result');
  const yieldPercent = (data.yield || 0) * 100;
  const statusClass = yieldPercent >= 80 ? 'good' : 'bad';
  const statusText = yieldPercent >= 80 ? 'Healthy Yield' : 'Yield Risk';

  result.innerHTML = `
    <div class="metric">
      <div class="label">Cost per Die</div>
      <div class="value">$${formatNum(data.costPerDieUsd, 2)}</div>
    </div>
    <div class="metric">
      <div class="label">Dies per Wafer</div>
      <div class="value">${formatNum(data.diesPerWafer, 2)}</div>
    </div>
    <div class="metric">
      <div class="label">Good Dies per Wafer</div>
      <div class="value">${formatNum(data.goodDiesPerWafer, 2)}</div>
    </div>
    <div class="metric">
      <div class="label">Yield</div>
      <div class="value">${formatNum(yieldPercent, 2)}% <span class="badge ${statusClass}">${statusText}</span></div>
    </div>
    <div class="metric">
      <div class="label">Model Used</div>
      <div class="value">${data.yieldModelUsed}</div>
    </div>
  `;
}
