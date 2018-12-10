$(document).ready(function(){
	var currentValue = null;

    $(".dial").knob({
        'change': function (v) {
			 $("#dial2").val(v).trigger("change");
		}
    });
    $('.dial').trigger('configure', {
        "min": 1,
            "max": 255,
            "fgColor": "#FF0000",
            "skin": "tron",
            "cursor": true,
            "step": 1
    });

	$(".infinite").knob({
		"change" : function (v) { 

		} 
		});

});


