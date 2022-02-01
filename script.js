function speakText(){
  var text = 'Thank you for registering !';
  responsiveVoice.speak(text);
  alert("You are a registered user now!")
}
function speakText2(){
  var text ='Logged in !';
  responsiveVoice.speak(text);
  alert("You are successfully logged into your account!")
}
const api_key=process.env.API_KEY;
var k="muskanthakur26a@gmail.com";
const settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://api.usebouncer.com/v1/email/verify?email="+k,
	"method": "GET",
	"headers": {
		"x-api-key": api_key
	}
};

$.ajax(settings).done(function (response) {
	console.log(response.status);
});
