<input type = "text" class="form-control" onblur='getVal()" id="number" name = "emailbody">
<input type = "text" class="form-control" onblur='getVal()" id="number" name = "subject">
<button type="submit" >submit</button>


function predict(){
  
  var subject= documnet.getElementById('Subject).value;
  var emailbody = documnet.getElementById('emailbody).value;
  console.log(number)
  alert(number)
  ver serverData = {
    'subject':subject,
    "body";emailbody
  }
  
  $ajax({
  url:'/ticketnum',
  method :"POST",
  contentType:'application/json',
  dataType:json,
  success. function(response){
  documnet.getElementById('Email').value = response['Email'];
  documnet.getElementById('mobile').value = response['mobile'];
  documnet.getElementById('address').value = response['address'];
  }
  });
  }
  
  
  
  
  data = request.get_json(silent=True,force=True)
  data
