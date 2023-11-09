var xValues = ["Jeb",'Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
var yValues = [45, 69, 40, 64, 35, 84, 54, 14, 44, 70, 45, 60, 100];
var barColors = ["red", "green","blue","orange","brown","red", "green","blue","orange","brown","orange","brown"];

new Chart("myChart1", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      backgroundColor: barColors,
      data: yValues
    }]
  },
  options: {
    legend: {display: false},
    title: {
      display: true,
      text: "Order Users"
    }
  }
});
