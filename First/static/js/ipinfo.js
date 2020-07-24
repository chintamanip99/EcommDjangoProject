
    document.getElementById ("reset1").addEventListener ("click", reset1, false);
    document.getElementById ("computenow").addEventListener ("click", computenow, false);
    document.getElementById ("defaultmask").addEventListener ("click", defaultmask, false);
  var ipd=document.getElementById("ipaddresslabel");
    function reset(){


    }
    function reset1(){
      document.getElementById("ipaddress").value="";
    }
    function computenow(){
      var ipaddress=document.getElementById("ipaddress").value;
      var mask=document.getElementById("subnetmask").value;
      // document.getElementById("ipaddresslabel").innerHTML="niceone";
      ipd.innerHTML="kklklk";
      var res=ipaddress.split(".");
      var subnetmask=mask.split(".");

      console.log(("00000000"+parseInt(res[0]).toString(2)).slice(-8));
      console.log(("00000000"+parseInt(res[1]).toString(2)).substr(-8));
      console.log(("00000000"+parseInt(res[2]).toString(2)).substr(-8));
      console.log(("00000000"+parseInt(res[3]).toString(2)).substr(-8));
      ipd.innerHTML=""+("00000000"+parseInt(res[0]).toString(2)).slice(-8)+"."+("00000000"+parseInt(res[1]).toString(2)).substr(-8)+"."+("00000000"+parseInt(res[2]).toString(2)).substr(-8)+"."+("00000000"+parseInt(res[3]).toString(2)).substr(-8);

      //////////////////////////////////////////////////////////////////////////////////////////////
      var bit1=(parseInt(res[0])&parseInt(subnetmask[0]));
      var bit2=(parseInt(res[1])&parseInt(subnetmask[1]));
      var bit3=(parseInt(res[2])&parseInt(subnetmask[2]));
      var bit4=(parseInt(res[3])&parseInt(subnetmask[3]));
      var networkid=""+bit1+"."+bit2+"."+bit3+"."+bit4;
      document.getElementById("networkid").value=""+bit1+"."+bit2+"."+bit3+"."+bit4;

      nl=document.getElementById("networkidlabel");
       nl.innerHTML=""+("00000000"+parseInt(bit1).toString(2)).slice(-8)+"."+("00000000"+parseInt(bit2).toString(2)).substr(-8)+"."+("00000000"+parseInt(bit3).toString(2)).substr(-8)+"."+("00000000"+parseInt(bit4).toString(2)).substr(-8);
       sml=document.getElementById("subnetmasklabel");
        sml.innerHTML=""+("00000000"+parseInt(subnetmask[0]).toString(2)).slice(-8)+"."+("00000000"+parseInt(subnetmask[1]).toString(2)).substr(-8)+"."+("00000000"+parseInt(subnetmask[2]).toString(2)).substr(-8)+"."+("00000000"+parseInt(subnetmask[3]).toString(2)).substr(-8);
////////////////////////////////////////////////////////////////////////////
        var mask0,mask1,mask2,mask3,mask4;
    var ipaddress=document.getElementById("ipaddress").value.split();
    var ipaddress1=parseInt(ipaddress[0]);
    if(ipaddress1>=0 && ipaddress1<=127){
      console.log("A");
      mask0=255;mask1=0;mask2=0;mask3=0;
      document.getElementById("ipaddressclasslabel").innerHTML="A";
    }
    if(ipaddress1>=128 && ipaddress1<=191){
      console.log("B");
      mask0=255;mask1=255;mask2=0;mask3=0;
      document.getElementById("ipaddressclasslabel").innerHTML="B";
    }
    if(ipaddress1>=192 && ipaddress1<=223){
      console.log("C");
      mask0=255;mask1=255;mask2=255;mask3=0;
      document.getElementById("ipaddressclasslabel").innerHTML="C";
    }


    ///////////////////////////////////////////////////////
    var mask0,mask1,mask2,mask3,mask4;
    var ipaddress=document.getElementById("ipaddress").value.split();
    var ipaddress1=parseInt(ipaddress[0]);
    if(ipaddress1>=0 && ipaddress1<=127){
      console.log("A");
      mask0=255;mask1=0;mask2=0;mask3=0;
      document.getElementById("ipaddressclasslabel").innerHTML="A";


//////////////////////////////////////////////////////////////////////////////////////////////
    var mask32=document.getElementById("subnetmask").value;
    var mask322=mask32.split(".");
    var str111="00000000"+parseInt(mask322[1]).toString(2)+"00000000"+parseInt(mask322[2]).toString(2)+"00000000"+parseInt(mask322[3]).toString(2);
    console.log(str111);
      var i=0;
      var counter=0;
      for(i=0;i<str111.length;i++){
        if(str111[i]=="1"){
          counter++;
        }
      }



      console.log(counter);
      var splittednid=networkid.split(".");
      var newendnid=splittednid[0]+"."+"255"+"."+"255"+"."+"255";
      document.getElementById("rangelabel").innerHTML=networkid+" to "+newendnid;
      document.getElementById("networkidlabel123").innerHTML=networkid;
      document.getElementById("broadcastidlabel").innerHTML=splittednid[0]+"."+"255"+"."+"255"+"."+"255";
      document.getElementById("noofhosts").innerHTML=""+Math.pow(2,24-counter)+" per subnetwork";
      document.getElementById("noofsubnetworks").innerHTML=""+Math.pow(2,counter);



    }
    if(ipaddress1>=128 && ipaddress1<=191){
      console.log("B");
      mask0=255;mask1=255;mask2=0;mask3=0;
      document.getElementById("ipaddressclasslabel").innerHTML="B";

      var mask32=document.getElementById("subnetmask").value;
    var mask322=mask32.split(".");

      var str111="00000000"+parseInt(mask322[2]).toString(2)+"00000000"+parseInt(mask322[3]).toString(2);
      var i=0;
      var counter=0;
      for(i=0;i<str111.length;i++){
        if(str111[i]=="1"){
          counter++;
        }
      }



      console.log(counter);
      var splittednid=networkid.split(".");
      var newendnid=splittednid[0]+"."+splittednid[1]+"."+"255"+"."+"255";
      document.getElementById("rangelabel").innerHTML=networkid+" to "+newendnid;
      document.getElementById("networkidlabel123").innerHTML=networkid;
      document.getElementById("broadcastidlabel").innerHTML=splittednid[0]+"."+splittednid[1]+"."+"255"+"."+"255";
      document.getElementById("noofhosts").innerHTML=""+Math.pow(2,16-counter)+" per subnetwork";
      document.getElementById("noofsubnetworks").innerHTML=""+Math.pow(2,counter);


    }
    if(ipaddress1>=192 && ipaddress1<=223){
      console.log("C");
      mask0=255;mask1=255;mask2=255;mask3=0;
      document.getElementById("ipaddressclasslabel").innerHTML="C";
      var str11=parseInt(subnetmask[3]).toString(2);
      var i=0;
      var counter=0;
      for(i=0;i<str11.length;i++){
        if(str11[i]=="1"){
          counter++;
        }
      }
      console.log(counter);
      var splittednid=networkid.split(".");
      var newendnid=splittednid[0]+"."+splittednid[1]+"."+splittednid[2]+"."+"255";
      document.getElementById("rangelabel").innerHTML=networkid+" to "+newendnid;
      document.getElementById("networkidlabel123").innerHTML=networkid;
      document.getElementById("broadcastidlabel").innerHTML=splittednid[0]+"."+splittednid[1]+"."+splittednid[2]+"."+"255";
      document.getElementById("noofhosts").innerHTML=""+Math.pow(2,8-counter)+" per subnetwork";
      document.getElementById("noofsubnetworks").innerHTML=""+Math.pow(2,counter);
    }

    }
    function dec2bin(dec){
      var res = str.split(".");
      return (dec >>> 0).toString(2);
  }
  function defaultmask(){
    var mask0,mask1,mask2,mask3,mask4;
    var ipaddress=document.getElementById("ipaddress").value.split();
    var ipaddress1=parseInt(ipaddress[0]);
    if(ipaddress1>=0 && ipaddress1<=127){
      console.log("A");
      mask0=255;mask1=0;mask2=0;mask3=0;
      document.getElementById("ipaddressclasslabel").innerHTML="A";
    }
    if(ipaddress1>=128 && ipaddress1<=191){
      console.log("B");
      mask0=255;mask1=255;mask2=0;mask3=0;
      document.getElementById("ipaddressclasslabel").innerHTML="B";
    }
    if(ipaddress1>=192 && ipaddress1<=223){
      console.log("C");
      mask0=255;mask1=255;mask2=255;mask3=0;
      document.getElementById("ipaddressclasslabel").innerHTML="C";
    }
    document.getElementById("subnetmask").value=""+mask0+"."+mask1+"."+mask2+"."+mask3;
  }
  