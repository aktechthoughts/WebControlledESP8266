$(document).ready(function() {
	 var socket = io.connect('http://' + document.domain + ':' + location.port);
	 
	 socket.on('mqtt_message', function(data) {
		 console.log(data);
		 if ( data['topic'] == 'AnalogValue'){
			  val = data['payload'].split('=')[1]
			  $("#dial2").val(val).trigger("change");	
		 }
	 })

	 $('input[type="checkbox"]').click(function(){
		if(($(this).is(":checked")) && ( $(this).attr('id').match("sw1") )) { 

			 var topic = 'AnalogValue';
			 var qos = 2
			 var data = '{"topic": "' + topic + '", "qos": ' + qos + '}';
			 socket.emit('subscribe', data=data);
			 
		} else if ( $(this).attr('id').match("sw1") ) {
			socket.emit('unsubscribe_all');
		}
	});
});

