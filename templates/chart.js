<meta charset="utf-8">
<title>Chart.js </title>

<!-- import plugin script -->
<script src="static/Chart.min.js"></script>
<h1>Flask Chart.js</h1>
<!-- bar chart canvas element -->
<canvas id="chart" width="600" height="400"></canvas>

<script></p>
<p>   // bar chart data<br />
   var barData = {<br />
   labels : [],<br />
   datasets : [<br />
      {<br />
            fillColor: "rgba(151,187,205,0.2)",<br />
            strokeColor: "rgba(151,187,205,1)",<br />
            pointColor: "rgba(151,187,205,1)",<br />
            pointStrokeColor: "#fff",<br />
            pointHighlightFill: "#fff",<br />
            pointHighlightStroke: "rgba(151,187,205,1)",<br />
            bezierCurve : false,<br />
            data : []<br />
      }]<br />
   }</p>
<p>    Chart.defaults.global.animationSteps = 50;<br />
    Chart.defaults.global.tooltipYPadding = 16;<br />
    Chart.defaults.global.tooltipCornerRadius = 0;<br />
    Chart.defaults.global.tooltipTitleFontStyle = "normal";<br />

 

    Chart.defaults.global.tooltipFillColor = "rgba(0,0,0,0.8)";<br />

 

    Chart.defaults.global.animationEasing = "easeOutBounce";<br />
    Chart.defaults.global.responsive = false;<br />
    Chart.defaults.global.scaleLineColor = "black";<br />
    Chart.defaults.global.scaleFontSize = 16;</p>
<p>   // get bar chart canvas<br />
   var mychart = document.getElementById("chart").getContext("2d");</p>
<p>   steps = 10<br />
   max = 10<br />
   // draw bar chart<br />
   var LineChartDemo = new Chart(mychart).Line(barData, {<br />
        scaleOverride: true,<br />
        scaleSteps: steps,<br />
        scaleStepWidth: Math.ceil(max / steps),<br />
        scaleStartValue: 0,<br />
        scaleShowVerticalLines: true,<br />
        scaleShowGridLines : true,<br />
        barShowStroke : true,<br />
        scaleShowLabels: true,<br />
        bezierCurve: false,</p>
<p>   });</p>
<p></script>