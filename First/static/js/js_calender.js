function myFunction(){
  			var person = prompt("Please enter your name", "Your Name");
  			if (person != null) {
    		document.getElementById("namelabel").innerHTML=person+"'\s Calender"
  			}
		}
 		function doit(){
 			var j=1;
 			for(j=1;j<=42;j++){
 					document.getElementById(String(j)).innerText=" ";
 			}
 			var i=1;
 			var monthselected=parseInt(document.getElementById("month").value);
 			var yearselected=parseInt(document.getElementById("year").value);
 			console.log(yearselected);
 			var dateselected=new Date(yearselected,monthselected,1,0,0,0);
 			var theday=dateselected.getDay();
 			var days=showdays(monthselected,yearselected);
 			var inr=1;
 			for(i=1;i<=days;i++){
 					document.getElementById(String(theday)).innerText=i;
 					theday++;
 			}
 			console.log(String(identity));
 		}
 		function showtoday(){
 			var j=1;
 			for(j=1;j<=42;j++){
 					document.getElementById(String(j)).innerText=" ";
 			}
 			var i=1;
 			var datesel=new Date();
 			var dateselected=datesel.getDate();
 			var theday=dateselected.getDay();
 			cansole.log(dateselected,theday);
 			var days=showdays(dateselected.getMonth(),dateselected.getFullYear());
 			var inr=1;
 			for(i=1;i<=days;i++){
 					document.getElementById(String(theday)).innerText=i;
 					theday++;
 			}
 			console.log(String(identity));
 		}
 		function showdays(month,year){
 			switch(month){
 				case 0:
 				case 2:
 				case 4:
 				case 6:
 				case 7:
 				case 9:
 				case 11:
 					return 31;
 					break;
 				case 3:
 				case 5:
 				case 8:
 				case 9:
 				case 10:
 					return 30;
 					break;
 				case 1:
 					var isleap=(year % 100 === 0) ? (year % 400 === 0) : (year % 4 === 0);
   					if(isleap==false){
   						return 28;
   					}
   					else{
   						return 29;
   					}
 			}
 		}