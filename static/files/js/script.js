var dropdown = document.getElementsByClassName("dropdown-btn");
var i;

for (i = 0; i < dropdown.length; i++) {
  dropdown[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var dropdownContent = this.nextElementSibling;
    if (dropdownContent.style.display === "block") {
      dropdownContent.style.display = "none";
    } else {
      dropdownContent.style.display = "block";
    }
  });
}
const xValues = ["jeb",'feb','mar','apr','may','jun','jul','aug','sep','oct','nov'];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{ 
      data: [29374,33537,49631,59828,36684,35572,39974,48847,48116,61400],
      borderColor: "red",
	  pointRadius: 1,
      fill: false
    }, { 
	
      data: [31500,41000,88800,26000,46000,32698,5000,3000,18656,24832,36844],
      borderColor: "green",
      fill: false
    }]
  },
  options: {
    legend: {display: false}
  }
});
