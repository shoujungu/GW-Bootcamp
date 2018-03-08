var svgWidth = 700;
var svgHeight = 700;

var margin = { top: 20, right: 50, bottom: 60, left: 50 };

var w = svgWidth - margin.left - margin.right;
var h = svgHeight - margin.top - margin.bottom;

var svg=d3.select("body").append("svg")
          .attr("width", w)
          .attr("height", h);

d3.csv('data.csv', function(error, data){
  if (error) throw error;

  let x_min=d3.min(data,function(data){return +data.asian_ratio;});
  let x_max=d3.max(data,function(data){return +data.asian_ratio;});
  let y_min=d3.min(data,function(data){return +data.depression;});
  let y_max=d3.max(data,function(data){return +data.depression;});
  let xscale = d3.scaleSqrt()
                .domain([0, x_max+10])
                .range([0,500]);
  let yscale = d3.scaleLinear()
                 .domain([0, y_max+15])
                 .range([500,0]);

  let circles=svg.selectAll('circle')
                 .data(data)
                 .enter()
                 .append('circle')
                 .attr('cx', function(d){return xscale(d.asian_ratio)+40;})
                 .attr('cy', function(d){return yscale(d.depression);})
                 .attr('r',8)
                 .attr('fill','rgba(128,128,128,0.5)');

  let texts=svg.selectAll('text')
               .data(data)
               .enter()
               .append('text')
               .text(function(data){return data.abbr;})
               .attr('x',function(d){return xscale(d.asian_ratio)+40;})
               .attr('y', function(d){return yscale(d.depression);})
               .attr("font-size", "7px")
               .attr("text-anchor", "middle");

  let xaxis=d3.axisBottom().scale(xscale);
  svg.append('g')
     .attr("class", "axis")
     .attr("transform", `translate(40,${h-50})`)
     .call(xaxis);

  svg.append('text')
     .attr("transform", `translate(${w/2}, ${h})`)
     .style("text-anchor", "middle")
     .text("Asian Ratio");

  let yaxis=d3.axisLeft().scale(yscale);
  svg.append('g')
     .attr("class", "axis")
     .attr("transform", `translate(40,${h-550})`)
     .call(yaxis);

})
