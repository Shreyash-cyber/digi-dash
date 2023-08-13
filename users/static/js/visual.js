const chartContainer = d3.select("#chartContainer")
.append("svg")
.attr("width", 400)
.attr("height", 300);

const chartTypeSelect = document.getElementById("chartType");

function updateChart(selectedChartType) {
chartContainer.selectAll("*").remove(); // Clear previous chart

if (selectedChartType === "bar") {
  const barChartSvg = d3.select("#barChart")
  .append("svg")
  .attr("width", 400)
  .attr("height", 300);

const barXScale = d3.scaleBand()
  .domain(jsonData.map(d => d.label))
  .range([0, 300])
  .padding(0.1);

const barYScale = d3.scaleLinear()
  .domain([0, d3.max(jsonData, d => d.value)])
  .range([250, 0]);

barChartSvg.selectAll(".bar")
  .data(jsonData)
  .enter().append("rect")
  .attr("class", "bar")
  .attr("x", d => barXScale(d.label))
  .attr("y", d => barYScale(d.value))
  .attr("width", barXScale.bandwidth())
  .attr("height", d => 250 - barYScale(d.value));

} else if (selectedChartType === "line") {
  const lineChartSvg = d3.select("#lineChart")
  .append("svg")
  .attr("width", 400)
  .attr("height", 300);

const lineXScale = d3.scaleBand()
  .domain(jsonData.map(d => d.label))
  .range([0, 300]);

const lineYScale = d3.scaleLinear()
  .domain([0, d3.max(jsonData, d => d.value)])
  .range([250, 0]);

const line = d3.line()
  .x(d => lineXScale(d.label) + lineXScale.bandwidth() / 2)
  .y(d => lineYScale(d.value));

lineChartSvg.append("path")
  .datum(jsonData)
  .attr("class", "line")
  .attr("d", line);

} else if (selectedChartType === "pie") {
   const pieChartSvg = d3.select("#pieChart")
.append("svg")
.attr("width", 400)
.attr("height", 300);

const pie = d3.pie()
.value(d => d.value);

const pieColors = d3.scaleOrdinal(d3.schemeCategory10);

const pieArc = d3.arc()
.innerRadius(0)
.outerRadius(150);

const pieChart = pieChartSvg.append("g")
.attr("transform", "translate(200, 150)");

const pieData = pie(jsonData);

pieChart.selectAll("path")
.data(pieData)
.enter().append("path")
.attr("d", pieArc)
.attr("fill", (d, i) => pieColors(i))
.attr("stroke", "white")
.attr("stroke-width", 2);
}
}

chartTypeSelect.addEventListener("change", function() {
const selectedChartType = chartTypeSelect.value;
updateChart(selectedChartType);
});

// Initial chart render
updateChart("bar");