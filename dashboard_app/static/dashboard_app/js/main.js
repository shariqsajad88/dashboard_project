// dashboard_app/static/dashboard_app/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    fetch('/api/data/')
        .then(response => response.json())
        .then(data => {
            // Create charts using D3.js
            createCharts(data);
        });

    function createCharts(data) {
        // Example D3 chart
        const svg = d3.select("#charts").append("svg")
            .attr("width", 600)
            .attr("height", 400);

        svg.selectAll("circle")
            .data(data)
            .enter()
            .append("circle")
            .attr("cx", (d, i) => i * 50 + 50)
            .attr("cy", 200)
            .attr("r", d => d.intensity)
            .attr("fill", "blue");
    }

    document.getElementById('year-filter').addEventListener('change', function() {
        const year = this.value;
        // Refetch and update charts based on selected year
    });
    
});
