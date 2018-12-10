$(document).ready(function(){
	$('input[type="checkbox"]').click(function(){
		if(($(this).is(":checked")) && ( $(this).attr('id').match("sw[2-4]") )) { 
			$.ajax({
				url: '/CheckBoxClick',
				data: $(this).attr('id')+"=True",
				type: 'POST',
				success: function(response) {
					console.log(response);
				},
				error: function(error) {
					console.log(error);
				}
			});
		} else if ( $(this).attr('id').match("sw[2-4]") ) {
			$.ajax({
				url: '/CheckBoxClick',
				data: $(this).attr('id')+"=False",
				type: 'POST',
				success: function(response) {
					console.log(response);
				},
				error: function(error) {
					console.log(error);
				}
			});
		}
	});
	
});

