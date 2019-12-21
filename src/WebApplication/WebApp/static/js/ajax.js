var safe_icon= "<img src=\"/static/img/checks.png\" alt=\"safe\" width=\"20px\" height=\"20px\" >";
var warning_icon= "<img src=\"/static/img/warning.png\" alt=\"safe\" width=\"20px\" height=\"20px\" >";
var x_icon= "<img src=\"/static/img/x.png\" alt=\"safe\" width=\"20px\" height=\"20px\" >";

        $.ajaxSetup({
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
        });

        $(document).ready(function() {

          $.get("/startprocess/", function(data) {
                 console.log("alldone");
            });
            $.get("/ajax_SC/", function(data) {           
                $('#SC_title').append(" (finished >///< )");
                for (var i in data) {

                 
                  if(i=="miningType"){
                    if (data['isMining']=="True"){
                       document.getElementById("SC_"+i+"_icon").innerHTML = warning_icon;
                        document.getElementById('SC_'+i).innerHTML =data[i];
                    }
                    else{
                       document.getElementById("SC_"+i+"_icon").innerHTML = safe_icon;
                        document.getElementById('SC_'+i).innerHTML = "no mining~";
                    }
                  }
                  else if (i=="hasHardwareAccess"){
                    
                    var empty=true;
                    for (var j in data[i]){
                      console.log("hasHardwareAccess")
                        empty=false;
                        $('#SC_hasHardwareAccess').append("<br>" + j + " : " + data[i][j] );
                    }
                    if (empty==false){
                        document.getElementById("SC_"+i+"_icon").innerHTML = warning_icon;
                    }
                    else{
                      document.getElementById("SC_"+i+"_icon").innerHTML = safe_icon;
                      document.getElementById('SC_'+i).innerHTML = "no hasHardwareAcess ~";
                    }
                    
                  }
                  else {
                    if (data[i]=="True")
                      document.getElementById("SC_"+i+"_icon").innerHTML = warning_icon;
                    else if(data[i]=="False")
                      document.getElementById("SC_"+i+"_icon").innerHTML = safe_icon;

                    document.getElementById('SC_'+i).innerHTML =data[i];
                  }
               
                }
            });
            $.get("/ajax_BL/", function(data) {
             $('#BL_title').append(" (finished >///< )");
              for (var i in data) {
                if (data[i]=="safe URL")
                  document.getElementById("BL_"+i+"_icon").innerHTML = safe_icon;
                else 
                  document.getElementById("BL_"+i+"_icon").innerHTML = warning_icon;
                 document.getElementById('BL_'+i).innerHTML =data[i];
              
              }
        
            });
           $.get("/ajax_BS/", function(data) {
               $('#BS_title').append(" (finished >///< )");

              for (var i in data) {
                if (i=="viewfilename"){
                  document.getElementById("BS_"+i+"_icon").innerHTML = safe_icon;
                  var IMG = "<img src=\"/static/img/screenshot/"+data[i]+"\" alt=\""+data[i]+"\" width=\"500px\" height=\"300px\" >"; 
                  console.log(IMG);
                  console.log(safe_icon);
                  
                  document.getElementById('BS_'+i).innerHTML = IMG;
               
               
                }
                else if (i=="mem"){
                  if (data[i]>1500)
                    document.getElementById("BS_"+i+"_icon").innerHTML = warning_icon;
                  else
                    document.getElementById("BS_"+i+"_icon").innerHTML = safe_icon;
                  document.getElementById('BS_'+i).innerHTML =data[i] + " KB" ;
                }
                else if (i=="cpu"){
                  if (data[i]>50)
                    document.getElementById("BS_"+i+"_icon").innerHTML = warning_icon;
                  else
                    document.getElementById("BS_"+i+"_icon").innerHTML = safe_icon;

                    document.getElementById('BS_'+i).innerHTML =data[i] + " %";
                }
                
              }
                    
            });
});