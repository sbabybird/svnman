$(document).ready(function() {
		$('#Query').click(function() {
			$('#display').hide();
			//$('#display').html($('#txtUserName').val());
			$.get('/getsvninfo', 'info='+$('#txtUserName').val()+':'+$('#txtPassword').val(), function(data, textStatus){
				$('#display').html(data.toString());
				$('#display').show('slow');
				});
			$('#display').show('slow');
			});
		});

