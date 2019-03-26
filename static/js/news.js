function getDate() {
              var event = new Date();
              var current_date=event.toDateString();
              var current_time=event.toLocaleTimeString('en-US');
              document.getElementById('date').innerText=current_date+ " | "+"UPDATED"+" "+current_time ;
        }